import json
import os
import shutil
import tempfile
from typing import Tuple

from lxml import etree
from PIL import Image

from core.logger.runtime import get_logger

logger = get_logger(name="Android Translator")

ANDROID_RESOURCE_VALUES_TAG_MAP = {
    "strings": "string",
    "colors": "color",
    "dimens": "dimen",
    "integers": "integer"
}

ANDROID_HARMONY_RESOURCE_MAP = {
    "strings": "string",
    "colors": "color",
    "dimens": "float",
    "integers": "integer"
}

ANDROID_HARMONY_RESOURCE_QUALIFIER_MAP = {
    "land": ("-", 5, "horizontal"),  # 横屏
    "port": ("-", 5, "vertical"),  # 竖屏
    "car": ("-", 6, "car"),  # 车机
    "watch": ("-", 6, "wearable"),  # 智能穿戴
    "television": ("-", 6, "tv"),  # 智慧屏
    "desk": ("-", 6, "tablet"),  # TODO: 平板?
    "night": ("-", 7, "dark"),  # 深色模式
    "notnight": ("-", 7, "light"),  # 浅色模式
    "ldpi": ("-", 8, "sdpi"),  # 低密度屏幕
    "mdpi": ("-", 8, "mdpi"),  # 中密度屏幕
    "hdpi": ("-", 8, "ldpi"),  # 高密度屏幕
    "xhdpi": ("-", 8, "xhdpi"),  # 超高密度屏幕
    "xxhdpi": ("-", 8, "xxhdpi"),  # 超超高密度屏幕
    "xxxhdpi": ("-", 8, "xxxhdpi"),  # 超超超高密度屏幕
    "anydpi": None,  # 任意密度屏幕
}


def translate_underscore_to_camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def translate_android_resource_qualifier_to_harmony_qualifier(qualifier: str) -> Tuple[str, int, str] | None:
    """将安卓资源限定符转换为鸿蒙资源限定符

    _移动国家码_移动网络码-语言_文字_国家或地区-横竖屏-设备类型-颜色模式-屏幕密度（抽象）

    :param qualifier: 安卓资源限定符
    :return: 鸿蒙资源限定符, 若无对应的鸿蒙资源限定符则返回 None

    TODO: 支持更多的资源限定符
    """
    if qualifier in ANDROID_HARMONY_RESOURCE_QUALIFIER_MAP:
        return ANDROID_HARMONY_RESOURCE_QUALIFIER_MAP[qualifier]
    else:
        if qualifier.startswith("w"):
            # 按照宽度适配
            width_value = int(qualifier[1:].replace("dp", ""))
            if width_value < 600:
                return None
            elif width_value < 1240:
                return "-", 6, "tablet"
            else:
                return "-", 6, "tv"
        elif qualifier.startswith("h"):
            # 按照高度适配
            height_value = int(qualifier[1:].replace("dp", ""))
            if height_value < 720:
                return None
            elif height_value < 1080:
                return "-", 6, "tablet"
            else:
                return "-", 6, "tv"
        elif qualifier.startswith("v"):
            # 按平台API版本适配
            return None
        else:
            logger.warning(f"Invalid qualifier value: {qualifier}")
            # raise ValueError(f"Invalid qualifier value: {qualifier}")
            return None


class HarmonyResourceJSONEncoder(json.JSONEncoder):
    """
    避免转译符号
    """

    def encode(self, obj):
        json_str = super().encode(obj)
        return json_str
        # return json_str.replace('\\', '\\')


def translate_android_pixel_to_harmony_pixel(pixel: str) -> str:
    """将安卓单位转换为鸿蒙单位

    将 dp 替换为 vp
    将 sp 替换为 fp
    保留 px 不变
    :param pixel:
    :return:
    """
    if pixel.endswith("dp"):
        return pixel.replace("dp", "vp")
    elif pixel.endswith("sp"):
        return pixel.replace("sp", "fp")
    elif pixel.endswith("px"):
        return pixel
    else:
        return pixel
        # raise ValueError(f"Invalid pixel value: {pixel}")


