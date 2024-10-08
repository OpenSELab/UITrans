"""
给出鸿蒙组件文档的URL地址，自动生成鸿蒙组件结构化数据及示例

同步执行 get_llm_friendly_document 函数，获取大模型友好文档
异步执行 generate_component_document 函数，生成组件结构化文档
异步执行 generate_example_document 函数，生成组件示例文档
"""
import asyncio
import concurrent.futures
import json
import os
import re
import time
from typing import List

import requests
import tqdm
from openai import OpenAI, AsyncOpenAI
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.component.schema import ComponentDeclaration

os.chdir("../")
ConfigLoader.from_file("./config.yaml")
llm_client_config = ConfigLoader.get_config().llm_config.get("deepseek")
llm_client = AsyncOpenAI(
    base_url=llm_client_config.base_url,
    api_key=llm_client_config.api_key
)

jina_api = "jina_ad1ff673a51041ec921a79484ff20f12ZzHuOAyTn33Ncve9ns4jaNxOF035"


def parse_arkui_response():
    with open("script/auto_harmony_document/arkui_tree.json", "r", encoding="utf-8") as f:
        arkui_tree = json.loads(f.read())

    # 行列与堆叠、栅格与分栏、滚动与滑动、导航与切换、按钮与选择、文本与输入、图片与视频、信息展示、空白与分隔、画布绘制、图形绘制
    focus_titles = ["行列与堆叠", "栅格与分栏", "滚动与滑动", "导航与切换", "按钮与选择", "文本与输入", "图片与视频",
                    "信息展示", "空白与分隔", "画布绘制", "图形绘制", "渲染绘制", "标题栏与工具栏", "菜单", "弹窗", "原子化服务", "安全", "状态管理与渲染控制", "主题"]
    base_url = "https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/"

    def has_chinese_char(s):
        for c in s:
            if '\u4e00' <= c <= '\u9fa5':
                return True
        return False

    with open("script/auto_harmony_document/harmony-component-urls.txt", "w", encoding="utf-8") as f:
        for title_node in arkui_tree["children"]:
            title_name = title_node["nodeName"]
            if title_name not in focus_titles:
                continue
            f.write("# " + title_name + "\n")
            for node in title_node["children"]:
                node_name = node["nodeName"]
                if title_name == "弹窗":
                    node_name = re.findall(r"[a-zA-Z]+", node_name)[0]
                if has_chinese_char(node_name):
                    # 非组件
                    continue
                relate_document_url = base_url + node["relateDocument"]
                f.write(node_name + ":" + relate_document_url + "\n")


