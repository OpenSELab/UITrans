from typing import List, Any, Dict, Union, Callable, Literal, Optional

from .base import Agent
from core.llms import LLMFactory
from core.config.schema import Config
from core.utils.function_utils import get_function_schema
from core.config.config_loader import ConfigLoader
from core.prompt.prompt_loader import PromptLoader
from ..llms.base import LLMClient


class LLMAgent:
    """基于大语言模型的智能体

    Args:
        name (str): 智能体的名称
        llm_client (LLMClient): 大语言模型客户端
        description (str): 智能体的描述
    """

    agent_role = "base"
    agent_description = """功能强大且高效的AI助手，具备与外部工具、API 和插件交互的强大能力。它擅长使用预定义的函数和工具完成编码任务，同时还能通过检索信息或在需要时执行命令，高效处理各种常规任务。"""
    default_system_message = """你是一个功能强大且高效的AI助手，具备与外部工具、API和插件交互的能力，可以收集信息、执行操作或提升任务处理效果。
对于编码任务：
- 使用提供给你的预定义函数和工具。不要在没有这些工具的情况下生成或猜测代码。
- 如果缺乏完成任务所需的信息，请使用适当的工具请求额外的资源或函数。

对于一般任务：
- 始终努力简洁、准确并节约资源。
- 如果外部工具或API能够帮助解决任务（例如检索信息、创建文件或执行命令），请按需调用它们。
- 当任务完成时，如果不需要进一步的操作，请在回答的末尾添加“TERMINATE”。
    """

    def __init__(
            self,
            name: str,
            llm_client: LLMClient,
            description: str = agent_description
    ):
        # 智能体的基本属性
        self._name = name
        self._description = description
        # 大语言模型客户端
        self._llm_client = llm_client
        # 对话记录：{sender: [message1, message2, ...]}
        self._chat_messages = {}
        # 工具
        self._tools = []
        self._tool_map = {}

        self._system_message = PromptLoader.get_prompt(
            f"{self.agent_role}/system.prompt"
        )

    @property
    def role(self):
        """智能体的角色/类型"""
        return self.agent_role

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
