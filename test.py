import os


def list_files(directory, indent=0):
    files_list = []
    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)
        if os.path.isdir(path):
            files_list.append(' ' * indent + f"[DIR] {entry}")  # 添加目录标识
            files_list.extend(list_files(path, indent + 4))  # 递归调用，增加缩进
        else:
            files_list.append(' ' * indent + entry)  # 添加文件
    return files_list


# 示例用法
directory_path = './core'
all_files = list_files(directory_path)
for file in all_files:
    print(file)
