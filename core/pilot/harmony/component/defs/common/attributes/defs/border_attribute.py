BORDER_ATTRIBUTES = {
    "border": {
        "description": "设置边框样式。",
        "params": {
            "value": {
                "type": "BorderOptions",
                "required": True,
                "description": "统一边框样式设置接口。"
            }
        }
    },
    "borderStyle": {
        "description": "设置元素的边框线条样式。",
        "params": {
            "value": {
                "type": "BorderStyle | EdgeStyles",
                "required": True,
                "description": "设置元素的边框样式。默认值：BorderStyle.Solid",
                "default": "BorderStyle.Solid"
            }
        }
    },
    "borderWidth": {
        "description": "设置边框的宽度。",
        "params": {
            "value": {
                "type": "Length | EdgeWidths | LocalizedEdgeWidths",
                "required": True,
                "description": "设置元素的边框宽度，不支持百分比。"
            }
        }
    },
    "borderColor": {
        "description": "设置边框的颜色。",
        "params": {
            "value": {
                "type": "ResourceColor | EdgeColors | LocalizedEdgeColors",
                "required": True,
                "description": "设置元素的边框颜色。默认值：Color.Black",
                "default": "Color.Black"
            }
        }
    },
    "borderRadius": {
        "description": "设置边框的圆角。",
        "params": {
            "value": {
                "type": "Length | BorderRadiuses | LocalizedBorderRadiuses",
                "required": True,
                "description": "设置元素的边框圆角半径，支持百分比，百分比依据组件宽度。"
            }
        }
    },
    "BorderOptions": {
        "description": "边框样式设置接口。",
        "params": {
            "width": {
                "type": "Length",
                "required": False,
                "description": "设置边框宽度。"
            },
            "color": {
                "type": "ResourceColor",
                "required": False,
                "description": "设置边框颜色。"
            },
            "radius": {
                "type": "Length",
                "required": False,
                "description": "设置边框圆角半径。"
            },
            "style": {
                "type": "BorderStyle",
                "required": False,
                "description": "设置边框样式。"
            }
        }
    },
    "EdgeWidths": {
        "description": "边框宽度类型，用于描述组件边框不同方向的宽度。",
        "params": {
            "left": {
                "type": "Length",
                "required": False,
                "description": "左侧边框宽度。"
            },
            "right": {
                "type": "Length",
                "required": False,
                "description": "右侧边框宽度。"
            },
            "top": {
                "type": "Length",
                "required": False,
                "description": "上侧边框宽度。"
            },
            "bottom": {
                "type": "Length",
                "required": False,
                "description": "下侧边框宽度。"
            }
        }
    },
    "LocalizedEdgeWidths": {
        "description": "边框宽度类型，用于描述组件边框不同方向的宽度。",
        "params": {
            "start": {
                "type": "LengthMetrics",
                "required": False,
                "description": "左侧边框宽度。"
            },
            "end": {
                "type": "LengthMetrics",
                "required": False,
                "description": "右侧边框宽度。"
            },
            "top": {
                "type": "LengthMetrics",
                "required": False,
                "description": "上侧边框宽度。"
            },
            "bottom": {
                "type": "LengthMetrics",
                "required": False,
                "description": "下侧边框宽度。"
            }
        }
    },
    "EdgeColors": {
        "description": "边框颜色，用于描述组件边框四条边的颜色。",
        "params": {
            "left": {
                "type": "ResourceColor",
                "required": False,
                "description": "左侧边框颜色。"
            },
            "right": {
                "type": "ResourceColor",
                "required": False,
                "description": "右侧边框颜色。"
            },
            "top": {
                "type": "ResourceColor",
                "required": False,
                "description": "上侧边框颜色。"
            },
            "bottom": {
                "type": "ResourceColor",
                "required": False,
                "description": "下侧边框颜色。"
            }
        }
    },
    "LocalizedEdgeColors": {
        "description": "边框颜色，用于描述组件边框四条边的颜色。",
        "params": {
            "start": {
                "type": "ResourceColor",
                "required": False,
                "description": "左侧边框颜色。"
            },
            "end": {
                "type": "ResourceColor",
                "required": False,
                "description": "右侧边框颜色。"
            },
            "top": {
                "type": "ResourceColor",
                "required": False,
                "description": "上侧边框颜色。"
            },
            "bottom": {
                "type": "ResourceColor",
                "required": False,
                "description": "下侧边框颜色。"
            }
        }
    },
    "BorderRadiuses": {
        "description": "圆角类型，用于描述组件边框圆角半径。",
        "params": {
            "topLeft": {
                "type": "Length",
                "required": False,
                "description": "左上角圆角半径。"
            },
            "topRight": {
                "type": "Length",
                "required": False,
                "description": "右上角圆角半径。"
            },
            "bottomLeft": {
                "type": "Length",
                "required": False,
                "description": "左下角圆角半径。"
            },
            "bottomRight": {
                "type": "Length",
                "required": False,
                "description": "右下角圆角半径。"
            }
        }
    },
    "LocalizedBorderRadiuses": {
        "description": "圆角类型，用于描述组件边框圆角半径。",
        "params": {
            "topStart": {
                "type": "LengthMetrics",
                "required": False,
                "description": "左上角圆角半径。"
            },
            "topEnd": {
                "type": "LengthMetrics",
                "required": False,
                "description": "右上角圆角半径。"
            },
            "bottomStart": {
                "type": "LengthMetrics",
                "required": False,
                "description": "左下角圆角半径。"
            },
            "bottomEnd": {
                "type": "LengthMetrics",
                "required": False,
                "description": "右下角圆角半径。"
            }
        }
    },
    "EdgeStyles": {
        "description": "边框样式类型，用于描述组件边框不同方向的样式。",
        "params": {
            "left": {
                "type": "BorderStyle",
                "required": False,
                "description": "左侧边框样式。"
            },
            "right": {
                "type": "BorderStyle",
                "required": False,
                "description": "右侧边框样式。"
            },
            "top": {
                "type": "BorderStyle",
                "required": False,
                "description": "上侧边框样式。"
            },
            "bottom": {
                "type": "BorderStyle",
                "required": False,
                "description": "下侧边框样式。"
            }
        }
    },
    "example": [
        """\n\n// xxx.ets\n@Entry\n@Component\nstruct BorderExample {\n  build() {\n    Column() {\n      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {\n        // 线段\n        Text('dashed')\n          .borderStyle(BorderStyle.Dashed).borderWidth(5).borderColor(0xAFEEEE).borderRadius(10)\n          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)\n          // 创建一个带有虚线边框的文本组件，边框颜色为浅蓝色，边框宽度为5，边框半径为10\n\n        // 点线\n        Text('dotted')\n          .border({ width: 5, color: 0x317AF7, radius: 10, style: BorderStyle.Dotted })\n          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)\n          // 创建一个带有点线边框的文本组件，边框颜色为蓝色，边框宽度为5，边框半径为10\n      }.width('100%').height(150)\n\n      Text('.border')\n        .fontSize(50)\n        .width(300)\n        .height(300)\n        .border({\n          width: { left: 3, right: 6, top: 10, bottom: 15 },\n          color: { left: '#e3bbbb', right: Color.Blue, top: Color.Red, bottom: Color.Green },\n          radius: { topLeft: 10, topRight: 20, bottomLeft: 40, bottomRight: 80 },\n          style: {\n            left: BorderStyle.Dotted,\n            right: BorderStyle.Dotted,\n            top: BorderStyle.Solid,\n            bottom: BorderStyle.Dashed\n          }\n        }).textAlign(TextAlign.Center)\n        // 创建一个文本组件，其边框具有不同的宽度、颜色、半径和样式。\n        // 左边框为点线，宽度为3，颜色为浅红色；右边框为点线，宽度为6，颜色为蓝色；\n        // 上边框为实线，宽度为10，颜色为红色；下边框为虚线，宽度为15，颜色为绿色。\n        // 边框半径分别为左上角10，右上角20，左下角40，右下角80。\n    }\n  }\n}    """
    ]
}
