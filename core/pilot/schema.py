import json
import jsonref
from typing import List, Any, Optional
import re
from pydantic import BaseModel, Field
from pydantic.json_schema import DEFAULT_REF_TEMPLATE, GenerateJsonSchema, JsonSchemaMode


class CommonBaseModel(BaseModel):

    @classmethod
    def common_parse_raw(cls, data: str):
        """对Markdown代码块格式的json进行解析并生成队形实例"""
        pattern = r"```json\s*([\s\S]*?)\s*```"
        matches = re.search(pattern, data)
        if matches:
            data = matches.group(1)
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


class JSONTypeModel(CommonBaseModel):
    """重写 BaseModel 的 __str__ 与 __repr__ 方法，实现在 prompt 中显示 JSON信息"""

    def __str__(self):
        return self.model_dump_json()

    def __repr__(self):
        return str(self)


class File(CommonBaseModel):
    # name: str = Field(description="文件名。")
    # path: str = Field(description="文件路径。")
    content: str = Field(description="文件内容。")
    description: str = Field(description="文件的描述，即对文件的内容、功能的简单介绍。")


class Files(CommonBaseModel):
    files: List[File] = Field(description="创建的文件列表。")


class Task(CommonBaseModel):
    description: str = Field(description="任务的描述。")
    done: bool = Field(default=False, description="当前任务是否已经完成。")


class BreakdownStory(CommonBaseModel):
    tasks: List[Task] = Field(description="为实施整个计划而需要完成的任务列表。")


class BreakdownLayoutTranslationTask(Task):
    harmony: str = Field(description="鸿蒙页面。")
    android: str = Field(description="鸿蒙页面对应的安卓页面，而非组件。")


class BreakdownLayoutTranslation(CommonBaseModel):
    tasks: List[BreakdownLayoutTranslationTask] = Field(description="为实施整个计划而需要完成的任务列表。")


class BreakdownComponentTranslationTask(Task):
    component: str = Field(description="待翻译的安卓组件代码。")


class BreakdownComponentTranslation(CommonBaseModel):
    tasks: List[BreakdownComponentTranslationTask] = Field(description="为实施整个计划而需要完成的任务列表。")


class ChooseComponent(CommonBaseModel):
    components: List[str] = Field(description="选择的组件列表。")
    explanation: str = Field(description="选择组件的解释。")


class BreakdownAndroidLayoutComponent(CommonBaseModel):
    name: List[str] = Field(description="待转译的所有安卓组件名称。")
    content: str = Field(description="待转译的安卓组件布局代码。")
    description: str = Field(description="待转译的组件的描述。")


class BreakdownAndroidLayoutTask(Task):
    component: BreakdownAndroidLayoutComponent = Field(description="待翻译的安卓布局组件")


class BreakdownAndroidLayout(CommonBaseModel):
    tasks: List[BreakdownAndroidLayoutTask] = Field(description="为实施整个页面转译而需要完成的组件转译任务列表。")


class TranslateAndroidComponent(CommonBaseModel):
    android_component: str = Field(description="待转译的Android组件")
    harmony_component: str = Field(description="转译后的Harmony组件")
    harmony_component_description: str = Field(description="Harmony组件的描述")
    explanation: str = Field(description="转译过程的解释")


class Translation(CommonBaseModel):
    description: str = Field(description="转译任务的描述")

    source_component: str = Field(description="源组件")
    source_component_code: str = Field(description="源组件代码")
    source_component_description: str = Field(description="源组件描述")

    target_component: List[str] = Field(description="目标组件")
    target_component_code: str = Field(description="目标组件代码")
    target_component_description: str = Field(description="目标组件描述")

    explanation: str = Field(description="转译过程的解释")
