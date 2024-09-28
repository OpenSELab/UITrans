import os
from typing import Annotated


def list_files(
    dirpath: Annotated[str, "目录路径"]
) -> Annotated[list[str], "目录下的文件列表"]:
    """递归列出目录下的全部文件"""
    def inner_list_files(dirpath: str, indent: int = 0):
        files_list = []
        for entry in os.listdir(dirpath):
            path = os.path.join(dirpath, entry)
            if os.path.isdir(path):
                files_list.append(' ' * indent + f"[DIR] {entry}")  # 添加目录标识
                files_list.extend(inner_list_files(path, indent + 4))  # 递归调用，增加缩进
            else:
                files_list.append(' ' * indent + f"[FILE] {entry}")  # 添加文件
        return files_list
    return inner_list_files(dirpath)


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