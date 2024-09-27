import os
from typing import Annotated


def list_files(
        dirpath: Annotated[str, "目录路径"]
) -> Annotated[list[str], "目录下的文件列表"]:
    """列出目录下的文件"""
    return os.listdir(dirpath)
    # files_list = []
    # for entry in os.listdir(dirpath):
    #     path = os.path.join(dirpath, entry)
    #     if os.path.isdir(path):
    #         files_list.extend(list_files(path))  # 递归调用
    #     else:
    #         files_list.append(path)  # 添加文件到列表
    # return files_list


def read_file(
        filepath: Annotated[str, "文件路径"]
) -> Annotated[str, "文件内容"]:
    """读取文件内容"""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def create_file(
        filepath: Annotated[str, "文件路径"],
        content: Annotated[str, "文件内容"]
) -> None:
    """创建文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':
    print(list_files("../../"))