def translate_android_color_to_harmony(color: str) -> str:
    def translate_argb_to_rgba(argb: str) -> str:
        """将 ARGB 颜色值转换为 RGBA 颜色值

        :param argb: ARGB 颜色值
        :return: RGBA 颜色值
        """
        if argb.startswith("#"):
            # 十六进制表示的颜色值
            argb = argb[1:]
            if len(argb) == 8:
                # ARGB
                return "#" + argb[2:] + argb[:2]
            elif len(argb) == 6:
                # RGB
                return "#" + argb
        else:
            raise ValueError(f"Invalid color value: {argb}")
    if color.startswith("#"):
        return translate_argb_to_rgba(color)
    elif color.startswith("@"):
        # 引用资源
        # TODO: 支持引用资源
        logger.warning(f"Unsupported color reference: {color}")
        return "#1E90FF"
    else:
        raise ValueError(f"Invalid color value: {color}")


def rename_filepath(filepath, overwrite=True) -> str:
    """若文件存在，则为文件名添加后缀序号

    :param filepath: 文件路径
    :param overwrite: 覆盖
    :return:
    """
    if overwrite:
        return filepath
    new_filepath = filepath
    try_count = 1
    while os.path.exists(new_filepath):
        filename, extension = os.path.splitext(filepath)
        new_filepath = f"{filename}_{try_count}{extension}"
        try_count += 1
    return new_filepath


