import copy
from abc import ABC
from typing import Dict, Any, Optional, List, Literal

from pydantic import BaseModel, Field

import jinja2


# class LLMConfig(BaseModel):
#     class GenerateConfig(BaseModel):
#         max_tokens: Optional[int]
#         temperature: Optional[float]
#         top_k: Optional[int]
#         top_p: Optional[float]
#         frequency_penalty: Optional[float]
#         presence_penalty: Optional[float]
#         stop: Optional[str]
#
#     provider: Optional[str]
#     base_url: str
#     api_key: str
#     generate_config: Optional[GenerateConfig, Dict[str, Any]]

class ToolFunction(BaseModel):
    name: str = Field(description="函数名称")
    description: str = Field(description="函数描述")
    parameters: Dict[str, Any] = Field(description="函数参数")
    required: List[str] = Field(description="必填参数")


class Tool(BaseModel):
    """工具"""

    type: Literal["function"] = "function"
    function: ToolFunction


class LLMResponseMessageToolCallFunction(BaseModel):
    name: str
    arguments: Dict[str, Any] | str


class LLMResponseMessageToolCall(BaseModel):
    """工具调用"""

    id: str
    type: str
    function: LLMResponseMessageToolCallFunction


class LLMResponseMessage(BaseModel):
    content: Optional[str]
    role: str
    tool_calls: Optional[List[LLMResponseMessageToolCall]]


class LLMResponseChoice(BaseModel):
    message: LLMResponseMessage


class LLMResponseUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class LLMClientResponse(BaseModel):
    """大语言模型客户端响应"""

    choices: List[LLMResponseChoice]
    model: str
    usage: Optional[LLMResponseUsage]


class LLMClient(ABC):
    """大语言模型客户端

    Attributes:
        BASE_URL (str): 请求基础URL
        DEFAULT_TIMEOUT_SECONDS (int): 默认超时时间

    """

    BASE_URL: str = None

    # 默认超时时间 300s
    DEFAULT_TIMEOUT_SECONDS: int = 300

    DEFAULT_JSON_SCHEMA_PROMPT = """你的回答必须符合以下JSON Schema：\n\n```json\n{json_schema}\n```\n\n你绝不能在你的JSON回答中添加任何额外字段，也绝不能添加类似“这是你的JSON”这样的额外前言。"""

    def __init__(self, llm_config: Dict[str, Any], **kwargs):
        """
        Args:
            llm_config (dict): 大模型配置
                - provider: 大模型服务提供商
                - base_url (str): 请求基础URL
                - api_key (str): API KEY
                - temperature (float): 温度
                - model (str): 模型
                - timeout (int): 超时时间(s)
                - generate_config (dict): 生成配置

            kwargs: 暂定

        """
        llm_config = copy.deepcopy(llm_config)
        # 请求基础URL
        if "base_url" not in llm_config and self.BASE_URL is None:
            raise ValueError(f"`base_url` 必须在 config 或 {self.__class__.__name__} 类中指定")
        self._base_url = llm_config.get("base_url", self.BASE_URL)

        # API KEY
        if "api_key" not in llm_config:
            raise ValueError("`api_key` 必须在 config 中指定")
        self._api_key = llm_config.get("api_key")

        # 模型
        if "model" not in llm_config:
            raise ValueError("`model` 必须在 config 中指定")
        self._model = llm_config.get("model")
        # 超时时间
        self._timeout = llm_config.get("timeout", self.DEFAULT_TIMEOUT_SECONDS)
        # 生成配置
        self._generate_config = llm_config.get("generate_config", {})

    def create(self, messages: List[Dict[str, Any]], **kwargs) -> LLMClientResponse:
        """生成对话回复"""
        # 是否输出JSON格式，并转为JSON对象
        model_schema = kwargs.get("model_schema", None)
        if model_schema and issubclass(model_schema, (BaseModel,)):
            messages = self._append_json_schema_message(messages, model=model_schema)
        params = self._construct_create_params(messages, **kwargs)
        response = self.do_create(**params)
        response = self._construct_response(response, **kwargs)

        return response

    def do_create(self, **params) -> LLMClientResponse:
        """生成对话回复"""
        raise NotImplementedError

    def get_usage(self, response: LLMClientResponse) -> Dict[str, Any]:
        """获取token使用情况"""
        raise NotImplementedError

    def _construct_create_params(self, messages: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """构造生成对话回复的参数

        优先采用传入的参数，其次采用初始化时的参数
        """
        raise NotImplementedError

    @classmethod
    def _append_json_schema_message(cls, messages: List[Dict[str, Any]], model: BaseModel,
                                    default_prompt: str = DEFAULT_JSON_SCHEMA_PROMPT) -> List[Dict[str, Any]]:
        json_schema_prompt = default_prompt.format(json_schema=model.model_json_schema())
        messages[-1]["content"] += "\n\n" + json_schema_prompt
        # messages.append({"content": json_schema_prompt, "role": "user"})
        return messages

    @classmethod
    def _generate_model_from_json(cls, response: LLMClientResponse, model: BaseModel) -> BaseModel | None:
        content = response.choices[0].message.content
        if content:
            content = content.strip("```")
            model_ins = model.model_validate(content)
            return model_ins
        else:
            return None

    @classmethod
    def _construct_message(cls, global_context: Dict[str, Any], content: str, **kwargs) -> Dict[str, Any]:
        """构造消息, 支持 jinja2 模板渲染

        Args:
            global_context (dict): 全局上下文
            content (str): 内容
        """
        allow_keys = ["content", "role", "name", "tool_calls"]
        message = {}
        context = kwargs.get("context", {})
        global_context = copy.deepcopy(global_context)
        global_context.update(context)
        for key in kwargs:
            if key in allow_keys:
                message[key] = kwargs[key]
        if global_context is None:
            message["content"] = content
        else:
            message["content"] = jinja2.Template(content).render(global_context)
        return message

    @classmethod
    def _merge_params(cls, origin: Dict[str, Any], params: Dict[str, Any], allow_keys: List[str]) -> None:
        """合并参数"""
        for key in allow_keys:
            if key in origin:
                params[key] = origin[key]

    def _construct_response(self, response, **kwargs) -> LLMClientResponse:
        """构造响应"""
        raise NotImplementedError
