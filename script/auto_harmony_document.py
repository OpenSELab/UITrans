"""
给出鸿蒙组件文档的URL地址，自动生成鸿蒙组件结构化数据及示例

同步执行 get_llm_friendly_document 函数，获取大模型友好文档
异步执行 generate_component_document 函数，生成组件结构化文档
异步执行 generate_example_document 函数，生成组件示例文档
"""
import asyncio
import json
import os
import re
import time

import requests
import tqdm
from openai import OpenAI, AsyncOpenAI
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.component.schema import ComponentDeclaration

os.chdir(r"D:\Codes\Python\harmony-pilot")
ConfigLoader.from_file("./config.yaml")
llm_client_config = ConfigLoader.get_config().llm_config.get("deepseek")
llm_client = AsyncOpenAI(
    base_url=llm_client_config.base_url,
    api_key=llm_client_config.api_key
)


def extract_code_blocks(markdown_text):
    """从 Markdown 文本中提取代码块"""
    code_block_pattern = re.compile(r'```.*?\n(.*?)\n```', re.DOTALL)
    code_blocks = code_block_pattern.findall(markdown_text)
    return code_blocks


def replace_py_bool_none(text: str):
    """将文本中的 true/false/null 替换为 True/False/None"""
    return text.replace(": true", ": True").replace(": false", ": False").replace(": null", ": None")


def get_llm_friendly_document(url: str):
    """使用通过在线 JinaAI Reader 获得大模型友好文档
    当文档中出现 unifiedSearch.onlySearchAnchor，说明文档有错，需要重试
    """
    error_message = ["unifiedSearch.onlySearchAnchor"]
    tries_count = 0
    while True:
        response = requests.get(f"https://r.jina.ai/{url}")
        content = response.text
        # 没有出现错误信息并且文档长度大于512，通常文档的长度不会小于512，太短的文档可能是错误的
        if not any([msg in content for msg in error_message]) and len(content) > 512:
            # 不需要重试
            return content
        if tries_count > 3:
            # 重试次数过多
            raise Exception("重试次数过多, 请稍后重试")
        tries_count += 1
        print("get_llm_friendly_document 重试中...")
        time.sleep(1)