def translate_android_drawable_xml_to_harmony_svg(android_vector_drawable_xml_path: str, harmony_svg_path: str):
    """将安卓矢量图标文件转换为鸿蒙SVG文件格式

    :param android_vector_drawable_xml_path: 安卓矢量图标文件路径
    :param harmony_svg_path: 鸿蒙SVG文件路径
    """
    ANDROID_RES_DRAWABLE_NAMESPACE = "http://schemas.android.com/apk/res/android"
    ANDROID_AAPT_NAMESPACE = "http://schemas.android.com/aapt"

    attributes_map = {
        "android:pathData": "d",
        "android:fillColor": "fill",
        "android:strokeLineJoin": "stroke-linejoin",
        "android:strokeLineCap": "stroke-linecap",
        "android:strokeMiterLimit": "stroke-miterlimit",
        "android:strokeWidth": "stroke-width",
        "android:strokeColor": "stroke",
        "android:fillType": "fill-rule",
        "android:fillAlpha": "fill-opacity",
        "android:strokeAlpha": "stroke-opacity"
    }
    attributes_transforms = {
        "android:fillType": lambda value: value.lower() if value else None,
        "android:fillColor": translate_android_color_to_harmony,
        "android:strokeColor": translate_android_color_to_harmony
    }
    group_attrs_map = {
        "android:name": "id",
        "android:pivotX": {"transform": "pivotX"},
        "android:pivotY": {"transform": "pivotX"},
        "android:rotation": {"transform": "rotation"},
        "android:scaleX": {"transform": "scaleX"},
        "android:scaleY": {"transform": "scaleY"},
        "android:translateX": {"transform": "translateX"},
        "android:translateY": {"transform": "translateY"},
    }
    gradient_attrs_map = {
        "android:startX": "x1",
        "android:startY": "y1",
        "android:endX": "x2",
        "android:endY": "y2",
        "android:centerX": "cx",
        "android:centerY": "cy",
        "android:gradientRadius": "r",
        "android:angle": "gradientTransform",  # 特殊处理
    }
    gradient_item_attrs_map = {
        "android:color": "stop-color",
        "android:offset": "offset",
    }

    gradient_item_attrs_transforms = {
        "android:color": translate_android_color_to_harmony,
        "android:offset": lambda value: f"{float(value) * 100}%",  # 将偏移量转换为百分比
    }

    def get_attr(element, attr_name):
        new_attr_name = attr_name.replace("android:", f"{{{ANDROID_RES_DRAWABLE_NAMESPACE}}}")
        if new_attr_name in element.attrib:
            attr_value = element.attrib[new_attr_name]
            return attr_value
        return None

    def parse_path_element(root, path_element, defs):
        """处理路径节点"""
        svg_path = root.makeelement("path")
        for origin_attr_name, target_attr_name in attributes_map.items():
            target_attr_value = get_attr(path_element, origin_attr_name)
            if target_attr_value is None:
                continue
            if origin_attr_name in attributes_transforms:
                target_attr_value = attributes_transforms[origin_attr_name](target_attr_value)
            svg_path.set(target_attr_name, target_attr_value)

        return svg_path

    def parse_gradient_element(root, gradient_element, defs):
        """处理渐变节点"""
        gradient_type = get_attr(gradient_element, "android:type")
        if gradient_type == "linear":
            svg_gradient = root.makeelement("linearGradient")
        elif gradient_type == "radial":
            svg_gradient = root.makeelement("radialGradient")
        elif gradient_type == "sweep":
            raise ValueError("Sweep gradient is not compatible by SVG")
        else:
            # logger.error(f"Unsupported gradient type: {gradient_type}")
            raise ValueError(f"Unsupported gradient type: {gradient_type}")

        svg_gradient.set('gradientUnits', 'userSpaceOnUse')

        # 渐变节点
        for origin_attr_name, target_attr_name in gradient_attrs_map.items():
            target_attr_value = get_attr(gradient_element, origin_attr_name)
            if target_attr_value is None:
                continue
            svg_gradient.set(target_attr_name, target_attr_value)

        start_color = get_attr(gradient_element, "android:startColor")
        end_color = get_attr(gradient_element, "android:endColor")
        if start_color and end_color:
            start_svg_stop = etree.Element("stop")
            start_svg_stop.set("offset", "0%")
            start_svg_stop.set("stop-color", translate_android_color_to_harmony(start_color))
            svg_gradient.append(start_svg_stop)

            end_svg_stop = etree.Element("stop")
            end_svg_stop.set("offset", "100%")
            end_svg_stop.set("stop-color", translate_android_color_to_harmony(end_color))
            svg_gradient.append(end_svg_stop)


        # 渐变节点的子节点
        for gradient_item_element in gradient_element:
            if gradient_item_element.tag == "item":
                svg_stop = etree.Element("stop")
                for origin_attr_name, target_attr_name in gradient_item_attrs_map.items():
                    target_attr_value = get_attr(gradient_item_element, origin_attr_name)
                    if target_attr_value is None:
                        continue
                    if origin_attr_name in gradient_item_attrs_transforms:
                        target_attr_value = gradient_item_attrs_transforms[origin_attr_name](target_attr_value)
                    svg_stop.set(target_attr_name, target_attr_value)
                svg_gradient.append(svg_stop)

        return svg_gradient

    def parse_group_element(root, group_element, defs):
        svg_group = root.makeelement("g")

        attrs = {}
        for origin_attr_name, target_attr_name in group_attrs_map.items():
            target_attr_value = get_attr(group_element, origin_attr_name)
            if target_attr_value is None:
                continue
            if isinstance(target_attr_name, dict) and "transform" in target_attr_name:
                prev_transform = attrs.get("transform", {})
                prev_transform[target_attr_name["transform"]] = target_attr_value
                attrs["transform"] = prev_transform
            else:
                attrs[target_attr_name] = target_attr_value
        if attrs:
            transforms = attrs.get("transform")
            if transforms:
                t = []

                scale_x = transforms.get('scaleX', 0)
                scale_y = transforms.get('scaleY', 0)
                has_scale = scale_x != 0 or scale_y != 0

                pivot_x = transforms.get('pivotX', 0)
                pivot_y = transforms.get('pivotY', 0)
                has_pivot = pivot_x != 0 or pivot_y != 0

                translate_x = transforms.get('translateX', 0)
                translate_y = transforms.get('translateY', 0)
                has_translation = translate_x != 0 or translate_y != 0

                rotation = transforms.get('rotation', 0)
                has_rotation = rotation != 0

                if has_pivot:
                    t.append(f"translate({pivot_x}, {pivot_y})")

                if has_scale:
                    t.append(f"scale({scale_x}, {scale_y})")

                if has_rotation:
                    t.append(f"rotate({rotation})")

                if has_translation:
                    t.append(f"translate({translate_x}, {translate_y})")

                if t:
                    svg_group.set('transform', ' '.join(t))
                del attrs['transform']

            for key, value in attrs.items():
                svg_group.set(key, value)

        return svg_group

    def parse_stroke_element(stroke_element):
        """处理 stroke 节点"""
        style_attrs = {}
        color = get_attr(stroke_element, "android:color")
        width = get_attr(stroke_element, "android:width")
        if color:
            style_attrs["stroke"] = translate_android_color_to_harmony(color)
        if width:
            style_attrs["stroke-width"] = width
        return style_attrs

    def parse_corners_element(corners_element):
        """处理 corners 节点"""
        style_attrs = {}
        radius = get_attr(corners_element, "android:radius")
        if radius:
            style_attrs["rx"] = radius
        return style_attrs

    def parse_solid_element(solid_element):
        """处理 solid 节点"""
        style_attrs = {}
        color = get_attr(solid_element, "android:color")
        if color:
            style_attrs["fill"] = translate_android_color_to_harmony(color)
        return style_attrs

    def parse_shape_element(root, shape_element, defs):
        """处理 shape 节点"""
        shape_type = get_attr(shape_element, "android:shape")

        svg_shape = None
        style_attrs = {}
        fill_value = None  # 用于存储填充的值（颜色或渐变）

        for child in shape_element:
            if child.tag == "stroke":
                style_attrs.update(parse_stroke_element(child))
            elif child.tag == "corners":
                style_attrs.update(parse_corners_element(child))
            elif child.tag == "solid":
                style_attrs.update(parse_solid_element(child))
            elif child.tag == "gradient":
                # 处理渐变
                svg_gradient = parse_gradient_element(root, child, defs)
                gradient_id = f"gradient_{len(defs)}"
                svg_gradient.set("id", gradient_id)
                defs.append(svg_gradient)
                fill_value = f"url(#{gradient_id})"

        if shape_type == "rectangle":
            svg_shape = root.makeelement("rect")
            # 处理圆角（半径）
            radius = style_attrs.pop("rx", None)
            if radius:
                svg_shape.set("rx", radius)
                svg_shape.set("ry", radius)
            svg_shape.set("x", "0")
            svg_shape.set("y", "0")
            svg_shape.set("width", get_attr(shape_element, "android:width") or "100%")
            svg_shape.set("height", get_attr(shape_element, "android:height") or "100%")
        elif shape_type == "oval":
            svg_shape = root.makeelement("ellipse")
            svg_shape.set("cx", str(float(get_attr(shape_element, "android:width")) / 2))
            svg_shape.set("cy", str(float(get_attr(shape_element, "android:height")) / 2))
            svg_shape.set("rx", str(float(get_attr(shape_element, "android:width")) / 2))
            svg_shape.set("ry", str(float(get_attr(shape_element, "android:height")) / 2))
        elif shape_type == "line":
            svg_shape = root.makeelement("line")
            svg_shape.set("x1", "0")
            svg_shape.set("y1", "0")
            svg_shape.set("x2", get_attr(shape_element, "android:width"))
            svg_shape.set("y2", get_attr(shape_element, "android:height"))
        elif shape_type == "ring":
            svg_shape = root.makeelement("circle")
            svg_shape.set("cx", str(float(get_attr(shape_element, "android:width")) / 2))
            svg_shape.set("cy", str(float(get_attr(shape_element, "android:height")) / 2))
            svg_shape.set("r", style_attrs.pop("stroke-width", "0"))
        else:
            logger.warning(f"Unsupported shape type: {shape_type} in {android_vector_drawable_xml_path}")
            return None

        # 应用填充
        if fill_value:
            style_attrs["fill"] = fill_value

        if style_attrs:
            for key, value in style_attrs.items():
                svg_shape.set(key, value)

        return svg_shape

    def transform_node(node, parent, root, defs):
        if node.tag == "path":
            svg_path = parse_path_element(root, node, defs)
            for child in node:
                if child.tag == f"{{{ANDROID_AAPT_NAMESPACE}}}attr":
                    # 处理属性节点
                    attr_name = child.get("name")
                    if attr_name in ["android:fillColor", "android:strokeColor"]:
                        # 渐变
                        for grandchild in child:
                            if grandchild.tag == "gradient":
                                svg_gradient = parse_gradient_element(root, grandchild)
                                size = len(defs)
                                gradient_id = f"gradient_{size}"
                                svg_gradient.set("id", gradient_id)
                                defs.append(svg_gradient)
                                svg_attr_name = attributes_map[attr_name]
                                svg_path.set(svg_attr_name, f"url(#{gradient_id})")
            return svg_path
        elif node.tag == "group":
            svg_group = parse_group_element(root, node, defs)
            prev_clip_path_id = None

            for child in node:
                child_path = transform_node(child, node, root, defs)

                if child_path:
                    clip_path_node = getattr(child_path, 'clip_path_node', None)
                    if clip_path_node:
                        if defs is not None:
                            size = len(defs)
                            prev_clip_path_id = f"clip_path_{size}"
                            clip_path_node.set('id', prev_clip_path_id)
                            defs.append(clip_path_node)
                        continue

                    if prev_clip_path_id:
                        child_path.set('clip-path', f"url(#{prev_clip_path_id})")
                        prev_clip_path_id = None

                    svg_group.append(child_path)
            return svg_group

        elif node.tag == "shape":
            svg_shape = parse_shape_element(root, node, defs)
            return svg_shape

        elif node.tag == "gradient":
            svg_gradient = parse_gradient_element(root, node, defs)
            return svg_gradient

        elif node.tag == "clip-path":
            path_data = get_attr(node, "android:pathData")
            svg_clip_path = root.makeelement("clipPath")
            path = root.makeelement("path")

            path.set("d", path_data)
            svg_clip_path.append(path)

            return {"clip_path_node": svg_clip_path}

        return None

    def remove_dimen_suffix(dimen):
        dimen = dimen.strip()

        if not dimen:
            return dimen

        if dimen.isdigit():
            return dimen

        if dimen.endswith("%"):
            return dimen

        if isinstance(dimen, str):
            return dimen[:-2]

        return dimen

    _root = etree.parse(android_vector_drawable_xml_path).getroot()

    if _root.tag == "vector":
        # 安卓矢量图标文件
        viewport_width = get_attr(_root, "android:viewportWidth")
        viewport_height = get_attr(_root, "android:viewportHeight")

        output_width = remove_dimen_suffix(get_attr(_root, "android:width"))
        output_height = remove_dimen_suffix(get_attr(_root, "android:height"))

        # 创建 svg 根元素
        svg_root = etree.Element("svg", {
            "xmlns": "http://www.w3.org/2000/svg",
            "width": get_attr(_root, "android:width").replace("dp", ""),
            "height": get_attr(_root, "android:height").replace("dp", ""),
            "viewBox": "0 0 {viewportWidth} {viewportHeight}".format(
                viewportWidth=viewport_width or output_width,
                viewportHeight=viewport_height or output_height
            )
        })

        _defs = etree.Element("defs")

        node_indices = {
            'g': 0,
            'path': 0,
        }

        for _node in _root:
            if isinstance(_node, etree._Comment):
                # 注释节点
                comment_node = etree.Comment(_node.text.strip())
                svg_root.append(comment_node)
                continue
            elif isinstance(_node, etree._Element):
                node = transform_node(_node, _root, _root, _defs)
                _id = node.get("id")

                current_id = node_indices.get(node.tag, 0)
                node_indices[node.tag] = current_id + 1

                node.set("id", _id or f"{node.tag}_{current_id}")
                svg_root.append(node)
            else:
                raise ValueError(f"Unsupported node type: {type(_node)}")

        if len(_defs):
            svg_root.append(_defs)

        os.makedirs(os.path.dirname(harmony_svg_path), exist_ok=True)
        with open(harmony_svg_path, "w", encoding="utf-8") as f:
            f.write(etree.tostring(svg_root, pretty_print=True, encoding="unicode"))
        logger.debug(f"Translate {android_vector_drawable_xml_path} to {harmony_svg_path}")
    elif _root.tag == "shape":

        svg_width = get_attr(_root, "android:width") or "100%"
        svg_height = get_attr(_root, "android:height") or "100%"
        svg_width = remove_dimen_suffix(svg_width)
        svg_height = remove_dimen_suffix(svg_height)
        viewport_width = get_attr(_root, "android:viewportWidth") or 100
        viewport_height = get_attr(_root, "android:viewportHeight") or 100

        svg_root = etree.Element("svg", {
            "xmlns": "http://www.w3.org/2000/svg",
            "width": svg_width,
            "height": svg_height,
            "viewBox": "0 0 {viewportWidth} {viewportHeight}".format(
                viewportWidth=viewport_width,
                viewportHeight=viewport_height
            )
        })

        _defs = etree.Element("defs")
        svg_shape = parse_shape_element(svg_root, _root, _defs)
        if svg_shape is not None:
            svg_root.append(svg_shape)
            if len(_defs):
                svg_root.append(_defs)
            # 写入文件
            os.makedirs(os.path.dirname(harmony_svg_path), exist_ok=True)
            with open(harmony_svg_path, "w", encoding="utf-8") as f:
                f.write(etree.tostring(svg_root, pretty_print=True, encoding="unicode"))
            logger.debug(f"Translated shape {android_vector_drawable_xml_path} to {harmony_svg_path}")
        else:
            logger.warning(f"Failed to parse shape element: {android_vector_drawable_xml_path}")
    elif _root.tag == "bitmap":
        # 位图文件
        logger.warning(f"Bitmap file is not supported: {android_vector_drawable_xml_path}")
    else:
        logger.warning(f"Unsupported file type: {android_vector_drawable_xml_path}")


