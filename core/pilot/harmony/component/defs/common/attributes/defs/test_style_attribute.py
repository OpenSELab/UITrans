TEXT_STYLE_ATTRIBUTE = {
    "fontColor": {
        "description": "设置字体颜色。",
        "params": {
            "value": {
                "type": "ResourceColor",
                "required": True,
                "description": "字体颜色。"
            }
        }
    },
    "fontSize": {
        "description": "设置字体大小。",
        "params": {
            "value": {
                "type": ["number", "string", "Resource"],
                "required": True,
                "description": "字体大小。fontSize为number类型时，使用fp单位。字体默认大小16fp。不支持设置百分比字符串。",
                "default": "16fp"
            }
        }
    },
    "fontStyle": {
        "description": "设置字体样式。",
        "params": {
            "value": {
                "type": "FontStyle",
                "required": True,
                "description": "字体样式。默认值：FontStyle.Normal",
                "default": "FontStyle.Normal"
            }
        }
    },
    "fontWeight": {
        "description": "设置文本的字体粗细，设置过大可能会在不同字体下有截断。",
        "params": {
            "value": {
                "type": ["number", "FontWeight", "string"],
                "required": True,
                "description": "文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如\"400\"，以及\"bold\"、\"bolder\"、\"lighter\"、\"regular\"、\"medium\"，分别对应FontWeight中相应的枚举值。默认值：FontWeight.Normal",
                "default": "FontWeight.Normal"
            }
        }
    },
    "fontFamily": {
        "description": "设置字体列表。",
        "params": {
            "value": {
                "type": ["string", "Resource"],
                "required": True,
                "description": "字体列表。默认字体'HarmonyOS Sans'。应用当前支持'HarmonyOS Sans'字体和注册自定义字体。卡片当前仅支持'HarmonyOS Sans'字体。",
                "default": 'HarmonyOS Sans'
            }
        }
    },
    "lineHeight": {
        "description": "设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小。",
        "params": {
            "value": {
                "type": ["number", "string", "Resource"],
                "required": True,
                "description": "文本行高，为number类型时单位为fp。"
            }
        }
    },
    "decoration": {
        "description": "设置文本装饰线样式及其颜色。",
        "params": {
            "value": {
                "type": "DecorationStyleInterface",
                "required": True,
                "description": "文本装饰线样式对象。默认值：{ type: TextDecorationType.None, color: Color.Black, style: TextDecorationStyle.SOLID } 说明：style参数不支持卡片能力。",
                "default": "{ type: TextDecorationType.None, color: Color.Black, style: TextDecorationStyle.SOLID } "
            }
        }
    },
    # "example": [
    #     """// xxx.ets\\n@Entry\\n@Component\\nstruct TextStyleExample {\\n  build() {\\n    Column({ space: 5 }) {\\n      // 默认样式的文本\\n      Text('default text')\\n      \\n      // 设置文本颜色为红色\\n      Text('text font color red').fontColor(Color.Red)\\n      \\n      // 默认样式的文本\\n      Text('text font default')\\n      \\n      // 设置文本字体大小为10像素\\n      Text('text font size 10').fontSize(10)\\n      \\n      // 设置文本字体大小为10fp（字体像素）\\n      Text('text font size 10fp').fontSize('10fp')\\n      \\n      // 设置文本字体大小为20像素\\n      Text('text font size 20').fontSize(20)\\n      \\n      // 设置文本字体样式为斜体\\n      Text('text font style Italic').fontStyle(FontStyle.Italic)\\n      \\n      // 设置文本字体粗细为700（粗体）\\n      Text('text fontWeight bold').fontWeight(700)\\n      \\n      // 设置文本字体粗细为较细\\n      Text('text fontWeight lighter').fontWeight(FontWeight.Lighter)\\n      \\n      // 设置文本颜色为红色，字体大小为20像素，字体样式为斜体，字体粗细为粗体\\n      Text('red 20 Italic bold text')\\n        .fontColor(Color.Red)\\n        .fontSize(20)\\n        .fontStyle(FontStyle.Italic)\\n        .fontWeight(FontWeight.Bold)\\n      \\n      // 设置文本颜色为橙色，字体大小为18像素，字体样式为正常\\n      Text('Orange 18 Normal text')\\n        .fontColor(Color.Orange)\\n        .fontSize(18)\\n        .fontStyle(FontStyle.Normal)\\n    }.width('100%')\\n  }\\n}"""
    # ]
}
