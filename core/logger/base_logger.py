from abc import ABC, abstractmethod


class BaseLogger(ABC):
    """日志记录器
    - 记录 Agent 的输入和输出日志
    - 记录 LLM 请求和响应的日志
    """

    @abstractmethod
    def debug(self, msg: str, *args, **kwargs) -> None:
        """记录调试日志"""
        ...

    @abstractmethod
    def info(self, msg: str, *args, **kwargs) -> None:
        """记录日志"""
        ...

    @abstractmethod
    def warning(self, msg: str, *args, **kwargs) -> None:
        """记录警告日志"""
        ...

    @abstractmethod
    def error(self, msg: str, *args, **kwargs) -> None:
        """记录错误日志"""
        ...

    @abstractmethod
    def disable(self):
        """禁用日志记录"""
        ...
