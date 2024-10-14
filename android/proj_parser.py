import copy
import json
import os
import re

import xmltodict
from lxml import etree
from openai import OpenAI

from android.util import extract_last, transform_to_xml_filename, read_file, find_file, parse_json_to_list, \
    evaluate_page_component_complexity
from android.layout_parser import generate_resources
from typing import Dict
from android.base import PageItem, CustomEncoder

client = OpenAI(api_key="sk-ffc130d906ac4de391b4720b8be8c034", base_url="https://api.deepseek.com/v1")


def init_proj_structure(android_config):
    """
    初始化项目结构配置项
    """
    for module in android_config.PROJ_STRUCTURE.keys():
        root_dir = android_config.PROJ_STRUCTURE[module]["MODULE_BASE_PATH"]
        for current_path, dirs, filenames in os.walk(root_dir):
            if current_path.endswith('src\\main\\java'):
                android_config.PROJ_STRUCTURE[module]["JAVA_ROOT"] = current_path
            elif current_path.endswith('src\\main\\res'):
                android_config.PROJ_STRUCTURE[module]["RES_ROOT"] = current_path
            elif 'AndroidManifest.xml' in filenames and current_path.endswith('src\\main'):
                android_config.PROJ_STRUCTURE[module]["MANIFEST_PATH"] = current_path + '\\AndroidManifest.xml'


def extract_manifest(f_path: str) -> dict:
    """
    提取AndroidManifest文件的内容
    1. 入口Activity
    2. 其他Activity
    """
    try:
        tree = etree.parse(f_path)
    except:
        print("无效的AndroidManifest.xml路径")
    activities = tree.xpath('/manifest/application/activity')
    activity_dicts = {'entrance_activity': {}, 'other_activities': {}}
    for activity in activities:
        entrance = False
        activity_xml = etree.tostring(activity, pretty_print=True).decode()
        activity_dict = xmltodict.parse(activity_xml)
        name = activity_dict.get('activity', {}).get('@android:name')
        intent_filters = activity.xpath('.//intent-filter')
        for intent_filter in intent_filters:
            actions = intent_filter.xpath('.//action')
            categorys = intent_filter.xpath('.//category')
            actions[0].attrib['{http://schemas.android.com/apk/res/android}name']
            if actions and categorys:
                action = actions[0].attrib['{http://schemas.android.com/apk/res/android}name']
                category = categorys[0].attrib['{http://schemas.android.com/apk/res/android}name']
            else:
                break
            if action == 'android.intent.action.MAIN' and category == 'android.intent.category.LAUNCHER':
                entrance = True
                break
        if entrance:
            activity_dicts['entrance_activity'][name] = activity_dict
        else:
            activity_dicts['other_activities'][name] = activity_dict
    return activity_dicts