def translate_android_resource_values_to_harmony(
        android_resource_values_path: str,
        harmony_resource_values_path: str,
):
    """将安卓资源文件转换为鸿蒙资源文件格式

    若鸿蒙资源文件存在，则合并
    若资源文件中键值对存在冲突，则会被覆盖
    :param android_resource_values_path: 安卓资源文件路径
    :param harmony_resource_values_path: 鸿蒙资源文件路径
    """
    if not android_resource_values_path.endswith(".xml"):
        raise ValueError("Android resource values file must be xml format")
    root = etree.parse(android_resource_values_path).getroot()
    assert root.tag == "resources", "Android resource xml file's root tag must be resources"
    os.makedirs(os.path.dirname(harmony_resource_values_path), exist_ok=True)
    android_resource_values_filename = os.path.splitext(os.path.basename(android_resource_values_path))[0]
    if android_resource_values_filename not in ANDROID_RESOURCE_VALUES_TAG_MAP:
        raise AssertionError(f"Android resource file `{android_resource_values_filename}` is not supported")
    android_resource_values_tag = ANDROID_RESOURCE_VALUES_TAG_MAP[android_resource_values_filename]
    harmony_resource_values_tag = ANDROID_HARMONY_RESOURCE_MAP[android_resource_values_filename]
    try:
        harmony_resource_values = {}
        if os.path.exists(harmony_resource_values_path):
            # 文件存在
            with open(harmony_resource_values_path, "r", encoding="utf-8") as f:
                _harmony_resource_values = json.loads(f.read())[harmony_resource_values_tag]
            harmony_resource_values = {item["name"]: item["value"] for item in _harmony_resource_values}
        # 获取安卓资源文件中的所有字符串
        if os.path.exists(harmony_resource_values_path):
            pass
        for element in root.findall(android_resource_values_tag):
            key = element.get("name")
            value = ""
            if element.text:
                for element_text_line in element.text.split("\n"):
                    value += element_text_line.strip()
            # TODO: 若有不同的数据类型，需要进行转换
            if harmony_resource_values_tag == "string":
                value = ""
                # 除去多余的空格与换行符
                if element.text:
                    for element_text_line in element.text.split("\n"):
                        value += element_text_line.strip()
            elif harmony_resource_values_tag == "color":
                # ARGB
                value = value
            elif harmony_resource_values_tag == "float":
                # 将安卓单位转换为鸿蒙单位
                value = translate_android_pixel_to_harmony_pixel(value)
            elif harmony_resource_values_tag == "integer":
                value = int(value)
            else:
                raise AssertionError(f"Android resource file `{android_resource_values_filename}` is not supported")
            # TODO：解决键值对冲突
            harmony_resource_values[key] = value

        with open(harmony_resource_values_path, "w", encoding="utf-8") as f:
            f.write(json.dumps({
                harmony_resource_values_tag: [
                    {"name": key, "value": value}
                    for key, value in harmony_resource_values.items()
                ]
            }, ensure_ascii=False, indent=4, cls=HarmonyResourceJSONEncoder))
    except Exception as e:
        raise e


