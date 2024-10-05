from core.logger.runtime import get_logger
from core.state.schema import State

logger = get_logger(name="Global State")


class GlobalState:
    """全局状态
    记录当前项目的全局状态信息

    Attributes:
        harmony (dict): 鸿蒙信息
        android (dict): 安卓信息


    """
    _instance = None

    def __init__(self):
        self.harmony = State()
        self.android = State()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GlobalState, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def dumps(self):
        """缓存信息，并将信息同步到文件中"""
        raise NotImplementedError


global_state = GlobalState()
