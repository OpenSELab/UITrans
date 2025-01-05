import os
import re
import shutil
import stat
import subprocess
import zipfile

from lxml import etree
from pyparsing import Word, alphas, alphanums, Suppress, Group, delimitedList, QuotedString, Literal, SkipTo

from android.base import simple_components
import pandas as pd
import json


def extract_last(text):
    # last_dot_index = text.rfind('.')
    #
    # if last_dot_index != -1:
    #     return text[last_dot_index + 1:]
    # else:
    #     return text
    match = re.search(r'[./]([^./]*)$', text)
    if match:
        return match.group(1)
    else:
        return text


def transform_to_xml_filename(name, type):
    if type not in ['activity', 'fragment']:
        raise ValueError("Invalid code_type. Expected 'activity' or 'fragment'.")
    underscored_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    if underscored_name.endswith(f'_{type}'):
        underscored_name = underscored_name[:-len(f'_{type}')]
    xml_filename = f"{type}_{underscored_name}.xml"
    return xml_filename


def read_file(f_path):
    try:
        with open(f_path, 'r', encoding='utf-8') as file:
            source_code = file.read()
            return source_code
    except FileNotFoundError:
        print(f"文件 {f_path} 未找到！")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")


def find_file(base_path, file_name):
    base_path = os.path.abspath(base_path)

    for root, dirs, files in os.walk(base_path):
        if file_name in files:
            return os.path.join(root, file_name)

    return None


def get_file_extension(file_path):
    file_name = os.path.basename(file_path)
    directory = os.path.dirname(file_path)
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.basename(full_path) == file_name:
            _, file_extension = os.path.splitext(filename)
            return file_extension
    return None


def move_dir(source_dir, destination_dir):
    try:
        shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    except PermissionError as e:
        print(f"权限错误: {e}")
        # 尝试修改目标目录的权限
        try:
            os.chmod(destination_dir, stat.S_IRWXU)  # 设置目标目录为可读、可写、可执行
            shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
        except Exception as ex:
            print(f"无法修改权限: {ex}")


def write_file_from_string(path, output_string):
    with open(path, 'w') as f:
        f.write(output_string)
    print(f"文件已生成：{output_string}")


def parse_json_to_list(json_str, module, android_config):
    if json_str == "{}":
        return []
    try:
        json_str = json_str.strip("```json")
        data = json.loads(json_str)
        return [value.replace("@", os.path.relpath(android_config.PROJ_STRUCTURE[module]["RES_ROOT"],
                                                   android_config.PROJECT_ROOT) + "/").replace("\\", "/") for value in
                data.values()]
    except json.JSONDecodeError as e:
        # TODO 处理格式解析失败的情况
        print(f"Error parsing JSON: {e} ===> LLM 输出格式非可解析的json格式，解析失败")
        return []


def get_modules(android_config):
    """
    基于规则解析得到当前安卓App有哪些模块及其对应的目录
    :return:
    {
        "模块名称": "模块相对于settings.gradle的路径"
    }
    支持settings.gradle和settings.gradle.kts两种类型的配置文件
    """
    sg_path = android_config.PROJECT_ROOT + "/settings.gradle"
    sg_kts_path = android_config.PROJECT_ROOT + "/settings.gradle.kts"

    # identifier = Word(alphas + "_", alphanums + "_")
    string = QuotedString('"', escChar='\\') | QuotedString("'", escChar='\\')
    include_stmt = Suppress("include") + delimitedList(string, delim=",")
    project_stmt = (
            Suppress("project") + Suppress("(") + string("module") + Suppress(")") +
            Suppress(".projectDir") + Suppress("=") + Suppress("new") + Suppress("File") +
            Suppress("(") + string("path") + Suppress(")")
    )

    kts_include_stmt = Suppress("include") + Suppress("(") + delimitedList(string, delim=",") + Suppress(")")

    modules = {}
    try:
        if os.path.isfile(sg_path):
            with open(sg_path, 'r') as file:
                content = file.read()
                include_results = include_stmt.searchString(content)
                # print(include_results)
                for result in include_results:
                    for module in result:
                        module_name = module.strip("'").lstrip(':')
                        modules[module_name] = module_name

                project_results = project_stmt.searchString(content)
                for result in project_results:
                    module_name = result[0].strip("'").lstrip(':')
                    module_path = result[1].strip("'")
                    modules[module_name] = module_path
        elif os.path.isfile(sg_kts_path):
            with open(sg_kts_path, 'r') as file:
                content = file.read()
                include_results = kts_include_stmt.searchString(content)
                for result in include_results:
                    for module in result:
                        module_name = module.strip("'").lstrip(':')
                        modules[module_name] = module_name

        return modules
    except FileNotFoundError:
        print(f"Error: The file '{sg_path}' was not found.")


