import copy
from typing import Any, Dict

from .base import (
    LLMClient,
    LLMClientResponse,
    LLMResponseMessage,
    LLMResponseChoice,
    LLMResponseMessageToolCall,
    LLMResponseMessageToolCallFunction,
    LLMResponseUsage
)

# 检查是否安装 OpenAI 的 Python SDK
try:
    import openai
    from openai.types.chat.chat_completion import ChatCompletion
except ImportError or ModuleNotFoundError:
    raise ImportError("请安装 OpenAI 的 Python SDK：`pip install openai`")

from core.logger.runtime import get_logger

logger = get_logger(name=__name__)


class OpenAIClient(LLMClient):
    BASE_URL = "https://api.openai.com/v1"

    def __init__(self, llm_config: Dict[str, Any], **kwargs):
        super().__init__(llm_config, **kwargs)
        self._openai_client = openai.Client(
            api_key=self._api_key,
            base_url=self._base_url,
            timeout=self._timeout
        )

    def _construct_create_params(self, messages, **kwargs) -> Dict[str, Any]:
        """构造生成对话回复的参数"""
        allow_keys = [
            "max_tokens",
            "frequency_penalty",
            "presence_penalty",
            "stop",
            "temperature",
            "top_p",
            "tools",
            "tool_choice"
        ]
        params = copy.deepcopy(self._generate_config)

        global_context = kwargs.get("context", {})
        # 请求消息
        params["messages"] = [
            self._construct_message(global_context, **message)
            for message in messages
        ]
        # 其他请求参数
        self._merge_params(kwargs, params, allow_keys)

        return params

    def do_create(self, **params) -> ChatCompletion:
        """生成对话回复"""

        # 目前不允许使用流式结果
        params["stream"] = False
        try:
            response = self._openai_client.chat.completions.create(
                model=self._model,
                **params
            )
            logger.debug(f"LLM 调用成功: {response}, 请求参数: {params}")
        except Exception as e:
            logger.error(f"LLM 调用失败: {e}, 请求参数: {params}")
            raise e

        return response

    def get_usage(self, response: LLMClientResponse) -> Dict[str, Any]:
        """获取token使用情况"""
        raise NotImplementedError

    def _construct_response(self, response: ChatCompletion, **kwargs) -> LLMClientResponse:
        """构造响应"""
        usage = LLMResponseUsage(
            prompt_tokens=response.usage.prompt_tokens,
            completion_tokens=response.usage.completion_tokens,
            total_tokens=response.usage.total_tokens
        )
        choices = [
            LLMResponseChoice(
                message=LLMResponseMessage(
                    content=choice.message.content,
                    role=choice.message.role,
                    tool_calls=[
                        LLMResponseMessageToolCall(
                            id=tool_call.id,
                            type=tool_call.type,
                            function=LLMResponseMessageToolCallFunction(
                                name=tool_call.function.name,
                                arguments=tool_call.function.arguments
                            )
                        )
                        for tool_call in choice.message.tool_calls
                    ] if choice.message.tool_calls else None
                )
            )
            for choice in response.choices
        ]
        return LLMClientResponse(
            choices=choices,
            model=response.model,
            usage=usage
        )
