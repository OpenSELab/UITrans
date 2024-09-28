from typing import Literal, Optional

from core.logger.base_logger import BaseLogger
from core.config.schema import LoggerConfig

# 日志的基本路径/项目路径
BASE_LOG_DIR = r"D:\Codes\Python\harmony-pilot"
# 日志配置
default_logger_config = LoggerConfig(
    level="DEBUG",
    type="console",
    fmt="%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    logfile=f"{BASE_LOG_DIR}/pilot_logs/%Y%m%d.log"
)


class LoggerManager:
    logger_dict = {}
    logger_config: LoggerConfig = default_logger_config

    @classmethod
    def set_logger_config(cls, logger_config: LoggerConfig):
        cls.logger_config = logger_config

    @classmethod
    def get_logger(cls, name: str, logger_type: Optional[Literal["file", "console"]] = None) -> BaseLogger:
        if cls.logger_config is None:
            raise ValueError("LoggerManager 未初始化")

        if name in cls.logger_dict:
            return cls.logger_dict[name]
        logger_type = logger_type or cls.logger_config.type
        if logger_type == "file":
            from .file_logger import FileLogger
            logger = FileLogger(
                name=name,
                level=cls.logger_config.level,
                fmt=cls.logger_config.fmt,
                logfile=cls.logger_config.logfile
            )
        elif logger_type == "console":
            from .stream_logger import StreamLogger
            logger = StreamLogger(
                name=name,
                level=cls.logger_config.level,
                fmt=cls.logger_config.fmt
            )
        else:
            raise ValueError(f"无效的日志类型: {logger_type}")
        cls.logger_dict[name] = logger
        return logger


def get_logger(name, **kwargs) -> BaseLogger:
    return LoggerManager.get_logger(name, **kwargs)
