from typing import List, Any, Dict, Union, Callable, Literal, Optional

import shortuuid
from core.llms import LLMFactory
from core.llms.base import Tool
from core.config.schema import Config
from core.utils.function_utils import get_function_schema
from core.config.config_loader import ConfigLoader
from core.prompt.prompt_loader import PromptLoader
from core.llms.base import LLMClient


class LLMAgent:
    """基于大语言模型的智能体
    Attributes:
        name: 智能体的名称
        description: 智能体的描述

    Args:
        name (str): 智能体的名称
        llm_client (LLMClient): 大语言模型客户端
        description (str): 智能体的描述
    """

    agent_role = "base"
    agent_description = """功能强大且高效的AI助手，具备与外部工具、API 和插件交互的强大能力。它擅长使用预定义的函数和工具完成编码任务，同时还能通过检索信息或在需要时执行命令，高效处理各种常规任务。"""

    def __init__(
            self,
            llm_client: LLMClient,
            name: str = f"{agent_role}-{shortuuid.uuid()}",
            description: str = agent_description
    ):
        # 智能体的基本属性
        self.name = name
        self.description = description
        # 大语言模型客户端
        self._llm_client = llm_client
        # 对话记录：{sender: [message1, message2, ...]}
        self._chat_messages = {}
        # 工具
        self._tools: List[Tool] = []
        self._tool_map: Dict[str, Callable] = {}
        # 回复钩子
        self._reply_hooks = []

        self._system_message = PromptLoader.get_prompt(
            f"{self.agent_role}/system.prompt"
        )

    @property
    def role(self):
        """智能体的角色/类型"""
        return self.agent_role

    @property
    def system_message(self) -> str:
        """系统提示词"""
        return self._system_message

    @property
    def chat_messages(self) -> Dict["LLMAgent", List[Dict[str, Any]]]:
        """对话记录"""
        return self._chat_messages

    @property
    def tools(self):
        """工具"""
        return self._tools

    def receive(
        self,
        messages: Union[str, Dict[str, Any], List[Dict[str, Any]]],
        sender: Union[str, "LLMAgent"] = "__temp__",
        remember: bool = True,
        **kwargs
    ) -> Union[str, Dict[str, Any], None]:
        """智能体感知外界信息

        Args:
            messages (str | list| dict): 外界信息
            sender (str | Agent): 信息发送者, 默认为临时发送者
            remember (bool): 是否记住对话记录
            **kwargs: 其他参数

        Returns:
            str | dict | None: 智能体的响应 | None
        """
        if isinstance(messages, str):
            messages = [{
                "role": "assistant" if sender and isinstance(sender, LLMAgent) else "user",
                "content": messages
            }]
        elif isinstance(messages, dict):
            messages = [messages]

        if kwargs.get("remember", True):
            if sender not in self._chat_messages:
                self._chat_messages[sender] = messages
            else:
                self._chat_messages[sender].extend(messages)
        #
        return self.execute(messages, sender, **kwargs)

    def generate_reply(self, messages: Union[str, List[Dict[str, Any]]], sender: Union[str, "LLMAgent"], **kwargs):
        """生成大模型回复"""
        # 格式化消息
        if isinstance(messages, str):
            messages = [
                {"role": "user", "content": messages}
            ]


    def generate_llm_reply(self, messages: Union[str, List[Dict[str, Any]]], sender: Union[str, "LLMAgent"], **kwargs):
        """生成大模型回复"""
        ...

    def generate_tool_reply(self, messages: Union[str, List[Dict[str, Any]]], sender: Union[str, "LLMAgent"], **kwargs):
        """生成工具回复"""
        ...


    def execute(self, messages: Union[str, Dict[str, Any], List[Dict[str, Any]]], sender: Union[str, "LLMAgent"],
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
                "role": "assistant" if sender and isinstance(sender, LLMAgent) else "user",
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
        response = self._llm_client.create(all_messages, tools=self._tools, **kwargs)
        return response.choices[0].message.content

    def register_tool(self, function: Callable[..., Any], *, name: Optional[str] = None, description: Optional[str] = None,
                      type: Literal["function"] = "function") -> None:
        """注册工具

        Args:
            function (Callable): 工具
            name (str): 工具名称
            description (str): 工具描述
            type: 工具类型
        """
        if type == "function":
            tool_desc = get_function_schema(function, name=name, description=description)
            tool = Tool(**tool_desc)
            self._tools.append(tool)
            self._tool_map[tool.function.name] = function
        else:
            raise ValueError(f"不支持的工具类型：{type}")

    def __repr__(self) -> str:
        return f"<LLMAgent name={self.name} description={self.description}>"
