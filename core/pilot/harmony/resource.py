import os
import json
from typing import Dict

from core.logger.runtime import get_logger
from core.state.schema import HarmonyResource

logger = get_logger(name="Harmony Resource Pilot")


def _load_harmony_resource_element(harmony_resource_element_path: str) -> Dict[str, Dict[str, str]]:
    """读取鸿蒙项目资源文件中的值文件"""
    values = {}
    for file in os.listdir(harmony_resource_element_path):
        filepath = os.path.join(harmony_resource_element_path, file).replace("\\", "/")
        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                element_dict = json.loads(f.read())
                assert len(element_dict) == 1, "Harmony resource element file has multiple keys."
                resource_type = os.path.splitext(file)[0]
                resource_values = {}
                for item in element_dict[resource_type]:
                    resource_values[item["name"]] = item["value"]
                values[resource_type] = resource_values
    return values


def _load_harmony_resource_media(harmony_resource_media_path: str) -> Dict[str, str]:
    """读取鸿蒙项目资源文件中的媒体文件"""
    medias = {}
    for file in os.listdir(harmony_resource_media_path):
        filepath = os.path.join(harmony_resource_media_path, file).replace("\\", "/")
        if os.path.isfile(filepath):
            # TODO: 对图片资源进行描述
            medias[file] = ""
    return medias


def load_harmony_resource(harmony_resource_path: str) -> HarmonyResource:
    """读取鸿蒙项目资源文件"""
    # 遍历资源文件夹
    resource_dirs = os.listdir(harmony_resource_path)
    # 默认
    values = None
    medias = None
    pages = None
    # 全部
    all_values = {}
    all_medias = {}
    for resource_dir in resource_dirs:
        temp_values = None
        temp_medias = None
        for resource_type in os.listdir(os.path.join(harmony_resource_path, resource_dir)):
            resource_path = os.path.join(harmony_resource_path, resource_dir, resource_type)
            if resource_type == "element":
                temp_values = _load_harmony_resource_element(resource_path)
            elif resource_type == "media":
                temp_medias = _load_harmony_resource_media(resource_path)
            elif resource_type == "profile":
                # main_pages.json, 只在 base 中存在
                if "main_pages.json" in os.listdir(resource_path):
                    with open(os.path.join(resource_path, "main_pages.json"), "r", encoding="utf-8") as f:
                        temp_pages = json.loads(f.read())["src"]
            else:
                logger.warning(f"Resource {resource_path} is not supported.")
        if resource_dir == "base":
            values = temp_values
            medias = temp_medias
            pages = temp_pages

            all_values[resource_dir] = temp_values
            all_medias[resource_dir] = temp_medias

    return HarmonyResource(
        pages=pages, values=values, medias=medias, all_values=all_values, all_medias=all_medias
    )


if __name__ == "__main__":
    resource = load_harmony_resource(r"D:\Codes\Python\harmony-pilot\demos\haromny_demos\hmdemo\entry\src\main\resources")
    print(resource)
