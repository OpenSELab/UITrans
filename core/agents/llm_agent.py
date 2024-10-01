import json
import logging
from collections import defaultdict
from typing import List, Any, Dict, Union, Callable, Literal, Optional, Protocol

import shortuuid
from core.logger.base_logger import BaseLogger
from core.logger.runtime import get_logger
from core.utils.function_utils import get_function_schema
from core.prompt.prompt_loader import PromptLoader
from core.llms.base import Tool, LLMClient
from core.agents.schema import AgentTasks


logger = get_logger(name="LLM Agent")

ReplyHookFunction = Callable[
    [
        List[Dict[str, Any]],  # messages
        Union[str, "LLMAgent"],  # sender
        Dict[str, Any]  # kwargs
    ],
    Dict[str, Any]
]
Sender = Union[str, "LLMAgent"]


def default_terminate_trigger(message_content: str) -> bool:
    """默认终止触发器"""
    if not message_content.strip():
        return True
    if message_content.endswith("TERMINATE"):
        return True
    return False


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
            description: str = agent_description,
            logger: BaseLogger | logging.Logger = logger
    ):
        # 智能体的基本属性
        self.name = name
        self.description = description
        # 大语言模型客户端
        self._llm_client = llm_client
        # 对话记录：{sender: [message1, message2, ...]}
        self._chat_messages: Dict[Sender, List[Dict[str, Any]]] = defaultdict(list)
        # 工具
        self._tools: List[Tool] = []
        self._tool_map: Dict[str, Callable] = {}
        # 回复钩子
        self._reply_hooks: List[ReplyHookFunction] = [
            self._generate_llm_reply,
            self._generate_tool_reply
        ]
        self.logger = logger

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
    def chat_messages(self) -> Dict[Sender, List[Dict[str, Any]]]:
        """对话记录"""
        return dict(self._chat_messages)

    @property
    def tools(self):
        """工具"""
        return self._tools

    def print_chat_messages(self, sender: Sender = "__temp__"):
        """打印对话记录

        Args:
            sender (str | Agent): 发送者
        """
        chat_messages = self._chat_messages.get(sender, [])
        for message in chat_messages:
            if "tool_calls" in message:
                print("Role: {role}".format(role=message["role"], content=message["content"]))
                for tool_call in message["tool_calls"]:
                    print("Tool Call: {tool_call}".format(tool_call=tool_call))
                print("\n")
            else:
                print("Role: {role}\nContent: {content}\n\n".format(role=message["role"], content=message["content"]))

    def make_plan(self, requirement: str, interactive: bool = False, **kwargs) -> AgentTasks:
        """制定计划

        Args:
            requirement (str): 需求
            interactive (bool): 是否支持交互式

        Jinja2 Variables:
            requirement: 需求
            tools (): 工具列表
            project_files (dict): 项目文件列表
            is_file_content (bool): 是否显示文件内容，默认为空
            project_resources (dict): 项目资源列表
            is_resource_content (bool): 是否显示资源内容，默认为空
        """
        make_plan_prompt = PromptLoader.get_prompt(
            f"base/make_plan.prompt",
            requirement=requirement,
            tools=self._tools,
            **kwargs
        )
        print(requirement)
        print(make_plan_prompt)
        make_plan_messages = self.generate_reply(make_plan_prompt, remember=False, model_schema=AgentTasks)
        print(make_plan_messages)
        print(make_plan_messages[-1]["content"])
        print(make_plan_messages[-1].get("tool_calls", None))

    def generate_reply(self, messages: Union[str, List[Dict[str, Any]]], sender: Sender = "__temp__",
                       remember: bool = True,
                       **kwargs) -> List[Dict[str, Any]]:
        """生成大模型回复

        Args:
            messages (str | list): 消息
            sender (str | Agent): 发送者
            remember (bool): 是否记住对话记录
            **kwargs: 其他参数
        """
        # 格式化消息
        if isinstance(messages, str):
            messages = [
                {"role": "user", "content": messages}
            ]
        # 获取对话记录
        # TODO: 裁剪对话记录使其不超过大模型上下文长度
        messages = self._chat_messages.get(sender, []) + messages

        # 生成回复
        for reply_hook in self._reply_hooks:
            message = reply_hook(messages, sender, **kwargs)
            # 若回复为空，则继续下一个回复钩子
            if not message:
                continue
            messages.append(message)

        if sender != "__temp__" and remember:
            # 记住对话记录
            self._chat_messages[sender] = messages

        return messages

    def solve(self, messages: Union[str, List[Dict[str, Any]]], sender: Sender = "__temp__", *,
              terminate_trigger: Callable = default_terminate_trigger, max_rounds: int = 3, plan: bool = True,
              **kwargs) -> List[Dict[str, Any]]:
        """通过多次循环来解决问题

        Args:
            messages (str | list): 消息
            sender (str | Agent): 发送者
            terminate_trigger (Callable): 终止触发器
            max_rounds (int): 最大循环次数
            plan (bool): 是否规划, 若开启规划，则 max_rounds 失效
            **kwargs: 其他参数
        """
        model_schema = kwargs.pop("model_schema", None)
        current_round = 0
        while current_round < max_rounds:
            if current_round == 0:
                temp_messages = self.generate_reply(messages, sender, **kwargs)
            else:
                temp_messages = self.generate_reply("", sender, **kwargs)
            if not temp_messages or terminate_trigger(temp_messages[-1].get("content", "")):
                break
            current_round += 1
        return messages

    def _generate_llm_reply(self, messages: List[Dict[str, Any]], sender: Sender, **kwargs) -> Dict[str, Any]:
        """生成大模型回复

        Args:
            messages (list): 消息
            sender (str | Agent): 发送者
            **kwargs: 其他参数
        """
        if messages[0].get("role") != "system":
            messages.insert(0, {
                "role": "system",
                "content": self.system_message
            })
        # 过滤掉工具调用消息
        messages = [message for message in messages if "tool_calls" not in message]
        response = self._llm_client.create(messages, tools=self._tools, **kwargs)
        self.logger.debug(
            "generate_llm_reply: messages={messages}, response={response}".format(messages=messages, response=response))
        response_message = {
            "role": "assistant",
            "content": response.choices[0].message.content,
        }
        if response.choices[0].message.tool_calls:
            response_message["tool_calls"] = [
                tool_call.model_dump() for tool_call in response.choices[0].message.tool_calls
            ]
        return response_message

    def _generate_tool_reply(self, messages: List[Dict[str, Any]], sender: Sender,
                             **kwargs) -> Dict[str, Any] | None:
        """生成工具回复

        Args:
            messages (list): 消息
            sender (str | Agent): 发送者
            **kwargs: 其他参数
        """
        if not messages:
            return
        if "tool_calls" not in messages[-1] or messages[-1]["tool_calls"] is None:
            return
        # [(tool_name, tool_args, result), ...]
        tool_calls_message_content = ""
        for tool_call in messages[-1]["tool_calls"]:
            tool_name = tool_call["function"]["name"]
            tool_json_args = tool_call["function"]["arguments"]
            try:
                tool_args = json.loads(tool_json_args)
            except json.JSONDecodeError:
                return {
                    "role": "user",
                    "content": f"工具参数解析错误：{tool_json_args}"
                }
            tool = self._tool_map.get(tool_name)
            if not tool:
                continue
            tool_signature = "{tool_name}({tool_args})".format(tool_name=tool_name, tool_args=', '.join(
                [f'{k}={v}' for k, v in tool_args.items()]))
            try:
                tool_response = tool(**tool_args)
                tool_calls_message_content += "# {tool_signature}\n工具调用结果：{tool_response}\n".format(
                    tool_signature=tool_signature, tool_response=tool_response)
            except Exception as e:
                tool_calls_message_content += "# {tool_signature}\n工具调用错误：{error}\n".format(
                    tool_signature=tool_signature, error=e)
        response = {
            "role": "user",
            "content": tool_calls_message_content,
        }
        self.logger.debug("generate_tool_reply: messages={messages}, response={response}".format(messages=messages,
                                                                                                 response=response))
        return response

    def register_reply_hook(self, function: ReplyHookFunction) -> None:
        """注册回复钩子

        Args:
            function (ReplyHookFunction): 回复钩子
        """
        self._reply_hooks.append(function)
        self.logger.debug("register_reply_hook: function={function}".format(function=function))

    def register_tool(self, function: Callable[..., Any], *, name: Optional[str] = None,
                      description: Optional[str] = None,
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
            self.logger.debug("register_tool: tool={tool}".format(tool=function))
        else:
            raise ValueError(f"不支持的工具类型：{type}")

    def __repr__(self) -> str:
        return f"<LLMAgent name={self.name} description={self.description}>"
