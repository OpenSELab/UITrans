import json
import os.path
from typing import Annotated

from core.utils.harmony_utils.page import create_harmony_page


def create_harmony_page_tool(
        page_code: Annotated[str, "页面代码"],
        page_name: Annotated[str, "页面名称"],
        project_dir: Annotated[str, "项目目录"],
        module_name: Annotated[str, "模块名称"] = "entry",
        package_name: Annotated[str, "包名称"] = "pages"
):
    """创建鸿蒙ArkUI页面，并自动注册该页面

    Args:
        page_code (str): 页面代码
        page_name (str): 页面名称
        project_dir (str): 项目目录
        module_name (str): 模块名称，默认为 entry
        package_name (str): 包名称，默认为 pages
    """
    create_harmony_page(
        page_code,
        page_name,
        project_dir,
        module_name,
        package_name
    )

