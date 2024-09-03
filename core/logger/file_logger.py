import json
import logging
import os
from datetime import datetime

from core.logger.base_logger import BaseLogger


class FileLogger(BaseLogger):
    """文件日志记录器

    将日志记录到文件中。
    """
    DEFAULT_FMT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DEFAULT_DATE_FMT = "%Y-%m-%d %H:%M:%S"

    def __init__(
            self,
            name: str,
            level: str,
            logfile: str = None,
            fmt: str = DEFAULT_FMT,
            date_fmt: str = DEFAULT_DATE_FMT
    ):
        # 根据当前时间创建对应文件夹, logdir中含有日期格式化字符串
        self.logfile = datetime.now().strftime(logfile)
        os.makedirs(os.path.dirname(self.logfile), exist_ok=True)
        # 创建日志文件
        try:
            with open(self.logfile, "a"):
                pass
        except Exception as e:
            logging.warning(f"[file_logger] 无法创建日志文件: {e}")
            raise Exception(f"[file_logger] 无法创建日志文件: {e}")

        self.logger = logging.getLogger("name")

        match level.upper():
            case "DEBUG":
                self.logger.setLevel(logging.DEBUG)
            case "INFO":
                self.logger.setLevel(logging.INFO)
            case "WARNING":
                self.logger.setLevel(logging.WARNING)
            case "ERROR":
                self.logger.setLevel(logging.ERROR)
            case _:
                raise ValueError(f"无效的日志等级: {level}")

        file_handler = logging.FileHandler(self.logfile)
        formatter = logging.Formatter(
            fmt,
            date_fmt
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, msg: str | dict, *args, **kwargs) -> None:
        if isinstance(msg, dict):
            msg = json.dumps(msg, indent=4)
        self.logger.info(msg)

    def debug(self, msg: str, *args, **kwargs) -> None:
        if isinstance(msg, dict):
            msg = json.dumps(msg, indent=4)
        self.logger.debug(msg)

    def warning(self, msg: str, *args, **kwargs) -> None:
        if isinstance(msg, dict):
            msg = json.dumps(msg, indent=4)
        self.logger.debug(msg)

    def error(self, msg: str, *args, **kwargs) -> None:
        if isinstance(msg, dict):
            msg = json.dumps(msg, indent=4)
        self.logger.debug(msg)

    def disable(self):
        self.logger.enable = False