async def generate_component_document(document: str):
    """依据组件文档，通过大模型生成组件结构化文档"""
    system_message = """你是一个强大的人工智能对话助手，你需要提供简洁、正确、精确满足用户需要的答案。"""
    prompt = """请根据以下文档，按照要求和规则提取组件的JSON信息。
文档：
[[文档]]
规则：
* 1. 对于具有默认值的参数、属性，请使用**default**指出，并在描述中去除关于默认值的介绍；
* 2. 在组件的描述中指出对子组件的支持描述，例如"可以包含单个子组件。"、"ListItem、ListItemGroup"等，具体内容请参考文档；
* 3. 对于有多种type的情况，请使用数组而非`|`, 对于只有单个type的情况，不要使用数组而是直接使用字符串；
* 4. 默认值为空时可以忽略不写，当前API版本为12，对于版本12之前的默认值可以忽略；
* 5. 你必须严格遵守以下 JSON Schema，绝对不要出现 JSON Schema 中未定义的属性；

JSON Schema: {'properties': {'description': {'description': '组件的描述', 'title': 'Description', 'type': 'string'}, 'details': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'description': '组件的详细描述', 'title': 'Details'}, 'interfaces': {'description': '组件的接口', 'items': {'properties': {'description': {'description': '接口的描述', 'title': 'Description', 'type': 'string'}, 'params': {'additionalProperties': {'properties': {'type': {'anyOf': [{'type': 'string'}, {'items': {'anyOf': [{'type': 'string'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}]}, 'type': 'array'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}], 'description': '参数的类型', 'title': 'Type'}, 'required': {'default': False, 'description': '是否必填参数', 'title': 'Required', 'type': 'boolean'}, 'description': {'description': '参数的描述', 'title': 'Description', 'type': 'string'}, 'default': {'anyOf': [{}, {'type': 'null'}], 'default': None, 'description': '参数的默认值', 'title': 'Default'}}, 'required': ['type', 'description'], 'title': 'ComponentParam', 'type': 'object'}, 'description': '接口的参数', 'title': 'Params', 'type': 'object'}}, 'required': ['description', 'params'], 'title': 'ComponentInterface', 'type': 'object'}, 'title': 'Interfaces', 'type': 'array'}, 'attributes': {'additionalProperties': {'properties': {'description': {'description': '属性的描述', 'title': 'Description', 'type': 'string'}, 'params': {'additionalProperties': {'properties': {'type': {'anyOf': [{'type': 'string'}, {'items': {'anyOf': [{'type': 'string'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}]}, 'type': 'array'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}], 'description': '参数的类型', 'title': 'Type'}, 'required': {'default': False, 'description': '是否必填参数', 'title': 'Required', 'type': 'boolean'}, 'description': {'description': '参数的描述', 'title': 'Description', 'type': 'string'}, 'default': {'anyOf': [{}, {'type': 'null'}], 'default': None, 'description': '参数的默认值', 'title': 'Default'}}, 'required': ['type', 'description'], 'title': 'ComponentParam', 'type': 'object'}, 'description': '属性的参数', 'title': 'Params', 'type': 'object'}}, 'required': ['description', 'params'], 'title': 'ComponentAttribute', 'type': 'object'}, 'description': '组件的属性', 'title': 'Attributes', 'type': 'object'}, 'events': {'additionalProperties': {'properties': {'description': {'description': '事件的描述', 'title': 'Description', 'type': 'string'}, 'params': {'anyOf': [{'additionalProperties': {'properties': {'type': {'anyOf': [{'type': 'string'}, {'items': {'anyOf': [{'type': 'string'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}]}, 'type': 'array'}, {'additionalProperties': {'type': 'string'}, 'type': 'object'}], 'description': '参数的类型', 'title': 'Type'}, 'required': {'default': False, 'description': '是否必填参数', 'title': 'Required', 'type': 'boolean'}, 'description': {'description': '参数的描述', 'title': 'Description', 'type': 'string'}, 'default': {'anyOf': [{}, {'type': 'null'}], 'default': None, 'description': '参数的默认值', 'title': 'Default'}}, 'required': ['type', 'description'], 'title': 'ComponentParam', 'type': 'object'}, 'type': 'object'}, {'type': 'null'}], 'description': '事件回调的参数', 'title': 'Params'}, 'returns': {'anyOf': [{'additionalProperties': {'properties': {'type': {'description': '返回值的类型', 'title': 'Type', 'type': 'string'}, 'description': {'description': '返回值的描述', 'title': 'Description', 'type': 'string'}}, 'required': ['type', 'description'], 'title': 'ComponentEventReturn', 'type': 'object'}, 'type': 'object'}, {'properties': {'type': {'description': '返回值的类型', 'title': 'Type', 'type': 'string'}, 'description': {'description': '返回值的描述', 'title': 'Description', 'type': 'string'}}, 'required': ['type', 'description'], 'title': 'ComponentEventReturn', 'type': 'object'}, {'type': 'null'}], 'default': None, 'description': '事件回调的返回值', 'title': 'Returns'}}, 'required': ['description', 'params'], 'title': 'ComponentEvent', 'type': 'object'}, 'description': '组件的事件', 'title': 'Events', 'type': 'object'}, 'rules': {'anyOf': [{'items': {'type': 'string'}, 'type': 'array'}, {'type': 'null'}], 'default': None, 'description': '组件的使用规则', 'title': 'Rules'}, 'examples': {'anyOf': [{'items': {'type': 'string'}, 'type': 'array'}, {'type': 'null'}], 'default': None, 'description': '组件的使用示例', 'title': 'Examples'}, 'is_common_attrs': {'default': True, 'description': '是否支持通用属性', 'title': 'Is Common Attrs', 'type': 'boolean'}}, 'required': ['description', 'interfaces', 'attributes', 'events'], 'title': 'ComponentDeclaration', 'type': 'object'}

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

注意：不要给出任何前缀回答，例如“根据提供的文档和规则，以下是从文档中提取的组件的JSON信息”之类的内容。
    """.replace("[[文档]]", document)
    response_message_content = ""
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    request_count = 0
    while True:
        response = await llm_client.chat.completions.create(
            model=llm_client_config.model,
            messages=messages,
            max_tokens=4096,
            temperature=0.7
        )
        response_message_content = response.choices[0].message.content
        # stream = llm_client.chat.completions.create(
        #     model=llm_client_config.model,
        #     messages=messages,
        #     stream=True,
        #     max_tokens=4096,
        #     temperature=0.7
        # )
        # for chunk in stream:
        #     if chunk.choices[0].delta.content is not None:
        #         response_message_content += chunk.choices[0].delta.content
        #         print(chunk.choices[0].delta.content, end="")
        if response_message_content.startswith("```"):
            if not response_message_content.endswith("```"):
                # 输出不完整，可能是因为超过了最大长度限制，需要继续请求
                messages.append({"role": "assistant", "content": response_message_content})
                messages.append({"role": "user", "content": "请继续"})
                if request_count > 2:
                    # 请求次数过多
                    raise Exception("请求次数过多, 请稍后重试")
                request_count += 1
            else:
                # 输出完整
                response_message_content = extract_code_blocks(response_message_content)[0]
                break
        else:
            try:
                json.loads(response_message_content)
                break
            except Exception as e:
                # 输出不完整，可能是因为超过了最大长度限制，需要继续请求
                messages.append({"role": "assistant", "content": response_message_content})
                messages.append({"role": "user", "content": "请继续"})
                if request_count > 2:
                    # 请求次数过多
                    raise Exception("请求次数过多, 请稍后重试")
                request_count += 1
    # 理论上 response_message_content 应该是一个 JSON 字符串
    return response_message_content


