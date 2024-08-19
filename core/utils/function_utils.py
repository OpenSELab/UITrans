import inspect
from typing import Any, Callable, Dict, Optional, Literal, Annotated, get_args, get_origin


def get_function_schema(f: Callable[..., Any], *, name: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    """获取 OpenAI API 定义的函数的 JSON schema

    Args:
        f: 要获取 JSON schema 的函数
        name: 函数的名称
        description: 函数的描述

    Returns:
        函数的 JSON schema

    Raises:
        AssertionError: 如果函数未注释

    Examples:

    ```python
    def f(a: Annotated[str, "Parameter a"], b: int = 2, c: Annotated[float, "Parameter c"] = 0.1) -> None:
        pass

    get_function_schema(f, description="function f")

    #   {'type': 'function',
    #    'function': {'description': 'function f',
    #        'name': 'f',
    #        'parameters': {'type': 'object',
    #           'properties': {'a': {'type': 'str', 'description': 'Parameter a'},
    #               'b': {'type': 'int', 'description': 'b'},
    #               'c': {'type': 'float', 'description': 'Parameter c'}},
    #           'required': ['a']}}
    #   }
    ```

    """

    param_type_dict = {
        "str": "string",
        "int": "integer",
        "float": "number",
        "bool": "boolean",
        "list": "array",
        "dict": "object"
    }

    # 函数名
    if name is None:
        name = f.__name__
    # 函数描述信息
    if description is None:
        if f.__doc__ is None:
            raise AssertionError(f"函数 {name} 需要 description 参数或函数文档字符串")
        description = f.__doc__

    # 获取函数参数信息
    signature = inspect.signature(f)
    parameters = {
        "type": "object",
        "properties": {},
        "required": []
    }
    for param in signature.parameters.values():
        _param = {}
        if param.default == inspect.Signature.empty:
            # 参数没有默认值
            parameters["required"].append(param.name)
        # 构建参数信息
        if param.annotation == inspect.Signature.empty:
            raise AssertionError(f"函数 {name} 参数 {param.name} 需要注释")
        if get_origin(param.annotation) is not Annotated:
            raise AssertionError(f"函数 {name} 参数 {param.name} 需要 Annotated 注释")
        # 参数注解
        _param["description"] = get_args(param.annotation)[1]
        # 参数类型
        # TODO：支持更多类型
        _param_type = get_args(param.annotation)[0]
        if get_origin(_param_type) is None:
            # 基本数据类型
            _param_type = _param_type.__name__
            if _param_type in param_type_dict:
                _param["type"] = param_type_dict[_param_type]
            else:
                raise AssertionError(f"函数 {name} 参数 {param.name} 类型 {_param_type} 不支持")
        else:
            # 包装类型，目前仅支持 Literal 枚举类型
            if get_origin(_param_type) is Literal:
                _param["enum"] = list(get_args(_param_type))
                # 枚举值的第一个值作为参数的类型
                _param["type"] = type(_param["enum"][0]).__name__

        parameters["properties"][param.name] = _param

    return {
        "type": "function",
        "function": {
            "description": description,
            "name": name,
            "parameters": parameters
        }
    }
