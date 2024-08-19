import json
import logging
import os
import time
import uuid
import warnings

from .base_logger import BaseLogger


class FileLogger(BaseLogger):
    """文件日志记录器

    将日志记录到文件中。
    """

    def __init__(self, name: str = "harmony-pilot", level: str = "info", filename: str = None):

        self.enable = True
        self.session_id = str(uuid.uuid4())

        cur_dir = os.getcwd()
        log_dir = os.path.join(cur_dir, "pilot_logs")
        os.makedirs(log_dir, exist_ok=True)
        if not filename:
            filename = f"{name}_{int(time.time())}.log"
        else:
            filename = f"{name}_{int(time.time())}.log"
        self.log_file = os.path.join(log_dir, filename)
        # 创建日志文件
        try:
            with open(self.log_file, "a"):
                pass
        except Exception as e:
            warnings.warn(f"[file_logger] 无法创建日志文件: {e}")
            raise Exception(f"[file_logger] 无法创建日志文件: {e}")

        self.logger = logging.getLogger("name")

        match level:
            case "debug":
                self.logger.setLevel(logging.DEBUG)
            case "info":
                self.logger.setLevel(logging.INFO)
            case "warning":
                self.logger.setLevel(logging.WARNING)
            case "error":
                self.logger.setLevel(logging.ERROR)
            case _:
                raise ValueError(f"无效的日志等级: {level}")

        file_handler = logging.FileHandler(self.log_file)
        self.logger.addHandler(file_handler)

    def info(self, msg: str | dict, *args, **kwargs) -> None:
        if not self.enable:
            return
        if isinstance(msg, dict):
            msg = json.dumps(msg, indent=4)
        self.logger.info(msg)

    def debug(self, msg: str, *args, **kwargs) -> None:
        if not self.enable:
            return
        if isinstance(msg, dict):
            msg = json.dumps(msg, indent=4)
        self.logger.debug(msg)

    def warning(self, msg: str, *args, **kwargs) -> None:
        if not self.enable:
            return
        if isinstance(msg, dict):
            msg = json.dumps(msg, indent=4)
        self.logger.debug(msg)

    def error(self, msg: str, *args, **kwargs) -> None:
        if not self.enable:
            return
        if isinstance(msg, dict):
            msg = json.dumps(msg, indent=4)
        self.logger.debug(msg)

    def disable(self):
        self.logger.enable = False
