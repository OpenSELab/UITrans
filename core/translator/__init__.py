import os.path
from template.manager import template_manager

from core.translator.resource import translate_android_resource_to_harmony


def init_harmony_from_android(android_project_path: str, harmony_project_path: str,
                              template: str = "harmony_empty_ability_v5"):
    """从安卓项目中初始化鸿蒙项目

    Args:
        android_project_path: 安卓项目路径
        harmony_project_path: 鸿蒙项目路径
        template: 模板名称
    """
    if not os.path.exists(android_project_path):
        raise FileNotFoundError(f'Android project path {android_project_path} not found')

    template_manager.get_template(template).dumps(harmony_project_path)
    translate_android_resource_to_harmony(
        os.path.join(android_project_path, "res"),
        os.path.join(harmony_project_path, "entry", "src", "main", "resources"),
        True
    )


if __name__ == '__main__':
    init_harmony_from_android(
        r"C:\Users\14514\Desktop\GoGrocery",
        r"D:\Codes\ArkTS\GoGrocery",
    )