def translate_android_resource_qualifier_to_harmony(android_resource_qualifier):
    """将安卓资源文件限定符转换为鸿蒙资源文件限定符

    :param android_resource_qualifier: 安卓资源文件限定符
    :return: 鸿蒙资源文件限定符
    """
    android_qualifier_list = android_resource_qualifier.split("-")[1:]
    harmony_qualifier_list = []
    for android_qualifier in android_qualifier_list:
        harmony_qualifier = translate_android_resource_qualifier_to_harmony_qualifier(android_qualifier)
        if harmony_qualifier is None:
            continue
        harmony_qualifier_list.append(harmony_qualifier)
    harmony_qualifier_list = sorted(harmony_qualifier_list, key=lambda x: x[1])
    total_harmony_qualifier = "".join([
        f"{harmony_qualifier[0]}{harmony_qualifier[2]}"
        for harmony_qualifier in harmony_qualifier_list
    ])[1:]
    return total_harmony_qualifier


def translate_android_resource_to_harmony(android_resource_path, harmony_resource_path, overwrite=False):
    """将安卓资源文件转换为鸿蒙资源文件格式
    :param android_resource_path: 安卓资源文件夹路径
    :param harmony_resource_path: 鸿蒙资源文件夹路径
    :param overwrite: 是否覆盖
    :return: None

    TODO: 并发处理
    TODO: 支持其他资源文件，如主题等
    """

    tasks = []
    # values 文件夹
    for resource_dir in os.listdir(android_resource_path):
        if resource_dir.startswith("values"):
            # 资源文件
            if resource_dir == "values":
                # 默认资源文件
                _harmony_resource_base_dir = os.path.join(harmony_resource_path, "base", "element")
            else:
                try:
                    # values-xxx 资源文件
                    total_harmony_qualifier = translate_android_resource_qualifier_to_harmony(resource_dir)
                    if total_harmony_qualifier:
                        _harmony_resource_base_dir = os.path.join(harmony_resource_path, total_harmony_qualifier, "element")
                    else:
                        _harmony_resource_base_dir = os.path.join(harmony_resource_path, "base", "element")
                except Exception as e:
                    logger.error(f"Failed to translate {resource_dir} to harmony: {e}")
                    continue

            for resource_file in os.listdir(os.path.join(android_resource_path, resource_dir)):
                if resource_file.endswith(".xml"):
                    if os.path.splitext(resource_file)[0] not in ANDROID_RESOURCE_VALUES_TAG_MAP:
                        logger.warning(f"Android resource file `{resource_file}` is not supported")
                        continue
                    origin_resource_file = os.path.join(android_resource_path, resource_dir, resource_file)
                    harmony_resource_file = os.path.join(_harmony_resource_base_dir,
                                                         f"{ANDROID_HARMONY_RESOURCE_MAP[os.path.splitext(resource_file)[0]]}.json")
                    logger.debug(f"Translate {origin_resource_file} to {harmony_resource_file}")
                    translate_android_resource_values_to_harmony(
                        origin_resource_file,
                        harmony_resource_file
                    )
        elif resource_dir.startswith("drawable"):
            if resource_dir == "drawable":
                _harmony_resource_base_dir = os.path.join(harmony_resource_path, "base", "media")
            else:
                total_harmony_qualifier = translate_android_resource_qualifier_to_harmony(resource_dir)

                _harmony_resource_base_dir = os.path.join(harmony_resource_path, total_harmony_qualifier, "media")

            for resource_file in os.listdir(os.path.join(android_resource_path, resource_dir)):
                if resource_file.endswith(".xml"):
                    origin_resource_file = os.path.join(android_resource_path, resource_dir, resource_file)
                    harmony_resource_file = os.path.join(_harmony_resource_base_dir,
                                                         resource_file.replace("xml", "svg"))
                    try:
                        # 避免文件名冲突
                        harmony_resource_file = rename_filepath(harmony_resource_file, overwrite)
                        translate_android_drawable_xml_to_harmony_svg(
                            origin_resource_file,
                            harmony_resource_file
                        )
                    except Exception as e:
                        logger.error(f"Failed to translate {origin_resource_file} to {harmony_resource_file}: {e}")
                elif resource_file.endswith((".png", ".jpg", ".jpeg")):
                    origin_resource_file = os.path.join(android_resource_path, resource_dir, resource_file)
                    harmony_resource_file = os.path.join(_harmony_resource_base_dir, resource_file)
                    os.makedirs(os.path.dirname(harmony_resource_file), exist_ok=True)
                    shutil.copy(origin_resource_file, harmony_resource_file)
        elif resource_dir.startswith("mipmap"):
            # TODO: 支持 mipmap 格式的资源
            # 启动图标, 目前使用默认图标
            logger.warning(f"Android Resource `{resource_dir}` is not supported")
            continue
            # if resource_dir == "mipmap":
            #     # 默认资源文件
            #     _harmony_resource_base_dir = os.path.join(harmony_resource_path, "base", "media")
            # else:
            #     # values-xxx 资源文件
            #     total_harmony_qualifier = translate_android_resource_qualifier_to_harmony(resource_dir)
            #     if total_harmony_qualifier:
            #         _harmony_resource_base_dir = os.path.join(harmony_resource_path, total_harmony_qualifier, "media")
            #     else:
            #         _harmony_resource_base_dir = os.path.join(harmony_resource_path, "base", "media")
            #
            # for resource_file in os.listdir(os.path.join(android_resource_path, resource_dir)):
            #     resource_file_type = os.path.splitext(resource_file)[1].lstrip(".")
            #     if resource_file_type == "webp":
            #         origin_resource_file = os.path.join(android_resource_path, resource_dir, resource_file)
            #         harmony_resource_file = os.path.join(_harmony_resource_base_dir,
            #                                              resource_file.replace("webp", "png"))
            #         os.makedirs(os.path.dirname(harmony_resource_file), exist_ok=True)
            #         webp_image = Image.open(origin_resource_file)
            #         webp_image.save(harmony_resource_file, "PNG")
            #     elif resource_file_type == "xml":
            #         # anydpi，合并两个 svg 文件并转换为 png
            #         harmony_resource_file = os.path.join(_harmony_resource_base_dir,
            #                                              resource_file.replace("xml", "png"))
            #         os.makedirs(os.path.dirname(harmony_resource_file), exist_ok=True)
            #
            #         mipmap_xml_root = etree.parse(os.path.join(android_resource_path, resource_dir, resource_file))
            #         mipmap_xml_background_node = mipmap_xml_root.find("background")
            #         mipmap_xml_background_file_ref = mipmap_xml_background_node.attrib[
            #             "{http://schemas.android.com/apk/res/android}drawable"]
            #         mipmap_xml_background_file = os.path.join(android_resource_path,
            #                                                   mipmap_xml_background_file_ref.lstrip("@") + ".xml")
            #         temp_background_svg, temp_background_svg_path = tempfile.mkstemp()
            #         translate_android_drawable_xml_to_harmony_svg(
            #             mipmap_xml_background_file,
            #             temp_background_svg_path
            #         )
            #         mipmap_xml_foreground_node = mipmap_xml_root.find("foreground")
            #         mipmap_xml_foreground_file_ref = mipmap_xml_foreground_node.attrib[
            #             "{http://schemas.android.com/apk/res/android}drawable"]
            #         mipmap_xml_foreground_file = os.path.join(android_resource_path,
            #                                                   mipmap_xml_foreground_file_ref.lstrip("@") + ".xml")
            #         temp_foreground_svg, temp_foreground_svg_path = tempfile.mkstemp()
            #         translate_android_drawable_xml_to_harmony_svg(
            #             mipmap_xml_foreground_file,
            #             temp_foreground_svg_path
            #         )
            #         # 合并两个 svg 文件
            #         svg1_root = etree.parse(temp_background_svg_path).getroot()
            #         svg2_root = etree.parse(temp_foreground_svg_path).getroot()
            #         combined_svg_root = etree.Element("svg", nsmap=svg1_root.nsmap)
            #         combined_svg_root.attrib.update(svg1_root.attrib)
            #         for element in svg1_root:
            #             combined_svg_root.append(element)
            #         for element in svg2_root:
            #             combined_svg_root.append(element)
            #         temp_combined_svg, temp_combined_svg_path = tempfile.mkstemp()
            #         with open(temp_combined_svg_path, "w", encoding="utf-8") as f:
            #             f.write(etree.tostring(combined_svg_root, pretty_print=True, encoding="unicode"))
            #         from svglib.svglib import svg2rlg
            #         from reportlab.graphics import renderPM
            #         drawing = svg2rlg(temp_combined_svg_path)
            #         # TODO: 渐变存在问题
            #         # 避免文件名冲突
            #         harmony_resource_file = rename_filepath(harmony_resource_file, overwrite)
            #         renderPM.drawToFile(drawing, harmony_resource_file, fmt="PNG", backendFmt="RGBA")
            #         # cairosvg.svg2png(url=temp_combined_svg_path, write_to=harmony_resource_file)
            #         os.close(temp_background_svg)
            #         os.remove(temp_background_svg_path)
            #         os.close(temp_foreground_svg)
            #         os.remove(temp_foreground_svg_path)
            #         os.close(temp_combined_svg)
            #         os.remove(temp_combined_svg_path)
            #     elif resource_file_type in (".png", ".jpg", ".jpeg"):
            #         origin_resource_file = os.path.join(android_resource_path, resource_dir, resource_file)
            #         harmony_resource_file = os.path.join(_harmony_resource_base_dir, resource_file)
            #         harmony_resource_file = rename_filepath(harmony_resource_file, overwrite)
            #         os.makedirs(os.path.dirname(harmony_resource_file), exist_ok=True)
            #         shutil.copy(origin_resource_file, harmony_resource_file)
        elif any([resource_dir.startswith(resource_type) for resource_type in ["layout", "menu", "navigation", "xml"]]):
            # 忽略 layout、menu、navigation、xml
            continue
        else:
            logger.warning(f"Android Resource `{resource_dir}` is not supported")


if __name__ == '__main__':
    translate_android_resource_to_harmony(
        r"C:\Users\14514\Desktop\bookdash\resources",
        r"C:\Users\14514\Desktop\bookdash\resources\harmony"
    )

# 你是谁
