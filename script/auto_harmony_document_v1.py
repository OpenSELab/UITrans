import os
import json
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

import requests
import tqdm
from openai import OpenAI

from core.config.config_loader import ConfigLoader

os.chdir("../")

ConfigLoader.from_file("./config.yaml")
llm_client_config = ConfigLoader.get_config().llm_config.get("deepseek")
llm_client = OpenAI(
    base_url=llm_client_config.base_url,
    api_key=llm_client_config.api_key
)
jina_api_key = "jina_988aca41347e4c05bf90408c61584c63mH4-B4sFWfalolJ6ons2Uy7N5kcD"


def extract_code_blocks(markdown_text):
    """从 Markdown 文本中提取代码块"""
    code_block_pattern = re.compile(r'```.*?\n(.*?)\n```', re.DOTALL)
    code_blocks = code_block_pattern.findall(markdown_text)
    if len(code_blocks) == 0:
        return [markdown_text]
    return code_blocks


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


def get_llm_friendly_document(url: str):
    """使用通过在线 JinaAI Reader 获得大模型友好文档
    当文档中出现 unifiedSearch.onlySearchAnchor等，说明文档有错，需要重试
    """
    headers = {
        "Authorization": f"Bearer {jina_api_key}"
    }
    error_message = ["unifiedSearch.onlySearchAnchor", "DOC.onlySearch", "DOC.searchTips",
                     "DOC.onlySearchunifiedSearch.onlySearchAnchor", "unifiedSearch.search"]
    tries_count = 0
    while True:
        response = requests.get(f"https://r.jina.ai/{url}", headers=headers)
        content = response.text
        # 没有出现错误信息并且文档长度大于512，通常文档的长度不会小于512，太短的文档可能是错误的
        if not any([msg in content for msg in error_message]) and len(content) > 512:
            # 不需要重试
            return content
        if tries_count > 3:
            # 重试次数过多
            # raise Exception("重试次数过多, 请稍后重试")
            print("重试次数过多, 请稍后重试")
            time.sleep(10)
        if "Slow down, turbo! You've hit the rate limit (requests per minute per IP address" in content:
            print("请求频率过快，等待60s")
            time.sleep(60)
        else:
            print("get_llm_friendly_document 重试中...")
            tries_count += 1
            time.sleep(5)


