import logging
import sys
import uuid

import colorlog

from .base_logger import BaseLogger


class StreamLogger(BaseLogger):
    """文件日志记录器

    将日志记录到文件中。
    """

    def __init__(self, name: str = "a2x", level: str = "info"):

        self.enable = True
        self.session_id = str(uuid.uuid4())
        self.logger = logging.getLogger(f"[{name}]")

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
                raise ValueError(f"Invalid log level: {level}")
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
            }
        )
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, msg: str | dict, *args, **kwargs) -> None:
        if not self.enable:
            return
        self.logger.info(msg)

    def debug(self, msg: str, *args, **kwargs) -> None:
        if not self.enable:
            return
        self.logger.debug(msg)

    def warning(self, msg: str, *args, **kwargs) -> None:
        if not self.enable:
            return
        self.logger.debug(msg)

    def error(self, msg: str, *args, **kwargs) -> None:
        if not self.enable:
            return
        self.logger.error(msg)

    def disable(self):
        self.logger.enable = False
