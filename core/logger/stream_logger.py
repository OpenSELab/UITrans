import logging
import sys
import uuid

import colorlog

from .base_logger import BaseLogger


class StreamLogger(BaseLogger):
    """文件日志记录器

    将日志记录到文件中。
    """

    DEFAULT_FMT = "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DEFAULT_DATE_FMT = "%Y-%m-%d %H:%M:%S"

    def __init__(
            self,
            name: str,
            level: str,
            fmt: str = DEFAULT_FMT,
            date_fmt: str = DEFAULT_DATE_FMT
    ):

        self.enable = True
        self.session_id = str(uuid.uuid4())
        self.logger = logging.getLogger(f"[{name}]")

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
                raise ValueError(f"Invalid log level: {level}")
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = colorlog.ColoredFormatter(
            fmt,
            datefmt=date_fmt,
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
