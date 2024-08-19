"""
Prompt:
请根据以下文档，提取各个属性的JSON信息。
文档：
[[文档]]
规则：
1. 对于具有默认值的参数，请使用default键指出，并在描述中去除关于默认值的介绍；
2. 在描述中指出对子组件的支持描述，例如"可以包含单个子组件。"，具体内容请参考文档。
3. 对于有多种type的情况，请使用数组而非`|`, 对于只有单个type的情况，不要使用数组而是直接使用字符串。
4. 默认值为空时可以忽略不写。
5. 非枚举类型无需编写 enum与enumDescriptions。
6. 需要将true转换为True，同理false转换为False。
7. 例如`11+`, `12+`等并非是属性名，而是版本要求，不需要提取。

JSON Schema: {'属性名': {'properties': {'description': {'title': 'Description', 'type': 'string'}, 'params': {'additionalProperties': {'properties': {'type': {'anyOf': [{'type': 'string'}, {'items': {'type': 'string'}, 'type': 'array'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}], 'title': 'Type'}, 'required': {'default': False, 'title': 'Required', 'type': 'boolean'}, 'description': {'title': 'Description', 'type': 'string'}, 'default': {'anyOf': [{}, {'type': 'null'}], 'default': None, 'title': 'Default'}}, 'required': ['type', 'description'], 'title': 'ComponentParam', 'type': 'object'}, 'title': 'Params', 'type': 'object'}}, 'required': ['description', 'params'], 'title': 'ComponentAttribute', 'type': 'object'}}
最后请将JSON Schema转为Python中的字典格式

示例：
{
    "width": {
        "description": "设置组件自身的宽度，缺省时使用元素自身内容需要的宽度。若子组件的宽大于父组件的宽，则会画出父组件的范围。从API version 10开始，该接口支持calc计算特性。",
        "params": {
          "value": {
            "type": "Length",
            "required": True,
            "description": "要设置的组件宽度。单位：vp"
          }
        }
    }
}
"""
from typing import Dict, Optional

from core.pilot.harmony.component.schema import ComponentAttribute
from core.pilot.harmony.component.defs.common.defs.size_attribute import SIZE_COMMON_ATTRIBUTES
from core.pilot.harmony.component.defs.common.defs.position_attribute import POSITION_COMMON_ATTRIBUTES
from core.pilot.harmony.component.defs.common.defs.layout_constraints_attribute import LAYOUT_CONSTRAINTS_ATTRIBUTE
from core.pilot.harmony.component.defs.common.defs.flex_layout_attribute import FLEX_LAYOUT_ATTRIBUTE

COMMON_ATTRIBUTES: Optional[Dict[str, ComponentAttribute]] = None


def _init_harmony_common_attributes():
    global COMMON_ATTRIBUTES
    COMMON_ATTRIBUTES = {}
    temp_common_attribute = {
        **SIZE_COMMON_ATTRIBUTES,
        **POSITION_COMMON_ATTRIBUTES,
        **LAYOUT_CONSTRAINTS_ATTRIBUTE,
        **FLEX_LAYOUT_ATTRIBUTE
    }
    for attribute_name, attribute in temp_common_attribute.items():
        COMMON_ATTRIBUTES[attribute_name] = ComponentAttribute(**attribute)


def get_harmony_common_attributes(attribute_name: Optional[str] = None) -> Dict[str, ComponentAttribute]:
    if attribute_name is not None:
        if COMMON_ATTRIBUTES is None:
            _init_harmony_common_attributes()
        return {
            attribute_name: COMMON_ATTRIBUTES[attribute_name]
        }
    return COMMON_ATTRIBUTES


_init_harmony_common_attributes()
