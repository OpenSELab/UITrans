from typing import Dict, List, Any, Optional

from pydantic import BaseModel

HarmonyResourceQualifierType = str
HarmonyResourceValueType = Dict[str, Dict[str, str]]


class HarmonyResource(BaseModel):
    """Harmony Resource"""
    pages: List[str]
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