async def generate_example_document(document: str):
    async def task(code_document: str):
        prompt = """你是一个专业的鸿蒙ArkUI开发者，你的任务是为示例代码编写详细的功能与效果描述、实现思路注释。
以下的组件文档，请你从中提取全部代码示例，并为其编写功能与效果描述、实现思路注释：
[[文档]]
在编写时你需要遵守以下规则：
* 1. 一个示例代码中可能含有多个功能块，你需要为每一个功能块编写功能与效果描述以及适当的注释，不需要指出功能块1、功能块2等。
* 2. 你需要尽可能为组件的属性、接口、事件等关键代码添加注释，例如代码的设计思路、实现细节等。
* 3. 对于关键的属性、方法、变量等，你需要给出其功能与效果描述以及适当的注释。
* 4. 功能与效果描述应该以注释的形式给出。
* 5. 实现思路应该以注释的形式给出，并将其编写在代码的起始位置。
* 6. 无需回答除了代码和注释以外的其他内容，包括解释、你的思路等等。
* 7. 请你尽可能地为每行代码添加注释。

以下是一个模板示例：
/*
{{ 实现思路 }}
{{ 总体功能与效果描述 }}
*/

// {{ 文件名，例如xxx.ets }}
{{ 代码，包括功能与效果描述注释、关键注释等 }}
"""
        example_prompt = prompt.replace("[[文档]]", code_document)
        example_document = ""
        example_message_content = ""
        request_count = 0
        messages = [
            {"role": "user", "content": example_prompt}
        ]
        while True:
            response = await llm_client.chat.completions.create(
                model=llm_client_config.model,
                messages=messages,
                max_tokens=4096,
                temperature=0.7
            )
            example_message_content = response.choices[0].message.content
            if example_message_content.startswith("```"):
                if not example_message_content.endswith("```"):
                    # 输出不完整，可能是因为超过了最大长度限制，需要继续请求
                    messages.append({"role": "assistant", "content": example_message_content})
                    messages.append({"role": "user", "content": "请继续"})
                    if request_count > 3:
                        # 请求次数过多
                        raise Exception("请求次数过多, 请稍后重试")
                    request_count += 1
                else:
                    example_document = extract_code_blocks(example_message_content)[0]
                    break
            else:
                example_document = example_message_content
                break
        return example_document.replace("\n", "\\n")

    example_pattern = re.compile("示例\d*\n([\s\S]*?)(?=\n\!\[Image|\Z)", re.DOTALL)
    all_examples = example_pattern.findall(document)
    async_tasks = []
    for example in all_examples:
        async_tasks.append(task(example))
    example_documents = []
    for coro in tqdm.tqdm(asyncio.as_completed(async_tasks), total=len(async_tasks), desc="生成示例文档"):
        result = await coro
        example_documents.append(result)
    return example_documents


