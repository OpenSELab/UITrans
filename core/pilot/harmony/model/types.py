"""
JSON Schema 介绍
BASIC_TYPES：基本类型定义
IMAGE_TYPES：图像类型定义
INTERFACE_TYPES：接口类型定义

对于对象的介绍
类型对象：{
    "type": [] | "",  // type除了标准的类型外，还可以是一些鸿蒙内置的类型或enum。
    "description": "类型介绍",
    "properties": {
        "属性1": {
            "type": "该属性支持的类型",
            "required": "true" | false,  // 是否必须,
            "description": "属性介绍"
            "enum": ["枚举值1", "枚举值2", ...],  // 如果属性是枚举类型，可以使用enum
            "enumDescriptions": {
                "枚举值1": "枚举值1的介绍",
                "枚举值2": "枚举值2的介绍",
                ...
            },
            "default": xxx  // 默认值
        }
        ...
    }
    "examples": ["示例1", ...]
}
"""
from typing import List, Optional, Dict, Any, Literal

from core.logger.runtime import get_logger
from core.pilot.schema import JSONTypeModel
from core.pilot.harmony.model.defs.basic_type import BASIC_TYPES

logger = get_logger(name="Harmony Types")

PropertyName = str


class TypeModel(JSONTypeModel):
    ...


class PropertyModel(JSONTypeModel):
    type: str | List[str] | Dict[str, str]
    required: bool = False
    description: str
    enum: Optional[List[str]] = None
    enumDescriptions: Optional[Dict[str, str]] = None
    default: Optional[Any] = None


class TypeInterface(JSONTypeModel):
    description: str
    type: Literal["object"]
    properties: Optional[Dict[PropertyName, PropertyModel]] = None
    examples: Optional[List[str]] = None


class TypeDeclaration(JSONTypeModel):
    description: str
    type: str | List[str]
    enum: Optional[List[str]] = None
    enumDescriptions: Optional[Dict[str, str]] = None
    examples: Optional[List[str]] = None


TYPES: Optional[Dict[str, TypeModel]] = None


def _init_harmony_types():
    """初始化全部类型，创建 TypeModel"""
    global TYPES
    logger.debug("Initializing types...")
    TYPES = {}
    for type_name, type_schema in BASIC_TYPES.items():
        is_interface = type_schema.get("type") == "object"
        if is_interface:
            TYPES[type_name] = TypeInterface(**type_schema)
        else:
            TYPES[type_name] = TypeDeclaration(**type_schema)


def get_harmony_type(type_name: Optional[str] = None) -> Dict[str, TypeModel]:
    """获取类型"""
    if type_name is not None:
        if TYPES is None:
            _init_harmony_types()
        return {type_name: TYPES[type_name]}
    return TYPES


_init_harmony_types()
print(TypeDeclaration.model_json_schema())