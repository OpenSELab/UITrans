"""
JSON Schema 介绍
BASIC_TYPES：基本类型定义
IMAGE_TYPES：图像类型定义
INTERFACE_TYPES：接口类型定义

组件: {
    "description": "组件描述“
}

示例：
Scroll: {
    "description": "可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动，支持单个子组件。"
    "constructor": {
        "scroller": {
            "type": "Scroller",
            "required": False,
            "description": "可滚动组件的控制器。用于与可滚动组件进行绑定。"
        }
    },
    "attributes": {
        "scrollable": {
            "description": "设置滚动方向。",
            "params": {
                "value": {
                    "type": "ScrollDirection",
                    "required": true,
                    "description": "滚动方向。",
                    "default": "ScrollDirection.Vertical"
                }
            }
        }
        ...
    },
    "events": {
        "onScrollFrameBegin": {
            "description": "onScrollFrameBegin(event: (offset: number, state: ScrollState) => { offsetRemain: number; })\n\n每帧开始滚动时触发，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。\n\n支持offsetRemain为负值。\n\n若通过onScrollFrameBegin事件和scrollBy方法实现容器嵌套滚动，需设置子滚动节点的EdgeEffect为None。如Scroll嵌套List滚动时，List组件的edgeEffect属性需设置为EdgeEffect.None。\n\n触发该事件的条件：\n\n1、滚动组件触发滚动时触发，包括键鼠操作等其他触发滚动的输入设置。\n\n2、调用控制器接口时不触发。\n\n3、越界回弹不触发。\n\n4、拖动滚动条不触发。",
            "params": {
                "offset": {
                    "type": "number",
                    "required": True,
                    "description": "即将发生的滑动量，单位vp。"
                },
                "state": {
                    "type": "ScrollState",
                    "required": True,
                    "description": "当前滑动状态。"
                }
            }
        }
    }
    ...
}

Prompt:
请根据以下文档，提取组件的JSON信息。
文档：
[[文档]]
规则：
* 1. 对于具有默认值的参数，请使用default键指出，并在描述中去除关于默认值的介绍；
* 2. 在描述中指出对子组件的支持描述，例如"可以包含单个子组件。"，具体内容请参考文档。
* 3. 对于有多种type的情况，请使用数组而非`|`, 对于只有单个type的情况，不要使用数组而是直接使用字符串。
* 4. 默认值为空时可以忽略不写，当前API版本为12，对于版本12之前的默认值可以忽略。

JSON Schema: {'properties': {'description': {'description': '组件的描述', 'title': 'Description', 'type': 'string'}, 'details': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'description': '组件的详细描述', 'title': 'Details'}, 'interfaces': {'description': '组件的接口', 'items': {'properties': {'description': {'description': '接口的描述', 'title': 'Description', 'type': 'string'}, 'params': {'additionalProperties': {'properties': {'type': {'anyOf': [{'type': 'string'}, {'items': {'anyOf': [{'type': 'string'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}]}, 'type': 'array'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}], 'description': '参数的类型', 'title': 'Type'}, 'required': {'default': False, 'description': '是否必填参数', 'title': 'Required', 'type': 'boolean'}, 'description': {'description': '参数的描述', 'title': 'Description', 'type': 'string'}, 'default': {'anyOf': [{}, {'type': 'null'}], 'default': None, 'description': '参数的默认值', 'title': 'Default'}}, 'required': ['type', 'description'], 'title': 'ComponentParam', 'type': 'object'}, 'description': '接口的参数', 'title': 'Params', 'type': 'object'}}, 'required': ['description', 'params'], 'title': 'ComponentInterface', 'type': 'object'}, 'title': 'Interfaces', 'type': 'array'}, 'attributes': {'additionalProperties': {'properties': {'description': {'description': '属性的描述', 'title': 'Description', 'type': 'string'}, 'params': {'additionalProperties': {'properties': {'type': {'anyOf': [{'type': 'string'}, {'items': {'anyOf': [{'type': 'string'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}]}, 'type': 'array'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}], 'description': '参数的类型', 'title': 'Type'}, 'required': {'default': False, 'description': '是否必填参数', 'title': 'Required', 'type': 'boolean'}, 'description': {'description': '参数的描述', 'title': 'Description', 'type': 'string'}, 'default': {'anyOf': [{}, {'type': 'null'}], 'default': None, 'description': '参数的默认值', 'title': 'Default'}}, 'required': ['type', 'description'], 'title': 'ComponentParam', 'type': 'object'}, 'description': '属性的参数', 'title': 'Params', 'type': 'object'}}, 'required': ['description', 'params'], 'title': 'ComponentAttribute', 'type': 'object'}, 'description': '组件的属性', 'title': 'Attributes', 'type': 'object'}, 'events': {'additionalProperties': {'properties': {'description': {'description': '事件的描述', 'title': 'Description', 'type': 'string'}, 'params': {'anyOf': [{'additionalProperties': {'properties': {'type': {'anyOf': [{'type': 'string'}, {'items': {'anyOf': [{'type': 'string'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}]}, 'type': 'array'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}], 'description': '参数的类型', 'title': 'Type'}, 'required': {'default': False, 'description': '是否必填参数', 'title': 'Required', 'type': 'boolean'}, 'description': {'description': '参数的描述', 'title': 'Description', 'type': 'string'}, 'default': {'anyOf': [{}, {'type': 'null'}], 'default': None, 'description': '参数的默认值', 'title': 'Default'}}, 'required': ['type', 'description'], 'title': 'ComponentParam', 'type': 'object'}, 'type': 'object'}, {'type': 'null'}], 'description': '事件回调的参数', 'title': 'Params'}, 'returns': {'anyOf': [{'additionalProperties': {'properties': {'type': {'description': '返回值的类型', 'title': 'Type', 'type': 'string'}, 'description': {'description': '返回值的描述', 'title': 'Description', 'type': 'string'}}, 'required': ['type', 'description'], 'title': 'ComponentEventReturn', 'type': 'object'}, 'type': 'object'}, {'properties': {'type': {'description': '返回值的类型', 'title': 'Type', 'type': 'string'}, 'description': {'description': '返回值的描述', 'title': 'Description', 'type': 'string'}}, 'required': ['type', 'description'], 'title': 'ComponentEventReturn', 'type': 'object'}, {'type': 'null'}], 'default': None, 'description': '事件回调的返回值', 'title': 'Returns'}}, 'required': ['description', 'params'], 'title': 'ComponentEvent', 'type': 'object'}, 'description': '组件的事件', 'title': 'Events', 'type': 'object'}, 'rules': {'anyOf': [{'items': {'type': 'string'}, 'type': 'array'}, {'type': 'null'}], 'default': None, 'description': '组件的使用规则', 'title': 'Rules'}, 'examples': {'anyOf': [{'items': {'type': 'string'}, 'type': 'array'}, {'type': 'null'}], 'default': None, 'description': '组件的使用示例', 'title': 'Examples'}, 'is_common_attrs': {'default': True, 'description': '是否支持通用属性', 'title': 'Is Common Attrs', 'type': 'boolean'}}, 'required': ['description', 'interfaces', 'attributes', 'events'], 'title': 'ComponentDeclaration', 'type': 'object'}
最后请将 JSON Schema 转为 Python 中的字典格式。

以下是一个示例：
{
    "description": "可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动，支持单个子组件。"
    "interfaces": [
        {
            "description": "Scroll(scroller?: Scroller)",
            "params": {
                "scroller": {
                    "type": "Scroller",
                    "description": "可滚动组件的控制器。用于与可滚动组件进行绑定。"
                }
            }
        }
    ],
    "attributes": {
        "scrollable": {
            "description": "设置滚动方向。",
            "params": {
                "value": {
                    "type": "ScrollDirection",
                    "required": true,
                    "description": "滚动方向。",
                    "default": "ScrollDirection.Vertical"
                }
            }
        }
        ...
    },
    "events": {
        "onScrollFrameBegin": {
            "description": "onScrollFrameBegin(event: (offset: number, state: ScrollState) => { offsetRemain: number; })\n\n每帧开始滚动时触发，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。\n\n支持offsetRemain为负值。\n\n若通过onScrollFrameBegin事件和scrollBy方法实现容器嵌套滚动，需设置子滚动节点的EdgeEffect为None。如Scroll嵌套List滚动时，List组件的edgeEffect属性需设置为EdgeEffect.None。\n\n触发该事件的条件：\n\n1、滚动组件触发滚动时触发，包括键鼠操作等其他触发滚动的输入设置。\n\n2、调用控制器接口时不触发。\n\n3、越界回弹不触发。\n\n4、拖动滚动条不触发。",
            "params": {
                "offset": {
                    "type": "number",
                    "required": True,
                    "description": "即将发生的滑动量，单位vp。"
                },
                "state": {
                    "type": "ScrollState",
                    "required": True,
                    "description": "当前滑动状态。"
                }
            }
        }
    }
    ...
}


示例代码 Prompt：
你是一个专业的鸿蒙ArkUI开发者，你的任务是为示例代码编写详细的功能与效果描述、实现思路注释。
以下的组件文档，请你从中提取全部代码示例，并为其编写功能与效果描述、实现思路注释：
[[文档]]
在编写时你需要遵守以下规则：
* 1. 一个示例代码中可能含有多个功能块，你需要为每一个功能块编写功能与效果描述以及适当的注释，不需要指出功能块1、功能块2等。
* 2. 适当的注释是指开发者无法从代码中**直接**获取的信息，例如代码的设计思路、实现细节等。
* 3. 对于关键的属性、方法、变量等，你需要给出其功能与效果描述以及适当的注释。
* 4. 功能与效果描述应该以注释的形式给出。
* 5. 实现思路应该以注释的形式给出，并将其编写在代码的起始位置。
* 6. 无需回答除了代码和注释以外的其他内容，包括解释、你的思路等等。
* 7. 你需要尽可能为组件的属性、接口、事件等关键代码添加注释。

以下是一个模板示例：
/*
{{ 实现思路 }}
{{ 总体功能与效果描述 }}
*/

// {{ 文件名，例如xxx.ets }}
{{ 代码，包括功能与效果描述注释、关键注释等 }}
"""
from typing import Optional, Dict

