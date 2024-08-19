from typing import List, Dict

from pydantic import BaseModel

from core.logger.runtime import get_logger

logger = get_logger(name="Global State")


class GlobalState:
    """全局状态
    记录当前项目的全局状态信息
    """
    _instance = None

    def __init__(self):
        self._data = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GlobalState, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def get_resource(self, key: str, default=None):
        """获取鸿蒙资源文件

        通过$key获取资源
        :param key: $key
        :param default: 默认值
        """
        assert key.startswith("$"), f"Key '{key}' must start with '$'"
        key = key.lstrip("$")
        key = key.replace(":", ".")
        if key.startswith("app."):
            key = key.replace("app.", "element.")
        # TODO: 默认为base资源
        return self.get(f"harmony.resources.base.{key}", default)

    def set(self, key, value):
        origin_key = key
        keys = key.split('.')
        data = self._data
        for key in keys[:-1]:
            data = data.setdefault(key, {})
        # 若key已存在, 则抛出异常
        if keys[-1] in data:
            raise KeyError(f"Key '{origin_key}' already exists")
        if isinstance(data, dict):
            data[keys[-1]] = value
            logger.debug(f"Set '{origin_key}': {value}")
        else:
            raise ValueError(f"Key '{origin_key}' is not a dict")

    def set_or_update(self, key, value):
        origin_key = key
        keys = key.split('.')
        data = self._data
        for key in keys[:-1]:
            data = data.setdefault(key, {})
        # 若key已存在，则覆盖
        data[keys[-1]] = value
        logger.debug(f"Set or update '{origin_key}': {value}")

    def update(self, key, value):
        origin_key = key
        keys = key.split('.')
        data = self._data
        for key in keys[:-1]:
            data = data.setdefault(key, {})
        # 若key已存在，则覆盖
        data[keys[-1]] = value
        if keys[-1] in data:
            raise KeyError(f"Key '{origin_key}' is not existed")
        logger.debug(f"Update '{key}': {value}")

    def get(self, key, default=None):
        if key.startswith("$"):
            return self.get_resource(key, default)
        origin_key = key
        keys = key.split('.')
        value = self._data
        try:
            for key in keys[:-1]:
                value = value[key]
                # 除最后一个value外，其余value必须是dict
                if not isinstance(value, dict):
                    raise ValueError(f"Key '{origin_key}' is not a dict")
            logger.debug(f"Get '{origin_key}': {value[keys[-1]]}")
            return value[keys[-1]]
        except (KeyError, TypeError):
            logger.debug(f"Get '{origin_key} failed, return default: {default}")
            return default

    def dumps(self):
        """缓存信息，并将信息同步到文件中"""
        raise NotImplementedError

    def clear(self):
        self._data.clear()

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)


global_state = GlobalState()
