from typing import List, Dict, Optional

from core.logger.runtime import get_logger
from core.pilot.harmony.component.schema import ComponentEventReturn
from core.pilot.harmony.model.types import TYPES, TypeModel
from core.pilot.harmony.component.components import COMPONENTS
from core.pilot.harmony.component import get_harmony_component

logger = get_logger(name="Harmony Pilot Utils")


def get_component_related_types(component_name: str | List[str], attributes_and_events: Optional[List[str]] = None) -> \
        Dict[str, TypeModel]:
    """获得组件相关的所有类型"""
    remaining_types = set()
    components_name = component_name if isinstance(component_name, list) else [component_name]
    for component_name in components_name:
        if component_name not in COMPONENTS:
            logger.error(f"Component {component_name} not found")
            continue
        component = COMPONENTS[component_name]
        # 对于接口的处理
        for interface in component.interfaces:
            for param_name, param_schema in interface.params.items():
                if isinstance(param_schema.type, list):
                    remaining_types.update(param_schema.type)
                elif isinstance(param_schema.type, dict):
                    remaining_types.update(param_schema.type.values())
                else:
                    remaining_types.add(param_schema.type)
        # 对于属性的处理
        if component.attributes:
            for attribute_name, attribute_schema in component.attributes.items():
                if attributes_and_events and attribute_name not in attributes_and_events:
                    continue
                for param_name, param_schema in attribute_schema.params.items():
                    if isinstance(param_schema.type, list):
                        for type_name in param_schema.type:
                            if isinstance(type_name, str):
                                remaining_types.add(type_name)
                        if isinstance(param_schema.type, str):
                            remaining_types.update(param_schema.type)
                    elif isinstance(param_schema.type, dict):
                        remaining_types.update(param_schema.type.values())
                    else:
                        remaining_types.add(param_schema.type)
        # 对于事件的处理
        if component.events:
            for event_name, event_schema in component.events.items():
                if attributes_and_events and event_name not in attributes_and_events:
                    continue
                # 对于事件参数的处理
                if event_schema.params:
                    for param_name, param_schema in event_schema.params.items():
                        if isinstance(param_schema.type, list):
                            remaining_types.update(param_schema.type)
                        elif isinstance(param_schema.type, dict):
                            remaining_types.update(param_schema.type.values())
                        else:
                            remaining_types.add(param_schema.type)
                # 对于事件返回值的处理
                # returns有两种类型，一种是Dict[str, ComponentEventReturn]，一种是ComponentEventReturn
                if event_schema.returns:
                    if isinstance(event_schema.returns, dict):
                        for return_name, return_schema in event_schema.returns.items():
                            if isinstance(return_schema.type, list):
                                remaining_types.update(return_schema.type)
                            else:
                                remaining_types.add(return_schema.type)
                    elif isinstance(event_schema.returns, ComponentEventReturn):
                        remaining_types.add(event_schema.returns.type)
    related_types = get_related_types(list(remaining_types))
    return related_types


def get_related_types(type_name: str | List[str]) -> Dict[str, TypeModel]:
    if not TYPES:
        logger.error("Types not initialized")
    assert TYPES, "Types not initialized"
    types_name = type_name if isinstance(type_name, list) else [type_name]
    related_types = {}
    for type_name in types_name:
        # 依次遍历找到每一个 type 的所有相关 type
        remaining_types = []
        if type_name not in TYPES:
            continue
        if type_name not in related_types:
            remaining_types.append(type_name)

        while remaining_types:
            current_type_name = remaining_types.pop()
            current_type = TYPES[current_type_name]
            # 将当前类型添加到 related_types 中
            related_types[current_type_name] = current_type
            if current_type.type == "object":
                # 如果是 object 类型，遍历 properties，将所有的 type 加入 remain_types
                for property_name, property_schema in current_type.properties.items():
                    property_types = property_schema.type if isinstance(property_schema.type, list) else [
                        property_schema.type]
                    for property_type in property_types:
                        if property_type not in TYPES:
                            # TODO：这里忽略了基本类型和函数类型
                            # logger.warning(f"Type {property_name} not found")
                            continue
                        if property_type not in related_types and property_type not in remaining_types:
                            remaining_types.append(property_type)
            else:
                temp_types = current_type.type if isinstance(current_type.type, list) else [current_type.type]
                for type_name in temp_types:
                    if type_name not in TYPES:
                        # TODO：这里忽略了基本类型和函数类型
                        # logger.warning(f"Type {type_name} not found")
                        continue
                    if type_name not in related_types and type_name not in remaining_types:
                        remaining_types.append(type_name)
    return related_types


def generate_component_interface_document(component_name: str) -> str:
    component = get_harmony_component(component_name)
    if component_name not in component:
        return ""
    component_schema = component[component_name]
    interface_documents = []
    for interface in component_schema.interfaces:
        interface_documents.append(f"""接口描述：{interface.description}
接口参数：{interface.params}
""")
    return "\n".join(interface_documents)


def generate_type_document(type_name: str, type_schema: TypeModel) -> str:
    if type_schema.type == "object":
        document = f"""类型名：{type_name}
类型描述：{type_schema.description}
参数：{type_schema.properties}
"""
    elif type_schema.type == "enum":
        # 枚举值介绍
        all_enum_description = ""
        for enum_value, enum_description in type_schema.enumDescriptions.items():
            all_enum_description += f"* {enum_value}: {enum_description}\n"
        document = f"""枚举类型名：{type_name}
枚举类型描述：{type_schema.description}
枚举值：{type_schema.enum}
枚举值描述：
{all_enum_description}
"""
    else:
        # 普通类型
        document = f"""类型名：{type_name}
类型描述：{type_schema.description}
类型：{type_schema.type}
"""
    if type_schema.examples:
        for example in type_schema.examples:
            document += f"""类型{type_name}示例：
{example}
"""
    return document


__all__ = ["get_component_related_types", "get_harmony_component", "generate_type_document", "generate_component_interface_document"]

if __name__ == '__main__':
    print(get_component_related_types("Button"))