def dumps_components():
    """将字典格式的组件信息转换为json格式并写入文件
    """
    from core.pilot.harmony.component.defs.advanced_component import ADVANCED_COMPONENT
    from core.pilot.harmony.component.defs.basic_component import BASIC_COMPONENT
    from core.pilot.harmony.component.defs.canvas_component import CANVAS_COMPONENT
    from core.pilot.harmony.component.defs.container_component import CONTAINER_COMPONENT
    from core.pilot.harmony.component.defs.drawing_component import DRAWING_COMPONENT
    from core.pilot.harmony.component.defs.global_component import GLOBAL_COMPONENT
    from core.pilot.harmony.component.defs.media_component import MEDIA_COMPONENT
    from core.pilot.harmony.component.defs.safe_component import SAFE_COMPONENT

    total_component = {
        **BASIC_COMPONENT,
        **CANVAS_COMPONENT,
        **CONTAINER_COMPONENT,
        **DRAWING_COMPONENT,
        **GLOBAL_COMPONENT,
        **MEDIA_COMPONENT,
        **SAFE_COMPONENT,
        **ADVANCED_COMPONENT
    }

    with open("script/auto_harmony_document/components_back.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(total_component, ensure_ascii=False, indent=2))


def load_components_declare():
    """加载组件的声明信息
    """
    with open("script/auto_harmony_document/components_back.json", "r", encoding="utf-8") as f:
        components_declare = json.loads(f.read())
    return components_declare


def load_components_url():
    """加载组件的url信息
    """
    with open("script/auto_harmony_document/harmony-component-urls.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        components_url = {}
        for line in lines:
            if line.startswith("#"):
                # 标题
                continue
            else:
                name, url = line.split(":", maxsplit=1)
                components_url[name] = url.strip()
    return components_url


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
    headers = {
        "Authorization": f"Bearer {jina_api}"
    }
    error_message = ["unifiedSearch.onlySearchAnchor", "DOC.onlySearch", "DOC.searchTips",
                     "DOC.onlySearchunifiedSearch.onlySearchAnchor", "unifiedSearch.search"]
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
        print(content)
        time.sleep(5)


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
    total_response_message_content = ""
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
                total_response_message_content += response_message_content
                if request_count > 2:
                    # 请求次数过多
                    raise Exception("请求次数过多, 请稍后重试")
                request_count += 1
            else:
                # 输出完整
                total_response_message_content = extract_code_blocks(response_message_content)[0]
                break
        else:
            try:
                json.loads(response_message_content)
                break
            except Exception as e:
                # 输出不完整，可能是因为超过了最大长度限制，需要继续请求
                messages.append({"role": "assistant", "content": response_message_content})
                messages.append({"role": "user", "content": "请继续"})
                total_response_message_content += response_message_content
                if request_count > 2:
                    # 请求次数过多
                    raise Exception("请求次数过多, 请稍后重试")
                request_count += 1
    # 理论上 response_message_content 应该是一个 JSON 字符串
    return total_response_message_content


async def generate_example_document(document: str):
    async def task(code_document: str):
        prompt = """你是一个专业的鸿蒙ArkUI开发者，你的任务是帮助我分析并详细解释这个示例的功能与用法以及组件功能、布局、样式描述。
[[文档]]
在编写时你需要遵守以下规则：
* 1. 你需要尽可能为组件的属性、接口、事件等关键代码添加注释，例如代码的设计思路、实现细节等。
* 2. 对于关键的属性、方法、变量等，你需要给出其功能与效果描述以及适当的注释。
* 3. 布局、样式及功能与效果描述应该以注释的形式给出，并将其编写在代码的起始位置。
* 4. 无需回答除了代码和注释以外的其他内容，包括解释、你的思路等等。
* 5. 请你尽可能地为每行代码添加注释。

**重要**：你编写的鸿蒙组件功能、布局、样式描述需要详细，使用段落的形式。
**重要**：组件功能、布局、样式描述需要涵盖以下方面：布局属性（如宽度、高度、边距等）、组件的样式和外观（如颜色、字体、透明度等）、组件的排列和嵌套关系（如垂直或水平布局、对齐方式）、组件的功能和交互（如点击事件、输入验证），当涉及到自定义背景、颜色等时需要指出资源名。
这是一个组件功能、布局、样式描述示例：“通过 Column 布局实现了一个包含图像按钮的界面，用于在应用中创建一个按钮界面。布局的宽度占据整个屏幕，高度也为 100%，内部包含一个 Button 组件。按钮内部包含一个 Image 组件，图像资源通过 $r("app.media.img02") 进行设置，图像适应方式为 ImageFit.Contain。按钮的内边距为 16vp。用户可以通过点击按钮触发相应的操作。整个布局使用了 Column 布局来确保按钮在垂直方向上排列。”

以下是模板：
/*
{{ 布局、样式及功能与效果描述，需要替换为具体的描述内容。 }}
*/

{{ 代码，包括功能与效果描述注释、关键注释等 }}
"""
        example_prompt = prompt.replace("[[文档]]", code_document)
        example_document = ""
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
                    example_document += example_message_content
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

    example_pattern = re.compile("示例\d*\n+([\s\S]*?)(?=\n\!\[|\Z)", re.DOTALL)
    all_examples = example_pattern.findall(document)
    async_tasks = []
    for example in all_examples:
        async_tasks.append(task(example))
    example_documents = []
    for coro in tqdm.tqdm(asyncio.as_completed(async_tasks), total=len(async_tasks), desc="生成示例文档"):
        result = await coro
        example_documents.append(result)
    return example_documents


async def generate_example_document_v1(all_examples: List[str]):
    async def task(code_document: str):
        prompt = """你是一个专业的鸿蒙ArkUI开发者，你的任务是帮助我分析并详细解释这个示例的功能与用法。
[[文档]]
在编写时你需要遵守以下规则：
* 1. 你需要尽可能为组件的属性、接口、事件等关键代码添加注释，例如代码的设计思路、实现细节等。
* 2. 对于关键的属性、方法、变量等，你需要给出其功能与效果描述以及适当的注释。
* 3. 布局、样式及功能与效果描述应该以注释的形式给出，并将其编写在代码的起始位置。
* 4. 无需回答除了代码和注释以外的其他内容，包括解释、你的思路等等。
* 5. 请你尽可能地为每行代码添加注释。

以下是模板：
/*
{{ 布局、样式及功能与效果描述，需要替换为具体的描述内容，例如“实现一个可滚动的列表组件，支持上拉加载更多功能。” }}
*/

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
    component_dir = f"script/auto_harmony_document/{component_filename}"
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
        return ""
        print("================= 生成组件结构化文档 =================")
        component_structure_document_filepath = f"{component_dir}/{component_filename}.structure_document"
        if os.path.exists(component_structure_document_filepath):
            with open(component_structure_document_filepath, "r", encoding="utf-8") as f:
                component_structure_document = f.read()
        else:
            component_structure_document = await generate_component_document(component_document)
            with open(component_structure_document_filepath, "w", encoding="utf-8") as f:
                f.write(component_structure_document)
        print("================= 生成组件结构化文档完成 =================")
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


def update_component_examples_task(component_name, component_url: str):
    component_filename = component_url.split("/")[-1]
    component_dir = f"script/auto_harmony_document/{component_filename}"
    component_document_filepath = f"{component_dir}/{component_filename}.document"
    example_description_pattern = re.compile("(?s)(.*?)(?=@Entry|import)(.*)")
    os.makedirs(os.path.dirname(component_document_filepath), exist_ok=True)
    components_declare = load_components_declare()
    # 生成组件示例文档
    component_examples_filepath = f"{component_dir}/{component_filename}.examples"
    if os.path.exists(component_examples_filepath):
        with open(component_examples_filepath, "r", encoding="utf-8") as f:
            component_examples = f.read().split("\n\n\n")
    else:
        if component_name in components_declare and "examples" in components_declare[component_name] and components_declare[component_name]["examples"]:
            if isinstance(components_declare[component_name]["examples"][0], dict):
                return components_declare[component_name]["examples"]
            component_examples = []
            for component_example in components_declare[component_name]["examples"]:
                match_result = example_description_pattern.search(component_example)
                if match_result:
                    example_description = match_result.group(1).strip()
                    example_code = match_result.group(2).strip()
                    component_examples.append(example_code)
                else:
                    print(f"组件 {component_name} 示例文档提取失败")
            component_examples = asyncio.run(generate_example_document_v1(component_examples))
        else:
            # 获取组件文档
            if os.path.exists(component_document_filepath):
                with open(component_document_filepath, "r", encoding="utf-8") as f:
                    component_document = f.read()
            else:
                component_document = get_llm_friendly_document(component_url)
                with open(component_document_filepath, "w", encoding="utf-8") as f:
                    f.write(component_document)
            component_examples = asyncio.run(generate_example_document(component_document))
        with open(component_examples_filepath, "w", encoding="utf-8") as f:
            f.write("\n\n\n".join(component_examples))

    final_examples = []
    for i, example in enumerate(component_examples):
        example = example.replace("\\n", "\n")
        match_result = example_description_pattern.search(example)
        if match_result:
            example_description = match_result.group(1).strip()
            example_code = match_result.group(2).strip()

            temp_example_description_lines = []
            for line in example_description.split("\n"):
                line = line.replace("//", "").replace("/*", "").replace("*/", "").replace("xxx.ets", "").strip()
                if len(line) == 0:
                    continue
                temp_example_description_lines.append(line)
            example_description = "\n".join(temp_example_description_lines)
            final_examples.append({
                "description": example_description,
                "code": example_code
            })
    return final_examples

async def only_generate_example_description_v1(all_examples):
    async def task(code_document: str):
        prompt = """你是一个专业的鸿蒙ArkUI开发者，你的任务是帮助我分析并详细解释这个示例的功能与用法以及组件功能、布局、样式描述。
[[文档]]

在编写时你需要遵守以下规则：
* 1. 你编写的鸿蒙组件功能、布局、样式描述需要详细，使用段落的形式。
* 2. 不需要给出代码，只需要给出功能与效果描述即可。

**重要**：你编写的鸿蒙组件功能、布局、样式描述需要详细，使用段落的形式。
**重要**：组件功能、布局、样式描述需要涵盖以下方面：布局属性（如宽度、高度、边距等）、组件的样式和外观（如颜色、字体、透明度等）、组件的排列和嵌套关系（如垂直或水平布局、对齐方式）、组件的功能和交互（如点击事件、输入验证），当涉及到自定义背景、颜色等时需要指出资源名。

示例1：
通过 Column 布局实现了一个包含图像按钮的界面，用于在应用中创建一个按钮界面。布局的宽度占据整个屏幕，高度也为 100%，内部包含一个 Button 组件。按钮内部包含一个 Image 组件，图像资源通过 $r("app.media.img02") 进行设置，图像适应方式为 ImageFit.Contain。按钮的内边距为 16vp。用户可以通过点击按钮触发相应的操作。整个布局使用了 Column 布局来确保按钮在垂直方向上排列。
示例2：
该组件通过 Flex 布局实现了一个展示多种类型按钮（如普通按钮、胶囊按钮、圆形按钮）及其状态效果的界面。布局宽度占据整个屏幕，高度设为 400vp，内边距为左右 35vp、顶部 35vp。组件的垂直方向上被分为多个部分，每个部分包含一个标题和一组按钮。每个按钮组的按钮以水平布局方式排列，按钮之间的间距均匀分布，且对齐方式为居中对齐。
按钮的样式包括背景颜色、边框圆角（或半径）、宽度和高度等属性，支持不同的样式展示。按钮组之间通过 Flex 组件进行分隔。按钮的功能包括点击事件和状态效果，用户可以通过点击按钮触发相应操作，按钮也可以在启用或禁用状态下进行展示。
整个布局通过 Flex 布局保证按钮在垂直方向上有序排列，确保界面整洁美观。

以下是模板：
/*
{{ 布局、样式及功能与效果描述，需要替换为具体的描述内容，以段落的形式。 }}
*/
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

    async_tasks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(all_examples)) as executor:
        futures = {}
        for i, example in enumerate(all_examples):
            future = executor.submit(task, example)
            futures[future] = i

        for future in tqdm.tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="生成示例描述文档"):
            i = futures[future]
            example_document = future.result()
            all_examples[i] = example_document

    for example in all_examples:
        async_tasks.append(task(example))
    example_documents = []
    for coro in tqdm.tqdm(asyncio.as_completed(async_tasks), total=len(async_tasks), desc="生成示例文档"):
        result = await coro
        example_documents.append(result)
    return example_documents


