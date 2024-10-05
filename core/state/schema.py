from typing import Dict, List, Any, Optional
from pydantic import BaseModel

HarmonyResourceQualifierType = str
HarmonyResourceValueType = Dict[str, Dict[str, str]]


class State(BaseModel):
    """
    支持a.b.c的访问方式
    Examples:
        >>> state = State()
        >>> state.set("a.b.c", 1)
        >>> state.get("a.b.c")
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        self._data = {}

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        keys = key.split(".")
        data = self._data
        # 逐层访问
        for key in keys:
            # 除非最后一层外，否则必须是dict
            if not isinstance(data, dict):
                raise ValueError(f"Invalid key: {key}, value is not a dict")
            if key not in data:
                return default
            data = data[key]
        return data

    def set(self, key: str, value: Any):
        keys = key.split(".")
        data = self._data
        for key in keys[:-1]:
            data = data.setdefault(key, {})
        data[keys[-1]] = value

    def update(self, key: str, value: Any):
        keys = key.split(".")
        data = self._data
        for key in keys[:-1]:
            data = data.setdefault(key, {})
        data.update({keys[-1]: value})


class HarmonyResource(BaseModel):
    """Harmony Resource

    Attributes:
        values: 资源值
        medias: 媒体资源
        all_values: 所有资源值
        all_medias: 所有媒体资源
    """
    values: HarmonyResourceValueType
    medias: Dict[str, str]
    all_values: Dict[HarmonyResourceQualifierType, HarmonyResourceValueType]
    all_medias: Dict[HarmonyResourceQualifierType, Dict[str, str]]


class HarmonyStateFile(BaseModel):
    """Harmony Project State File"""
    name: str
    path: str
    description: str
    content: str


class HarmonyStatePage(BaseModel):
    """Harmony Project State Page"""
    name: str
    path: str
    description: str
    content: str


class HarmonyStateComponent(BaseModel):
    """Harmony Project State Component"""
    name: str
    path: str
    description: str
    content: str


class HarmonyState(BaseModel):
    """Harmony Project State"""
    name: str = None  # 项目名称
    path: str = None  # 项目路径
    description: str = None  # 项目描述
    files: Dict[str, HarmonyStateFile] = None  # 文件信息
    pages: Dict[str, HarmonyStatePage] = None  # 页面信息
    components: Dict[str, HarmonyStateComponent] = None
    resources: HarmonyResource = None  # 资源文件