from core.pilot.harmony.component.defs.common.attributes import get_harmony_common_attributes
from core.pilot.harmony.component.defs.basic_component import BASIC_COMPONENT
from core.pilot.harmony.component.defs.canvas_component import CANVAS_COMPONENT
from core.pilot.harmony.component.defs.container_component import CONTAINER_COMPONENT
from core.pilot.harmony.component.defs.drawing_component import DRAWING_COMPONENT
from core.pilot.harmony.component.defs.global_component import GLOBAL_COMPONENT
from core.pilot.harmony.component.defs.media_component import MEDIA_COMPONENT
from core.pilot.harmony.component.defs.safe_component import SAFE_COMPONENT
from core.pilot.harmony.component.defs.advanced_component import ADVANCED_COMPONENT
from core.logger.runtime import get_logger
from core.pilot.harmony.component.schema import ComponentDeclaration

logger = get_logger(name="Harmony Types")

COMPONENTS: Optional[Dict[str, ComponentDeclaration]] = None
CUSTOM_COMPONENTS: Dict[str, ComponentDeclaration] = {}


def _init_harmony_components():
    global COMPONENTS
    logger.debug("Initializing Harmony components...")
    COMPONENTS = {}
    temp_component = {
        **BASIC_COMPONENT,
        **CANVAS_COMPONENT,
        **CONTAINER_COMPONENT,
        **DRAWING_COMPONENT,
        **GLOBAL_COMPONENT,
        **MEDIA_COMPONENT,
        **SAFE_COMPONENT,
        **ADVANCED_COMPONENT
    }
    for component_name, component in temp_component.items():
        if not component.get("interfaces", None):
            continue
        component_schema = ComponentDeclaration(**component)
        if component_schema.is_common_attrs:
            component_schema.attributes.update(get_harmony_common_attributes())
        COMPONENTS[component_name] = component_schema


def get_harmony_component(component_name: Optional[str] = None) -> Dict[str, ComponentDeclaration]:
    if component_name is not None:
        if COMPONENTS is None:
            _init_harmony_components()
        if component_name in COMPONENTS:
            return {component_name: COMPONENTS[component_name]}
        return {component_name: None}
    return COMPONENTS


_init_harmony_components()