def update_component_examples():
    components_url = load_components_url()

    def update_document_example(component_name, examples):
        components_declare = load_components_declare()
        if component_name in components_declare:
            components_declare[component_name]["examples"] = examples
            with open("script/auto_harmony_document/components_back.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(components_declare, ensure_ascii=False, indent=2))
            with open("script/auto_harmony_document/update_component_examples.txt", "a", encoding="utf-8") as f:
                f.write(f"{component_name}\n")
        else:
            with open("script/auto_harmony_document/update_component_examples_error.txt", "a", encoding="utf-8") as f:
                f.write(f"{component_name}\n")

    if os.path.exists("script/auto_harmony_document/update_component_examples.txt"):
        with open("script/auto_harmony_document/update_component_examples.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if line:
                    del components_url[line]

    if os.path.exists("script/auto_harmony_document/update_component_examples_error.txt"):
        os.remove("script/auto_harmony_document/update_component_examples_error.txt")

    # for component_name, component_url in tqdm.tqdm(components_url.items(), total=len(components_url), desc="更新组件示例文档"):
    #     final_examples = update_component_examples_task(component_name, component_url)
    #     update_document_example(component_name, final_examples)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {}
        for component_name, component_url in components_url.items():
            future = executor.submit(update_component_examples_task, component_name, component_url)
            futures[future] = component_name

        for future in tqdm.tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="更新组件示例文档"):
            component_name = futures[future]
            try:
                final_examples = future.result()
                update_document_example(component_name, final_examples)
            except Exception as e:
                print(f"Task failed with error: {e}")


if __name__ == '__main__':
    # urls = [
    #     # TODO: 该组件文档存在问题的
    #     # "https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-canvasrenderingcontext2d-V5",
    #     # "https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-container-relativecontainer-V5"
    #     "https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-textinput-V5"
    # ]
    # for url in urls:
    #     asyncio.run(generate_component_declaration(url))
    update_component_examples()
    # parse_arkui_response()