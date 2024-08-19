import os
import warnings
from typing import Literal

from .base_logger import BaseLogger

DEFAULT_LOGGER_TYPE = os.environ.get("HARMONY_PILOT_LOGGER_TYPE", "console")
DEFAULT_LOGGER_LEVEL = os.environ.get("HARMONY_PILOT_LOGGER_LEVEL", "info").lower()


class LoggerFactory:
    _instance = None

    def __init__(self):
        self.logger_dict = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggerFactory, cls).__new__(cls)
        return cls._instance

    def get_logger(self, logger_type: Literal["file", "console"], **kwargs) -> BaseLogger:
        if "name" in kwargs and kwargs["name"] in self.logger_dict:
            return self.logger_dict[kwargs["name"]]
        if logger_type == "file":
            from .file_logger import FileLogger
            if "filename" not in kwargs:
                raise ValueError("文件日志记录器需要指定文件名")
            logger = FileLogger(**kwargs)
        elif logger_type == "console":
            from .stream_logger import StreamLogger
            logger = StreamLogger(**kwargs)
        else:
            raise ValueError(f"无效的日志类型: {logger_type}")
        self.logger_dict[logger_type] = logger
        return logger


__LOGGER_FACTORY_INSTANCE = LoggerFactory()


def get_logger(logger_type: Literal["file", "console"] = DEFAULT_LOGGER_TYPE, **kwargs) -> BaseLogger:
    if "level" not in kwargs:
        kwargs["level"] = DEFAULT_LOGGER_LEVEL
    return __LOGGER_FACTORY_INSTANCE.get_logger(logger_type, **kwargs)


def disable_logger():
    """
    禁用所有日志记录器
    """
    warnings.warn("禁用日志输出！")
    for logger_type in __LOGGER_FACTORY_INSTANCE.logger_dict.keys():
        __LOGGER_FACTORY_INSTANCE.logger_dict[logger_type].disable()
