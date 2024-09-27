import copy
import json
import re
import uuid
from typing import Any, Dict, List, Callable

import httpx
from tenacity import retry, stop_after_attempt, retry_if_exception, RetryError, wait_exponential

from .base import (
    LLMClient,
    LLMClientResponse,
    LLMResponseMessage,
    LLMResponseChoice,
    LLMResponseMessageToolCall,
    LLMResponseMessageToolCallFunction,
    LLMResponseUsage
)
from core.logger.runtime import get_logger

logger = get_logger(name=__name__)

CHINESE_CHAR_RE = re.compile(r"[\u4e00-\u9fff]")


def has_chinese_chars(data: Any) -> bool:
    text = str(data)
    return bool(CHINESE_CHAR_RE.search(text))


class BasicLLMClient(LLMClient):
    """基础的大语言模型客户端，兼容 OpenAI 接口

    为不支持工具调用的大语言模型提供工具调用的支持
    """

    BASE_URL = "https://api.openai.com/v1"

    CHAT_COMPLETION_ENDPOINT = "/chat/completions"
    TOOL_CALL_PATTERN = re.compile(r"<FUNCTION><FUNCNAME>(.*?)</FUNCNAME><FUNCARGS>(.*?)</FUNCARGS></FUNCTION>")
    # 为了实现工具调用的系统提示词
    DEFAULT_SYSTEM_MESSAGE_EN = "You are a helpful assistant."
    DEFAULT_TOOL_CALL_SYSTEM_MESSAGE_ZH = """# 工具
    
## 你拥有如下工具：
{% for __a2x_inner_tool in __a2x_inner_tools %}
### {{ __a2x_inner_tool.name }}

函数描述：{{ __a2x_inner_tool.description }}
函数参数描述：{{ __a2x_inner_tool.parameters }}

{% endfor %}
## 函数名和函数参数字典分别由XML标签<FUNCNAME>和<FUNCARGS>包裹，每个函数调用由XML标签<FUNCTION>包裹。
## 你可以在回复中插入零次、一次或多次以下命令以调用工具：

<FUNCTION><FUNCNAME>工具名称，必须是{{ __a2x_inner_tool_names }}之一。</FUNCNAME><FUNCARGS>工具输入，必须是一个字典，其中键是参数名，值为参数值。</FUNCARGS></FUNCTION>
"""

    DEFAULT_TOOL_CALL_SYSTEM_MESSAGE_EN = """# Tools
    
## You have access to the following tools:
{% for __a2x_inner_tool in __a2x_inner_tools %}
### {{ __a2x_inner_tool.name }}

Function Description: {{ __a2x_inner_tool.description }}
Function Parameters Description：{{ __a2x_inner_tool.parameters }}

{% endfor %}
## When you need to call a tool, please insert the following command in your reply, which can be called zero or multiple times according to your needs:

<FUNCTION><FUNCNAME>The tool to use, should be one of {{ __a2x_inner_tool_names }}.</FUNCNAME><FUNCARGS>The input of the tool，It must be a dictionary where the key is the parameter name and the value is the parameter value.</FUNCARGS></FUNCTION>
"""

    def __init__(self, llm_config: Dict[str, Any], **kwargs):
        super().__init__(llm_config, **kwargs)
        self._max_retries = kwargs.get("max_retries", 3)

        self._request_fn = self.__build_request_fn()

    def build_client(self):
        return httpx.Client(
            headers={"Authorization": f"Bearer {self._api_key}"},
            base_url=self._base_url,
            timeout=self._timeout,
        )

    def _preprocess_tool_call(self, messages: List[Dict[str, Any]], tools: List[Dict[str, Any]]) -> List[
        Dict[str, Any]]:
        """预处理工具调用

        添加工具调用消息

        Args:
            messages : 消息列表
            tools: 工具列表
                - type: 类型
                - function: 函数
                    - name: 函数名
                    - parameters: 参数
                    - description: 描述
        """
        if not tools:
            return messages
        __a2x_inner_tools = [tool["function"] for tool in tools]
        __a2x_inner_tool_names = [tool["name"] for tool in __a2x_inner_tools]
        context = {
            "__a2x_inner_tools": __a2x_inner_tools,
            "__a2x_inner_tool_names": __a2x_inner_tool_names
        }
        if not messages:
            return messages
        if len(messages) >= 1 and messages[0].get("role") != "system":
            # 且非系统消息, 默认为英文提示词
            messages.insert(0, {
                "role": "system",
                "content": self.DEFAULT_SYSTEM_MESSAGE_EN + self.DEFAULT_TOOL_CALL_SYSTEM_MESSAGE_EN,
                "context": context
            })
            return messages
        # 有系统消息，则根据系统消息的语言类型选择提示词，并插入
        assert messages[0]["role"] == "system", "第一条消息必须为系统消息"
        if has_chinese_chars(messages[0]["content"]):
            messages[0]["content"] += self.DEFAULT_TOOL_CALL_SYSTEM_MESSAGE_ZH
        else:
            messages[0]["content"] += self.DEFAULT_TOOL_CALL_SYSTEM_MESSAGE_EN

        if "context" in messages[0]:
            messages[0]["context"].update(context)
        else:
            messages[0]["context"] = context

        return messages

    def _postprocess_tool_call(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """后处理工具调用

        Args:
            message: 消息
        """
        assert message["role"] == "assistant", "消息必须为模型消息"
        # 提取工具调用
        tool_calls = []
        tool_call_matches = self.TOOL_CALL_PATTERN.findall(message["content"])
        if not tool_call_matches:
            return message
        for tool_call in tool_call_matches:
            tool_name, tool_args = tool_call
            tool_calls.append({
                "id": "cu-" + str(uuid.uuid4().hex),
                "type": "function",
                "function": {
                    "name": tool_name,
                    "arguments": json.loads(tool_args)
                }
            })
        message["tool_calls"] = tool_calls
        message["content"] = None
        return message

    def _construct_create_params(self, messages, **kwargs) -> Dict[str, Any]:
        """构造生成对话回复的参数"""
        allow_keys = [
            "max_tokens",
            "frequency_penalty",
            "presence_penalty",
            "stop",
            "temperature",
            "top_p",
        ]
        params = copy.deepcopy(self._generate_config)

        global_context = kwargs.get("context", {})
        messages = self._preprocess_tool_call(messages, kwargs.get("tools", []))
        # 请求消息
        params["messages"] = [
            self._construct_message(global_context, **message)
            for message in messages
        ]
        # 其他请求参数
        self._merge_params(kwargs, params, allow_keys)

        return params

    def do_create(self, **params) -> Dict[str, Any]:
        """生成对话回复"""

        # 目前不允许使用流式结果
        params["stream"] = False
        params["model"] = self._model
        try:
            response = self._request_fn(url=self.CHAT_COMPLETION_ENDPOINT, json=params)
            logger.debug(f"LLM 调用成功: {response}, 请求参数: {params}")
        except RetryError as er:
            logger.error(f"LLM 调用失败: {er.last_attempt.exception()}, 请求参数: {params}")
            raise er.last_attempt.exception()
        except Exception as e:
            logger.error(f"LLM 调用失败: {e}, 请求参数: {params}")
            raise e

        return response

    def __build_request_fn(self) -> Callable[..., Dict[str, Any]]:
        """构建请求函数

        TODO: 抽象成通用高阶函数，生成可重试的函数
        """

        def __retry_if_exception_type(exception: BaseException) -> bool:
            """是否重试"""
            return isinstance(exception, (httpx.HTTPStatusError, httpx.TimeoutException, httpx.NetworkError))

        @retry(stop=stop_after_attempt(self._max_retries), wait=wait_exponential(multiplier=1, max=10),
               retry=retry_if_exception(__retry_if_exception_type))
        def __inner_request_fn(**params) -> Dict[str, Any]:
            with self.build_client() as client:
                response = client.post(**params)
                response.raise_for_status()
                response = response.json()
            return response

        return __inner_request_fn

    def get_usage(self, response: LLMClientResponse | Dict[str, Any]) -> LLMResponseUsage | None:
        """获取token使用情况"""
        if isinstance(response, LLMClientResponse):
            return response.usage

        if "usage" in response:
            return LLMResponseUsage(
                prompt_tokens=response["usage"]["prompt_tokens"],
                completion_tokens=response["usage"]["completion_tokens"],
                total_tokens=response["usage"]["total_tokens"]
            )
        return None

    def _construct_response(self, response: Dict[str, Any]) -> LLMClientResponse:
        """构造响应"""

        response["choices"][-1]["message"] = self._postprocess_tool_call(response["choices"][-1]["message"])

        choices = [
            LLMResponseChoice(
                message=LLMResponseMessage(
                    content=choice["message"]["content"],
                    role=choice["message"]["role"],
                    tool_calls=[
                        LLMResponseMessageToolCall(
                            id=tool_call["id"],
                            type=tool_call["type"],
                            function=LLMResponseMessageToolCallFunction(
                                name=tool_call["function"]["name"],
                                arguments=tool_call["function"]["arguments"]
                            )
                        )
                        for tool_call in choice["message"]["tool_calls"]
                    ] if "tool_calls" in choice["message"] else None
                )
            )
            for choice in response["choices"]
        ]
        return LLMClientResponse(
            choices=choices,
            model=response["model"],
            usage=self.get_usage(response)
        )


if __name__ == '__main__':
    llm_config = {
        "api_key": "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",
        "model": "gpt-3.5-turbo",
        "generate_config": {
            "temperature": 0.7,
        }
    }
    openai_client = BasicLLMClient(llm_config)
    messages = [
        {"content": "你是一个乐于助人的助手。", "role": "system"},
        {"content": "你好，我是小红", "role": "assistant"},
        {"content": "你好，我是小明, 请你使用xml标签调用工具 tool1", "role": "user"}
    ]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "tool1",
                "parameters": {
                    "param1": "参数1"
                },
                "description": "This is a tool，just for test"
            }
        }
    ]
    response = openai_client.create(messages, tools=tools)
    print(response)
