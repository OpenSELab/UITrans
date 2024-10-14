
from android.util import get_file_extension
from lxml import etree

attribute_values = []


def generate_resources(layout_file_path, android_config):
    with open(layout_file_path, 'r', encoding='utf-8') as file:
        layout = file.read().encode('utf-8')
    root = etree.fromstring(layout)
    traverse_tree(root)
    # print(attribute_values)
    return build_resources_dict(android_config)


def traverse_tree(element):
    for attr, value in element.attrib.items():
        if value.startswith('@string/') or value.startswith('@style/'):
            attribute_values.append(value)
    for child in element:
        traverse_tree(child)


def build_resources_dict(android_config):
    """
    @string,@style等引用单个字段的语句采用按类型聚合到单个文件的方式实现
    例如，@string所指向的字段均存储于xxx/xxx/strings.xml，直接按类型构造索引
    而@drawable引用的资源文件则需要自动化寻找该文件，实现一对一的索引构造（因为后缀名是不一定的）
    """
    resources_dict = {}
    for i in attribute_values:
        if i.startswith("@drawable"):
            suffix = get_file_extension(android_config.RES_ROOT + "\\drawable\\" + i.split("@drawable/", 1))
            resources_dict[i] = "resources/drawable/" + i.split("@drawable/", 1) + suffix
        elif i.startswith("@string"):
            resources_dict[i] = "resources/values/strings.xml"
        elif i.startswith("@style"):
            resources_dict[i] = "resources/values/styles.xml"
        elif i.startswith("@color"):
            resources_dict[i] = "resources/values/colors.xml"
        elif i.startswith("@dimen"):
            resources_dict[i] = "resources/values/dimens.xml"
        else:
            # 当前不支持解析的资源引用类型
            resources_dict[i] = ""
    return resources_dict
