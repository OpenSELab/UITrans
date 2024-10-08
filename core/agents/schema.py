import json
import jsonref
from typing import Any, Literal, Optional, Dict, List
import re
from pydantic import BaseModel, Field
from pydantic.json_schema import DEFAULT_REF_TEMPLATE, GenerateJsonSchema, JsonSchemaMode


class CommonBaseModel(BaseModel):
    """
    实现 common_parse_raw 方法，支持对 Markdown 代码块格式的 json 进行解析并生成实例
    重写 model_json_schema 方法，去掉 $defs，$ref 引用的 JSON Schema
    重写 BaseModel 的 __str__ 与 __repr__ 方法，实现在 prompt 中显示 JSON信息
    """

    @classmethod
    def common_parse_raw(cls, data: str):
        """对Markdown代码块格式的json进行解析并生成队形实例"""
        pattern = r"```json\s*([\s\S]*?)\s*```"
        matches = re.search(pattern, data)
        if matches:
            data = matches.group(1)
        # FIX: 'Don\'t have an Account?' -> 'Don\\'t have an Account?', 解决 json.loads() 解析失败的问题
        data = data.replace("\\'", "\\\\'")
        return cls.model_validate_json(data)

    @classmethod
    def model_json_schema(
            cls,
            by_alias: bool = True,
            ref_template: str = DEFAULT_REF_TEMPLATE,
            schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
            mode: JsonSchemaMode = 'validation',
    ) -> dict[str, Any]:
        """没有$defs，$ref引用的JSON Schema。"""

        def remove_defs(d):
            if isinstance(d, dict):
                return {k: remove_defs(v) for k, v in d.items() if k != "$defs"}
            elif isinstance(d, list):
                return [remove_defs(v) for v in d]
            else:
                return d

        schema = super().model_json_schema()
        schema = remove_defs(jsonref.loads(json.dumps(schema)))
        return schema

    def __str__(self):
        return self.model_dump_json()

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))


class AgentTaskTool(CommonBaseModel):
    name: str = Field(description="工具名称")
    parameters: Dict[str, Any] = Field(description="工具参数, key 为参数名, value 为参数值")


class AgentTask(CommonBaseModel):
    type: Literal["normal", "tool"] = Field(
        description="任务类型, normal: 一般任务, tool: 需要调用工具的任务")
    description: str = Field(description="任务描述")
    tool: Optional[List[AgentTaskTool]] = Field(description="需要调用的工具列表，仅当 type 为 tool 时有效")
    explanation: Optional[str] = Field(description="原因说明")


class AgentTasks(CommonBaseModel):
    tasks: list[AgentTask] = Field(description="任务列表")
