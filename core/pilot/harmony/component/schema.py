from typing import Dict, List, Optional, Any, Literal
from pydantic import Field

from core.pilot.schema import JSONTypeModel


class ComponentParam(JSONTypeModel):
    type: str | List[str | Dict[str, str]] | Dict[str, str] = Field(description="参数的类型")
    required: bool = Field(default=False, description="是否必填参数")
    description: str = Field(description="参数的描述")
    default: Optional[Any] = Field(default=None, description="参数的默认值")


class ComponentAttribute(JSONTypeModel):
    description: str = Field(description="属性的描述")
    params: Dict[str, ComponentParam] = Field(description="属性的参数")


class ComponentEventReturn(JSONTypeModel):
    type: str = Field(description="返回值的类型")
    description: str = Field(description="返回值的描述")


class ComponentEvent(JSONTypeModel):
    description: str = Field(description="事件的描述")
    params: Optional[Dict[str, ComponentParam]] = Field(description="事件回调的参数")
    returns: Optional[Dict[str, ComponentEventReturn] | ComponentEventReturn] = Field(default=None, description="事件回调的返回值")


class ComponentInterface(JSONTypeModel):
    description: str = Field(description="接口的描述")
    params: Dict[str, ComponentParam] = Field(description="接口的参数")


class ComponentDeclaration(JSONTypeModel):
    description: str = Field(description="组件的描述")
    details: Optional[str] = Field(default=None, description="组件的详细描述")
    interfaces: List[ComponentInterface] = Field(description="组件的接口")
    attributes: Dict[str, ComponentAttribute] = Field(description="组件的属性")
    events: Dict[str, ComponentEvent] = Field(description="组件的事件")
    rules: Optional[List[str]] = Field(default=None, description="组件的使用规则")

    examples: Optional[List[str]] = Field(default=None, description="组件的使用示例")

    is_common_attrs: bool = Field(default=True, description="是否支持通用属性")