class PageAnalyser:
    def __init__(self, android_config):
        # 默认分析app模块下的页面
        self.module = 'app'
        self.android_config = android_config

    def analyse_xml_contains_by_llm(self, content, code_type):
        """
        使用llm分析该页面所依赖的xml文件
        支持xml和java两种文件类型进行分析
        """
        if code_type not in ['java', 'xml']:
            raise ValueError("Invalid code_type. Expected 'java' or 'xml'.")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": f"""你是专业的代码分析人员，请分析输入的{code_type}文件依赖了哪几个本项目内部的xml布局文件，
                    包括菜单（menu）文件、RecyclerView中引用的tools:listitem="@layout/list_item_book"、app:navGraph="@navigation/nav_graph或者在java中通过.xml引用的资源（例如R.xml.app_preferences）等等，
                    但不包括对于TextView、Button或者某个组件id等的依赖以及对应的主布局文件，例如setContentView(该文件对应的主布局文件)指定的文件不能包括。
                    返回格式必须是一个json对象，返回格式示例如下：
                    例如 {{"文件名1": "文件引用路径1", "文件名2": "文件引用路径2"}}.
                    注意，如果所给代码为java，请将文件引用路径修改为与xml相同的格式，例如R.layout.A，应当改为@layout/A.xml
                    如果没有依赖任何布局文件，则直接返回一个空的json对象，即{{}}
                    只返回json数据本身，不允许有其他任何附加解释内容。"""},
                {"role": "user", "content": content},
            ],
            stream=False
        )
        print(response.choices[0].message.content)
        contains_list = parse_json_to_list(response.choices[0].message.content, self.module, self.android_config)
        contains_list = [item if item.endswith(".xml") else item + ".xml" for item in contains_list]
        return contains_list

    def analyse_fragments_by_llm(self, content, code_type):
        """
        利用llm分析Activity下包含的Fragment个数
        支持java和xml两种文件格式
        """
        if code_type not in ['java', 'xml']:
            raise ValueError("Invalid code_type. Expected 'java' or 'xml'.")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": f"""你是专业的代码分析人员，请分析输入的{code_type}文件中依赖了哪几个本项目中的Fragment，
                        返回格式必须是一个json对象，返回格式示例如下：
                        {{"Fragment名称": "Fragment文件对应的java文件名称"}}.
                        如果没有依赖任何布局文件，则直接返回一个空的json对象，即{{}}
                        只返回json数据本身，不允许有其他任何附加解释内容。"""},
                {"role": "user", "content": content},
            ],
            stream=False
        )
        print(response.choices[0].message.content)
        return json.loads(response.choices[0].message.content.strip("```json"))

    def find_xml_by_java(self, java_code):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": """你是专业的代码分析人员，请分析输入的java文件中对应的主布局文件
                            例如setContentView(a.xml)会将该java文件对应的主布局文件设置为a.xml
                            返回数据要求为json格式, 示例如下：
                            {"引用语句": "主布局文件名称"}
                            如果没有找到主布局文件，则直接返回一个空的json对象，即{}
                            只返回json数据本身，不允许有其他任何附加解释内容。"""},
                {"role": "user", "content": java_code},
            ],
            stream=False
        )
        main_xml_dict = json.loads(response.choices[0].message.content.strip("```json"))
        print(main_xml_dict)
        xml_file_name = ""
        for k in main_xml_dict.keys():
            xml_file_name = extract_last(main_xml_dict[k]) + ".xml"
        print("对应的主布局文件为：" + xml_file_name)
        return xml_file_name

    def find_adapter_by_recycler(self, java_code, recycler_id):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": f"""你是专业的代码分析人员，请分析输入的java文件中为id为{recycler_id}的Recycler组件设置的Adapter的类名
                            例如以下代码片段：RecyclerView order_detail_item_recyclerview = findViewById(R.id.recyclerview_item_orders);
                                order_detail_item_recyclerview.setLayoutManager(new LinearLayoutManager(OrderDetailsActivity.this));
                                order_detail_item_recyclerview.setAdapter(new Item_Order_Detail(product_ids, product_names, product_descs, product_imgs, product_prices, product_brands, product_sps, product_dps, product_qtys,  OrderDetailsActivity.this));
                            应该返回{{"recyclerview_item_orders": "Item_Order_Detail"}}
                            返回数据要求为json格式, 示例如下：
                            {{"recycler_id": "Adapter类名"}}
                            如果没有找到主布局文件，则直接返回一个空的json对象，即{{}}
                            只返回json数据本身，不允许有其他任何附加解释内容。"""},
                {"role": "user", "content": java_code},
            ],
            stream=False
        )
        adapter_dict = json.loads(response.choices[0].message.content.strip("```json"))
        print(adapter_dict)
        adpter_class_name = ""
        for k in adapter_dict.keys():
            adpter_class_name = adapter_dict[k]
        print("对应的Adapter为：" + adpter_class_name)
        return adpter_class_name

    def analyse_contains_by_adapter(self, java_code):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": """你是专业的代码分析人员，请分析输入的java文件（是一个安卓Adapter定义）中所引用的视图容器对应的xml文件名称
                            例如：View view = inflater.inflate(R.layout.list_orders, parent, false);
                            应当返回{"list_orders": "@layout/list_orders.xml"}
                            返回数据要求为json格式, 示例如下：
                            {"文件名称": "文件引用路径"}
                            注意，请将文件引用路径修改为与xml相同的格式，例如R.layout.A，应当改为@layout/A.xml
                            如果没有找到主布局文件，则直接返回一个空的json对象，即{{}}
                            只返回json数据本身，不允许有其他任何附加解释内容。"""},
                {"role": "user", "content": java_code},
            ],
            stream=False
        )
        print(response.choices[0].message.content)
        contains_list = parse_json_to_list(response.choices[0].message.content, self.module)
        contains_list = [item if item.endswith(".xml") else item + ".xml" for item in contains_list]
        return contains_list

    def organize_page_from_fragment(self, fragments: dict, page_dict):
        """
        将fragment也组织成为一个主页面
        """
        for fragment_name in fragments.keys():
            fragment_java_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["JAVA_ROOT"],
                                           fragments[fragment_name])
            if fragment_java_path is None:
                print(f"{fragment_name}对应的java文件{fragment_java_path}未找到")
                continue

            java = read_file(fragment_java_path)
            fragment_xml_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["RES_ROOT"],
                                          transform_to_xml_filename(fragment_name, 'fragment'))
            if fragment_xml_path is None:
                xml_file_name = self.find_xml_by_java(java)
                fragment_xml_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["RES_ROOT"], xml_file_name)
            if fragment_xml_path is None:
                print(fragment_name + "未找到对应的布局文件")
                continue
            else:
                print(fragment_name + "成功找到对应的布局文件")
            content = read_file(fragment_xml_path)

            page_name = os.path.relpath(fragment_xml_path, self.android_config.PROJECT_ROOT).replace("\\", "/")
            resources = generate_resources(fragment_xml_path, self.android_config)
            contains_by_xml = self.analyse_xml_contains_by_llm(content, 'xml')
            contains_by_java = self.analyse_xml_contains_by_llm(java, 'java')

            print('通过java文件找到的依赖')
            print(contains_by_java)
            print('通过xml文件找到的依赖')
            print(contains_by_xml)

            contains = list(set(contains_by_xml + contains_by_java))
            contains = list(filter(lambda x: x != page_name, contains))

            def organize_sub_page(contained_pages):
                for sub_page in contained_pages:
                    if sub_page == page_name: continue
                    if not sub_page.endswith('.xml'):
                        sub_page_name = sub_page + ".xml"
                    else:
                        sub_page_name = sub_page
                    sub_page_xml_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["RES_ROOT"],
                                                  os.path.basename(sub_page_name))
                    print(os.path.basename(sub_page_name))
                    if sub_page_xml_path is not None:
                        print(f"{sub_page_name}对应的主布局文件成功找到！")
                    else:
                        print(f"{sub_page_name}对应的主布局文件未找到 ===> 将跳过该子页面")
                        return
                    # 当前默认被包含的页面都是子页面，不对应java代码
                    sub_page_java = ""
                    sub_page_content = read_file(sub_page_xml_path)
                    sub_page_contains = self.analyse_xml_contains_by_llm(sub_page_content, 'xml')
                    organize_sub_page(sub_page_contains)
                    sub_page_resources = generate_resources(sub_page_xml_path, self.android_config)
                    sub_page_item = PageItem(sub_page_name, sub_page_content, sub_page_java, sub_page_contains,
                                             sub_page_resources, False, self.module, self.android_config.PROJ_NAME)
                    page_dict[sub_page_name] = sub_page_item

            print(f">>>>>>>>>>>>>>>>>>>>>>>{fragment_name}开始递归寻找子页面<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            organize_sub_page(contains)
            print(f">>>>>>>>>>>>>>>>>>>>>>>{fragment_name}结束递归寻找子页面<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            page_item = PageItem(page_name, content, java, contains, resources, True, self.module, self.android_config.PROJ_NAME)
            page_dict[page_name] = page_item

    def is_dynamic_data_binding_required(self, xml_content) -> bool:
        """
        判断页面是否需要动态数据绑定
        如果需要，则应当提供对应的模拟数据用于效果预览
        当前基于规则实现：
        1. 是否包含<data>标签（已实现）
        2. 是否包含类似RecyclerView等必须动态设置数据的组件（未实现）
        """
        try:
            root = etree.fromstring(xml_content.encode('utf-8'))
            data_tags = root.xpath("//data")
            return len(data_tags) > 0
        except etree.XMLSyntaxError as e:
            print(f"XML 解析错误: {e}")
            return False

    def process_dynamic_data(self, page_dict: Dict[str, PageItem]):
        """
        为涉及到动态数据绑定的页面生成模拟数据
        目前只支持在数据模型中进行直接数据绑定的类型，即采用了<data>标签
        """
        for page_name in page_dict.keys():
            page = page_dict[page_name]
            if self.is_dynamic_data_binding_required(page.content):
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system",
                         "content": """你是专业的代码分析人员，输入的xml文件中包含数据绑定语句。
                                       请你分析，要使得该xml文件能够正确渲染，需要在本项目中找到哪些数据模型类，
                                       注意，不包括与逻辑交互相关的变量绑定。
                                        返回数据要求为json格式, 示例如下：
                                        {"变量名称": "数据模型名称"}
                                        如果没有任何数据绑定变量，则直接返回一个空的json对象，即{}
                                        只返回json数据本身，不允许有其他任何附加解释内容。"""},
                        {"role": "user", "content": page.content},
                    ],
                    stream=False
                )
                # TODO 进行解析失败的异常处理
                data_model_dict = json.loads(response.choices[0].message.content.strip("```json"))
                print("*****************************************************")
                print(data_model_dict)
                print("*****************************************************")
                for k in data_model_dict.keys():
                    model_file_path = find_file(self.android_config.PROJ_STRUCTURE[page.module]["JAVA_ROOT"],
                                                extract_last(data_model_dict[k]) + '.java')
                    print(model_file_path)
                    model_code = read_file(model_file_path)
                    page.mock_data[k] = self.generate_mock_data_by_llm(model_code)

    def generate_mock_data_by_llm(self, model_code):
        if model_code is None:
            return {}
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": """输入的内容为java数据模型定义代码，请根据该数据模型代码生成一组模拟数据
                                            如果模拟数据内容涉及到图片链接，统一构造为：https://bookdash.org/wp-content/uploads/2024/09/978-1-77632-585-6-880x880.jpg
                                            如果模拟数据内容涉及到书本链接，统一构造为：https://bookdash.org/book-source-files/?download-folder=its-my-book/e-book/en_english
                                            返回数据要求为json格式, 示例如下：
                                            {变量名1": "变量值1",
                                             "变量名2": "变量值2"},
                                            如果没有任何数据绑定变量，则直接返回一个空的json对象，即{}
                                            只返回json数据本身，不允许有其他任何附加解释内容。"""},
                {"role": "user", "content": model_code},
            ],
            stream=False
        )
        # TODO 进行解析失败的异常处理,目前可能报错，与返回值的随机性有关
        mock_data_dict = json.loads(response.choices[0].message.content.strip("```json"))
        return mock_data_dict

    def build_nested_result(self, page_dict: Dict[str, PageItem]):
        """
        根据输入的页面列表，将结果解析为嵌套的json结构
        其嵌套关系根据contains属性递归构造
        若某个页面被多个页面引用，那么该页面数据会在json结构中出现多次
        """
        result_dict = {}

        # for main_page_name in page_dict.keys():
        #     # 过滤掉无效的包含引用（LLM可能出现不存在的引用）
        #     page_dict[main_page_name].contains = [contained_page for contained_page in
        #                                           page_dict[main_page_name].contains if
        #                                           contained_page in page_dict or contained_page + '.xml' in page_dict]
        #     try:
        #         if page_dict[main_page_name].is_main_page:
        #             main_page = {}
        #             main_page[main_page_name] = page_dict[main_page_name]
        #             result_dict[main_page_name] = main_page
        #             for sub_page_name in page_dict[main_page_name].contains:
        #                 if not sub_page_name.endswith('.xml'):
        #                     sub_page_name = sub_page_name + '.xml'
        #                 try:
        #                     result_dict[main_page_name][sub_page_name] = page_dict[sub_page_name]
        #                 except KeyError:
        #                     print(f"Warning：子页面：'{sub_page_name}' 不在page_dict中")
        #     except KeyError:
        #         print(f"Warning：主页面：'{main_page_name}' 不在page_dict中")

        def build_contains(page_name):
            page_item = page_dict[page_name]
            page_item_dict = page_item.to_dict()
            if len(page_item.contains) == 0:
                result_dict[page_name] = page_item.to_dict()
                return
            for contained_page_name in page_item.contains:
                build_contains(contained_page_name)
                page_item_dict[contained_page_name] = result_dict[contained_page_name]
            result_dict[page_name] = page_item_dict

        for main_page_name in page_dict.keys():
            # 过滤掉无效的包含引用（LLM可能出现不存在的引用）
            page_dict[main_page_name].contains = [contained_page for contained_page in
                                                  page_dict[main_page_name].contains if
                                                  contained_page in page_dict or contained_page + '.xml' in page_dict]
            try:
                if page_dict[main_page_name].is_main_page:
                    build_contains(main_page_name)
            except KeyError:
                print(f"Warning：主页面：'{main_page_name}' 不在page_dict中")
        filtered_result = {key: value for key, value in result_dict.items() if value['is_main_page']}
        return filtered_result

    def get_activity_module(self, activity_name):
        """
        根据Activity的android:name属性判断其所属模块
        """
        if activity_name.startswith('.'):
            return self.module
        for module in self.android_config.PROJ_STRUCTURE.keys():
            pattern = r".*\." + re.escape(module) + r"\."
            if re.search(pattern, activity_name):
                return module
        return None

    def analyse_page_data(self, page_dict: Dict[str, PageItem]):
        """
        根据抽取的页面进行数据分析：
        1. 页面总数 *
        2. 每个页面的组件数 *
        3. 每个页面的组件类型数 *
        4. 每个页面是否包含复杂组件 *
        4. 项目总体的组件数 *
        5. 项目总体的组件类型数 *
        6. 项目中每个页面的复杂度（需要对所有项目批处理后进行评估）
        """
        proj_components_num = 0
        proj_components_types = set()
        for page_name in page_dict.keys():
            # 得到页面组件数、页面组件类型数、是否包含复杂组件
            page = page_dict[page_name]
            page_components_data, page_component_types = evaluate_page_component_complexity(page.content)
            proj_components_types.update(page_component_types)
            proj_components_num = proj_components_num + page_components_data["total_components"]
            print(page_components_data)
            page.data_analysis["compnents_data"] = page_components_data
        print("=======================项目统计信息=======================")
        print("项目抽取到的xml文件总数为：", len(page_dict))
        print("项目包含的组件总数为：", proj_components_num)
        print("项目包含的组件种类总数", len(proj_components_types))
        print("=======================项目统计信息=======================")

    def contains_recyclerview(self, xml_content):
        root = etree.fromstring(xml_content.encode('utf-8'))
        recyclerviews = root.xpath('//android.support.v7.widget.RecyclerView')
        if len(recyclerviews) > 0:
            return recyclerviews[0].get('android:id')
        else:
            return ""

    def organize_page(self, activities):
        page_list = []
        activity_list = list(activities["entrance_activity"].keys()) + list(activities["other_activities"].keys())
        page_dict = {}

        for activity_name in activity_list:
            # 根据Activity所属模块确定页面组织的范围
            activity_module = self.get_activity_module(activity_name)
            if activity_module is not None and activity_module != self.module:
                self.module = self.get_activity_module(activity_name)
                print("===========================================================================")
                print(activity_name)
                print("本来的模块名", self.module)
                print("基于activity名称解析后的模块名", activity_module)
                print("===========================================================================")
            # 构造主页面
            activity_name = extract_last(activity_name)
            # TODO 目前仅支持使用kotlin编写的Activity逻辑文件，尚未支持基于kotlin的页面依赖分析
            activity_java_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["JAVA_ROOT"],
                                           activity_name + '.java') or find_file(
                self.android_config.PROJ_STRUCTURE[self.module]["JAVA_ROOT"], activity_name + '.kt')
            java = read_file(activity_java_path) if read_file(activity_java_path) else ""
            activity_xml_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["RES_ROOT"],
                                          transform_to_xml_filename(activity_name, 'activity'))
            if activity_xml_path is None and java != "":
                xml_file_name = self.find_xml_by_java(java)
                activity_xml_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["RES_ROOT"], xml_file_name)
            print(f"------------------------{activity_name}-----------------------------")
            print(activity_java_path)
            print(activity_xml_path)
            print("---------------------------------------------------------------------")

            if activity_xml_path is not None:
                main_page_name = os.path.relpath(activity_xml_path, self.android_config.PROJECT_ROOT).replace("\\", "/")
            else:
                print(activity_name + " 对应的主布局文件未找到 ===> " + " 将跳过该Activity！")
                continue

            content = read_file(activity_xml_path)
            # 如果输入的代码中包含android.support.v7.widget.RecyclerView，那么返回其id
            recycler_id = self.contains_recyclerview(content)
            contains_by_adapter = []
            if recycler_id != "":
                # 根据id在该页面对应的java文件中寻找对应的Adapter类
                adapter = self.find_adapter_by_recycler(java, recycler_id)
                if adapter != "":
                    adapter_file_name = adapter + '.java'
                    adapter_file_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["JAVA_ROOT"],
                                                  adapter_file_name)
                    adapter_file_code = read_file(adapter_file_path)
                    contains_by_adapter = self.analyse_contains_by_adapter(adapter_file_code)
                    # TODO 根据Adapter生成模拟数据

            # 在Adapter类中寻找依赖的文件
            # 根据java和xml代码分析依赖的其他xml文件（目前不分析java依赖）
            contains_by_xml = self.analyse_xml_contains_by_llm(content, 'xml')
            contains_by_java = self.analyse_xml_contains_by_llm(java, 'java')

            contains = list(set(contains_by_xml + contains_by_java + contains_by_adapter))
            contains = list(filter(lambda x: x != main_page_name + '.xml', contains))

            # 根据某个Activity对应的java代码分析依赖的Fragment，Fragment也作为主页面进行分析
            fragments = self.analyse_fragments_by_llm(java, 'java')

            # 递归构造子页面
            def organize_sub_page(contained_pages):
                for sub_page in contained_pages:
                    if sub_page == main_page_name: continue
                    if not sub_page.endswith('.xml'):
                        sub_page_name = sub_page + ".xml"
                    else:
                        sub_page_name = sub_page
                    sub_page_xml_path = find_file(self.android_config.PROJ_STRUCTURE[self.module]["RES_ROOT"],
                                                  os.path.basename(sub_page_name))
                    if sub_page_xml_path is not None:
                        print(f"{sub_page_name}对应的主布局文件成功找到！")
                    else:
                        print(f"{sub_page_name}对应的主布局文件未找到 ===> 将跳过该子页面")
                        return
                    # 当前默认被包含的页面都是子页面，不对应java代码
                    sub_page_java = ""
                    sub_page_content = read_file(sub_page_xml_path)
                    sub_page_contains = self.analyse_xml_contains_by_llm(sub_page_content, 'xml')
                    organize_sub_page(sub_page_contains)
                    sub_page_resources = generate_resources(sub_page_xml_path, self.android_config)
                    sub_page_item = PageItem(sub_page_name, sub_page_content, sub_page_java, sub_page_contains,
                                             sub_page_resources, False, self.module, self.android_config.PROJ_NAME)
                    page_dict[sub_page_name] = sub_page_item

            print(f">>>>>>>>>>>>>>>>>>>>>>>{activity_name}开始递归寻找子页面<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            organize_sub_page(contains)
            print(f">>>>>>>>>>>>>>>>>>>>>>>{activity_name}结束递归寻找子页面<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

            resources = generate_resources(activity_xml_path, self.android_config)
            page_item = PageItem(main_page_name, content, java, contains, resources, True, self.module, self.android_config.PROJ_NAME)
            page_list.append(page_item)
            page_dict[main_page_name] = page_item
            self.organize_page_from_fragment(fragments, page_dict)

        print(json.dumps(page_dict, cls=CustomEncoder, indent=4))
        self.process_dynamic_data(page_dict)
        self.analyse_page_data(page_dict)
        # return self.build_nested_result(page_dict), page_dict
        return {key: value for key, value in page_dict.items() if 'layout' in key.split('/')}, page_dict
