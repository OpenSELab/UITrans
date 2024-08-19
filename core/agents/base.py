from abc import ABC
from typing import List, Dict, Any, Optional, Union


class Agent(ABC):
    """智能体的基本接口
    """

    def __init__(self, name: str, description: str, config: Optional[dict] = None, **kwargs):
        self._name = name
        self._description = description
        self._config = config if config else {}

    @property
    def name(self) -> str:
        """智能体的名称"""
        return self._name

    @property
    def description(self) -> str:
        """智能体的描述"""
        return self._description

    def receive(
            self,
            messages: Union[str, Dict[str, Any], List[Dict[str, Any]]],
            sender: Optional[Union[str, "Agent"]],
            is_execute: bool = False,
            **kwargs
    ) -> Union[str, Dict[str, Any], None]:
        """智能体感知外界信息

        Args:
            messages (str | list| dict): 外界信息
            sender (str | Agent): 信息发送者
            is_execute (bool): 接收外界信息后是否做出响应
            **kwargs: 其他参数

        Returns:
            str | dict | None: 智能体的响应 | None
        """
        raise NotImplementedError

    def execute(self, messages: Union[str, Dict[str, Any], List[Dict[str, Any]]], sender: Union[str, "Agent"],
                **kwargs) -> Union[str, Dict[str, Any], None]:
        """智能体对外界感知做出响应

        Args:
            messages (str, dict, list): 外界信息
            sender (str | Agent): 信息发送者
            **kwargs: 其他参数
        """
        raise NotImplementedError

