from typing import List, Any, Dict, Union, Callable, Literal, Optional

from .base import Agent
from core.llms import LLMFactory
from core.config.schema import Config
from core.utils.function_utils import get_function_schema


class LLMAgent:
    """基于大语言模型的智能体

    """

    __agent_name__ = ""

    def __init__(self, name: str, description: str, config: Config, system_message: str = None):
        """
        Args:
            name (str): 智能体的名称
            description (str): 智能体的描述
            system_message (str): 系统提示词
            config (dict): 配置
                - client: 客户端
                - llm_config: 大语言模型配置
        """
        # 智能体的基本属性
        self._name = name
        self._description = description
        # 大模型相关配置
        self._system_message = system_message
        if "client" not in config and "llm_config" not in config:
            raise ValueError("`client` 或 `llm_config` 必须在 config 中指定")

        # 对话记录：{sender: [message1, message2, ...]}
        self._chat_messages = {}
        # 工具
        self._tools = []
        self._tool_map = {}

        self._client = LLMFactory.create_llm_from_config(config["llm_config"])

    @property
    def name(self) -> str:
        """智能体的名称"""
        return self._name

    @property
    def description(self) -> str:
        """智能体的描述"""
        return self._description

    @property
    def system_message(self) -> str:
        """系统提示词"""
        return self._system_message

    def update_system_message(self, system_message: str) -> None:
        """更新系统提示词

        Args:
            system_message (str): 系统提示词
        """
        self._system_message = system_message

    def receive(self, messages: Union[str, Dict[str, Any], List[Dict[str, Any]]], sender: Union[str, "Agent"],
                is_execute: bool = False, **kwargs) -> Union[str, Dict[str, Any], None]:
        """智能体感知外界信息

        Args:
            messages (str | list| dict): 外界信息
            sender (str | Agent): 信息发送者
            is_execute (bool): 接收外界信息后是否做出响应
            **kwargs: 其他参数

        Returns:
            str | dict | None: 智能体的响应 | None
        """
        if isinstance(messages, str):
            messages = [{
                "role": "assistant" if sender and isinstance(sender, Agent) else "user",
                "content": messages
            }]
        elif isinstance(messages, dict):
            messages = [messages]

        if kwargs.get("remember", True):
            if sender not in self._chat_messages:
                self._chat_messages[sender] = messages
            else:
                self._chat_messages[sender].extend(messages)
        if is_execute:
            return self.execute(self._chat_messages[sender], sender, **kwargs)

    def execute(self, messages: Union[str, Dict[str, Any], List[Dict[str, Any]]], sender: Union[str, "Agent"],
                **kwargs) -> Union[str, Dict[str, Any], None]:
        """智能体对外界感知做出响应

        Args:
            messages (str, dict, list): 外界信息
            sender (str | Agent): 信息发送者
            **kwargs: 其他参数
        """
        # 构建消息
        all_messages = []
        if isinstance(messages, str):
            messages = [{
                "role": "assistant" if sender and isinstance(sender, Agent) else "user",
                "content": messages
            }]
        elif isinstance(messages, dict):
            messages = [messages]
        if sender and sender in self._chat_messages:
            all_messages.extend(self._chat_messages[sender])

        all_messages.extend(messages)
        # 系统提示词
        if all_messages[0].get("role") != "system":
            all_messages.insert(0, {
                "role": "system",
                "content": self.system_message
            })
        response = self._client.create(all_messages, tools=self._tools, **kwargs)
        return response

    def register_tool(self, tool: Callable[..., Any], *, name: Optional[str] = None, description: Optional[str] = None,
                      type: Literal["function"] = "function") -> None:
        """注册工具

        Args:
            tool (Callable): 工具
            name (str): 工具名称
            description (str): 工具描述
            type: 工具类型
        """
        if type == "function":
            tool_desc = get_function_schema(tool, name=name, description=description)
            self._tools.append(tool_desc)
            self._tool_map[tool_desc["function"]["name"]] = tool
        else:
            raise ValueError(f"不支持的工具类型：{type}")