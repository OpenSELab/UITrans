import json
import os


def create_harmony_page(
        page_code: str,
        page_name: str,
        project_dir: str,
        module_name: str = "entry",
        package_name: str = "pages"
):
    """创建鸿蒙ArkUI页面，并自动注册该页面

    Args:
        page_code (str): 页面代码
        page_name (str): 页面名称
        project_dir (str): 项目目录
        module_name (str): 模块名称，默认为 entry
        package_name (str): 包名称，默认为 pages
    """
    # 格式化文件名
    if page_name.endswith(".ets"):
        page_name = page_name[:-4]
    if "_" in page_name:
        # 将下划线分隔的名称转换为全大写驼峰命名
        words = reversed(page_name.split("_"))
        page_name = "".join([word.capitalize() for word in words])
    # 创建页面文件
    page_filepath = os.path.join(project_dir, module_name, "src", "main", "ets", package_name, page_name + ".ets")
    with open(page_filepath, "w", encoding="utf-8") as f:
        f.write(page_code)
    # 注册页面
    main_pages_filepath = os.path.join(project_dir, module_name, "src", "main", "resources", "base", "profile",
                                       "main_pages.json")
    with open(main_pages_filepath, "r", encoding="utf-8") as f:
        main_pages = json.load(f)
    if "src" not in main_pages:
        main_pages["src"] = [
            f"{package_name}/{page_name}"
        ]
    else:
        main_pages["src"].append(f"{package_name}/{page_name}")
    with open(main_pages_filepath, "w", encoding="utf-8") as f:
        json.dump(main_pages, f, indent=2)