import json
import os

from android.base import AndroidProjConfig, CustomEncoder
from android.proj_parser import PageAnalyser, init_proj_structure, extract_manifest
from android.util import write_file_from_string, get_modules, move_dir


def analyse_page_dict(base_path, android_config):
    # 得到项目模块信息
    modules = get_modules(android_config)
    if modules is None:
        raise ValueError("Android项目中的模块数不能为0")
    # 依据模块初始化项目配置字典
    for m in modules:
        android_config.PROJ_STRUCTURE[m] = {
            "MODULE_BASE_PATH": os.path.join(android_config.PROJECT_ROOT, modules[m]).replace("\\", "/"),
            "MANIFEST_PATH": "",
            "JAVA_ROOT": "",
            "RES_ROOT": ""
        }
    # 初始化项目结构配置
    init_proj_structure(android_config)
    print(json.dumps(android_config.PROJ_STRUCTURE, indent=4))
    print(type(list(android_config.PROJ_STRUCTURE.keys())))
    page_analyser = PageAnalyser(android_config)
    nested_page_dict = {}
    page_dict = {}
    for module in android_config.PROJ_STRUCTURE.keys():
        # 抽取activity信息
        if android_config.PROJ_STRUCTURE[module]["MANIFEST_PATH"] == "":
            continue
        activities = extract_manifest(android_config.PROJ_STRUCTURE[module]["MANIFEST_PATH"])
        # print(json.dumps(activities, indent=4))
        # 只有模块内部包含Activity才对该模块进行分析
        if len(activities["entrance_activity"]) + len(activities["other_activities"]) >= 1:
            page_analyser.module = module
            module_nested_page_dict, module_page_dict = page_analyser.organize_page(activities)
            nested_page_dict.update(module_nested_page_dict)
            page_dict.update(module_page_dict)
    output_dir = f"{base_path}/output/{android_config.PROJ_NAME}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"{output_dir}已成功初始化")
    output_res_dir = f"{output_dir}/res"
    if not os.path.exists(output_res_dir):
        os.makedirs(output_res_dir)
        print(f"{output_res_dir}已成功初始化")
    page_json_path = f"{output_dir}/page_data.json"
    with open(page_json_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(nested_page_dict, cls=CustomEncoder, indent=4))
        print(f"{page_json_path}文件已生成")
    # TODO 移动资源的多模块处理
    move_dir(android_config.PROJ_STRUCTURE['app']["RES_ROOT"], output_res_dir)
    return output_dir
