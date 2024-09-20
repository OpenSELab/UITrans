DRAWING_COMPONENT = {
    "Circle": {
        "description": "用于绘制圆形的组件。",
        "interfaces": [
            {
                "description": "Circle(value?: CircleOptions)",
                "params": {
                    "value": {
                        "type": "CircleOptions",
                        "description": "设置圆形尺寸"
                    }
                }
            }
        ],
        "attributes": {
            "fill": {
                "description": "设置填充区域颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "填充区域颜色。",
                        "default": "Color.Black"
                    }
                }
            },
            "fillOpacity": {
                "description": "设置填充区域透明度。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "填充区域透明度。",
                        "default": 1
                    }
                }
            },
            "stroke": {
                "description": "设置边框颜色，不设置时，默认没有边框。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "边框颜色。"
                    }
                }
            },
            "strokeDashArray": {
                "description": "设置边框间隙。",
                "params": {
                    "value": {
                        "type": "Array<any>",
                        "required": True,
                        "description": "边框间隙。",
                        "default": []
                    }
                }
            },
            "strokeDashOffset": {
                "description": "设置边框绘制起点的偏移量。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "边框绘制起点的偏移量。",
                        "default": 0
                    }
                }
            },
            "strokeLineCap": {
                "description": "设置边框端点绘制样式。",
                "params": {
                    "value": {
                        "type": "LineCapStyle",
                        "required": True,
                        "description": "边框端点绘制样式。",
                        "default": "LineCapStyle.Butt"
                    }
                }
            },
            "strokeLineJoin": {
                "description": "设置边框拐角绘制样式。Circle组件无法形成拐角，该属性设置无效。",
                "params": {
                    "value": {
                        "type": "LineJoinStyle",
                        "required": True,
                        "description": "边框拐角绘制样式。",
                        "default": "LineJoinStyle.Miter"
                    }
                }
            },
            "strokeMiterLimit": {
                "description": "设置斜接长度与边框宽度比值的极限值。Circle组件无法设置尖角图形，该属性设置无效。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "斜接长度与边框宽度比值的极限值。",
                        "default": 4
                    }
                }
            },
            "strokeOpacity": {
                "description": "设置边框透明度。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "边框透明度。",
                        "default": 1
                    }
                }
            },
            "strokeWidth": {
                "description": "设置边框宽度。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "边框宽度。",
                        "default": 1
                    }
                }
            },
            "antiAlias": {
                "description": "设置是否开启抗锯齿效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启抗锯齿效果。",
                        "default": True
                    }
                }
            }
        },
        "events": {}
    },
    "Ellipse": {
        "description": "椭圆绘制组件。",
        "details": "该组件从API Version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。从API version 11开始，该接口支持在元服务中使用。",
        "interfaces": [
            {
                "description": "Ellipse(options?: {width?: string | number, height?: string | number})",
                "params": {
                    "width": {
                        "type": ["string", "number"],
                        "description": "宽度，异常值按照默认值处理。",
                        "default": 0
                    },
                    "height": {
                        "type": ["string", "number"],
                        "description": "高度，异常值按照默认值处理。",
                        "default": 0
                    }
                }
            }
        ],
        "attributes": {
            "fill": {
                "description": "设置填充区域颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "填充区域颜色。",
                        "default": "Color.Black"
                    }
                }
            },
            "fillOpacity": {
                "description": "设置填充区域透明度。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "填充区域透明度。",
                        "default": 1
                    }
                }
            },
            "stroke": {
                "description": "设置边框颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "边框颜色。"
                    }
                }
            },
            "strokeDashArray": {
                "description": "设置边框间隙。",
                "params": {
                    "value": {
                        "type": "Array<any>",
                        "required": True,
                        "description": "边框间隙。",
                        "default": []
                    }
                }
            },
            "strokeDashOffset": {
                "description": "设置边框绘制起点的偏移量。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "边框绘制起点的偏移量。",
                        "default": 0
                    }
                }
            },
            "strokeLineCap": {
                "description": "设置边框端点绘制样式。",
                "params": {
                    "value": {
                        "type": "LineCapStyle",
                        "required": True,
                        "description": "边框端点绘制样式。",
                        "default": "LineCapStyle.Butt"
                    }
                }
            },
            "strokeLineJoin": {
                "description": "设置边框拐角绘制样式。Ellipse组件无法形成拐角，该属性设置无效。",
                "params": {
                    "value": {
                        "type": "LineJoinStyle",
                        "required": True,
                        "description": "边框拐角绘制样式。",
                        "default": "LineJoinStyle.Miter"
                    }
                }
            },
            "strokeMiterLimit": {
                "description": "设置斜接长度与边框宽度比值的极限值。Ellipse组件无法设置尖角图形，该属性设置无效。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "斜接长度与边框宽度比值的极限值。",
                        "default": 4
                    }
                }
            },
            "strokeOpacity": {
                "description": "设置边框透明度。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "边框透明度。",
                        "default": 1
                    }
                }
            },
            "strokeWidth": {
                "description": "设置边框宽度。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "边框宽度。",
                        "default": 1
                    }
                }
            },
            "antiAlias": {
                "description": "设置是否开启抗锯齿效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启抗锯齿效果。",
                        "default": True
                    }
                }
            }
        },
        "events": {},
        "rules": None,
        "examples": None,
        "is_common_attrs": True
    },
    "Line": {
        "description": "直线绘制组件。",
        "interfaces": [
            {
                "description": "Line(value?: {width?: string | number, height?: string | number})",
                "params": {
                    "value": {
                        "type": ["string", "number"],
                        "description": "宽度。值为异常值或缺省时按照自身内容需要的宽度处理。"
                    },
                    "height": {
                        "type": ["string", "number"],
                        "description": "高度。值为异常值或缺省时按照自身内容需要的高度处理。"
                    }
                }
            }
        ],
        "attributes": {
            "startPoint": {
                "description": "设置直线起点坐标点（相对坐标），异常值按照默认值处理。",
                "params": {
                    "value": {
                        "type": ["Array<Length>"],
                        "required": True,
                        "description": "直线起点坐标点（相对坐标），单位vp。",
                        "default": [0, 0]
                    }
                }
            },
            "endPoint": {
                "description": "设置直线终点坐标点（相对坐标），异常值按照默认值处理。",
                "params": {
                    "value": {
                        "type": ["Array<Length>"],
                        "required": True,
                        "description": "直线终点坐标点（相对坐标），单位vp。",
                        "default": [0, 0]
                    }
                }
            },
            "fill": {
                "description": "设置填充区域颜色。Line组件无法形成闭合区域，该属性设置无效。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "填充区域颜色。"
                    }
                }
            },
            "fillOpacity": {
                "description": "设置填充区域透明度。Line组件无法形成闭合区域，该属性设置无效。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "填充区域透明度。",
                        "default": 1
                    }
                }
            },
            "stroke": {
                "description": "设置边框颜色，不设置时，默认没有边框。异常值不会绘制边框线条。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "边框颜色。"
                    }
                }
            },
            "strokeDashArray": {
                "description": "设置边框间隙。线段相交时可能会出现重叠现象。异常值按照默认值处理。",
                "params": {
                    "value": {
                        "type": ["Array<Length>"],
                        "required": True,
                        "description": "边框间隙。",
                        "default": []
                    }
                }
            },
            "strokeDashOffset": {
                "description": "设置边框绘制起点的偏移量。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "边框绘制起点的偏移量。",
                        "default": 0
                    }
                }
            },
            "strokeLineCap": {
                "description": "设置边框端点绘制样式。",
                "params": {
                    "value": {
                        "type": "LineCapStyle",
                        "required": True,
                        "description": "边框端点绘制样式。",
                        "default": "LineCapStyle.Butt"
                    }
                }
            },
            "strokeLineJoin": {
                "description": "设置边框拐角绘制样式。Line组件无法形成拐角，该属性设置无效。",
                "params": {
                    "value": {
                        "type": "LineJoinStyle",
                        "required": True,
                        "description": "边框拐角绘制样式。",
                        "default": "LineJoinStyle.Miter"
                    }
                }
            },
            "strokeMiterLimit": {
                "description": "设置锐角绘制成斜角的极限值。Line组件无法设置锐角图形，该属性设置无效。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "锐角绘制成斜角的极限值。",
                        "default": 4
                    }
                }
            },
            "strokeOpacity": {
                "description": "设置边框透明度。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "边框透明度。",
                        "default": 1
                    }
                }
            },
            "strokeWidth": {
                "description": "设置边框宽度。该属性若为string类型, 暂不支持百分比，百分比按照1px处理。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "边框宽度。",
                        "default": 1
                    }
                }
            },
            "antiAlias": {
                "description": "设置是否开启抗锯齿效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启抗锯齿效果。",
                        "default": True
                    }
                }
            }
        },
        "events": {},
        "rules": None,
        "examples": None,
        "is_common_attrs": True
    },
    "Polyline": {
        "description": "折线绘制组件。",
        "interfaces": [
            {
                "description": "Polyline(value?: {width?: string | number, height?: string | number})",
                "params": {
                    "value": {
                        "type": ["object"],
                        "description": "可选参数对象，包含宽度和高度。",
                        "params": {
                            "width": {
                                "type": ["string", "number"],
                                "required": False,
                                "description": "宽度。",
                                "default": "0"
                            },
                            "height": {
                                "type": ["string", "number"],
                                "required": False,
                                "description": "高度。",
                                "default": "0"
                            }
                        }
                    }
                }
            }
        ],
        "attributes": {
            "points": {
                "description": "设置折线经过坐标点列表。",
                "params": {
                    "value": {
                        "type": [
                            "Array<[Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-drawing-components-polyline-V5#point)>"],
                        "required": True,
                        "description": "折线经过坐标点列表。",
                        "default": "[]"
                    }
                }
            },
            "fill": {
                "description": "设置填充区域颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "填充区域颜色。"
                    }
                }
            },
            "fillOpacity": {
                "description": "设置填充区域透明度。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "填充区域透明度。",
                        "default": "1"
                    }
                }
            },
            "stroke": {
                "description": "设置边框颜色，不设置时，默认没有边框线条。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "边框颜色。"
                    }
                }
            },
            "strokeDashArray": {
                "description": "设置线条间隙。",
                "params": {
                    "value": {
                        "type": ["Array<any>"],
                        "required": True,
                        "description": "线条间隙。",
                        "default": "[]"
                    }
                }
            },
            "strokeDashOffset": {
                "description": "设置线条绘制起点的偏移量。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "线条绘制起点的偏移量。",
                        "default": "0"
                    }
                }
            },
            "strokeLineCap": {
                "description": "设置线条端点绘制样式。",
                "params": {
                    "value": {
                        "type": "LineCapStyle",
                        "required": True,
                        "description": "线条端点绘制样式。",
                        "default": "LineCapStyle.Butt"
                    }
                }
            },
            "strokeLineJoin": {
                "description": "设置线条拐角绘制样式。",
                "params": {
                    "value": {
                        "type": "LineJoinStyle",
                        "required": True,
                        "description": "线条拐角绘制样式。",
                        "default": "LineJoinStyle.Miter"
                    }
                }
            },
            "strokeMiterLimit": {
                "description": "设置斜接长度与边框宽度比值的极限值。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "斜接长度与边框宽度比值的极限值。",
                        "default": "4"
                    }
                }
            },
            "strokeOpacity": {
                "description": "设置线条透明度。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "线条透明度。",
                        "default": "1"
                    }
                }
            },
            "strokeWidth": {
                "description": "设置线条宽度。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "线条宽度。",
                        "default": "1"
                    }
                }
            },
            "antiAlias": {
                "description": "设置是否开启抗锯齿效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启抗锯齿效果。",
                        "default": "true"
                    }
                }
            }
        },
        "events": {}
    },
    "Polygon": {
        "description": "多边形绘制组件。",
        "interfaces": [
            {
                "description": "Polygon(value?: {width?: string | number, height?: string | number})",
                "params": {
                    "value": {
                        "type": [
                            "object",
                            "null"
                        ],
                        "description": "组件的初始化参数。",
                        "default": None
                    },
                    "width": {
                        "type": [
                            "string",
                            "number"
                        ],
                        "description": "宽度。",
                        "default": 0
                    },
                    "height": {
                        "type": [
                            "string",
                            "number"
                        ],
                        "description": "高度。",
                        "default": 0
                    }
                }
            }
        ],
        "attributes": {
            "points": {
                "description": "设置多边形的顶点坐标列表。",
                "params": {
                    "value": {
                        "type": "Array<[Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-drawing-components-polyline-V5#point)>",
                        "required": True,
                        "description": "多边形的顶点坐标列表。",
                        "default": []
                    }
                }
            },
            "fill": {
                "description": "设置填充区域颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "填充区域颜色。"
                    }
                }
            },
            "fillOpacity": {
                "description": "设置填充区域透明度。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string",
                            "Resource"
                        ],
                        "required": True,
                        "description": "填充区域透明度。",
                        "default": 1
                    }
                }
            },
            "stroke": {
                "description": "设置边框颜色，不设置时，默认没有边框。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "边框颜色。"
                    }
                }
            },
            "strokeDashArray": {
                "description": "设置边框间隙。",
                "params": {
                    "value": {
                        "type": "Array<any>",
                        "required": True,
                        "description": "边框间隙。",
                        "default": []
                    }
                }
            },
            "strokeDashOffset": {
                "description": "设置边框绘制起点的偏移量。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string"
                        ],
                        "required": True,
                        "description": "边框绘制起点的偏移量。",
                        "default": 0
                    }
                }
            },
            "strokeLineCap": {
                "description": "设置边框端点绘制样式。",
                "params": {
                    "value": {
                        "type": "LineCapStyle",
                        "required": True,
                        "description": "边框端点绘制样式。",
                        "default": "LineCapStyle.Butt"
                    }
                }
            },
            "strokeLineJoin": {
                "description": "设置边框拐角绘制样式。",
                "params": {
                    "value": {
                        "type": "LineJoinStyle",
                        "required": True,
                        "description": "边框拐角绘制样式。",
                        "default": "LineJoinStyle.Miter"
                    }
                }
            },
            "strokeMiterLimit": {
                "description": "设置斜接长度与边框宽度比值的极限值。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string"
                        ],
                        "required": True,
                        "description": "斜接长度与边框宽度比值的极限值。",
                        "default": 4
                    }
                }
            },
            "strokeOpacity": {
                "description": "设置边框透明度。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string",
                            "Resource"
                        ],
                        "required": True,
                        "description": "边框透明度。",
                        "default": 1
                    }
                }
            },
            "strokeWidth": {
                "description": "设置边框宽度。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "边框宽度。",
                        "default": 1
                    }
                }
            },
            "antiAlias": {
                "description": "设置是否开启抗锯齿效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启抗锯齿效果。",
                        "default": True
                    }
                }
            }
        },
        "events": {}
    },
    "Path": {
        "description": "路径绘制组件，根据绘制路径生成封闭的自定义形状。",
        "interfaces": [
            {
                "description": "Path(value?: { width?: number | string; height?: number | string; commands?: string })",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "description": "路径所在矩形的宽度。值为异常值或缺省时按照自身内容需要的宽度处理。"
                    },
                    "height": {
                        "type": ["number", "string"],
                        "description": "路径所在矩形的高度。值为异常值或缺省时按照自身内容需要的高度处理。"
                    },
                    "commands": {
                        "type": "string",
                        "description": "路径绘制的命令字符串。默认值：''。异常值按照默认值处理。"
                    }
                }
            }
        ],
        "attributes": {
            "commands": {
                "description": "设置路径绘制的命令字符串，单位为px。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "线条绘制的路径。"
                    }
                }
            },
            "fill": {
                "description": "设置填充区域颜色。异常值按照默认值处理。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "填充区域颜色。"
                    }
                }
            },
            "fillOpacity": {
                "description": "设置填充区域透明度。取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "填充区域透明度。",
                        "default": 1
                    }
                }
            },
            "stroke": {
                "description": "设置边框颜色，不设置时，默认没有边框线条。异常值不会绘制边框线条。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "边框颜色。"
                    }
                }
            },
            "strokeDashArray": {
                "description": "设置线条间隙。线段相交时可能会出现重叠现象。异常值按照默认值处理。",
                "params": {
                    "value": {
                        "type": "Array<any>",
                        "required": True,
                        "description": "线条间隙。",
                        "default": []
                    }
                }
            },
            "strokeDashOffset": {
                "description": "设置线条绘制起点的偏移量。异常值按照默认值处理。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "线条绘制起点的偏移量。",
                        "default": 0
                    }
                }
            },
            "strokeLineCap": {
                "description": "设置线条端点绘制样式。",
                "params": {
                    "value": {
                        "type": "LineCapStyle",
                        "required": True,
                        "description": "线条端点绘制样式。",
                        "default": "LineCapStyle.Butt"
                    }
                }
            },
            "strokeLineJoin": {
                "description": "设置线条拐角绘制样式。",
                "params": {
                    "value": {
                        "type": "LineJoinStyle",
                        "required": True,
                        "description": "线条拐角绘制样式。",
                        "default": "LineJoinStyle.Miter"
                    }
                }
            },
            "strokeMiterLimit": {
                "description": "设置斜接长度与边框宽度比值的极限值。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "斜接长度与边框宽度比值的极限值。",
                        "default": 4
                    }
                }
            },
            "strokeOpacity": {
                "description": "设置线条透明度。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "线条透明度。",
                        "default": 1
                    }
                }
            },
            "strokeWidth": {
                "description": "设置线条宽度。该属性若为string类型, 暂不支持百分比，百分比按照1px处理。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "线条宽度。",
                        "default": 1
                    }
                }
            },
            "antiAlias": {
                "description": "设置是否开启抗锯齿效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启抗锯齿效果。",
                        "default": True
                    }
                }
            }
        },
        "events": {},
        "rules": None,
        "examples": None,
        "is_common_attrs": True
    },
    "Rect": {
        "description": "绘制组件的父组件，实现类似SVG的效果。绘制组件单独使用，用于在页面上绘制指定的图形。",
        "interfaces": [
            {
                "description": "Shape(value?: PixelMap)",
                "params": {
                    "value": {
                        "type": "PixelMap",
                        "required": False,
                        "description": "绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则在当前绘制目标中进行绘制。"
                    }
                }
            }
        ],
        "attributes": {
            "viewPort": {
                "description": "设置形状的视口。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string"
                        ],
                        "required": True,
                        "description": "形状的视口。",
                        "default": {
                            "x": 0,
                            "y": 0,
                            "width": 0,
                            "height": 0
                        }
                    }
                }
            },
            "fill": {
                "description": "设置填充区域颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "填充区域颜色。"
                    }
                }
            },
            "fillOpacity": {
                "description": "设置填充区域透明度。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string",
                            "Resource"
                        ],
                        "required": True,
                        "description": "填充区域透明度。",
                        "default": 1
                    }
                }
            },
            "stroke": {
                "description": "设置边框颜色，不设置时，默认没有边框。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "边框颜色。"
                    }
                }
            },
            "strokeDashArray": {
                "description": "设置边框间隙。",
                "params": {
                    "value": {
                        "type": "Array<any>",
                        "required": True,
                        "description": "边框间隙。",
                        "default": []
                    }
                }
            },
            "strokeDashOffset": {
                "description": "设置边框绘制起点的偏移量。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string"
                        ],
                        "required": True,
                        "description": "边框绘制起点的偏移量。",
                        "default": 0
                    }
                }
            },
            "strokeLineCap": {
                "description": "设置边框端点绘制样式。",
                "params": {
                    "value": {
                        "type": "LineCapStyle",
                        "required": True,
                        "description": "边框端点绘制样式。",
                        "default": "LineCapStyle.Butt"
                    }
                }
            },
            "strokeLineJoin": {
                "description": "设置边框拐角绘制样式。",
                "params": {
                    "value": {
                        "type": "LineJoinStyle",
                        "required": True,
                        "description": "边框拐角绘制样式。",
                        "default": "LineJoinStyle.Miter"
                    }
                }
            },
            "strokeMiterLimit": {
                "description": "设置斜接长度与边框宽度比值的极限值。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string"
                        ],
                        "required": True,
                        "description": "斜接长度与边框宽度比值的极限值。",
                        "default": 4
                    }
                }
            },
            "strokeOpacity": {
                "description": "设置边框透明度。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string",
                            "Resource"
                        ],
                        "required": True,
                        "description": "边框透明度。",
                        "default": 1
                    }
                }
            },
            "strokeWidth": {
                "description": "设置边框宽度。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "边框宽度。",
                        "default": 1
                    }
                }
            },
            "antiAlias": {
                "description": "设置是否开启抗锯齿效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启抗锯齿效果。",
                        "default": True
                    }
                }
            },
            "mesh": {
                "description": "设置mesh效果。",
                "params": {
                    "value": {
                        "type": "Array<number>",
                        "required": True,
                        "description": "长度（column + 1）* （row + 1）* 2的数组，它记录了扭曲后的位图各个顶点位置。"
                    },
                    "column": {
                        "type": "number",
                        "required": True,
                        "description": "mesh矩阵列数。"
                    },
                    "row": {
                        "type": "number",
                        "required": True,
                        "description": "mesh矩阵行数。"
                    }
                }
            }
        },
        "events": {}
    },
    "Shape": {
        "description": "矩形绘制组件。",
        "interfaces": [
            {
                "description": "Rect(value?: {width?: string | number, height?: string | number, radius?: string | number | Array<string | number>} | {width?: string | number, height?: string | number, radiusWidth?: string | number, radiusHeight?: string | number})",
                "params": {
                    "width": {
                        "type": ["string", "number"],
                        "description": "宽度，异常值按照默认值处理。",
                        "default": "0"
                    },
                    "height": {
                        "type": ["string", "number"],
                        "description": "高度，异常值按照默认值处理。",
                        "default": "0"
                    },
                    "radius": {
                        "type": ["string", "number", "Array<string | number>"],
                        "description": "圆角半径，支持分别设置四个角的圆角度数，异常值按照默认值处理。",
                        "default": "0"
                    },
                    "radiusWidth": {
                        "type": ["string", "number"],
                        "description": "圆角宽度，异常值按照默认值处理。",
                        "default": "0"
                    },
                    "radiusHeight": {
                        "type": ["string", "number"],
                        "description": "圆角高度，异常值按照默认值处理。",
                        "default": "0"
                    }
                }
            }
        ],
        "attributes": {
            "width": {
                "description": "宽度。",
                "params": {
                    "value": {
                        "type": ["string", "number"],
                        "description": "宽度值。",
                        "default": "0"
                    }
                }
            },
            "height": {
                "description": "高度。",
                "params": {
                    "value": {
                        "type": ["string", "number"],
                        "description": "高度值。",
                        "default": "0"
                    }
                }
            },
            "radius": {
                "description": "圆角半径，支持分别设置四个角的圆角度数。",
                "params": {
                    "value": {
                        "type": ["string", "number", "Array<string | number>"],
                        "description": "圆角半径值。",
                        "default": "0"
                    }
                }
            },
            "radiusWidth": {
                "description": "圆角宽度。",
                "params": {
                    "value": {
                        "type": ["string", "number"],
                        "description": "圆角宽度值。",
                        "default": "0"
                    }
                }
            },
            "radiusHeight": {
                "description": "圆角高度。",
                "params": {
                    "value": {
                        "type": ["string", "number"],
                        "description": "圆角高度值。",
                        "default": "0"
                    }
                }
            }
        },
        "events": {}
    }
}