def generate_complexity(input_file, output_file):
    df = pd.read_excel(input_file)

    df_sorted = df.sort_values(by=['组件种类数', '组件个数', '是否包含复杂组件'], ascending=[False, False, False])

    total_rows = len(df_sorted)
    print(total_rows)

    complex_end = int(total_rows * 0.2)
    print(complex_end)
    medium_end = int(total_rows * 0.6)
    print(medium_end)

    df_sorted.iloc[:complex_end, df_sorted.columns.get_loc('页面复杂度')] = '复杂'
    df_sorted.iloc[complex_end:medium_end, df_sorted.columns.get_loc('页面复杂度')] = '中等'
    df_sorted.iloc[medium_end:, df_sorted.columns.get_loc('页面复杂度')] = '简单'

    df_sorted.sort_values('序号', ascending=True).to_excel(output_file, index=False)


def is_complex_component(component_name):
    """
    通过简单组件的列表判断组件复杂度
    :param component_name:
    :return: bool
    """
    return component_name not in simple_components


def evaluate_page_component_complexity(content):
    """
    对页面的复杂度进行评估
    从三个维度进行考虑：
    1. 页面包含的组件类型数
    2，页面中的组件总数
    3. 页面中是否包含复杂组件
    """
    if content.strip().startswith('<?xml'):
        content = content.split('?>', 1)[1].strip()
    root = etree.fromstring(content)

    component_types = set()
    total_components = 0
    has_complex_component = False

    # 递归遍历
    def traverse(element):
        nonlocal total_components, has_complex_component
        component_name = element.tag
        component_types.add(component_name)
        total_components += 1

        if is_complex_component(component_name):
            has_complex_component = True

        for child in element:
            traverse(child)

    traverse(root)

    component_count = {
        "component_types_count": len(component_types),
        "total_components": total_components,
        "has_complex_component": has_complex_component
    }

    return component_count, component_types


from collections import OrderedDict


def load_json_file(file_path):
    """
    读取JSON文件并返回字典对象
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def sort_key(item):
    """
    定义排序规则
    """
    compnents_data = item['data_analysis']['compnents_data']
    return (-compnents_data['component_types_count'],
            -compnents_data['total_components'],
            not compnents_data['has_complex_component'])


def sort_and_label_complexity(json_data):
    """
    对数据进行排序并添加复杂度标签
    """
    # 对数据进行排序
    sorted_data = sorted(json_data.items(), key=lambda x: sort_key(x[1]))

    # 计算复杂度标签
    total_items = len(sorted_data)
    complex_threshold = int(total_items * 0.2)
    medium_threshold = int(total_items * 0.6)

    for i, (key, value) in enumerate(sorted_data):
        if i < complex_threshold:
            complexity = '复杂'
        elif i < medium_threshold:
            complexity = '中等'
        else:
            complexity = '简单'

        value['complexity'] = complexity

    # 构建新的字典
    sorted_dict = OrderedDict(sorted_data)
    return sorted_dict


def save_json_file(data, file_path):
    """
    将字典对象保存为JSON文件
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def write_result_to_json(result, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