async def generate_component_declaration(url: str):
    """生成组件声明数据文档，包括组件结构化数据、示例文档等
    同步执行 get_llm_friendly_document 函数，获取大模型友好文档
    异步执行 generate_component_document 函数，生成组件结构化文档
    异步执行 generate_example_document 函数，生成组件示例文档
    最终合并组件结构化数据
    """
    async_tasks = []
    component_filename = url.split("/")[-1]
    component_dir = f"script/auto_harmony_component/{component_filename}"
    os.makedirs(component_dir, exist_ok=True)
    print("================= 获取组件文档 =================")
    component_document_filepath = f"{component_dir}/{component_filename}.document"
    if os.path.exists(component_document_filepath):
        with open(component_document_filepath, "r", encoding="utf-8") as f:
            component_document = f.read()
    else:
        component_document = get_llm_friendly_document(url)
        with open(component_document_filepath, "w", encoding="utf-8") as f:
            f.write(component_document)
    print("================= 获取组件文档完成 =================")

    async def generate_component_document_task():
        print("================= 生成组件结构化文档 =================")
        component_structure_document_filepath = f"{component_dir}/{component_filename}.structure_document"
        if os.path.exists(component_structure_document_filepath):
            with open(component_structure_document_filepath, "r", encoding="utf-8") as f:
                component_structure_document = f.read()
        else:
            component_structure_document = await generate_component_document(component_document)
            with open(component_structure_document_filepath, "w", encoding="utf-8") as f:
                f.write(component_structure_document)
        print("================= 生成组件结构化完成 =================")
        return component_structure_document

    async_tasks.append(generate_component_document_task())

    async def generate_example_document_task():
        print("================= 生成组件示例文档 =================")
        component_examples_filepath = f"{component_dir}/{component_filename}.examples"
        if os.path.exists(component_examples_filepath):
            with open(component_examples_filepath, "r", encoding="utf-8") as f:
                component_examples = f.read().split("\n\n\n")
        else:
            component_examples = await generate_example_document(component_document)
            with open(component_examples_filepath, "w", encoding="utf-8") as f:
                f.write("\n\n\n".join(component_examples))
        print("================= 生成组件示例文档完成 =================")
        return component_examples

    async_tasks.append(generate_example_document_task())
    # 等待异步任务完成
    component_structure_document, component_examples = await asyncio.gather(*async_tasks)
    print("================= 合并组件结构化数据 =================")
    component_structure = json.loads(component_structure_document)
    component_structure["examples"] = component_examples
    try:
        # 验证数据是否符合组件声明的数据结构
        component_declaration_filepath = f"{component_dir}/{component_filename}.declaration"
        component_declaration = ComponentDeclaration(**component_structure)
        with open(component_declaration_filepath, "w", encoding="utf-8") as f:
            f.write(json.dumps(component_declaration.model_dump(), ensure_ascii=False, indent=4))
        # os.remove(component_document_filepath)
        # os.remove(component_structure_document_filepath)
        # os.remove(component_examples_filepath)
        print("================= 组件结构化数据生成结束 =================")
    except Exception as e:
        print(f"组件文档提取失败: {e}")


if __name__ == '__main__':
    urls = [
        "https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ohos-arkui-advanced-toolbar-V5"
    ]
    for url in urls:
        asyncio.run(generate_component_declaration(url))