def generate_component_structure_document(document: str):
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
当你的答案不完整时，你不可以闭合代码块，直到你的答案完整为止。
    """.replace("[[文档]]", document)
    total_response_message_content = ""
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    request_count = 0
    is_continue = False
    while True:
        response = llm_client.chat.completions.create(
            model=llm_client_config.model,
            messages=messages,
            max_tokens=4096,
            temperature=0.7
        )
        # 响应结果
        response_message_content = response.choices[0].message.content
        if response_message_content.startswith("```"):
            # 若输出结果为 Markdown 但未闭合，则继续请求
            if not response_message_content.endswith("```"):
                # 输出不完整，可能是因为超过了最大长度限制，需要继续请求
                messages.append({"role": "assistant", "content": response_message_content})
                messages.append({"role": "user", "content": "请继续"})
                total_response_message_content += response_message_content
                is_continue = True
                if request_count > 2:
                    # 请求次数过多
                    raise Exception("请求次数过多, 请稍后重试")
                request_count += 1
            else:
                if is_continue:
                    total_response_message_content += response_message_content
                    total_response_message_content = extract_code_blocks(total_response_message_content)[0]
                else:
                    # 输出完整
                    total_response_message_content = extract_code_blocks(response_message_content)[0]
                break
        else:
            try:
                # 尝试解析，若成功解析则退出
                json.loads(response_message_content)
                total_response_message_content = response_message_content
                break
            except Exception as e:
                # 输出不完整，可能是因为超过了最大长度限制，需要继续请求
                messages.append({"role": "assistant", "content": response_message_content})
                messages.append({"role": "user", "content": "请继续"})
                total_response_message_content += response_message_content
                is_continue = True
                if request_count > 2:
                    # 请求次数过多
                    raise Exception("请求次数过多, 请稍后重试")
                request_count += 1
    # 理论上 response_message_content 应该是一个 JSON 字符串
    return total_response_message_content


def _extract_examples_from_component_document(document: str):
    example_pattern = re.compile("示例\d*\n+([\s\S]*?)(?=\n\!\[|\Z)", re.DOTALL)
    examples = example_pattern.findall(document)
    return examples


def generate_component_examples(document: str):
    """依据组件文档，通过大模型生成组件示例"""

    def inner_task(code_document):
        example_pattern = r"/\*(.*?)\*/(.*)"
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

组件功能、布局、样式描述示例：
该组件通过 Flex 布局实现了一个展示多种类型按钮（如普通按钮、胶囊按钮、圆形按钮）及其状态效果的界面。布局宽度占据整个屏幕，高度设为 400vp，内边距为左右 35vp、顶部 35vp。组件的垂直方向上被分为多个部分，每个部分包含一个标题和一组按钮。每个按钮组的按钮以水平布局方式排列，按钮之间的间距均匀分布，且对齐方式为居中对齐。
按钮的样式包括背景颜色、边框圆角（或半径）、宽度和高度等属性，支持不同的样式展示。按钮组之间通过 Flex 组件进行分隔。按钮的功能包括点击事件和状态效果，用户可以通过点击按钮触发相应操作，按钮也可以在启用或禁用状态下进行展示。
整个布局通过 Flex 布局保证按钮在垂直方向上有序排列，确保界面整洁美观。

以下是模板：
/*
{{ 布局、样式及功能与效果描述，需要替换为具体的描述内容。 }}
*/

{{ 代码，包括功能与效果描述注释、关键注释等 }}

/*
布局、样式及功能与效果描述，需要替换为具体的描述内容。
*/

代码，包括功能与效果描述注释、关键注释等
""".replace("[[文档]]", code_document)
        request_count = 0
        messages = [
            {"role": "user", "content": prompt}
        ]
        while True:
            response = llm_client.chat.completions.create(
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
        match = re.search(example_pattern, example_document, re.DOTALL)
        if match:
            description = match.group(1).strip()
            code = match.group(2).strip()
            return {
                "description": description,
                "code": code
            }
        else:
            return {
                "description": "",
                "code": example_document
            }

    examples = _extract_examples_from_component_document(document)
    if len(examples) == 0:
        return []
    with ThreadPoolExecutor(max_workers=len(examples)) as executor:
        tasks = [executor.submit(inner_task, example) for example in examples]
        results = [task.result() for task in as_completed(tasks)]
    return results


def only_generate_example_description(code_examples: List[str]):
    def inner_task(code_document):
        example_pattern = r"/\*(.*?)\*/(.*)"
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
""".replace("[[文档]]", code_document)
        request_count = 0
        messages = [
            {"role": "user", "content": prompt}
        ]
        while True:
            response = llm_client.chat.completions.create(
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
        match = re.search(example_pattern, example_document, re.DOTALL)
        if match:
            description = match.group(1).strip()
            return {
                "description": description,
                "code": code_document
            }
        else:
            return {
                "description": example_document,
                "code": code_document
            }

    with ThreadPoolExecutor(max_workers=len(code_examples)) as executor:
        tasks = [executor.submit(inner_task, example) for example in code_examples]
        results = [task.result() for task in as_completed(tasks)]
    return results


def auto_harmony_document():
    existed_harmony_component_filepath = "script/auto_harmony_document/components_back.json"
    if not os.path.exists(existed_harmony_component_filepath):
        with open("script/auto_harmony_document/components_back.json", "r", encoding="utf-8") as f:
            components = json.load(f)
    else:
        components = {}

    def inner_task(component_name, component_url):
        component_identifier = component_url.split("/")[-1]
        document_filepath = f"script/auto_harmony_document/{component_identifier}/{component_identifier}.document"
        examples_filepath = f"script/auto_harmony_document/{component_identifier}/{component_identifier}.examples.json"
        structure_document_filepath = f"script/auto_harmony_document/{component_identifier}/{component_identifier}.structure_document.json"
        declaration_filepath = f"script/auto_harmony_document/{component_identifier}/{component_identifier}.declaration.json"
        if not os.path.exists(document_filepath):
            raise Exception(f"组件 {component_name} 的文档不存在")
        with open(document_filepath, "r", encoding="utf-8") as f:
            component_document = f.read()
        # ----------------------------- 生成示例文档 -----------------------------
        print(f"获取组件 {component_name} 的示例文档")
        if not os.path.exists(examples_filepath):
            # 首先从文档中读取，若有则直接写入
            if component_name in components and "examples" in components[component_name] and components[component_name][
                "examples"]:
                if isinstance(components[component_name]["examples"][0], dict):
                    component_examples = only_generate_example_description([
                        example["code"] for example in components[component_name]["examples"]
                    ])
                    try:
                        with open(examples_filepath, "w", encoding="utf-8") as f:
                            json.dump(component_examples, f, ensure_ascii=False, indent=4)
                    except Exception as e:
                        print(f"组件 {component_name} 的示例文档写入失败: {e}")
                        with open(examples_filepath + ".temp", "w", encoding="utf-8") as f:
                            for example in component_examples:
                                f.write(str(example) + "\n")
                else:
                    raise Exception(f"组件 {component_name} 的示例非字典，需要更新")
            # 从文档中提取示例
            else:
                component_examples = generate_component_examples(component_document)
                try:
                    with open(examples_filepath, "w", encoding="utf-8") as f:
                        json.dump(component_examples, f, ensure_ascii=False, indent=4)
                except Exception as e:
                    print(f"组件 {component_name} 的示例文档写入失败: {e}")
                    with open(examples_filepath + ".temp", "w", encoding="utf-8") as f:
                        for example in component_examples:
                            f.write(str(example) + "\n")
        # ----------------------------- 生成结构化文档 -----------------------------
        print(f"获取组件 {component_name} 的结构化文档")
        if not os.path.exists(structure_document_filepath):
            # 首先从文档中读取，若有则直接写入
            if component_name in components:
                structure_document_dict = components[component_name]
                if "examples" in structure_document_dict:
                    del structure_document_dict["examples"]
                try:
                    with open(structure_document_filepath, "w", encoding="utf-8") as f:
                        json.dump(structure_document_dict, f, ensure_ascii=False, indent=4)
                except Exception as e:
                    print(f"组件 {component_name} 的结构化文档写入失败: {e}")
                    with open(structure_document_filepath + ".temp", "w", encoding="utf-8") as f:
                        f.write(str(structure_document_dict))
            else:
                structure_document = generate_component_structure_document(component_document)
                try:
                    with open(structure_document_filepath, "w", encoding="utf-8") as f:
                        f.write(structure_document)
                        # json.dump(json.loads(structure_document_filepath), f, ensure_ascii=False, indent=4)
                except Exception as e:
                    print(f"组件 {component_name} 的结构化文档写入失败: {e}")
                    with open(structure_document_filepath + ".temp", "w", encoding="utf-8") as f:
                        f.write(str(structure_document))
        # ----------------------------- 生成组件声明文档 -----------------------------
        print(f"获取组件 {component_name} 的声明文档")
        if not os.path.exists(declaration_filepath):
            if component_name in components:
                declaration_dict = components[component_name]
            else:
                try:
                    with open(structure_document_filepath, "r", encoding="utf-8") as f:
                        declaration_dict = json.load(f)
                except Exception as e:
                    raise Exception(f"组件 {component_name} 的结构化文档读取失败: {e}")
            if os.path.exists(examples_filepath):
                try:
                    with open(examples_filepath, "r", encoding="utf-8") as f:
                        component_examples = json.load(f)
                    declaration_dict["examples"] = component_examples
                except Exception as e:
                    raise Exception(f"组件 {component_name} 的示例文档读取失败: {e}")
            try:
                with open(declaration_filepath, "w", encoding="utf-8") as f:
                    json.dump(declaration_dict, f, ensure_ascii=False, indent=4)
            except Exception as e:
                print(f"组件 {component_name} 的声明文档写入失败: {e}")
                with open(declaration_filepath + ".temp", "w", encoding="utf-8") as f:
                    f.write(str(declaration_dict))

    auto_harmony_document_filepath = "script/auto_harmony_document/auto_harmony_document.txt"
    auto_harmony_document_error_filepath = "script/auto_harmony_document/auto_harmony_document.error"
    if os.path.exists(auto_harmony_document_filepath):
        with open(auto_harmony_document_filepath, "r", encoding="utf-8") as f:
            existed_harmony_document = f.read().split("\n")
    else:
        existed_harmony_document = []

    error_components = []
    if os.path.exists(auto_harmony_document_error_filepath):
        with open(auto_harmony_document_error_filepath, "r", encoding="utf-8") as f:
            for error_component in f.read().split("\n"):
                error_component_name = error_component.split(":", maxsplit=1)[0]
                error_components.append(error_component_name)

    components_url = load_components_url()

    tasks = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        for component_name, component_url in components_url.items():
            if component_name in existed_harmony_document:
                continue
            if component_name in error_components:
                continue
            future = executor.submit(inner_task, component_name, component_url)
            tasks[future] = component_name

        for future in tqdm.tqdm(as_completed(tasks), total=len(tasks), desc="处理组件"):
            component_name = tasks[future]
            try:
                future.result()
                with open(auto_harmony_document_filepath, "a", encoding="utf-8") as f:
                    f.write(f"{component_name}\n")
            except Exception as e:
                with open(auto_harmony_document_error_filepath, "a", encoding="utf-8") as f:
                    f.write(f"{component_name}:{e}\n")
                print(f"组件 {component_name} 处理失败: {e}")


def create_total_components_document():
    components = {}
    components_url = load_components_url()
    auto_harmony_document_error_filepath = "script/auto_harmony_document/auto_harmony_document.error"
    error_components = []
    if os.path.exists(auto_harmony_document_error_filepath):
        with open(auto_harmony_document_error_filepath, "r", encoding="utf-8") as f:
            for error_component in f.read().split("\n"):
                error_component_name = error_component.split(":", maxsplit=1)[0]
                error_components.append(error_component_name)
    for component_name, component_url in components_url.items():
        if component_name in error_components:
            print(f"跳过组件 {component_name}")
        component_identifier = component_url.split("/")[-1]
        declaration_filepath = f"script/auto_harmony_document/{component_identifier}/{component_identifier}.declaration.json"
        if os.path.exists(declaration_filepath):
            with open(declaration_filepath, "r", encoding="utf-8") as f:
                component_declaration = json.load(f)
            components[component_name] = component_declaration
    with open("script/auto_harmony_document/components.json", "w", encoding="utf-8") as f:
        json.dump(components, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # auto_harmony_document()
    create_total_components_document()
