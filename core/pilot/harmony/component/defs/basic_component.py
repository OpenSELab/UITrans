BASIC_COMPONENT = {
    "AlphabetIndexer": {
        "description": "可以与容器组件联动用于按逻辑结构快速定位容器显示区域的组件。",
        "interfaces": [
            {
                "description": "AlphabetIndexer(value: {arrayValue: Array<string>, selected: number})",
                "params": {
                    "value": {
                        "type": "object",
                        "required": True,
                        "description": "包含字母索引字符串数组和初始选中项索引值的对象",
                        "properties": {
                            "arrayValue": {
                                "type": ["string"],
                                "required": True,
                                "description": "字母索引字符串数组，不可设置为空。"
                            },
                            "selected": {
                                "type": "number",
                                "required": True,
                                "description": "初始选中项索引值，若超出索引值范围，则取默认值0。从API version 10开始，该参数支持双向绑定变量。"
                            }
                        }
                    }
                }
            }
        ],
        "attributes": {
            "color": {
                "description": "设置文字颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "文字颜色。"
                    }
                }
            },
            "selectedColor": {
                "description": "设置选中项文字颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "选中项文字颜色。"
                    }
                }
            },
            "popupColor": {
                "description": "设置提示弹窗文字颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "提示弹窗文字颜色。"
                    }
                }
            },
            "selectedBackgroundColor": {
                "description": "设置选中项背景颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "选中项背景颜色。"
                    }
                }
            },
            "popupBackground": {
                "description": "设置提示弹窗背景色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "提示弹窗背景色。",
                        "default": "#66808080"
                    }
                }
            },
            "usingPopup": {
                "description": "设置是否使用提示弹窗。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否使用提示弹窗。",
                        "default": False
                    }
                }
            },
            "selectedFont": {
                "description": "设置选中项文字样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "选中项文字样式。",
                        "default": {
                            "size": "10.0vp",
                            "style": "FontStyle.Normal",
                            "weight": "FontWeight.Medium",
                            "family": "HarmonyOS Sans"
                        }
                    }
                }
            },
            "popupFont": {
                "description": "设置提示弹窗字体样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "提示弹窗字体样式。",
                        "default": {
                            "size": "24.0vp",
                            "style": "FontStyle.Normal",
                            "weight": "FontWeight.Normal",
                            "family": "HarmonyOS Sans"
                        }
                    }
                }
            },
            "font": {
                "description": "设置字母索引条默认字体样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "字母索引条默认字体样式。",
                        "default": {
                            "size": "10.0vp",
                            "style": "FontStyle.Normal",
                            "weight": "FontWeight.Medium",
                            "family": "HarmonyOS Sans"
                        }
                    }
                }
            },
            "itemSize": {
                "description": "设置字母索引条字母区域大小。",
                "params": {
                    "value": {
                        "type": ["string", "number"],
                        "required": True,
                        "description": "字母索引条字母区域大小，字母区域为正方形，即正方形边长。不支持设置为百分比。",
                        "default": 16.0
                    }
                }
            },
            "alignStyle": {
                "description": "设置字母索引条弹框的对齐样式。",
                "params": {
                    "value": {
                        "type": "IndexerAlign",
                        "required": True,
                        "description": "字母索引条弹框的对齐样式，支持弹窗显示在索引条右侧和左侧。",
                        "default": "IndexerAlign.END"
                    },
                    "offset": {
                        "type": "Length",
                        "required": False,
                        "description": "提示弹窗与索引条之间间距，大于等于0为有效值，在不设置或设置为小于0的情况下间距与popupPosition.x相同。与popupPosition同时设置时，水平方向上offset生效，竖直方向上popupPosition.y生效。"
                    }
                }
            },
            "selected": {
                "description": "设置选中项索引值。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "选中项索引值。",
                        "default": 0
                    }
                }
            },
            "popupPosition": {
                "description": "设置弹出窗口相对于索引器条上边框中点的位置。",
                "params": {
                    "value": {
                        "type": "Position",
                        "required": True,
                        "description": "弹出窗口相对于索引器条上边框中点的位置。",
                        "default": {
                            "x": 60.0,
                            "y": 48.0
                        }
                    }
                }
            },
            "popupSelectedColor": {
                "description": "设置提示弹窗非字母部分选中文字色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "提示弹窗非字母部分选中文字色。"
                    }
                }
            },
            "popupUnselectedColor": {
                "description": "设置提示弹窗非字母部分未选中文字色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "提示弹窗非字母部分未选中文字色。",
                        "default": "#FF182431"
                    }
                }
            },
            "popupItemFont": {
                "description": "设置提示弹窗非字母部分字体样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "提示弹窗非字母部分字体样式。",
                        "default": {
                            "size": 24,
                            "weight": "FontWeight.Medium"
                        }
                    }
                }
            },
            "popupItemBackgroundColor": {
                "description": "设置提示弹窗非字母部分背景色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "提示弹窗非字母部分背景色。",
                        "default": "#00000000"
                    }
                }
            },
            "autoCollapse": {
                "description": "设置是否使用自适应折叠模式。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否使用自适应折叠模式。",
                        "default": False
                    }
                }
            },
            "popupItemBorderRadius": {
                "description": "设置提示弹窗索引项背板圆角半径。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "提示弹窗索引项背板圆角半径。",
                        "default": 24
                    }
                }
            },
            "itemBorderRadius": {
                "description": "设置索引项背板圆角半径。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "索引项背板圆角半径。",
                        "default": 8
                    }
                }
            },
            "popupBackgroundBlurStyle": {
                "description": "设置提示弹窗的背景模糊材质。",
                "params": {
                    "value": {
                        "type": "BlurStyle",
                        "required": True,
                        "description": "提示弹窗的背景模糊材质。",
                        "default": "COMPONENT_REGULAR"
                    }
                }
            },
            "popupTitleBackground": {
                "description": "设置提示弹窗首个索引项背板颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "提示弹窗首个索引项背板颜色。",
                        "default": {
                            "提示弹窗只有一个索引项": "#00FFFFFF",
                            "提示弹窗有多个索引项": "#0c182431"
                        }
                    }
                }
            },
            "enableHapticFeedback": {
                "description": "支持触控反馈。",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "required": False,
                        "description": "是否支持触控反馈。",
                        "default": True
                    }
                }
            }
        },
        "events": {
            "onSelected": {
                "description": "索引条选中回调，返回值为当前选中索引。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前选中的索引。"
                    }
                }
            },
            "onSelect": {
                "description": "索引条选中回调，返回值为当前选中索引。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前选中的索引。"
                    }
                }
            },
            "onRequestPopupData": {
                "description": "选中字母索引后，请求索引提示弹窗显示内容回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前选中的索引。"
                    }
                },
                "returns": {
                    "type": "string",
                    "description": "索引对应的字符串数组，此字符串数组在弹窗中竖排显示，字符串列表最多显示5个，超出部分可以滑动显示。"
                }
            },
            "onPopupSelect": {
                "description": "字母索引提示弹窗字符串列表选中回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前选中的索引。"
                    }
                }
            }
        },
        "examples": [
            "// xxx.ets\n// 该代码定义了一个名为AlphabetIndexerSample的组件，该组件展示了一个带有字母索引的列表。\n// 用户可以通过点击右侧的字母索引快速定位到列表中的相应部分。\n// 字母索引支持弹出提示框，显示与选中字母相关的详细内容。\n\n@Entry\n@Component\nstruct AlphabetIndexerSample {\n  // 定义四个字符串数组，分别对应不同的字母索引内容\n  private arrayA: string[] = ['安']\n  private arrayB: string[] = ['卜', '白', '包', '毕', '丙']\n  private arrayC: string[] = ['曹', '成', '陈', '催']\n  private arrayL: string[] = ['刘', '李', '楼', '梁', '雷', '吕', '柳', '卢']\n  // 定义字母索引的值数组\n  private value: string[] = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G',\n  'H', 'I', 'J', 'K', 'L', 'M', 'N',\n  'O', 'P', 'Q', 'R', 'S', 'T', 'U',\n  'V', 'W', 'X', 'Y', 'Z']\n\n  build() {\n    Stack({ alignContent: Alignment.Start }) {\n      Row() {\n        // 创建一个列表，显示arrayA, arrayB, arrayC, arrayL的内容\n        List({ space: 20, initialIndex: 0 }) {\n          ForEach(this.arrayA, (item: string) => {\n            ListItem() {\n              Text(item)\n                .width('80%')\n                .height('5%')\n                .fontSize(30)\n                .textAlign(TextAlign.Center)\n            }\n          }, (item: string) => item)\n\n          ForEach(this.arrayB, (item: string) => {\n            ListItem() {\n              Text(item)\n                .width('80%')\n                .height('5%')\n                .fontSize(30)\n                .textAlign(TextAlign.Center)\n            }\n          }, (item: string) => item)\n\n          ForEach(this.arrayC, (item: string) => {\n            ListItem() {\n              Text(item)\n                .width('80%')\n                .height('5%')\n                .fontSize(30)\n                .textAlign(TextAlign.Center)\n            }\n          }, (item: string) => item)\n\n          ForEach(this.arrayL, (item: string) => {\n            ListItem() {\n              Text(item)\n                .width('80%')\n                .height('5%')\n                .fontSize(30)\n                .textAlign(TextAlign.Center)\n            }\n          }, (item: string) => item)\n        }\n        .width('50%')\n        .height('100%')\n\n        // 创建字母索引器，并设置其样式和行为\n        AlphabetIndexer({ arrayValue: this.value, selected: 0 })\n          .selectedColor(0xFFFFFF) // 选中项文本颜色\n          .popupColor(0xFFFAF0) // 弹出框文本颜色\n          .selectedBackgroundColor(0xCCCCCC) // 选中项背景颜色\n          .popupBackground(0xD2B48C) // 弹出框背景颜色\n          .usingPopup(true) // 是否显示弹出框\n          .selectedFont({ size: 16, weight: FontWeight.Bolder }) // 选中项字体样式\n          .popupFont({ size: 30, weight: FontWeight.Bolder }) // 弹出框内容的字体样式\n          .itemSize(28) // 每一项的尺寸大小\n          .alignStyle(IndexerAlign.Left) // 弹出框在索引条右侧弹出\n          .popupItemBorderRadius(24) // 设置提示弹窗索引项背板圆角半径\n          .itemBorderRadius(14) // 设置索引项背板圆角半径\n          .popupBackgroundBlurStyle(BlurStyle.NONE) // 设置提示弹窗的背景模糊材质\n          .popupTitleBackground(0xCCCCCC) // 设置提示弹窗首个索引项背板颜色\n          .popupSelectedColor(0x00FF00)\n          .popupUnselectedColor(0x0000FF)\n          .popupItemFont({ size: 30, style: FontStyle.Normal })\n          .popupItemBackgroundColor(0xCCCCCC)\n          .onSelect((index: number) => {\n            console.info(this.value[index] + ' Selected!')\n          })\n          .onRequestPopupData((index: number) => {\n            if (this.value[index] == 'A') {\n              return this.arrayA // 当选中A时，弹出框里面的提示文本列表显示A对应的列表arrayA，选中B、C、L时也同样\n            } else if (this.value[index] == 'B') {\n              return this.arrayB\n            } else if (this.value[index] == 'C') {\n              return this.arrayC\n            } else if (this.value[index] == 'L') {\n              return this.arrayL\n            } else {\n              return [] // 选中其余子母项时，提示文本列表为空\n            }\n          })\n          .onPopupSelect((index: number) => {\n            console.info('onPopupSelected:' + index)\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n  }\n}",
        ],
        "is_common_attrs": True
    },
    "Blank": {
        "description": "空白填充组件，在容器主轴方向上，空白填充组件具有自动填充容器空余部分的能力。仅当父组件为Row/Column/Flex时生效。",
        "interfaces": [
            {
                "description": "Blank(min?: number | string)",
                "params": {
                    "min": {
                        "type": ["number", "string"],
                        "required": False,
                        "description": "空白填充组件在容器主轴上的最小大小。不支持设置百分比。负值使用默认值。当最小值大于容器可用空间时，使用最小值作为自身大小并超出容器。"
                    }
                }
            }
        ],
        "attributes": {
            "color": {
                "description": "设置空白填充的填充颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "空白填充的填充颜色。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            "/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中创建一个包含蓝牙开关的界面。通过使用Column和Row组件来布局文本和开关控件，并利用Blank组件来实现布局中的空白间隔。整体界面背景设置为浅灰色，以增强视觉效果。\n\n总体功能与效果描述：\n该界面展示了一个蓝牙开关控件，用户可以通过开关来控制蓝牙的开启和关闭。界面设计简洁，易于操作。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct BlankExample {\n  build() {\n    Column() {\n      Row() {\n        Text('Bluetooth').fontSize(18) // 显示蓝牙文本，字体大小设置为18\n        Blank() // 使用Blank组件在文本和开关之间创建空白间隔，以改善布局美观性\n        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 }) // 创建一个开关类型的Toggle控件，设置其上下左右边距以调整布局\n      }.width('100%').backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }) // 设置Row组件的宽度为100%，背景颜色为白色，边框圆角为15，左侧内边距为12\n    }.backgroundColor(0xEFEFEF).padding(20) // 设置Column组件的背景颜色为浅灰色，内边距为20\n  }\n}",
            "/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中使用Blank组件来控制布局中的空白间隔。通过设置Blank组件的最小宽度，确保在父组件未明确设置宽度时，Blank组件仍能有效填充固定宽度。示例中包含两个Row组件，分别展示了未设置和设置了Blank最小宽度的效果。\n\n总体功能与效果描述：\n该界面展示了两个蓝牙开关控件，通过Blank组件的不同设置来调整布局中的空白间隔。第一个Row组件中的Blank未设置最小宽度，而第二个Row组件中的Blank设置了最小宽度为160，以确保在父组件未设置宽度时，Blank仍能填充固定宽度。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct BlankExample {\n  build() {\n    Column({ space: 20 }) {\n      // blank父组件不设置宽度时，Blank失效，可以通过设置min最小宽度填充固定宽度\n      Row() {\n        Text('Bluetooth').fontSize(18) // 显示蓝牙文本，字体大小设置为18\n        Blank().color(Color.Yellow) // 使用Blank组件在文本和开关之间创建空白间隔，并设置颜色为黄色\n        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 }) // 创建一个开关类型的Toggle控件，设置其上下左右边距以调整布局\n      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }) // 设置Row组件的背景颜色为白色，边框圆角为15，左侧内边距为12\n\n      Row() {\n        Text('Bluetooth').fontSize(18) // 显示蓝牙文本，字体大小设置为18\n        // 设置最小宽度为160\n        Blank('160').color(Color.Yellow) // 使用Blank组件在文本和开关之间创建空白间隔，并设置最小宽度为160，颜色为黄色\n        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 }) // 创建一个开关类型的Toggle控件，设置其上下左右边距以调整布局\n      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }) // 设置Row组件的背景颜色为白色，边框圆角为15，左侧内边距为12\n\n    }.backgroundColor(0xEFEFEF).padding(20).width('100%') // 设置Column组件的背景颜色为浅灰色，内边距为20，宽度为100%\n  }\n}"
        ],
        "is_common_attrs": True
    },
    "Button": {
        "description": "按钮组件，可快速创建不同样式的按钮。可以包含单个子组件。",
        "interfaces": [
            {
                "description": "创建可以包含单个子组件的按钮。",
                "params": {
                    "options": {
                        "type": "ButtonOptions",
                        "required": True,
                        "description": "按钮选项"
                    }
                }
            },
            {
                "description": "使用文本内容创建相应的按钮组件，此时Button无法包含子组件。文本内容默认单行显示。",
                "params": {
                    "label": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "按钮的文本标签"
                    },
                    "options": {
                        "type": "ButtonOptions",
                        "required": False,
                        "description": "按钮选项"
                    }
                }
            }
        ],
        "attributes": {
            "type": {
                "description": "设置Button样式。",
                "params": {
                    "value": {
                        "type": ["ButtonType"],
                        "required": True,
                        "description": "Button样式",
                        "default": "ButtonType.Capsule"
                    }
                }
            },
            "stateEffect": {
                "description": "设置是否开启按压态显示效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "按钮按下时是否开启按压态显示效果",
                        "default": True
                    }
                }
            },
            "buttonStyle": {
                "description": "设置Button组件的样式和重要程度。",
                "params": {
                    "value": {
                        "type": ["ButtonStyleMode"],
                        "required": True,
                        "description": "Button组件的样式和重要程度",
                        "default": "ButtonStyleMode.EMPHASIZED"
                    }
                }
            },
            "controlSize": {
                "description": "设置Button组件的尺寸。",
                "params": {
                    "value": {
                        "type": ["ControlSize"],
                        "required": True,
                        "description": "Button组件的尺寸",
                        "default": "ControlSize.NORMAL"
                    }
                }
            },
            "role": {
                "description": "设置Button组件的角色。",
                "params": {
                    "value": {
                        "type": ["ButtonRole"],
                        "required": True,
                        "description": "Button组件的角色",
                        "default": "ButtonRole.NORMAL"
                    }
                }
            }
        },
        "events": {},
        "is_common_attrs": True,
        "examples": [
            """// xxx.ets\n@Entry\n@Component\nstruct ButtonExample {\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {\n      // 显示文本“Normal button”\n      Text('Normal button').fontSize(9).fontColor(0xCCCCCC)\n      // 创建一个Flex布局，对齐方式为中心对齐，间距均匀分布\n      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {\n        // 创建一个显示文本为“OK”的普通按钮，启用状态效果\n        Button('OK', { type: ButtonType.Normal, stateEffect: True })\n          .borderRadius(8) // 设置按钮的边框圆角半径为8\n          .backgroundColor(0x317aff) // 设置按钮的背景颜色为蓝色\n          .width(90) // 设置按钮的宽度为90\n          .onClick(() => {\n            console.log('ButtonType.Normal') // 点击按钮时在控制台输出信息\n          })\n        // 创建一个显示加载中的普通按钮，启用状态效果\n        Button({ type: ButtonType.Normal, stateEffect: True }) {\n          Row() {\n            LoadingProgress().width(20).height(20).margin({ left: 12 }).color(0xFFFFFF) // 加载进度条\n            Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 }) // 加载文本\n          }.alignItems(VerticalAlign.Center) // 垂直居中对齐\n        }.borderRadius(8).backgroundColor(0x317aff).width(90).height(40) // 设置按钮样式\n\n        // 创建一个显示文本为“Disable”的普通按钮，禁用状态效果，设置透明度为0.4\n        Button('Disable', { type: ButtonType.Normal, stateEffect: False }).opacity(0.4)\n          .borderRadius(8).backgroundColor(0x317aff).width(90)\n      }\n\n      // 显示文本“Capsule button”\n      Text('Capsule button').fontSize(9).fontColor(0xCCCCCC)\n      // 创建一个Flex布局，对齐方式为中心对齐，间距均匀分布\n      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {\n        // 创建一个显示文本为“OK”的胶囊按钮，启用状态效果\n        Button('OK', { type: ButtonType.Capsule, stateEffect: True }).backgroundColor(0x317aff).width(90)\n        // 创建一个显示加载中的胶囊按钮，启用状态效果\n        Button({ type: ButtonType.Capsule, stateEffect: True }) {\n          Row() {\n            LoadingProgress().width(20).height(20).margin({ left: 12 }).color(0xFFFFFF) // 加载进度条\n            Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 }) // 加载文本\n          }.alignItems(VerticalAlign.Center).width(90).height(40) // 垂直居中对齐\n        }.backgroundColor(0x317aff)\n\n        // 创建一个显示文本为“Disable”的胶囊按钮，禁用状态效果，设置透明度为0.4\n        Button('Disable', { type: ButtonType.Capsule, stateEffect: False }).opacity(0.4)\n          .backgroundColor(0x317aff).width(90)\n      }\n\n      // 显示文本“Circle button”\n      Text('Circle button').fontSize(9).fontColor(0xCCCCCC)\n      // 创建一个Flex布局，对齐方式为中心对齐，允许换行\n      Flex({ alignItems: ItemAlign.Center, wrap: FlexWrap.Wrap }) {\n        // 创建一个显示加载中的圆形按钮，启用状态效果\n        Button({ type: ButtonType.Circle, stateEffect: True }) {\n          LoadingProgress().width(20).height(20).color(0xFFFFFF) // 加载进度条\n        }.width(55).height(55).backgroundColor(0x317aff) // 设置按钮样式\n\n        // 创建另一个显示加载中的圆形按钮，启用状态效果，设置不同的背景颜色\n        Button({ type: ButtonType.Circle, stateEffect: True }) {\n          LoadingProgress().width(20).height(20).color(0xFFFFFF) // 加载进度条\n        }.width(55).height(55).margin({ left: 20 }).backgroundColor(0xF55A42) // 设置按钮样式\n      }\n    }.height(400).padding({ left: 35, right: 35, top: 35 }) // 设置整体布局的高度和内边距\n  }\n}""",
            """// xxx.ets\n// 这段代码实现了一个简单的按钮组件，按钮显示的文本为overflowTextOverlengthTextOverflow.Clip，宽度为200，高度为100。按钮的文本样式设置为裁剪溢出、单行显示、固定字体大小为20，字体粗细为粗体，字体家族为草书，字体样式为斜体。按钮的字体大小为40。\n@Entry\n@Component\nstruct buttonTestDemo {\n  @State txt: string = 'overflowTextOverlengthTextOverflow.Clip'; // 按钮显示的文本\n  @State widthShortSize: number = 200; // 按钮的宽度\n\n  build() {\n    Row() {\n      Column() {\n        Button(this.txt)\n          .width(this.widthShortSize) // 设置按钮宽度\n          .height(100) // 设置按钮高度\n          .labelStyle({ \n            overflow: TextOverflow.Clip, // 文本溢出时裁剪\n            maxLines: 1, // 最大行数为1\n            minFontSize: 20, // 最小字体大小\n            maxFontSize: 20, // 最大字体大小\n            font: {\n              size: 20, // 字体大小\n              weight: FontWeight.Bolder, // 字体粗细\n              family: 'cursive', // 字体家族\n              style: FontStyle.Italic // 字体样式\n            }\n          })\n          .fontSize(40) // 按钮字体大小\n      }\n      .width('100%')\n    }\n    .height('100%')\n  }\n}""",
            """// xxx.ets\n// 这段代码实现了一个展示不同样式和大小的按钮的组件。组件包含三个部分，每个部分显示一组按钮，分别是正常尺寸和小尺寸的按钮，每组按钮包括强调样式、普通样式和文本样式。组件的高度为400，并设置了左右上方的内边距。\n@Entry\n@Component\nstruct ButtonExample {\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {\n      Text('Normal size button').fontSize(9).fontColor(0xCCCCCC) // 显示标题“Normal size button”\n      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {\n        Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED }); // 强调样式按钮\n        Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL }); // 普通样式按钮\n        Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL }); // 文本样式按钮\n      }\n\n      Text('Small size button').fontSize(9).fontColor(0xCCCCCC) // 显示标题“Small size button”\n      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {\n        Button('Emphasized', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.EMPHASIZED }); // 小尺寸强调样式按钮\n        Button('Normal', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.NORMAL }); // 小尺寸普通样式按钮\n        Button('Textual', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.TEXTUAL }); // 小尺寸文本样式按钮\n      }\n\n      Text('Small size button').fontSize(9).fontColor(0xCCCCCC) // 显示标题“Small size button”\n      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {\n        Button('Emphasized').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.EMPHASIZED); // 小尺寸强调样式按钮\n        Button('Normal').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.NORMAL); // 小尺寸普通样式按钮\n        Button('Textual').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.TEXTUAL); // 小尺寸文本样式按钮\n      }\n\n    }.height(400).padding({ left: 35, right: 35, top: 35 })\n  }\n}""",
            """// xxx.ets\n// 这段代码实现了一个展示不同角色（正常和错误）的按钮的组件。组件包含两个部分，每个部分显示一组按钮，分别是角色为正常和错误的按钮，每组按钮包括强调样式、普通样式和文本样式。组件的高度为200，并设置了左右上方的内边距。\n@Entry\n@Component\nstruct ButtonExample {\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {\n      Text('Role is Normal button').fontSize(9).fontColor(0xCCCCCC) // 显示标题“Role is Normal button”\n      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {\n        Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.NORMAL }); // 强调样式且角色为正常的按钮\n        Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL, role: ButtonRole.NORMAL }); // 普通样式且角色为正常的按钮\n        Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL, role: ButtonRole.NORMAL }); // 文本样式且角色为正常的按钮\n      }\n      Text('Role is Error button').fontSize(9).fontColor(0xCCCCCC) // 显示标题“Role is Error button”\n      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {\n        Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR}); // 强调样式且角色为错误的按钮\n        Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL, role: ButtonRole.ERROR }); // 普通样式且角色为错误的按钮\n        Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL, role: ButtonRole.ERROR }); // 文本样式且角色为错误的按钮\n      }\n    }.height(200).padding({ left: 35, right: 35, top: 35 })\n  }\n}""",
            """// 这段代码实现了一个自定义样式的按钮组件，按钮显示为“OK”，并包含一个开关控件用于启用或禁用按钮。按钮点击时会记录点击位置的坐标，并在按钮上显示这些坐标。按钮的按压状态和启用状态也会在按钮上显示。按钮的样式和行为通过 MyButtonStyle 类和 buildButton1 函数进行自定义。如果按压，圆圈将变成红色，标题会显示按压字样；如果没有按压，圆圈将变成黑色，标题会显示非按压字样。\nclass MyButtonStyle implements ContentModifier<ButtonConfiguration> {\n  x: number = 0\n  y: number = 0\n  selectedColor: Color = Color.Black\n\n  constructor(x: number, y: number, ColorType: Color) {\n    this.x = x\n    this.y = y\n    this.selectedColor = ColorType\n  }\n\n  applyContent(): WrappedBuilder<[ButtonConfiguration]> {\n    return wrapBuilder(buildButton1)\n  }\n}\n\n@Builder function buildButton1(config: ButtonConfiguration) {\n  Column({ space: 30 }) {\n    Text(config.enabled ? "enabled True" : "enabled False") // 显示按钮是否启用\n    Text('圆圈状态' + (config.pressed ? "（ 按压 ）" : "（ 非按压 ）")) // 显示按钮按压状态\n    Text('点击位置x坐标：' + (config.enabled ? (config.contentModifier as MyButtonStyle).x : "0")) // 显示点击位置x坐标\n    Text('点击位置y坐标：' + (config.enabled ? (config.contentModifier as MyButtonStyle).y : "0")) // 显示点击位置y坐标\n    Circle({ width: 50, height: 50 })\n      .fill(config.pressed ? (config.contentModifier as MyButtonStyle).selectedColor : Color.Black) // 根据按压状态填充颜色\n      .gesture(\n        TapGesture({ count: 1 }).onAction((event: GestureEvent) => {\n          config.triggerClick(event.fingerList[0].localX, event.fingerList[0].localY) // 触发点击事件\n        })\n      ).opacity(config.enabled ? 1 : 0.1) // 根据启用状态设置透明度\n  }\n}\n\n@Entry\n@Component\nstruct ButtonExample {\n  @State buttonEnabled: boolean = True; // 按钮启用状态\n  @State positionX: number = 0 // 点击位置x坐标\n  @State positionY: number = 0 // 点击位置y坐标\n  @State state: boolean[] = [True, False]\n  @State index: number = 0\n\n  build() {\n    Column() {\n      Button('OK')\n        .contentModifier(new MyButtonStyle(this.positionX, this.positionY, Color.Red)) // 应用自定义按钮样式\n        .onClick((event) => {\n          console.info('change' + JSON.stringify(event))\n          this.positionX = event.displayX // 更新点击位置x坐标\n          this.positionY = event.displayY // 更新点击位置y坐标\n        }).enabled(this.buttonEnabled) // 设置按钮启用状态\n      Row() {\n        Toggle({ type: ToggleType.Switch, isOn: True }).onChange((value: boolean) => {\n          if (value) {\n            this.buttonEnabled = True // 启用按钮\n          } else {\n            this.buttonEnabled = False // 禁用按钮\n          }\n        }).margin({ left: -80 })\n      }\n    }.height('100%').width('100%').justifyContent(FlexAlign.Center)\n  }\n}""",

        ]
    },
    "CalendarPicker": {
        "description": "日历选择器组件，提供下拉日历弹窗，可以让用户选择日期。",
        "interfaces": [
            {
                "description": "日历选择器。",
                "params": {
                    "options": {
                        "type": "CalendarOptions",
                        "required": False,
                        "description": "配置日历选择器组件的参数。"
                    }
                }
            }
        ],
        "attributes": {
            "edgeAlign": {
                "description": "设置选择器与入口组件的对齐方式。",
                "params": {
                    "alignType": {
                        "type": "CalendarAlign",
                        "required": True,
                        "description": "对齐方式类型。默认值：",
                        "default": "CalendarAlign.END"
                    },
                    "offset": {
                        "type": "Offset",
                        "required": False,
                        "description": "按照对齐类型对齐后，选择器相对入口组件的偏移量。",
                        "default": "{dx: 0, dy: 0}"
                    }
                }
            },
            "textStyle": {
                "description": "入口区的文本颜色、字号、字体粗细。",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "设置入口区的文本颜色、字号、字体粗细。",
                        "default": "{color: '#ff182431', font: {size: '16fp', weight: FontWeight.Regular}}"
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "选择日期时触发该事件。",
                "params": {
                    "value": {
                        "type": "Date",
                        "required": True,
                        "description": "选中的日期值。"
                    }
                }
            }
        },
        "examples": [
            """// 这段代码实现了一个月历日期选择器组件，其中包括一个默认选定日期为'2024-03-05'的日历选择器。日历选择器具有自定义样式，包括圆角提示、选定日期样式、文本样式等。用户可以在日历选择器上选择日期，并在日期发生变化时触发onChange事件，将选定的日期信息以JSON格式打印到控制台中。\n\n在给出的例子中，展示了一个自定义样式的按钮组件，按钮显示为“OK”，并包含一个开关控件用于启用或禁用按钮。按钮的点击位置坐标会被记录，并显示在按钮上。按钮的按压状态和启用状态也会在按钮上显示。通过MyButtonStyle类和buildButton1函数进行按钮样式和行为的自定义。按钮的样式会根据按压状态显示不同的颜色和标题。用户可以通过点击按钮来触发事件，更新按钮的点击位置坐标，并根据开关控件的状态来启用或禁用按钮。\n// xxx.ets\n@Entry\n@Component\nstruct CalendarPickerExample {\n  private selectedDate: Date = new Date('2024-03-05')\n\n  build() {\n    Column() {\n      Text('月历日期选择器').fontSize(30)\n      Column() {\n        CalendarPicker({ hintRadius: 10, selected: this.selectedDate })\n          .edgeAlign(CalendarAlign.END)\n          .textStyle({ color: "  # ff182431", font: { size: 20, weight: FontWeight.Normal } })\n          .margin(10)\n          .onChange((value) => {\n            console.info("CalendarPicker onChange:" + JSON.stringify(value))\n          })\n      }.alignItems(HorizontalAlign.End).width("100%")\n    }.width('100%').margin({ top: 350 })\n  }\n}"""],
        "is_common_attrs": True
    },
    "Checkbox": {
        "description": "提供多选框组件，通常用于某选项的打开或关闭。可以包含Text组件。",
        "interfaces": [
            {
                "description": "多选框组件。",
                "params": {
                    "options": {
                        "type": "CheckboxOptions",
                        "required": False,
                        "description": "多选框选项。"
                    }
                }
            }
        ],
        "attributes": {
            "select": {
                "description": "设置多选框是否选中。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "多选框是否选中。",
                        "default": "false"
                    }
                }
            },
            "selectedColor": {
                "description": "设置多选框选中状态颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "多选框选中状态颜色。",
                        "default": "$r('sys.color.ohos_id_color_text_primary_activated')"
                    }
                }
            },
            "unselectedColor": {
                "description": "设置多选框非选中状态边框颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "多选框非选中状态边框颜色。",
                        "default": "#33ffffff"
                    }
                }
            },
            "mark": {
                "description": "设置多选框内部图标样式。",
                "params": {
                    "value": {
                        "type": "MarkStyle",
                        "required": True,
                        "description": "多选框内部图标样式。"
                    }
                }
            },
            "shape": {
                "description": "设置CheckBox组件形状, 包括圆形和圆角方形。",
                "params": {
                    "value": {
                        "type": "CheckBoxShape",
                        "required": True,
                        "description": "CheckBox组件形状, 包括圆形和圆角方形。",
                        "default": "CheckBoxShape.CIRCLE"
                    }
                }
            },
            "contentModifier": {
                "description": "定制CheckBox内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<CheckBoxConfiguration>",
                        "required": True,
                        "description": "定制CheckBox内容区的方法。"
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "当选中状态发生变化时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "(value: boolean) => void",
                        "required": True,
                        "description": "当选中状态发生变化时，触发该回调。"
                    }
                }
            }
        },
        "examples": [
            "/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中使用Flex布局和Checkbox组件来创建一个简单的复选框组。通过Flex布局的justifyContent和alignItems属性，确保复选框和文本在水平和垂直方向上居中对齐。Checkbox组件用于创建可选择的复选框，用户可以选择或取消选择。\n\n总体功能与效果描述：\n该示例创建了一个包含两个复选框的界面，每个复选框旁边都有相应的文本标签。复选框和文本标签在水平和垂直方向上都居中对齐，用户可以通过点击复选框来选择或取消选择。\n*/\n\n// Index.ets\n@Entry\n@Component\nstruct Index {\n  build() {\n    Row() {\n      Column() {\n        // 创建一个Flex布局，水平和垂直居中对齐其子组件\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建第一个复选框，设置宽度和高度\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            .width(30) // 设置复选框宽度为30\n            .height(30) // 设置复选框高度为30\n          // 创建文本标签，设置字体大小\n          Text('Checkbox1').fontSize(20)\n        }\n\n        // 创建另一个Flex布局，水平和垂直居中对齐其子组件\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建第二个复选框，设置宽度和高度\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            .width(30) // 设置复选框宽度为30\n            .height(30) // 设置复选框高度为30\n          // 创建文本标签，设置字体大小\n          Text('Checkbox2').fontSize(20)\n        }\n      }\n      .width('100%') // 设置Column的宽度为100%\n    }\n    .height('100%') // 设置Row的高度为100%\n  }\n}",
            "/*\n实现思路：\n本示例代码定义了一个名为CheckedTextView的组件，该组件包含一个Checkbox和一个Text。Checkbox用于显示和切换选中状态，Text用于显示提示信息并响应点击事件以切换Checkbox的状态。整个组件使用Flex布局，确保内容在屏幕中心对齐。\n\n总体功能与效果描述：\n该组件实现了一个简单的用户界面，用户可以通过点击文本或Checkbox来切换Checkbox的选中状态。\n*/\n\n// CheckedTextView.ets\n@Entry\n@Component\nstruct CheckedTextView {\n  // 定义一个状态变量checked，用于存储Checkbox的选中状态，初始值为false\n  @State checked: boolean = false; \n\n  build() {\n    // 使用Flex布局，设置布局方向为行（水平），对齐方式为中心对齐\n    Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\n      // 创建一个Checkbox组件，绑定到状态变量checked，设置宽度和高度\n      Checkbox()\n        .select($$this.checked) // 绑定Checkbox的选中状态到状态变量checked\n        .width(30) // 设置Checkbox的宽度为30\n        .height(30) // 设置Checkbox的高度为30\n      \n      // 创建一个Text组件，显示文本\"Click to check\"，设置字体大小和文本对齐方式\n      Text('Click to check')\n        .fontSize(18) // 设置字体大小为18\n        .textAlign(TextAlign.Center) // 设置文本对齐方式为中心对齐\n        .onClick(() => {\n          // 点击Text时，切换状态变量checked的值\n          this.checked = !this.checked\n        })\n    }\n    .width('100%') // 设置Flex容器的宽度为100%\n    .height('100%') // 设置Flex容器的高度为100%\n  }\n}",
            # "/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中使用Checkbox组件。通过创建两个Checkbox实例，并设置其样式和事件处理，展示了Checkbox的基本功能和自定义样式。每个Checkbox都有独立的选中状态和事件回调，用于处理用户交互。\n*/\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    Row() {\n      Column() {\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // Checkbox1组件，用于用户选择，自定义了选中颜色、形状和事件处理\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            .selectedColor(0x39a2db) // 设置选中时的颜色\n            .shape(CheckBoxShape.ROUNDED_SQUARE) // 设置Checkbox的形状为圆角方形\n            .onChange((value: boolean) => {\n              console.info('Checkbox1 change is'+ value) // 当Checkbox状态改变时，输出当前状态\n            })\n            .mark({\n              strokeColor:Color.Black, // 设置标记的颜色\n              size: 50, // 设置标记的大小\n              strokeWidth: 5 // 设置标记的线条宽度\n            })\n            .unselectedColor(Color.Red) // 设置未选中时的颜色\n            .width(30) // 设置Checkbox的宽度\n            .height(30) // 设置Checkbox的高度\n          Text('Checkbox1').fontSize(20) // 显示Checkbox的标签文本\n        }\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // Checkbox2组件，用于用户选择，自定义了选中颜色、形状和事件处理\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            .selectedColor(0x39a2db) // 设置选中时的颜色\n            .shape(CheckBoxShape.ROUNDED_SQUARE) // 设置Checkbox的形状为圆角方形\n            .onChange((value: boolean) => {\n              console.info('Checkbox2 change is' + value) // 当Checkbox状态改变时，输出当前状态\n            })\n            .width(30) // 设置Checkbox的宽度\n            .height(30) // 设置Checkbox的高度\n          Text('Checkbox2').fontSize(20) // 显示Checkbox的标签文本\n        }\n      }\n      .width('100%') // 设置列的宽度为100%\n    }\n    .height('100%') // 设置行的宽度为100%\n  }\n}",
            # "/*\n实现思路：\n本示例代码定义了一个自定义的复选框样式类 `MyCheckboxStyle`，并通过 `buildCheckbox` 函数构建复选框的UI。在主组件 `Index` 中，使用该自定义样式并实现了复选框的状态切换和启用/禁用功能。通过 `Toggle` 组件控制复选框的启用状态。\n该示例实现了自定义复选框样式的功能，自定义样式实现了一个五边形复选框，如果选中，内部会出现红色三角图案，标题会显示选中字样，如果取消选中，红色三角图案消失，标题会显示非选中字样。\n*/\n// xxx.ets\nclass MyCheckboxStyle implements ContentModifier<CheckBoxConfiguration> {\n  selectedColor: Color = Color.White\n  constructor(selectedColor: Color) {\n    this.selectedColor = selectedColor;\n  }\n  applyContent() : WrappedBuilder<[CheckBoxConfiguration]>\n  {\n    return wrapBuilder(buildCheckbox)\n  }\n}\n\n@Builder function buildCheckbox(config: CheckBoxConfiguration) {\n  Column({space:10}) {\n      // 显示复选框的名称和选中状态\n      Text(config.name  + (config.selected ? \"（ 选中 ）\" : \"（ 非选中 ）\")).margin({right : 70, top : 50})\n      // 显示复选框的启用状态\n      Text(config.enabled ? \"enabled true\" : \"enabled false\").margin({right : 110})\n      Shape() {\n        Path().width(100).height(100).commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z').fillOpacity(0).strokeWidth(3).onClick(()=>{\n          // 切换复选框的选中状态\n          if (config.selected) {\n            config.triggerChange(false)\n          } else {\n            config.triggerChange(true)\n          }\n        }).opacity(config.enabled ? 1 : 0.1)\n        Path().width(10).height(10).commands('M50 0 L100 100 L0 100 Z')\n          .visibility(config.selected ? Visibility.Visible : Visibility.Hidden)\n          .fill(config.selected ? (config.contentModifier as MyCheckboxStyle).selectedColor : Color.Black)\n          .stroke((config.contentModifier as MyCheckboxStyle).selectedColor)\n          .margin({left:11,top:10})\n          .opacity(config.enabled ? 1 : 0.1)\n      }\n      .width(300)\n      .height(200)\n      .viewPort({ x: 0, y: 0, width: 310, height: 310 })\n      .strokeLineJoin(LineJoinStyle.Miter)\n      .strokeMiterLimit(5)\n      .margin({left:50})\n  }\n}\n\n@Entry\n@Component\nstruct Index {\n  @State checkboxEnabled: boolean = true;\n  build() {\n    Column({ space: 100 }) {\n        // 使用自定义样式创建复选框，并监听状态变化\n        Checkbox({ name: '复选框状态', group: 'checkboxGroup' })\n        .contentModifier(new MyCheckboxStyle(Color.Red))\n        .onChange((value: boolean) => {\n          console.info('Checkbox change is' + value)\n        }).enabled(this.checkboxEnabled)\n\n      Row() {\n        // 使用Toggle组件控制复选框的启用状态\n        Toggle({ type: ToggleType.Switch, isOn: true }).onChange((value: boolean) => {\n          if (value) {\n            this.checkboxEnabled = true\n          } else {\n            this.checkboxEnabled = false\n          }\n        })\n      }\n    }.margin({top : 30})\n  }\n}",
            # "/*\n实现思路：\n本示例展示了如何使用ArkUI框架创建自定义样式的复选框组件。通过定义一个Builder函数来动态生成复选框的指示器，并根据不同的值显示不同的文本和字体大小。每个复选框都有自己的样式和事件处理逻辑。\n\n总体功能与效果描述：\n该示例包含两个复选框，每个复选框具有不同的形状和指示器样式。第一个复选框为圆形，第二个复选框为圆角矩形。每个复选框的指示器显示一个数字，如果数字大于99，则显示为“99+”。复选框的状态变化会通过控制台输出。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct CheckboxExample {\n  // 定义一个Builder函数，用于生成复选框的指示器\n  @Builder\n  indicatorBuilder(value: number) {\n    Column(){\n      // 根据值的大小显示不同的文本和字体大小\n      Text(value > 99 ? '99+': value.toString())\n        .textAlign(TextAlign.Center)\n        .fontSize(value > 99 ?  '16vp': '20vp')\n        .fontWeight(FontWeight.Medium)\n        .fontColor('#ffffffff')\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        // 第一个复选框，圆形形状\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center}) {\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup', indicatorBuilder:()=>{this.indicatorBuilder(9)}})\n            .shape(CheckBoxShape.CIRCLE) // 设置复选框形状为圆形\n            .onChange((value: boolean) => {\n              console.info('Checkbox1 change is'+ value) // 输出复选框状态变化\n            })\n            .mark({\n              strokeColor:Color.Black,\n              size: 50,\n              strokeWidth: 5\n            })\n            .width(30)\n            .height(30)\n          Text('Checkbox1').fontSize(20)\n        }.padding(15)\n\n        // 第二个复选框，圆角矩形形状\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup', indicatorBuilder:()=>{this.indicatorBuilder(100)}})\n            .shape(CheckBoxShape.ROUNDED_SQUARE) // 设置复选框形状为圆角矩形\n            .onChange((value: boolean) => {\n              console.info('Checkbox2 change is' + value) // 输出复选框状态变化\n            })\n            .width(30)\n            .height(30)\n          Text('Checkbox2').fontSize(20)\n        }\n      }\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"

        ],
        "is_common_attrs": True
    },
    "CheckboxGroup": {
        "description": "多选框群组，用于控制多选框全选或者不全选状态。",
        "interfaces": [
            {
                "description": "创建多选框群组，可以控制群组内的Checkbox全选或者不全选，group值相同的Checkbox和CheckboxGroup为同一群组。\n在结合带缓存组件使用时(如List)，未被创建的Checkbox选中状态需要应用手动控制。",
                "params": {
                    "options": {
                        "type": "CheckboxGroupOptions",
                        "required": False,
                        "description": "CheckboxGroup的选项配置。"
                    }
                }
            }
        ],
        "attributes": {
            "selectAll": {
                "description": "设置是否全选。若同组的Checkbox显式设置了select属性，则Checkbox的优先级高。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否全选。",
                        "default": False
                    }
                }
            },
            "selectedColor": {
                "description": "设置被选中或部分选中状态的颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "被选中或部分选中状态的颜色。",
                        "default": "$r('sys.color.ohos_id_color_text_primary_activated')"
                    }
                }
            },
            "unselectedColor": {
                "description": "设置非选中状态边框颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "非选中状态边框颜色。"
                    }
                }
            },
            "mark": {
                "description": "设置多选框内部图标样式。",
                "params": {
                    "value": {
                        "type": "MarkStyle",
                        "required": True,
                        "description": "多选框内部图标样式。"
                    }
                }
            },
            "checkboxShape": {
                "description": "设置CheckboxGroup组件形状， 包括圆形和圆角方形。",
                "params": {
                    "value": {
                        "type": "CheckBoxShape",
                        "required": True,
                        "description": "CheckboxGroup组件形状， 包括圆形和圆角方形。",
                        "default": "CheckBoxShape.CIRCLE"
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "回调函数，参数为CheckboxGroupResult对象。"
                    }
                }
            }
        },
        "examples": [
            """示例1:```java\n// CheckboxExample.ets\n\n// 创建一个包含多个复选框的示例界面，包括全选按钮和三个选项复选框\n@Entry\n@Component\nstruct CheckboxExample {\n  build() {\n    Scroll() {\n      Column() {\n        // 全选按钮，用于选择所有选项\n        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {\n          CheckboxGroup({ group: 'checkboxGroup' })\n            .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)\n            .selectedColor('#007DFF')\n            .onChange((itemName: CheckboxGroupResult) => {\n              console.info("checkbox group content" + JSON.stringify(itemName))\n            })\n          Text('Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)\n        }\n\n        // 选项1，用于选择第一个选项\n        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            .selectedColor('#007DFF')\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox1 change is' + value)\n            })\n          Text('Checkbox1').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)\n        }.margin({ left: 36 })\n\n        // 选项2，用于选择第二个选项\n        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            .selectedColor('#007DFF')\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox2 change is' + value)\n            })\n          Text('Checkbox2').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)\n        }.margin({ left: 36 })\n\n        // 选项3，用于选择第三个选项\n        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox3', group: 'checkboxGroup' })\n            .selectedColor('#007DFF')\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox3 change is' + value)\n            })\n          Text('Checkbox3').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)\n        }.margin({ left: 36 })\n      }\n    }\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct CheckboxExample {\n  build() {\n    Scroll() {\n      Column() {\n        // 全选按钮\n        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {\n          CheckboxGroup({ group: 'checkboxGroup' })\n            .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)\n            .selectedColor('#007DFF')\n            .onChange((itemName: CheckboxGroupResult) => {\n              console.info("checkbox group content" + JSON.stringify(itemName))\n            })\n          Text('Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)\n        }\n\n        // 选项1\n        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            .selectedColor('#007DFF')\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox1 change is' + value)\n            })\n          Text('Checkbox1').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)\n        }.margin({ left: 36 })\n\n        // 选项2\n        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            .selectedColor('#007DFF')\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox2 change is' + value)\n            })\n          Text('Checkbox2').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)\n        }.margin({ left: 36 })\n\n        // 选项3\n        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox3', group: 'checkboxGroup' })\n            .selectedColor('#007DFF')\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox3 change is' + value)\n            })\n          Text('Checkbox3').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)\n        }.margin({ left: 36 })\n      }\n    }\n  }\n}"""
            """示例2:```java\n// xxx.ets\n\n// 创建一个页面入口组件Index\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    // 创建一个横向布局Row\n    Row() {\n      // 创建一个纵向布局Column\n      Column() {\n        // 创建一个弹性布局Flex，用于包裹复选框组\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建一个复选框组CheckboxGroup\n          CheckboxGroup({ group: 'checkboxGroup' })\n            // 设置复选框形状为圆角方形\n            .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)\n            // 设置选中状态的颜色为橙色\n            .selectedColor(Color.Orange)\n            // 监听复选框组的状态变化\n            .onChange((itemName: CheckboxGroupResult) => {\n              console.info("checkbox group content" + JSON.stringify(itemName))\n            })\n            // 标记复选框组的样式\n            .mark({\n              strokeColor:Color.Black,\n              size: 40,\n              strokeWidth: 5\n            })\n            // 设置未选中状态的颜色为红色\n            .unselectedColor(Color.Red)\n            // 设置复选框的宽度和高度\n            .width(30)\n            .height(30)\n          // 显示文本"Select All"，设置字体大小为20\n          Text('Select All').fontSize(20)\n        }.margin({right:15}) // 设置右边距为15\n\n        // 创建一个弹性布局Flex，用于包裹复选框1\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建一个单独的复选框Checkbox1\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            // 设置选中状态的颜色为蓝色\n            .selectedColor(0x39a2db)\n            // 设置复选框形状为圆角方形\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            // 监听复选框状态变化\n            .onChange((value: boolean) => {\n              console.info('Checkbox1 change is'+ value)\n            })\n            // 标记复选框的样式\n            .mark({\n              strokeColor:Color.Black,\n              size: 50,\n              strokeWidth: 5\n            })\n            // 设置未选中状态的颜色为红色\n            .unselectedColor(Color.Red)\n            // 设置复选框的宽度和高度\n            .width(30)\n            .height(30)\n          // 显示文本"Checkbox1"，设置字体大小为20\n          Text('Checkbox1').fontSize(20)\n        }\n\n        // 创建一个弹性布局Flex，用于包裹复选框2\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建一个单独的复选框Checkbox2\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            // 设置选中状态的颜色为蓝色\n            .selectedColor(0x39a2db)\n            // 设置复选框形状为圆角方形\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            // 监听复选框状态变化\n            .onChange((value: boolean) => {\n              console.info('Checkbox2 change is' + value)\n            })\n            // 设置复选框的宽度和高度\n            .width(30)\n            .height(30)\n          // 显示文本"Checkbox2"，设置字体大小为20\n          Text('Checkbox2').fontSize(20)\n        }\n\n        // 创建一个弹性布局Flex，用于包裹复选框3\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建一个单独的复选框Checkbox3\n          Checkbox({ name: 'checkbox3', group: 'checkboxGroup' })\n            // 设置选中状态的颜色为蓝色\n            .selectedColor(0x39a2db)\n            // 设置复选框形状为圆角方形\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            // 监听复选框状态变化\n            .onChange((value: boolean) => {\n              console.info('Checkbox3 change is' + value)\n            })\n            // 设置复选框的宽度和高度\n            .width(30)\n            .height(30)\n          // 显示文本"Checkbox3"，设置字体大小为20\n          Text('Checkbox3').fontSize(20)\n        }\n      }\n      // 设置Column的宽度为100%\n      .width('100%')\n    }\n    // 设置Row的高度为100%\n    .height('100%')\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    Row() {\n      Column() {\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          CheckboxGroup({ group: 'checkboxGroup' })\n            .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)\n            .selectedColor(Color.Orange)\n            .onChange((itemName: CheckboxGroupResult) => {\n              console.info("checkbox group content" + JSON.stringify(itemName))\n            })\n            .mark({\n              strokeColor:Color.Black,\n              size: 40,\n              strokeWidth: 5\n            })\n            .unselectedColor(Color.Red)\n            .width(30)\n            .height(30)\n          Text('Select All').fontSize(20)\n        }.margin({right:15})\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            .selectedColor(0x39a2db)\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox1 change is'+ value)\n            })\n            .mark({\n              strokeColor:Color.Black,\n              size: 50,\n              strokeWidth: 5\n            })\n            .unselectedColor(Color.Red)\n            .width(30)\n            .height(30)\n          Text('Checkbox1').fontSize(20)\n        }\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            .selectedColor(0x39a2db)\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox2 change is' + value)\n            })\n            .width(30)\n            .height(30)\n          Text('Checkbox2').fontSize(20)\n        }\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox3', group: 'checkboxGroup' })\n            .selectedColor(0x39a2db)\n            .shape(CheckBoxShape.ROUNDED_SQUARE)\n            .onChange((value: boolean) => {\n              console.info('Checkbox3 change is' + value)\n            })\n            .width(30)\n            .height(30)\n          Text('Checkbox3').fontSize(20)\n        }\n      }\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Component3D": {
        "description": "3D渲染组件，可以加载3D模型资源并做自定义渲染，通常用于3D动效场景。",
        "interfaces": [
            {
                "description": "Component3D((sceneOptions?: SceneOptions))",
                "params": {
                    "sceneOptions": {
                        "type": "SceneOptions",
                        "required": False,
                        "description": "3D场景配置选项。"
                    }
                }
            }
        ],
        "attributes": {
            "environment": {
                "description": "设置3D环境资源。",
                "params": {
                    "uri": {
                        "type": "Resource",
                        "required": True,
                        "description": "3D环境资源。"
                    }
                }
            },
            "customRender": {
                "description": "设置三维场景渲染的渲染管道。",
                "params": {
                    "uri": {
                        "type": "Resource",
                        "required": True,
                        "description": "自定义渲染管线的配置文件。"
                    },
                    "selfRenderUpdate": {
                        "type": "boolean",
                        "required": True,
                        "description": "外部UI没有更新时是否触发动效渲染。"
                    }
                }
            },
            "shader": {
                "description": "设置自定义渲染的shader文件资源。",
                "params": {
                    "uri": {
                        "type": "Resource",
                        "required": True,
                        "description": "自定义渲染的shader文件资源。"
                    }
                }
            },
            "shaderImageTexture": {
                "description": "设置自定义渲染用到的纹理资源。",
                "params": {
                    "uri": {
                        "type": "Resource",
                        "required": True,
                        "description": "自定义渲染用到的纹理资源。"
                    }
                }
            },
            "shaderInputBuffer": {
                "description": "设置自定义渲染用到的动效参数。",
                "params": {
                    "buffer": {
                        "type": "Array<number>",
                        "required": True,
                        "description": "自定义渲染用到的动效参数。"
                    }
                }
            },
            "renderWidth": {
                "description": "设置3D渲染分辨率的宽度。",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "3D渲染分辨率的宽度。"
                    }
                }
            },
            "renderHeight": {
                "description": "设置3D渲染分辨率的长度。",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "3D渲染分辨率的长度。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """// GLTF模型加载示例。xxx.ets\n\n// 定义入口结构体Index，用于展示3D场景\n@Entry\n@Component\nstruct Index {\n  // 定义场景选项，包括加载的3D模型和模型类型\n  scene: SceneOptions = { scene: $rawfile('gltf/DamageHemlt/glTF/DamagedHelmet.gltf'), modelType: ModelType.SURFACE};\n\n  // 构建页面布局\n  build() {\n    // 创建一个横向布局\n    Row() {\n      // 创建一个纵向布局\n      Column() {\n        // 显示文本“GLTF Example”\n        Text('GLTF Example')\n        \n        // 显示3D组件，加载场景模型并设置环境\n        Component3D( this.scene )\n          .environment($rawfile('gltf/Environment/glTF/Environment.gltf'))\n          .renderWidth('90%').renderHeight('90%')\n      }.width('100%') // 设置纵向布局宽度为100%\n    }\n    .height('100%') // 设置横向布局高度为100%\n  }\n}\n```\n\n在以上代码中：\n- `Index` 结构体用于展示3D场景，包含了加载的3D模型和模型类型的定义。\n- `build()` 方法用于构建页面布局，首先创建一个横向布局，内部包含一个纵向布局。\n- 在纵向布局中，首先显示文本“GLTF Example”，然后展示3D组件，加载指定的场景模型，并设置环境。\n- 通过设置宽度和高度的百分比，实现了布局的自适应效果。\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  scene: SceneOptions = { scene: $rawfile('gltf/DamageHemlt/glTF/DamagedHelmet.gltf'), modelType: ModelType.SURFACE};\n  build() {\n    Row() {\n      Column() {\n        Text('GLTF Example')\n        Component3D( this.scene )\n          .environment($rawfile('gltf/Environment/glTF/Environment.gltf'))\n          .renderWidth('90%').renderHeight('90%')\n      }.width('100%')\n    }\n    .height('100%')\n  }\n}"""
            """//自定义渲染示例。 定义引擎时间类，用于计算总时间和每帧时间间隔\nclass EngineTime {\n  totalTimeUs = 0; // 总时间\n  deltaTimeUs = 0; // 每帧时间间隔\n};\n\nlet engineTime = new EngineTime(); // 创建引擎时间实例\nlet frameCount: number = 0; // 帧计数器\n\n// 模拟每帧更新\nfunction TickFrame() {\n  if (frameCount == 10) {\n    engineTime.totalTimeUs += 1.0; // 累加总时间\n    engineTime.deltaTimeUs += 1.0; // 累加每帧时间间隔\n    frameCount = 0; // 重置帧计数器\n  } else {\n    frameCount++; // 帧计数器递增\n  }\n}\n\n@Entry\n@Component\nstruct Index {\n  scene: SceneOptions = { scene: $rawfile('gltf/DamageHemlt/glTF/DamagedHelmet.gltf'), modelType: ModelType.SURFACE};\n  backAnimator: AnimatorResult = animator.create({\n    duration: 2000, // 动画持续时间\n    easing: "ease", // 缓动函数\n    delay: 0, // 延迟时间\n    fill: "none", // 动画填充模式\n    direction: "normal", // 播放方向\n    iterations: -1, // 播放次数，-1为无限循环\n    begin: 100, // 起始值\n    end: 200, // 结束值\n  });\n  @State timeDelta: number[] = [1.0, 2.0]; // 时间间隔数组\n\n  // 创建函数，设置动画回调\n  create() {\n    this.backAnimator.onfinish = () => {\n      console.log('backAnimator onfinish'); // 动画播放完成回调\n    }\n    this.backAnimator.onframe = value => {\n      TickFrame(); // 模拟每帧更新\n      this.timeDelta[0] = engineTime.deltaTimeUs; // 更新时间间隔数组\n    }\n  }\n\n  // 构建函数，渲染UI组件\n  build() {\n    Row() {\n      Column() {\n        Text('custom rendering') // 显示文本\n        Component3D()\n          .shader($rawfile('assets/app/shaders/shader/London.shader')) // 设置着色器\n          .shaderImageTexture($rawfile('assets/London.jpg')) // 设置着色器纹理\n          .shaderInputBuffer(this.timeDelta) // 设置着色器输入缓冲\n          .customRender($rawfile('assets/app/rendernodegraphs/London.rng'), true) // 自定义渲染\n          .renderWidth('90%').renderHeight('90%') // 设置渲染宽度和高度\n          .onAppear(() => {\n            this.create(); // 创建动画回调\n            this.backAnimator.play(); // 播放动画\n          }).width('50%').height('50%') // 设置宽度和高度\n      }.width('100%') // 设置宽度\n    }\n    .height('100%') // 设置高度\n  }\n}\n```\nimport { Animator as animator, AnimatorResult } from '@kit.ArkUI';\n\nclass EngineTime {\n  totalTimeUs = 0;\n  deltaTimeUs = 0;\n};\n\nlet engineTime = new EngineTime();\nlet frameCount: number = 0;\n\nfunction TickFrame() {\n  if (frameCount == 10) {\n    engineTime.totalTimeUs += 1.0;\n    engineTime.deltaTimeUs += 1.0;\n    frameCount = 0;\n  } else {\n    frameCount++;\n  }\n}\n\n@Entry\n@Component\nstruct Index {\n  scene: SceneOptions = { scene: $rawfile('gltf/DamageHemlt/glTF/DamagedHelmet.gltf'), modelType: ModelType.SURFACE};\n  backAnimator: AnimatorResult = animator.create({\n    duration: 2000,\n    easing: "ease",\n    delay: 0,\n    fill: "none",\n    direction: "normal",\n    iterations: -1,\n    begin: 100,\n    end: 200,\n  });\n  @State timeDelta: number[] = [1.0, 2.0];\n  create() {\n    this.backAnimator.onfinish = () => {\n      console.log('backAnimator onfinish');\n    }\n    this.backAnimator.onframe = value => {\n      TickFrame();\n      this.timeDelta[0] = engineTime.deltaTimeUs;\n    }\n\n  }\n  build() {\n    Row() {\n      Column() {\n        Text('custom rendering')\n        Component3D()\n          .shader($rawfile('assets/app/shaders/shader/London.shader'))\n          .shaderImageTexture($rawfile('assets/London.jpg'))\n          .shaderInputBuffer(this.timeDelta)\n          .customRender($rawfile('assets/app/rendernodegraphs/London.rng'), true)\n          .renderWidth('90%').renderHeight('90%')\n          .onAppear(() => {\n            this.create();\n            this.backAnimator.play();\n          }).width('50%').height('50%')\n      }.width('100%')\n    }\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "ContainerSpan": {
        "description": "Text组件的子组件，用于统一管理多个Span、ImageSpan的背景色及圆角弧度。",
        "interfaces": [
            {
                "description": "ContainerSpan()创建ContainerSpan组件。",
                "params": {}
            }
        ],
        "attributes": {
            "textBackgroundStyle": {
                "description": "设置文本背景样式。子组件在不设置该属性时，将继承此属性值。",
                "params": {
                    "style": {
                        "type": "TextBackgroundStyle",
                        "required": True,
                        "description": "文本背景样式。",
                        "default": {
                            "color": "Color.Transparent",
                            "radius": 0
                        }
                    }
                }
            },
            "attributeModifier": {
                "description": "设置组件的动态属性。",
                "params": {
                    "modifier": {
                        "type": "AttributeModifier<ContainerSpanAttribute>",
                        "required": True,
                        "description": "动态设置组件的属性。",
                        "default": {
                            "color": "Color.Transparent",
                            "radius": 0
                        }
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """// xxx.ets\n\n// 创建一个名为Index的组件，作为入口组件\n@Component\n@Entry\nstruct Index {\n  build() {\n    // 创建一个垂直布局的Column组件\n    Column() {\n      // 创建一个文本组件\n      Text() {\n        // 创建一个容器内的图片组件，显示应用图标\n        ContainerSpan() {\n          ImageSpan($r('app.media.app_icon'))\n            .width('40vp') // 设置图片宽度为40vp\n            .height('40vp') // 设置图片高度为40vp\n            .verticalAlign(ImageSpanAlignment.CENTER) // 图片垂直居中显示\n          // 创建一个文本Span，显示"Hello World !"\n          Span('   Hello World !   ').fontSize('16fp').fontColor(Color.White)\n        }.textBackgroundStyle({color: "#7F007DFF", radius: "12vp"}) // 设置文本背景样式为紫色圆角矩形\n      }\n    }.width('100%').alignItems(HorizontalAlign.Center) // 设置Column宽度为100%，水平居中对齐\n  }\n}\n```\n\n功能与效果描述：\n1. 创建了一个名为Index的入口组件，包含了一个垂直布局的Column组件。\n2. 在Column组件中，包含了一个文本组件，其中嵌套了一个容器内的图片组件和一个文本Span组件。\n3. 图片组件显示了应用图标，设置了宽度、高度和垂直居中显示。\n4. 文本Span组件显示了"Hello World !"文本，设置了字体大小、字体颜色以及文本背景样式为紫色圆角矩形。\n5. 整体布局宽度为100%，并且水平居中对齐。\n// xxx.ets\n@Component\n@Entry\nstruct Index {\n  build() {\n    Column() {\n      Text() {\n        ContainerSpan() {\n          ImageSpan($r('app.media.app_icon'))\n            .width('40vp')\n            .height('40vp')\n            .verticalAlign(ImageSpanAlignment.CENTER)\n          Span('   Hello World !   ').fontSize('16fp').fontColor(Color.White)\n        }.textBackgroundStyle({color: "#7F007DFF", radius: "12vp"})\n      }\n    }.width('100%').alignItems(HorizontalAlign.Center)\n  }\n}"""
        ],
        "is_common_attrs": False
    },
    "DataPanel": {
        "description": "数据面板组件，用于将多个数据占比情况使用占比图进行展示。",
        "interfaces": [
            {
                "description": "DataPanel(options: DataPanelOptions)",
                "params": {
                    "options": {
                        "type": "DataPanelOptions",
                        "required": True,
                        "description": "数据面板的配置选项。"
                    }
                }
            }
        ],
        "attributes": {
            "closeEffect": {
                "description": "设置关闭数据占比图表旋转动效和投影效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "关闭数据占比图表旋转动效和投影效果。",
                        "default": False
                    }
                }
            },
            "valueColors": {
                "description": "设置各数据段颜色。",
                "params": {
                    "value": {
                        "type": "Array<ResourceColor | LinearGradient>",
                        "required": True,
                        "description": "各数据段颜色。"
                    }
                }
            },
            "trackBackgroundColor": {
                "description": "设置底板颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "底板颜色。",
                        "default": "#08182431"
                    }
                }
            },
            "strokeWidth": {
                "description": "设置圆环粗细。数据面板的类型为 DataPanelType.Line 时该属性不生效。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "圆环粗细。",
                        "default": 24
                    }
                }
            },
            "trackShadow": {
                "description": "设置投影样式。",
                "params": {
                    "value": {
                        "type": "DataPanelShadowOptions",
                        "required": True,
                        "description": "投影样式。"
                    }
                }
            },
            "contentModifier": {
                "description": "定制 DataPanel 内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<DataPanelConfiguration>",
                        "required": True,
                        "description": "定制 DataPanel 内容区的方法。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """// xxx.ets\n@Entry\n@Component\nstruct DataPanelExample {\n  public valueArr: number[] = [10, 10, 10, 10, 10, 10, 10, 10, 10]\n\n  build() {\n    // 创建一个包含多个数据面板的布局\n    Column({ space: 5 }) {\n      // 第一个数据面板\n      Row() {\n        Stack() {\n          // 创建一个圆形数据面板，数值为30，最大值为100\n          DataPanel({ values: [30], max: 100, type: DataPanelType.Circle }).width(168).height(168)\n          // 数值显示为30\n          Column() {\n            Text('30').fontSize(35).fontColor('#182431')\n            // 版本号显示为1.0.0\n            Text('1.0.0').fontSize(9.33).lineHeight(12.83).fontWeight(500).opacity(0.6)\n          }\n\n          // 百分号显示\n          Text('%')\n            .fontSize(9.33)\n            .lineHeight(12.83)\n            .fontWeight(500)\n            .opacity(0.6)\n            .position({ x: 104.42, y: 78.17 })\n        }.margin({ right: 44 })\n\n        Stack() {\n          // 创建另一个圆形数据面板，数值为50, 12, 8, 5，最大值为100\n          DataPanel({ values: [50, 12, 8, 5], max: 100, type: DataPanelType.Circle }).width(168).height(168)\n          // 数值显示为75\n          Column() {\n            Text('75').fontSize(35).fontColor('#182431')\n            // 已使用空间显示为98GB/128GB\n            Text('已使用98GB/128GB').fontSize(8.17).lineHeight(11.08).fontWeight(500).opacity(0.6)\n          }\n\n          // 百分号显示\n          Text('%')\n            .fontSize(9.33)\n            .lineHeight(12.83)\n            .fontWeight(500)\n            .opacity(0.6)\n            .position({ x: 104.42, y: 78.17 })\n        }\n      }.margin({ bottom: 59 })\n\n      // 创建一条线形数据面板，显示valueArr数组的数据，最大值为100\n      DataPanel({ values: this.valueArr, max: 100, type: DataPanelType.Line }).width(300).height(20)\n    }.width('100%').margin({ top: 5 })\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct DataPanelExample {\n  public valueArr: number[] = [10, 10, 10, 10, 10, 10, 10, 10, 10]\n\n  build() {\n    Column({ space: 5 }) {\n      Row() {\n        Stack() {\n          DataPanel({ values: [30], max: 100, type: DataPanelType.Circle }).width(168).height(168)\n          Column() {\n            Text('30').fontSize(35).fontColor('#182431')\n            Text('1.0.0').fontSize(9.33).lineHeight(12.83).fontWeight(500).opacity(0.6)\n          }\n\n          Text('%')\n            .fontSize(9.33)\n            .lineHeight(12.83)\n            .fontWeight(500)\n            .opacity(0.6)\n            .position({ x: 104.42, y: 78.17 })\n        }.margin({ right: 44 })\n\n        Stack() {\n          DataPanel({ values: [50, 12, 8, 5], max: 100, type: DataPanelType.Circle }).width(168).height(168)\n          Column() {\n            Text('75').fontSize(35).fontColor('#182431')\n            Text('已使用98GB/128GB').fontSize(8.17).lineHeight(11.08).fontWeight(500).opacity(0.6)\n          }\n\n          Text('%')\n            .fontSize(9.33)\n            .lineHeight(12.83)\n            .fontWeight(500)\n            .opacity(0.6)\n            .position({ x: 104.42, y: 78.17 })\n        }\n      }.margin({ bottom: 59 })\n\n      DataPanel({ values: this.valueArr, max: 100, type: DataPanelType.Line }).width(300).height(20)\n    }.width('100%').margin({ top: 5 })\n  }\n}"""
            """// xxx.ets\n@Entry\n@Component\nstruct LinearGradientDataPanelExample {\n  public values1: number[] = [20, 20, 20, 20]\n  public color1: LinearGradient = new LinearGradient([{ color: "#65EEC9A3", offset: 0 }, { color: "#FFEF629F", offset: 1 }])\n  public color2: LinearGradient = new LinearGradient([{ color: "#FF67F9D4", offset: 0 }, { color: "#FFFF9554", offset: 1 }])\n  public colorShadow1: LinearGradient = new LinearGradient([{ color: "#65EEC9A3", offset: 0 }, { color: "#65EF629F", offset: 1 }])\n  public colorShadow2: LinearGradient = new LinearGradient([{ color: "#65e26709", offset: 0 }, { color: "#65efbd08", offset: 1 }])\n  public colorShadow3: LinearGradient = new LinearGradient([{ color: "#6572B513", offset: 0 }, { color: "#6508efa6", offset: 1 }])\n  public colorShadow4: LinearGradient = new LinearGradient([{ color: "#65ed08f5", offset: 0 }, { color: "#65ef0849", offset: 1 }])\n  @State color3: string = '#00FF00'\n  @State color4: string = '#20FF0000'\n  @State bgColor: string = '#08182431'\n  @State offsetX: number = 15\n  @State offsetY: number = 15\n  @State radius: number = 5\n  @State colorArray: Array<LinearGradient | ResourceColor> = [this.color1, this.color2, this.color3, this.color4]\n  @State shadowColorArray: Array<LinearGradient | ResourceColor> = [this.colorShadow1, this.colorShadow2, this.colorShadow3, this.colorShadow4]\n\n  // 构建线性渐变数据面板示例\n  build() {\n    Column({ space: 5 }) {\n      // 添加线性渐变文本\n      Text('LinearGradient').fontSize(9).fontColor(0xCCCCCC).textAlign(TextAlign.Start).width('100%').margin({ top: 20, left: 20})\n      // 创建数据面板，展示数据值，采用圆形展示方式\n      DataPanel({ values: this.values1, max: 100, type: DataPanelType.Circle })\n        .width(300)\n        .height(300)\n        .valueColors(this.colorArray) // 设置数据值颜色\n        .trackShadow({\n          radius: this.radius, // 设置阴影半径\n          colors: this.shadowColorArray, // 设置阴影颜色\n          offsetX: this.offsetX, // 设置阴影水平偏移量\n          offsetY: this.offsetY // 设置阴影垂直偏移量\n        })\n        .strokeWidth(30) // 设置描边宽度\n        .trackBackgroundColor(this.bgColor) // 设置背景颜色\n    }.width('100%').margin({ top: 5 }) // 设置宽度和外边距\n  }\n}     \n```\n// xxx.ets\n@Entry\n@Component\nstruct LinearGradientDataPanelExample {\n  public values1: number[] = [20, 20, 20, 20]\n  public color1: LinearGradient = new LinearGradient([{ color: "#65EEC9A3", offset: 0 }, { color: "#FFEF629F", offset: 1 }])\n  public color2: LinearGradient = new LinearGradient([{ color: "#FF67F9D4", offset: 0 }, { color: "#FFFF9554", offset: 1 }])\n  public colorShadow1: LinearGradient = new LinearGradient([{ color: "#65EEC9A3", offset: 0 }, { color: "#65EF629F", offset: 1 }])\n  public colorShadow2: LinearGradient = new LinearGradient([{ color: "#65e26709", offset: 0 }, { color: "#65efbd08", offset: 1 }])\n  public colorShadow3: LinearGradient = new LinearGradient([{ color: "#6572B513", offset: 0 }, { color: "#6508efa6", offset: 1 }])\n  public colorShadow4: LinearGradient = new LinearGradient([{ color: "#65ed08f5", offset: 0 }, { color: "#65ef0849", offset: 1 }])\n  @State color3: string = '#00FF00'\n  @State color4: string = '#20FF0000'\n  @State bgColor: string = '#08182431'\n  @State offsetX: number = 15\n  @State offsetY: number = 15\n  @State radius: number = 5\n  @State colorArray: Array<LinearGradient | ResourceColor> = [this.color1, this.color2, this.color3, this.color4]\n  @State shadowColorArray: Array<LinearGradient | ResourceColor> = [this.colorShadow1, this.colorShadow2, this.colorShadow3, this.colorShadow4]\n\n  build() {\n    Column({ space: 5 }) {\n      Text('LinearGradient').fontSize(9).fontColor(0xCCCCCC).textAlign(TextAlign.Start).width('100%').margin({ top: 20, left: 20})\n      DataPanel({ values: this.values1, max: 100, type: DataPanelType.Circle })\n        .width(300)\n        .height(300)\n        .valueColors(this.colorArray)\n        .trackShadow({\n          radius: this.radius,\n          colors: this.shadowColorArray,\n          offsetX: this.offsetX,\n          offsetY: this.offsetY\n        })\n        .strokeWidth(30)\n        .trackBackgroundColor(this.bgColor)\n    }.width('100%').margin({ top: 5 })\n  }\n}"""
            """// xxx.ets\n\n// 构建数据面板，展示数据列表及相关信息\n@Builder\nfunction buildDataPanel(config: DataPanelConfiguration) {\n  Column() {\n    // 列表展示数据项\n    Column() {\n      ForEach(config.values, (item: number, index: number) => {\n        ChildItem({ item: item, index: index, max:config.maxValue })\n      }, (item: string) => item)\n    }.padding(10)\n\n    // 分割线\n    Line().width(360).backgroundColor("#ff373737").margin({bottom:5})\n\n    // 显示数据面板信息\n    Row() {\n      Text('Length=' + config.values.length + '    ').margin({ left: 10 }).align(Alignment.Start)\n      Text('Max=' + config.maxValue).margin({ left: 10 }).align(Alignment.Start)\n    }\n  }\n}\n\n// 数据面板构建器，用于应用内容修改器\nclass DataPanelBuilder implements ContentModifier<DataPanelConfiguration> {\n  constructor() {\n  }\n  applyContent () : WrappedBuilder<[DataPanelConfiguration]> {\n    return wrapBuilder(buildDataPanel)\n  }\n}\n\n// 入口组件\n@Entry\n@Component\nstruct Index {\n  build() {\n    Column() {\n      // 标题\n      Text("Data panel").margin({ top: 12 });\n\n      // 数据面板展示\n      Row() {\n        DataPanel({ values: [12.3, 21.1, 13.4, 35.2, 26.0, 32.0], max: 140, type: DataPanelType.Circle })\n          .width(400).height(260)\n          .padding({ top: 10 })\n          .contentModifier(new DataPanelBuilder())\n      }.margin(15).backgroundColor("#fff5f5f5")\n    }\n  }\n}\n\n// 子项组件，展示数据子项\n@Component\nstruct ChildItem {\n  @Prop item: number;\n  @Prop index: number;\n  @Prop max: number;\n  public color1: string = "#65ff00dd"\n  public color2: string = "#6500ff99"\n  public color3: string = "#65ffe600"\n  public color4: string = "#6595ff00"\n  public color5: string = "#65000dff"\n  public color6: string = "#650099ff"\n  public colorArray: Array<string> = [this.color1, this.color2, this.color3, this.color4, this.color5, this.color6]\n\n  build() {\n    // 相对容器\n    RelativeContainer() {\n      Row() {\n        // 矩形条展示数据大小\n        Rect().height(25).width(this.item * 600 / this.max).foregroundColor(this.colorArray[this.index]).radius(5)\n          .align(Alignment.Start)\n        // 文本显示数据值\n        Text(" "+this.item)\n          .fontSize(17)\n      }\n    }.height(28)\n  }\n}\n```\n// xxx.ets\n@Builder\nfunction buildDataPanel(config: DataPanelConfiguration) {\n  Column() {\n    Column() {\n      ForEach(config.values, (item: number, index: number) => {\n        ChildItem({ item: item, index: index, max:config.maxValue})\n      }, (item: string) => item)\n    }.padding(10)\n    Line().width(360).backgroundColor("#ff373737").margin({bottom:5})\n    Row() {\n      Text('Length=' + config.values.length + '    ').margin({ left: 10 }).align(Alignment.Start)\n      Text('Max=' + config.maxValue).margin({ left: 10 }).align(Alignment.Start)\n    }\n  }\n}\n\nclass DataPanelBuilder implements ContentModifier<DataPanelConfiguration> {\n  constructor() {\n  }\n  applyContent () : WrappedBuilder<[DataPanelConfiguration]> {\n    return wrapBuilder(buildDataPanel)\n  }\n}\n\n@Entry\n@Component\nstruct Index {\n  build() {\n    Column() {\n      Text("Data panel").margin({ top: 12 });\n      Row() {\n        DataPanel({ values: [12.3, 21.1, 13.4, 35.2, 26.0, 32.0], max: 140, type: DataPanelType.Circle })\n          .width(400).height(260)\n          .padding({ top: 10 })\n          .contentModifier(new DataPanelBuilder())\n      }.margin(15).backgroundColor("#fff5f5f5")\n    }\n  }\n}\n\n@Component\nstruct ChildItem {\n  @Prop item: number;\n  @Prop index: number;\n  @Prop max: number;\n  public color1: string = "#65ff00dd"\n  public color2: string = "#6500ff99"\n  public color3: string = "#65ffe600"\n  public color4: string = "#6595ff00"\n  public color5: string = "#65000dff"\n  public color6: string = "#650099ff"\n  public colorArray: Array<string> = [this.color1, this.color2, this.color3, this.color4, this.color5, this.color6]\n\n  build() {\n    RelativeContainer() {\n      Row() {\n        Rect().height(25).width(this.item * 600 / this.max).foregroundColor(this.colorArray[this.index]).radius(5)\n          .align(Alignment.Start)\n        Text(" "+this.item)\n          .fontSize(17)\n      }\n    }.height(28)\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "DatePicker": {
        "description": "日期选择器组件，用于根据指定日期范围创建日期滑动选择器。",
        "interfaces": [
            {
                "description": "根据指定范围的Date创建可以选择日期的滑动选择器。",
                "params": {
                    "options": {
                        "type": "DatePickerOptions",
                        "required": False,
                        "description": "配置日期选择器组件的参数。"
                    }
                }
            }
        ],
        "attributes": {
            "lunar": {
                "description": "设置弹窗的日期是否显示农历。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "日期是否显示农历。"
                    }
                }
            },
            "disappearTextStyle": {
                "description": "设置所有选项中最上和最下两个选项的文本样式。",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。"
                    }
                }
            },
            "textStyle": {
                "description": "设置所有选项中除了最上、最下及选中项以外的文本样式。",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。"
                    }
                }
            },
            "selectedTextStyle": {
                "description": "设置选中项的文本样式。",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "选中项的文本颜色、字号、字体粗细。"
                    }
                }
            }
        },
        "events": {
            "onDateChange": {
                "description": "选择日期时触发该事件。",
                "params": {
                    "value": {
                        "type": "Date",
                        "required": True,
                        "description": "返回选中的时间，年月日为选中的日期，时分取决于当前系统时间的时分，秒恒为00。"
                    }
                }
            }
        },
        "examples": [
            "/*\n实现思路：\n本示例展示了如何使用DatePicker组件来选择日期，并支持切换公历和农历显示。通过一个按钮来切换日期显示模式，并在日期选择变化时更新选中的日期。\n*/\n// DatePickerExample.ets\n@Entry\n@Component\nstruct DatePickerExample {\n  @State isLunar: boolean = false // 用于控制日期显示模式，初始为公历\n  private selectedDate: Date = new Date('2021-08-08') // 初始选中的日期\n\n  build() {\n    Column() {\n      Button('切换公历农历')\n        .margin({ top: 30, bottom: 30 })\n        .onClick(() => {\n          this.isLunar = !this.isLunar // 切换日期显示模式\n        })\n      DatePicker({\n        start: new Date('1970-1-1'), // 日期选择范围的起始日期\n        end: new Date('2100-1-1'), // 日期选择范围的结束日期\n        selected: this.selectedDate // 当前选中的日期\n      })\n        .disappearTextStyle({color: Color.Gray, font: {size: '16fp', weight: FontWeight.Bold}}) // 设置不可见文本的样式\n        .textStyle({color: '#ff182431', font: {size: '18fp', weight: FontWeight.Normal}}) // 设置普通文本的样式\n        .selectedTextStyle({color: '#ff0000FF', font: {size: '26fp', weight: FontWeight.Regular}}) // 设置选中日期的文本样式\n        .lunar(this.isLunar) // 根据isLunar状态切换公历或农历显示\n        .onDateChange((value: Date) => {\n          this.selectedDate = value // 更新选中的日期\n          console.info('select current date is: ' + value.toString()) // 输出当前选中的日期\n        })\n\n    }.width('100%')\n  }\n}"
        ]
    },
    "Divider": {
        "description": "提供分隔器组件，分隔不同内容块/内容元素。",
        "interfaces": [
            {
                "description": "创建Divider组件。",
                "params": {}
            }
        ],
        "attributes": {
            "vertical": {
                "description": "设置分割线的方向。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "使用水平分割线还是垂直分割线。",
                        "default": False
                    }
                }
            },
            "color": {
                "description": "设置分割线的颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "分割线颜色。",
                        "default": "#33182431"
                    }
                }
            },
            "strokeWidth": {
                "description": "设置分割线的宽度。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "分割线宽度。",
                        "default": "1px"
                    }
                }
            },
            "lineCap": {
                "description": "设置分割线的端点样式。",
                "params": {
                    "value": {
                        "type": "LineCapStyle",
                        "required": True,
                        "description": "分割线的端点样式。",
                        "default": "LineCapStyle.Butt"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """示例1:```typescript\n// xxx.ets\n\n// 示例代码展示了如何使用横向和纵向分割线，以及在不同场景下的效果展示\n\n@Entry\n@Component\nstruct DividerExample {\n  build() {\n    // 横向分割线场景\n    Column() {\n      // 横向分割线标题\n      Text('Horizontal divider').fontSize(9).fontColor(0xCCCCCC)\n      \n      // 列表1\n      List() {\n        ForEach([1, 2, 3], (item: number) => {\n          ListItem() {\n            Text('list' + item).width('100%').fontSize(14).fontColor('#182431').textAlign(TextAlign.Start)\n          }.width(244).height(48)\n        }, (item: number) => item.toString())\n      }.padding({ left: 24, bottom: 8 })\n\n      // 横向分割线\n      Divider().strokeWidth(8).color('#F1F3F5')\n      \n      // 列表2\n      List() {\n        ForEach([4, 5], (item: number) => {\n          ListItem() {\n            Text('list' + item).width('100%').fontSize(14).fontColor('#182431').textAlign(TextAlign.Start)\n          }.width(244).height(48)\n        }, (item: number) => item.toString())\n      }.padding({ left: 24, top: 8 })\n\n      // 纵向分割线场景\n      Text('Vertical divider').fontSize(9).fontColor(0xCCCCCC)\n      \n      // 纵向分割线内容\n      Column() {\n        Column() {\n          // 左侧内容\n          Row().width(288).height(64).backgroundColor('#30C9F0').opacity(0.3)\n          Row() {\n            // 左侧按钮\n            Button('Button')\n              .width(136)\n              .height(22)\n              .fontSize(16)\n              .fontColor('#007DFF')\n              .fontWeight(500)\n              .backgroundColor(Color.Transparent)\n            // 纵向分割线\n            Divider().vertical(true).height(22).color('#182431').opacity(0.6).margin({ left: 8, right: 8 })\n            // 右侧按钮\n            Button('Button')\n              .width(136)\n              .height(22)\n              .fontSize(16)\n              .fontColor('#007DFF')\n              .fontWeight(500)\n              .backgroundColor(Color.Transparent)\n          }.margin({ top: 17 })\n        }\n        .width(336)\n        .height(152)\n        .backgroundColor('#FFFFFF')\n        .borderRadius(24)\n        .padding(24)\n      }\n      .width('100%')\n      .height(168)\n      .backgroundColor('#F1F3F5')\n      .justifyContent(FlexAlign.Center)\n      .margin({ top: 8 })\n    }.width('100%').padding({ top: 24 })\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct DividerExample {\n  build() {\n    Column() {\n      // 使用横向分割线场景\n      Text('Horizontal divider').fontSize(9).fontColor(0xCCCCCC)\n      List() {\n        ForEach([1, 2, 3], (item: number) => {\n          ListItem() {\n            Text('list' + item).width('100%').fontSize(14).fontColor('#182431').textAlign(TextAlign.Start)\n          }.width(244).height(48)\n        }, (item: number) => item.toString())\n      }.padding({ left: 24, bottom: 8 })\n\n      Divider().strokeWidth(8).color('#F1F3F5')\n      List() {\n        ForEach([4, 5], (item: number) => {\n          ListItem() {\n            Text('list' + item).width('100%').fontSize(14).fontColor('#182431').textAlign(TextAlign.Start)\n          }.width(244).height(48)\n        }, (item: number) => item.toString())\n      }.padding({ left: 24, top: 8 })\n\n      // 使用纵向分割线场景\n      Text('Vertical divider').fontSize(9).fontColor(0xCCCCCC)\n      Column() {\n        Column() {\n          Row().width(288).height(64).backgroundColor('#30C9F0').opacity(0.3)\n          Row() {\n            Button('Button')\n              .width(136)\n              .height(22)\n              .fontSize(16)\n              .fontColor('#007DFF')\n              .fontWeight(500)\n              .backgroundColor(Color.Transparent)\n            Divider().vertical(true).height(22).color('#182431').opacity(0.6).margin({ left: 8, right: 8 })\n            Button('Button')\n              .width(136)\n              .height(22)\n              .fontSize(16)\n              .fontColor('#007DFF')\n              .fontWeight(500)\n              .backgroundColor(Color.Transparent)\n          }.margin({ top: 17 })\n        }\n        .width(336)\n        .height(152)\n        .backgroundColor('#FFFFFF')\n        .borderRadius(24)\n        .padding(24)\n      }\n      .width('100%')\n      .height(168)\n      .backgroundColor('#F1F3F5')\n      .justifyContent(FlexAlign.Center)\n      .margin({ top: 8 })\n    }.width('100%').padding({ top: 24 })\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Gauge": {
        "description": "数据量规图表组件，用于将数据展示为环形图表。",
        "interfaces": [
            {
                "description": "创建数据量规图表组件。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "量规图的当前数据值，即图中指针指向位置。用于组件创建时量规图初始值的预置。"
                    },
                    "min": {
                        "type": "number",
                        "required": False,
                        "description": "当前数据段最小值。",
                        "default": 0
                    },
                    "max": {
                        "type": "number",
                        "required": False,
                        "description": "当前数据段最大值。",
                        "default": 100
                    }
                }
            }
        ],
        "attributes": {
            "value": {
                "description": "设置量规图的数据值。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "量规图的数据值，可用于动态修改量规图的数据值。",
                        "default": 0
                    }
                }
            },
            "startAngle": {
                "description": "设置起始角度位置。",
                "params": {
                    "angle": {
                        "type": "number",
                        "required": True,
                        "description": "起始角度位置，时钟0点为0度，顺时针方向为正角度。",
                        "default": 0
                    }
                }
            },
            "endAngle": {
                "description": "设置终止角度位置。起始角度位置和终止角度位置差过小时，会绘制出异常图像，请取合理的起始角度位置和终止角度位置。建议使用单色环改变Gauge的value参数实现数据值的调节，可通过定时器setTimeout进行数值的延迟加载。",
                "params": {
                    "angle": {
                        "type": "number",
                        "required": True,
                        "description": "终止角度位置，时钟0点为0度，顺时针方向为正角度。",
                        "default": 360
                    }
                }
            },
            "colors": {
                "description": "设置量规图的颜色。",
                "params": {
                    "colors": {
                        "type": ["ResourceColor", "LinearGradient", "Array<[ResourceColor | LinearGradient | number]>"],
                        "required": True,
                        "description": "量规图的颜色。"
                    }
                }
            },
            "strokeWidth": {
                "description": "设置环形量规图的环形厚度。",
                "params": {
                    "length": {
                        "type": "Length",
                        "required": True,
                        "description": "环形量规图的环形厚度。",
                        "default": 4
                    }
                }
            },
            "description": {
                "description": "设置说明内容。",
                "params": {
                    "value": {
                        "type": "CustomBuilder",
                        "required": True,
                        "description": "说明内容。"
                    }
                }
            },
            "trackShadow": {
                "description": "设置阴影样式。",
                "params": {
                    "value": {
                        "type": "GaugeShadowOptions",
                        "required": True,
                        "description": "阴影样式。"
                    }
                }
            },
            "indicator": {
                "description": "设置指针样式。",
                "params": {
                    "value": {
                        "type": "GaugeIndicatorOptions",
                        "required": True,
                        "description": "指针样式。"
                    }
                }
            },
            "privacySensitive": {
                "description": "设置隐私敏感。",
                "params": {
                    "isPrivacySensitiveMode": {
                        "type": "Optional<boolean>",
                        "required": True,
                        "description": "设置隐私敏感，隐私模式下Gauge指针指向0位置，最大值最小值文本将被遮罩，量程显示灰色或者底色。"
                    }
                }
            },
            "contentModifier": {
                "description": "定制Slider内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<GaugeConfiguration>",
                        "required": True,
                        "description": "定制Slider内容区的方法。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """示例1:@Entry\n@Component\nstruct Gauge1 {\n  @Builder descriptionBuilder() {\n    Text('说明文本')\n      .maxFontSize('30sp')\n      .minFontSize("10.0vp")\n      .fontColor("#fffa2a2d")\n      .fontWeight(FontWeight.Medium)\n      .width('100%')\n      .height("100%")\n      .textAlign(TextAlign.Center)\n  }\n\n  build() {\n    Column() {\n      // 创建一个仪表盘组件，显示数值为50，范围从1到100\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          // 显示当前数值为50\n          Text('50')\n            .fontWeight(FontWeight.Medium)\n            .width('62%')\n            .fontColor("#ff182431")\n            .maxFontSize("60.0vp")\n            .minFontSize("30.0vp")\n            .textAlign(TextAlign.Center)\n            .margin({ top: '35%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n          // 显示辅助文本\n          Text('辅助文本')\n            .maxFontSize("16.0fp")\n            .minFontSize("10.0vp")\n            .fontColor($r('sys.color.ohos_id_color_text_secondary'))\n            .fontWeight(FontWeight.Regular)\n            .width('67.4%')\n            .height('9.5%')\n            .textAlign(TextAlign.Center)\n        }.width('100%').height('100%')\n      }\n      // 设置仪表盘的样式和属性\n      .value(50)\n      .startAngle(210)\n      .endAngle(150)\n      .colors([[...]]) // 设置不同数值范围的颜色渐变\n      .width('80%')\n      .height('80%')\n      .strokeWidth(18)\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n      .description(this.descriptionBuilder) // 设置说明文本\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}\n```\n\n在上述代码中：\n- `Gauge1` 结构体定义了一个仪表盘组件，用于展示数值在范围内的情况。\n- `descriptionBuilder` 方法用于构建说明文本的样式，包括字体大小、颜色、对齐方式等。\n- `build` 方法包含了整个仪表盘的布局和属性设置。\n- 仪表盘内部包含了显示当前数值和辅助文本的 `Text` 组件。\n- 通过设置 `value`、`startAngle`、`endAngle`、`colors`、`width`、`height`、`strokeWidth` 等属性来定制仪表盘的外观和行为。\n- `trackShadow` 方法添加了仪表盘的阴影效果。\n- `description` 方法将说明文本应用到仪表盘中。\n- 整体布局采用 `Column` 组件，并设置了外边距和宽高比例。\n@Entry\n@Component\nstruct Gauge1 {\n  @Builder descriptionBuilder() {\n    Text('说明文本')\n      .maxFontSize('30sp')\n      .minFontSize("10.0vp")\n      .fontColor("#fffa2a2d")\n      .fontWeight(FontWeight.Medium)\n      .width('100%')\n      .height("100%")\n      .textAlign(TextAlign.Center)\n  }\n\n  build() {\n    Column() {\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          Text('50')\n            .fontWeight(FontWeight.Medium)\n            .width('62%')\n            .fontColor("#ff182431")\n            .maxFontSize("60.0vp")\n            .minFontSize("30.0vp")\n            .textAlign(TextAlign.Center)\n            .margin({ top: '35%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n          Text('辅助文本')\n            .maxFontSize("16.0fp")\n            .minFontSize("10.0vp")\n            .fontColor($r('sys.color.ohos_id_color_text_secondary'))\n            .fontColor($r('sys.color.ohos_id_color_text_secondary'))\n            .fontWeight(FontWeight.Regular)\n            .width('67.4%')\n            .height('9.5%')\n            .textAlign(TextAlign.Center)\n        }.width('100%').height('100%')\n      }\n      .value(50)\n      .startAngle(210)\n      .endAngle(150)\n      .colors([[new LinearGradient([{ color: "#deb6fb", offset: 0 }, { color: "#ac49f5", offset: 1 }]), 9],\n        [new LinearGradient([{ color: "#bbb7fc", offset: 0 }, { color: "#564af7", offset: 1 }]), 8],\n        [new LinearGradient([{ color: "#f5b5c2", offset: 0 }, { color: "#e64566", offset: 1 }]), 7],\n        [new LinearGradient([{ color: "#f8c5a6", offset: 0 }, { color: "#ed6f21", offset: 1 }]), 6],\n        [new LinearGradient([{ color: "#fceb99", offset: 0 }, { color: "#f7ce00", offset: 1 }]), 5],\n        [new LinearGradient([{ color: "#dbefa5", offset: 0 }, { color: "#a5d61d", offset: 1 }]), 4],\n        [new LinearGradient([{ color: "#c1e4be", offset: 0 }, { color: "#64bb5c", offset: 1 }]), 3],\n        [new LinearGradient([{ color: "#c0ece5", offset: 0 }, { color: "#61cfbe", offset: 1 }]), 2],\n        [new LinearGradient([{ color: "#b5e0f4", offset: 0 }, { color: "#46b1e3", offset: 1 }]), 1]])\n      .width('80%')\n      .height('80%')\n      .strokeWidth(18)\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n      .description(this.descriptionBuilder)\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}"""
            """示例2:@Entry\n@Component\nstruct Gauge2 {\n  @Builder descriptionBuilderImage() {\n    // 创建一个描述构建器，用于构建描述图片\n    Image($r('sys.media.ohos_ic_public_clock')).width(72).height(72)\n  }\n\n  build() {\n    // 构建函数，用于构建仪表盘组件\n    Column() {\n      // 创建一个垂直布局\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        // 创建一个仪表盘，初始值为50，范围为1到100\n        Column() {\n          // 创建一个垂直布局\n          Text('50')\n            // 显示文本为'50'\n            .fontWeight(FontWeight.Medium)\n            // 设置文本字体粗细为中等\n            .width('62%')\n            // 设置文本宽度占比\n            .fontColor("#ff182431")\n            // 设置文本颜色\n            .maxFontSize("60.0vp")\n            // 设置最大字体大小\n            .minFontSize("30.0vp")\n            // 设置最小字体大小\n            .textAlign(TextAlign.Center)\n            // 设置文本居中对齐\n            .margin({ top: '35%' })\n            // 设置文本上边距\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            // 设置文本溢出处理方式为省略号\n            .maxLines(1)\n            // 设置最大行数为1\n        }.width('100%').height('100%')\n        // 设置垂直布局宽度和高度为100%\n      }\n      .startAngle(210)\n      // 设置仪表盘起始角度\n      .endAngle(150)\n      // 设置仪表盘结束角度\n      .colors('#cca5d61d')\n      // 设置仪表盘颜色\n      .width('80%')\n      // 设置仪表盘宽度占比\n      .height('80%')\n      // 设置仪表盘高度占比\n      .strokeWidth(18)\n      // 设置仪表盘边框宽度\n      .description(this.descriptionBuilderImage)\n      // 设置仪表盘描述为描述构建器构建的图片\n      .padding(18)\n      // 设置仪表盘内边距\n    }.margin({ top: 40 }).width('100%').height('100%')\n    // 设置整体布局外边距、宽度和高度为100%\n  }\n}\n```\n@Entry\n@Component\nstruct Gauge2 {\n  @Builder descriptionBuilderImage() {\n    Image($r('sys.media.ohos_ic_public_clock')).width(72).height(72)\n  }\n\n  build() {\n    Column() {\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          Text('50')\n            .fontWeight(FontWeight.Medium)\n            .width('62%')\n            .fontColor("#ff182431")\n            .maxFontSize("60.0vp")\n            .minFontSize("30.0vp")\n            .textAlign(TextAlign.Center)\n            .margin({ top: '35%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n        }.width('100%').height('100%')\n      }\n      .startAngle(210)\n      .endAngle(150)\n      .colors('#cca5d61d')\n      .width('80%')\n      .height('80%')\n      .strokeWidth(18)\n      .description(this.descriptionBuilderImage)\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}"""
            """示例3:@Entry\n@Component\nstruct Gauge3 {\n  @Builder descriptionBuilder() {\n    // 创建说明文本\n    Text('说明文本')\n      .maxFontSize('30sp') // 设置最大字体大小为30sp\n      .minFontSize("10.0vp") // 设置最小字体大小为10.0vp\n      .fontColor("#fffa2a2d") // 设置字体颜色为#fffa2a2d\n      .fontWeight(FontWeight.Medium) // 设置字体粗细为Medium\n      .width('100%') // 设置宽度为100%\n      .height("100%") // 设置高度为100%\n      .textAlign(TextAlign.Center) // 设置文本居中对齐\n  }\n\n  build() {\n    // 构建整体布局\n    Column() {\n      Column() {\n        // 创建仪表盘\n        Gauge({ value: 50, min: 1, max: 100 }) {\n          Column() {\n            // 显示当前数值\n            Text('50')\n              .fontWeight(FontWeight.Medium) // 设置字体粗细为Medium\n              .width('62%') // 设置宽度为62%\n              .fontColor("#ff182431") // 设置字体颜色为#ff182431\n              .maxFontSize("60.0vp") // 设置最大字体大小为60.0vp\n              .minFontSize("30.0vp") // 设置最小字体大小为30.0vp\n              .textAlign(TextAlign.Center) // 设置文本居中对齐\n              .margin({ top: '35%' }) // 设置上边距为35%\n              .textOverflow({ overflow: TextOverflow.Ellipsis }) // 设置文本溢出时显示省略号\n              .maxLines(1) // 设置最大行数为1\n          }.width('100%').height('100%') // 设置宽度和高度为100%\n        }\n        .startAngle(210) // 设置起始角度为210度\n        .endAngle(150) // 设置结束角度为150度\n        .colors([[...]]) // 设置颜色渐变数组\n        .width('80%') // 设置宽度为80%\n        .height('80%') // 设置高度为80%\n        .strokeWidth(18) // 设置描边宽度为18\n        .description(this.descriptionBuilder) // 设置描述信息为descriptionBuilder返回的内容\n        .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 }) // 设置轨道阴影效果\n        .padding(18) // 设置内边距为18\n      }.margin({ top: 40 }).width('100%').height('100%') // 设置外边距、宽度和高度为100%\n    }\n  }\n}\n```\n@Entry\n@Component\nstruct Gauge3 {\n  @Builder descriptionBuilder() {\n    Text('说明文本')\n      .maxFontSize('30sp')\n      .minFontSize("10.0vp")\n      .fontColor("#fffa2a2d")\n      .fontWeight(FontWeight.Medium)\n      .width('100%')\n      .height("100%")\n      .textAlign(TextAlign.Center)\n  }\n\n  build() {\n    Column() {\n      Column() {\n        Gauge({ value: 50, min: 1, max: 100 }) {\n          Column() {\n            Text('50')\n              .fontWeight(FontWeight.Medium)\n              .width('62%')\n              .fontColor("#ff182431")\n              .maxFontSize("60.0vp")\n              .minFontSize("30.0vp")\n              .textAlign(TextAlign.Center)\n              .margin({ top: '35%' })\n              .textOverflow({ overflow: TextOverflow.Ellipsis })\n              .maxLines(1)\n          }.width('100%').height('100%')\n        }\n        .startAngle(210)\n        .endAngle(150)\n        .colors([[new LinearGradient([{ color: "#deb6fb", offset: 0 }, { color: "#ac49f5", offset: 1 }]), 9],\n          [new LinearGradient([{ color: "#bbb7fc", offset: 0 }, { color: "#564af7", offset: 1 }]), 8],\n          [new LinearGradient([{ color: "#f5b5c2", offset: 0 }, { color: "#e64566", offset: 1 }]), 7],\n          [new LinearGradient([{ color: "#f8c5a6", offset: 0 }, { color: "#ed6f21", offset: 1 }]), 6],\n          [new LinearGradient([{ color: "#fceb99", offset: 0 }, { color: "#f7ce00", offset: 1 }]), 5],\n          [new LinearGradient([{ color: "#dbefa5", offset: 0 }, { color: "#a5d61d", offset: 1 }]), 4],\n          [new LinearGradient([{ color: "#c1e4be", offset: 0 }, { color: "#64bb5c", offset: 1 }]), 3],\n          [new LinearGradient([{ color: "#c0ece5", offset: 0 }, { color: "#61cfbe", offset: 1 }]), 2],\n          [new LinearGradient([{ color: "#b5e0f4", offset: 0 }, { color: "#46b1e3", offset: 1 }]), 1]])\n        .width('80%')\n        .height('80%')\n        .strokeWidth(18)\n        .description(this.descriptionBuilder)\n        .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n        .padding(18)\n      }.margin({ top: 40 }).width('100%').height('100%')\n    }\n  }\n}"""
            """示例4:@Entry\n@Component\nstruct Gauge4 {\n  build() {\n    Column() {\n      // 创建一个仪表盘控件\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          // 显示当前数值文本\n          Text('50')\n            .maxFontSize("72.0vp")\n            .minFontSize("10.0vp")\n            .fontColor("#ff182431")\n            .width('40%')\n            .textAlign(TextAlign.Center)\n            .margin({ top: '35%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n          // 显示辅助文本\n          Text('辅助文本')\n            .maxFontSize("30.0vp")\n            .minFontSize("18.0vp")\n            .fontWeight(FontWeight.Medium)\n            .fontColor($r('sys.color.ohos_id_color_text_secondary'))\n            .width('62%')\n            .height('15.9%')\n            .textAlign(TextAlign.Center)\n        }.width('100%').height('100%')\n      }\n      // 设置仪表盘的起始角度和结束角度\n      .startAngle(210)\n      .endAngle(150)\n      // 设置不同数值范围的颜色渐变\n      .colors([[new LinearGradient([{ color: "#deb6fb", offset: 0 }, { color: "#ac49f5", offset: 1 }]), 9],\n        [new LinearGradient([{ color: "#bbb7fc", offset: 0 }, { color: "#564af7", offset: 1 }]), 8],\n        // 更多颜色设置...\n      ])\n      .width('80%')\n      .height('80%')\n      .strokeWidth(18)\n      .description(null)\n      // 设置轨道阴影效果\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}\n```\n@Entry\n@Component\nstruct Gauge4 {\n  build() {\n    Column() {\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          Text('50')\n            .maxFontSize("72.0vp")\n            .minFontSize("10.0vp")\n            .fontColor("#ff182431")\n            .width('40%')\n            .textAlign(TextAlign.Center)\n            .margin({ top: '35%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n          Text('辅助文本')\n            .maxFontSize("30.0vp")\n            .minFontSize("18.0vp")\n            .fontWeight(FontWeight.Medium)\n            .fontColor($r('sys.color.ohos_id_color_text_secondary'))\n            .width('62%')\n            .height('15.9%')\n            .textAlign(TextAlign.Center)\n        }.width('100%').height('100%')\n      }\n      .startAngle(210)\n      .endAngle(150)\n      .colors([[new LinearGradient([{ color: "#deb6fb", offset: 0 }, { color: "#ac49f5", offset: 1 }]), 9],\n        [new LinearGradient([{ color: "#bbb7fc", offset: 0 }, { color: "#564af7", offset: 1 }]), 8],\n        [new LinearGradient([{ color: "#f5b5c2", offset: 0 }, { color: "#e64566", offset: 1 }]), 7],\n        [new LinearGradient([{ color: "#f8c5a6", offset: 0 }, { color: "#ed6f21", offset: 1 }]), 6],\n        [new LinearGradient([{ color: "#fceb99", offset: 0 }, { color: "#f7ce00", offset: 1 }]), 5],\n        [new LinearGradient([{ color: "#dbefa5", offset: 0 }, { color: "#a5d61d", offset: 1 }]), 4],\n        [new LinearGradient([{ color: "#c1e4be", offset: 0 }, { color: "#64bb5c", offset: 1 }]), 3],\n        [new LinearGradient([{ color: "#c0ece5", offset: 0 }, { color: "#61cfbe", offset: 1 }]), 2],\n        [new LinearGradient([{ color: "#b5e0f4", offset: 0 }, { color: "#46b1e3", offset: 1 }]), 1]])\n      .width('80%')\n      .height('80%')\n      .strokeWidth(18)\n      .description(null)\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}"""
            """示例5:@Entry\n@Component\nstruct Gauge5 {\n  build() {\n    Column() {\n      // 创建一个仪表盘控件\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          // 显示当前数值为50的文本\n          Text('50')\n            .maxFontSize("80sp") // 设置最大字体大小为80sp\n            .minFontSize("60.0vp") // 设置最小字体大小为60.0vp\n            .fontWeight(FontWeight.Medium) // 设置字体粗细为中等\n            .fontColor("#ff182431") // 设置字体颜色为#ff182431\n            .width('40%') // 设置文本宽度为40%\n            .height('30%') // 设置文本高度为30%\n            .textAlign(TextAlign.Center) // 设置文本居中对齐\n            .margin({ top: '22.2%' }) // 设置文本上边距为22.2%\n            .textOverflow({ overflow: TextOverflow.Ellipsis }) // 设置文本溢出时显示省略号\n            .maxLines(1) // 设置最大显示行数为1\n        }.width('100%').height('100%') // 设置内部Column宽度和高度为100%\n      }\n      // 设置仪表盘的起始角度为225度，结束角度为135度\n      .startAngle(225)\n      .endAngle(135)\n      // 设置仪表盘的颜色渐变\n      .colors(new LinearGradient([{ color: "#e84026", offset: 0 },\n        { color: "#f7ce00", offset: 0.6 },\n        { color: "#64bb5c", offset: 1 }]))\n      .width('80%') // 设置仪表盘宽度为80%\n      .height('80%') // 设置仪表盘高度为80%\n      .strokeWidth(18) // 设置仪表盘边框宽度为18\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 }) // 设置仪表盘边框阴影效果\n      .padding(18) // 设置内边距为18\n    }.margin({ top: 40 }).width('100%').height('100%') // 设置外部Column的上边距、宽度和高度为100%\n  }\n}\n```\n@Entry\n@Component\nstruct Gauge5 {\n  build() {\n    Column() {\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          Text('50')\n            .maxFontSize("80sp")\n            .minFontSize("60.0vp")\n            .fontWeight(FontWeight.Medium)\n            .fontColor("#ff182431")\n            .width('40%')\n            .height('30%')\n            .textAlign(TextAlign.Center)\n            .margin({ top: '22.2%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n        }.width('100%').height('100%')\n      }\n      .startAngle(225)\n      .endAngle(135)\n      .colors(new LinearGradient([{ color: "#e84026", offset: 0 },\n        { color: "#f7ce00", offset: 0.6 },\n        { color: "#64bb5c", offset: 1 }]))\n      .width('80%')\n      .height('80%')\n      .strokeWidth(18)\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}"""
            """示例6:@Entry\n@Component\nstruct Gauge6 {\n  build() {\n    Column() {\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          // 显示当前数值为50的文本\n          Text('50')\n            .maxFontSize('60sp')\n            .minFontSize('30.0vp')\n            .fontWeight(FontWeight.Medium)\n            .fontColor("#ff182431")\n            .width('62%')\n            .textAlign(TextAlign.Center)\n            .margin({ top: '35%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n          // 显示辅助文本\n          Text('辅助文本')\n            .maxFontSize('16sp')\n            .minFontSize("10.0vp")\n            .fontColor($r('sys.color.ohos_id_color_text_secondary'))\n            .fontWeight(FontWeight.Regular)\n            .width('67.4%')\n            .height('9.5%')\n            .textAlign(TextAlign.Center)\n        }.width('100%').height('100%')\n      }\n      // 设置仪表盘的样式和属性\n      .startAngle(225)\n      .endAngle(135)\n      .colors(Color.Red)\n      .width('80%')\n      .height('80%')\n      .indicator(null)\n      .strokeWidth(18)\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}\n```\n\n在上述代码中，对`Gauge6`组件的功能与效果进行了详细描述和注释：\n1. 创建了一个仪表盘(`Gauge`)，显示数值为50，数值文本样式设置为居中显示，字体大小在60sp和30.0vp之间变化，字体颜色为"#ff182431"。\n2. 显示了一个辅助文本，样式设置为居中显示，字体大小在16sp和10.0vp之间变化，字体颜色为系统次要文本颜色。\n3. 设置了仪表盘的样式，包括起始角度、结束角度、颜色、宽度、高度、指示器等属性。\n4. 最外层`Column`设置了仪表盘的布局，包括外边距、宽度和高度。\n@Entry\n@Component\nstruct Gauge6 {\n  build() {\n    Column() {\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          Text('50')\n            .maxFontSize('60sp')\n            .minFontSize('30.0vp')\n            .fontWeight(FontWeight.Medium)\n            .fontColor("#ff182431")\n            .width('62%')\n            .textAlign(TextAlign.Center)\n            .margin({ top: '35%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n          Text('辅助文本')\n            .maxFontSize('16sp')\n            .minFontSize("10.0vp")\n            .fontColor($r('sys.color.ohos_id_color_text_secondary'))\n            .fontWeight(FontWeight.Regular)\n            .width('67.4%')\n            .height('9.5%')\n            .textAlign(TextAlign.Center)\n        }.width('100%').height('100%')\n      }\n      .startAngle(225)\n      .endAngle(135)\n      .colors(Color.Red)\n      .width('80%')\n      .height('80%')\n      .indicator(null)\n      .strokeWidth(18)\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}"""
            """示例7:@Entry\n@Component\nstruct Gauge7 {\n  build() {\n    Column() {\n      // 创建一个仪表盘控件\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          // 显示当前数值为50的文本\n          Text('50')\n            .maxFontSize('60sp') // 设置最大字体大小为60sp\n            .minFontSize('30.0vp') // 设置最小字体大小为30.0vp\n            .fontWeight(FontWeight.Medium) // 设置字体粗细为中等\n            .fontColor("#ff182431") // 设置字体颜色为深红色\n            .width('62%') // 设置文本宽度为62%\n            .textAlign(TextAlign.Center) // 设置文本居中对齐\n            .margin({ top: '35%' }) // 设置文本距离顶部的边距为35%\n            .textOverflow({ overflow: TextOverflow.Ellipsis }) // 设置文本溢出时显示省略号\n            .maxLines(1) // 设置最大显示行数为1\n        }.width('100%').height('100%') // 设置内部Column的宽度和高度均为100%\n      }\n      // 设置仪表盘的起始角度为225度，结束角度为135度\n      .startAngle(225)\n      .endAngle(135)\n      .colors(Color.Red) // 设置仪表盘颜色为红色\n      .width('80%') // 设置仪表盘宽度为80%\n      .height('80%') // 设置仪表盘高度为80%\n      .indicator(null) // 不显示指示器\n      .strokeWidth(18) // 设置仪表盘边框宽度为18\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 }) // 设置仪表盘轨道阴影效果\n      .padding(18) // 设置内边距为18\n    }.margin({ top: 40 }).width('100%').height('100%') // 设置外部Column的边距、宽度和高度均为100%\n  }\n}\n```\n@Entry\n@Component\nstruct Gauge7 {\n  build() {\n    Column() {\n      Gauge({ value: 50, min: 1, max: 100 }) {\n        Column() {\n          Text('50')\n            .maxFontSize('60sp')\n            .minFontSize('30.0vp')\n            .fontWeight(FontWeight.Medium)\n            .fontColor("#ff182431")\n            .width('62%')\n            .textAlign(TextAlign.Center)\n            .margin({ top: '35%' })\n            .textOverflow({ overflow: TextOverflow.Ellipsis })\n            .maxLines(1)\n        }.width('100%').height('100%')\n      }\n      .startAngle(225)\n      .endAngle(135)\n      .colors(Color.Red)\n      .width('80%')\n      .height('80%')\n      .indicator(null)\n      .strokeWidth(18)\n      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n      .padding(18)\n    }.margin({ top: 40 }).width('100%').height('100%')\n  }\n}"""
            """示例8:// xxx.ets\n// 该示例实现了Gauge组件使用Builder定制内容区，使用了环形图表组件，按钮和文本框。点击增加按钮，环形图表指针位置会向右偏移，反之点减少按钮环形图表指针位置会向左偏移。\n\n// 定义一个构建Gauge组件的函数，接受配置参数config\n@Builder\nfunction buildGauge(config: GaugeConfiguration) {\n  // 垂直布局，设置间距为30\n  Column({ space: 30 }) {\n    // 水平布局\n    Row() {\n      // 显示内容修改器的数值范围\n      Text('【ContentModifier】 value：' + JSON.stringify((config.contentModifier as MyGaugeStyle).value) +\n        '  min：' + JSON.stringify((config.contentModifier as MyGaugeStyle).min) +\n        '  max：' + JSON.stringify((config.contentModifier as MyGaugeStyle).max))\n        .fontSize(12)\n    }\n\n    // 显示配置参数的数值范围\n    Text('【Config】value：' + config.value + '  min：' + config.min + '  max：' + config.max).fontSize(12)\n    // 创建环形图表组件\n    Gauge({\n      value: config.value,\n      min: config.min,\n      max: config.max\n    }).width("50%")\n  }\n  .width("100%")\n  .padding(20)\n  .margin({ top: 5 })\n  .alignItems(HorizontalAlign.Center)\n}\n\n// 定义MyGaugeStyle类，实现ContentModifier接口\nclass MyGaugeStyle implements ContentModifier<GaugeConfiguration> {\n  value: number = 0\n  min: number = 0\n  max: number = 0\n\n  constructor(value: number, min: number, max: number) {\n    this.value = value\n    this.min = min\n    this.max = max\n  }\n\n  // 应用内容修改器\n  applyContent(): WrappedBuilder<[GaugeConfiguration]> {\n    return wrapBuilder(buildGauge)\n  }\n}\n\n// 入口组件\n@Entry\n@Component\nstruct refreshExample {\n  @State gaugeValue: number = 20\n  @State gaugeMin: number = 0\n  @State gaugeMax: number = 100\n\n  build() {\n    // 垂直布局，设置间距为20\n    Column({ space: 20 }) {\n      // 创建Gauge组件，并应用自定义的内容修改器MyGaugeStyle\n      Gauge({\n        value: this.gaugeValue,\n        min: this.gaugeMin,\n        max: this.gaugeMax\n      })\n        .contentModifier(new MyGaugeStyle(30, 10, 100))\n\n      // 垂直布局，设置间距为20\n      Column({ space: 20 }) {\n        // 水平布局，设置间距为20\n        Row({ space: 20 }) {\n          // 创建增加按钮，点击增加时增加指针位置\n          Button('增加').onClick(() => {\n            if (this.gaugeValue < this.gaugeMax) {\n              this.gaugeValue += 1\n            }\n          })\n          // 创建减少按钮，点击减少时减少指针位置\n          Button('减少').onClick(() => {\n            if (this.gaugeValue > this.gaugeMin) {\n              this.gaugeValue -= 1\n            }\n          })\n        }\n      }.width('100%')\n    }.width('100%').margin({ top: 5 })\n  }\n}\n```\n// xxx.ets\n//该示例实现了Gauge组件使用Builder定制内容区，使用了环形图表组件，按钮和文本框。点击增加按钮，环形图表指针位置会向右偏移，反之点减少按钮环形图表指针位置会向左偏移。\n@Builder\nfunction buildGauge(config: GaugeConfiguration) {\n  Column({ space: 30 }) {\n    Row() {\n      Text('【ContentModifier】 value：' + JSON.stringify((config.contentModifier as MyGaugeStyle).value) +\n        '  min：' + JSON.stringify((config.contentModifier as MyGaugeStyle).min) +\n        '  max：' + JSON.stringify((config.contentModifier as MyGaugeStyle).max))\n        .fontSize(12)\n    }\n\n    Text('【Config】value：' + config.value + '  min：' + config.min + '  max：' + config.max).fontSize(12)\n    Gauge({\n      value: config.value,\n      min: config.min,\n      max: config.max\n    }).width("50%")\n  }\n  .width("100%")\n  .padding(20)\n  .margin({ top: 5 })\n  .alignItems(HorizontalAlign.Center)\n}\n\nclass MyGaugeStyle implements ContentModifier<GaugeConfiguration> {\n  value: number = 0\n  min: number = 0\n  max: number = 0\n\n  constructor(value: number, min: number, max: number) {\n    this.value = value\n    this.min = min\n    this.max = max\n  }\n\n  applyContent(): WrappedBuilder<[GaugeConfiguration]> {\n    return wrapBuilder(buildGauge)\n  }\n}\n\n@Entry\n@Component\nstruct refreshExample {\n  @State gaugeValue: number = 20\n  @State gaugeMin: number = 0\n  @State gaugeMax: number = 100\n\n  build() {\n    Column({ space: 20 }) {\n      Gauge({\n        value: this.gaugeValue,\n        min: this.gaugeMin,\n        max: this.gaugeMax\n      })\n        .contentModifier(new MyGaugeStyle(30, 10, 100))\n\n      Column({ space: 20 }) {\n        Row({ space: 20 }) {\n          Button('增加').onClick(() => {\n            if (this.gaugeValue < this.gaugeMax) {\n              this.gaugeValue += 1\n            }\n          })\n          Button('减少').onClick(() => {\n            if (this.gaugeValue > this.gaugeMin) {\n              this.gaugeValue -= 1\n            }\n          })\n        }\n      }.width('100%')\n    }.width('100%').margin({ top: 5 })\n  }\n}"""
            """示例9:@Entry\n@Component\nstruct GaugeExample {\n  build() {\n    Scroll() {\n      Column({ space: 15 }) {\n        Row() {\n          // 创建一个仪表盘控件，显示数值为60，范围1-100\n          Gauge({ value: 50, min: 1, max: 100 }) {\n            Column() {\n              // 显示数值为60的文本\n              Text('60')\n                .maxFontSize("180sp")  // 设置最大字体大小\n                .minFontSize("160.0vp")  // 设置最小字体大小\n                .fontWeight(FontWeight.Medium)  // 设置字体粗细\n                .fontColor("#ff182431")  // 设置字体颜色\n                .width('40%')  // 设置宽度\n                .height('30%')  // 设置高度\n                .textAlign(TextAlign.Center)  // 设置文本对齐方式为居中\n                .margin({ top: '22.2%' })  // 设置外边距\n                .textOverflow({ overflow: TextOverflow.Ellipsis })  // 设置文本溢出处理方式\n                .maxLines(1)  // 设置最大行数为1\n            }.width('100%').height('100%')\n          }\n          // 设置仪表盘的起始角度和结束角度\n          .startAngle(225)\n          .endAngle(135)\n          // 设置仪表盘颜色为红色\n          .colors(Color.Red)\n          .width('80%')  // 设置宽度\n          .height('80%')  // 设置高度\n          .strokeWidth(18)  // 设置描边宽度\n          .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })  // 设置轨道阴影效果\n          .padding(18)  // 设置内边距\n          .privacySensitive(true)  // 设置为隐私敏感模式\n        }\n      }\n    }\n  }\n}\n```\n@Entry\n@Component\nstruct GaugeExample {\n  build() {\n    Scroll() {\n      Column({ space: 15 }) {\n        Row() {\n          Gauge({ value: 50, min: 1, max: 100 }) {\n            Column() {\n              Text('60')\n                .maxFontSize("180sp")\n                .minFontSize("160.0vp")\n                .fontWeight(FontWeight.Medium)\n                .fontColor("#ff182431")\n                .width('40%')\n                .height('30%')\n                .textAlign(TextAlign.Center)\n                .margin({ top: '22.2%' })\n                .textOverflow({ overflow: TextOverflow.Ellipsis })\n                .maxLines(1)\n            }.width('100%').height('100%')\n          }\n          .startAngle(225)\n          .endAngle(135)\n          .colors(Color.Red)\n          .width('80%')\n          .height('80%')\n          .strokeWidth(18)\n          .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n          .padding(18)\n          .privacySensitive(true)\n        }\n      }\n    }\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Image": {
        "description": "图片组件，常用于在应用中显示图片。Image支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。",
        "interfaces": [
            {
                "description": "通过图片数据源获取图片，用于后续渲染展示。",
                "params": {
                    "src": {
                        "type": ["PixelMap", "ResourceStr", "DrawableDescriptor"],
                        "required": True,
                        "description": "图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/arkts-graphics-display-V5#%E5%8A%A0%E8%BD%BD%E5%9B%BE%E7%89%87%E8%B5%84%E6%BA%90)。"
                    }
                }
            },
            {
                "description": "通过图片数据源获取图片，用于后续渲染展示。",
                "params": {
                    "src": {
                        "type": ["PixelMap", "ResourceStr", "DrawableDescriptor"],
                        "required": True,
                        "description": "图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/arkts-graphics-display-V5#%E5%8A%A0%E8%BD%BD%E5%9B%BE%E7%89%87%E8%B5%84%E6%BA%90)。"
                    },
                    "imageAIOptions": {
                        "type": "ImageAIOptions",
                        "required": True,
                        "description": "给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。"
                    }
                }
            }
        ],
        "attributes": {
            "alt": {
                "description": "设置图片加载时显示的占位图。",
                "params": {
                    "value": {
                        "type": ["string", "Resource", "PixelMap"],
                        "required": True,
                        "description": "加载时显示的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型）,支持PixelMap类型图片，不支持网络图片。"
                    }
                }
            },
            "objectFit": {
                "description": "设置图片的填充效果。",
                "params": {
                    "value": {
                        "type": "ImageFit",
                        "required": True,
                        "description": "图片的填充效果。",
                        "default": "ImageFit.Cover"
                    }
                }
            },
            "objectRepeat": {
                "description": "设置图片的重复样式，从中心点向两边重复，剩余空间不足放下一张图片时会截断。svg类型图源不支持该属性。",
                "params": {
                    "value": {
                        "type": "ImageRepeat",
                        "required": True,
                        "description": "图片的重复样式。",
                        "default": "ImageRepeat.NoRepeat"
                    }
                }
            },
            "interpolation": {
                "description": "设置图片的插值效果，即缓解图片在缩放时的锯齿问题。svg类型图源不支持该属性。",
                "params": {
                    "value": {
                        "type": "ImageInterpolation",
                        "required": True,
                        "description": "图片的插值效果。",
                        "default": "ImageInterpolation.None"
                    }
                }
            },
            "renderMode": {
                "description": "设置图片的渲染模式。svg类型图源不支持该属性。",
                "params": {
                    "value": {
                        "type": "ImageRenderMode",
                        "required": True,
                        "description": "图片的渲染模式为原色或黑白。",
                        "default": "ImageRenderMode.Original"
                    }
                }
            },
            "sourceSize": {
                "description": "设置图片解码尺寸。仅在目标尺寸小于图源尺寸时生效。svg类型图源和PixelMap资源不支持该属性。",
                "params": {
                    "value": {
                        "type": {
                            "width": "number",
                            "height": "number"
                        },
                        "required": True,
                        "description": "图片解码尺寸，降低图片的分辨率，常用于需要让图片显示尺寸比组件尺寸更小的场景。和ImageFit.None配合使用时可在组件内显示小图。"
                    }
                }
            },
            "matchTextDirection": {
                "description": "设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "图片是否跟随系统语言方向。",
                        "default": False
                    }
                }
            },
            "fitOriginalSize": {
                "description": "设置图片的显示尺寸是否跟随图源尺寸。图片组件尺寸未设置时，其显示尺寸是否跟随图源尺寸。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "图片的显示尺寸是否跟随图源尺寸",
                        "default": False
                    }
                }
            },
            "fillColor": {
                "description": "设置填充颜色，设置后填充颜色会覆盖在图片上。仅对svg图源生效，设置后会替换svg图片的填充颜色。如需对png图片进行修改颜色，可以使用colorFilter。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "填充颜色。"
                    }
                }
            },
            "autoResize": {
                "description": "设置图片解码过程中是否对图源自动缩放。降采样解码时图片的部分信息丢失，因此可能会导致图片质量的下降（如：出现锯齿），这时可以选择把autoResize设为false，按原图尺寸解码，提升显示效果，但会增加内存占用。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "图片解码过程中是否对图源自动缩放。",
                        "default": False
                    }
                }
            },
            "syncLoad": {
                "description": "设置是否同步加载图片。建议加载尺寸较小的本地图片时将syncLoad设为true，因为耗时较短，在主线程上执行即可。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。",
                        "default": False
                    }
                }
            },
            "copyOption": {
                "description": "设置图片是否可复制。当copyOption设置为非CopyOptions.None时，支持使用长按、鼠标右击、快捷组合键'CTRL+C'等方式进行复制。svg图片不支持复制。",
                "params": {
                    "value": {
                        "type": "CopyOptions",
                        "required": True,
                        "description": "图片是否可复制。",
                        "default": "CopyOptions.None"
                    }
                }
            },
            "colorFilter": {
                "description": "为图像设置颜色滤镜效果。",
                "params": {
                    "value": {
                        "type": ["ColorFilter", "DrawingColorFilter"],
                        "required": True,
                        "description": "给图像设置颜色滤镜效果，入参为一个的4x5的RGBA转换矩阵。"
                    }
                }
            },
            "draggable": {
                "description": "设置组件默认拖拽效果。不能和onDragStart事件同时使用。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "组件默认拖拽效果，设置为true时，组件可拖拽。",
                        "default": True
                    }
                }
            },
            "enableAnalyzer": {
                "description": "设置组件支持AI分析。不能和overlay属性同时使用，两者同时设置时overlay中CustomBuilder属性将失效。该特性依赖设备能力。",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "required": True,
                        "description": "组件支持AI分析，设置为true时，组件可进行AI分析。",
                        "default": False
                    }
                }
            },
            "resizable": {
                "description": "设置图像拉伸时可调整大小的图像选项。拉伸对拖拽缩略图以及占位图有效。",
                "params": {
                    "value": {
                        "type": "ResizableOptions",
                        "required": True,
                        "description": "图像拉伸时可调整大小的图像选项。"
                    }
                }
            },
            "privacySensitive": {
                "description": "设置是否支持卡片敏感隐私信息。",
                "params": {
                    "supported": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否支持卡片敏感隐私信息。",
                        "default": False
                    }
                }
            },
            "dynamicRangeMode": {
                "description": "设置期望展示的图像动态范围。",
                "params": {
                    "value": {
                        "type": "DynamicRangeMode",
                        "required": True,
                        "description": "期望展示的图像动态范围。"
                    }
                }
            }
        },
        "events": {
            "onComplete": {
                "description": "图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。",
                "params": {
                    "width": {
                        "type": "number",
                        "required": True,
                        "description": "图片的宽。单位：像素"
                    },
                    "height": {
                        "type": "number",
                        "required": True,
                        "description": "图片的高。单位：像素"
                    },
                    "componentWidth": {
                        "type": "number",
                        "required": True,
                        "description": "组件的宽。单位：像素"
                    },
                    "componentHeight": {
                        "type": "number",
                        "required": True,
                        "description": "组件的高。单位：像素"
                    },
                    "loadingStatus": {
                        "type": "number",
                        "required": True,
                        "description": "图片加载成功的状态值。返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。"
                    },
                    "contentWidth": {
                        "type": "number",
                        "required": True,
                        "description": "图片实际绘制的宽度。单位：像素。仅在loadingStatus返回1时有效。"
                    },
                    "contentHeight": {
                        "type": "number",
                        "required": True,
                        "description": "图片实际绘制的高度。单位：像素。仅在loadingStatus返回1时有效。"
                    },
                    "contentOffsetX": {
                        "type": "number",
                        "required": True,
                        "description": "实际绘制内容相对于组件自身的x轴偏移。单位：像素。仅在loadingStatus返回1时有效。"
                    },
                    "contentOffsetY": {
                        "type": "number",
                        "required": True,
                        "description": "实际绘制内容相对于组件自身的y轴偏移。单位：像素。仅在loadingStatus返回1时有效。"
                    }
                }
            },
            "onError": {
                "description": "图片加载异常时触发该回调。",
                "params": {
                    "componentWidth": {
                        "type": "number",
                        "required": True,
                        "description": "组件的宽。单位：像素"
                    },
                    "componentHeight": {
                        "type": "number",
                        "required": True,
                        "description": "组件的高。单位：像素"
                    },
                    "message": {
                        "type": "string",
                        "required": True,
                        "description": "报错信息。"
                    }
                }
            },
            "onFinish": {
                "description": "onFinish(event: () => void)当加载的源文件为带动效的svg格式图片时，svg动效播放完成时会触发这个回调。如果动效为无限循环动效，则不会触发这个回调。",
                "params": {}
            }
        },
        "examples": [
            """示例1:\n// 加载基本类型图片示例\n// 该示例展示了如何加载不同格式的图片，并添加覆盖效果\n\n@Entry\n@Component\nstruct ImageExample1 {\n  build() {\n    Column() {\n      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {\n        Row() {\n          // 加载png格式图片\n          Image($r('app.media.ic_camera_master_ai_leaf'))\n            .width(110).height(110).margin(15)\n            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n          // 加载gif格式图片\n          Image($r('app.media.loading'))\n            .width(110).height(110).margin(15)\n            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n        }\n        Row() {\n          // 加载svg格式图片\n          Image($r('app.media.ic_camera_master_ai_clouded'))\n            .width(110).height(110).margin(15)\n            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n          // 加载jpg格式图片\n          Image($r('app.media.ic_public_favor_filled'))\n            .width(110).height(110).margin(15)\n            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n        }\n      }\n    }.height(320).width(360).padding({ right: 10, top: 10 })\n  }\n}\n```\n\n**功能与效果描述：**\n- 该示例展示了如何在鸿蒙ArkUI中加载不同格式的图片，并为图片添加覆盖效果。\n- 第一个Row展示了加载png格式和gif格式的图片，分别展示了加载不同格式图片的方法。\n- 第二个Row展示了加载svg格式和jpg格式的图片，同样展示了加载不同格式图片的方法。\n- 每张图片设置了相同的宽度和高度为110，间距为15，并在底部添加了覆盖效果，偏移量为{ x: 0, y: 20 }。\n- 整体布局为一个高度为320，宽度为360的Column，内部包含两个Row，每个Row包含两张图片。\n\n**注释：**\n- `$r('app.media.ic_camera_master_ai_leaf')`：加载png格式图片的资源路径。\n- `$r('app.media.loading')`：加载gif格式图片的资源路径。\n- `$r('app.media.ic_camera_master_ai_clouded')`：加载svg格式图片的资源路径。\n- `$r('app.media.ic_public_favor_filled')`：加载jpg格式图片的资源路径。\n- `overlay`方法：用于添加覆盖效果，参数为覆盖效果类型和配置。\n- `width`、`height`、`margin`方法：分别设置图片的宽度、高度和外边距。\n- `alignItems`、`offset`：用于设置覆盖效果的对齐方式和偏移量。\n- `padding`方法：设置整体布局的内边距。\n```\n@Entry\n@Component\nstruct ImageExample1 {\n  build() {\n    Column() {\n      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {\n        Row() {\n          // 加载png格式图片\n          Image($r('app.media.ic_camera_master_ai_leaf'))\n            .width(110).height(110).margin(15)\n            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n          // 加载gif格式图片\n          Image($r('app.media.loading'))\n            .width(110).height(110).margin(15)\n            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n        }\n        Row() {\n          // 加载svg格式图片\n          Image($r('app.media.ic_camera_master_ai_clouded'))\n            .width(110).height(110).margin(15)\n            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n          // 加载jpg格式图片\n          Image($r('app.media.ic_public_favor_filled'))\n            .width(110).height(110).margin(15)\n            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n        }\n      }\n    }.height(320).width(360).padding({ right: 10, top: 10 })\n  }\n}"""
            """示例2:// 加载网络图片时，默认网络超时是5分钟，建议使用alt配置加载时的占位图。\n// 如果需要更灵活的网络配置，可以使用HTTP工具包发送网络请求，接着将返回的数据解码为Image组件中的PixelMap，图片开发可参考图片处理。\n// 使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考声明权限。\n\n@Entry\n@Component\nstruct ImageExample2 {\n  build() {\n    Column({ space: 10 }) {\n      // 直接加载网络地址，请填写一个具体的网络图片地址\n      Image("https://www.example.com/xxx.png")\n        // 使用alt，在网络图片加载成功前使用占位图\n        .alt($r('app.media.LoadingProgress'))\n        .width(375)\n        .height(300)\n    }\n  }\n}\n``` \n\n```java\n// 该示例代码展示了如何在ArkUI中加载网络图片并使用占位图进行展示。\n\n// 在Column布局中，创建一个Image组件用于加载网络图片。\n// 通过指定网络图片的URL地址："https://www.example.com/xxx.png"，实现加载网络图片的功能。\n\n// 使用.alt()方法配置加载时的占位图，即在网络图片加载成功前显示指定的占位图，提升用户体验。\n\n// 设置Image组件的宽度为375，高度为300，以适配展示区域的大小。\n\n// 开发者需要注意，加载网络图片时需要申请权限ohos.permission.INTERNET，具体申请方式可参考声明权限的相关文档。\n```  \n@Entry\n@Component\nstruct ImageExample2 {\n  build() {\n    Column({ space: 10 }) {\n      Image("https://www.example.com/xxx.png")// 直接加载网络地址，请填写一个具体的网络图片地址\n        .alt($r('app.media.LoadingProgress'))// 使用alt，在网络图片加载成功前使用占位图\n        .width(375)\n        .height(300)\n    }\n  }\n}"""
            """示例3:@Entry\n@Component\nstruct ImageExample3 {\n  private imageOne: Resource = $r('app.media.earth');\n  private imageTwo: Resource = $r('app.media.star');\n  private imageThree: Resource = $r('app.media.moveStar');\n  @State src: Resource = this.imageOne\n  @State src2: Resource = this.imageThree\n\n  build(){\n    Column(){\n      // 为图片添加点击事件，点击完成后加载特定图片\n      Image(this.src)\n        .width(100)\n        .height(100)\n        .onClick(() => {\n          this.src = this.imageTwo\n        })\n\n      // 当加载图片为SVG格式时\n      Image(this.src2)\n        .width(100)\n        .height(100)\n        .onClick(() => {\n          // SVG动效播放完成时加载另一张图片\n          this.src2 = this.imageOne\n        })\n    }.width('100%').height('100%')\n  }\n}\n```\n\n```java\n// 为图片添加点击事件，点击图片一时加载图片二，点击图片二时加载图片一\n// 点击第一张图片时，切换显示第二张图片；点击第二张图片时，切换显示第一张图片\n// 点击第一张图片时，切换显示第二张图片；点击第二张图片时，切换显示第一张图片\n// 当加载的图片为SVG格式时，点击图片播放SVG动效，播放完成后加载另一张图片\n// 当加载的图片为SVG格式时，点击图片播放SVG动效，播放完成后加载另一张图片\n// 图片一初始加载为地球图片，点击后切换为星球图片；图片二初始加载为移动星球图片，点击后切换为地球图片\n// 图片一初始加载为地球图片，点击后切换为星球图片；图片二初始加载为移动星球图片，点击后切换为地球图片\n```\n@Entry\n@Component\nstruct ImageExample3 {\n  private imageOne: Resource = $r('app.media.earth');\n  private imageTwo: Resource = $r('app.media.star');\n  private imageThree: Resource = $r('app.media.moveStar');\n  @State src: Resource = this.imageOne\n  @State src2: Resource = this.imageThree\n  build(){\n    Column(){\n      // 为图片添加点击事件，点击完成后加载特定图片\n      Image(this.src)\n        .width(100)\n        .height(100)\n        .onClick(() => {\n          this.src = this.imageTwo\n        })\n\n      // 当加载图片为SVG格式时\n      Image(this.src2)\n        .width(100)\n        .height(100)\n        .onClick(() => {\n          // SVG动效播放完成时加载另一张图片\n          this.src2 = this.imageOne\n        })\n    }.width('100%').height('100%')\n  }\n}"""
            """示例4:/**\n * 使用PixelMap开启图像分析功能\n * 1. 在该示例中，通过PixelMap开启图像分析功能，展示图像分析结果。\n * 2. 通过按钮触发获取图像分析支持类型的操作。\n */\n\nimport { image } from '@kit.ImageKit'\n\n@Entry\n@Component\nstruct ImageExample4 {\n  @State imagePixelMap: image.PixelMap | undefined = undefined // 存储图像的PixelMap对象\n  private aiController: ImageAnalyzerController = new ImageAnalyzerController() // 创建图像分析控制器\n  private options: ImageAIOptions = {\n    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT], // 设置图像分析类型为主体和文本\n    aiController: this.aiController\n  }\n\n  async aboutToAppear() {\n    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.app_icon')) // 从媒体资源获取PixelMap对象\n  }\n\n  build() {\n    Column() {\n      Image(this.imagePixelMap, this.options) // 显示图像并设置图像分析选项\n        .enableAnalyzer(true) // 启用图像分析功能\n        .width(200) // 设置图像显示宽度\n        .height(200) // 设置图像显示高度\n        .margin({bottom:10}) // 设置图像底部边距\n      Button('getTypes') // 创建获取支持类型的按钮\n        .width(80) // 设置按钮宽度\n        .height(80) // 设置按钮高度\n        .onClick(() => {\n          this.aiController.getImageAnalyzerSupportTypes() // 点击按钮获取图像分析支持类型\n        })\n    }\n  }\n\n  /**\n   * 从媒体资源获取PixelMap对象\n   * @param resource - 资源对象\n   * @returns Promise<image.PixelMap> - 返回获取的PixelMap对象\n   */\n  private async getPixmapFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    })\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength))\n    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    })\n    await imageSource.release()\n    return createPixelMap\n  }\n}\n```\nimport { image } from '@kit.ImageKit'\n\n@Entry\n@Component\nstruct ImageExample4 {\n  @State imagePixelMap: image.PixelMap | undefined = undefined\n  private aiController: ImageAnalyzerController = new ImageAnalyzerController()\n  private options: ImageAIOptions = {\n    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],\n    aiController: this.aiController\n  }\n\n  async aboutToAppear() {\n    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.app_icon'))\n  }\n\n  build() {\n    Column() {\n      Image(this.imagePixelMap, this.options)\n        .enableAnalyzer(true)\n        .width(200)\n        .height(200)\n        .margin({bottom:10})\n      Button('getTypes')\n        .width(80)\n        .height(80)\n        .onClick(() => {\n          this.aiController.getImageAnalyzerSupportTypes()\n        })\n    }\n  }\n  private async getPixmapFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    })\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength))\n    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    })\n    await imageSource.release()\n    return createPixelMap\n  }\n}"""
            """示例5:@Entry\n@Component\nstruct Index {\n  @State top: number = 40 // 定义顶部拉伸量，默认为40\n  @State bottom: number = 5 // 定义底部拉伸量，默认为5\n  @State left: number = 40 // 定义左侧拉伸量，默认为40\n  @State right: number = 10 // 定义右侧拉伸量，默认为10\n\n  build() {\n    Column({ space: 5 }) {\n      // 原图效果\n      Image($r("app.media.sky"))\n        .width(200).height(200)\n        .border({ width: 2, color: Color.Pink })\n        .objectFit(ImageFit.Contain) // 图片填充方式为Contain，保持比例拉伸\n\n      // 图像拉伸效果，设置resizable属性，对图片不同方向进行拉伸\n      Image($r("app.media.sky"))\n        .resizable({\n          slice: {\n            left: this.left,\n            right: this.right,\n            top: this.top,\n            bottom: this.bottom\n          }\n        })\n        .width(200)\n        .height(200)\n        .border({ width: 2, color: Color.Pink })\n        .objectFit(ImageFit.Contain) // 图片填充方式为Contain，保持比例拉伸\n\n      Row() {\n        Button("add top to " + this.top).fontSize(10)\n          .onClick(() => {\n            this.top += 2 // 点击按钮增加顶部拉伸量\n          })\n        Button("add bottom to " + this.bottom).fontSize(10)\n          .onClick(() => {\n            this.bottom += 2 // 点击按钮增加底部拉伸量\n          })\n      }\n\n      Row() {\n        Button("add left to " + this.left).fontSize(10)\n          .onClick(() => {\n            this.left += 2 // 点击按钮增加左侧拉伸量\n          })\n        Button("add right to " + this.right).fontSize(10)\n          .onClick(() => {\n            this.right += 2 // 点击按钮增加右侧拉伸量\n          })\n      }\n\n    }\n    .justifyContent(FlexAlign.Start).width('100%').height('100%') // 设置布局属性\n  }\n}\n```\n@Entry\n@Component\nstruct Index {\n  @State top: number = 40\n  @State bottom: number = 5\n  @State left: number = 40\n  @State right: number = 10\n\n  build() {\n    Column({ space: 5 }) {\n      // 原图效果\n      Image($r("app.media.sky"))\n        .width(200).height(200)\n        .border({ width: 2, color: Color.Pink })\n        .objectFit(ImageFit.Contain)\n\n      // 图像拉伸效果，设置resizable属性，对图片不同方向进行拉伸\n      Image($r("app.media.sky"))\n        .resizable({\n          slice: {\n            left: this.left,\n            right: this.right,\n            top: this.top,\n            bottom: this.bottom\n          }\n        })\n        .width(200)\n        .height(200)\n        .border({ width: 2, color: Color.Pink })\n        .objectFit(ImageFit.Contain)\n\n      Row() {\n        Button("add top to " + this.top).fontSize(10)\n          .onClick(() => {\n            this.top += 2\n          })\n        Button("add bottom to " + this.bottom).fontSize(10)\n          .onClick(() => {\n            this.bottom += 2\n          })\n      }\n\n      Row() {\n        Button("add left to " + this.left).fontSize(10)\n          .onClick(() => {\n            this.left += 2\n          })\n        Button("add right to " + this.right).fontSize(10)\n          .onClick(() => {\n            this.right += 2\n          })\n      }\n\n    }\n    .justifyContent(FlexAlign.Start).width('100%').height('100%')\n  }\n}"""
            """示例6:/**\n * 该示例代码实现了播放PixelMap数组动画的功能，包括设置动画的时长和循环次数，以及通过按钮控制动画播放方式。\n */\n\nimport { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';\nimport { image } from '@kit.ImageKit';\n\n@Entry\n@Component\nstruct ImageExample {\n  pixelmaps: Array<PixelMap> = []; // 存储PixelMap数组\n  options: AnimationOptions = { duration: 2000, iterations: 1 }; // 动画选项，包括时长和循环次数\n  @State animated: AnimatedDrawableDescriptor | undefined = undefined; // 动画描述符\n\n  /**\n   * 在组件即将显示时，获取PixelMaps并创建动画描述符\n   */\n  async aboutToAppear() {\n    this.pixelmaps = await this.getPixelMaps();\n    this.animated = new AnimatedDrawableDescriptor(this.pixelmaps, this.options);\n  }\n\n  /**\n   * 构建UI界面，包括显示动画和控制按钮\n   */\n  build() {\n    Column() {\n      Row() {\n        Image(this.animated)\n          .width('500px').height('500px')\n          .onFinish(() => {\n            console.info("finish");\n          });\n      }.height('50%');\n      Row() {\n        Button('once').width(100).padding(5).onClick(() => {\n          this.options = { duration: 2000, iterations: 1 };\n          this.animated = new AnimatedDrawableDescriptor(this.pixelmaps, this.options);\n        }).margin(5);\n        Button('infinite').width(100).padding(5).onClick(() => {\n          this.options = { duration: 2000, iterations: -1 };\n          this.animated = new AnimatedDrawableDescriptor(this.pixelmaps, this.options);\n        }).margin(5);\n      }\n    }.width('50%');\n  }\n\n  /**\n   * 从资源中获取PixelMap列表\n   * @param resource 资源对象\n   * @returns PixelMap数组\n   */\n  private async getPixmapListFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    });\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength));\n    let createPixelMap: Array<image.PixelMap> = await imageSource.createPixelMapList({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    });\n    await imageSource.release();\n    return createPixelMap;\n  }\n\n  /**\n   * 从资源中获取单个PixelMap\n   * @param resource 资源对象\n   * @returns 单个PixelMap\n   */\n  private async getPixmapFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    });\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength));\n    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    });\n    await imageSource.release();\n    return createPixelMap;\n  }\n\n  /**\n   * 获取所有PixelMaps，包括列表和单个PixelMap\n   * @returns PixelMap数组\n   */\n  private async getPixelMaps() {\n    let Mypixelmaps: Array<PixelMap> = await this.getPixmapListFromMedia($r('app.media.view')); // 获取PixelMap列表\n    Mypixelmaps.push(await this.getPixmapFromMedia($r('app.media.icon'))); // 添加单个PixelMap\n    return Mypixelmaps;\n  }\n}\n```\nimport {AnimationOptions, AnimatedDrawableDescriptor} from '@kit.ArkUI'\nimport { image } from '@kit.ImageKit'\n\n@Entry\n@Component\nstruct ImageExample {\n  pixelmaps: Array<PixelMap>  = [];\n  options: AnimationOptions = {duration:2000, iterations:1};\n  @State animated: AnimatedDrawableDescriptor | undefined = undefined;\n\n  async aboutToAppear() {\n    this.pixelmaps = await this.getPixelMaps();\n    this.animated = new AnimatedDrawableDescriptor(this.pixelmaps, this.options);\n  }\n\n  build() {\n    Column() {\n      Row() {\n        Image(this.animated)\n          .width('500px').height('500px')\n          .onFinish(() => {\n            console.info("finish")\n          })\n      }.height('50%')\n      Row() {\n        Button('once').width(100).padding(5).onClick(() => {\n          this.options = {duration:2000, iterations:1};\n          this.animated = new AnimatedDrawableDescriptor(this.pixelmaps, this.options);\n        }).margin(5)\n        Button('infinite').width(100).padding(5).onClick(() => {\n          this.options = {duration:2000, iterations:-1};\n          this.animated = new AnimatedDrawableDescriptor(this.pixelmaps, this.options);\n        }).margin(5)\n      }\n    }.width('50%')\n  }\n\n  private async getPixmapListFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    })\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength))\n    let createPixelMap: Array<image.PixelMap> = await imageSource.createPixelMapList({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    })\n    await imageSource.release()\n    return createPixelMap\n  }\n\n  private async getPixmapFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    })\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength))\n    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    })\n    await imageSource.release()\n    return createPixelMap\n  }\n\n  private async getPixelMaps() {\n    let Mypixelmaps:Array<PixelMap> = await this.getPixmapListFromMedia($r('app.media.view'))//gif图, 生成多张PixelMap\n    Mypixelmaps.push(await this.getPixmapFromMedia($r('app.media.icon'))) //添加一张图片\n    return Mypixelmaps;\n  }\n}"""
            """示例7:// 该示例实现了给图像设置颜色滤镜效果\n\nimport { drawing, common2D } from '@kit.ArkGraphics2D';\n\n@Entry\n@Component\nstruct ImageExample3 {\n  private imageOne: Resource = $r('app.media.1'); // 定义第一张图片资源\n  private imageTwo: Resource = $r('app.media.2'); // 定义第二张图片资源\n  @State src: Resource = this.imageOne // 设置第一张图片为初始显示图片\n  @State src2: Resource = this.imageTwo // 设置第二张图片为初始显示图片\n  private ColorFilterMatrix: number[] = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]; // 颜色滤镜矩阵\n  private color: common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 }; // 定义颜色对象\n  @State DrawingColorFilterFirst: ColorFilter | undefined = undefined // 第一张图片的颜色滤镜\n  @State DrawingColorFilterSecond: ColorFilter | undefined = undefined // 第二张图片的颜色滤镜\n  @State DrawingColorFilterThird: ColorFilter | undefined = undefined // 第三张图片的颜色滤镜\n\n  build() {\n    Column() {\n      // 第一张图片\n      Image(this.src)\n        .width(100)\n        .height(100)\n        .colorFilter(this.DrawingColorFilterFirst) // 设置颜色滤镜\n        .onClick(()=>{\n          this.DrawingColorFilterFirst = drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN); // 点击后应用颜色混合滤镜\n        })\n\n      // 第二张图片\n      Image(this.src2)\n        .width(100)\n        .height(100)\n        .colorFilter(this.DrawingColorFilterSecond) // 设置颜色滤镜\n        .onClick(()=>{\n          this.DrawingColorFilterSecond = new ColorFilter(this.ColorFilterMatrix); // 点击后应用自定义颜色滤镜矩阵\n        })\n\n      // 加载SVG格式图片\n      Image($r('app.media.test_self'))\n        .width(110).height(110).margin(15)\n        .colorFilter(this.DrawingColorFilterThird) // 设置颜色滤镜\n        .onClick(()=>{\n          this.DrawingColorFilterThird = drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN); // 点击后应用颜色混合滤镜\n        })\n    }\n  }\n}\n```\nimport { drawing, common2D } from '@kit.ArkGraphics2D';\n\n@Entry\n@Component\nstruct ImageExample3 {\n  private imageOne: Resource = $r('app.media.1');\n  private imageTwo: Resource = $r('app.media.2');\n  @State src: Resource = this.imageOne\n  @State src2: Resource = this.imageTwo\n  private ColorFilterMatrix: number[] = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]\n  private color: common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };\n  @State DrawingColorFilterFirst: ColorFilter | undefined = undefined\n  @State DrawingColorFilterSecond: ColorFilter | undefined = undefined\n  @State DrawingColorFilterThird: ColorFilter | undefined = undefined\n\n  build() {\n    Column() {\n      Image(this.src)\n        .width(100)\n        .height(100)\n        .colorFilter(this.DrawingColorFilterFirst)\n        .onClick(()=>{\n          this.DrawingColorFilterFirst = drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN);\n        })\n\n      Image(this.src2)\n        .width(100)\n        .height(100)\n        .colorFilter(this.DrawingColorFilterSecond)\n        .onClick(()=>{\n          this.DrawingColorFilterSecond = new ColorFilter(this.ColorFilterMatrix);\n        })\n\n      //当加载图片为SVG格式时\n      Image($r('app.media.test_self'))\n        .width(110).height(110).margin(15)\n        .colorFilter(this.DrawingColorFilterThird)\n        .onClick(()=>{\n          this.DrawingColorFilterThird = drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN);\n        })\n    }\n  }\n}"""
            """示例8:@Entry\n@Component\nstruct ImageExample {\n    build() {\n        Column() {\n            Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {\n                Row() {\n                    // 加载png格式图片，设置objectFit效果为TOP_START\n                    Image($r('app.media.sky'))\n                        .width(110).height(110).margin(15)\n                        .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n                        .border({ width: 2, color: Color.Pink })\n                        .objectFit(ImageFit.TOP_START)\n                    // 加载gif格式图片，设置objectFit效果为BOTTOM_START\n                    Image($r('app.media.loading'))\n                        .width(110).height(110).margin(15)\n                        .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n                        .border({ width: 2, color: Color.Pink })\n                        .objectFit(ImageFit.BOTTOM_START)\n                }\n                Row() {\n                    // 加载svg格式图片，设置objectFit效果为TOP_END\n                    Image($r('app.media.svg'))\n                        .width(110).height(110).margin(15)\n                        .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n                        .border({ width: 2, color: Color.Pink })\n                        .objectFit(ImageFit.TOP_END)\n                    // 加载jpg格式图片，设置objectFit效果为CENTER\n                    Image($r('app.media.jpg'))\n                        .width(110).height(110).margin(15)\n                        .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n                        .border({ width: 2, color: Color.Pink })\n                        .objectFit(ImageFit.CENTER)\n                }\n            }\n        }.height(320).width(360).padding({ right: 10, top: 10 })\n    }\n}\n```\n\n```plaintext\n// 功能与效果描述：\n// - 该示例代码展示了如何给不同格式的图片设置不同的objectFit效果。\n// - 每个Image组件加载不同格式的图片，并设置了不同的objectFit属性。\n// - objectFit属性决定了图片在容器中的展示方式，如填充、拉伸等。\n// - 每个Image组件还设置了边框、大小、边距等样式属性，以及覆盖层的相关配置。\n\n// 注释：\n// - 第一个Row中加载了png格式的图片，并设置了objectFit为TOP_START，展示在容器的顶部左侧。\n// - 第一个Row中加载了gif格式的图片，并设置了objectFit为BOTTOM_START，展示在容器的底部左侧。\n// - 第二个Row中加载了svg格式的图片，并设置了objectFit为TOP_END，展示在容器的顶部右侧。\n// - 第二个Row中加载了jpg格式的图片，并设置了objectFit为CENTER，展示在容器的中心位置。\n// - 每个Image组件都设置了固定的宽度、高度和边距，以及边框样式和覆盖层的配置。\n// - 整体布局为Column内嵌套Flex，展示了不同图片格式的objectFit效果。\n```\n@Entry\n@Component\nstruct ImageExample{\n  build() {\n    Column() {\n      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {\n        Row() {\n          // 加载png格式图片\n          Image($r('app.media.sky'))\n            .width(110).height(110).margin(15)\n            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n            .border({ width: 2, color: Color.Pink })\n            .objectFit(ImageFit.TOP_START)\n          // 加载gif格式图片\n          Image($r('app.media.loading'))\n            .width(110).height(110).margin(15)\n            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n            .border({ width: 2, color: Color.Pink })\n            .objectFit(ImageFit.BOTTOM_START)\n        }\n        Row() {\n          // 加载svg格式图片\n          Image($r('app.media.svg'))\n            .width(110).height(110).margin(15)\n            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n            .border({ width: 2, color: Color.Pink })\n            .objectFit(ImageFit.TOP_END)\n          // 加载jpg格式图片\n          Image($r('app.media.jpg'))\n            .width(110).height(110).margin(15)\n            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })\n            .border({ width: 2, color: Color.Pink })\n            .objectFit(ImageFit.CENTER)\n        }\n      }\n    }.height(320).width(360).padding({ right: 10, top: 10 })\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "ImageAnimator": {
        "description": "提供帧动画组件来实现逐帧播放图片的能力，可以配置需要播放的图片列表，每张图片可以配置时长。",
        "interfaces": [
            {
                "description": "ImageAnimator()创建帧动画组件。",
                "params": {}
            }
        ],
        "attributes": {
            "images": {
                "description": "设置图片帧信息集合。不支持动态更新。",
                "params": {
                    "value": {
                        "type": "Array<ImageFrameInfo>",
                        "required": True,
                        "description": "设置图片帧信息集合。每一帧的帧信息(ImageFrameInfo)包含图片路径、图片大小、图片位置和图片播放时长信息，详见ImageFrameInfo属性说明。",
                        "default": []
                    }
                }
            },
            "state": {
                "description": "控制播放状态。",
                "params": {
                    "value": {
                        "type": "AnimationStatus",
                        "required": True,
                        "description": "默认为初始状态，用于控制播放状态。",
                        "default": "AnimationStatus.Initial"
                    }
                }
            },
            "duration": {
                "description": "设置播放时长。当Images中任意一帧图片设置了单独的duration后，该属性设置无效。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "播放时长。value为0时，不播放图片。value的改变只会在下一次循环开始时生效。单位：毫秒",
                        "default": 1000
                    }
                }
            },
            "reverse": {
                "description": "设置播放方向。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "播放方向。false表示从第1张图片播放到最后1张图片，true表示从最后1张图片播放到第1张图片。",
                        "default": False
                    }
                }
            },
            "fixedSize": {
                "description": "设置图片大小是否固定为组件大小。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "设置图片大小是否固定为组件大小。true表示图片大小与组件大小一致，此时设置图片的width 、height 、top 和left属性是无效的。false表示每一张图片的width 、height 、top和left属性都要单独设置。",
                        "default": True
                    }
                }
            },
            "fillMode": {
                "description": "设置当前播放方向下，动画开始前和结束后的状态。动画结束后的状态由fillMode和reverse属性共同决定。",
                "params": {
                    "value": {
                        "type": "FillMode",
                        "required": True,
                        "description": "当前播放方向下，动画开始前和结束后的状态。",
                        "default": "FillMode.Forwards"
                    }
                }
            },
            "iterations": {
                "description": "设置播放次数。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "默认播放一次，设置为-1时表示无限次播放。",
                        "default": 1
                    }
                }
            }
        },
        "events": {
            "onStart": {
                "description": "状态回调，动画开始播放时触发。",
                "params": {}
            },
            "onPause": {
                "description": "状态回调，动画暂停播放时触发。",
                "params": {}
            },
            "onRepeat": {
                "description": "状态回调，动画重复播放时触发。",
                "params": {}
            },
            "onCancel": {
                "description": "状态回调，动画返回最初状态时触发。",
                "params": {}
            },
            "onFinish": {
                "description": "状态回调，动画播放完成时或者停止播放时触发。",
                "params": {}
            }
        },
        "examples": [
            """示例1:// ImageAnimatorExample.ets\n\n/**\n * This component demonstrates the usage of ImageAnimator to create an animation with multiple images.\n * It allows controlling the animation state, reverse playback, iteration count, and provides callbacks for different animation events.\n */\n\n@Entry\n@Component\nstruct ImageAnimatorExample {\n  @State state: AnimationStatus = AnimationStatus.Initial // Represents the current animation state\n  @State reverse: boolean = false // Indicates if the animation should play in reverse\n  @State iterations: number = 1 // Number of times the animation should repeat (-1 for infinite loop)\n\n  build() {\n    Column({ space: 10 }) {\n      // Setting up ImageAnimator with multiple images and animation properties\n      ImageAnimator()\n        .images([\n          { src: $r('app.media.img1') },\n          { src: $r('app.media.img2') },\n          { src: $r('app.media.img3') },\n          { src: $r('app.media.img4') }\n        ])\n        .duration(2000)\n        .state(this.state).reverse(this.reverse)\n        .fillMode(FillMode.None).iterations(this.iterations).width(340).height(240)\n        .margin({ top: 100 })\n        .onStart(() => {\n          console.info('Start') // Callback when the animation starts\n        })\n        .onPause(() => {\n          console.info('Pause') // Callback when the animation is paused\n        })\n        .onRepeat(() => {\n          console.info('Repeat') // Callback when the animation repeats\n        })\n        .onCancel(() => {\n          console.info('Cancel') // Callback when the animation is canceled\n        })\n        .onFinish(() => {\n          console.info('Finish') // Callback when the animation finishes\n          this.state = AnimationStatus.Stopped // Update the animation state to Stopped\n        })\n\n      // Buttons for controlling the animation\n      Row() {\n        Button('start').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Running // Start the animation\n        }).margin(5)\n        Button('pause').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Paused // Pause the animation\n        }).margin(5)\n        Button('stop').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Stopped // Stop the animation\n        }).margin(5)\n      }\n\n      // Buttons for additional animation control\n      Row() {\n        Button('reverse').width(100).padding(5).onClick(() => {\n          this.reverse = !this.reverse // Toggle the reverse playback\n        }).margin(5)\n        Button('once').width(100).padding(5).onClick(() => {\n          this.iterations = 1 // Set the animation to play once\n        }).margin(5)\n        Button('infinite').width(100).padding(5).onClick(() => {\n          this.iterations = -1 // Set the animation to loop infinitely\n        }).margin(5)\n      }\n    }.width('100%').height('100%')\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct ImageAnimatorExample {\n  @State state: AnimationStatus = AnimationStatus.Initial\n  @State reverse: boolean = false\n  @State iterations: number = 1\n\n  build() {\n    Column({ space: 10 }) {\n      ImageAnimator()\n        .images([\n          {\n            src: $r('app.media.img1')\n          },\n          {\n            src: $r('app.media.img2')\n          },\n          {\n            src: $r('app.media.img3')\n          },\n          {\n            src: $r('app.media.img4')\n          }\n        ])\n        .duration(2000)\n        .state(this.state).reverse(this.reverse)\n        .fillMode(FillMode.None).iterations(this.iterations).width(340).height(240)\n        .margin({ top: 100 })\n        .onStart(() => {\n          console.info('Start')\n        })\n        .onPause(() => {\n          console.info('Pause')\n        })\n        .onRepeat(() => {\n          console.info('Repeat')\n        })\n        .onCancel(() => {\n          console.info('Cancel')\n        })\n        .onFinish(() => {\n          console.info('Finish')\n          this.state = AnimationStatus.Stopped\n        })\n      Row() {\n        Button('start').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Running\n        }).margin(5)\n        Button('pause').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Paused     // 显示当前帧图片\n        }).margin(5)\n        Button('stop').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Stopped    // 显示动画的起始帧图片\n        }).margin(5)\n      }\n\n      Row() {\n        Button('reverse').width(100).padding(5).onClick(() => {\n          this.reverse = !this.reverse\n        }).margin(5)\n        Button('once').width(100).padding(5).onClick(() => {\n          this.iterations = 1\n        }).margin(5)\n        Button('infinite').width(100).padding(5).onClick(() => {\n          this.iterations = -1 // 无限循环播放\n        }).margin(5)\n      }\n    }.width('100%').height('100%')\n  }\n}"""
            """示例2:import { image } from '@kit.ImageKit'\n\n@Entry\n@Component\nstruct ImageAnimatorExample {\n  imagePixelMap: Array<PixelMap> = [] // 存储图片像素信息的数组\n  @State state: AnimationStatus = AnimationStatus.Initial // 动画状态，默认为初始状态\n  @State reverse: boolean = false // 是否反向播放动画\n  @State iterations: number = 1 // 动画循环次数，默认为1次\n  @State images:Array<ImageFrameInfo> = [] // 存储图片帧信息的数组\n\n  async aboutToAppear() {\n    // 异步加载图片像素信息\n    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.icon')))\n    this.images.push({src:this.imagePixelMap[0]}) // 将图片像素信息添加到帧信息数组中\n  }\n\n  build() {\n    Column({ space: 10 }) {\n      // 创建图片动画组件\n      ImageAnimator()\n        .images(this.images) // 设置动画帧信息\n        .duration(2000) // 设置动画持续时间为2秒\n        .state(this.state).reverse(this.reverse) // 设置动画状态和是否反向播放\n        .fillMode(FillMode.None).iterations(this.iterations).width(340).height(240) // 设置填充模式、循环次数、宽度和高度\n        .margin({ top: 100 }) // 设置边距\n        .onStart(() => {\n          console.info('Start') // 动画开始时的回调\n        })\n        .onPause(() => {\n          console.info('Pause') // 动画暂停时的回调\n        })\n        .onRepeat(() => {\n          console.info('Repeat') // 动画重复播放时的回调\n        })\n        .onCancel(() => {\n          console.info('Cancel') // 动画取消时的回调\n        })\n        .onFinish(() => {\n          console.info('Finish') // 动画结束时的回调\n          this.state = AnimationStatus.Stopped // 将动画状态设置为停止\n        })\n\n      Row() {\n        // 开始、暂停、停止按钮\n        Button('start').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Running // 开始播放动画\n        }).margin(5)\n        Button('pause').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Paused // 暂停动画\n        }).margin(5)\n        Button('stop').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Stopped // 停止动画\n        }).margin(5)\n      }\n\n      Row() {\n        // 反向播放、单次循环、无限循环按钮\n        Button('reverse').width(100).padding(5).onClick(() => {\n          this.reverse = !this.reverse // 切换反向播放状态\n        }).margin(5)\n        Button('once').width(100).padding(5).onClick(() => {\n          this.iterations = 1 // 设置为单次循环\n        }).margin(5)\n        Button('infinite').width(100).padding(5).onClick(() => {\n          this.iterations = -1 // 设置为无限循环播放\n        }).margin(5)\n      }\n    }.width('100%').height('100%') // 设置容器宽度和高度\n  }\n\n  private async getPixmapFromMedia(resource: Resource) {\n    // 从媒体资源获取像素信息\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    })\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength))\n    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    })\n    await imageSource.release()\n    return createPixelMap\n  }\n}\n```\nimport { image } from '@kit.ImageKit'\n\n@Entry\n@Component\nstruct ImageAnimatorExample {\n  imagePixelMap: Array<PixelMap> = []\n  @State state: AnimationStatus = AnimationStatus.Initial\n  @State reverse: boolean = false\n  @State iterations: number = 1\n  @State images:Array<ImageFrameInfo> = []\n  async aboutToAppear() {\n    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.icon')))\n    this.images.push({src:this.imagePixelMap[0]})\n  }\n  build() {\n    Column({ space: 10 }) {\n      ImageAnimator()\n        .images(this.images)\n        .duration(2000)\n        .state(this.state).reverse(this.reverse)\n        .fillMode(FillMode.None).iterations(this.iterations).width(340).height(240)\n        .margin({ top: 100 })\n        .onStart(() => {\n          console.info('Start')\n        })\n        .onPause(() => {\n          console.info('Pause')\n        })\n        .onRepeat(() => {\n          console.info('Repeat')\n        })\n        .onCancel(() => {\n          console.info('Cancel')\n        })\n        .onFinish(() => {\n          console.info('Finish')\n          this.state = AnimationStatus.Stopped\n        })\n      Row() {\n        Button('start').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Running\n        }).margin(5)\n        Button('pause').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Paused     // 显示当前帧图片\n        }).margin(5)\n        Button('stop').width(100).padding(5).onClick(() => {\n          this.state = AnimationStatus.Stopped    // 显示动画的起始帧图片\n        }).margin(5)\n      }\n      Row() {\n        Button('reverse').width(100).padding(5).onClick(() => {\n          this.reverse = !this.reverse\n        }).margin(5)\n        Button('once').width(100).padding(5).onClick(() => {\n          this.iterations = 1\n        }).margin(5)\n        Button('infinite').width(100).padding(5).onClick(() => {\n          this.iterations = -1 // 无限循环播放\n        }).margin(5)\n      }\n    }.width('100%').height('100%')\n  }\n\n  private async getPixmapFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    })\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength))\n    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    })\n    await imageSource.release()\n    return createPixelMap\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "ImageSpan": {
        "description": "Text、ContainerSpan组件的子组件，用于显示行内图片。",
        "interfaces": [
            {
                "description": "创建ImageSpan组件。",
                "params": {
                    "value": {
                        "type": ["ResourceStr", "PixelMap"],
                        "required": True,
                        "description": "图片的数据源，支持本地图片和网络图片。当使用相对路径引用图片资源时，例如ImageSpan(\"common/test.jpg\")，不支持跨包/跨模块调用该ImageSpan组件，建议使用$r方式来管理需全局使用的图片资源。支持的图片格式包括png、jpg、bmp、svg、gif和heif。支持Base64字符串。格式data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data], 其中[base64 data]为Base64字符串数据。支持file:///data/storage路径前缀的字符串，用于读取本应用安装目录下files文件夹下的图片资源。需要保证目录包路径下的文件有可读权限。"
                    }
                }
            }
        ],
        "attributes": {
            "alt": {
                "description": "设置图片加载时显示的占位图。",
                "params": {
                    "value": {
                        "type": "PixelMap",
                        "required": True,
                        "description": "图片加载时显示的占位图。"
                    }
                }
            },
            "verticalAlign": {
                "description": "设置图片基于文本的对齐方式。",
                "params": {
                    "value": {
                        "type": "ImageSpanAlignment",
                        "required": True,
                        "description": "图片基于文本的对齐方式。"
                    }
                }
            },
            "objectFit": {
                "description": "设置图片的缩放类型。",
                "params": {
                    "value": {
                        "type": "ImageFit",
                        "required": True,
                        "description": "图片的缩放类型。",
                        "default": "ImageFit.Cover"
                    }
                }
            }
        },
        "events": {
            "onComplete": {
                "description": "图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。",
                "params": {
                    "callback": {
                        "type": "ImageCompleteCallback",
                        "required": True,
                        "description": "图片数据加载成功和解码成功时触发的回调。"
                    }
                }
            },
            "onError": {
                "description": "图片加载异常时触发该回调。",
                "params": {
                    "callback": {
                        "type": "ImageErrorCallback",
                        "required": True,
                        "description": "图片加载异常时触发的回调。"
                    }
                }
            }
        },
        "examples": [
            """示例1:// SpanExample.ets该示例实现了设置ImageSpan的基本属性和图片基于文本的对齐方式。\n\n// 创建一个包含Span和ImageSpan组件的示例，展示不同的文本装饰效果和图片排列方式\n@Entry\n@Component\nstruct SpanExample {\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\n      // 第一个Text组件包含一个Span文本，展示文本的装饰效果\n      Text() {\n        Span('This is the Span and ImageSpan component').fontSize(25).textCase(TextCase.Normal)\n          .decoration({ type: TextDecorationType.None, color: Color.Pink })\n      }.width('100%').textAlign(TextAlign.Center)\n\n      // 第二个Text组件展示不同的ImageSpan和Span组合效果\n      Text() {\n        // 第一个ImageSpan展示图片并设置宽高和填充方式\n        ImageSpan($r('app.media.icon'))\n          .width('200px')\n          .height('200px')\n          .objectFit(ImageFit.Fill)\n          .verticalAlign(ImageSpanAlignment.CENTER)\n        // 第一个Span展示带有删除线的文本\n        Span('I am LineThrough-span')\n          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red }).fontSize(25)\n        // 第二个ImageSpan展示图片并设置垂直对齐方式\n        ImageSpan($r('app.media.icon'))\n          .width('50px')\n          .height('50px')\n          .verticalAlign(ImageSpanAlignment.TOP)\n        // 第二个Span展示带有下划线的文本\n        Span('I am Underline-span')\n          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)\n        // 第三个ImageSpan展示图片并设置尺寸和垂直对齐方式\n        ImageSpan($r('app.media.icon'))\n          .size({ width: '100px', height: '100px' })\n          .verticalAlign(ImageSpanAlignment.BASELINE)\n        // 第三个Span展示带有下划线的文本\n        Span('I am Underline-span')\n          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)\n        // 第四个ImageSpan展示图片并设置宽高和垂直对齐方式\n        ImageSpan($r('app.media.icon'))\n          .width('70px')\n          .height('70px')\n          .verticalAlign(ImageSpanAlignment.BOTTOM)\n        // 第四个Span展示带有下划线的文本，字体大小更大\n        Span('I am Underline-span')\n          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(50)\n      }\n      .width('100%')\n      .textIndent(50)\n    }.width('100%').height('100%').padding({ left: 0, right: 0, top: 0 })\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct SpanExample {\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\n      Text() {\n        Span('This is the Span and ImageSpan component').fontSize(25).textCase(TextCase.Normal)\n          .decoration({ type: TextDecorationType.None, color: Color.Pink })\n      }.width('100%').textAlign(TextAlign.Center)\n\n      Text() {\n        ImageSpan($r('app.media.icon'))\n          .width('200px')\n          .height('200px')\n          .objectFit(ImageFit.Fill)\n          .verticalAlign(ImageSpanAlignment.CENTER)\n        Span('I am LineThrough-span')\n          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red }).fontSize(25)\n        ImageSpan($r('app.media.icon'))\n          .width('50px')\n          .height('50px')\n          .verticalAlign(ImageSpanAlignment.TOP)\n        Span('I am Underline-span')\n          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)\n        ImageSpan($r('app.media.icon'))\n          .size({ width: '100px', height: '100px' })\n          .verticalAlign(ImageSpanAlignment.BASELINE)\n        Span('I am Underline-span')\n          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)\n        ImageSpan($r('app.media.icon'))\n          .width('70px')\n          .height('70px')\n          .verticalAlign(ImageSpanAlignment.BOTTOM)\n        Span('I am Underline-span')\n          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(50)\n      }\n      .width('100%')\n      .textIndent(50)\n    }.width('100%').height('100%').padding({ left: 0, right: 0, top: 0 })\n  }\n}"""
            """示例2:// 该示例实现了如何设置ImageSpan图片的背景样式。\n\n// 创建一个Column布局，包含一个Text组件\nColumn() {\n    // 在Text组件中添加一个ImageSpan图片\n    Text() {\n        ImageSpan($r('app.media.app_icon'))\n          .width('60vp') // 设置图片宽度为60vp\n          .height('60vp') // 设置图片高度为60vp\n          .verticalAlign(ImageSpanAlignment.CENTER) // 设置图片垂直居中对齐\n          .textBackgroundStyle({color: Color.Green, radius: "5vp"}) // 设置文本背景样式为绿色圆角边框\n    }\n}.width('100%').alignItems(HorizontalAlign.Center) // 设置Column布局宽度为100%，水平居中对齐\n\n```\n// xxx.ets\n@Component\n@Entry\nstruct Index {\n  build() {\n    Column() {\n      Text() {\n        ImageSpan($r('app.media.app_icon'))\n          .width('60vp')\n          .height('60vp')\n          .verticalAlign(ImageSpanAlignment.CENTER)\n          .textBackgroundStyle({color: Color.Green, radius: "5vp"})\n      }\n    }.width('100%').alignItems(HorizontalAlign.Center)\n  }\n}"""
            """示例3:// ImageSpan设置图片成功加载解码和图片加载异常事件回调\n\n// 创建一个Index结构体，用于展示图片加载功能\n@Entry\n@Component\nstruct Index {\n  @State src: ResourceStr = $r('app.media.icon'); // 定义图片资源路径\n\n  build(){\n    Column(){ // 创建垂直布局\n      Text(){ // 创建文本组件\n        ImageSpan(this.src) // 设置图片资源路径\n          .width(100).height(100) // 设置图片宽高为100\n          .onError((err)=>{ // 当图片加载异常时的回调函数\n            console.log("onError:" + err.message) // 打印错误信息\n          })\n          .onComplete((event)=>{ // 当图片加载完成时的回调函数\n            console.log("onComplete: " + event.loadingStatus) // 打印加载状态\n          })\n      }\n    }.width('100%').height('100%') // 设置布局宽高为100%\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  @State src: ResourceStr = $r('app.media.icon');\n  build(){\n    Column(){\n      Text(){\n        ImageSpan(this.src)\n          .width(100).height(100)\n          .onError((err)=>{\n            console.log("onError:" + err.message)\n          })\n          .onComplete((event)=>{\n            console.log("onComplete: " + event.loadingStatus)\n          })\n      }\n    }.width('100%').height('100%')\n  }\n}"""
            """示例4:// xxx.ets\n\n// 导入网络请求、图片处理和基础服务模块\nimport { http } from '@kit.NetworkKit'\nimport { image } from '@kit.ImageKit'\nimport { BusinessError } from '@kit.BasicServicesKit'\n\n// 定义 SpanExample 结构体\n@Entry\n@Component\nstruct SpanExample {\n  // 定义 imageAlt 状态变量，用于存储网络图片的像素图\n  @State imageAlt: PixelMap | undefined = undefined\n\n  // 发起网络请求获取图片数据\n  httpRequest() {\n    // 直接加载网络地址，请填写一个具体的网络图片地址\n    http.createHttp().request("https://www.example.com/xxx.png", (error: BusinessError, data: http.HttpResponse) => {\n      if (error) {\n        console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`)\n      } else {\n        console.log(`http request success.`)\n        let imageData: ArrayBuffer = data.result as ArrayBuffer\n        let imageSource: image.ImageSource = image.createImageSource(imageData)\n\n        // 定义图片创建参数\n        class tmp {\n          height: number = 100\n          width: number = 100\n        }\n\n        let option: Record<string, number | boolean | tmp> = {\n          'alphaType': 0, // 透明度\n          'editable': false, // 是否可编辑\n          'pixelFormat': 3, // 像素格式\n          'scaleMode': 1, // 缩略值\n          'size': { height: 100, width: 100 }\n        }\n\n        // 创建像素图并将其赋值给 imageAlt 状态变量\n        imageSource.createPixelMap(option).then((pixelMap: PixelMap) => {\n          this.imageAlt = pixelMap\n        })\n      }\n    })\n  }\n\n  // 构建 UI\n  build() {\n    Column() {\n      // 创建按钮，点击触发网络请求\n      Button("获取网络图片")\n        .onClick(() => {\n          this.httpRequest()\n        })\n\n      // 显示图片\n      Text() {\n        // 直接加载网络地址，请填写一个具体的网络图片地址\n        ImageSpan('https://www.example.com/xxx.png')\n          .alt(this.imageAlt) // 设置图片的像素图\n          .width(300) // 设置图片宽度\n          .height(300) // 设置图片高度\n      }\n\n    }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })\n  }\n}\n```\n\n在以上代码中：\n1. `httpRequest` 方法发起网络请求，获取指定网络图片的数据，并根据返回结果进行处理。\n2. `build` 方法用于构建用户界面，包括一个按钮用于触发网络请求和一个用于显示网络图片的 ImageSpan 组件。\n3. `imageAlt` 是一个状态变量，用于存储网络图片的像素图。\n4. 通过网络请求获取的图片数据，经过处理后生成像素图，并赋值给 `imageAlt` 变量。\n5. 点击按钮会触发 `httpRequest` 方法，发起网络请求获取图片数据。\n6. ImageSpan 组件显示网络图片，设置了图片的像素图、宽度和高度。\n7. 其他注释中包括了一些代码的功能描述和参数说明，帮助开发者理解代码的作用和实现细节。\n// xxx.ets\nimport { http } from '@kit.NetworkKit'\nimport { image } from '@kit.ImageKit'\nimport { BusinessError } from '@kit.BasicServicesKit'\n\n@Entry\n@Component\nstruct SpanExample {\n  @State imageAlt: PixelMap | undefined = undefined\n\n  httpRequest() {\n    // 直接加载网络地址，请填写一个具体的网络图片地址\n    http.createHttp().request("https://www.example.com/xxx.png", (error: BusinessError, data: http.HttpResponse) => {\n      if (error) {\n        console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`)\n      } else {\n        console.log(`http request success.`)\n        let imageData: ArrayBuffer = data.result as ArrayBuffer\n        let imageSource: image.ImageSource = image.createImageSource(imageData)\n\n        class tmp {\n          height: number = 100\n          width: number = 100\n        }\n\n        let option: Record<string, number | boolean | tmp> = {\n          'alphaType': 0, // 透明度\n          'editable': false, // 是否可编辑\n          'pixelFormat': 3, // 像素格式\n          'scaleMode': 1, // 缩略值\n          'size': { height: 100, width: 100 }\n        }\n        //创建图片大小\n        imageSource.createPixelMap(option).then((pixelMap: PixelMap) => {\n          this.imageAlt = pixelMap\n        })\n      }\n    })\n  }\n\n  build() {\n    Column() {\n      Button("获取网络图片")\n        .onClick(() => {\n          this.httpRequest()\n        })\n\n      Text() {\n        // 直接加载网络地址，请填写一个具体的网络图片地址\n        ImageSpan('https://www.example.com/xxx.png')\n          .alt(this.imageAlt)\n          .width(300)\n          .height(300)\n      }\n\n    }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "LoadingProgress": {
        "description": "用于显示加载动效的组件。",
        "interfaces": [
            {
                "description": "创建加载进展组件。",
                "params": {}
            }
        ],
        "attributes": {
            "color": {
                "description": "设置加载进度条前景色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "加载进度条的前景色。",
                        "default": "API version 11及以上：'#ff666666'"
                    }
                }
            },
            "enableLoading": {
                "description": "设置LoadingProgress动画显示或者不显示。LoadingProgress动画不显示时，该组件依旧占位。通用属性[Visibility.Hidden](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-universal-attributes-visibility-V5#visibility)隐藏的是包括[border](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-universal-attributes-border-V5#border)、[padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-universal-attributes-size-V5#padding)等整个组件范围，而enableLoading=false只隐藏LoadingProgress本身动画内容，不包括border等。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "LoadingProgress动画是否显示。",
                        "default": True
                    }
                }
            },
            "contentModifier": {
                "description": "定制LoadingProgress内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<LoadingProgressConfiguration>",
                        "required": True,
                        "description": "定制LoadingProgress内容区的方法。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """// LoadingProgressExample.ets\n\n@Entry\n@Component\nstruct LoadingProgressExample {\n  build() {\n    // 创建一个垂直布局的加载进度示例，包括文字和加载进度条\n\n    Column({ space: 5 }) {\n      // 显示文字描述加载进度\n      Text('Orbital LoadingProgress ').fontSize(9).fontColor(0xCCCCCC).width('90%')\n\n      // 创建加载进度条组件\n      LoadingProgress()\n        .color(Color.Blue) // 设置加载进度条颜色为蓝色\n        .layoutWeight(1) // 设置加载进度条在布局中的权重，占据剩余空间\n    }.width('100%').margin({ top: 5 }) // 设置整体布局宽度为100%，顶部外边距为5\n  }\n}\n```\n\n在这段示例代码中，我们为LoadingProgressExample结构体的build方法添加了详细的功能与效果描述注释：\n\n1. 创建一个垂直布局的加载进度示例，包括文字和加载进度条。\n2. 显示文字描述加载进度，文字内容为'Orbital LoadingProgress'，字体大小为9，字体颜色为浅灰色，宽度占据90%。\n3. 创建加载进度条组件，设置加载进度条颜色为蓝色，布局权重为1，占据剩余空间。\n4. 整体布局宽度为100%，顶部外边距为5。\n// xxx.ets\n@Entry\n@Component\nstruct LoadingProgressExample {\n  build() {\n    Column({ space: 5 }) {\n      Text('Orbital LoadingProgress ').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      LoadingProgress()\n        .color(Color.Blue)\n        .layoutWeight(1)\n    }.width('100%').margin({ top: 5 })\n  }\n}"""
            """// 该示例实现了自定义LoadingProgress的功能，实现了通过按钮切换是否显示LoadingProgress。点击按钮，config.enableLoading切换为false, 不显示LoadingProgress。\n\n// 导入性能分析工具和ArkUI组件\nimport { hilog } from '@kit.PerformanceAnalysisKit'\nimport { promptAction } from '@kit.ArkUI'\n\n// 定义MyLoadingProgressStyle类，实现LoadingProgress的自定义样式\nclass MyLoadingProgressStyle implements ContentModifier<LoadingProgressConfiguration> {\n  enableLoading: boolean = false\n\n  constructor(enableLoading: boolean) {\n    this.enableLoading = enableLoading\n  }\n\n  // 应用自定义样式到LoadingProgress\n  applyContent(): WrappedBuilder<[LoadingProgressConfiguration]> {\n    return wrapBuilder(buildLoadingProgress)\n  }\n}\n\n// 初始化两个字符串数组\nlet arr1: string[] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]\nlet arr2: string[] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]\n\n// 构建LoadingProgress组件\n@Builder\nfunction buildLoadingProgress(config: LoadingProgressConfiguration) {\n  // 创建LoadingProgress的布局\n  Column({ space: 8 }) {\n    // 第一行\n    Row() {\n      // 左侧圆形\n      Column() {\n        Circle({\n          width: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? 100 : 80,\n          height: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? 100 : 80\n        })\n          .fill(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)\n      }.width('50%')\n\n      // 右侧按钮\n      Column() {\n        Button('' + ((config.contentModifier as MyLoadingProgressStyle).enableLoading))\n          .onClick((event: ClickEvent) => {\n            promptAction.showToast({\n              message: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) + ''\n            })\n          })\n          .fontColor(Color.White)\n          .backgroundColor(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)\n      }.width('50%')\n\n    }\n\n    // 第二行\n    Row() {\n      // 进度条\n      Column() {\n        Gauge({\n          value: (config.contentModifier as MyLoadingProgressStyle).enableLoading ? 50 : 30, min: 11, max: 100\n        }) {\n          Column() {\n            Text('60')\n              .maxFontSize("180sp")\n              .minFontSize("160.0vp")\n              .fontWeight(FontWeight.Medium)\n              .fontColor("#ff182431")\n              .width('40%')\n              .height('30%')\n              .textAlign(TextAlign.Center)\n              .margin({ top: '22.2%' })\n              .textOverflow({ overflow: TextOverflow.Ellipsis })\n              .maxLines(1)\n          }.width('100%').height('100%')\n        }\n\n        .colors(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)\n        .width(200)\n        .strokeWidth(18)\n        .padding(5)\n        .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n        .height(200)\n      }.width('100%')\n\n    }\n\n    // 列表\n    Column() {\n      List({ space: 20, initialIndex: 0 }) {\n        ForEach(arr2, (item: string) => {\n          ListItem() {\n            Text((config.contentModifier as MyLoadingProgressStyle).enableLoading ? '' + item : Number(item) * 2 + '')\n              .width('100%')\n              .height('100%')\n              .fontColor((config.contentModifier as MyLoadingProgressStyle).enableLoading ? Color.White : Color.Orange)\n              .fontSize((config.contentModifier as MyLoadingProgressStyle).enableLoading ? 16 : 20)\n              .textAlign(TextAlign.Center)\n              .backgroundColor((config.contentModifier as MyLoadingProgressStyle).enableLoading ? Color.Grey : 0x2577e3)\n          }\n          .height(110)\n          .border({\n            width: 2,\n            color: Color.White\n          })\n        }, (item: string) => item)\n      }\n      .height(200)\n      .width('100%')\n      .friction(0.6)\n\n      .lanes({ minLength: (config.contentModifier as MyLoadingProgressStyle).enableLoading ? 40 : 80, maxLength: (config.contentModifier as MyLoadingProgressStyle).enableLoading ? 40 : 80 })\n      .scrollBar(BarState.Off)\n    }\n\n  }.width("100%").padding(10)\n}\n\n// LoadingProgressDemoExample组件\n@Entry\n@Component\nstruct LoadingProgressDemoExample {\n  @State loadingProgressList: (boolean | undefined | null)[] = [undefined, true, null, false]\n  @State widthList: (number | string)[] = ['110%', 220, '40%', 80]\n  @State loadingProgressIndex: number = 0\n  @State clickFlag: number = 0\n  scroller: Scroller = new Scroller()\n\n  // 构建LoadingProgressDemoExample组件\n  build() {\n    Column() {\n      // 滚动视图\n      Scroll(this.scroller) {\n        Column({ space: 5 }) {\n          Column() {\n            // 创建LoadingProgress组件\n            LoadingProgress()\n              .color('#106836')\n              .size({ width: '100%' })\n              .contentModifier(new MyLoadingProgressStyle(this.loadingProgressList[this.loadingProgressIndex]))\n          }.width('100%').backgroundColor(0xdcdcdc)\n        }.width('100%').margin({ top: 5 })\n      }.height('85%')\n\n      // 切换按钮\n      Button('点击切换config.enableloading').onClick(() => {\n        this.clickFlag++\n        this.loadingProgressIndex = (this.loadingProgressIndex + 1) % this.loadingProgressList.length\n        console.log('enableLoading:' + this.loadingProgressList[this.loadingProgressIndex])\n      }).margin(20)\n    }\n\n  }\n}\n```\n//该示例实现了自定义LoadingProgress的功能，实现了通过按钮切换是否显示LoadingProgress。点击按钮，config.enableLoading切换为false, 不显示LoadingProgress。\n// xxx.ets\nimport { hilog } from '@kit.PerformanceAnalysisKit'\nimport { promptAction } from '@kit.ArkUI'\n\nclass MyLoadingProgressStyle implements ContentModifier<LoadingProgressConfiguration> {\n  enableLoading: boolean = false\n\n  constructor(enableLoading: boolean) {\n    this.enableLoading = enableLoading\n  }\n\n  applyContent(): WrappedBuilder<[LoadingProgressConfiguration]> {\n    return wrapBuilder(buildLoadingProgress)\n  }\n}\n\nlet arr1: string[] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]\nlet arr2: string[] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]\n\n@Builder\nfunction buildLoadingProgress(config: LoadingProgressConfiguration) {\n  Column({ space: 8 }) {\n    Row() {\n      Column() {\n        Circle({\n          width: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? 100 : 80,\n          height: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? 100 : 80\n        })\n          .fill(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)\n      }.width('50%')\n\n      Column() {\n        Button('' + ((config.contentModifier as MyLoadingProgressStyle).enableLoading))\n          .onClick((event: ClickEvent) => {\n            promptAction.showToast({\n              message: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) + ''\n            })\n          })\n          .fontColor(Color.White)\n          .backgroundColor(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)\n      }.width('50%')\n\n    }\n\n    Row() {\n      Column() {\n        Gauge({\n          value: (config.contentModifier as MyLoadingProgressStyle).enableLoading?50:30, min: 11, max: 100\n        }) {\n          Column() {\n            Text('60')\n              .maxFontSize("180sp")\n              .minFontSize("160.0vp")\n              .fontWeight(FontWeight.Medium)\n              .fontColor("#ff182431")\n              .width('40%')\n              .height('30%')\n              .textAlign(TextAlign.Center)\n              .margin({ top: '22.2%' })\n              .textOverflow({ overflow: TextOverflow.Ellipsis })\n              .maxLines(1)\n          }.width('100%').height('100%')\n        }\n\n        .colors(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)\n        .width(200)\n        .strokeWidth(18)\n        .padding(5)\n        .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })\n        .height(200)\n      }.width('100%')\n\n    }\n\n    Column() {\n      List({ space: 20, initialIndex: 0 }) {\n        ForEach(arr2, (item: string) => {\n          ListItem() {\n            Text((config.contentModifier as MyLoadingProgressStyle).enableLoading ? '' + item : Number(item) * 2 + '')\n              .width('100%')\n              .height('100%')\n              .fontColor((config.contentModifier as MyLoadingProgressStyle).enableLoading ? Color.White : Color.Orange)\n              .fontSize((config.contentModifier as MyLoadingProgressStyle).enableLoading ? 16 : 20)\n              .textAlign(TextAlign.Center)\n              .backgroundColor((config.contentModifier as MyLoadingProgressStyle).enableLoading ? Color.Grey : 0x2577e3)\n          }\n          .height(110)\n          .border({\n            width: 2,\n            color: Color.White\n          })\n        }, (item: string) => item)\n      }\n      .height(200)\n      .width('100%')\n      .friction(0.6)\n\n      .lanes({ minLength: (config.contentModifier as MyLoadingProgressStyle).enableLoading?40:80, maxLength: (config.contentModifier as MyLoadingProgressStyle).enableLoading?40:80 })\n      .scrollBar(BarState.Off)\n    }\n\n  }.width("100%").padding(10)\n}\n\n\n\n@Entry\n@Component\nstruct LoadingProgressDemoExample {\n  @State loadingProgressList: (boolean | undefined | null)[] = [undefined, true, null, false]\n  @State widthList: (number | string)[] = ['110%', 220, '40%', 80]\n  @State loadingProgressIndex: number = 0\n  @State clickFlag: number = 0\n  scroller: Scroller = new Scroller()\n\n  build() {\n    Column() {\n      Scroll(this.scroller) {\n        Column({ space: 5 }) {\n          Column() {\n            LoadingProgress()\n              .color('#106836')\n              .size({ width: '100%' })\n              .contentModifier(new MyLoadingProgressStyle(this.loadingProgressList[this.loadingProgressIndex]))\n          }.width('100%').backgroundColor(0xdcdcdc)\n        }.width('100%').margin({ top: 5 })\n      }.height('85%')\n\n      Button('点击切换config.enableloading').onClick(() => {\n        this.clickFlag++\n        this.loadingProgressIndex = (this.loadingProgressIndex + 1) % this.loadingProgressList.length\n        console.log('enableLoading:' + this.loadingProgressList[this.loadingProgressIndex])\n      }).margin(20)\n    }\n\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Marquee": {
        "description": "跑马灯组件，用于滚动展示一段单行文本。仅当文本内容宽度超过跑马灯组件宽度时滚动，不超过时不滚动。",
        "interfaces": [
            {
                "description": "创建跑马灯组件。",
                "params": {
                    "value": {
                        "type": {
                            "start": "boolean",
                            "step": "number",
                            "loop": "number",
                            "fromStart": "boolean",
                            "src": "string"
                        },
                        "required": True,
                        "description": "配置跑马灯组件的参数。\n- start：控制跑马灯是否进入播放状态。\n- step：滚动动画文本滚动步长，当step大于Marquee的文本宽度时，取默认值。\n- loop：设置重复滚动的次数，小于等于零时无限循环。\n- fromStart：设置文本从头开始滚动或反向滚动。\n- src：需要滚动的文本。",
                        "default": {
                            "step": 6,
                            "loop": -1,
                            "fromStart": True
                        }
                    }
                }
            }
        ],
        "attributes": {
            "allowScale": {
                "description": "设置是否允许文本缩放。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否允许文本缩放。",
                        "default": False
                    }
                }
            },
            "marqueeUpdateStrategy": {
                "description": "跑马灯组件属性更新后，跑马灯的滚动策略。(当跑马灯为播放状态，且文本内容宽度超过跑马灯组件宽度时，该属性生效。)",
                "params": {
                    "value": {
                        "type": "MarqueeUpdateStrategy",
                        "required": True,
                        "description": "跑马灯组件属性更新后，跑马灯的滚动策略。",
                        "default": "MarqueeUpdateStrategy.DEFAULT"
                    }
                }
            }
        },
        "events": {
            "onStart": {
                "description": "开始滚动时触发回调。",
                "params": {}
            },
            "onBounce": {
                "description": "完成一次滚动时触发，若循环次数不为1，则该事件会多次触发。",
                "params": {}
            },
            "onFinish": {
                "description": "滚动全部循环次数完成时触发回调。",
                "params": {}
            }
        },
        "examples": [
            """// xxx.ets\n\n// 定义一个跑马灯示例组件，包括跑马灯文本内容、动画控制等功能\n@Entry\n@Component\nstruct MarqueeExample {\n  @State start: boolean = false // 控制跑马灯动画开始或停止的状态\n  @State src: string = '' // 跑马灯文本内容的来源\n  @State marqueeText: string = 'Running Marquee' // 默认的跑马灯文本内容\n\n  private fromStart: boolean = true // 跑马灯动画是否从头开始的标识\n  private step: number = 10 // 跑马灯文本滚动的步长\n  private loop: number = Number.POSITIVE_INFINITY // 跑马灯文本滚动的循环次数\n\n  controller: TextClockController = new TextClockController() // 文本时钟控制器实例\n\n  // 将数字转换为时间格式的字符串，格式为"HH:MM:SS"\n  convert2time(value: number): string {\n    let date = new Date(Number(value + '000'));\n    let hours = date.getHours().toString().padStart(2, '0');\n    let minutes = date.getMinutes().toString().padStart(2, '0');\n    let seconds = date.getSeconds().toString().padStart(2, '0');\n    return hours + ":" + minutes + ":" + seconds;\n  }\n\n  // 构建跑马灯示例组件\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\n      // 创建跑马灯组件，并设置相关属性\n      Marquee({\n        start: this.start,\n        step: this.step,\n        loop: this.loop,\n        fromStart: this.fromStart,\n        src: this.marqueeText + this.src\n      })\n        .marqueeUpdateStrategy(MarqueeUpdateStrategy.PRESERVE_POSITION)\n        .width(300)\n        .height(80)\n        .fontColor('#FFFFFF')\n        .fontSize(48)\n        .fontWeight(700)\n        .backgroundColor('#182431')\n        .margin({ bottom: 40 })\n        .onStart(() => {\n          console.info('Marquee animation complete onStart')\n        })\n        .onBounce(() => {\n          console.info('Marquee animation complete onBounce')\n        })\n        .onFinish(() => {\n          console.info('Marquee animation complete onFinish')\n        })\n\n      // 创建一个按钮用于启动跑马灯动画\n      Button('Start')\n        .onClick(() => {\n          this.start = true\n          // 启动文本时钟\n          this.controller.start()\n        })\n        .width(120)\n        .height(40)\n        .fontSize(16)\n        .fontWeight(500)\n        .backgroundColor('#007DFF')\n\n      // 创建文本时钟组件，用于显示时间\n      TextClock({ timeZoneOffset: -8, controller: this.controller })\n        .format('hms')\n        .onDateChange((value: number) => {\n          this.src = this.convert2time(value);\n        })\n        .margin(20)\n        .fontSize(30)\n    }\n    .width('100%')\n    .height('100%')\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct MarqueeExample {\n  @State start: boolean = false\n  @State src: string = ''\n  @State marqueeText: string = 'Running Marquee'\n  private fromStart: boolean = true\n  private step: number = 10\n  private loop: number = Number.POSITIVE_INFINITY\n  controller: TextClockController = new TextClockController()\n  convert2time(value: number): string{\n    let date = new Date(Number(value+'000'));\n    let hours = date.getHours().toString().padStart(2, '0');\n    let minutes = date.getMinutes().toString().padStart(2, '0');\n    let seconds = date.getSeconds().toString().padStart(2, '0');\n    return hours+ ":" + minutes + ":" + seconds;\n  }\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\n      Marquee({\n        start: this.start,\n        step: this.step,\n        loop: this.loop,\n        fromStart: this.fromStart,\n        src: this.marqueeText + this.src\n      })\n        .marqueeUpdateStrategy(MarqueeUpdateStrategy.PRESERVE_POSITION)\n        .width(300)\n        .height(80)\n        .fontColor('#FFFFFF')\n        .fontSize(48)\n        .fontWeight(700)\n        .backgroundColor('#182431')\n        .margin({ bottom: 40 })\n        .onStart(() => {\n          console.info('Marquee animation complete onStart')\n        })\n        .onBounce(() => {\n          console.info('Marquee animation complete onBounce')\n        })\n        .onFinish(() => {\n          console.info('Marquee animation complete onFinish')\n        })\n      Button('Start')\n        .onClick(() => {\n          this.start = true\n          //启动文本时钟\n          this.controller.start()\n        })\n        .width(120)\n        .height(40)\n        .fontSize(16)\n        .fontWeight(500)\n        .backgroundColor('#007DFF')\n      TextClock({ timeZoneOffset: -8, controller: this.controller })\n        .format('hms')\n        .onDateChange((value: number) => {\n          this.src = this.convert2time(value);\n        })\n        .margin(20)\n        .fontSize(30)\n    }\n    .width('100%')\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Menu": {
        "description": "以垂直列表形式显示的菜单。",
        "interfaces": [
            {
                "description": "作为菜单的固定容器，无参数。菜单和菜单项宽度计算规则：布局过程中，期望每个菜单项的宽度一致。若子组件设置了宽度，则以尺寸计算规则为准。不设置宽度的情况：菜单组件会对子组件MenuItem、MenuItemGroup设置默认2栅格的宽度，若菜单项内容区比2栅格宽，则会自适应撑开。设置宽度的情况：菜单组件会对子组件MenuItem、MenuItemGroup设置减去padding后的固定宽度。",
                "params": {}
            }
        ],
        "attributes": {
            "fontSize": {
                "description": "统一设置Menu中所有文本的尺寸。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "Menu中所有文本的尺寸，Length为number类型时，使用fp单位。"
                    }
                }
            },
            "font": {
                "description": "统一设置Menu中所有文本的尺寸。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "Menu中所有文本的尺寸。"
                    }
                }
            },
            "fontColor": {
                "description": "统一设置Menu中所有文本的颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "Menu中所有文本的颜色。"
                    }
                }
            },
            "radius": {
                "description": "设置Menu边框圆角半径。",
                "params": {
                    "value": {
                        "type": ["Dimension", "BorderRadiuses"],
                        "required": True,
                        "description": "Menu边框圆角半径。默认值跟随主题。"
                    }
                }
            },
            "width": {
                "description": "设置Menu边框宽度，支持设置的最小宽度为64vp。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "Menu边框宽度。"
                    }
                }
            },
            "menuItemDivider": {
                "description": "设置menuItem分割线样式, 不设置该属性则不展示分割线。",
                "params": {
                    "options": {
                        "type": ["DividerStyleOptions", "undefined"],
                        "required": True,
                        "description": "设置menuItem分割线样式。"
                    }
                }
            },
            "menuItemGroupDivider": {
                "description": "设置menuItemGroup上下分割线的样式, 不设置该属性则默认展示分割线。",
                "params": {
                    "options": {
                        "type": ["DividerStyleOptions", "undefined"],
                        "required": True,
                        "description": "设置menuItemGroup顶部和底部分割线样式。"
                    }
                }
            },
            "subMenuExpandingMode": {
                "description": "设置Menu子菜单展开样式。",
                "params": {
                    "mode": {
                        "type": "SubMenuExpandingMode",
                        "required": True,
                        "description": "Menu子菜单展开样式。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """示例1:\n@Entry\n@Component\nstruct Index {\n  @State select: boolean = true // 定义一个状态变量select，初始值为true\n  private iconStr: ResourceStr = $r("app.media.view_list_filled") // 定义私有变量iconStr，用于存储图标资源\n  private iconStr2: ResourceStr = $r("app.media.arrow_right_filled") // 定义私有变量iconStr2，用于存储另一个图标资源\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" }) // 创建一个菜单项"复制"，并显示快捷键信息\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" }) // 创建一个菜单项"粘贴"，并显示快捷键信息\n    }\n  }\n\n  @Builder\n  MyMenu(){\n    Menu() {\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" }) // 创建一个带图标的菜单项\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" }) // 创建另一个带图标的菜单项\n        .enabled(false) // 禁用该菜单项\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n        endIcon: this.iconStr2,\n        builder: ():void=>this.SubMenu() // 创建一个带图标和子菜单的菜单项\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          startIcon: this.iconStr,\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu() // 在菜单组中创建带图标和子菜单的菜单项\n        })\n        MenuItem({\n          startIcon: $r("app.media.app_icon"),\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu() // 在菜单组中创建带图标和子菜单的菜单项\n        })\n      }\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n      })\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu') // 显示文本"click to show menu"\n          .fontSize(50) // 设置字体大小为50\n          .fontWeight(FontWeight.Bold) // 设置字体加粗\n      }\n      .bindMenu(this.MyMenu) // 绑定菜单到Column上\n      .width('100%') // 设置宽度为100%\n    }\n    .height('100%') // 设置高度为100%\n  }\n}\n```\n@Entry\n@Component\nstruct Index {\n  @State select: boolean = true\n  private iconStr: ResourceStr = $r("app.media.view_list_filled")\n  private iconStr2: ResourceStr = $r("app.media.arrow_right_filled")\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" })\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })\n    }\n  }\n\n  @Builder\n  MyMenu(){\n    Menu() {\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })\n        .enabled(false)\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n        endIcon: this.iconStr2,\n        builder: ():void=>this.SubMenu()\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          startIcon: this.iconStr,\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu()\n        })\n        MenuItem({\n          startIcon: $r("app.media.app_icon"),\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu()\n        })\n      }\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n      })\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu')\n          .fontSize(50)\n          .fontWeight(FontWeight.Bold)\n      }\n      .bindMenu(this.MyMenu)\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
            """示例2:\n// xxx.ets\n\n// 定义普通菜单组件，包含多个菜单项\n// 菜单项包括不同的图标、文本内容和交互功能\n@Builder\nMyMenu() {\n  Menu() {\n    // 创建带有symbol类型图标的菜单项\n    MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n    \n    // 创建带有symbol类型图标的菜单项，并设置为不可用状态\n    MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n      .enabled(false)\n    \n    // 创建带有起始和结束symbol类型图标的菜单项，并包含子菜单\n    MenuItem({\n      symbolStartIcon: this.startIconModifier,\n      content: "菜单选项",\n      symbolEndIcon: this.endIconModifier,\n      builder: (): void => this.SubMenu()\n    })\n    \n    // 创建带有标题的菜单项组，包含多个带有图标的菜单项和子菜单\n    MenuItemGroup({ header: '小标题' }) {\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n    }\n    \n    // 创建带有选中状态的菜单项，并设置选中图标\n    MenuItem({\n      content: "菜单选项",\n    }).selected(this.select).selectIcon(this.selectIconModifier)\n  }\n}\n\n// 构建页面布局，包含一个点击展示菜单的按钮\nbuild() {\n  Row() {\n    Column() {\n      // 显示点击展示菜单的文本\n      Text('click to show menu')\n        .fontSize(50)\n        .fontWeight(FontWeight.Bold)\n    }\n    // 将MyMenu绑定到按钮，点击按钮展示菜单\n    .bindMenu(this.MyMenu)\n    .width('100%')\n  }\n  .height('100%')\n}\n```\n\n在以上代码中：\n- `MyMenu`函数定义了一个包含多个菜单项的普通菜单组件，每个菜单项包含不同的图标、文本内容和交互功能。\n- `MenuItem`用于创建单个菜单项，其中`symbolStartIcon`表示起始图标，`symbolEndIcon`表示结束图标，`content`表示菜单项文本内容。\n- `MenuItemGroup`用于创建带有标题的菜单项组，包含多个菜单项和子菜单。\n- `selected`属性用于设置菜单项的选中状态，`selectIcon`用于设置选中状态的图标。\n- `build`函数定义了页面布局，包含一个按钮，点击按钮可以展示定义的菜单。\n- 通过`bindMenu`将`MyMenu`与按钮绑定，实现点击展示菜单的功能。\n// xxx.ets\nimport { SymbolGlyphModifier } from '@kit.ArkUI';\n\n@Entry\n@Component\nstruct Index {\n  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic')).fontSize('24vp');\n  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontSize('24vp');\n  @State selectIconModifier: SymbolGlyphModifier =\n    new SymbolGlyphModifier($r('sys.symbol.checkmark')).fontSize('24vp');\n  @State select: boolean = true;\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" })\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })\n    }\n  }\n\n  @Builder\n  MyMenu() {\n    Menu() {\n      MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n      MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n        .enabled(false)\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          symbolStartIcon: this.startIconModifier,\n          content: "菜单选项",\n          symbolEndIcon: this.endIconModifier,\n          builder: (): void => this.SubMenu()\n        })\n        MenuItem({\n          symbolStartIcon: this.startIconModifier,\n          content: "菜单选项",\n          symbolEndIcon: this.endIconModifier,\n          builder: (): void => this.SubMenu()\n        })\n      }\n      MenuItem({\n        content: "菜单选项",\n      }).selected(this.select).selectIcon(this.selectIconModifier)\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu')\n          .fontSize(50)\n          .fontWeight(FontWeight.Bold)\n      }\n      .bindMenu(this.MyMenu)\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "MenuItem": {
        "description": "用来展示菜单Menu中具体的item菜单项。",
        "interfaces": [
            {
                "description": "创建MenuItem组件。",
                "params": {
                    "value": {
                        "type": ["MenuItemOptions", "CustomBuilder"],
                        "required": False,
                        "description": "包含设置MenuItem的各项信息。"
                    }
                }
            }
        ],
        "attributes": {
            "selected": {
                "description": "设置菜单项是否选中。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "菜单项是否选中。",
                        "default": False
                    }
                }
            },
            "selectIcon": {
                "description": "设置当菜单项被选中时，是否显示被选中的图标。",
                "params": {
                    "value": {
                        "type": ["boolean", "ResourceStr", "SymbolGlyphModifier"],
                        "required": True,
                        "description": "菜单项被选中时，是否显示被选中的图标。",
                        "default": False
                    }
                }
            },
            "contentFont": {
                "description": "设置菜单项中内容信息的字体样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "菜单项中内容信息的字体样式。"
                    }
                }
            },
            "contentFontColor": {
                "description": "设置菜单项中内容信息的字体颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "菜单项中内容信息的字体颜色。"
                    }
                }
            },
            "labelFont": {
                "description": "设置菜单项中标签信息的字体样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "菜单项中标签信息的字体样式。"
                    }
                }
            },
            "labelFontColor": {
                "description": "设置菜单项中标签信息的字体颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "菜单项中标签信息的字体颜色。"
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "当选中状态发生变化时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "选中状态发生变化时，触发该回调。",
                        "params": {
                            "selected": {
                                "type": "boolean",
                                "description": "选中状态发生变化时，触发该回调。返回值为true时，表示已选中，为false时，表示未选中。"
                            }
                        }
                    }
                }
            }
        },
        "examples": [
            """@Entry\n@Component\nstruct Index {\n  @State select: boolean = true // 定义一个状态变量select，初始值为true\n  private iconStr: ResourceStr = $r("app.media.view_list_filled") // 定义私有变量iconStr，用于存储图标资源\n  private iconStr2: ResourceStr = $r("app.media.arrow_right_filled") // 定义私有变量iconStr2，用于存储另一个图标资源\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" }) // 创建一个菜单项"复制"，并显示快捷键信息\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" }) // 创建一个菜单项"粘贴"，并显示快捷键信息\n    }\n  }\n\n  @Builder\n  MyMenu(){\n    Menu() {\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" }) // 创建一个带图标的菜单项\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" }) // 创建另一个带图标的菜单项\n        .enabled(false) // 禁用该菜单项\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n        endIcon: this.iconStr2,\n        builder: ():void=>this.SubMenu() // 创建一个带图标和子菜单的菜单项\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          startIcon: this.iconStr,\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu() // 在菜单组中创建带图标和子菜单的菜单项\n        })\n        MenuItem({\n          startIcon: $r("app.media.app_icon"),\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu() // 在菜单组中创建带图标和子菜单的菜单项\n        })\n      }\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n      })\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu') // 显示文本"click to show menu"\n          .fontSize(50) // 设置字体大小为50\n          .fontWeight(FontWeight.Bold) // 设置字体加粗\n      }\n      .bindMenu(this.MyMenu) // 绑定菜单到Column上\n      .width('100%') // 设置宽度为100%\n    }\n    .height('100%') // 设置高度为100%\n  }\n}\n```\n@Entry\n@Component\nstruct Index {\n  @State select: boolean = true\n  private iconStr: ResourceStr = $r("app.media.view_list_filled")\n  private iconStr2: ResourceStr = $r("app.media.arrow_right_filled")\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" })\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })\n    }\n  }\n\n  @Builder\n  MyMenu(){\n    Menu() {\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })\n        .enabled(false)\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n        endIcon: this.iconStr2,\n        builder: ():void=>this.SubMenu()\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          startIcon: this.iconStr,\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu()\n        })\n        MenuItem({\n          startIcon: $r("app.media.app_icon"),\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu()\n        })\n      }\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n      })\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu')\n          .fontSize(50)\n          .fontWeight(FontWeight.Bold)\n      }\n      .bindMenu(this.MyMenu)\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
            """// xxx.ets\n\n// 定义普通菜单组件，包含多个菜单项\n// 菜单项包括不同的图标、文本内容和交互功能\n@Builder\nMyMenu() {\n  Menu() {\n    // 创建带有symbol类型图标的菜单项\n    MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n    \n    // 创建带有symbol类型图标的菜单项，并设置为不可用状态\n    MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n      .enabled(false)\n    \n    // 创建带有起始和结束symbol类型图标的菜单项，并包含子菜单\n    MenuItem({\n      symbolStartIcon: this.startIconModifier,\n      content: "菜单选项",\n      symbolEndIcon: this.endIconModifier,\n      builder: (): void => this.SubMenu()\n    })\n    \n    // 创建带有标题的菜单项组，包含多个带有图标的菜单项和子菜单\n    MenuItemGroup({ header: '小标题' }) {\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n    }\n    \n    // 创建带有选中状态的菜单项，并设置选中图标\n    MenuItem({\n      content: "菜单选项",\n    }).selected(this.select).selectIcon(this.selectIconModifier)\n  }\n}\n\n// 构建页面布局，包含一个点击展示菜单的按钮\nbuild() {\n  Row() {\n    Column() {\n      // 显示点击展示菜单的文本\n      Text('click to show menu')\n        .fontSize(50)\n        .fontWeight(FontWeight.Bold)\n    }\n    // 将MyMenu绑定到按钮，点击按钮展示菜单\n    .bindMenu(this.MyMenu)\n    .width('100%')\n  }\n  .height('100%')\n}\n```\n\n在以上代码中：\n- `MyMenu`函数定义了一个包含多个菜单项的普通菜单组件，每个菜单项包含不同的图标、文本内容和交互功能。\n- `MenuItem`用于创建单个菜单项，其中`symbolStartIcon`表示起始图标，`symbolEndIcon`表示结束图标，`content`表示菜单项文本内容。\n- `MenuItemGroup`用于创建带有标题的菜单项组，包含多个菜单项和子菜单。\n- `selected`属性用于设置菜单项的选中状态，`selectIcon`用于设置选中状态的图标。\n- `build`函数定义了页面布局，包含一个按钮，点击按钮可以展示定义的菜单。\n- 通过`bindMenu`将`MyMenu`与按钮绑定，实现点击展示菜单的功能。\n// xxx.ets\nimport { SymbolGlyphModifier } from '@kit.ArkUI';\n\n@Entry\n@Component\nstruct Index {\n  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic')).fontSize('24vp');\n  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontSize('24vp');\n  @State selectIconModifier: SymbolGlyphModifier =\n    new SymbolGlyphModifier($r('sys.symbol.checkmark')).fontSize('24vp');\n  @State select: boolean = true;\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" })\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })\n    }\n  }\n\n  @Builder\n  MyMenu() {\n    Menu() {\n      MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n      MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n        .enabled(false)\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          symbolStartIcon: this.startIconModifier,\n          content: "菜单选项",\n          symbolEndIcon: this.endIconModifier,\n          builder: (): void => this.SubMenu()\n        })\n        MenuItem({\n          symbolStartIcon: this.startIconModifier,\n          content: "菜单选项",\n          symbolEndIcon: this.endIconModifier,\n          builder: (): void => this.SubMenu()\n        })\n      }\n      MenuItem({\n        content: "菜单选项",\n      }).selected(this.select).selectIcon(this.selectIconModifier)\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu')\n          .fontSize(50)\n          .fontWeight(FontWeight.Bold)\n      }\n      .bindMenu(this.MyMenu)\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "MenuItemGroup": {
        "description": "该组件用来展示菜单MenuItem的分组。",
        "interfaces": [
            {
                "description": "创建MenuItemGroup组件。",
                "params": {
                    "value": {
                        "type": "MenuItemGroupOptions",
                        "required": False,
                        "description": "包含设置MenuItemGroup的标题和尾部显示信息。"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {},
        "examples": [
            """@Entry\n@Component\nstruct Index {\n  @State select: boolean = true // 定义一个状态变量select，初始值为true\n  private iconStr: ResourceStr = $r("app.media.view_list_filled") // 定义私有变量iconStr，用于存储图标资源\n  private iconStr2: ResourceStr = $r("app.media.arrow_right_filled") // 定义私有变量iconStr2，用于存储另一个图标资源\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" }) // 创建一个菜单项"复制"，并显示快捷键信息\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" }) // 创建一个菜单项"粘贴"，并显示快捷键信息\n    }\n  }\n\n  @Builder\n  MyMenu(){\n    Menu() {\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" }) // 创建一个带图标的菜单项\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" }) // 创建另一个带图标的菜单项\n        .enabled(false) // 禁用该菜单项\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n        endIcon: this.iconStr2,\n        builder: ():void=>this.SubMenu() // 创建一个带图标和子菜单的菜单项\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          startIcon: this.iconStr,\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu() // 在菜单组中创建带图标和子菜单的菜单项\n        })\n        MenuItem({\n          startIcon: $r("app.media.app_icon"),\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu() // 在菜单组中创建带图标和子菜单的菜单项\n        })\n      }\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n      })\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu') // 显示文本"click to show menu"\n          .fontSize(50) // 设置字体大小为50\n          .fontWeight(FontWeight.Bold) // 设置字体加粗\n      }\n      .bindMenu(this.MyMenu) // 绑定菜单到Column上\n      .width('100%') // 设置宽度为100%\n    }\n    .height('100%') // 设置高度为100%\n  }\n}\n```\n@Entry\n@Component\nstruct Index {\n  @State select: boolean = true\n  private iconStr: ResourceStr = $r("app.media.view_list_filled")\n  private iconStr2: ResourceStr = $r("app.media.arrow_right_filled")\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" })\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })\n    }\n  }\n\n  @Builder\n  MyMenu(){\n    Menu() {\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })\n        .enabled(false)\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n        endIcon: this.iconStr2,\n        builder: ():void=>this.SubMenu()\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          startIcon: this.iconStr,\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu()\n        })\n        MenuItem({\n          startIcon: $r("app.media.app_icon"),\n          content: "菜单选项",\n          endIcon: this.iconStr2,\n          builder: ():void=>this.SubMenu()\n        })\n      }\n      MenuItem({\n        startIcon: this.iconStr,\n        content: "菜单选项",\n      })\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu')\n          .fontSize(50)\n          .fontWeight(FontWeight.Bold)\n      }\n      .bindMenu(this.MyMenu)\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
            """// xxx.ets\n\n// 定义普通菜单组件，包含多个菜单项\n// 菜单项包括不同的图标、文本内容和交互功能\n@Builder\nMyMenu() {\n  Menu() {\n    // 创建带有symbol类型图标的菜单项\n    MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n    \n    // 创建带有symbol类型图标的菜单项，并设置为不可用状态\n    MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n      .enabled(false)\n    \n    // 创建带有起始和结束symbol类型图标的菜单项，并包含子菜单\n    MenuItem({\n      symbolStartIcon: this.startIconModifier,\n      content: "菜单选项",\n      symbolEndIcon: this.endIconModifier,\n      builder: (): void => this.SubMenu()\n    })\n    \n    // 创建带有标题的菜单项组，包含多个带有图标的菜单项和子菜单\n    MenuItemGroup({ header: '小标题' }) {\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n    }\n    \n    // 创建带有选中状态的菜单项，并设置选中图标\n    MenuItem({\n      content: "菜单选项",\n    }).selected(this.select).selectIcon(this.selectIconModifier)\n  }\n}\n\n// 构建页面布局，包含一个点击展示菜单的按钮\nbuild() {\n  Row() {\n    Column() {\n      // 显示点击展示菜单的文本\n      Text('click to show menu')\n        .fontSize(50)\n        .fontWeight(FontWeight.Bold)\n    }\n    // 将MyMenu绑定到按钮，点击按钮展示菜单\n    .bindMenu(this.MyMenu)\n    .width('100%')\n  }\n  .height('100%')\n}\n```\n\n在以上代码中：\n- `MyMenu`函数定义了一个包含多个菜单项的普通菜单组件，每个菜单项包含不同的图标、文本内容和交互功能。\n- `MenuItem`用于创建单个菜单项，其中`symbolStartIcon`表示起始图标，`symbolEndIcon`表示结束图标，`content`表示菜单项文本内容。\n- `MenuItemGroup`用于创建带有标题的菜单项组，包含多个菜单项和子菜单。\n- `selected`属性用于设置菜单项的选中状态，`selectIcon`用于设置选中状态的图标。\n- `build`函数定义了页面布局，包含一个按钮，点击按钮可以展示定义的菜单。\n- 通过`bindMenu`将`MyMenu`与按钮绑定，实现点击展示菜单的功能。\n// xxx.ets\nimport { SymbolGlyphModifier } from '@kit.ArkUI';\n\n@Entry\n@Component\nstruct Index {\n  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic')).fontSize('24vp');\n  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontSize('24vp');\n  @State selectIconModifier: SymbolGlyphModifier =\n    new SymbolGlyphModifier($r('sys.symbol.checkmark')).fontSize('24vp');\n  @State select: boolean = true;\n\n  @Builder\n  SubMenu() {\n    Menu() {\n      MenuItem({ content: "复制", labelInfo: "Ctrl+C" })\n      MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })\n    }\n  }\n\n  @Builder\n  MyMenu() {\n    Menu() {\n      MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n      MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })\n        .enabled(false)\n      MenuItem({\n        symbolStartIcon: this.startIconModifier,\n        content: "菜单选项",\n        symbolEndIcon: this.endIconModifier,\n        builder: (): void => this.SubMenu()\n      })\n      MenuItemGroup({ header: '小标题' }) {\n        MenuItem({\n          symbolStartIcon: this.startIconModifier,\n          content: "菜单选项",\n          symbolEndIcon: this.endIconModifier,\n          builder: (): void => this.SubMenu()\n        })\n        MenuItem({\n          symbolStartIcon: this.startIconModifier,\n          content: "菜单选项",\n          symbolEndIcon: this.endIconModifier,\n          builder: (): void => this.SubMenu()\n        })\n      }\n      MenuItem({\n        content: "菜单选项",\n      }).selected(this.select).selectIcon(this.selectIconModifier)\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text('click to show menu')\n          .fontSize(50)\n          .fontWeight(FontWeight.Bold)\n      }\n      .bindMenu(this.MyMenu)\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Navigation": {
        "description": "Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-navdestination-V5)的子组件），首页和非首页通过路由进行切换。",
        "interfaces": [
            {
                "description": "Navigation(pathInfos: NavPathStack)\n\n绑定路由栈到Navigation组件。",
                "params": {
                    "pathInfos": {
                        "type": "NavPathStack",
                        "required": True,
                        "description": "Navigation路由栈，允许被继承12+。开发者可以在派生类中新增属性方法，也可以重写基类NavPathStack的方法。派生类对象可以替代基类NavPathStack对象使用。使用示例参见[示例10](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-navigation-V5#%E7%A4%BA%E4%BE%8B10)。"
                    }
                }
            }
        ],
        "attributes": {
            "title": {
                "description": "title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle, options?: NavigationTitleOptions)\n\n设置页面标题。",
                "params": {
                    "value": {
                        "type": ["ResourceStr", "CustomBuilder", "NavigationCommonTitle", "NavigationCustomTitle"],
                        "required": True,
                        "description": "页面标题，使用NavigationCustomTitle类型设置height高度时，titleMode属性不会生效。字符串超长时，如果不设置副标题，先缩小再换行（2行）最后...截断。如果设置副标题，先缩小最后...截断。"
                    },
                    "options": {
                        "type": "NavigationTitleOptions",
                        "required": False,
                        "description": "标题栏的额外配置选项。"
                    }
                }
            },
            "subTitle(deprecated)": {
                "description": "设置页面副标题。从API Version 9开始废弃，建议使用title代替。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "页面副标题。"
                    }
                }
            },
            "menus": {
                "description": "menus(value: Array<NavigationMenuItem> | CustomBuilder)\n\n设置页面右上角菜单。不设置时不显示菜单项。使用Array<[NavigationMenuItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-navigation-V5#navigationmenuitem%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E)> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。",
                "params": {
                    "value": {
                        "type": ["Array<NavigationMenuItem>", "CustomBuilder"],
                        "required": True,
                        "description": "菜单项的内容。"
                    }
                }
            },
            "titleMode": {
                "description": "titleMode(value: NavigationTitleMode)\n\n设置页面标题栏显示模式。",
                "params": {
                    "value": {
                        "type": "NavigationTitleMode",
                        "required": True,
                        "description": "标题栏显示模式。"
                    }
                }
            },
            "toolBar": {
                "description": "toolBar(value: object | CustomBuilder)\n\n设置工具栏内容。不设置时不显示工具栏。items均分底部工具栏，在每个均分内容区布局文本和图标，文本超长时，逐级缩小，缩小之后换行，最后...截断。",
                "params": {
                    "value": {
                        "type": ["object", "CustomBuilder"],
                        "required": True,
                        "description": "工具栏的内容。"
                    }
                }
            },
            "toolbarConfiguration": {
                "description": "设置工具栏内容。不设置时不显示工具栏。",
                "params": {
                    "value": {
                        "type": ["Array<ToolbarItem>", "CustomBuilder"],
                        "required": True,
                        "description": "工具栏内容。"
                    },
                    "options": {
                        "type": "NavigationToolbarOptions",
                        "required": False,
                        "description": "工具栏选项。"
                    }
                }
            },
            "hideToolBar": {
                "description": "hideToolBar(value: boolean)\n\n设置是否隐藏工具栏。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否隐藏工具栏。",
                        "default": False
                    }
                }
            },
            "hideTitleBar": {
                "description": "hideTitleBar(value: boolean)\n\n设置是否隐藏标题栏。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否隐藏标题栏。",
                        "default": False
                    }
                }
            },
            "hideBackButton": {
                "description": "hideBackButton(value: boolean)\n\n设置是否隐藏标题栏中的返回键。返回键仅针对[titleMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-navigation-V5#titlemode)为NavigationTitleMode.Mini时才生效。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否隐藏标题栏中的返回键。",
                        "default": False
                    }
                }
            },
            "navBarWidth": {
                "description": "设置导航栏宽度。仅在Navigation组件分栏时生效。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "导航栏宽度。",
                        "default": 240
                    }
                }
            },
            "navBarPosition": {
                "description": "设置导航栏位置。仅在Navigation组件分栏时生效。",
                "params": {
                    "value": {
                        "type": "NavBarPosition",
                        "required": True,
                        "description": "导航栏位置。"
                    }
                }
            },
            "mode": {
                "description": "设置导航栏的显示模式。支持Stack、Split与Auto模式。",
                "params": {
                    "value": {
                        "type": "NavigationMode",
                        "required": True,
                        "description": "导航栏的显示模式。",
                        "default": "NavigationMode.Auto"
                    }
                }
            },
            "backButtonIcon": {
                "description": "设置标题栏中返回键图标。",
                "params": {
                    "value": {
                        "type": ["string", "PixelMap", "Resource", "SymbolGlyphModifier"],
                        "required": True,
                        "description": "返回键图标。"
                    }
                }
            },
            "hideNavBar": {
                "description": "设置是否隐藏导航栏。设置为true时，隐藏Navigation的导航栏，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否隐藏导航栏。",
                        "default": False
                    }
                }
            },
            "navDestination": {
                "description": "创建NavDestination组件。使用builder函数，基于name和param构造NavDestination组件。builder下只能有一个根节点。builder中允许在NavDestination组件外包含一层自定义组件， 但自定义组件不允许设置属性和事件，否则仅显示空白。",
                "params": {
                    "builder": {
                        "type": {
                            "name": "string",
                            "param": "unknown"
                        },
                        "required": True,
                        "description": "创建NavDestination组件。"
                    }
                }
            },
            "navBarWidthRange": {
                "description": "设置导航栏最小和最大宽度（双栏模式下生效）。",
                "params": {
                    "value": {
                        "type": ["Dimension", "Dimension"],
                        "required": True,
                        "description": "导航栏最小和最大宽度。",
                        "default": [240, "组件宽度的40%"]
                    }
                }
            },
            "minContentWidth": {
                "description": "设置导航栏内容区最小宽度（双栏模式下生效）。",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "导航栏内容区最小宽度。",
                        "default": 360
                    }
                }
            },
            "ignoreLayoutSafeArea": {
                "description": "控制组件的布局，使其扩展到非安全区域。",
                "params": {
                    "types": {
                        "type": "Array<LayoutSafeAreaType>",
                        "required": False,
                        "description": "配置扩展安全区域的类型。",
                        "default": ["LayoutSafeAreaType.SYSTEM"]
                    },
                    "edges": {
                        "type": "Array<LayoutSafeAreaEdge>",
                        "required": False,
                        "description": "配置扩展安全区域的方向。",
                        "default": ["LayoutSafeAreaEdge.TOP", "LayoutSafeAreaEdge.BOTTOM"]
                    }
                }
            },
            "systemBarStyle": {
                "description": "当Navigation中显示Navigation首页时，设置对应系统状态栏的样式。",
                "params": {
                    "style": {
                        "type": "Optional<SystemBarStyle>",
                        "required": True,
                        "description": "系统状态栏的样式。"
                    }
                }
            }
        },
        "events": {
            "onTitleModeChange": {
                "description": "onTitleModeChange(callback: (titleMode: NavigationTitleMode) => void)\n\n当[titleMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-navigation-V5#titlemode)为NavigationTitleMode.Free时，随着可滚动组件的滑动标题栏模式发生变化时触发此回调。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "标题栏模式变化时的回调函数。"
                    }
                }
            },
            "onNavBarStateChange": {
                "description": "onNavBarStateChange(callback: (isVisible: boolean) => void)\n\n导航栏显示状态切换时触发该回调。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "导航栏显示状态切换时的回调函数。"
                    }
                }
            },
            "onNavigationModeChange": {
                "description": "onNavigationModeChange(callback: (mode: NavigationMode) => void)\n\n当Navigation首次显示或者单双栏状态发生变化时触发该回调。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "单双栏状态变化时的回调函数。"
                    }
                }
            },
            "customNavContentTransition": {
                "description": "customNavContentTransition(delegate(from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined)\n\n自定义转场动画回调。",
                "params": {
                    "delegate": {
                        "type": "function",
                        "required": True,
                        "description": "自定义转场动画的回调函数。"
                    }
                }
            }
        },
        "examples": [
            """// NavigationExample.ets\n\n/**\n * NavigationExample struct represents a navigation page layout.\n * It includes a title, menus, search input, list of items, and toolbar configuration.\n */\n@Entry\n@Component\nstruct NavigationExample {\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n  @State currentIndex: number = 0\n\n  /**\n   * NavigationTitle builder function creates the title section of the navigation.\n   * It includes a main title and a subtitle.\n   */\n  @Builder NavigationTitle() {\n    Column() {\n      Text('Title')\n        .fontColor('#182431')\n        .fontSize(30)\n        .lineHeight(41)\n        .fontWeight(700)\n      Text('subtitle')\n        .fontColor('#182431')\n        .fontSize(14)\n        .lineHeight(19)\n        .opacity(0.4)\n        .margin({ top: 2, bottom: 20 })\n    }.alignItems(HorizontalAlign.Start)\n  }\n\n  /**\n   * NavigationMenus builder function creates the menu section of the navigation.\n   * It includes three images for menu options.\n   */\n  @Builder NavigationMenus() {\n    Row() {\n      Image('resources/base/media/ic_public_add.svg')\n        .width(24)\n        .height(24)\n      Image('resources/base/media/ic_public_add.svg')\n        .width(24)\n        .height(24)\n        .margin({ left: 24 })\n      Image('common/ic_public_more.svg')\n        .width(24)\n        .height(24)\n        .margin({ left: 24 })\n    }\n  }\n\n  /**\n   * build function constructs the overall layout of the navigation page.\n   * It includes search input, list of items, toolbar configuration, and title/menus settings.\n   */\n  build() {\n    Column() {\n      Navigation() {\n        TextInput({ placeholder: 'search...' })\n          .width('90%')\n          .height(40)\n          .backgroundColor('#FFFFFF')\n          .margin({ top: 8 })\n\n        List({ space: 12, initialIndex: 0 }) {\n          ForEach(this.arr, (item: number) => {\n            ListItem() {\n              Text('' + item)\n                .width('90%')\n                .height(72)\n                .backgroundColor('#FFFFFF')\n                .borderRadius(24)\n                .fontSize(16)\n                .fontWeight(500)\n                .textAlign(TextAlign.Center)\n            }\n          }, (item: number) => item.toString())\n        }\n        .height(324)\n        .width('100%')\n        .margin({ top: 12, left: '10%' })\n      }\n      .title(this.NavigationTitle)\n      .menus(this.NavigationMenus)\n      .titleMode(NavigationTitleMode.Full)\n      .toolbarConfiguration([\n        {\n          value: $r("app.string.navigation_toolbar_add"),\n          icon: $r("app.media.ic_public_highlightsed")\n        },\n        {\n          value: $r("app.string.navigation_toolbar_app"),\n          icon: $r("app.media.ic_public_highlights")\n        },\n        {\n          value: $r("app.string.navigation_toolbar_collect"),\n          icon: $r("app.media.ic_public_highlights")\n        }\n      ])\n      .hideTitleBar(false)\n      .hideToolBar(false)\n      .onTitleModeChange((titleModel: NavigationTitleMode) => {\n        console.info('titleMode' + titleModel)\n      })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}\n```\n// xxx.ets\nclass A {\n  text: string = ''\n  num: number = 0\n}\n\n@Entry\n@Component\nstruct NavigationExample {\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n  @State currentIndex: number = 0\n\n  @Builder NavigationTitle() {\n    Column() {\n      Text('Title')\n        .fontColor('#182431')\n        .fontSize(30)\n        .lineHeight(41)\n        .fontWeight(700)\n      Text('subtitle')\n        .fontColor('#182431')\n        .fontSize(14)\n        .lineHeight(19)\n        .opacity(0.4)\n        .margin({ top: 2, bottom: 20 })\n    }.alignItems(HorizontalAlign.Start)\n  }\n\n  @Builder NavigationMenus() {\n    Row() {\n      Image('resources/base/media/ic_public_add.svg')\n        .width(24)\n        .height(24)\n      Image('resources/base/media/ic_public_add.svg')\n        .width(24)\n        .height(24)\n        .margin({ left: 24 })\n      Image('common/ic_public_more.svg')\n        .width(24)\n        .height(24)\n        .margin({ left: 24 })\n    }\n  }\n\n  build() {\n    Column() {\n      Navigation() {\n        TextInput({ placeholder: 'search...' })\n          .width('90%')\n          .height(40)\n          .backgroundColor('#FFFFFF')\n          .margin({ top: 8 })\n\n        List({ space: 12, initialIndex: 0 }) {\n          ForEach(this.arr, (item: number) => {\n            ListItem() {\n              Text('' + item)\n                .width('90%')\n                .height(72)\n                .backgroundColor('#FFFFFF')\n                .borderRadius(24)\n                .fontSize(16)\n                .fontWeight(500)\n                .textAlign(TextAlign.Center)\n            }\n          }, (item: number) => item.toString())\n        }\n        .height(324)\n        .width('100%')\n        .margin({ top: 12, left: '10%' })\n      }\n      .title(this.NavigationTitle)\n      .menus(this.NavigationMenus)\n      .titleMode(NavigationTitleMode.Full)\n      .toolbarConfiguration([\n        {\n          value: $r("app.string.navigation_toolbar_add"),\n          icon: $r("app.media.ic_public_highlightsed")\n        },\n        {\n          value: $r("app.string.navigation_toolbar_app"),\n          icon: $r("app.media.ic_public_highlights")\n        },\n        {\n          value: $r("app.string.navigation_toolbar_collect"),\n          icon: $r("app.media.ic_public_highlights")\n        }\n      ])\n      .hideTitleBar(false)\n      .hideToolBar(false)\n      .onTitleModeChange((titleModel: NavigationTitleMode) => {\n        console.info('titleMode' + titleModel)\n      })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            """// Index.ets\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfos: NavPathStack = new NavPathStack()\n  isUseInterception: boolean = false;\n\n  // 注册拦截器，用于拦截路由跳转并进行相应处理\n  registerInterception() {\n    this.pageInfos.setInterception({\n      // 当即将显示目标页面时的拦截处理\n      willShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",\n                 operation: NavigationOperation, animated: boolean) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        if (typeof to === "string") {\n          console.log("target page is navigation home");\n          return;\n        }\n        // 重定向目标页面，将pageTwo替换为pageOne\n        let target: NavDestinationContext = to as NavDestinationContext;\n        if (target.pathInfo.name === 'pageTwo') {\n          target.pathStack.pop();\n          target.pathStack.pushPathByName('pageOne', null);\n        }\n      },\n      // 当页面显示完成后的拦截处理\n      didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",\n                operation: NavigationOperation, isAnimated: boolean) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        if (typeof from === "string") {\n          console.log("current transition is from navigation home");\n        } else {\n          console.log(`current transition is from  ${(from as NavDestinationContext).pathInfo.name}`)\n        }\n        if (typeof to === "string") {\n          console.log("current transition to is navBar");\n        } else {\n          console.log(`current transition is to ${(to as NavDestinationContext).pathInfo.name}`);\n        }\n      },\n      // 当导航模式改变时的拦截处理\n      modeChange: (mode: NavigationMode) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        console.log(`current navigation mode is ${mode}`);\n      }\n    })\n  }\n\n  // 构建页面结构\n  build() {\n    Navigation(this.pageInfos) {\n      Column() {\n        // 创建一个按钮，用于将页面信息入栈\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.pageInfos.pushPath({ name: 'pageOne' }) //将name指定的NavDestination页面信息入栈\n          })\n        // 创建一个按钮，用于开启或关闭拦截器\n        Button('use interception', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.isUseInterception = !this.isUseInterception;\n            if (this.isUseInterception) {\n              this.registerInterception();\n            } else {\n              this.pageInfos.setInterception(undefined);\n            }\n          })\n      }\n    }.title('NavIndex')\n  }\n}\n```\n// Index.ets\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfos: NavPathStack = new NavPathStack()\n  isUseInterception: boolean = false;\n\n  registerInterception() {\n    this.pageInfos.setInterception({\n      willShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",\n                 operation: NavigationOperation, animated: boolean) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        if (typeof to === "string") {\n          console.log("target page is navigation home");\n          return;\n        }\n        // redirect target page.Change pageTwo to pageOne.\n        let target: NavDestinationContext = to as NavDestinationContext;\n        if (target.pathInfo.name === 'pageTwo') {\n          target.pathStack.pop();\n          target.pathStack.pushPathByName('pageOne', null);\n        }\n      },\n      didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",\n                operation: NavigationOperation, isAnimated: boolean) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        if (typeof from === "string") {\n          console.log("current transition is from navigation home");\n        } else {\n          console.log(`current transition is from  ${(from as NavDestinationContext).pathInfo.name}`)\n        }\n        if (typeof to === "string") {\n          console.log("current transition to is navBar");\n        } else {\n          console.log(`current transition is to ${(to as NavDestinationContext).pathInfo.name}`);\n        }\n      },\n      modeChange: (mode: NavigationMode) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        console.log(`current navigation mode is ${mode}`);\n      }\n    })\n  }\n\n  build() {\n    Navigation(this.pageInfos) {\n      Column() {\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.pageInfos.pushPath({ name: 'pageOne' }) //将name指定的NavDestination页面信息入栈\n          })\n        Button('use interception', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.isUseInterception = !this.isUseInterception;\n            if (this.isUseInterception) {\n              this.registerInterception();\n            } else {\n              this.pageInfos.setInterception(undefined);\n            }\n          })\n      }\n    }.title('NavIndex')\n  }\n}"""
            """// Index.ets\n\n// 该示例主要演示设置每个NavDestination子页面的自定义转场动画及可交互转场动画。\n\nimport { CustomTransition, AnimateCallback } from './CustomNavigationUtils'\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfos: NavPathStack = new NavPathStack();\n\n  // 当页面即将出现时触发的方法\n  aboutToAppear() {\n    if (this.pageInfos === undefined) {\n      this.pageInfos = new NavPathStack();\n    }\n    // 将页面信息添加到页面信息栈中\n    this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });\n  }\n\n  // 构建导航页面\n  build() {\n    Navigation(this.pageInfos) {\n    }\n    .title('NavIndex')\n    .hideNavBar(true)\n    // 设置自定义导航内容转场动画\n    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {\n      if (from.mode == NavDestinationMode.DIALOG || to.mode == NavDestinationMode.DIALOG) {\n        return undefined;\n      }\n\n      // 首页不进行自定义动画\n      if (from.index === -1 || to.index === -1) {\n        return undefined;\n      }\n\n      CustomTransition.getInstance().operation = operation;\n      if (CustomTransition.getInstance().interactive) {\n        // 创建可交互的自定义动画\n        let customAnimation: NavigationAnimatedTransition = {\n          onTransitionEnd: (isSuccess: boolean) => {\n            console.log("===== current transition is " + isSuccess);\n            CustomTransition.getInstance().recoverState();\n            CustomTransition.getInstance().proxy = undefined;\n          },\n          transition: (transitionProxy: NavigationTransitionProxy) => {\n            CustomTransition.getInstance().proxy = transitionProxy;\n            let targetIndex: string | undefined = operation == NavigationOperation.PUSH ?\n              (to.navDestinationId) : (from.navDestinationId);\n            if (targetIndex) {\n              CustomTransition.getInstance().fireInteractiveAnimation(targetIndex, operation);\n            }\n          },\n          isInteractive: CustomTransition.getInstance().interactive\n        }\n        return customAnimation;\n      } else {\n        // 创建非交互的自定义动画\n        let customAnimation: NavigationAnimatedTransition = {\n          onTransitionEnd: (isSuccess: boolean)=>{\n            console.log(`current transition result is ${isSuccess}`)\n          },\n          timeout: 7000,\n          transition: (transitionProxy: NavigationTransitionProxy) => {\n            if (!from.navDestinationId || !to.navDestinationId) {\n              return;\n            }\n            // 获取转场动画回调参数\n            let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);\n            let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);\n            if (operation == NavigationOperation.PUSH) {\n              if (toParam.start) {\n                toParam.start(true, false);\n              }\n              animateTo({\n                duration: 500, onFinish: () => {\n                  transitionProxy.finishTransition();\n                }\n              }, () => {\n                if (toParam.finish) {\n                  toParam.finish(true, false);\n                }\n              })\n            } else {\n              if (fromParam.start) {\n                fromParam.start(true, true);\n              }\n              animateTo({\n                duration: 500, onFinish: () => {\n                  transitionProxy.finishTransition();\n                }\n              }, () => {\n                if (fromParam.finish) {\n                  fromParam.finish(true, true);\n                }\n              })\n            }\n          }\n        };\n        return customAnimation;\n      }\n    })\n  }\n}\n```\n\n这段代码实现了为每个NavDestination子页面设置自定义转场动画及可交互转场动画的功能。具体包括：\n1. 在页面即将出现时，将页面信息添加到页面信息栈中。\n2. 构建导航页面，并设置自定义导航内容转场动画。\n3. 根据不同情况，创建可交互的自定义动画或非交互的自定义动画。\n4. 在转场过程中，根据操作类型执行相应的动画操作，包括开始动画、结束动画等。\n// Index.ets\nimport { CustomTransition, AnimateCallback } from './CustomNavigationUtils'\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfos: NavPathStack = new NavPathStack();\n\n  aboutToAppear() {\n    if (this.pageInfos === undefined) {\n      this.pageInfos = new NavPathStack();\n    }\n    this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });\n  }\n\n  build() {\n    Navigation(this.pageInfos) {\n    }\n    .title('NavIndex')\n    .hideNavBar(true)\n    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {\n      if (from.mode == NavDestinationMode.DIALOG || to.mode == NavDestinationMode.DIALOG) {\n        return undefined;\n      }\n\n      // 首页不进行自定义动画\n      if (from.index === -1 || to.index === -1) {\n        return undefined;\n      }\n\n      CustomTransition.getInstance().operation = operation;\n      if (CustomTransition.getInstance().interactive) {\n        let customAnimation: NavigationAnimatedTransition = {\n          onTransitionEnd: (isSuccess: boolean) => {\n            console.log("===== current transition is " + isSuccess);\n            CustomTransition.getInstance().recoverState();\n            CustomTransition.getInstance().proxy = undefined;\n          },\n          transition: (transitionProxy: NavigationTransitionProxy) => {\n            CustomTransition.getInstance().proxy = transitionProxy;\n            let targetIndex: string | undefined = operation == NavigationOperation.PUSH ?\n              (to.navDestinationId) : (from.navDestinationId);\n            if (targetIndex) {\n              CustomTransition.getInstance().fireInteractiveAnimation(targetIndex, operation);\n            }\n          },\n          isInteractive: CustomTransition.getInstance().interactive\n        }\n        return customAnimation;\n      }\n      let customAnimation: NavigationAnimatedTransition = {\n        onTransitionEnd: (isSuccess: boolean)=>{\n          console.log(`current transition result is ${isSuccess}`)\n        },\n        timeout: 7000,\n        // 转场开始时系统调用该方法，并传入转场上下文代理对象\n        transition: (transitionProxy: NavigationTransitionProxy) => {\n          if (!from.navDestinationId || !to.navDestinationId) {\n            return;\n          }\n          // 从封装类CustomTransition中根据子页面的序列获取对应的转场动画回调\n          let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);\n          let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);\n          if (operation == NavigationOperation.PUSH) {\n            if (toParam.start) {\n              toParam.start(true, false);\n            }\n            animateTo({\n              duration: 500, onFinish: () => {\n                transitionProxy.finishTransition();\n              }\n            }, () => {\n              if (toParam.finish) {\n                toParam.finish(true, false);\n              }\n            })\n          } else {\n            if (fromParam.start) {\n              fromParam.start(true, true);\n            }\n            animateTo({\n              duration: 500, onFinish: () => {\n                transitionProxy.finishTransition();\n              }\n            }, () => {\n              if (fromParam.finish) {\n                fromParam.finish(true, true);\n              }\n            })\n          }\n        }\n      };\n      return customAnimation;\n    })\n  }\n}"""
            """// Index.ets\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfo: NavPathStack = new NavPathStack()\n\n  build() {\n    // 创建一个Navigation组件，用于管理页面导航\n    Navigation(this.pageInfo) {\n      // 创建一个垂直布局Column\n      Column() {\n        // 创建一个带有特定样式的按钮，点击后将页面信息入栈\n        Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%') // 设置按钮宽度为80%\n          .height(40) // 设置按钮高度为40\n          .margin(20) // 设置按钮外边距为20\n          .onClick(() => {\n            this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。\n          })\n      }\n    }.title('NavIndex') // 设置Navigation的标题为'NavIndex'\n  }\n}\n```\n\n在上述示例代码中：\n- `NavigationExample` 结构体包含了一个 `pageInfo` 变量，用于管理页面导航信息。\n- `build` 方法用于构建页面内容。\n- `Navigation` 组件用于管理页面导航，传入了 `pageInfo` 变量。\n- `Column` 组件用于创建垂直布局。\n- `Button` 组件创建一个特定样式的按钮，点击按钮后执行指定操作。\n- `width`、`height`、`margin` 方法分别设置按钮的宽度、高度和外边距。\n- `onClick` 方法设置按钮点击事件，将指定页面信息入栈。\n- `title` 方法设置 Navigation 的标题为 'NavIndex'。\n// Index.ets\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfo: NavPathStack = new NavPathStack()\n\n  build() {\n    Navigation(this.pageInfo) {\n      Column() {\n        Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。\n          })\n      }\n    }.title('NavIndex')\n  }\n}。"""
            """// 该示例主要演示设置Navigation主页的标题栏、工具栏和NavDestination页面的标题栏的背景颜色和背景模糊效果。\n\n// 定义两种背景颜色和两种背景模糊效果\nlet COLOR1: string = "#80004AAF"; // 第一种背景颜色\nlet COLOR2: string = "#802787D9"; // 第二种背景颜色\nlet BLUR_STYLE_1: BlurStyle = BlurStyle.BACKGROUND_THIN; // 第一种背景模糊效果\nlet BLUR_STYLE_2: BlurStyle = BlurStyle.BACKGROUND_THICK; // 第二种背景模糊效果\n\n// BackComponent组件，用于创建背景颜色块\n@Component\nstruct BackComponent {\n  build() {\n    Row() {\n      Column() {}\n      .height('100%')\n      .backgroundColor("#3D9DB4")\n      .layoutWeight(9)\n      Column() {}\n      .height('100%')\n      .backgroundColor("17A98D")\n      .layoutWeight(9)\n      Column() {}\n      .height('100%')\n      .backgroundColor("FFC000")\n      .layoutWeight(9)\n    }\n    .height('100%')\n    .width('100%')\n  }\n}\n\n// ColorAndBlur组件，用于切换背景颜色和背景模糊效果\n@Component\nstruct ColorAndBlur {\n  @State useColor1: boolean = true; // 控制是否使用第一种背景颜色\n  @State useBlur1: boolean = true; // 控制是否使用第一种背景模糊效果\n\n  build() {\n    NavDestination() {\n      Stack({alignContent: Alignment.Center}) {\n        BackComponent()\n          .width('100%')\n          .height('100%')\n        Column() {\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch color")\n              .onClick(() => {\n                this.useColor1 = !this.useColor1; // 切换背景颜色\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch blur")\n              .onClick(() => {\n                this.useBlur1 = !this.useBlur1; // 切换背景模糊效果\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n        }\n        .width('100%')\n        .height('100%')\n      }.width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    // 设置标题栏的背景颜色和背景模糊效果\n    .title("switch titlebar color and blur", {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,\n      barStyle: BarStyle.STACK\n    })\n  }\n}\n\n// Index组件，作为入口组件，展示导航、工具栏以及页面切换\n@Entry\n@Component\nstruct Index {\n  private stack: NavPathStack = new NavPathStack();\n  @State useColor1: boolean = true; // 控制是否使用第一种背景颜色\n  @State useBlur1: boolean = true; // 控制是否使用第一种背景模糊效果\n\n  @Builder\n  PageBuilder(name: string) {\n    ColorAndBlur()\n  }\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        BackComponent()\n          .width('100%')\n          .height('100%')\n        Column() {\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch color")\n              .onClick(() => {\n                this.useColor1 = !this.useColor1; // 切换背景颜色\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch blur")\n              .onClick(() => {\n                this.useBlur1 = !this.useBlur1; // 切换背景模糊效果\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("push page")\n              .onClick(() => {\n                this.stack.pushPath({name: "page"}); // 页面切换\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n        }\n        .width('100%')\n        .height('80%')\n      }.width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .navDestination(this.PageBuilder)\n    // 设置标题栏的背景颜色和背景模糊效果\n    .title("NavTitle", {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,\n      barStyle: BarStyle.STACK\n    })\n    // 设置工具栏的背景颜色和背景模糊效果\n    .toolbarConfiguration([\n      {value: "a"},\n      {value: "b"},\n      {value: "c"}\n    ], {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2\n    })\n  }\n}\n```\nlet COLOR1: string = "#80004AAF";\nlet COLOR2: string = "#802787D9";\nlet BLUR_STYLE_1: BlurStyle = BlurStyle.BACKGROUND_THIN;\nlet BLUR_STYLE_2: BlurStyle = BlurStyle.BACKGROUND_THICK;\n\n@Component\nstruct BackComponent {\n  build() {\n    Row() {\n      Column() {}\n      .height('100%')\n      .backgroundColor("#3D9DB4")\n      .layoutWeight(9)\n      Column() {}\n      .height('100%')\n      .backgroundColor("17A98D")\n      .layoutWeight(9)\n      Column() {}\n      .height('100%')\n      .backgroundColor("FFC000")\n      .layoutWeight(9)\n    }\n    .height('100%')\n    .width('100%')\n  }\n}\n\n@Component\nstruct ColorAndBlur {\n  @State useColor1: boolean = true;\n  @State useBlur1: boolean = true;\n\n  build() {\n    NavDestination() {\n      Stack({alignContent: Alignment.Center}) {\n        BackComponent()\n          .width('100%')\n          .height('100%')\n        Column() {\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch color")\n              .onClick(() => {\n                this.useColor1 = !this.useColor1;\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch blur")\n              .onClick(() => {\n                this.useBlur1 = !this.useBlur1;\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n        }\n        .width('100%')\n        .height('100%')\n      }.width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    // 开发者可以设置标题栏的背景颜色和背景模糊效果\n    .title("switch titlebar color and blur", {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,\n      barStyle: BarStyle.STACK\n    })\n  }\n}\n\n@Entry\n@Component\nstruct Index {\n  private stack: NavPathStack = new NavPathStack();\n  @State useColor1: boolean = true;\n  @State useBlur1: boolean = true;\n\n  @Builder\n  PageBuilder(name: string) {\n    ColorAndBlur()\n  }\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        BackComponent()\n          .width('100%')\n          .height('100%')\n        Column() {\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch color")\n              .onClick(() => {\n                this.useColor1 = !this.useColor1;\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch blur")\n              .onClick(() => {\n                this.useBlur1 = !this.useBlur1;\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("push page")\n              .onClick(() => {\n                this.stack.pushPath({name: "page"})\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n        }\n        .width('100%')\n        .height('80%')\n      }.width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .navDestination(this.PageBuilder)\n    // 开发者可以设置标题栏的背景颜色和背景模糊效果\n    .title("NavTitle", {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,\n      barStyle: BarStyle.STACK\n    })\n    // 开发者可以设置工具栏的背景颜色和背景模糊效果\n    .toolbarConfiguration([\n      {value: "a"},\n      {value: "b"},\n      {value: "c"}\n    ], {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2\n    })\n  }\n}"""
            """@Entry\n@Component\nstruct NavigationExample1 {\n  @State childNavStack: NavPathStack = new NavPathStack();\n\n  build() {\n    Navigation() {\n      Stack({alignContent: Alignment.Center}) {\n        // 在嵌套Navigation场景下创建子Navigation，并演示如何获取父NavPathStack\n        Navigation(this.childNavStack) {\n          Button('push Path to parent Navigation', { stateEffect: true, type: ButtonType.Capsule })\n            .width('80%')\n            .height(40)\n            .margin(20)\n            .onClick(() => {\n              // 点击按钮时获取父NavPathStack，并向其推送新的路径\n              let parentStack = this.childNavStack.getParent();\n              parentStack?.pushPath({ name: "pageOne"})\n            })\n        }\n        .clip(true)\n        .backgroundColor(Color.Orange)\n        .width('80%')\n        .height('80%')\n        .title('ChildNavigation')\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .backgroundColor(Color.Green)\n    .width('100%')\n    .height('100%')\n    .title('ParentNavigation')\n  }\n}\n```\n\n在上述示例代码中：\n- 创建了一个嵌套Navigation场景，包含父导航和子导航。\n- 子导航使用了传入的childNavStack作为导航栈。\n- 通过按钮的点击事件演示了如何获取父导航的NavPathStack，并向其推送新的路径。\n- 父导航的背景色为绿色，宽高为100%，标题为'ParentNavigation'。\n- 子导航的背景色为橙色，宽高为80%，标题为'ChildNavigation'。\n@Entry\n@Component\nstruct NavigationExample1 {\n  @State childNavStack: NavPathStack = new NavPathStack();\n\n  build() {\n    Navigation() {\n      Stack({alignContent: Alignment.Center}) {\n        Navigation(this.childNavStack) {\n          Button('push Path to parent Navigation', { stateEffect: true, type: ButtonType.Capsule })\n            .width('80%')\n            .height(40)\n            .margin(20)\n            .onClick(() => {\n              // 可以获取父NavPathStack\n              let parentStack = this.childNavStack.getParent();\n              parentStack?.pushPath({ name: "pageOne"})\n            })\n        }\n        .clip(true)\n        .backgroundColor(Color.Orange)\n        .width('80%')\n        .height('80%')\n        .title('ChildNavigation')\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .backgroundColor(Color.Green)\n    .width('100%')\n    .height('100%')\n    .title('ParentNavigation')\n  }\n}"""
            """// NavPathStack无需声明为状态变量，也可以实现页面栈操作功能。\n// NavDestination通过onReady事件能够拿到对应的NavPathInfo和所属的NavPathStack。\n\n// PageParam类用于存储页面参数\nclass PageParam {\n  constructor(num_: number) {\n    this.num = num_;\n  }\n  num: number = 0;\n}\n\n// PageOneBuilder函数用于构建页面One\n@Builder\nexport function PageOneBuilder(name: string, param: Object) {\n  PageOne()\n}\n\n// PageOne组件用于展示页面One的内容和操作按钮\n@Component\nstruct PageOne {\n  private stack: NavPathStack | null = null; // 页面所属的页面栈\n  private name: string = ""; // 页面名称\n  private paramNum: number = 0; // 页面参数\n\n  build() {\n    NavDestination() {\n      Column() {\n        Text("NavPathInfo: name: " + this.name + ", paramNum: " + this.paramNum) // 显示页面信息\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule }) // 按钮用于推入新页面\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            if (this.stack) {\n              let p = new PageParam(this.paramNum + 1);\n              this.stack.pushPath({name: "pageOne", param: p}); // 推入新页面\n            }\n          })\n        Button('pop', { stateEffect: true, type: ButtonType.Capsule }) // 按钮用于弹出当前页面\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack?.pop(); // 弹出当前页面\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .title('pageOne')\n    .onReady((ctx: NavDestinationContext) => {\n      // 在NavDestination中能够拿到传来的NavPathInfo和当前所处的NavPathStack\n      try {\n        this.name = ctx?.pathInfo?.name; // 获取页面名称\n        this.paramNum = (ctx?.pathInfo?.param as PageParam)?.num; // 获取页面参数\n        this.stack = ctx.pathStack; // 获取页面所属的页面栈\n      } catch (e) {\n        console.log(`testTag onReady catch exception: ${JSON.stringify(e)}`)\n      }\n    })\n  }\n}\n\n// NavigationExample2组件用于展示导航示例2的内容和操作按钮\n@Entry\n@Component\nstruct NavigationExample2 {\n  private stack : NavPathStack = new NavPathStack(); // 创建一个页面栈\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule }) // 按钮用于推入新页面\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            let p = new PageParam(1);\n            this.stack.pushPath({ name: "pageOne", param: p }); // 推入新页面\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .title('Navigation')\n  }\n}\n\n// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}\n// route_map.json\n{\n  "routerMap": [\n    {\n      "name": "pageOne",\n      "pageSourceFile": "src/main/ets/pages/Index.ets",\n      "buildFunction": "PageOneBuilder",\n      "data": {\n        "description": "this is pageOne"\n      }\n    }\n  ]\n}\n```\nclass PageParam {\n  constructor(num_: number) {\n    this.num = num_;\n  }\n  num: number = 0;\n}\n\n@Builder\nexport function PageOneBuilder(name: string, param: Object) {\n  PageOne()\n}\n\n@Component\nstruct PageOne {\n  private stack: NavPathStack | null = null;\n  private name: string = "";\n  private paramNum: number = 0;\n\n  build() {\n    NavDestination() {\n      Column() {\n        Text("NavPathInfo: name: " + this.name + ", paramNum: " + this.paramNum)\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            if (this.stack) {\n              let p = new PageParam(this.paramNum + 1);\n              this.stack.pushPath({name: "pageOne", param: p});\n            }\n          })\n        Button('pop', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack?.pop()\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .title('pageOne')\n    .onReady((ctx: NavDestinationContext) => {\n      // 在NavDestination中能够拿到传来的NavPathInfo和当前所处的NavPathStack\n      try {\n        this.name = ctx?.pathInfo?.name;\n        this.paramNum = (ctx?.pathInfo?.param as PageParam)?.num;\n        this.stack = ctx.pathStack;\n      } catch (e) {\n        console.log(`testTag onReady catch exception: ${JSON.stringify(e)}`)\n      }\n    })\n  }\n}\n\n@Entry\n@Component\nstruct NavigationExample2 {\n  private stack : NavPathStack = new NavPathStack();\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            let p = new PageParam(1);\n            this.stack.pushPath({ name: "pageOne", param: p })\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .title('Navigation')\n  }\n}\n// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}\n// route_map.json\n{\n  "routerMap": [\n    {\n      "name": "pageOne",\n      "pageSourceFile": "src/main/ets/pages/Index.ets",\n      "buildFunction": "PageOneBuilder",\n      "data": {\n        "description": "this is pageOne"\n      }\n    }\n  ]\n}"""
            """// 该示例演示NavDestination的生命周期时序。\n\n// NavDestination表示导航目的地，包含了页面的生命周期方法和事件处理。\n// PageOneBuilder用于构建页面One的组件。\n@Builder\nexport function PageOneBuilder(name: string, param: Object) {\n  PageOneComponent()\n}\n\n// PageOneComponent是页面One的组件，包含了页面布局和生命周期方法的定义。\n@Component\nstruct PageOneComponent {\n  private stack: NavPathStack | null = null;\n  @State eventStr: string = "";\n\n  // build方法用于构建页面的UI布局和定义页面的生命周期方法。\n  build() {\n    NavDestination() {\n      Column() {\n        // 显示当前事件字符串\n        Text("event: " + this.eventStr)\n        \n        // 点击按钮，将页面One推入导航栈\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            if (this.stack) {\n              this.stack.pushPath({name: "pageOne"});\n            }\n          })\n        \n        // 点击按钮，将页面One从导航栈中弹出\n        Button('pop', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack?.pop()\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    // 设置页面标题为'pageOne'\n    .title('pageOne')\n    // 页面生命周期方法的定义\n    .onAppear(() => { this.eventStr += "<onAppear>"; })\n    .onDisAppear(() => { this.eventStr += "<onDisAppear>"; })\n    .onShown(() => { this.eventStr += "<onShown>"; })\n    .onHidden(() => { this.eventStr += "<onHidden>"; })\n    .onWillAppear(() => { this.eventStr += "<onWillAppear>"; })\n    .onWillDisappear(() => { this.eventStr += "<onWillDisappear>"; })\n    .onWillShow(() => { this.eventStr += "<onWillShow>"; })\n    .onWillHide(() => { this.eventStr += "<onWillHide>"; })\n    // onReady会在onAppear之前调用\n    .onReady((ctx: NavDestinationContext) => {\n      try {\n        this.eventStr += "<onReady>";\n        this.stack = ctx.pathStack;\n      } catch (e) {\n        console.log(`testTag onReady catch exception: ${JSON.stringify(e)}`)\n      }\n    })\n  }\n}\n\n// NavigationExample3是导航示例的入口组件，包含了导航栈的初始化和页面One的跳转按钮。\n@Entry\n@Component\nstruct NavigationExample3 {\n  private stack : NavPathStack = new NavPathStack();\n\n  // 构建导航示例的UI布局\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        // 点击按钮，将页面One推入导航栈\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack.pushPath({ name: "pageOne" })\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .title('Navigation')\n  }\n}\n\n// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}\n// route_map.json\n// 路由映射配置，指定页面One的信息\n{\n  "routerMap": [\n    {\n      "name": "pageOne",\n      "pageSourceFile": "src/main/ets/pages/Index.ets",\n      "buildFunction": "PageOneBuilder",\n      "data": {\n        "description": "this is pageOne"\n      }\n    }\n  ]\n}\n```\n@Builder\nexport function PageOneBuilder(name: string, param: Object) {\n  PageOneComponent()\n}\n\n@Component\nstruct PageOneComponent {\n  private stack: NavPathStack | null = null;\n  @State eventStr: string = "";\n\n  build() {\n    NavDestination() {\n      Column() {\n        Text("event: " + this.eventStr)\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            if (this.stack) {\n              this.stack.pushPath({name: "pageOne"});\n            }\n          })\n        Button('pop', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack?.pop()\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .title('pageOne')\n    .onAppear(() => { this.eventStr += "<onAppear>"; })\n    .onDisAppear(() => { this.eventStr += "<onDisAppear>"; })\n    .onShown(() => { this.eventStr += "<onShown>"; })\n    .onHidden(() => { this.eventStr += "<onHidden>"; })\n    .onWillAppear(() => { this.eventStr += "<onWillAppear>"; })\n    .onWillDisappear(() => { this.eventStr += "<onWillDisappear>"; })\n    .onWillShow(() => { this.eventStr += "<onWillShow>"; })\n    .onWillHide(() => { this.eventStr += "<onWillHide>"; })\n    // onReady会在onAppear之前调用\n    .onReady((ctx: NavDestinationContext) => {\n      try {\n        this.eventStr += "<onReady>";\n        this.stack = ctx.pathStack;\n      } catch (e) {\n        console.log(`testTag onReady catch exception: ${JSON.stringify(e)}`)\n      }\n    })\n  }\n}\n\n@Entry\n@Component\nstruct NavigationExample3 {\n  private stack : NavPathStack = new NavPathStack();\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack.pushPath({ name: "pageOne" })\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .title('Navigation')\n  }\n}\n// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}\n// route_map.json\n{\n  "routerMap": [\n    {\n      "name": "pageOne",\n      "pageSourceFile": "src/main/ets/pages/Index.ets",\n      "buildFunction": "PageOneBuilder",\n      "data": {\n        "description": "this is pageOne"\n      }\n    }\n  ]\n}"""
            """// 该示例演示Navigation标题栏STACK布局效果。\n\n@Entry\n@Component\nstruct NavigationExample {\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];\n  private scrollerForScroll: Scroller = new Scroller();\n  @State barStyle: BarStyle = BarStyle.STANDARD;\n\n  build() {\n    Column() {\n      Navigation() {\n        Column() {\n          // 在Navigation中嵌套Column，实现布局层叠效果\n          Scroll(this.scrollerForScroll) {\n            Column() {\n              Image($r('app.media.image_1'))\n                // 设置与标题栏高度一致，以便观察STACK效果\n                .height(138)\n                .width('100%')\n              Button('BarStyle.STANDARD')\n                .height('50vp')\n                .onClick(() => {\n                  this.barStyle = BarStyle.STANDARD;\n                })\n              Button('BarStyle.STACK')\n                .height('50vp')\n                .margin({ top: 12 })\n                .onClick(() => {\n                  this.barStyle = BarStyle.STACK;\n                })\n\n              // 遍历数组，创建带有数字的ListItem\n              ForEach(this.arr, (item: number) => {\n                ListItem() {\n                  Text('' + item)\n                    .width('100%')\n                    .height(100)\n                    .fontSize(16)\n                    .textAlign(TextAlign.Center)\n                    .borderRadius(10)\n                    .backgroundColor(Color.Orange)\n                    .margin({ top: 12 })\n                }\n              }, (item: string) => item)\n            }\n          }\n        }\n        .width('100%')\n        .height('100%')\n        .backgroundColor(0xDCDCDC)\n      }\n      // 设置Navigation的标题内容和样式\n      .title(\n        {\n          main: 'NavTitle',\n          sub: 'subtitle'\n        },\n        {\n          backgroundBlurStyle: BlurStyle.COMPONENT_THICK,\n          barStyle: this.barStyle,\n        }\n      )\n      .titleMode(NavigationTitleMode.Free)\n      .hideTitleBar(false)\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}\n```\n\n在上述代码中：\n- `NavigationExample` 结构体定义了一个示例，展示了Navigation标题栏的STACK布局效果。\n- `barStyle` 为状态变量，用于控制标题栏的样式，包括 `BarStyle.STANDARD` 和 `BarStyle.STACK` 两种样式。\n- `build()` 方法构建了页面布局，包括嵌套的 `Column`、`Navigation`、`Scroll` 等组件。\n- `Image` 显示图片，高度设置与标题栏高度一致，用于观察STACK效果。\n- `Button` 组件用于切换标题栏样式，分别为 `BarStyle.STANDARD` 和 `BarStyle.STACK`。\n- `ForEach` 遍历数组 `arr`，创建带有数字的 `ListItem`，展示不同数字的方块。\n- `Navigation` 设置了标题栏的样式和内容，包括主标题、副标题、背景模糊样式和标题栏样式。\n- `titleMode(NavigationTitleMode.Free)` 设置标题栏自由模式，不固定在顶部。\n- `hideTitleBar(false)` 显示标题栏。\n- 页面整体设置了背景颜色为 `#F1F3F5`。\n@Entry\n@Component\nstruct NavigationExample {\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];\n  private scrollerForScroll: Scroller = new Scroller();\n  @State barStyle: BarStyle = BarStyle.STANDARD;\n\n  build() {\n    Column() {\n      Navigation() {\n        Column() {\n          Scroll(this.scrollerForScroll) {\n            Column() {\n              Image($r('app.media.image_1'))\n                // 设置与标题栏高度一致，以便观察STACK效果\n                .height(138)\n                .width('100%')\n              Button('BarStyle.STANDARD')\n                .height('50vp')\n                .onClick(() => {\n                  this.barStyle = BarStyle.STANDARD;\n                })\n              Button('BarStyle.STACK')\n                .height('50vp')\n                .margin({ top: 12 })\n                .onClick(() => {\n                  this.barStyle = BarStyle.STACK;\n                })\n\n              ForEach(this.arr, (item: number) => {\n                ListItem() {\n                  Text('' + item)\n                    .width('100%')\n                    .height(100)\n                    .fontSize(16)\n                    .textAlign(TextAlign.Center)\n                    .borderRadius(10)\n                    .backgroundColor(Color.Orange)\n                    .margin({ top: 12 })\n                }\n              }, (item: string) => item)\n            }\n          }\n        }\n        .width('100%')\n        .height('100%')\n        .backgroundColor(0xDCDCDC)\n      }\n      .title(\n        {\n          main: 'NavTitle',\n          sub: 'subtitle'\n        },\n        {\n          backgroundBlurStyle: BlurStyle.COMPONENT_THICK,\n          barStyle: this.barStyle,\n        }\n      )\n      .titleMode(NavigationTitleMode.Free)\n      .hideTitleBar(false)\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            """// 该示例主要演示如何定义NavPathStack的派生类和派生类在Navigation中的基本用法。\n\n// 定义派生类DerivedNavPathStack，扩展自NavPathStack\nclass DerivedNavPathStack extends NavPathStack {\n  // 用户定义属性'id'，默认值为'__default__'\n  id: string = "__default__"\n\n  // 设置id属性的方法\n  setId(id: string) {\n    this.id = id;\n  }\n\n  // 获取信息的方法\n  getInfo(): string {\n    return "this page used Derived NavPathStack, id: " + this.id\n  }\n\n  // 重写NavPathStack的pushPath方法\n  pushPath(info: NavPathInfo, animated?: boolean): void\n  pushPath(info: NavPathInfo, options?: NavigationOptions): void\n  pushPath(info: NavPathInfo, secArg?: boolean | NavigationOptions): void {\n    console.log('[derive-test] reached DerivedNavPathStack's pushPath');\n    if (typeof secArg === 'boolean') {\n      super.pushPath(info, secArg);\n    } else {\n      super.pushPath(info, secArg);\n    }\n  }\n\n  // 重写和重载NavPathStack的pop方法\n  pop(animated?: boolean | undefined): NavPathInfo | undefined\n  pop(result: Object, animated?: boolean | undefined): NavPathInfo | undefined\n  pop(result?: Object, animated?: boolean | undefined): NavPathInfo | undefined {\n    console.log('[derive-test] reached DerivedNavPathStack's pop');\n    return super.pop(result, animated);\n  }\n\n  // 其他基类函数...\n}\n\n// 定义参数类param\nclass param {\n  info: string = "__default_param__";\n  constructor(info: string) { this.info = info }\n}\n\n// 入口组件Index\n@Entry\n@Component\nstruct Index {\n  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();\n\n  // 生命周期钩子函数，页面即将显示时调用\n  aboutToAppear(): void {\n    this.derivedStack.setId('origin stack');\n  }\n\n  // 构建页面映射\n  @Builder\n  pageMap(name: string) {\n    PageOne()\n  }\n\n  // 构建页面\n  build() {\n    Navigation(this.derivedStack) {\n      Button('to Page One').margin(20).onClick(() => {\n        this.derivedStack.pushPath({\n          name: 'pageOne',\n          param: new param('push pageOne in homePage when stack size: ' + this.derivedStack.size())\n        });\n      })\n    }.navDestination(this.pageMap)\n    .title('Home Page')\n  }\n}\n\n// 页面组件PageOne\n@Component\nstruct PageOne {\n  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();\n  curStringifyParam: string = "NA";\n\n  // 构建页面\n  build() {\n    NavDestination() {\n      Column() {\n        // 显示DerivedNavPathStack的信息\n        Text(this.derivedStack.getInfo())\n          .margin(10)\n          .fontSize(25)\n          .fontWeight(FontWeight.Bold)\n          .textAlign(TextAlign.Start)\n        Text('current page param info:')\n          .margin(10)\n          .fontSize(25)\n          .fontWeight(FontWeight.Bold)\n          .textAlign(TextAlign.Start)\n        Text(this.curStringifyParam)\n          .margin(20)\n          .fontSize(20)\n          .textAlign(TextAlign.Start)\n      }.backgroundColor(Color.Pink)\n      Button('to Page One').margin(20).onClick(() => {\n        this.derivedStack.pushPath({\n          name: 'pageOne',\n          param: new param('push pageOne in pageOne when stack size: ' + this.derivedStack.size())\n        });\n      })\n    }.title('Page One')\n    .onReady((context: NavDestinationContext) => {\n      console.log('[derive-test] reached PageOne's onReady');\n      // 从NavDestinationContext中获取DerivedNavPathStack\n      this.derivedStack = context.pathStack as DerivedNavPathStack;\n      console.log('[derive-test] -- got derivedStack: ' + this.derivedStack.id);\n      this.curStringifyParam = JSON.stringify(context.pathInfo.param);\n      console.log('[derive-test] -- got param: ' + this.curStringifyParam);\n    })\n  }\n}\n```\nclass DerivedNavPathStack extends NavPathStack {\n  // usr defined property 'id'\n  id: string = "__default__"\n\n  // new function in derived class\n  setId(id: string) {\n    this.id = id;\n  }\n\n  // new function in derived class\n  getInfo(): string {\n    return "this page used Derived NavPathStack, id: " + this.id\n  }\n\n  // overwrite function of NavPathStack\n  pushPath(info: NavPathInfo, animated?: boolean): void\n  pushPath(info: NavPathInfo, options?: NavigationOptions): void\n  pushPath(info: NavPathInfo, secArg?: boolean | NavigationOptions): void {\n    console.log('[derive-test] reached DerivedNavPathStack\\'s pushPath');\n    if (typeof secArg === 'boolean') {\n      super.pushPath(info, secArg);\n    } else {\n      super.pushPath(info, secArg);\n    }\n  }\n\n  // overwrite and overload function of NavPathStack\n  pop(animated?: boolean | undefined): NavPathInfo | undefined\n  pop(result: Object, animated?: boolean | undefined): NavPathInfo | undefined\n  pop(result?: Object, animated?: boolean | undefined): NavPathInfo | undefined {\n    console.log('[derive-test] reached DerivedNavPathStack\\'s pop');\n    return super.pop(result, animated);\n  }\n\n  // other function of base class...\n}\n\nclass param {\n  info: string = "__default_param__";\n  constructor(info: string) { this.info = info }\n}\n\n@Entry\n@Component\nstruct Index {\n  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();\n\n  aboutToAppear(): void {\n    this.derivedStack.setId('origin stack');\n  }\n\n  @Builder\n  pageMap(name: string) {\n    PageOne()\n  }\n\n  build() {\n    Navigation(this.derivedStack) {\n      Button('to Page One').margin(20).onClick(() => {\n        this.derivedStack.pushPath({\n          name: 'pageOne',\n          param: new param('push pageOne in homePage when stack size: ' + this.derivedStack.size())\n        });\n      })\n    }.navDestination(this.pageMap)\n    .title('Home Page')\n  }\n}\n\n@Component\nstruct PageOne {\n  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();\n  curStringifyParam: string = "NA";\n\n  build() {\n    NavDestination() {\n      Column() {\n        Text(this.derivedStack.getInfo())\n          .margin(10)\n          .fontSize(25)\n          .fontWeight(FontWeight.Bold)\n          .textAlign(TextAlign.Start)\n        Text('current page param info:')\n          .margin(10)\n          .fontSize(25)\n          .fontWeight(FontWeight.Bold)\n          .textAlign(TextAlign.Start)\n        Text(this.curStringifyParam)\n          .margin(20)\n          .fontSize(20)\n          .textAlign(TextAlign.Start)\n      }.backgroundColor(Color.Pink)\n      Button('to Page One').margin(20).onClick(() => {\n        this.derivedStack.pushPath({\n          name: 'pageOne',\n          param: new param('push pageOne in pageOne when stack size: ' + this.derivedStack.size())\n        });\n      })\n    }.title('Page One')\n    .onReady((context: NavDestinationContext) => {\n      console.log('[derive-test] reached PageOne\\'s onReady');\n      // get derived stack from navdestinationContext\n      this.derivedStack = context.pathStack as DerivedNavPathStack;\n      console.log('[derive-test] -- got derivedStack: ' + this.derivedStack.id);\n      this.curStringifyParam = JSON.stringify(context.pathInfo.param);\n      console.log('[derive-test] -- got param: ' + this.curStringifyParam);\n    })\n  }\n}"""
            """/**\n * 该示例主要演示Navigation和NavDestination如何使用Symbol组件。\n */\n\n@Entry\n@Component\nstruct NavigationExample {\n  // 定义导航路径栈和菜单项\n  @Provide('navPathStack') navPathStack:NavPathStack = new NavPathStack();\n  @State menuItems:Array<NavigationMenuItem> = [\n    {\n      value:'menuItem1',\n      icon:'resources/base/media/ic_public_ok.svg' // 图标资源路径\n    },\n    {\n      value:'menuItem2',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n    },\n    {\n      value:'menuItem3',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n    },\n  ]\n\n  // 定义工具栏项\n  @State toolItems:Array<ToolbarItem>= [\n    {\n      value:'toolItem1',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n      action:()=>{}\n    },\n    {\n      value:'toolItem2',\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeIcon: 'resources/base/media/ic_public_more.svg', // 图标资源路径\n      action:()=>{}\n    },\n    {\n      value:'toolItem3',\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n      action:()=>{}\n    }\n  ]\n\n  // 定义路由构建器\n  @Builder\n  myRouter(name:string,param?:Object) {\n    if(name === 'NavigationMenu') {\n      NavigationMenu();\n    }\n  }\n\n  // 构建导航页面\n  build() {\n    Navigation(this.navPathStack) {\n      Column() {\n        Button('跳转').onClick(()=> {\n          this.navPathStack.pushPathByName('NavigationMenu', null);\n        })\n      }\n    }\n    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))\n    .titleMode(NavigationTitleMode.Mini)\n    .menus(this.menuItems)\n    .toolbarConfiguration(this.toolItems)\n    .title('一级页面')\n    .navDestination(this.myRouter)\n  }\n}\n\n@Component\nexport struct NavigationMenu{\n  @Consume('navPathStack') navPathStack:NavPathStack;\n  @State menuItems:Array<NavigationMenuItem> = [\n    {\n      value:'menuItem1',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action:()=>{}\n    },\n    {\n      value:'menuItem2',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n      action:()=>{}\n    },\n    {\n      value:'menuItem3',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat_1')),\n      action:()=>{}\n    },\n  ]\n\n  // 构建导航目的地页面\n  build() {\n    NavDestination(){\n      Row() {\n        Column(){\n        }\n        .width('100%')\n      }\n      .height('100%')\n    }\n    .hideTitleBar(false)\n    .title('NavDestination title')\n    .backgroundColor($r('sys.color.ohos_id_color_titlebar_sub_bg'))\n    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Blue]))\n    .menus(this.menuItems)\n  }\n}\n```\nimport { SymbolGlyphModifier } from '@kit.ArkUI';\n\n@Entry\n@Component\nstruct NavigationExample {\n  @Provide('navPathStack') navPathStack:NavPathStack = new NavPathStack();\n  @State menuItems:Array<NavigationMenuItem> = [\n    {\n      value:'menuItem1',\n      icon:'resources/base/media/ic_public_ok.svg' // 图标资源路径\n    },\n    {\n      value:'menuItem2',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n    },\n    {\n      value:'menuItem3',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n    },\n  ]\n\n  @State toolItems:Array<ToolbarItem>= [\n    {\n      value:'toolItem1',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n      action:()=>{}\n    },\n    {\n      value:'toolItem2',\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeIcon: 'resources/base/media/ic_public_more.svg', // 图标资源路径\n      action:()=>{}\n    },\n    {\n      value:'toolItem3',\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n      action:()=>{}\n    }\n  ]\n\n  @Builder\n  myRouter(name:string,param?:Object) {\n    if(name === 'NavigationMenu') {\n      NavigationMenu();\n    }\n  }\n\n  build() {\n    Navigation(this.navPathStack) {\n      Column() {\n        Button('跳转').onClick(()=> {\n          this.navPathStack.pushPathByName('NavigationMenu', null);\n        })\n      }\n    }\n    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))\n    .titleMode(NavigationTitleMode.Mini)\n    .menus(this.menuItems)\n    .toolbarConfiguration(this.toolItems)\n    .title('一级页面')\n    .navDestination(this.myRouter)\n  }\n}\n\n@Component\nexport struct NavigationMenu{\n  @Consume('navPathStack') navPathStack:NavPathStack;\n  @State menuItems:Array<NavigationMenuItem> = [\n    {\n      value:'menuItem1',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action:()=>{}\n    },\n    {\n      value:'menuItem2',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n      action:()=>{}\n    },\n    {\n      value:'menuItem3',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat_1')),\n      action:()=>{}\n    },\n  ]\n\n  build() {\n    NavDestination(){\n      Row() {\n        Column(){\n        }\n        .width('100%')\n      }\n      .height('100%')\n    }\n    .hideTitleBar(false)\n    .title('NavDestination title')\n    .backgroundColor($r('sys.color.ohos_id_color_titlebar_sub_bg'))\n    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Blue]))\n    .menus(this.menuItems)\n  }\n}"""
            """/**\n * 该示例演示了如何自定义设置标题栏边距，包括Navigation和NavDestination两个组件。\n * 开发者可以通过按钮点击事件切换标题栏内间距的大小，并跳转到另一个页面查看效果。\n */\n\n// NavigationExample组件\n@Entry\n@Component\nstruct NavigationExample {\n  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();\n  // 初始化标题栏起始端内间距\n  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);\n  // 初始化标题栏结束端内间距\n  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);\n  @State menuItems: Array<NavigationMenuItem> = [\n    {\n      value: 'menuItem1',\n      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action: () => {\n      }\n    }\n  ]\n\n  @Builder\n  myRouter(name: string, param?: Object) {\n    if (name === 'NavDestinationExample') {\n      NavDestinationExample();\n    }\n  }\n\n  build() {\n    Navigation(this.navPathStack) {\n      Column() {\n        // 切换标题栏内间距为16vp的按钮\n        Button('切换标题栏内间距为16vp')\n          .onClick(() => {\n            this.paddingStart = LengthMetrics.vp(16);\n            this.paddingEnd = LengthMetrics.vp(16);\n          })\n          .margin({ top: 5 })\n\n        // 切换标题栏内间距为24vp的按钮\n        Button('切换标题栏内间距为24vp')\n          .onClick(() => {\n            this.paddingStart = LengthMetrics.vp(24);\n            this.paddingEnd = LengthMetrics.vp(24);\n          })\n          .margin({ top: 5 })\n\n        // 跳转按钮\n        Button('跳转')\n          .onClick(() => {\n            this.navPathStack.pushPathByName('NavDestinationExample', null);\n          })\n          .margin({ top: 5 })\n      }\n    }\n    .titleMode(NavigationTitleMode.Mini)\n    .title('一级页面', {\n      paddingStart: this.paddingStart,\n      paddingEnd: this.paddingEnd,\n    })\n    .menus(this.menuItems)\n    .navDestination(this.myRouter)\n  }\n}\n\n// NavDestinationExample组件\n@Component\nexport struct NavDestinationExample {\n  @Consume('navPathStack') navPathStack: NavPathStack;\n  @State menuItems: Array<NavigationMenuItem> = [\n    {\n      value: 'menuItem1',\n      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action: () => {\n      }\n    }\n  ]\n  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);\n  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);\n\n  build() {\n    NavDestination() {\n      Row() {\n        Column() {\n          // 切换标题栏内间距为32vp的按钮\n          Button('切换标题栏内间距为32vp')\n            .onClick(() => {\n              this.paddingStart = LengthMetrics.vp(32);\n              this.paddingEnd = LengthMetrics.vp(32);\n            })\n            .margin({ top: 5 })\n\n          // 切换标题栏内间距为20vp的按钮\n          Button('切换标题栏内间距为20vp')\n            .onClick(() => {\n              this.paddingStart = LengthMetrics.vp(20);\n              this.paddingEnd = LengthMetrics.vp(20);\n            })\n            .margin({ top: 5 })\n        }\n        .width('100%')\n      }\n      .height('100%')\n    }\n    .hideTitleBar(false)\n    .title('NavDestination title', {\n      paddingStart: this.paddingStart,\n      paddingEnd: this.paddingEnd,\n    })\n    .menus(this.menuItems)\n  }\n}\n```\nimport { LengthMetrics } from '@kit.ArkUI';\n\n@Entry\n@Component\nstruct NavigationExample {\n  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();\n  // 初始化标题栏起始端内间距\n  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);\n  // 初始化标题栏结束端内间距\n  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);\n  @State menuItems: Array<NavigationMenuItem> = [\n    {\n      value: 'menuItem1',\n      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action: () => {\n      }\n    }\n  ]\n\n  @Builder\n  myRouter(name: string, param?: Object) {\n    if (name === 'NavDestinationExample') {\n      NavDestinationExample();\n    }\n  }\n\n  build() {\n    Navigation(this.navPathStack) {\n      Column() {\n        // 标题栏内间距切换\n        Button('切换标题栏内间距为16vp')\n          .onClick(() => {\n            this.paddingStart = LengthMetrics.vp(16);\n            this.paddingEnd = LengthMetrics.vp(16);\n          })\n          .margin({ top: 5 })\n\n        Button('切换标题栏内间距为24vp')\n          .onClick(() => {\n            this.paddingStart = LengthMetrics.vp(24);\n            this.paddingEnd = LengthMetrics.vp(24);\n          })\n          .margin({ top: 5 })\n\n        Button('跳转')\n          .onClick(() => {\n            this.navPathStack.pushPathByName('NavDestinationExample', null);\n          })\n          .margin({ top: 5 })\n      }\n    }\n    .titleMode(NavigationTitleMode.Mini)\n    .title('一级页面', {\n      paddingStart: this.paddingStart,\n      paddingEnd: this.paddingEnd,\n    })\n    .menus(this.menuItems)\n    .navDestination(this.myRouter)\n  }\n}\n\n@Component\nexport struct NavDestinationExample {\n  @Consume('navPathStack') navPathStack: NavPathStack;\n  @State menuItems: Array<NavigationMenuItem> = [\n    {\n      value: 'menuItem1',\n      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action: () => {\n      }\n    }\n  ]\n  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);\n  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);\n\n  build() {\n    NavDestination() {\n      Row() {\n        Column() {\n          // 标题栏内间距切换\n          Button('切换标题栏内间距为32vp')\n            .onClick(() => {\n              this.paddingStart = LengthMetrics.vp(32);\n              this.paddingEnd = LengthMetrics.vp(32);\n            })\n            .margin({ top: 5 })\n\n          Button('切换标题栏内间距为20vp')\n            .onClick(() => {\n              this.paddingStart = LengthMetrics.vp(20);\n              this.paddingEnd = LengthMetrics.vp(20);\n            })\n            .margin({ top: 5 })\n        }\n        .width('100%')\n      }\n      .height('100%')\n    }\n    .hideTitleBar(false)\n    .title('NavDestination title', {\n      paddingStart: this.paddingStart,\n      paddingEnd: this.paddingEnd,\n    })\n    .menus(this.menuItems)\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "NavRouter": {
        "description": "导航组件，默认提供点击响应处理，不需要开发者自定义点击事件逻辑。",
        "interfaces": [
            {
                "description": "NavRouter()\n\n创建NavRouter组件。",
                "params": {}
            },
            {
                "description": "NavRouter(value: RouteInfo)\n\n提供路由信息，指定点击NavRouter时，要跳转的NavDestination页面。",
                "params": {
                    "value": {
                        "type": "RouteInfo",
                        "required": False,
                        "description": "路由信息"
                    }
                }
            }
        ],
        "attributes": {
            "mode": {
                "description": "mode(mode: NavRouteMode)\n\n设置指定点击NavRouter跳转到NavDestination页面时，使用的路由模式。",
                "params": {
                    "mode": {
                        "type": "NavRouteMode",
                        "required": True,
                        "description": "指定点击NavRouter跳转到NavDestination页面时，使用的路由模式。",
                        "default": "NavRouteMode.PUSH_WITH_RECREATE"
                    }
                }
            }
        },
        "events": {
            "onStateChange": {
                "description": "onStateChange(callback: (isActivated: boolean) => void)\n\n组件激活状态切换时触发该回调。开发者点击激活NavRouter，加载对应的NavDestination子组件时，回调onStateChange(true)。NavRouter对应的NavDestination子组件不再显示时，回调onStateChange(false)。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "组件激活状态切换时的回调函数。"
                    }
                }
            }
        },
        "examples": [
            """// NavRouterExample.ets\n\n// 定义一个示例组件，包含两个导航路由，分别用于展示WLAN和蓝牙相关信息\n// 当用户点击WLAN导航时，展示未找到可用WLAN的提示信息，并根据用户操作改变背景颜色\n// 当用户点击蓝牙导航时，展示未找到可用蓝牙的提示信息，并根据用户操作改变背景颜色\n@Entry\n@Component\nstruct NavRouterExample {\n  @State isActiveWLAN: boolean = false // 用于记录WLAN导航的激活状态\n  @State isActiveBluetooth: boolean = false // 用于记录蓝牙导航的激活状态\n\n  build() {\n    Navigation() {\n      // WLAN导航路由\n      NavRouter() {\n        // WLAN导航内容\n        Row() {\n          Row()\n            .width(30)\n            .height(30)\n            .borderRadius(30)\n            .margin({ left: 3, right: 10 })\n            .backgroundColor(Color.Pink)\n          Text(`WLAN`)\n            .fontSize(22)\n            .fontWeight(500)\n            .textAlign(TextAlign.Center)\n        }\n        .width('90%')\n        .height(60)\n\n        // WLAN导航目的地\n        NavDestination() {\n          Flex({ direction: FlexDirection.Row }) {\n            Text('未找到可用WLAN').fontSize(30).padding({ left: 15 })\n          }\n        }.title("WLAN")\n      }\n      .margin({ top: 10, bottom: 10 })\n      .backgroundColor(this.isActiveWLAN ? '#ccc' : '#fff') // 根据激活状态改变背景颜色\n      .borderRadius(20)\n      .mode(NavRouteMode.PUSH_WITH_RECREATE) // 设置路由模式为PUSH_WITH_RECREATE\n      .onStateChange((isActivated: boolean) => {\n        this.isActiveWLAN = isActivated // 监听激活状态变化\n      })\n\n      // 蓝牙导航路由，与WLAN导航类似\n      NavRouter() {\n        Row() {\n          Row()\n            .width(30)\n            .height(30)\n            .borderRadius(30)\n            .margin({ left: 3, right: 10 })\n            .backgroundColor(Color.Pink)\n          Text(`蓝牙`)\n            .fontSize(22)\n            .fontWeight(500)\n            .textAlign(TextAlign.Center)\n        }\n        .width('90%')\n        .height(60)\n\n        NavDestination() {\n          Flex({ direction: FlexDirection.Row }) {\n            Text('未找到可用蓝牙').fontSize(30).padding({ left: 15 })\n          }\n        }.title("蓝牙")\n      }\n      .margin({ top: 10, bottom: 10 })\n      .backgroundColor(this.isActiveBluetooth ? '#ccc' : '#fff') // 根据激活状态改变背景颜色\n      .borderRadius(20)\n      .mode(NavRouteMode.REPLACE) // 设置路由模式为REPLACE\n      .onStateChange((isActivated: boolean) => {\n        this.isActiveBluetooth = isActivated // 监听激活状态变化\n      })\n    }\n    .height('100%')\n    .width('100%')\n    .title('设置')\n    .backgroundColor("#F2F3F5")\n    .titleMode(NavigationTitleMode.Free)\n    .mode(NavigationMode.Auto)\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct NavRouterExample {\n  @State isActiveWLAN: boolean = false\n  @State isActiveBluetooth: boolean = false\n\n  build() {\n    Navigation() {\n      NavRouter() {\n        Row() {\n          Row()\n            .width(30)\n            .height(30)\n            .borderRadius(30)\n            .margin({ left: 3, right: 10 })\n            .backgroundColor(Color.Pink)\n          Text(`WLAN`)\n            .fontSize(22)\n            .fontWeight(500)\n            .textAlign(TextAlign.Center)\n        }\n        .width('90%')\n        .height(60)\n\n        NavDestination() {\n          Flex({ direction: FlexDirection.Row }) {\n            Text('未找到可用WLAN').fontSize(30).padding({ left: 15 })\n          }\n        }.title("WLAN")\n      }\n      .margin({ top: 10, bottom: 10 })\n      .backgroundColor(this.isActiveWLAN ? '#ccc' : '#fff')\n      .borderRadius(20)\n      .mode(NavRouteMode.PUSH_WITH_RECREATE)\n      .onStateChange((isActivated: boolean) => {\n        this.isActiveWLAN = isActivated\n      })\n\n      NavRouter() {\n        Row() {\n          Row()\n            .width(30)\n            .height(30)\n            .borderRadius(30)\n            .margin({ left: 3, right: 10 })\n            .backgroundColor(Color.Pink)\n          Text(`蓝牙`)\n            .fontSize(22)\n            .fontWeight(500)\n            .textAlign(TextAlign.Center)\n        }\n        .width('90%')\n        .height(60)\n\n        NavDestination() {\n          Flex({ direction: FlexDirection.Row }) {\n            Text('未找到可用蓝牙').fontSize(30).padding({ left: 15 })\n          }\n        }.title("蓝牙")\n      }\n      .margin({ top: 10, bottom: 10 })\n      .backgroundColor(this.isActiveBluetooth ? '#ccc' : '#fff')\n      .borderRadius(20)\n      .mode(NavRouteMode.REPLACE)\n      .onStateChange((isActivated: boolean) => {\n        this.isActiveBluetooth = isActivated\n      })\n    }\n    .height('100%')\n    .width('100%')\n    .title('设置')\n    .backgroundColor("#F2F3F5")\n    .titleMode(NavigationTitleMode.Free)\n    .mode(NavigationMode.Auto)\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "NavDestination": {
        "description": "作为子页面的根容器，用于显示Navigation的内容区。",
        "interfaces": [
            {
                "description": "NavDestination()\n\n创建NavDestination组件。",
                "params": {}
            }
        ],
        "attributes": {
            "title": {
                "description": "title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle, options?: NavigationTitleOptions)\n\n设置页面标题。使用NavigationCustomTitle类型设置height高度时，titleMode属性不会生效。字符串超长时，如果不设置副标题，先缩小再换行2行后以...截断。如果设置副标题，先缩小后以...截断。",
                "params": {
                    "value": {
                        "type": ["string", "CustomBuilder", "NavDestinationCommonTitle", "NavDestinationCustomTitle"],
                        "required": True,
                        "description": "页面标题。"
                    },
                    "options": {
                        "type": "NavigationTitleOptions",
                        "required": False,
                        "description": "标题栏选项。"
                    }
                }
            },
            "hideTitleBar": {
                "description": "hideTitleBar(value: boolean)\n\n设置是否隐藏标题栏。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否隐藏标题栏。",
                        "default": False
                    }
                }
            },
            "mode": {
                "description": "mode(value: NavDestinationMode)\n\n设置NavDestination类型，不支持动态修改。",
                "params": {
                    "value": {
                        "type": "NavDestinationMode",
                        "required": True,
                        "description": "NavDestination类型。",
                        "default": "NavDestinationMode.STANDARD"
                    }
                }
            },
            "backButtonIcon": {
                "description": "backButtonIcon(value: ResourceStr | PixelMap | SymbolGlyphModifier)\n\n设置标题栏返回键图标。",
                "params": {
                    "value": {
                        "type": ["ResourceStr", "PixelMap", "SymbolGlyphModifier"],
                        "required": True,
                        "description": "标题栏返回键图标。"
                    }
                }
            },
            "menus": {
                "description": "menus(value: Array<NavigationMenuItem> | CustomBuilder)\n\n设置页面右上角菜单。不设置时不显示菜单项。使用Array<[NavigationMenuItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-navigation-V5#navigationmenuitem%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E)\> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。",
                "params": {
                    "value": {
                        "type": ["Array<NavigationMenuItem>", "CustomBuilder"],
                        "required": True,
                        "description": "页面右上角菜单。"
                    }
                }
            },
            "ignoreLayoutSafeArea": {
                "description": "ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)\n\n控制组件的布局，使其扩展到非安全区域",
                "params": {
                    "types": {
                        "type": "Array<LayoutSafeAreaType>",
                        "required": False,
                        "description": "配置扩展安全区域的类型。",
                        "default": ["LayoutSafeAreaType.SYSTEM"]
                    },
                    "edges": {
                        "type": "Array<LayoutSafeAreaEdge>",
                        "required": False,
                        "description": "配置扩展安全区域的方向。",
                        "default": ["LayoutSafeAreaEdge.TOP", "LayoutSafeAreaEdge.BOTTOM"]
                    }
                }
            },
            "systemBarStyle": {
                "description": "systemBarStyle(style: Optional<SystemBarStyle>)\n\n当Navigation中显示当前NavDestination时，设置对应系统状态栏的样式。",
                "params": {
                    "style": {
                        "type": "Optional<SystemBarStyle>",
                        "required": True,
                        "description": "系统状态栏样式。"
                    }
                }
            }
        },
        "events": {
            "onShown": {
                "description": "onShown(callback: () => void)\n\n当该NavDestination页面显示时触发此回调。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "页面显示时的回调函数。"
                    }
                }
            },
            "onHidden": {
                "description": "onHidden(callback: () => void)\n\n当该NavDestination页面隐藏时触发此回调。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "页面隐藏时的回调函数。"
                    }
                }
            },
            "onWillAppear": {
                "description": "onWillAppear(callback: Callback<void>)\n\n当该Destination挂载之前触发此回调。在该回调中允许修改页面栈，当前帧生效。",
                "params": {
                    "callback": {
                        "type": "Callback<void>",
                        "required": True,
                        "description": "挂载之前的回调函数。"
                    }
                }
            },
            "onWillShow": {
                "description": "onWillShow(callback: Callback<void>)\n\n当该Destination显示之前触发此回调。",
                "params": {
                    "callback": {
                        "type": "Callback<void>",
                        "required": True,
                        "description": "显示之前的回调函数。"
                    }
                }
            },
            "onWillHide": {
                "description": "onWillHide(callback: Callback<void>)\n\n当该Destination隐藏之前触发此回调。",
                "params": {
                    "callback": {
                        "type": "Callback<void>",
                        "required": True,
                        "description": "隐藏之前的回调函数。"
                    }
                }
            },
            "onWillDisappear": {
                "description": "onWillDisappear(callback: Callback<void>)\n\n当该Destination卸载之前触发的生命周期(有转场动画时，在转场动画开始之前触发)。",
                "params": {
                    "callback": {
                        "type": "Callback<void>",
                        "required": True,
                        "description": "卸载之前的回调函数。"
                    }
                }
            },
            "onBackPressed": {
                "description": "onBackPressed(callback: () => boolean)\n\n当与Navigation绑定的页面栈中存在内容时，此回调生效。当点击返回键时，触发该回调。返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。",
                "params": {
                    "callback": {
                        "type": "function",
                        "required": True,
                        "description": "返回键点击时的回调函数。"
                    }
                }
            },
            "onReady": {
                "description": "onReady(callback: Callback<NavDestinationContext>)\n\n当NavDestination即将构建子组件之前会触发此回调。",
                "params": {
                    "callback": {
                        "type": "Callback<NavDestinationContext>",
                        "required": True,
                        "description": "构建子组件之前的回调函数。"
                    }
                }
            }
        },
        "examples": [
            """// NavigationExample.ets\n\n/**\n * NavigationExample struct represents a navigation page layout.\n * It includes a title, menus, search input, list of items, and toolbar configuration.\n */\n@Entry\n@Component\nstruct NavigationExample {\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n  @State currentIndex: number = 0\n\n  /**\n   * NavigationTitle builder function creates the title section of the navigation.\n   * It includes a main title and a subtitle.\n   */\n  @Builder NavigationTitle() {\n    Column() {\n      Text('Title')\n        .fontColor('#182431')\n        .fontSize(30)\n        .lineHeight(41)\n        .fontWeight(700)\n      Text('subtitle')\n        .fontColor('#182431')\n        .fontSize(14)\n        .lineHeight(19)\n        .opacity(0.4)\n        .margin({ top: 2, bottom: 20 })\n    }.alignItems(HorizontalAlign.Start)\n  }\n\n  /**\n   * NavigationMenus builder function creates the menu section of the navigation.\n   * It includes three images for menu options.\n   */\n  @Builder NavigationMenus() {\n    Row() {\n      Image('resources/base/media/ic_public_add.svg')\n        .width(24)\n        .height(24)\n      Image('resources/base/media/ic_public_add.svg')\n        .width(24)\n        .height(24)\n        .margin({ left: 24 })\n      Image('common/ic_public_more.svg')\n        .width(24)\n        .height(24)\n        .margin({ left: 24 })\n    }\n  }\n\n  /**\n   * build function constructs the overall layout of the navigation page.\n   * It includes search input, list of items, toolbar configuration, and title/menus settings.\n   */\n  build() {\n    Column() {\n      Navigation() {\n        TextInput({ placeholder: 'search...' })\n          .width('90%')\n          .height(40)\n          .backgroundColor('#FFFFFF')\n          .margin({ top: 8 })\n\n        List({ space: 12, initialIndex: 0 }) {\n          ForEach(this.arr, (item: number) => {\n            ListItem() {\n              Text('' + item)\n                .width('90%')\n                .height(72)\n                .backgroundColor('#FFFFFF')\n                .borderRadius(24)\n                .fontSize(16)\n                .fontWeight(500)\n                .textAlign(TextAlign.Center)\n            }\n          }, (item: number) => item.toString())\n        }\n        .height(324)\n        .width('100%')\n        .margin({ top: 12, left: '10%' })\n      }\n      .title(this.NavigationTitle)\n      .menus(this.NavigationMenus)\n      .titleMode(NavigationTitleMode.Full)\n      .toolbarConfiguration([\n        {\n          value: $r("app.string.navigation_toolbar_add"),\n          icon: $r("app.media.ic_public_highlightsed")\n        },\n        {\n          value: $r("app.string.navigation_toolbar_app"),\n          icon: $r("app.media.ic_public_highlights")\n        },\n        {\n          value: $r("app.string.navigation_toolbar_collect"),\n          icon: $r("app.media.ic_public_highlights")\n        }\n      ])\n      .hideTitleBar(false)\n      .hideToolBar(false)\n      .onTitleModeChange((titleModel: NavigationTitleMode) => {\n        console.info('titleMode' + titleModel)\n      })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}\n```\n// xxx.ets\nclass A {\n  text: string = ''\n  num: number = 0\n}\n\n@Entry\n@Component\nstruct NavigationExample {\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n  @State currentIndex: number = 0\n\n  @Builder NavigationTitle() {\n    Column() {\n      Text('Title')\n        .fontColor('#182431')\n        .fontSize(30)\n        .lineHeight(41)\n        .fontWeight(700)\n      Text('subtitle')\n        .fontColor('#182431')\n        .fontSize(14)\n        .lineHeight(19)\n        .opacity(0.4)\n        .margin({ top: 2, bottom: 20 })\n    }.alignItems(HorizontalAlign.Start)\n  }\n\n  @Builder NavigationMenus() {\n    Row() {\n      Image('resources/base/media/ic_public_add.svg')\n        .width(24)\n        .height(24)\n      Image('resources/base/media/ic_public_add.svg')\n        .width(24)\n        .height(24)\n        .margin({ left: 24 })\n      Image('common/ic_public_more.svg')\n        .width(24)\n        .height(24)\n        .margin({ left: 24 })\n    }\n  }\n\n  build() {\n    Column() {\n      Navigation() {\n        TextInput({ placeholder: 'search...' })\n          .width('90%')\n          .height(40)\n          .backgroundColor('#FFFFFF')\n          .margin({ top: 8 })\n\n        List({ space: 12, initialIndex: 0 }) {\n          ForEach(this.arr, (item: number) => {\n            ListItem() {\n              Text('' + item)\n                .width('90%')\n                .height(72)\n                .backgroundColor('#FFFFFF')\n                .borderRadius(24)\n                .fontSize(16)\n                .fontWeight(500)\n                .textAlign(TextAlign.Center)\n            }\n          }, (item: number) => item.toString())\n        }\n        .height(324)\n        .width('100%')\n        .margin({ top: 12, left: '10%' })\n      }\n      .title(this.NavigationTitle)\n      .menus(this.NavigationMenus)\n      .titleMode(NavigationTitleMode.Full)\n      .toolbarConfiguration([\n        {\n          value: $r("app.string.navigation_toolbar_add"),\n          icon: $r("app.media.ic_public_highlightsed")\n        },\n        {\n          value: $r("app.string.navigation_toolbar_app"),\n          icon: $r("app.media.ic_public_highlights")\n        },\n        {\n          value: $r("app.string.navigation_toolbar_collect"),\n          icon: $r("app.media.ic_public_highlights")\n        }\n      ])\n      .hideTitleBar(false)\n      .hideToolBar(false)\n      .onTitleModeChange((titleModel: NavigationTitleMode) => {\n        console.info('titleMode' + titleModel)\n      })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            """// Index.ets\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfos: NavPathStack = new NavPathStack()\n  isUseInterception: boolean = false;\n\n  // 注册拦截器，用于拦截路由跳转并进行相应处理\n  registerInterception() {\n    this.pageInfos.setInterception({\n      // 当即将显示目标页面时的拦截处理\n      willShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",\n                 operation: NavigationOperation, animated: boolean) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        if (typeof to === "string") {\n          console.log("target page is navigation home");\n          return;\n        }\n        // 重定向目标页面，将pageTwo替换为pageOne\n        let target: NavDestinationContext = to as NavDestinationContext;\n        if (target.pathInfo.name === 'pageTwo') {\n          target.pathStack.pop();\n          target.pathStack.pushPathByName('pageOne', null);\n        }\n      },\n      // 当页面显示完成后的拦截处理\n      didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",\n                operation: NavigationOperation, isAnimated: boolean) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        if (typeof from === "string") {\n          console.log("current transition is from navigation home");\n        } else {\n          console.log(`current transition is from  ${(from as NavDestinationContext).pathInfo.name}`)\n        }\n        if (typeof to === "string") {\n          console.log("current transition to is navBar");\n        } else {\n          console.log(`current transition is to ${(to as NavDestinationContext).pathInfo.name}`);\n        }\n      },\n      // 当导航模式改变时的拦截处理\n      modeChange: (mode: NavigationMode) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        console.log(`current navigation mode is ${mode}`);\n      }\n    })\n  }\n\n  // 构建页面结构\n  build() {\n    Navigation(this.pageInfos) {\n      Column() {\n        // 创建一个按钮，用于将页面信息入栈\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.pageInfos.pushPath({ name: 'pageOne' }) //将name指定的NavDestination页面信息入栈\n          })\n        // 创建一个按钮，用于开启或关闭拦截器\n        Button('use interception', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.isUseInterception = !this.isUseInterception;\n            if (this.isUseInterception) {\n              this.registerInterception();\n            } else {\n              this.pageInfos.setInterception(undefined);\n            }\n          })\n      }\n    }.title('NavIndex')\n  }\n}\n```\n// Index.ets\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfos: NavPathStack = new NavPathStack()\n  isUseInterception: boolean = false;\n\n  registerInterception() {\n    this.pageInfos.setInterception({\n      willShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",\n                 operation: NavigationOperation, animated: boolean) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        if (typeof to === "string") {\n          console.log("target page is navigation home");\n          return;\n        }\n        // redirect target page.Change pageTwo to pageOne.\n        let target: NavDestinationContext = to as NavDestinationContext;\n        if (target.pathInfo.name === 'pageTwo') {\n          target.pathStack.pop();\n          target.pathStack.pushPathByName('pageOne', null);\n        }\n      },\n      didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",\n                operation: NavigationOperation, isAnimated: boolean) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        if (typeof from === "string") {\n          console.log("current transition is from navigation home");\n        } else {\n          console.log(`current transition is from  ${(from as NavDestinationContext).pathInfo.name}`)\n        }\n        if (typeof to === "string") {\n          console.log("current transition to is navBar");\n        } else {\n          console.log(`current transition is to ${(to as NavDestinationContext).pathInfo.name}`);\n        }\n      },\n      modeChange: (mode: NavigationMode) => {\n        if (!this.isUseInterception) {\n          return;\n        }\n        console.log(`current navigation mode is ${mode}`);\n      }\n    })\n  }\n\n  build() {\n    Navigation(this.pageInfos) {\n      Column() {\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.pageInfos.pushPath({ name: 'pageOne' }) //将name指定的NavDestination页面信息入栈\n          })\n        Button('use interception', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.isUseInterception = !this.isUseInterception;\n            if (this.isUseInterception) {\n              this.registerInterception();\n            } else {\n              this.pageInfos.setInterception(undefined);\n            }\n          })\n      }\n    }.title('NavIndex')\n  }\n}"""
            """// Index.ets\n\n// 该示例主要演示设置每个NavDestination子页面的自定义转场动画及可交互转场动画。\n\nimport { CustomTransition, AnimateCallback } from './CustomNavigationUtils'\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfos: NavPathStack = new NavPathStack();\n\n  // 当页面即将出现时触发的方法\n  aboutToAppear() {\n    if (this.pageInfos === undefined) {\n      this.pageInfos = new NavPathStack();\n    }\n    // 将页面信息添加到页面信息栈中\n    this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });\n  }\n\n  // 构建导航页面\n  build() {\n    Navigation(this.pageInfos) {\n    }\n    .title('NavIndex')\n    .hideNavBar(true)\n    // 设置自定义导航内容转场动画\n    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {\n      if (from.mode == NavDestinationMode.DIALOG || to.mode == NavDestinationMode.DIALOG) {\n        return undefined;\n      }\n\n      // 首页不进行自定义动画\n      if (from.index === -1 || to.index === -1) {\n        return undefined;\n      }\n\n      CustomTransition.getInstance().operation = operation;\n      if (CustomTransition.getInstance().interactive) {\n        // 创建可交互的自定义动画\n        let customAnimation: NavigationAnimatedTransition = {\n          onTransitionEnd: (isSuccess: boolean) => {\n            console.log("===== current transition is " + isSuccess);\n            CustomTransition.getInstance().recoverState();\n            CustomTransition.getInstance().proxy = undefined;\n          },\n          transition: (transitionProxy: NavigationTransitionProxy) => {\n            CustomTransition.getInstance().proxy = transitionProxy;\n            let targetIndex: string | undefined = operation == NavigationOperation.PUSH ?\n              (to.navDestinationId) : (from.navDestinationId);\n            if (targetIndex) {\n              CustomTransition.getInstance().fireInteractiveAnimation(targetIndex, operation);\n            }\n          },\n          isInteractive: CustomTransition.getInstance().interactive\n        }\n        return customAnimation;\n      } else {\n        // 创建非交互的自定义动画\n        let customAnimation: NavigationAnimatedTransition = {\n          onTransitionEnd: (isSuccess: boolean)=>{\n            console.log(`current transition result is ${isSuccess}`)\n          },\n          timeout: 7000,\n          transition: (transitionProxy: NavigationTransitionProxy) => {\n            if (!from.navDestinationId || !to.navDestinationId) {\n              return;\n            }\n            // 获取转场动画回调参数\n            let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);\n            let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);\n            if (operation == NavigationOperation.PUSH) {\n              if (toParam.start) {\n                toParam.start(true, false);\n              }\n              animateTo({\n                duration: 500, onFinish: () => {\n                  transitionProxy.finishTransition();\n                }\n              }, () => {\n                if (toParam.finish) {\n                  toParam.finish(true, false);\n                }\n              })\n            } else {\n              if (fromParam.start) {\n                fromParam.start(true, true);\n              }\n              animateTo({\n                duration: 500, onFinish: () => {\n                  transitionProxy.finishTransition();\n                }\n              }, () => {\n                if (fromParam.finish) {\n                  fromParam.finish(true, true);\n                }\n              })\n            }\n          }\n        };\n        return customAnimation;\n      }\n    })\n  }\n}\n```\n\n这段代码实现了为每个NavDestination子页面设置自定义转场动画及可交互转场动画的功能。具体包括：\n1. 在页面即将出现时，将页面信息添加到页面信息栈中。\n2. 构建导航页面，并设置自定义导航内容转场动画。\n3. 根据不同情况，创建可交互的自定义动画或非交互的自定义动画。\n4. 在转场过程中，根据操作类型执行相应的动画操作，包括开始动画、结束动画等。\n// Index.ets\nimport { CustomTransition, AnimateCallback } from './CustomNavigationUtils'\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfos: NavPathStack = new NavPathStack();\n\n  aboutToAppear() {\n    if (this.pageInfos === undefined) {\n      this.pageInfos = new NavPathStack();\n    }\n    this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });\n  }\n\n  build() {\n    Navigation(this.pageInfos) {\n    }\n    .title('NavIndex')\n    .hideNavBar(true)\n    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {\n      if (from.mode == NavDestinationMode.DIALOG || to.mode == NavDestinationMode.DIALOG) {\n        return undefined;\n      }\n\n      // 首页不进行自定义动画\n      if (from.index === -1 || to.index === -1) {\n        return undefined;\n      }\n\n      CustomTransition.getInstance().operation = operation;\n      if (CustomTransition.getInstance().interactive) {\n        let customAnimation: NavigationAnimatedTransition = {\n          onTransitionEnd: (isSuccess: boolean) => {\n            console.log("===== current transition is " + isSuccess);\n            CustomTransition.getInstance().recoverState();\n            CustomTransition.getInstance().proxy = undefined;\n          },\n          transition: (transitionProxy: NavigationTransitionProxy) => {\n            CustomTransition.getInstance().proxy = transitionProxy;\n            let targetIndex: string | undefined = operation == NavigationOperation.PUSH ?\n              (to.navDestinationId) : (from.navDestinationId);\n            if (targetIndex) {\n              CustomTransition.getInstance().fireInteractiveAnimation(targetIndex, operation);\n            }\n          },\n          isInteractive: CustomTransition.getInstance().interactive\n        }\n        return customAnimation;\n      }\n      let customAnimation: NavigationAnimatedTransition = {\n        onTransitionEnd: (isSuccess: boolean)=>{\n          console.log(`current transition result is ${isSuccess}`)\n        },\n        timeout: 7000,\n        // 转场开始时系统调用该方法，并传入转场上下文代理对象\n        transition: (transitionProxy: NavigationTransitionProxy) => {\n          if (!from.navDestinationId || !to.navDestinationId) {\n            return;\n          }\n          // 从封装类CustomTransition中根据子页面的序列获取对应的转场动画回调\n          let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);\n          let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);\n          if (operation == NavigationOperation.PUSH) {\n            if (toParam.start) {\n              toParam.start(true, false);\n            }\n            animateTo({\n              duration: 500, onFinish: () => {\n                transitionProxy.finishTransition();\n              }\n            }, () => {\n              if (toParam.finish) {\n                toParam.finish(true, false);\n              }\n            })\n          } else {\n            if (fromParam.start) {\n              fromParam.start(true, true);\n            }\n            animateTo({\n              duration: 500, onFinish: () => {\n                transitionProxy.finishTransition();\n              }\n            }, () => {\n              if (fromParam.finish) {\n                fromParam.finish(true, true);\n              }\n            })\n          }\n        }\n      };\n      return customAnimation;\n    })\n  }\n}"""
            """// Index.ets\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfo: NavPathStack = new NavPathStack()\n\n  build() {\n    // 创建一个Navigation组件，用于管理页面导航\n    Navigation(this.pageInfo) {\n      // 创建一个垂直布局Column\n      Column() {\n        // 创建一个带有特定样式的按钮，点击后将页面信息入栈\n        Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%') // 设置按钮宽度为80%\n          .height(40) // 设置按钮高度为40\n          .margin(20) // 设置按钮外边距为20\n          .onClick(() => {\n            this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。\n          })\n      }\n    }.title('NavIndex') // 设置Navigation的标题为'NavIndex'\n  }\n}\n```\n\n在上述示例代码中：\n- `NavigationExample` 结构体包含了一个 `pageInfo` 变量，用于管理页面导航信息。\n- `build` 方法用于构建页面内容。\n- `Navigation` 组件用于管理页面导航，传入了 `pageInfo` 变量。\n- `Column` 组件用于创建垂直布局。\n- `Button` 组件创建一个特定样式的按钮，点击按钮后执行指定操作。\n- `width`、`height`、`margin` 方法分别设置按钮的宽度、高度和外边距。\n- `onClick` 方法设置按钮点击事件，将指定页面信息入栈。\n- `title` 方法设置 Navigation 的标题为 'NavIndex'。\n// Index.ets\n\n@Entry\n@Component\nstruct NavigationExample {\n  pageInfo: NavPathStack = new NavPathStack()\n\n  build() {\n    Navigation(this.pageInfo) {\n      Column() {\n        Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。\n          })\n      }\n    }.title('NavIndex')\n  }\n}。"""
            """// 该示例主要演示设置Navigation主页的标题栏、工具栏和NavDestination页面的标题栏的背景颜色和背景模糊效果。\n\n// 定义两种背景颜色和两种背景模糊效果\nlet COLOR1: string = "#80004AAF"; // 第一种背景颜色\nlet COLOR2: string = "#802787D9"; // 第二种背景颜色\nlet BLUR_STYLE_1: BlurStyle = BlurStyle.BACKGROUND_THIN; // 第一种背景模糊效果\nlet BLUR_STYLE_2: BlurStyle = BlurStyle.BACKGROUND_THICK; // 第二种背景模糊效果\n\n// BackComponent组件，用于创建背景颜色块\n@Component\nstruct BackComponent {\n  build() {\n    Row() {\n      Column() {}\n      .height('100%')\n      .backgroundColor("#3D9DB4")\n      .layoutWeight(9)\n      Column() {}\n      .height('100%')\n      .backgroundColor("17A98D")\n      .layoutWeight(9)\n      Column() {}\n      .height('100%')\n      .backgroundColor("FFC000")\n      .layoutWeight(9)\n    }\n    .height('100%')\n    .width('100%')\n  }\n}\n\n// ColorAndBlur组件，用于切换背景颜色和背景模糊效果\n@Component\nstruct ColorAndBlur {\n  @State useColor1: boolean = true; // 控制是否使用第一种背景颜色\n  @State useBlur1: boolean = true; // 控制是否使用第一种背景模糊效果\n\n  build() {\n    NavDestination() {\n      Stack({alignContent: Alignment.Center}) {\n        BackComponent()\n          .width('100%')\n          .height('100%')\n        Column() {\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch color")\n              .onClick(() => {\n                this.useColor1 = !this.useColor1; // 切换背景颜色\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch blur")\n              .onClick(() => {\n                this.useBlur1 = !this.useBlur1; // 切换背景模糊效果\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n        }\n        .width('100%')\n        .height('100%')\n      }.width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    // 设置标题栏的背景颜色和背景模糊效果\n    .title("switch titlebar color and blur", {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,\n      barStyle: BarStyle.STACK\n    })\n  }\n}\n\n// Index组件，作为入口组件，展示导航、工具栏以及页面切换\n@Entry\n@Component\nstruct Index {\n  private stack: NavPathStack = new NavPathStack();\n  @State useColor1: boolean = true; // 控制是否使用第一种背景颜色\n  @State useBlur1: boolean = true; // 控制是否使用第一种背景模糊效果\n\n  @Builder\n  PageBuilder(name: string) {\n    ColorAndBlur()\n  }\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        BackComponent()\n          .width('100%')\n          .height('100%')\n        Column() {\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch color")\n              .onClick(() => {\n                this.useColor1 = !this.useColor1; // 切换背景颜色\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch blur")\n              .onClick(() => {\n                this.useBlur1 = !this.useBlur1; // 切换背景模糊效果\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("push page")\n              .onClick(() => {\n                this.stack.pushPath({name: "page"}); // 页面切换\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n        }\n        .width('100%')\n        .height('80%')\n      }.width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .navDestination(this.PageBuilder)\n    // 设置标题栏的背景颜色和背景模糊效果\n    .title("NavTitle", {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,\n      barStyle: BarStyle.STACK\n    })\n    // 设置工具栏的背景颜色和背景模糊效果\n    .toolbarConfiguration([\n      {value: "a"},\n      {value: "b"},\n      {value: "c"}\n    ], {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2\n    })\n  }\n}\n```\nlet COLOR1: string = "#80004AAF";\nlet COLOR2: string = "#802787D9";\nlet BLUR_STYLE_1: BlurStyle = BlurStyle.BACKGROUND_THIN;\nlet BLUR_STYLE_2: BlurStyle = BlurStyle.BACKGROUND_THICK;\n\n@Component\nstruct BackComponent {\n  build() {\n    Row() {\n      Column() {}\n      .height('100%')\n      .backgroundColor("#3D9DB4")\n      .layoutWeight(9)\n      Column() {}\n      .height('100%')\n      .backgroundColor("17A98D")\n      .layoutWeight(9)\n      Column() {}\n      .height('100%')\n      .backgroundColor("FFC000")\n      .layoutWeight(9)\n    }\n    .height('100%')\n    .width('100%')\n  }\n}\n\n@Component\nstruct ColorAndBlur {\n  @State useColor1: boolean = true;\n  @State useBlur1: boolean = true;\n\n  build() {\n    NavDestination() {\n      Stack({alignContent: Alignment.Center}) {\n        BackComponent()\n          .width('100%')\n          .height('100%')\n        Column() {\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch color")\n              .onClick(() => {\n                this.useColor1 = !this.useColor1;\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch blur")\n              .onClick(() => {\n                this.useBlur1 = !this.useBlur1;\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n        }\n        .width('100%')\n        .height('100%')\n      }.width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    // 开发者可以设置标题栏的背景颜色和背景模糊效果\n    .title("switch titlebar color and blur", {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,\n      barStyle: BarStyle.STACK\n    })\n  }\n}\n\n@Entry\n@Component\nstruct Index {\n  private stack: NavPathStack = new NavPathStack();\n  @State useColor1: boolean = true;\n  @State useBlur1: boolean = true;\n\n  @Builder\n  PageBuilder(name: string) {\n    ColorAndBlur()\n  }\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        BackComponent()\n          .width('100%')\n          .height('100%')\n        Column() {\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch color")\n              .onClick(() => {\n                this.useColor1 = !this.useColor1;\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("switch blur")\n              .onClick(() => {\n                this.useBlur1 = !this.useBlur1;\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n          Stack({alignContent: Alignment.Center}) {\n            Button("push page")\n              .onClick(() => {\n                this.stack.pushPath({name: "page"})\n              })\n          }\n          .width('100%')\n          .layoutWeight(1)\n        }\n        .width('100%')\n        .height('80%')\n      }.width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .navDestination(this.PageBuilder)\n    // 开发者可以设置标题栏的背景颜色和背景模糊效果\n    .title("NavTitle", {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,\n      barStyle: BarStyle.STACK\n    })\n    // 开发者可以设置工具栏的背景颜色和背景模糊效果\n    .toolbarConfiguration([\n      {value: "a"},\n      {value: "b"},\n      {value: "c"}\n    ], {\n      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,\n      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2\n    })\n  }\n}"""
            """@Entry\n@Component\nstruct NavigationExample1 {\n  @State childNavStack: NavPathStack = new NavPathStack();\n\n  build() {\n    Navigation() {\n      Stack({alignContent: Alignment.Center}) {\n        // 在嵌套Navigation场景下创建子Navigation，并演示如何获取父NavPathStack\n        Navigation(this.childNavStack) {\n          Button('push Path to parent Navigation', { stateEffect: true, type: ButtonType.Capsule })\n            .width('80%')\n            .height(40)\n            .margin(20)\n            .onClick(() => {\n              // 点击按钮时获取父NavPathStack，并向其推送新的路径\n              let parentStack = this.childNavStack.getParent();\n              parentStack?.pushPath({ name: "pageOne"})\n            })\n        }\n        .clip(true)\n        .backgroundColor(Color.Orange)\n        .width('80%')\n        .height('80%')\n        .title('ChildNavigation')\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .backgroundColor(Color.Green)\n    .width('100%')\n    .height('100%')\n    .title('ParentNavigation')\n  }\n}\n```\n\n在上述示例代码中：\n- 创建了一个嵌套Navigation场景，包含父导航和子导航。\n- 子导航使用了传入的childNavStack作为导航栈。\n- 通过按钮的点击事件演示了如何获取父导航的NavPathStack，并向其推送新的路径。\n- 父导航的背景色为绿色，宽高为100%，标题为'ParentNavigation'。\n- 子导航的背景色为橙色，宽高为80%，标题为'ChildNavigation'。\n@Entry\n@Component\nstruct NavigationExample1 {\n  @State childNavStack: NavPathStack = new NavPathStack();\n\n  build() {\n    Navigation() {\n      Stack({alignContent: Alignment.Center}) {\n        Navigation(this.childNavStack) {\n          Button('push Path to parent Navigation', { stateEffect: true, type: ButtonType.Capsule })\n            .width('80%')\n            .height(40)\n            .margin(20)\n            .onClick(() => {\n              // 可以获取父NavPathStack\n              let parentStack = this.childNavStack.getParent();\n              parentStack?.pushPath({ name: "pageOne"})\n            })\n        }\n        .clip(true)\n        .backgroundColor(Color.Orange)\n        .width('80%')\n        .height('80%')\n        .title('ChildNavigation')\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .backgroundColor(Color.Green)\n    .width('100%')\n    .height('100%')\n    .title('ParentNavigation')\n  }\n}"""
            """// NavPathStack无需声明为状态变量，也可以实现页面栈操作功能。\n// NavDestination通过onReady事件能够拿到对应的NavPathInfo和所属的NavPathStack。\n\n// PageParam类用于存储页面参数\nclass PageParam {\n  constructor(num_: number) {\n    this.num = num_;\n  }\n  num: number = 0;\n}\n\n// PageOneBuilder函数用于构建页面One\n@Builder\nexport function PageOneBuilder(name: string, param: Object) {\n  PageOne()\n}\n\n// PageOne组件用于展示页面One的内容和操作按钮\n@Component\nstruct PageOne {\n  private stack: NavPathStack | null = null; // 页面所属的页面栈\n  private name: string = ""; // 页面名称\n  private paramNum: number = 0; // 页面参数\n\n  build() {\n    NavDestination() {\n      Column() {\n        Text("NavPathInfo: name: " + this.name + ", paramNum: " + this.paramNum) // 显示页面信息\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule }) // 按钮用于推入新页面\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            if (this.stack) {\n              let p = new PageParam(this.paramNum + 1);\n              this.stack.pushPath({name: "pageOne", param: p}); // 推入新页面\n            }\n          })\n        Button('pop', { stateEffect: true, type: ButtonType.Capsule }) // 按钮用于弹出当前页面\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack?.pop(); // 弹出当前页面\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .title('pageOne')\n    .onReady((ctx: NavDestinationContext) => {\n      // 在NavDestination中能够拿到传来的NavPathInfo和当前所处的NavPathStack\n      try {\n        this.name = ctx?.pathInfo?.name; // 获取页面名称\n        this.paramNum = (ctx?.pathInfo?.param as PageParam)?.num; // 获取页面参数\n        this.stack = ctx.pathStack; // 获取页面所属的页面栈\n      } catch (e) {\n        console.log(`testTag onReady catch exception: ${JSON.stringify(e)}`)\n      }\n    })\n  }\n}\n\n// NavigationExample2组件用于展示导航示例2的内容和操作按钮\n@Entry\n@Component\nstruct NavigationExample2 {\n  private stack : NavPathStack = new NavPathStack(); // 创建一个页面栈\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule }) // 按钮用于推入新页面\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            let p = new PageParam(1);\n            this.stack.pushPath({ name: "pageOne", param: p }); // 推入新页面\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .title('Navigation')\n  }\n}\n\n// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}\n// route_map.json\n{\n  "routerMap": [\n    {\n      "name": "pageOne",\n      "pageSourceFile": "src/main/ets/pages/Index.ets",\n      "buildFunction": "PageOneBuilder",\n      "data": {\n        "description": "this is pageOne"\n      }\n    }\n  ]\n}\n```\nclass PageParam {\n  constructor(num_: number) {\n    this.num = num_;\n  }\n  num: number = 0;\n}\n\n@Builder\nexport function PageOneBuilder(name: string, param: Object) {\n  PageOne()\n}\n\n@Component\nstruct PageOne {\n  private stack: NavPathStack | null = null;\n  private name: string = "";\n  private paramNum: number = 0;\n\n  build() {\n    NavDestination() {\n      Column() {\n        Text("NavPathInfo: name: " + this.name + ", paramNum: " + this.paramNum)\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            if (this.stack) {\n              let p = new PageParam(this.paramNum + 1);\n              this.stack.pushPath({name: "pageOne", param: p});\n            }\n          })\n        Button('pop', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack?.pop()\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .title('pageOne')\n    .onReady((ctx: NavDestinationContext) => {\n      // 在NavDestination中能够拿到传来的NavPathInfo和当前所处的NavPathStack\n      try {\n        this.name = ctx?.pathInfo?.name;\n        this.paramNum = (ctx?.pathInfo?.param as PageParam)?.num;\n        this.stack = ctx.pathStack;\n      } catch (e) {\n        console.log(`testTag onReady catch exception: ${JSON.stringify(e)}`)\n      }\n    })\n  }\n}\n\n@Entry\n@Component\nstruct NavigationExample2 {\n  private stack : NavPathStack = new NavPathStack();\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            let p = new PageParam(1);\n            this.stack.pushPath({ name: "pageOne", param: p })\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .title('Navigation')\n  }\n}\n// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}\n// route_map.json\n{\n  "routerMap": [\n    {\n      "name": "pageOne",\n      "pageSourceFile": "src/main/ets/pages/Index.ets",\n      "buildFunction": "PageOneBuilder",\n      "data": {\n        "description": "this is pageOne"\n      }\n    }\n  ]\n}"""
            """// 该示例演示NavDestination的生命周期时序。\n\n// NavDestination表示导航目的地，包含了页面的生命周期方法和事件处理。\n// PageOneBuilder用于构建页面One的组件。\n@Builder\nexport function PageOneBuilder(name: string, param: Object) {\n  PageOneComponent()\n}\n\n// PageOneComponent是页面One的组件，包含了页面布局和生命周期方法的定义。\n@Component\nstruct PageOneComponent {\n  private stack: NavPathStack | null = null;\n  @State eventStr: string = "";\n\n  // build方法用于构建页面的UI布局和定义页面的生命周期方法。\n  build() {\n    NavDestination() {\n      Column() {\n        // 显示当前事件字符串\n        Text("event: " + this.eventStr)\n        \n        // 点击按钮，将页面One推入导航栈\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            if (this.stack) {\n              this.stack.pushPath({name: "pageOne"});\n            }\n          })\n        \n        // 点击按钮，将页面One从导航栈中弹出\n        Button('pop', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack?.pop()\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    // 设置页面标题为'pageOne'\n    .title('pageOne')\n    // 页面生命周期方法的定义\n    .onAppear(() => { this.eventStr += "<onAppear>"; })\n    .onDisAppear(() => { this.eventStr += "<onDisAppear>"; })\n    .onShown(() => { this.eventStr += "<onShown>"; })\n    .onHidden(() => { this.eventStr += "<onHidden>"; })\n    .onWillAppear(() => { this.eventStr += "<onWillAppear>"; })\n    .onWillDisappear(() => { this.eventStr += "<onWillDisappear>"; })\n    .onWillShow(() => { this.eventStr += "<onWillShow>"; })\n    .onWillHide(() => { this.eventStr += "<onWillHide>"; })\n    // onReady会在onAppear之前调用\n    .onReady((ctx: NavDestinationContext) => {\n      try {\n        this.eventStr += "<onReady>";\n        this.stack = ctx.pathStack;\n      } catch (e) {\n        console.log(`testTag onReady catch exception: ${JSON.stringify(e)}`)\n      }\n    })\n  }\n}\n\n// NavigationExample3是导航示例的入口组件，包含了导航栈的初始化和页面One的跳转按钮。\n@Entry\n@Component\nstruct NavigationExample3 {\n  private stack : NavPathStack = new NavPathStack();\n\n  // 构建导航示例的UI布局\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        // 点击按钮，将页面One推入导航栈\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack.pushPath({ name: "pageOne" })\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .title('Navigation')\n  }\n}\n\n// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}\n// route_map.json\n// 路由映射配置，指定页面One的信息\n{\n  "routerMap": [\n    {\n      "name": "pageOne",\n      "pageSourceFile": "src/main/ets/pages/Index.ets",\n      "buildFunction": "PageOneBuilder",\n      "data": {\n        "description": "this is pageOne"\n      }\n    }\n  ]\n}\n```\n@Builder\nexport function PageOneBuilder(name: string, param: Object) {\n  PageOneComponent()\n}\n\n@Component\nstruct PageOneComponent {\n  private stack: NavPathStack | null = null;\n  @State eventStr: string = "";\n\n  build() {\n    NavDestination() {\n      Column() {\n        Text("event: " + this.eventStr)\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            if (this.stack) {\n              this.stack.pushPath({name: "pageOne"});\n            }\n          })\n        Button('pop', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack?.pop()\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .title('pageOne')\n    .onAppear(() => { this.eventStr += "<onAppear>"; })\n    .onDisAppear(() => { this.eventStr += "<onDisAppear>"; })\n    .onShown(() => { this.eventStr += "<onShown>"; })\n    .onHidden(() => { this.eventStr += "<onHidden>"; })\n    .onWillAppear(() => { this.eventStr += "<onWillAppear>"; })\n    .onWillDisappear(() => { this.eventStr += "<onWillDisappear>"; })\n    .onWillShow(() => { this.eventStr += "<onWillShow>"; })\n    .onWillHide(() => { this.eventStr += "<onWillHide>"; })\n    // onReady会在onAppear之前调用\n    .onReady((ctx: NavDestinationContext) => {\n      try {\n        this.eventStr += "<onReady>";\n        this.stack = ctx.pathStack;\n      } catch (e) {\n        console.log(`testTag onReady catch exception: ${JSON.stringify(e)}`)\n      }\n    })\n  }\n}\n\n@Entry\n@Component\nstruct NavigationExample3 {\n  private stack : NavPathStack = new NavPathStack();\n\n  build() {\n    Navigation(this.stack) {\n      Stack({alignContent: Alignment.Center}) {\n        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })\n          .width('80%')\n          .height(40)\n          .margin(20)\n          .onClick(() => {\n            this.stack.pushPath({ name: "pageOne" })\n          })\n      }\n      .width('100%')\n      .height('100%')\n    }\n    .width('100%')\n    .height('100%')\n    .title('Navigation')\n  }\n}\n// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}\n// route_map.json\n{\n  "routerMap": [\n    {\n      "name": "pageOne",\n      "pageSourceFile": "src/main/ets/pages/Index.ets",\n      "buildFunction": "PageOneBuilder",\n      "data": {\n        "description": "this is pageOne"\n      }\n    }\n  ]\n}"""
            """// 该示例演示Navigation标题栏STACK布局效果。\n\n@Entry\n@Component\nstruct NavigationExample {\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];\n  private scrollerForScroll: Scroller = new Scroller();\n  @State barStyle: BarStyle = BarStyle.STANDARD;\n\n  build() {\n    Column() {\n      Navigation() {\n        Column() {\n          // 在Navigation中嵌套Column，实现布局层叠效果\n          Scroll(this.scrollerForScroll) {\n            Column() {\n              Image($r('app.media.image_1'))\n                // 设置与标题栏高度一致，以便观察STACK效果\n                .height(138)\n                .width('100%')\n              Button('BarStyle.STANDARD')\n                .height('50vp')\n                .onClick(() => {\n                  this.barStyle = BarStyle.STANDARD;\n                })\n              Button('BarStyle.STACK')\n                .height('50vp')\n                .margin({ top: 12 })\n                .onClick(() => {\n                  this.barStyle = BarStyle.STACK;\n                })\n\n              // 遍历数组，创建带有数字的ListItem\n              ForEach(this.arr, (item: number) => {\n                ListItem() {\n                  Text('' + item)\n                    .width('100%')\n                    .height(100)\n                    .fontSize(16)\n                    .textAlign(TextAlign.Center)\n                    .borderRadius(10)\n                    .backgroundColor(Color.Orange)\n                    .margin({ top: 12 })\n                }\n              }, (item: string) => item)\n            }\n          }\n        }\n        .width('100%')\n        .height('100%')\n        .backgroundColor(0xDCDCDC)\n      }\n      // 设置Navigation的标题内容和样式\n      .title(\n        {\n          main: 'NavTitle',\n          sub: 'subtitle'\n        },\n        {\n          backgroundBlurStyle: BlurStyle.COMPONENT_THICK,\n          barStyle: this.barStyle,\n        }\n      )\n      .titleMode(NavigationTitleMode.Free)\n      .hideTitleBar(false)\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}\n```\n\n在上述代码中：\n- `NavigationExample` 结构体定义了一个示例，展示了Navigation标题栏的STACK布局效果。\n- `barStyle` 为状态变量，用于控制标题栏的样式，包括 `BarStyle.STANDARD` 和 `BarStyle.STACK` 两种样式。\n- `build()` 方法构建了页面布局，包括嵌套的 `Column`、`Navigation`、`Scroll` 等组件。\n- `Image` 显示图片，高度设置与标题栏高度一致，用于观察STACK效果。\n- `Button` 组件用于切换标题栏样式，分别为 `BarStyle.STANDARD` 和 `BarStyle.STACK`。\n- `ForEach` 遍历数组 `arr`，创建带有数字的 `ListItem`，展示不同数字的方块。\n- `Navigation` 设置了标题栏的样式和内容，包括主标题、副标题、背景模糊样式和标题栏样式。\n- `titleMode(NavigationTitleMode.Free)` 设置标题栏自由模式，不固定在顶部。\n- `hideTitleBar(false)` 显示标题栏。\n- 页面整体设置了背景颜色为 `#F1F3F5`。\n@Entry\n@Component\nstruct NavigationExample {\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];\n  private scrollerForScroll: Scroller = new Scroller();\n  @State barStyle: BarStyle = BarStyle.STANDARD;\n\n  build() {\n    Column() {\n      Navigation() {\n        Column() {\n          Scroll(this.scrollerForScroll) {\n            Column() {\n              Image($r('app.media.image_1'))\n                // 设置与标题栏高度一致，以便观察STACK效果\n                .height(138)\n                .width('100%')\n              Button('BarStyle.STANDARD')\n                .height('50vp')\n                .onClick(() => {\n                  this.barStyle = BarStyle.STANDARD;\n                })\n              Button('BarStyle.STACK')\n                .height('50vp')\n                .margin({ top: 12 })\n                .onClick(() => {\n                  this.barStyle = BarStyle.STACK;\n                })\n\n              ForEach(this.arr, (item: number) => {\n                ListItem() {\n                  Text('' + item)\n                    .width('100%')\n                    .height(100)\n                    .fontSize(16)\n                    .textAlign(TextAlign.Center)\n                    .borderRadius(10)\n                    .backgroundColor(Color.Orange)\n                    .margin({ top: 12 })\n                }\n              }, (item: string) => item)\n            }\n          }\n        }\n        .width('100%')\n        .height('100%')\n        .backgroundColor(0xDCDCDC)\n      }\n      .title(\n        {\n          main: 'NavTitle',\n          sub: 'subtitle'\n        },\n        {\n          backgroundBlurStyle: BlurStyle.COMPONENT_THICK,\n          barStyle: this.barStyle,\n        }\n      )\n      .titleMode(NavigationTitleMode.Free)\n      .hideTitleBar(false)\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            """// 该示例主要演示如何定义NavPathStack的派生类和派生类在Navigation中的基本用法。\n\n// 定义派生类DerivedNavPathStack，扩展自NavPathStack\nclass DerivedNavPathStack extends NavPathStack {\n  // 用户定义属性'id'，默认值为'__default__'\n  id: string = "__default__"\n\n  // 设置id属性的方法\n  setId(id: string) {\n    this.id = id;\n  }\n\n  // 获取信息的方法\n  getInfo(): string {\n    return "this page used Derived NavPathStack, id: " + this.id\n  }\n\n  // 重写NavPathStack的pushPath方法\n  pushPath(info: NavPathInfo, animated?: boolean): void\n  pushPath(info: NavPathInfo, options?: NavigationOptions): void\n  pushPath(info: NavPathInfo, secArg?: boolean | NavigationOptions): void {\n    console.log('[derive-test] reached DerivedNavPathStack's pushPath');\n    if (typeof secArg === 'boolean') {\n      super.pushPath(info, secArg);\n    } else {\n      super.pushPath(info, secArg);\n    }\n  }\n\n  // 重写和重载NavPathStack的pop方法\n  pop(animated?: boolean | undefined): NavPathInfo | undefined\n  pop(result: Object, animated?: boolean | undefined): NavPathInfo | undefined\n  pop(result?: Object, animated?: boolean | undefined): NavPathInfo | undefined {\n    console.log('[derive-test] reached DerivedNavPathStack's pop');\n    return super.pop(result, animated);\n  }\n\n  // 其他基类函数...\n}\n\n// 定义参数类param\nclass param {\n  info: string = "__default_param__";\n  constructor(info: string) { this.info = info }\n}\n\n// 入口组件Index\n@Entry\n@Component\nstruct Index {\n  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();\n\n  // 生命周期钩子函数，页面即将显示时调用\n  aboutToAppear(): void {\n    this.derivedStack.setId('origin stack');\n  }\n\n  // 构建页面映射\n  @Builder\n  pageMap(name: string) {\n    PageOne()\n  }\n\n  // 构建页面\n  build() {\n    Navigation(this.derivedStack) {\n      Button('to Page One').margin(20).onClick(() => {\n        this.derivedStack.pushPath({\n          name: 'pageOne',\n          param: new param('push pageOne in homePage when stack size: ' + this.derivedStack.size())\n        });\n      })\n    }.navDestination(this.pageMap)\n    .title('Home Page')\n  }\n}\n\n// 页面组件PageOne\n@Component\nstruct PageOne {\n  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();\n  curStringifyParam: string = "NA";\n\n  // 构建页面\n  build() {\n    NavDestination() {\n      Column() {\n        // 显示DerivedNavPathStack的信息\n        Text(this.derivedStack.getInfo())\n          .margin(10)\n          .fontSize(25)\n          .fontWeight(FontWeight.Bold)\n          .textAlign(TextAlign.Start)\n        Text('current page param info:')\n          .margin(10)\n          .fontSize(25)\n          .fontWeight(FontWeight.Bold)\n          .textAlign(TextAlign.Start)\n        Text(this.curStringifyParam)\n          .margin(20)\n          .fontSize(20)\n          .textAlign(TextAlign.Start)\n      }.backgroundColor(Color.Pink)\n      Button('to Page One').margin(20).onClick(() => {\n        this.derivedStack.pushPath({\n          name: 'pageOne',\n          param: new param('push pageOne in pageOne when stack size: ' + this.derivedStack.size())\n        });\n      })\n    }.title('Page One')\n    .onReady((context: NavDestinationContext) => {\n      console.log('[derive-test] reached PageOne's onReady');\n      // 从NavDestinationContext中获取DerivedNavPathStack\n      this.derivedStack = context.pathStack as DerivedNavPathStack;\n      console.log('[derive-test] -- got derivedStack: ' + this.derivedStack.id);\n      this.curStringifyParam = JSON.stringify(context.pathInfo.param);\n      console.log('[derive-test] -- got param: ' + this.curStringifyParam);\n    })\n  }\n}\n```\nclass DerivedNavPathStack extends NavPathStack {\n  // usr defined property 'id'\n  id: string = "__default__"\n\n  // new function in derived class\n  setId(id: string) {\n    this.id = id;\n  }\n\n  // new function in derived class\n  getInfo(): string {\n    return "this page used Derived NavPathStack, id: " + this.id\n  }\n\n  // overwrite function of NavPathStack\n  pushPath(info: NavPathInfo, animated?: boolean): void\n  pushPath(info: NavPathInfo, options?: NavigationOptions): void\n  pushPath(info: NavPathInfo, secArg?: boolean | NavigationOptions): void {\n    console.log('[derive-test] reached DerivedNavPathStack\\'s pushPath');\n    if (typeof secArg === 'boolean') {\n      super.pushPath(info, secArg);\n    } else {\n      super.pushPath(info, secArg);\n    }\n  }\n\n  // overwrite and overload function of NavPathStack\n  pop(animated?: boolean | undefined): NavPathInfo | undefined\n  pop(result: Object, animated?: boolean | undefined): NavPathInfo | undefined\n  pop(result?: Object, animated?: boolean | undefined): NavPathInfo | undefined {\n    console.log('[derive-test] reached DerivedNavPathStack\\'s pop');\n    return super.pop(result, animated);\n  }\n\n  // other function of base class...\n}\n\nclass param {\n  info: string = "__default_param__";\n  constructor(info: string) { this.info = info }\n}\n\n@Entry\n@Component\nstruct Index {\n  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();\n\n  aboutToAppear(): void {\n    this.derivedStack.setId('origin stack');\n  }\n\n  @Builder\n  pageMap(name: string) {\n    PageOne()\n  }\n\n  build() {\n    Navigation(this.derivedStack) {\n      Button('to Page One').margin(20).onClick(() => {\n        this.derivedStack.pushPath({\n          name: 'pageOne',\n          param: new param('push pageOne in homePage when stack size: ' + this.derivedStack.size())\n        });\n      })\n    }.navDestination(this.pageMap)\n    .title('Home Page')\n  }\n}\n\n@Component\nstruct PageOne {\n  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();\n  curStringifyParam: string = "NA";\n\n  build() {\n    NavDestination() {\n      Column() {\n        Text(this.derivedStack.getInfo())\n          .margin(10)\n          .fontSize(25)\n          .fontWeight(FontWeight.Bold)\n          .textAlign(TextAlign.Start)\n        Text('current page param info:')\n          .margin(10)\n          .fontSize(25)\n          .fontWeight(FontWeight.Bold)\n          .textAlign(TextAlign.Start)\n        Text(this.curStringifyParam)\n          .margin(20)\n          .fontSize(20)\n          .textAlign(TextAlign.Start)\n      }.backgroundColor(Color.Pink)\n      Button('to Page One').margin(20).onClick(() => {\n        this.derivedStack.pushPath({\n          name: 'pageOne',\n          param: new param('push pageOne in pageOne when stack size: ' + this.derivedStack.size())\n        });\n      })\n    }.title('Page One')\n    .onReady((context: NavDestinationContext) => {\n      console.log('[derive-test] reached PageOne\\'s onReady');\n      // get derived stack from navdestinationContext\n      this.derivedStack = context.pathStack as DerivedNavPathStack;\n      console.log('[derive-test] -- got derivedStack: ' + this.derivedStack.id);\n      this.curStringifyParam = JSON.stringify(context.pathInfo.param);\n      console.log('[derive-test] -- got param: ' + this.curStringifyParam);\n    })\n  }\n}"""
            """/**\n * 该示例主要演示Navigation和NavDestination如何使用Symbol组件。\n */\n\n@Entry\n@Component\nstruct NavigationExample {\n  // 定义导航路径栈和菜单项\n  @Provide('navPathStack') navPathStack:NavPathStack = new NavPathStack();\n  @State menuItems:Array<NavigationMenuItem> = [\n    {\n      value:'menuItem1',\n      icon:'resources/base/media/ic_public_ok.svg' // 图标资源路径\n    },\n    {\n      value:'menuItem2',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n    },\n    {\n      value:'menuItem3',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n    },\n  ]\n\n  // 定义工具栏项\n  @State toolItems:Array<ToolbarItem>= [\n    {\n      value:'toolItem1',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n      action:()=>{}\n    },\n    {\n      value:'toolItem2',\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeIcon: 'resources/base/media/ic_public_more.svg', // 图标资源路径\n      action:()=>{}\n    },\n    {\n      value:'toolItem3',\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n      action:()=>{}\n    }\n  ]\n\n  // 定义路由构建器\n  @Builder\n  myRouter(name:string,param?:Object) {\n    if(name === 'NavigationMenu') {\n      NavigationMenu();\n    }\n  }\n\n  // 构建导航页面\n  build() {\n    Navigation(this.navPathStack) {\n      Column() {\n        Button('跳转').onClick(()=> {\n          this.navPathStack.pushPathByName('NavigationMenu', null);\n        })\n      }\n    }\n    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))\n    .titleMode(NavigationTitleMode.Mini)\n    .menus(this.menuItems)\n    .toolbarConfiguration(this.toolItems)\n    .title('一级页面')\n    .navDestination(this.myRouter)\n  }\n}\n\n@Component\nexport struct NavigationMenu{\n  @Consume('navPathStack') navPathStack:NavPathStack;\n  @State menuItems:Array<NavigationMenuItem> = [\n    {\n      value:'menuItem1',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action:()=>{}\n    },\n    {\n      value:'menuItem2',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n      action:()=>{}\n    },\n    {\n      value:'menuItem3',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat_1')),\n      action:()=>{}\n    },\n  ]\n\n  // 构建导航目的地页面\n  build() {\n    NavDestination(){\n      Row() {\n        Column(){\n        }\n        .width('100%')\n      }\n      .height('100%')\n    }\n    .hideTitleBar(false)\n    .title('NavDestination title')\n    .backgroundColor($r('sys.color.ohos_id_color_titlebar_sub_bg'))\n    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Blue]))\n    .menus(this.menuItems)\n  }\n}\n```\nimport { SymbolGlyphModifier } from '@kit.ArkUI';\n\n@Entry\n@Component\nstruct NavigationExample {\n  @Provide('navPathStack') navPathStack:NavPathStack = new NavPathStack();\n  @State menuItems:Array<NavigationMenuItem> = [\n    {\n      value:'menuItem1',\n      icon:'resources/base/media/ic_public_ok.svg' // 图标资源路径\n    },\n    {\n      value:'menuItem2',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n    },\n    {\n      value:'menuItem3',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n    },\n  ]\n\n  @State toolItems:Array<ToolbarItem>= [\n    {\n      value:'toolItem1',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n      action:()=>{}\n    },\n    {\n      value:'toolItem2',\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeIcon: 'resources/base/media/ic_public_more.svg', // 图标资源路径\n      action:()=>{}\n    },\n    {\n      value:'toolItem3',\n      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),\n      status:ToolbarItemStatus.ACTIVE,\n      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),\n      action:()=>{}\n    }\n  ]\n\n  @Builder\n  myRouter(name:string,param?:Object) {\n    if(name === 'NavigationMenu') {\n      NavigationMenu();\n    }\n  }\n\n  build() {\n    Navigation(this.navPathStack) {\n      Column() {\n        Button('跳转').onClick(()=> {\n          this.navPathStack.pushPathByName('NavigationMenu', null);\n        })\n      }\n    }\n    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))\n    .titleMode(NavigationTitleMode.Mini)\n    .menus(this.menuItems)\n    .toolbarConfiguration(this.toolItems)\n    .title('一级页面')\n    .navDestination(this.myRouter)\n  }\n}\n\n@Component\nexport struct NavigationMenu{\n  @Consume('navPathStack') navPathStack:NavPathStack;\n  @State menuItems:Array<NavigationMenuItem> = [\n    {\n      value:'menuItem1',\n      icon:'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action:()=>{}\n    },\n    {\n      value:'menuItem2',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),\n      action:()=>{}\n    },\n    {\n      value:'menuItem3',\n      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat_1')),\n      action:()=>{}\n    },\n  ]\n\n  build() {\n    NavDestination(){\n      Row() {\n        Column(){\n        }\n        .width('100%')\n      }\n      .height('100%')\n    }\n    .hideTitleBar(false)\n    .title('NavDestination title')\n    .backgroundColor($r('sys.color.ohos_id_color_titlebar_sub_bg'))\n    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Blue]))\n    .menus(this.menuItems)\n  }\n}"""
            """/**\n * 该示例演示了如何自定义设置标题栏边距，包括Navigation和NavDestination两个组件。\n * 开发者可以通过按钮点击事件切换标题栏内间距的大小，并跳转到另一个页面查看效果。\n */\n\n// NavigationExample组件\n@Entry\n@Component\nstruct NavigationExample {\n  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();\n  // 初始化标题栏起始端内间距\n  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);\n  // 初始化标题栏结束端内间距\n  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);\n  @State menuItems: Array<NavigationMenuItem> = [\n    {\n      value: 'menuItem1',\n      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action: () => {\n      }\n    }\n  ]\n\n  @Builder\n  myRouter(name: string, param?: Object) {\n    if (name === 'NavDestinationExample') {\n      NavDestinationExample();\n    }\n  }\n\n  build() {\n    Navigation(this.navPathStack) {\n      Column() {\n        // 切换标题栏内间距为16vp的按钮\n        Button('切换标题栏内间距为16vp')\n          .onClick(() => {\n            this.paddingStart = LengthMetrics.vp(16);\n            this.paddingEnd = LengthMetrics.vp(16);\n          })\n          .margin({ top: 5 })\n\n        // 切换标题栏内间距为24vp的按钮\n        Button('切换标题栏内间距为24vp')\n          .onClick(() => {\n            this.paddingStart = LengthMetrics.vp(24);\n            this.paddingEnd = LengthMetrics.vp(24);\n          })\n          .margin({ top: 5 })\n\n        // 跳转按钮\n        Button('跳转')\n          .onClick(() => {\n            this.navPathStack.pushPathByName('NavDestinationExample', null);\n          })\n          .margin({ top: 5 })\n      }\n    }\n    .titleMode(NavigationTitleMode.Mini)\n    .title('一级页面', {\n      paddingStart: this.paddingStart,\n      paddingEnd: this.paddingEnd,\n    })\n    .menus(this.menuItems)\n    .navDestination(this.myRouter)\n  }\n}\n\n// NavDestinationExample组件\n@Component\nexport struct NavDestinationExample {\n  @Consume('navPathStack') navPathStack: NavPathStack;\n  @State menuItems: Array<NavigationMenuItem> = [\n    {\n      value: 'menuItem1',\n      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action: () => {\n      }\n    }\n  ]\n  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);\n  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);\n\n  build() {\n    NavDestination() {\n      Row() {\n        Column() {\n          // 切换标题栏内间距为32vp的按钮\n          Button('切换标题栏内间距为32vp')\n            .onClick(() => {\n              this.paddingStart = LengthMetrics.vp(32);\n              this.paddingEnd = LengthMetrics.vp(32);\n            })\n            .margin({ top: 5 })\n\n          // 切换标题栏内间距为20vp的按钮\n          Button('切换标题栏内间距为20vp')\n            .onClick(() => {\n              this.paddingStart = LengthMetrics.vp(20);\n              this.paddingEnd = LengthMetrics.vp(20);\n            })\n            .margin({ top: 5 })\n        }\n        .width('100%')\n      }\n      .height('100%')\n    }\n    .hideTitleBar(false)\n    .title('NavDestination title', {\n      paddingStart: this.paddingStart,\n      paddingEnd: this.paddingEnd,\n    })\n    .menus(this.menuItems)\n  }\n}\n```\nimport { LengthMetrics } from '@kit.ArkUI';\n\n@Entry\n@Component\nstruct NavigationExample {\n  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();\n  // 初始化标题栏起始端内间距\n  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);\n  // 初始化标题栏结束端内间距\n  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);\n  @State menuItems: Array<NavigationMenuItem> = [\n    {\n      value: 'menuItem1',\n      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action: () => {\n      }\n    }\n  ]\n\n  @Builder\n  myRouter(name: string, param?: Object) {\n    if (name === 'NavDestinationExample') {\n      NavDestinationExample();\n    }\n  }\n\n  build() {\n    Navigation(this.navPathStack) {\n      Column() {\n        // 标题栏内间距切换\n        Button('切换标题栏内间距为16vp')\n          .onClick(() => {\n            this.paddingStart = LengthMetrics.vp(16);\n            this.paddingEnd = LengthMetrics.vp(16);\n          })\n          .margin({ top: 5 })\n\n        Button('切换标题栏内间距为24vp')\n          .onClick(() => {\n            this.paddingStart = LengthMetrics.vp(24);\n            this.paddingEnd = LengthMetrics.vp(24);\n          })\n          .margin({ top: 5 })\n\n        Button('跳转')\n          .onClick(() => {\n            this.navPathStack.pushPathByName('NavDestinationExample', null);\n          })\n          .margin({ top: 5 })\n      }\n    }\n    .titleMode(NavigationTitleMode.Mini)\n    .title('一级页面', {\n      paddingStart: this.paddingStart,\n      paddingEnd: this.paddingEnd,\n    })\n    .menus(this.menuItems)\n    .navDestination(this.myRouter)\n  }\n}\n\n@Component\nexport struct NavDestinationExample {\n  @Consume('navPathStack') navPathStack: NavPathStack;\n  @State menuItems: Array<NavigationMenuItem> = [\n    {\n      value: 'menuItem1',\n      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径\n      action: () => {\n      }\n    }\n  ]\n  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);\n  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);\n\n  build() {\n    NavDestination() {\n      Row() {\n        Column() {\n          // 标题栏内间距切换\n          Button('切换标题栏内间距为32vp')\n            .onClick(() => {\n              this.paddingStart = LengthMetrics.vp(32);\n              this.paddingEnd = LengthMetrics.vp(32);\n            })\n            .margin({ top: 5 })\n\n          Button('切换标题栏内间距为20vp')\n            .onClick(() => {\n              this.paddingStart = LengthMetrics.vp(20);\n              this.paddingEnd = LengthMetrics.vp(20);\n            })\n            .margin({ top: 5 })\n        }\n        .width('100%')\n      }\n      .height('100%')\n    }\n    .hideTitleBar(false)\n    .title('NavDestination title', {\n      paddingStart: this.paddingStart,\n      paddingEnd: this.paddingEnd,\n    })\n    .menus(this.menuItems)\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "NodeContainer": {
        "description": "基础组件，不支持尾随添加子节点。组件接受一个NodeController的实例接口。需要NodeController组合使用。该组件下仅支持挂载自定义节点FrameNode或者是BuilderNode中获取的根节点FrameNode。不支持挂载查询获得的原生系统组件代理节点。",
        "interfaces": [
            {
                "description": "NodeContainer(controller: NodeController)\n\n创建NodeContainer组件。",
                "params": {
                    "controller": {
                        "type": "NodeController",
                        "required": True,
                        "description": "NodeController用于控制NodeContainer中的节点的上树和下树，反映NodeContainer容器的生命周期。"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {},
        "examples": [
            """// 为按钮构建器添加功能与效果描述\n// 创建一个按钮构建器，包含文本和按钮组件，设置文本和按钮的样式属性\nfunction buttonBuilder(params: Params) {\n  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceEvenly }) {\n    // 创建文本组件并设置字体大小\n    Text(params.text)\n      .fontSize(12)\n    // 创建按钮组件并设置样式属性\n    Button(`This is a Button`, { type: ButtonType.Normal, stateEffect: true })\n      .fontSize(12)\n      .borderRadius(8)\n      .backgroundColor(0x317aff)\n  }\n  .height(100)\n  .width(200)\n}\n\n// 为节点控制器添加功能与效果描述\n// 创建自定义节点控制器，用于构建按钮组件\nclass MyNodeController extends NodeController {\n  private rootNode: BuilderNode<[Params]> | null = null;\n  private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);\n\n  // 构建节点并返回帧节点\n  makeNode(uiContext: UIContext): FrameNode | null {\n    if (this.rootNode === null) {\n      this.rootNode = new BuilderNode(uiContext);\n      this.rootNode.build(this.wrapBuilder, { text: "This is a Text" })\n    }\n    return this.rootNode.getFrameNode();\n  }\n}\n\n// 为入口组件添加功能与效果描述\n// 创建入口组件，包含一个自定义节点控制器，构建文本和按钮组件\n@Entry\n@Component\nstruct Index {\n  private baseNode: MyNodeController = new MyNodeController()\n\n  // 构建组件结构，包含文本和按钮组件\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceEvenly }) {\n      // 创建文本组件并设置字体大小和颜色\n      Text("This is a NodeContainer contains a text and a button ")\n        .fontSize(9)\n        .fontColor(0xCCCCCC)\n      // 创建节点容器并添加自定义节点控制器\n      NodeContainer(this.baseNode)\n        .borderWidth(1)\n        .onClick(() => {\n          console.log("click event");\n        })\n    }\n    .padding({ left: 35, right: 35, top: 35 })\n    .height(200)\n    .width(300)\n  }\n}\n```\nimport { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';\n\ndeclare class Params {\n  text: string\n}\n\n@Builder\nfunction buttonBuilder(params: Params) {\n  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceEvenly }) {\n    Text(params.text)\n      .fontSize(12)\n    Button(`This is a Button`, { type: ButtonType.Normal, stateEffect: true })\n      .fontSize(12)\n      .borderRadius(8)\n      .backgroundColor(0x317aff)\n  }\n  .height(100)\n  .width(200)\n}\n\nclass MyNodeController extends NodeController {\n  private rootNode: BuilderNode<[Params]> | null = null;\n  private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);\n\n  makeNode(uiContext: UIContext): FrameNode | null {\n    if (this.rootNode === null) {\n      this.rootNode = new BuilderNode(uiContext);\n      this.rootNode.build(this.wrapBuilder, { text: "This is a Text" })\n    }\n    return this.rootNode.getFrameNode();\n  }\n}\n\n\n\n@Entry\n@Component\nstruct Index {\n  private baseNode: MyNodeController = new MyNodeController()\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceEvenly }) {\n      Text("This is a NodeContainer contains a text and a button ")\n        .fontSize(9)\n        .fontColor(0xCCCCCC)\n      NodeContainer(this.baseNode)\n        .borderWidth(1)\n        .onClick(() => {\n          console.log("click event");\n        })\n    }\n    .padding({ left: 35, right: 35, top: 35 })\n    .height(200)\n    .width(300)\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "PatternLock": {
        "description": "图案密码锁组件，以九宫格图案的方式输入密码，用于密码验证场景。手指在PatternLock组件区域按下时开始进入输入状态，手指离开屏幕时结束输入状态完成密码输入。",
        "interfaces": [
            {
                "description": "PatternLock(controller?: PatternLockController)\n\n创建PatternLock组件。",
                "params": {
                    "controller": {
                        "type": "PatternLockController",
                        "required": False,
                        "description": "设置PatternLock组件控制器，可用于控制组件状态重置。"
                    }
                }
            }
        ],
        "attributes": {
            "sideLength": {
                "description": "sideLength(value: Length)\n\n设置组件的宽度和高度（宽高相同）。设置为0或负数时组件不显示。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "组件的宽度和高度。",
                        "default": "288vp"
                    }
                }
            },
            "circleRadius": {
                "description": "circleRadius(value: Length)\n\n设置宫格中圆点的半径。设置为0或负数时取默认值。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "宫格中圆点的半径。",
                        "default": "6vp"
                    }
                }
            },
            "regularColor": {
                "description": "regularColor(value: ResourceColor)\n\n设置宫格圆点在“未选中”状态的填充颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "宫格圆点在“未选中”状态的填充颜色。",
                        "default": "'#ff182431'"
                    }
                }
            },
            "selectedColor": {
                "description": "selectedColor(value: ResourceColor)\n\n设置宫格圆点在“选中“状态的填充颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "宫格圆点在“选中”状态的填充颜色。",
                        "default": "'#ff182431'"
                    }
                }
            },
            "activeColor": {
                "description": "activeColor(value: ResourceColor)\n\n设置宫格圆点在“激活”状态的填充颜色，“激活”状态为手指经过圆点但还未选中的状态。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "宫格圆点在“激活”状态的填充颜色。",
                        "default": "'#ff182431'"
                    }
                }
            },
            "pathColor": {
                "description": "pathColor(value: ResourceColor)\n\n设置连线的颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "连线的颜色。",
                        "default": "'#33182431'"
                    }
                }
            },
            "pathStrokeWidth": {
                "description": "pathStrokeWidth(value: number | string)\n\n设置连线的宽度。设置为0或负数时连线不显示。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "连线的宽度。",
                        "default": "12vp"
                    }
                }
            },
            "autoReset": {
                "description": "autoReset(value: boolean)\n\n设置在完成密码输入后再次在组件区域按下时是否重置组件状态。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "在完成密码输入后再次在组件区域按下时是否重置组件状态。",
                        "default": True
                    }
                }
            },
            "activateCircleStyle": {
                "description": "activateCircleStyle(options: Optional<CircleStyleOptions>)\n\n设置宫格圆点在“激活”状态的背景圆环样式。",
                "params": {
                    "options": {
                        "type": "CircleStyleOptions",
                        "required": True,
                        "description": "宫格圆点在“激活”状态的背景圆环样式。"
                    }
                }
            }
        },
        "events": {
            "onPatternComplete": {
                "description": "onPatternComplete(callback: (input: Array<number>) => void)\n\n密码输入结束时触发该回调。",
                "params": {
                    "input": {
                        "type": "Array<number>",
                        "required": True,
                        "description": "与选中宫格圆点顺序一致的数字数组，数字为选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点依次为3、4、5，第三行圆点依次为6、7、8）。"
                    }
                }
            },
            "onDotConnect": {
                "description": "onDotConnect(callback: CallBack<number>)\n\n密码输入选中宫格圆点时触发该回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "选中宫格圆点顺序的数字，数字为选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点依次为3、4、5，第三行圆点依次为6、7、8）。"
                    }
                }
            }
        },
        "examples": [
            """// xxx.ets\nimport { LengthUnit } from '@kit.ArkUI'\n\n@Entry\n@Component\nstruct PatternLockExample {\n  @State passwords: Number[] = [] // 用于存储密码的数组\n  @State message: string = 'please input password!' // 初始提示信息\n  private patternLockController: PatternLockController = new PatternLockController() // 创建密码锁控制器实例\n\n  build() {\n    Column() {\n      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20) // 展示提示信息\n      PatternLock(this.patternLockController)\n        .sideLength(200) // 设置密码锁边长\n        .circleRadius(9) // 设置密码锁圆圈半径\n        .pathStrokeWidth(18) // 设置密码路径线宽度\n        .activeColor('#B0C4DE') // 设置激活状态颜色\n        .selectedColor('#228B22') // 设置选中状态颜色\n        .pathColor('#90EE90') // 设置路径线颜色\n        .backgroundColor('#F5F5F5') // 设置背景颜色\n        .autoReset(true) // 设置是否自动重置密码锁\n        .activateCircleStyle({\n          color: '#90EE90', // 设置激活圆圈颜色\n          radius: { value: 16, unit: LengthUnit.VP }, // 设置激活圆圈半径\n          enableWaveEffect: true // 启用波浪效果\n        })\n        .onDotConnect((index: number) => {\n          console.log("onDotConnect index: " + index) // 当连接圆点时触发\n        })\n        .onPatternComplete((input: Array<number>) => {\n          // 判断密码长度是否符合要求\n          if (input === null || input === undefined || input.length < 5) {\n            this.message = 'The password length needs to be greater than 5, please enter again.' // 提示重新输入密码\n            return\n          }\n          // 判断是否已经设置过密码\n          if (this.passwords.length > 0) {\n            // 判断密码是否一致\n            if (this.passwords.toString() === input.toString()) {\n              this.passwords = input\n              this.message = 'Set password successfully: ' + this.passwords.toString() // 提示密码设置成功\n              this.patternLockController.setChallengeResult(PatternLockChallengeResult.CORRECT) // 设置密码锁挑战结果为正确\n            } else {\n              this.message = 'Inconsistent passwords, please enter again.' // 提示密码不一致，重新输入\n              this.patternLockController.setChallengeResult(PatternLockChallengeResult.WRONG) // 设置密码锁挑战结果为错误\n            }\n          } else {\n            this.passwords = input\n            this.message = "Please enter again." // 提示再次输入密码\n          }\n        })\n      Button('Reset PatternLock').margin(30).onClick(() => {\n        // 重置密码锁\n        this.patternLockController.reset()\n        this.passwords = []\n        this.message = 'Please input password' // 提示重新输入密码\n      })\n    }.width('100%').height('100%') // 设置布局宽高为100%\n  }\n}\n```\n// xxx.ets\nimport { LengthUnit } from '@kit.ArkUI'\n\n@Entry\n@Component\nstruct PatternLockExample {\n  @State passwords: Number[] = []\n  @State message: string = 'please input password!'\n  private patternLockController: PatternLockController = new PatternLockController()\n\n  build() {\n    Column() {\n      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)\n      PatternLock(this.patternLockController)\n        .sideLength(200)\n        .circleRadius(9)\n        .pathStrokeWidth(18)\n        .activeColor('#B0C4DE')\n        .selectedColor('#228B22')\n        .pathColor('#90EE90')\n        .backgroundColor('#F5F5F5')\n        .autoReset(true)\n        .activateCircleStyle({\n          color: '#90EE90',\n          radius: { value: 16, unit: LengthUnit.VP },\n          enableWaveEffect: true\n        })\n        .onDotConnect((index: number) => {\n          console.log("onDotConnect index: " + index)\n        })\n        .onPatternComplete((input: Array<number>) => {\n          // 输入的密码长度小于5时，提示重新输入\n          if (input === null || input === undefined || input.length < 5) {\n            this.message = 'The password length needs to be greater than 5, please enter again.'\n            return\n          }\n          // 判断密码长度是否大于0\n          if (this.passwords.length > 0) {\n            // 判断两次输入的密码是否相同，相同则提示密码设置成功，否则提示重新输入\n            if (this.passwords.toString() === input.toString()) {\n              this.passwords = input\n              this.message = 'Set password successfully: ' + this.passwords.toString()\n              this.patternLockController.setChallengeResult(PatternLockChallengeResult.CORRECT)\n            } else {\n              this.message = 'Inconsistent passwords, please enter again.'\n              this.patternLockController.setChallengeResult(PatternLockChallengeResult.WRONG)\n            }\n          } else {\n            // 提示第二次输入密码\n            this.passwords = input\n            this.message = "Please enter again."\n          }\n        })\n      Button('Reset PatternLock').margin(30).onClick(() => {\n        // 重置密码锁\n        this.patternLockController.reset()\n        this.passwords = []\n        this.message = 'Please input password'\n      })\n    }.width('100%').height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Progress": {
        "description": "进度条组件，用于显示内容加载或操作处理等进度。",
        "interfaces": [
            {
                "description": "创建进度组件，用于显示内容加载或操作处理进度。",
                "params": {
                    "options": {
                        "type": "ProgressOptions<Type>",
                        "required": True,
                        "description": "进度条组件参数。"
                    }
                }
            }
        ],
        "attributes": {
            "options": {
                "description": "进度条组件参数。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "指定当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。"
                    },
                    "total": {
                        "type": "number",
                        "required": False,
                        "description": "指定进度总长。设置小于等于0的数值时置为100。"
                    },
                    "type": {
                        "type": "[ProgressType]",
                        "required": False,
                        "description": "指定进度条类型。"
                    },
                    "style(deprecated)": {
                        "type": "[ProgressStyle]",
                        "required": False,
                        "description": "指定进度条样式。该参数从API version8开始废弃，建议使用type替代。"
                    }
                }
            },
            "value": {
                "description": "设置当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。非法数值不生效。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "当前进度值。"
                    }
                }
            },
            "color": {
                "description": "设置进度条前景色。",
                "params": {
                    "value": {
                        "type": "[ResourceColor | LinearGradient]",
                        "required": True,
                        "description": "进度条前景色。"
                    }
                }
            },
            "backgroundColor": {
                "description": "设置进度条底色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "进度条底色。"
                    }
                }
            },
            "style": {
                "description": "设置组件的样式。",
                "params": {
                    "value": {
                        "type": "ProgressStyleOptions | CapsuleStyleOptions | RingStyleOptions | LinearStyleOptions | ScaleRingStyleOptions | EclipseStyleOptions",
                        "required": True,
                        "description": "设置组件的样式。"
                    }
                }
            },
            "contentModifier": {
                "description": "定制progress内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<ProgressConfiguration>",
                        "required": True,
                        "description": "在progress组件上，定ressConfiguration>制内容区的方法。modifier:内容修改器，开发者需要自定义class实现ContentModifier接口。"
                    }
                }
            },
            "privacySensitive": {
                "description": "设置隐私敏感。",
                "params": {
                    "isPrivacySensitiveMode": {
                        "type": "[Optional<boolean>]",
                        "required": True,
                        "description": "设置隐私敏感，隐私模式下进度清零，文字将被遮罩。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """// xxx.ets\n@Entry\n@Component\nstruct ProgressExample {\n  build() {\n    Column({ space: 15 }) {\n      // 显示线性进度条的标题\n      Text('Linear Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      // 显示一个线性进度条，初始值为10，总长度为默认值100\n      Progress({ value: 10, type: ProgressType.Linear }).width(200)\n      // 显示一个线性进度条，初始值为50，总长度为150，颜色为灰色\n      Progress({ value: 20, total: 150, type: ProgressType.Linear }).color(Color.Grey).value(50).width(200)\n\n      // 显示环形进度条的标题\n      Text('Eclipse Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Row({ space: 40 }) {\n        // 显示一个环形进度条，初始值为10，总长度为默认值100\n        Progress({ value: 10, type: ProgressType.Eclipse }).width(100)\n        // 显示一个环形进度条，初始值为50，总长度为150，颜色为灰色\n        Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).value(50).width(100)\n      }\n\n      // 显示刻度环形进度条的标题\n      Text('ScaleRing Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Row({ space: 40 }) {\n        // 显示一个刻度环形进度条，初始值为10，总长度为默认值100\n        Progress({ value: 10, type: ProgressType.ScaleRing }).width(100)\n        // 显示一个刻度环形进度条，初始值为50，总长度为150，颜色为灰色，设置刻度和宽度\n        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })\n          .color(Color.Grey).value(50).width(100)\n          .style({ strokeWidth: 15, scaleCount: 15, scaleWidth: 5 })\n      }\n\n      // 对比不同刻度数量和宽度的效果\n      Row({ space: 40 }) {\n        // 显示一个刻度环形进度条，初始值为50，总长度为150，颜色为灰色，设置刻度和宽度\n        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })\n          .color(Color.Grey).value(50).width(100)\n          .style({ strokeWidth: 20, scaleCount: 20, scaleWidth: 5 })\n        // 显示一个刻度环形进度条，初始值为50，总长度为150，颜色为灰色，设置刻度和宽度\n        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })\n          .color(Color.Grey).value(50).width(100)\n          .style({ strokeWidth: 20, scaleCount: 30, scaleWidth: 3 })\n      }\n\n      // 显示环形进度条的标题\n      Text('Ring Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Row({ space: 40 }) {\n        // 显示一个环形进度条，初始值为10，总长度为默认值100\n        Progress({ value: 10, type: ProgressType.Ring }).width(100)\n        // 显示一个环形进度条，初始值为50，总长度为150，颜色为灰色，设置宽度\n        Progress({ value: 20, total: 150, type: ProgressType.Ring })\n          .color(Color.Grey).value(50).width(100)\n          .style({ strokeWidth: 20 })\n      }\n\n      // 显示胶囊进度条的标题\n      Text('Capsule Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Row({ space: 40 }) {\n        // 显示一个胶囊进度条，初始值为10，总长度为默认值100，高度为50\n        Progress({ value: 10, type: ProgressType.Capsule }).width(100).height(50)\n        // 显示一个胶囊进度条，初始值为50，总长度为150，颜色为灰色，高度为50\n        Progress({ value: 20, total: 150, type: ProgressType.Capsule })\n          .color(Color.Grey)\n          .value(50)\n          .width(100)\n          .height(50)\n      }\n    }.width('100%').margin({ top: 30 })\n  }\n}"""
            # """实例1：这段代码实现了一个展示不同类型进度条的示例组件。包括线性进度条、环形进度条、椭圆进度条、刻度环形进度条和胶囊形进度条。每种进度条都具有不同的样式和属性设置，如进度值、总进度、颜色、宽度等。通过展示不同类型的进度条，可以帮助用户了解各种进度条的外观和功能特点。\n\n具体实现包括：\n- 线性进度条：展示线性进度条的样式和属性设置，包括进度值、总进度、颜色和宽度。\n- 椭圆进度条：展示椭圆形进度条的样式和属性设置，包括进度值、总进度、颜色和宽度。\n- 刻度环形进度条：展示刻度环形进度条的样式和属性设置，包括进度值、总进度、颜色、宽度以及刻度相关设置。\n- 环形进度条：展示环形进度条的样式和属性设置，包括进度值、总进度、颜色和宽度。\n- 胶囊形进度条：展示胶囊形进度条的样式和属性设置，包括进度值、总进度、颜色、宽度和高度。\n// xxx.ets\n@Entry\n@Component\nstruct ProgressExample {\n  build() {\n    Column({ space: 15 }) {\n      Text('Linear Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Progress({ value: 10, type: ProgressType.Linear }).width(200)\n      Progress({ value: 20, total: 150, type: ProgressType.Linear }).color(Color.Grey).value(50).width(200)\n\n\n\n      Text('Eclipse Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Row({ space: 40 }) {\n        Progress({ value: 10, type: ProgressType.Eclipse }).width(100)\n        Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).value(50).width(100)\n      }\n\n      Text('ScaleRing Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Row({ space: 40 }) {\n        Progress({ value: 10, type: ProgressType.ScaleRing }).width(100)\n        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })\n          .color(Color.Grey).value(50).width(100)\n          .style({ strokeWidth: 15, scaleCount: 15, scaleWidth: 5 })\n      }\n\n      // scaleCount和scaleWidth效果对比\n      Row({ space: 40 }) {\n        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })\n          .color(Color.Grey).value(50).width(100)\n          .style({ strokeWidth: 20, scaleCount: 20, scaleWidth: 5 })\n        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })\n          .color(Color.Grey).value(50).width(100)\n          .style({ strokeWidth: 20, scaleCount: 30, scaleWidth: 3 })\n      }\n\n      Text('Ring Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Row({ space: 40 }) {\n        Progress({ value: 10, type: ProgressType.Ring }).width(100)\n        Progress({ value: 20, total: 150, type: ProgressType.Ring })\n          .color(Color.Grey).value(50).width(100)\n          .style({ strokeWidth: 20 })\n      }\n\n      Text('Capsule Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Row({ space: 40 }) {\n        Progress({ value: 10, type: ProgressType.Capsule }).width(100).height(50)\n        Progress({ value: 20, total: 150, type: ProgressType.Capsule })\n          .color(Color.Grey)\n          .value(50)\n          .width(100)\n          .height(50)\n      }\n    }.width('100%').margin({ top: 30 })\n  }\n}"""
            # """实例2：// ProgressExample结构体实现了一个进度示例组件，包括渐变颜色的进度条和带阴影的进度条。\n// 通过build方法构建组件，其中包括渐变颜色的进度条和带阴影的进度条，以及相关的文本说明。\n// ProgressExample结构体包含一个私有的渐变颜色线性渐变对象gradientColor，用于定义进度条的渐变颜色。\n// build方法中使用Column布局嵌套Text和Progress组件，展示渐变颜色的进度条和带阴影的进度条。\n// 第一个Progress组件使用渐变颜色，设置数值为70，总数为100，类型为环形，样式为宽度100，描边宽度20。\n// 第二个Progress组件设置数值为70，总数为100，类型为环形，样式为宽度120，颜色为橙色，描边宽度20，带阴影。\n// 整体布局设置为100%宽度，顶部内边距为5。\n// xxx.ets\n@Entry\n@Component\nstruct ProgressExample {\n  private gradientColor: LinearGradient = new LinearGradient([{ color: Color.Yellow, offset: 0.5 },\n                                                              { color: Color.Orange, offset: 1.0 }])\n  build() {\n    Column({ space: 15 }) {\n      Text('Gradient Color').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Progress({ value: 70, total: 100, type: ProgressType.Ring })\n        .width(100).style({ strokeWidth: 20 })\n        .color(this.gradientColor)\n\n      Text('Shadow').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Progress({ value: 70, total: 100, type: ProgressType.Ring })\n        .width(120).color(Color.Orange)\n        .style({ strokeWidth: 20, shadow: true })\n    }.width('100%').padding({ top: 5 })\n  }\n}"""
            # """实例3：该代码示例展示了一个自定义的进度条组件，包含了加载效果和扫描效果。进度条的样式和行为通过设置不同的属性来实现，如颜色、宽度、类型等。具体实现如下：\n\n1. 创建一个名为 ProgressExample 的结构体，用于定义进度条组件。\n2. 定义了两种不同样式的进度条：加载效果和扫描效果。\n3. 加载效果的进度条显示为蓝色，具有指定的数值和总数，以环形形式展示。\n4. 扫描效果的进度条显示为橙色，具有指定的数值和总数，以环形形式展示，并启用了扫描效果。\n5. 每个进度条下方有相应的文本说明，描述了进度条的作用或效果。\n6. 整体布局为垂直排列的列，宽度占满父容器，顶部留有一定的间距。\n// xxx.ets\n@Entry\n@Component\nstruct ProgressExample {\n  private gradientColor: LinearGradient = new LinearGradient([{ color: Color.Yellow, offset: 0.5 },\n                                                              { color: Color.Orange, offset: 1.0 }])\n  build() {\n    Column({ space: 15 }) {\n      Text('Loading Effect').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Progress({ value: 0, total: 100, type: ProgressType.Ring })\n        .width(100).color(Color.Blue)\n        .style({ strokeWidth: 20, status: ProgressStatus.LOADING })\n\n      Text('Scan Effect').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      Progress({ value: 30, total: 100, type: ProgressType.Ring })\n        .width(100).color(Color.Orange)\n        .style({ strokeWidth: 20, enableScanEffect: true })\n    }.width('100%').padding({ top: 5 })\n  }\n}"""
            # """实例4：\n该代码文件（xxx.ets）定义了一个名为ProgressExample的组件结构，用于展示一个进度条。在该组件中，通过build()方法构建了一个包含进度条的布局，进度条的数值为100，总数为100，类型为Capsule。进度条的样式设置包括边框颜色为蓝色、边框宽度为1、内容显示为'Installing...'、字体大小为13、字体样式为Normal、字体颜色为灰色，扫描效果禁用，默认百分比不显示。\n\nButtonExample结构定义了一个按钮示例组件，包括一个显示为“OK”的按钮和一个开关控件用于启用或禁用按钮。按钮点击时记录点击位置的坐标，并在按钮上显示这些坐标。按钮的按压状态和启用状态也会在按钮上显示。通过MyButtonStyle类和buildButton1函数自定义了按钮的样式和行为。按压时，圆圈变为红色，标题显示按压字样；未按压时，圆圈变为黑色，标题显示非按压字样。\n\nMyButtonStyle类实现了ContentModifier接口，用于应用按钮的自定义样式。buildButton1函数根据ButtonConfiguration配置参数构建按钮的内容，显示按钮是否启用、按压状态、点击位置x坐标、点击位置y坐标，并根据状态设置圆圈颜色和透明度。\n\n整体功能为展示一个自定义样式的按钮组件，实现了按钮的点击记录和状态显示，以及按钮的样式和行为定制。\n// xxx.ets\n@Entry\n@Component\nstruct ProgressExample {\n\n  build() {\n    Column({ space: 15 }) {\n      Row({ space: 40 }) {\n        Progress({ value: 100, total: 100,type: ProgressType.Capsule }).width(100).height(50)\n          .style({borderColor: Color.Blue, borderWidth: 1, content: 'Installing...',\n                  font: {size: 13, style: FontStyle.Normal}, fontColor: Color.Gray,\n                  enableScanEffect: false, showDefaultPercentage: false})\n      }\n    }.width('100%').padding({ top: 5 })\n  }\n}"""
            # """实例5：/**\n * 该代码定义了一个名为 Index 的组件，包含一个数字类型的状态值和一个 build 方法。\n * 在 build 方法中，创建了一个 Column 布局，包含两个进度条组件和一个按钮组件。\n * 第一个进度条显示了 enableSmoothEffect 为 true 时的样式，第二个进度条显示了 enableSmoothEffect 为 false 时的样式。\n * 按钮点击时会使状态值增加 10。\n * 整体布局宽度为 50%，高度为 100%，左边距为 20。\n */\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  @State value: number = 0\n\n  build() {\n    Column({space: 10}) {\n      Text('enableSmoothEffect: true').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(5)\n        .margin({top: 20})\n      Progress({value: this.value, total: 100, type:ProgressType.Linear})\n        .style({strokeWidth: 10, enableSmoothEffect: true})\n\n      Text('enableSmoothEffect: false').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(5)\n      Progress({value: this.value, total: 100, type:ProgressType.Linear})\n        .style({strokeWidth: 10, enableSmoothEffect: false})\n\n      Button('value +10').onClick(() => {\n        this.value += 10\n      })\n        .width(75)\n        .height(15)\n        .fontSize(9)\n    }\n    .width('50%')\n    .height('100%')\n    .margin({left:20})\n  }\n}"""
            # """实例6：// MyProgressModifier 类实现了 ContentModifier 接口，用于自定义进度条样式。\n// 通过构造函数可以传入颜色参数来设置进度条的颜色。\n// applyContent 方法返回一个 WrappedBuilder，用于包装 myProgress 函数。\n// myProgress 函数定义了一个进度条的显示逻辑，根据配置参数显示不同的进度条状态。\n// Index 结构体作为入口组件，包含了当前进度值、进度条样式修改器等状态。\n// build 方法定义了页面的布局结构，包括显示当前进度条、增加和减少进度按钮的逻辑。\n// 按钮点击事件会更新当前进度值，并根据值的变化更新进度条的显示状态。\n// xxx.ets\nclass MyProgressModifier implements ContentModifier<ProgressConfiguration> {\n  color: Color = Color.White\n\n\n\n  constructor(color:Color) {\n    this.color = color\n  }\n  applyContent() : WrappedBuilder<[ProgressConfiguration]>\n  {\n    return wrapBuilder(myProgress)\n  }\n}\n\n@Builder function myProgress(config: ProgressConfiguration ) {\n\n  Column({space:30}) {\n    Text("当前进度：" + config.value + "/" + config.total).fontSize(20)\n    Row() {\n      Flex({ justifyContent: FlexAlign.SpaceBetween }) {\n        Path()\n          .width('30%')\n          .height('30%')\n          .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')\n          .fill(config.enabled && config.value >=1 ? (config.contentModifier as MyProgressModifier).color : Color.White)\n          .stroke(Color.Black)\n          .strokeWidth(3)\n        Path()\n          .width('30%')\n          .height('30%')\n          .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')\n          .fill(config.enabled && config.value >=2 ? (config.contentModifier as MyProgressModifier).color : Color.White)\n          .stroke(Color.Black)\n          .strokeWidth(3)\n        Path()\n          .width('30%')\n          .height('30%')\n          .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')\n          .fill(config.enabled && config.value >=3 ? (config.contentModifier as MyProgressModifier).color : Color.White)\n          .stroke(Color.Black)\n          .strokeWidth(3)\n      }.width('100%')\n    }\n  }.margin({bottom:100})\n}\n\n@Entry\n@Component\nstruct Index {\n  @State currentValue: number = 0\n  modifier = new MyProgressModifier(Color.Red)\n  @State myModifier:(MyProgressModifier | undefined)  = this.modifier\n  build() {\n    Column() {\n        Progress({ value: this.currentValue, total: 3, type: ProgressType.Ring}).contentModifier(this.modifier)\n        Button('Progress++').onClick(()=>{\n          if (this.currentValue < 3) {\n            this.currentValue += 1\n          }\n        }).width('30%')\n        Button('addProgress--').onClick(()=>{\n          if (this.currentValue > 0) {\n            this.currentValue -= 1\n          }\n        }).width('30%')\n    }.width('100%').height('100%')\n  }\n}"""
            # """实例7：/**\n * 这段代码实现了一个展示进度条的示例组件。\n * 进度条显示当前进度值和总进度值，以胶囊形式展示。进度条样式可以自定义，包括边框颜色、宽度、高度、内容、字体样式、字体颜色等。\n * 进度条还支持隐私敏感设置，可以设置扫描效果和显示默认百分比。在代码中，通过调用 Progress() 方法来创建进度条，并设置相关属性。\n * 该示例展示了如何在组件中嵌套使用 Scroll、Column、Row 等布局组件来构建界面布局，实现进度条的显示和样式设置。\n */\n@Entry\n@Component\nstruct ProgressExample {\n  build() {\n    Scroll() {\n      Column({ space: 15 }) {\n        Row() {\n          Progress({ value: 50, total: 100, type: ProgressType.Capsule }).width(100).height(50)\n            .style({\n              borderColor: Color.Blue,\n              borderWidth: 1,\n              content: 'Installing...',\n              font: { size: 13, style: FontStyle.Normal },\n              fontColor: Color.Gray,\n              enableScanEffect: false,\n              showDefaultPercentage: true\n            })\n            .privacySensitive(true)\n        }\n      }\n    }\n  }\n}"""
        ]
    },
    "QRCode": {
        "description": "用于显示单个二维码的组件。",
        "interfaces": [
            {
                "description": "QRCode(value: string)\n\n创建二维码组件。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "二维码内容字符串。最大支持256个字符，若超出，则截取前256个字符。"
                    }
                }
            }
        ],
        "attributes": {
            "color": {
                "description": "color(value: ResourceColor)\n\n设置二维码颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "二维码颜色。",
                        "default": "#ff182431"
                    }
                }
            },
            "backgroundColor": {
                "description": "backgroundColor(value: ResourceColor)\n\n设置二维码背景颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "二维码背景颜色。",
                        "default": "#ffffffff"
                    }
                }
            },
            "contentOpacity": {
                "description": "contentOpacity(value: number | Resource)\n\n设置二维码内容颜色的不透明度。不透明度最小值为0，最大值为1。",
                "params": {
                    "value": {
                        "type": ["number", "Resource"],
                        "required": True,
                        "description": "二维码内容颜色的不透明度。",
                        "default": 1
                    }
                }
            }
        },
        "events": {
            "onClick": {
                "description": "点击事件。",
                "params": {}
            },
            "onTouch": {
                "description": "触摸事件。",
                "params": {}
            },
            "onAttach": {
                "description": "组件挂载至组件树时触发此回调。",
                "params": {}
            },
            "onDetach": {
                "description": "组件从组件树卸载时触发此回调。。",
                "params": {}
            }
        },
        "examples": [
            """// xxx.ets\n@Entry\n@Component\nstruct QRCodeExample {\n  private value: string = 'hello world'\n\n  // 创建包含不同二维码效果的列布局\n  build() {\n    Column({ space: 5 }) {\n      // 显示普通二维码\n      Text('normal').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)\n      QRCode(this.value).width(140).height(140)\n\n      // 设置二维码颜色为金黄色\n      Text('color').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)\n      QRCode(this.value).color(0xF7CE00).width(140).height(140)\n\n      // 设置二维码背景色为橙色\n      Text('backgroundColor').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)\n      QRCode(this.value).width(140).height(140).backgroundColor(Color.Orange)\n\n      // 设置二维码内容不透明度为0.1\n      Text('contentOpacity').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)\n      QRCode(this.value).width(140).height(140).color(Color.Black).contentOpacity(0.1)\n    }.width('100%').margin({ top: 5 })\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct QRCodeExample {\n  private value: string = 'hello world'\n  build() {\n    Column({ space: 5 }) {\n      Text('normal').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)\n      QRCode(this.value).width(140).height(140)\n\n      // 设置二维码颜色\n      Text('color').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)\n      QRCode(this.value).color(0xF7CE00).width(140).height(140)\n\n      // 设置二维码背景色\n      Text('backgroundColor').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)\n      QRCode(this.value).width(140).height(140).backgroundColor(Color.Orange)\n\n      // 设置二维码不透明度\n      Text('contentOpacity').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)\n      QRCode(this.value).width(140).height(140).color(Color.Black).contentOpacity(0.1)\n    }.width('100%').margin({ top: 5 })\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Radio": {
        "description": "单选框，提供相应的用户交互选择项。",
        "interfaces": [
            {
                "description": "创建单选框组件。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前单选框的值。"
                    },
                    "group": {
                        "type": "string",
                        "required": True,
                        "description": "当前单选框的所属群组名称，相同group的Radio只能有一个被选中。"
                    },
                    "indicatorType": {
                        "type": "RadioIndicatorType",
                        "required": False,
                        "description": "配置单选框的选中样式。未设置时按照RadioIndicatorType.TICK进行显示。"
                    },
                    "indicatorBuilder": {
                        "type": "CustomBuilder",
                        "required": False,
                        "description": "配置单选框的选中样式为自定义组件。自定义组件与Radio组件为中心点对齐显示。indicatorBuilder设置为undefined时，按照RadioIndicatorType.TICK进行显示。"
                    }
                }
            },
            {
                "description": "设置单选框的选中状态。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "单选框的选中状态。"
                    }
                }
            },
            {
                "description": "设置单选框选中状态和非选中状态的样式。",
                "params": {
                    "value": {
                        "type": "RadioStyle",
                        "required": False,
                        "description": "单选框选中状态和非选中状态的样式。"
                    }
                }
            },
            {
                "description": "定制Radio内容区的方法。",
                "params": {}
            },
            {
                "description": "单选框选中状态改变时触发回调。",
                "params": {
                    "isChecked": {
                        "type": "boolean",
                        "required": True,
                        "description": "单选框的状态。为true时，表示从未选中变为选中。为false时，表示从选中变为未选中。"
                    }
                }
            }
        ],
        "attributes": {
            "checkedBackgroundColor": {
                "description": "开启状态底板颜色。",
                "params": {
                    "type": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "开启状态底板颜色。"
                    }
                }
            },
            "uncheckedBorderColor": {
                "description": "关闭状态描边颜色。",
                "params": {
                    "type": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "关闭状态描边颜色。"
                    }
                }
            },
            "indicatorColor": {
                "description": "开启状态内部圆饼颜色。",
                "params": {
                    "type": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "开启状态内部圆饼颜色。从API version 12开始，indicatorType设置为RadioIndicatorType.TICK和RadioIndicatorType.DOT时，支持修改内部颜色。indicatorType设置为RadioIndicatorType.CUSTOM时，不支持修改内部颜色。"
                    }
                }
            }
        },
        "events": {
            "checked": {
                "description": "设置单选框的选中状态。",
                "params": {
                    "value": {
                        "description": "单选框的选中状态。",
                        "type": "boolean",
                        "required": True,
                        "default": False
                    }
                }
            },
            "onChange": {
                "description": "单选框选中状态改变时触发回调。",
                "params": {
                    "isChecked": {
                        "type": "boolean",
                        "required": True,
                        "description": "单选框的状态。为true时，表示从未选中变为选中。为false时，表示从选中变为未选中。"
                    }
                }
            }
        },
        "examples": [
            "/*\n实现思路：\n本示例展示了如何使用ArkUI框架中的Radio组件来实现单选按钮功能。通过创建多个Radio组件并将其分组，确保同一组内的Radio组件互斥选择。每个Radio组件都设置了初始选中状态和样式，并监听其选中状态的变化，以便在用户选择时进行相应的处理。\n\n总体功能与效果描述：\n该示例展示了三个单选按钮，用户可以选择其中一个。每个单选按钮的选中状态变化会被监听，并在控制台输出相应的状态信息。\n*/\n\n// RadioExample.ets\n@Entry\n@Component\nstruct RadioExample {\n  build() {\n    // 创建一个Flex布局，水平和垂直居中对齐其子组件\n    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n      Column() {\n        Text('Radio1')\n        // 创建一个Radio组件，设置其初始选中状态和样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和样式以确保其显示效果。\n        Radio({ value: 'Radio1', group: 'radioGroup' }).checked(true)\n          .radioStyle({\n            checkedBackgroundColor: Color.Pink\n          })\n          .height(50)\n          .width(50)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio1 status is ' + isChecked)\n          })\n      }\n      Column() {\n        Text('Radio2')\n        // 创建一个Radio组件，设置其初始选中状态和样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和样式以确保其显示效果。\n        Radio({ value: 'Radio2', group: 'radioGroup' }).checked(false)\n          .radioStyle({\n            checkedBackgroundColor: Color.Pink\n          })\n          .height(50)\n          .width(50)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio2 status is ' + isChecked)\n          })\n      }\n      Column() {\n        Text('Radio3')\n        // 创建一个Radio组件，设置其初始选中状态和样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和样式以确保其显示效果。\n        Radio({ value: 'Radio3', group: 'radioGroup' }).checked(false)\n          .radioStyle({\n            checkedBackgroundColor: Color.Pink\n          })\n          .height(50)\n          .width(50)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio3 status is ' + isChecked)\n          })\n      }\n    }.padding({ top: 30 })\n  }\n}",
            "/*\n设置选中样式为图片。\n实现思路：\n本示例通过使用鸿蒙ArkUI框架，构建了一个包含三个Radio组件的界面。每个Radio组件都包含一个文本标签，用于标识不同的选项。通过Flex布局和Column组件的使用，确保Radio组件在界面中水平排列，并且每个组件都有自己的列布局。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听。此外，还使用了不同的指示器类型和自定义指示器来增强视觉效果。\n\n总体功能与效果描述：\n该界面展示了三个Radio组件，每个组件旁边都有一个文本标签。用户可以通过点击Radio来选择某个选项，同时其他选项会自动取消选中。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听，以便在用户选择时进行相应的处理。此外，还使用了不同的指示器类型和自定义指示器来增强视觉效果。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct RadioExample {\n  @Builder \n  indicatorBuilder() {\n    // 创建一个自定义的指示器，使用一个星形图标\n    // 功能与效果描述：自定义指示器用于在Radio组件选中时显示一个星形图标。\n    Image($r(\"app.media.star\"))\n  }\n  build() {\n    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n      Column() {\n        Text('Radio1')\n        // 创建一个Radio组件，设置其初始选中状态和指示器类型\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和指示器类型以确保其显示效果。\n        Radio({ value: 'Radio1', group: 'radioGroup',\n          indicatorType:RadioIndicatorType.TICK\n        }).checked(true)\n          .height(50)\n          .width(80)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio1 status is ' + isChecked)\n          })\n      }\n      Column() {\n        Text('Radio2')\n        // 创建一个Radio组件，设置其初始选中状态和指示器类型\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和指示器类型以确保其显示效果。\n        Radio({ value: 'Radio2', group: 'radioGroup',\n          indicatorType:RadioIndicatorType.DOT\n        }).checked(false)\n          .height(50)\n          .width(80)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio2 status is ' + isChecked)\n          })\n      }\n      Column() {\n        Text('Radio3')\n        // 创建一个Radio组件，设置其初始选中状态和自定义指示器\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和自定义指示器以确保其显示效果。\n        Radio({ value: 'Radio3', group: 'radioGroup',\n          indicatorType:RadioIndicatorType.CUSTOM,\n          indicatorBuilder:()=>{this.indicatorBuilder()}\n        }).checked(false)\n          .height(50)\n          .width(80)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio3 status is ' + isChecked)\n          })\n      }\n    }.padding({ top: 30 })\n  }\n}",
            "/*\n设置自定义单选样式\n实现思路：\n本示例通过使用鸿蒙ArkUI框架，构建了一个包含两个自定义样式的Radio组件的界面。每个Radio组件都包含一个自定义的样式类`MyRadioStyle`，用于设置Radio组件的选中颜色和类型。通过自定义的`buildRadio`函数，实现了Radio组件的布局和样式。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听。\n\n总体功能与效果描述：\n该界面展示了两个自定义样式的Radio组件。用户可以通过点击Radio来选择某个选项，同时其他选项会自动取消选中。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听，以便在用户选择时进行相应的处理。自定义样式类`MyRadioStyle`用于设置Radio组件的选中颜色和类型，增强了视觉效果。\n*/\n\n// 定义一个自定义样式类，用于设置Radio组件的选中颜色和类型\n// 功能与效果描述：自定义样式类用于设置Radio组件的选中颜色和类型，以便在用户选择时进行相应的处理。\nclass MyRadioStyle implements ContentModifier<RadioConfiguration> {\n  type: number = 0\n  selectedColor: Color = Color.Black\n\n  constructor(numberType: number, colorType: Color) {\n    this.type = numberType\n    this.selectedColor = colorType\n  }\n\n  applyContent(): WrappedBuilder<[RadioConfiguration]> {\n    return wrapBuilder(buildRadio)\n  }\n}\n\n// 定义一个自定义的Radio组件布局和样式函数\n// 功能与效果描述：自定义的Radio组件布局和样式函数用于设置Radio组件的布局和样式，以便在用户选择时进行相应的处理。\n@Builder function buildRadio(config: RadioConfiguration) {\n  Row({ space: 30 }) {\n    Circle({ width: 50, height: 50 })\n      .stroke(Color.Black)\n      .fill(config.checked ? (config.contentModifier as MyRadioStyle).selectedColor : Color.White)\n    Button(config.checked ? \"off\" : \"on\")\n      .width(100)\n      .type(config.checked ? (config.contentModifier as MyRadioStyle).type : ButtonType.Normal)\n      .backgroundColor(0xAABBCC)\n      .onClick(() => {\n        if (config.checked) {\n          config.triggerChange(false)\n        } else {\n          config.triggerChange(true)\n        }\n      })\n  }\n}\n\n@Entry\n@Component\nstruct refreshExample {\n  build() {\n    Column({ space: 50 }) {\n      Row() {\n        // 创建一个Radio组件，设置其初始选中状态和自定义样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和自定义样式以确保其显示效果。\n        Radio({ value: 'Radio1', group: 'radioGroup' })\n          .contentModifier(new MyRadioStyle(1, Color.Red))\n          .checked(false)\n          .width(300)\n          .height(100)\n      }\n      Row() {\n        // 创建一个Radio组件，设置其初始选中状态和自定义样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和自定义样式以确保其显示效果。\n        Radio({ value: 'Radio2', group: 'radioGroup' })\n          .checked(true)\n          .width(300)\n          .height(60)\n          .contentModifier(new MyRadioStyle(2, Color.Red))\n      }\n    }\n  }\n}",
            "/*\n实现思路：\n本示例展示了如何使用ArkUI框架中的Flex布局和Radio组件来创建一个简单的单选按钮组。通过使用Flex布局来确保子组件在水平和垂直方向上居中对齐，并使用Radio组件来实现单选按钮功能。每个Radio组件都设置了固定的大小，并配有一个文本标签来标识其选项。\n\n总体功能与效果描述：\n该示例展示了两个单选按钮，每个按钮都包含一个文本标签。整个布局使用了Flex布局来确保按钮和文本标签在水平和垂直方向上居中对齐。\n*/\n\n// Index.ets\n@Entry\n@Component\nstruct Index {\n  build() {\n    Row() {\n      Column() {\n        // 创建一个Flex布局，水平和垂直居中对齐其子组件\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          Radio({ value: 'value1', group: 'radioGroup' })\n            .width(30)\n            .height(30)\n          // 创建文本标签，设置字体大小\n          Text('Radio1').fontSize(20)\n        }\n\n        // 创建另一个Flex布局，水平和垂直居中对齐其子组件\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          Radio({ value: 'value2', group: 'radioGroup' })\n            .width(30)\n            .height(30)\n          // 创建文本标签，设置字体大小\n          Text('Radio2').fontSize(20)\n        }\n      }\n      .width('100%') // 设置Column的宽度为100%\n    }\n    .height('100%') // 设置Row的高度为100%\n  }\n}"
        ]
    },
    "Rating": {
        "description": "提供在给定范围内选择评分的组件。Rating组件的接口，用于设置评分值和是否作为指示器使用。",
        "interfaces": [
            {
                "description": "Rating(options?: { rating: number, indicator?: boolean })",
                "params": {
                    "rating": {
                        "type": "number",
                        "required": True,
                        "description": "设置并接收评分值。取值范围：[0, stars]。小于0取0，大于stars取最大值stars。从API version 10开始，该参数支持双向绑定变量。",
                        "default": 0
                    },
                    "indicator": {
                        "type": "boolean",
                        "required": False,
                        "description": "设置评分组件作为指示器使用，不可改变评分。",
                        "default": False
                    }
                }
            }
        ],
        "attributes": {
            "stars": {
                "description": "stars(value: number)",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "设置评分总数。",
                        "default": 5
                    }
                }
            },
            "stepSize": {
                "description": "stepSize(value: number)",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "设置操作评级的步长。",
                        "default": 0.5,
                        "range": "[0.1, stars]"
                    }
                }
            },
            "starStyle": {
                "description": "starStyle(value: { backgroundUri: string, foregroundUri: string, secondaryUri?: string })",
                "params": {
                    "value": {
                        "type": {
                            "backgroundUri": "string",
                            "foregroundUri": "string",
                            "secondaryUri": "string"
                        },
                        "required": True,
                        "description": "backgroundUri：未选中的星级的图片链接，可由用户自定义或使用系统默认图片。foregroundUri：选中的星级的图片路径，可由用户自定义或使用系统默认图片。secondaryUri：部分选中的星级的图片路径，可由用户自定义或使用系统默认图片。说明：backgroundUri或者foregroundUri或者secondaryUri设置的图片路径错误时，图片不显示。backgroundUri或者foregroundUri设置为undefined或者空字符串时，rating会选择加载系统默认星型图源。secondaryUri不设置或者设置的值为undefined或者空字符串时，优先设置为backgroundUri，效果上等同于只设置了foregroundUri、backgroundUri。",
                    }
                }
            },
            "contentModifier": {
                "description": "contentModifier(modifier: ContentModifier<RatingConfiguration>)",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<RatingConfiguration>",
                        "required": True,
                        "description": "定制Rating内容区的方法。"
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "onChange(callback:(value: number) => void)",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "评分条的评分。"
                    }
                }
            }
        },
        "examples": [
            """// RatingExample.ets\n\n@Entry\n@Component\nstruct RatingExample {\n  @State rating: number = 3.5 // 初始评分为3.5\n\n  build() {\n    Column() {\n      Column() {\n        // 创建一个评分组件，包括星星数量、步长、边距等设置，支持评分变化时的回调\n        Rating({ rating: this.rating, indicator: false })\n          .stars(5) // 设置星星数量为5\n          .stepSize(0.5) // 设置步长为0.5\n          .margin({ top: 24 }) // 设置边距\n          .onChange((value: number) => {\n            this.rating = value // 当评分变化时更新当前评分值\n          })\n        Text('current score is ' + this.rating)\n          .fontSize(16) // 设置字体大小\n          .fontColor('rgba(24,36,49,0.60)') // 设置字体颜色\n          .margin({ top: 16 }) // 设置边距\n      }.width(360).height(113).backgroundColor('#FFFFFF').margin({ top: 68 }) // 设置宽度、高度、背景色和边距\n\n      Row() {\n        // 创建一个圆形头像图片\n        Image('common/testImage.jpg')\n          .width(40) // 设置宽度\n          .height(40) // 设置高度\n          .borderRadius(20) // 设置圆角半径\n          .margin({ left: 24 }) // 设置边距\n        Column() {\n          Text('Yue')\n            .fontSize(16) // 设置字体大小\n            .fontColor('#182431') // 设置字体颜色\n            .fontWeight(500) // 设置字体粗细\n          Row() {\n            // 创建一个评分组件，显示日期信息\n            Rating({ rating: 3.5, indicator: false }).margin({ top: 1, right: 8 }) // 设置评分和边距\n            Text('2021/06/02')\n              .fontSize(10) // 设置字体大小\n              .fontColor('#182431') // 设置字体颜色\n          }\n        }.margin({ left: 12 }).alignItems(HorizontalAlign.Start) // 设置边距和对齐方式\n\n        Text('1st Floor')\n          .fontSize(10) // 设置字体大小\n          .fontColor('#182431') // 设置字体颜色\n          .position({ x: 295, y: 8 }) // 设置位置\n      }.width(360).height(56).backgroundColor('#FFFFFF').margin({ top: 64 }) // 设置宽度、高度、背景色和边距\n    }.width('100%').height('100%').backgroundColor('#F1F3F5') // 设置宽度、高度和背景色\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct RatingExample {\n  @State rating: number = 3.5\n\n  build() {\n    Column() {\n      Column() {\n        Rating({ rating: this.rating, indicator: false })\n          .stars(5)\n          .stepSize(0.5)\n          .margin({ top: 24 })\n          .onChange((value: number) => {\n            this.rating = value\n          })\n        Text('current score is ' + this.rating)\n          .fontSize(16)\n          .fontColor('rgba(24,36,49,0.60)')\n          .margin({ top: 16 })\n      }.width(360).height(113).backgroundColor('#FFFFFF').margin({ top: 68 })\n\n      Row() {\n        Image('common/testImage.jpg')\n          .width(40)\n          .height(40)\n          .borderRadius(20)\n          .margin({ left: 24 })\n        Column() {\n          Text('Yue')\n            .fontSize(16)\n            .fontColor('#182431')\n            .fontWeight(500)\n          Row() {\n            Rating({ rating: 3.5, indicator: false }).margin({ top: 1, right: 8 })\n            Text('2021/06/02')\n              .fontSize(10)\n              .fontColor('#182431')\n          }\n        }.margin({ left: 12 }).alignItems(HorizontalAlign.Start)\n\n        Text('1st Floor')\n          .fontSize(10)\n          .fontColor('#182431')\n          .position({ x: 295, y: 8 })\n      }.width(360).height(56).backgroundColor('#FFFFFF').margin({ top: 64 })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            """// xxx.ets\n@Entry\n@Component\nstruct RatingExample {\n  @State rating: number = 3.5\n\n  build() {\n    Column() {\n      // 创建一个评分组件，包括星级评分和当前评分显示\n      Rating({ rating: this.rating, indicator: false })\n        .stars(5) // 设置星星总数为5\n        .stepSize(0.5) // 设置评分步长为0.5\n        .starStyle({\n          backgroundUri: '/common/imag1.png', // 设置背景星星图片路径\n          foregroundUri: '/common/imag2.png', // 设置前景星星图片路径\n          secondaryUri: '/common/imag3.png' // 设置次要星星图片路径\n        })\n        .margin({ top: 24 }) // 设置评分组件的上边距\n        .onChange((value: number) => {\n          this.rating = value // 当评分改变时更新当前评分值\n        })\n      // 显示当前评分值的文本\n      Text('current score is ' + this.rating)\n        .fontSize(16) // 设置字体大小为16\n        .fontColor('rgba(24,36,49,0.60)') // 设置字体颜色\n        .margin({ top: 16 }) // 设置文本的上边距\n    }.width('100%').height('100%').backgroundColor('#F1F3F5') // 设置Column组件的宽度、高度和背景颜色\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct RatingExample {\n  @State rating: number = 3.5\n\n  build() {\n    Column() {\n      Rating({ rating: this.rating, indicator: false })\n        .stars(5)\n        .stepSize(0.5)\n        .starStyle({\n          backgroundUri: '/common/imag1.png', // common目录与pages同级\n          foregroundUri: '/common/imag2.png',\n          secondaryUri: '/common/imag3.png'\n        })\n        .margin({ top: 24 })\n        .onChange((value: number) => {\n          this.rating = value\n        })\n      Text('current score is ' + this.rating)\n        .fontSize(16)\n        .fontColor('rgba(24,36,49,0.60)')\n        .margin({ top: 16 })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            """// 该示例实现了自定义评分条的功能，每个圆圈表示0.5分。ratingIndicator为true时表示评分条作为一个指示器不可改变评分；为false时可以进行评分。ratingStars可改变评分总数。ratingStepsize可改变评分步长。\n\n// MyRatingStyle类用于定义评分条的样式，包括名称和样式值\nclass MyRatingStyle implements ContentModifier<RatingConfiguration> {\n  name: string = "" // 评分条样式名称\n  style: number = 0 // 评分条样式值\n  constructor(value1: string, value2: number) {\n    this.name = value1\n    this.style = value2\n  }\n  applyContent() : WrappedBuilder<[RatingConfiguration]> {\n    return wrapBuilder(buildRating)\n  }\n}\n\n// buildRating函数用于构建评分条的UI结构\n@Builder function buildRating(config: RatingConfiguration) {\n  Column() {\n    // 创建每个圆圈表示0.5分的评分点，根据评分值显示不同颜色，点击事件用于改变评分\n    // 根据评分条是否作为指示器、评分步长和评分总数来控制显示与行为\n  }\n}\n\n// ratingExample结构体定义了评分示例的整体结构和行为\n@Entry\n@Component\nstruct ratingExample {\n  @State rating: number = 0; // 当前评分值\n  @State ratingIndicator: boolean = true; // 评分条是否作为指示器\n  @State ratingStars: number = 0; // 评分总数\n  @State ratingStepsize: number = 0.5; // 评分步长\n  @State ratingEnabled: boolean = true; // 评分是否可用\n\n  build() {\n    Row() {\n      Column() {\n        // 创建评分条组件，根据状态设置属性，包括评分值、指示器状态等\n        // 可根据评分变化触发onChange事件\n        // contentModifier用于应用自定义样式\n        Rating({\n          rating: 0,\n          indicator: this.ratingIndicator\n        })\n          .stepSize(this.ratingStepsize)\n          .stars(this.ratingStars)\n          .backgroundColor(Color.Transparent)\n          .width('100%')\n          .height(50)\n          .onChange((value: number) => {\n            console.info('Rating change is'+ value);\n            this.rating = value\n          })\n          .contentModifier(new MyRatingStyle("hello", 3))\n\n        // 按钮用于切换评分条是否作为指示器\n        Button(this.ratingIndicator ? "ratingIndicator : true" : "ratingIndicator : false")\n          .onClick((event) => {\n            if (this.ratingIndicator) {\n              this.ratingIndicator = false\n            } else {\n              this.ratingIndicator = true\n            }\n          }).margin({top : 5})\n\n        // 按钮用于增加评分总数\n        Button(this.ratingStars < 5 ? "ratingStars + 1, ratingStars =" + this.ratingStars : "ratingStars最大值为5")\n          .onClick((event) => {\n            if (this.ratingStars < 5) {\n              this.ratingStars += 1\n            }\n          }).margin({top : 5})\n\n        // 按钮用于减少评分总数\n        Button(this.ratingStars > 0 ? "ratingStars - 1, ratingStars =" + this.ratingStars : "ratingStars小于等于0时默认等于5")\n          .onClick((event) => {\n            if (this.ratingStars > 0) {\n              this.ratingStars -= 1\n            }\n          }).margin({top : 5})\n\n        // 按钮用于切换评分步长\n        Button(this.ratingStepsize == 0.5 ? "ratingStepsize : 0.5" : "ratingStepsize : 1")\n          .onClick((event) => {\n            if (this.ratingStepsize == 0.5) {\n              this.ratingStepsize = 1\n            } else {\n              this.ratingStepsize = 0.5\n            }\n          }).margin({top : 5})\n      }\n      .width('100%')\n      .height('100%')\n      .justifyContent(FlexAlign.Center)\n    }\n    .height('100%')\n  }\n}\n```\n// xxx.ets\nclass MyRatingStyle implements ContentModifier<RatingConfiguration> {\n  name: string = ""\n  style: number = 0\n  constructor(value1: string, value2: number) {\n    this.name = value1\n    this.style = value2\n  }\n  applyContent() : WrappedBuilder<[RatingConfiguration]> {\n    return wrapBuilder(buildRating)\n  }\n}\n\n@Builder function buildRating(config: RatingConfiguration) {\n  Column() {\n    Row() {\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 0.4 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            if (config.stepSize = 0.5) {\n              config.triggerChange(0.5);\n              return\n            }\n            if (config.stepSize = 1) {\n              config.triggerChange(1);\n              return\n            }\n          }\n        }).visibility(config.stars >= 1 ? Visibility.Visible : Visibility.Hidden)\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 0.9 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            config.triggerChange(1);\n          }\n        }).visibility(config.stars >= 1 ? Visibility.Visible : Visibility.Hidden)\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 1.4 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            if (config.stepSize = 0.5) {\n              config.triggerChange(1.5);\n              return\n            }\n            if (config.stepSize = 1) {\n              config.triggerChange(2);\n              return\n            }\n          }\n        }).visibility(config.stars >= 2 ? Visibility.Visible : Visibility.Hidden).margin({left:10})\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 1.9 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            config.triggerChange(2);\n          }\n        }).visibility(config.stars >= 2 ? Visibility.Visible : Visibility.Hidden)\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 2.4 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            if (config.stepSize = 0.5) {\n              config.triggerChange(2.5);\n              return\n            }\n            if (config.stepSize = 1) {\n              config.triggerChange(3);\n              return\n            }\n          }\n        }).visibility(config.stars >= 3 ? Visibility.Visible : Visibility.Hidden).margin({left:10})\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 2.9 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            config.triggerChange(3);\n          }\n        }).visibility(config.stars >= 3 ? Visibility.Visible : Visibility.Hidden)\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 3.4 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            if (config.stepSize = 0.5) {\n              config.triggerChange(3.5);\n              return\n            }\n            if (config.stepSize = 1) {\n              config.triggerChange(4);\n              return\n            }\n          }\n        }).visibility(config.stars >= 4 ? Visibility.Visible : Visibility.Hidden).margin({left:10})\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 3.9 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            config.triggerChange(4);\n          }\n        }).visibility(config.stars >= 4 ? Visibility.Visible : Visibility.Hidden)\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 4.4 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            if (config.stepSize = 0.5) {\n              config.triggerChange(4.5);\n              return\n            }\n            if (config.stepSize = 1) {\n              config.triggerChange(5);\n              return\n            }\n          }\n        }).visibility(config.stars >= 5 ? Visibility.Visible : Visibility.Hidden).margin({left:10})\n      Circle({ width: 25, height: 25 })\n        .fill(config.rating >= 4.9 ? Color.Black : Color.Red)\n        .onClick((event: ClickEvent) => {\n          if (!config.indicator) {\n            config.triggerChange(5);\n          }\n        }).visibility(config.stars >= 5 ? Visibility.Visible : Visibility.Hidden)\n    }\n    Text("分值：" + config.rating)\n  }\n}\n\n@Entry\n@Component\nstruct ratingExample {\n  @State rating: number = 0;\n  @State ratingIndicator: boolean = true;\n  @State ratingStars: number = 0;\n  @State ratingStepsize: number = 0.5;\n  @State ratingEnabled: boolean = true;\n  build() {\n    Row() {\n      Column() {\n        Rating({\n          rating: 0,\n          indicator: this.ratingIndicator\n        })\n          .stepSize(this.ratingStepsize)\n          .stars(this.ratingStars)\n          .backgroundColor(Color.Transparent)\n          .width('100%')\n          .height(50)\n          .onChange((value: number) => {\n            console.info('Rating change is'+ value);\n            this.rating = value\n          })\n          .contentModifier(new MyRatingStyle("hello", 3))\n        Button(this.ratingIndicator ? "ratingIndicator : true" : "ratingIndicator : false")\n          .onClick((event) => {\n            if (this.ratingIndicator) {\n              this.ratingIndicator = false\n            } else {\n              this.ratingIndicator = true\n            }\n          }).margin({top : 5})\n\n        Button(this.ratingStars < 5 ? "ratingStars + 1, ratingStars =" + this.ratingStars : "ratingStars最大值为5")\n          .onClick((event) => {\n            if (this.ratingStars < 5) {\n              this.ratingStars += 1\n            }\n          }).margin({top : 5})\n\n        Button(this.ratingStars > 0 ? "ratingStars - 1, ratingStars =" + this.ratingStars : "ratingStars小于等于0时默认等于5")\n          .onClick((event) => {\n            if (this.ratingStars > 0) {\n              this.ratingStars -= 1\n            }\n          }).margin({top : 5})\n\n        Button(this.ratingStepsize == 0.5 ? "ratingStepsize : 0.5" : "ratingStepsize : 1")\n          .onClick((event) => {\n            if (this.ratingStepsize == 0.5) {\n              this.ratingStepsize = 1\n            } else {\n              this.ratingStepsize = 0.5\n            }\n          }).margin({top : 5})\n      }\n      .width('100%')\n      .height('100%')\n      .justifyContent(FlexAlign.Center)\n    }\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "RichEditor": {
        "description": "支持图文混排和文本交互式编辑的组件。",
        "interfaces": [
            {
                "description": "RichEditor(value: RichEditorOptions)\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。",
                "params": {
                    "value": {
                        "type": "RichEditorOptions",
                        "required": True,
                        "description": "RichEditor初始化参数。"
                    }
                }
            },
            {
                "description": "RichEditor(options: RichEditorStyledStringOptions)12+\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。",
                "params": {
                    "options": {
                        "type": "RichEditorStyledStringOptions",
                        "required": True,
                        "description": "RichEditor初始化参数。"
                    }
                }
            }
        ],
        "attributes": {
            "customKeyboard": {
                "description": "customKeyboard(value: CustomBuilder, options?: KeyboardOptions)\n\n设置自定义键盘。\n\n当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。\n\n自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。\n\n自定义键盘无法获取焦点，但是会拦截手势事件。\n\n默认在输入控件失去焦点时，关闭自定义键盘。\n\n如果设备支持拍摄输入，设置自定义键盘后，该输入框会不支持拍摄输入。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "value": {
                        "type": "CustomBuilder",
                        "required": True,
                        "description": "自定义键盘的构建器。"
                    },
                    "options": {
                        "type": "KeyboardOptions",
                        "required": False,
                        "description": "自定义键盘的选项。"
                    }
                }
            },
            "bindSelectionMenu": {
                "description": "bindSelectionMenu(spanType: RichEditorSpanType, content: CustomBuilder, responseType: ResponseType | RichEditorResponseType,options?: SelectionMenuOptions)设置自定义选择菜单。自定义菜单超长时，设置自定义选择菜单。自定义菜单超长时，建议内部嵌套Scroll组件使用，避免键盘被遮挡。",
                "params": {
                    "spanType": {
                        "type": "RichEditorSpanType",
                        "required": True,
                        "description": "菜单的类型。",
                        "default": "RichEditorSpanType.TEXT"
                    },
                    "content": {
                        "type": "CustomBuilder",
                        "required": True,
                        "description": "菜单的内容。"
                    },
                    "responseType": {
                        "type": ["ResponseType", "RichEditorResponseType"],
                        "required": True,
                        "description": "菜单的响应类型。",
                        "default": "ResponseType.LongPress"
                    },
                    "options": {
                        "type": "SelectionMenuOptions",
                        "required": False,
                        "description": "菜单的选项。"
                    },
                }
            },
            "copyOptions": {
                "description": "copyOptions(value: CopyOptions)\n\n设置组件是否支持文本内容可复制粘贴。\n\ncopyOptions不为CopyOptions.None时，长按组件内容，会弹出文本选择弹框。如果通过bindSelectionMenu等方式自定义文本选择菜单，则会弹出自定义的菜单。\n\n设置copyOptions为CopyOptions.None，复制、剪切功能不生效。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "value": {
                        "type": "CopyOptions",
                        "required": True,
                        "description": "组件支持文本内容是否可复制粘贴。",
                        "default": "CopyOptions.LocalDevice"
                    }
                }
            },
            "enableDataDetector": {
                "description": "enableDataDetector(enable: boolean)\n\n设置使能文本识别。\n\n所识别实体的fontColor和decoration会被更改为如下样式：\n\nfontColor：Color.Blue\n\ndecoration: {\n\ntype: TextDecorationType.Underline,\n\ncolor: Color.Blue\n\n}\n\n该接口依赖设备底层应具有文本识别能力，否则设置不会生效。\n\n当enableDataDetector设置为true，同时不设置dataDetectorConfig属性时，默认识别所有类型的实体。\n\n当copyOptions设置为CopyOptions.None时，点击实体弹出的菜单没有选择文本功能。\n\n对addBuilderSpan的节点文本，该功能不会生效。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "required": True,
                        "description": "使能文本识别。",
                        "default": False
                    }
                }
            },
            "dataDetectorConfig": {
                "description": "dataDetectorConfig(config: TextDataDetectorConfig)\n\n设置文本识别配置。需配合[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-richeditor-V5#enabledatadetector11)一起使用，设置enableDataDetector为true时，dataDetectorConfig的配置才能生效。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "config": {
                        "type": "TextDataDetectorConfig",
                        "required": True,
                        "description": "文本识别配置参数。"
                    }
                }
            },
            "enablePreviewText": {
                "description": "enablePreviewText(enable: boolean)\n\n设置是否开启预上屏功能。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "required": True,
                        "description": "使能预上屏功能。",
                        "default": True
                    }
                }
            },
            "placeholder": {
                "description": "placeholder(value: ResourceStr, style?: PlaceholderStyle)\n\n设置无输入时的提示文本。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "value": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "无输入时的提示文本。"
                    },
                    "style": {
                        "type": "PlaceholderStyle",
                        "required": False,
                        "description": "提示文本的样式。"
                    }
                }
            },
            "caretColor": {
                "description": "caretColor(value: ResourceColor)\n\n设置输入框光标、手柄颜色。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "输入框光标、手柄颜色。"
                    }
                }
            },
            "selectedBackgroundColor": {
                "description": "selectedBackgroundColor(value: ResourceColor)\n\n设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "文本选中底板颜色。"
                    }
                }
            },
            "editMenuOptions": {
                "description": "editMenuOptions(editMenu: EditMenuOptions)\n\n设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "editMenu": {
                        "type": "EditMenuOptions",
                        "required": True,
                        "description": "自定义菜单扩展项。"
                    }
                }
            },
            "enterKeyType": {
                "description": "enterKeyType(value: EnterKeyType)\n\n设置软键盘输入法回车键类型。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "value": {
                        "type": "EnterKeyType",
                        "required": True,
                        "description": "键盘输入法回车键类型。",
                        "default": "EnterKeyType.NEW_LINE"
                    }
                }
            }
        },
        "events": {
            "onReady": {
                "description": "onReady(callback:Callback<void>)\n\n富文本组件初始化完成后，触发回调。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "Callback<void>",
                        "required": True,
                        "description": "订阅富文本组件初始化完成的回调。"
                    }
                }
            },
            "onSelect": {
                "description": "onSelect(callback:Callback<RichEditorSelection>)鼠标左键按下选择，松开左键后触发回调。用手指选择时，松开手指触发回调。",
                "params": {
                    "callback": {
                        "type": "Callback<RichEditorSelection>",
                        "required": True,
                        "description": "RichEditorSelection为选中的所有span信息。选择时触发的回调。"
                    }
                }
            },
            "aboutToIMEInput": {
                "description": "aboutToIMEInput(callback:Callback<RichEditorInsertValue, boolean>)输入法输入内容前，触发回调。",
                "params": {
                    "callback": {
                        "type": "Callback<RichEditorInsertValue, boolean>",
                        "required": True,
                        "description": "RichEditorInsertValue为输入法将要输入内容信息。true:组件执行添加内容操作。false:组件不执行添加内容操作输入法输入内容前的回调。"
                    }
                }
            },
            "onIMEInputComplete": {
                "description": "onIMEInputComplete(callback:Callback<RichEditorTextSpanResult>)输入法完成输入后，触发回调。",
                "params": {
                    "callback": {
                        "type": "Callback<RichEditorTextSpanResult>",
                        "required": True,
                        "description": "RichEditorTextSpanResult为输入法完成输入后的文本Span信息。输入法完成输入后的回调。"
                    }
                }
            },
            "aboutToDelete": {
                "description": "aboutToDelete(callback:Callback<RichEditorDeleteValue, boolean>)输入法删除内容前，触发回调。使用RichEditorStyledStringOptions构建的RichEditor组件时不支持该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<RichEditorDeleteValue, boolean>",
                        "required": True,
                        "description": "RichEditorDeleteValue为准备删除的内容所在的文本或者图片Span信息。true:组件执行删除操作。false:组件不执行删除操作。输入法删除内容前的回调。"
                    }
                }
            },
            "onDeleteComplete": {
                "description": "onDeleteComplete(callback:Callback<void>)\n\n输入法完成删除后，触发回调。\n\n使用[RichEditorStyledStringOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-richeditor-V5#richeditorstyledstringoptions12)构建的RichEditor组件时不支持该回调。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "Callback<void>",
                        "required": True,
                        "description": "onDeleteComplete(callback:Callback<void>)输入法完成删除后，触发回调。使用RichEditorStyledStringOptions构建的RichEditor组件时不支持该回调。"
                    }
                }
            },
            "onPaste": {
                "description": "onPaste(callback: [PasteEventCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-richeditor-V5#pasteeventcallback12) )\n\n完成粘贴前，触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的粘贴。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "PasteEventCallback",
                        "required": True,
                        "description": "完成粘贴前的回调。"
                    }
                }
            },
            "onSelectionChange": {
                "description": "onSelectionChange(callback:Callback<[RichEditorRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-richeditor-V5#richeditorrange)>)\n\n组件内所有内容选择区域发生变化或编辑状态下光标位置发生变化时触发该回调。光标位置发生变化回调时，选择区域的起始位置等于终止位置。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "Callback<RichEditorRange>",
                        "required": True,
                        "description": "选择区域或光标位置变化的回调。"
                    }
                }
            },
            "onEditingChange": {
                "description": "onEditingChange(callback: Callback<boolean>)\n\n组件内所有内容的编辑状态发生改变时触发该回调函数。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "Callback<boolean>",
                        "required": True,
                        "description": "编辑状态变化的回调。",
                        "returns": {
                            "type": "boolean",
                            "description": "true表示编辑态，false表示非编辑态。"
                        }
                    }
                }
            },
            "onSubmit": {
                "description": "onSubmit(callback: SubmitCallback)\n\n按下软键盘输入法回车键触发该回调。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "SubmitCallback",
                        "required": True,
                        "description": "软键盘输入法回车键触发的回调。"
                    }
                }
            },
            "onWillChange": {
                "description": "onWillChange(callback: Callback<RichEditorChangeValue, boolean>)\n\n组件内图文变化前，触发回调。\n\n使用[RichEditorStyledStringOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-richeditor-V5#richeditorstyledstringoptions12)构建的RichEditor组件时不支持该回调。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "Callback<RichEditorChangeValue, boolean>",
                        "required": True,
                        "description": "图文变化前的回调。",
                        "returns": {
                            "type": "boolean",
                            "description": "是否允许变化。"
                        }
                    }
                }
            },
            "onDidChange": {
                "description": "onDidChange(callback: OnDidChangeCallback)\n\n图文变化后，触发回调。\n\n使用[RichEditorStyledStringOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-basic-components-richeditor-V5#richeditorstyledstringoptions12)构建的RichEditor组件时不支持该回调。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "OnDidChangeCallback",
                        "required": True,
                        "description": "图文变化后的回调。"
                    }
                }
            },
            "onCut": {
                "description": "onCut(callback: Callback<CutEvent>)\n\n完成剪切前，触发回调。系统的默认剪切行为，只支持纯文本的剪切。开发者可以通过该方法，覆盖系统默认行为，实现图文的剪切。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "Callback<CutEvent>",
                        "required": True,
                        "description": "定义用户剪切事件。"
                    }
                }
            },
            "onCopy": {
                "description": "onCopy(callback: Callback<CopyEvent>)\n\n完成复制前，触发回调。系统的默认复制行为，只支持纯文本的复制。开发者可以通过该方法，覆盖系统默认行为，实现图文的复制。\n\n**元服务API：** 从API version 12开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "callback": {
                        "type": "Callback<CopyEvent>",
                        "required": True,
                        "description": "定义用户复制事件。"
                    }
                }
            }
        },
        "examples": [
            """// xxx.ets\n@Entry\n@Component\nstruct RichEditorExample {\n  controller: RichEditorController = new RichEditorController()\n\n  // 自定义键盘组件\n  @Builder CustomKeyboardBuilder() {\n    // 定义自定义键盘布局\n    Column() {\n      // 创建网格布局\n      Grid() {\n        // 遍历数字和特殊字符数组，生成对应按钮\n        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {\n          GridItem() {\n            // 创建按钮，点击按钮将对应字符插入到富文本编辑器中\n            Button(item + "")\n              .width(110).onClick(() => {\n              // 在光标位置插入字符，并设置样式\n              this.controller.addTextSpan(item + '', {\n                offset: this.controller.getCaretOffset(),\n                style:\n                {\n                  fontColor: Color.Orange, // 设置字体颜色为橙色\n                  fontSize: 30 // 设置字体大小为30\n                }\n              })\n              this.controller.setCaretOffset(this.controller.getCaretOffset() + item.toString().length) // 移动光标位置\n            })\n          }\n        })\n      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5) // 设置网格布局属性\n    }.backgroundColor(Color.Gray) // 设置自定义键盘背景颜色为灰色\n  }\n\n  build() {\n    // 构建富文本编辑器示例\n    Column() {\n      RichEditor({ controller: this.controller })\n        // 绑定自定义键盘\n        .customKeyboard(this.CustomKeyboardBuilder()).margin(10).border({ width: 1 }) // 设置边距和边框\n        .height(200) // 设置高度为200\n        .borderWidth(1) // 设置边框宽度为1\n        .borderColor(Color.Red) // 设置边框颜色为红色\n        .width("100%") // 设置宽度为100%\n    }\n  }\n}\n```\n\n在以上代码中：\n- `CustomKeyboardBuilder`函数定义了一个自定义键盘组件，包含数字和特殊字符按钮，点击按钮将字符插入到富文本编辑器中，并设置样式。\n- 每个按钮的点击事件会在富文本编辑器中插入对应字符，并将光标位置移动到插入字符的末尾。\n- `RichEditorExample`结构体包含了一个富文本编辑器示例，其中包括自定义键盘组件的绑定和设置富文本编辑器的样式属性。\n- 最终的富文本编辑器示例将展示一个带有自定义键盘的编辑器界面，用户可以通过点击按钮插入字符到编辑器中。\n// xxx.ets\n@Entry\n@Component\nstruct RichEditorExample {\n  controller: RichEditorController = new RichEditorController()\n\n  // 自定义键盘组件\n  @Builder CustomKeyboardBuilder() {\n    Column() {\n      Grid() {\n        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {\n          GridItem() {\n            Button(item + "")\n              .width(110).onClick(() => {\n              this.controller.addTextSpan(item + '', {\n                offset: this.controller.getCaretOffset(),\n                style:\n                {\n                  fontColor: Color.Orange,\n                  fontSize: 30\n                }\n              })\n              this.controller.setCaretOffset(this.controller.getCaretOffset() + item.toString().length)\n            })\n          }\n        })\n      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)\n    }.backgroundColor(Color.Gray)\n  }\n\n  build() {\n    Column() {\n      RichEditor({ controller: this.controller })\n        // 绑定自定义键盘\n        .customKeyboard(this.CustomKeyboardBuilder()).margin(10).border({ width: 1 })\n        .height(200)\n        .borderWidth(1)\n        .borderColor(Color.Red)\n        .width("100%")\n    }\n  }\n}"""
            """// 为 SelectionMenu 结构体编写功能与效果描述注释\n\n@Entry\n@Component\nstruct SelectionMenu {\n  // 定义状态变量和控制器\n  @State message: string = 'Hello World'\n  @State textSize: number = 40\n  @State sliderShow: boolean = false\n  @State start: number = -1\n  @State end: number = -1\n  @State colorTransparent: Color = Color.Transparent\n  controller: RichEditorController = new RichEditorController();\n  options: RichEditorOptions = { controller: this.controller }\n  private iconArr: Array<Resource> = [$r('app.media.icon'), $r("app.media.icon"), $r('app.media.icon'), $r("app.media.icon"), $r('app.media.icon')]\n  @State iconBgColor: ResourceColor[] = new Array(this.iconArr.length).fill(this.colorTransparent)\n  @State pasteEnable: boolean = false\n  @State visibilityValue: Visibility = Visibility.Visible\n  @State textStyle: RichEditorTextStyle = {}\n  private fontWeightTable: string[] = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "bold", "normal", "bolder", "lighter", "medium", "regular"]\n  private theme: SelectionMenuTheme = defaultTheme;\n\n  // 在组件即将显示时执行的操作\n  aboutToAppear() {\n    // 检查富文本编辑器的选择状态和剪贴板数据，控制粘贴按钮的可用性\n  }\n\n  // 构建组件结构\n  build() {\n    // 构建富文本编辑器和相关菜单\n  }\n\n  // 将选中内容复制到剪贴板\n  PushDataToPasteboard(richEditorSelection: RichEditorSelection) {\n    // 处理选中内容，创建剪贴板数据并设置到系统剪贴板\n  }\n\n  // 从剪贴板粘贴内容到富文本编辑器\n  PopDataFromPasteboard(richEditorSelection: RichEditorSelection) {\n    // 从系统剪贴板获取数据并插入到富文本编辑器中\n  }\n\n  // 构建图标面板\n  @Builder\n  iconPanel() {\n    // 构建包含图标的面板，处理图标点击、样式修改等操作\n  }\n\n  // 构建系统菜单\n  @Builder\n  SystemMenu() {\n    // 构建包含系统菜单项的菜单，处理剪切、复制、粘贴等操作\n  }\n\n  // 构建滑块面板\n  @Builder\n  sliderPanel() {\n    // 构建包含滑块的面板，处理文本大小调整操作\n  }\n}\n```\n// xxx.ets\nimport { BusinessError, pasteboard } from '@kit.BasicServicesKit';\n\nexport interface SelectionMenuTheme {\n  imageSize: number;\n  buttonSize: number;\n  menuSpacing: number;\n  editorOptionMargin: number;\n  expandedOptionPadding: number;\n  defaultMenuWidth: number;\n  imageFillColor: Resource;\n  backGroundColor: Resource;\n  iconBorderRadius: Resource;\n  containerBorderRadius: Resource;\n  cutIcon: Resource;\n  copyIcon: Resource;\n  pasteIcon: Resource;\n  selectAllIcon: Resource;\n  shareIcon: Resource;\n  translateIcon: Resource;\n  searchIcon: Resource;\n  arrowDownIcon: Resource;\n  iconPanelShadowStyle: ShadowStyle;\n  iconFocusBorderColor: Resource;\n}\n\nexport const defaultTheme: SelectionMenuTheme = {\n  imageSize: 24,\n  buttonSize: 48,\n  menuSpacing: 8,\n  editorOptionMargin: 1,\n  expandedOptionPadding: 3,\n  defaultMenuWidth: 256,\n  imageFillColor: $r('sys.color.ohos_id_color_primary'),\n  backGroundColor: $r('sys.color.ohos_id_color_dialog_bg'),\n  iconBorderRadius: $r('sys.float.ohos_id_corner_radius_default_m'),\n  containerBorderRadius: $r('sys.float.ohos_id_corner_radius_card'),\n  cutIcon: $r("sys.media.ohos_ic_public_cut"),\n  copyIcon: $r("sys.media.ohos_ic_public_copy"),\n  pasteIcon: $r("sys.media.ohos_ic_public_paste"),\n  selectAllIcon: $r("sys.media.ohos_ic_public_select_all"),\n  shareIcon: $r("sys.media.ohos_ic_public_share"),\n  translateIcon: $r("sys.media.ohos_ic_public_translate_c2e"),\n  searchIcon: $r("sys.media.ohos_ic_public_search_filled"),\n  arrowDownIcon: $r("sys.media.ohos_ic_public_arrow_down"),\n  iconPanelShadowStyle: ShadowStyle.OUTER_DEFAULT_MD,\n  iconFocusBorderColor: $r('sys.color.ohos_id_color_focused_outline'),\n}\n\n@Entry\n@Component\nstruct SelectionMenu {\n  @State message: string = 'Hello World'\n  @State textSize: number = 40\n  @State sliderShow: boolean = false\n  @State start: number = -1\n  @State end: number = -1\n  @State colorTransparent: Color = Color.Transparent\n  controller: RichEditorController = new RichEditorController();\n  options: RichEditorOptions = { controller: this.controller }\n  private iconArr: Array<Resource> =\n    [$r('app.media.icon'), $r("app.media.icon"), $r('app.media.icon'),\n    $r("app.media.icon"), $r('app.media.icon')]\n  @State iconBgColor: ResourceColor[] = new Array(this.iconArr.length).fill(this.colorTransparent)\n  @State pasteEnable: boolean = false\n  @State visibilityValue: Visibility = Visibility.Visible\n  @State textStyle: RichEditorTextStyle = {}\n  private fontWeightTable: string[] = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "bold", "normal", "bolder", "lighter", "medium", "regular"]\n  private theme: SelectionMenuTheme = defaultTheme;\n\n  aboutToAppear() {\n    if (this.controller) {\n      let richEditorSelection = this.controller.getSelection()\n      if (richEditorSelection) {\n        let start = richEditorSelection.selection[0]\n        let end = richEditorSelection.selection[1]\n        if (start === 0 && this.controller.getSpans({ start: end + 1, end: end + 1 }).length === 0) {\n          this.visibilityValue = Visibility.None\n        } else {\n          this.visibilityValue = Visibility.Visible\n        }\n      }\n    }\n    let sysBoard = pasteboard.getSystemPasteboard()\n    if (sysBoard && sysBoard.hasDataSync()) {\n      this.pasteEnable = true\n    } else {\n      this.pasteEnable = false\n    }\n  }\n\n  build() {\n    Column() {\n      Column() {\n        RichEditor(this.options)\n          .onReady(() => {\n            this.controller.addTextSpan(this.message, { style: { fontColor: Color.Orange, fontSize: 30 } })\n          })\n          .onSelect((value: RichEditorSelection) => {\n            if (value.selection[0] == -1 && value.selection[1] == -1) {\n              return\n            }\n            this.start = value.selection[0]\n            this.end = value.selection[1]\n          })\n          .bindSelectionMenu(RichEditorSpanType.TEXT, this.panel, ResponseType.LongPress, { onDisappear: () => {\n            this.sliderShow = false\n          }})\n          .bindSelectionMenu(RichEditorSpanType.TEXT, this.panel, ResponseType.RightClick, { onDisappear: () => {\n            this.sliderShow = false\n          }})\n          .borderWidth(1)\n          .borderColor(Color.Red)\n          .width(200)\n          .height(200)\n      }.width('100%').backgroundColor(Color.White)\n    }.height('100%')\n  }\n\n  PushDataToPasteboard(richEditorSelection: RichEditorSelection) {\n    let sysBoard = pasteboard.getSystemPasteboard()\n    let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, '')\n    if (richEditorSelection.spans && richEditorSelection.spans.length > 0) {\n      let count = richEditorSelection.spans.length\n      for (let i = count - 1; i >= 0; i--) {\n        let item = richEditorSelection.spans[i]\n        if ((item as RichEditorTextSpanResult)?.textStyle) {\n          let span = item as RichEditorTextSpanResult\n          let style = span.textStyle\n          let data = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_PLAIN, span.value.substring(span.offsetInSpan[0], span.offsetInSpan[1]))\n          let prop = pasteData.getProperty()\n          let temp: Record<string, Object> = {\n            'color': style.fontColor,\n            'size': style.fontSize,\n            'style': style.fontStyle,\n            'weight': this.fontWeightTable[style.fontWeight],\n            'fontFamily': style.fontFamily,\n            'decorationType': style.decoration.type,\n            'decorationColor': style.decoration.color\n          }\n          prop.additions[i] = temp;\n          pasteData.addRecord(data)\n          pasteData.setProperty(prop)\n        }\n      }\n    }\n    sysBoard.clearData()\n    sysBoard.setData(pasteData).then(() => {\n      console.info('SelectionMenu copy option, Succeeded in setting PasteData.');\n      this.pasteEnable = true;\n    }).catch((err: BusinessError) => {\n      console.error('SelectionMenu copy option, Failed to set PasteData. Cause:' + err.message);\n    })\n  }\n\n  PopDataFromPasteboard(richEditorSelection: RichEditorSelection) {\n    let start = richEditorSelection.selection[0]\n    let end = richEditorSelection.selection[1]\n    if (start == end && this.controller) {\n      start = this.controller.getCaretOffset()\n      end = this.controller.getCaretOffset()\n    }\n    let moveOffset = 0\n    let sysBoard = pasteboard.getSystemPasteboard()\n    sysBoard.getData((err, data) => {\n      if (err) {\n        return\n      }\n      let count = data.getRecordCount()\n      for (let i = 0; i < count; i++) {\n        const element = data.getRecord(i);\n        let tex: RichEditorTextStyle = {\n          fontSize: 16,\n          fontColor: Color.Black,\n          fontWeight: FontWeight.Normal,\n          fontFamily: "HarmonyOS Sans",\n          fontStyle: FontStyle.Normal,\n          decoration: { type: TextDecorationType.None, color: "#FF000000", style: TextDecorationStyle.SOLID }\n        }\n        if (data.getProperty() && data.getProperty().additions[i]) {\n          const tmp = data.getProperty().additions[i] as Record<string, Object | undefined>;\n          if (tmp.color) {\n            tex.fontColor = tmp.color as ResourceColor;\n          }\n          if (tmp.size) {\n            tex.fontSize = tmp.size as Length | number;\n          }\n          if (tmp.style) {\n            tex.fontStyle = tmp.style as FontStyle;\n          }\n          if (tmp.weight) {\n            tex.fontWeight = tmp.weight as number | FontWeight | string;\n          }\n          if (tmp.fontFamily) {\n            tex.fontFamily = tmp.fontFamily as ResourceStr;\n          }\n          if (tmp.decorationType && tex.decoration) {\n            tex.decoration.type = tmp.decorationType as TextDecorationType;\n          }\n          if (tmp.decorationColor && tex.decoration) {\n            tex.decoration.color = tmp.decorationColor as ResourceColor;\n          }\n          if (tex.decoration) {\n            tex.decoration = { type: tex.decoration.type, color: tex.decoration.color }\n          }\n        }\n        if (element && element.plainText && element.mimeType === pasteboard.MIMETYPE_TEXT_PLAIN && this.controller) {\n          this.controller.addTextSpan(element.plainText,\n            {\n              style: tex,\n              offset: start + moveOffset\n            }\n          )\n          moveOffset += element.plainText.length\n        }\n      }\n      if (this.controller) {\n        this.controller.setCaretOffset(start + moveOffset)\n        this.controller.closeSelectionMenu()\n      }\n      if (start != end && this.controller) {\n        this.controller.deleteSpans({ start: start + moveOffset, end: end + moveOffset })\n      }\n    })\n  }\n\n  @Builder\n  panel() {\n    Column() {\n      this.iconPanel()\n      if (!this.sliderShow) {\n        this.SystemMenu()\n      } else {\n        this.sliderPanel()\n      }\n    }.width(256)\n  }\n\n  @Builder iconPanel() {\n    Column() {\n      Row({ space: 2 }) {\n        ForEach(this.iconArr, (item:Resource, index ?: number) => {\n          Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n            Image(item).fillColor(this.theme.imageFillColor).width(24).height(24).focusable(true).draggable(false)\n          }\n          .borderRadius(this.theme.iconBorderRadius)\n          .width(this.theme.buttonSize)\n          .height(this.theme.buttonSize)\n          .onClick(() => {\n            if (index as number == 0) {\n              this.sliderShow = false\n              if (this.controller) {\n                let selection = this.controller.getSelection();\n                let spans = selection.spans\n                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {\n                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {\n                    let span = item as RichEditorTextSpanResult\n                    this.textStyle = span.textStyle\n                    let start = span.offsetInSpan[0]\n                    let end = span.offsetInSpan[1]\n                    let offset = span.spanPosition.spanRange[0]\n                    if (this.textStyle.fontWeight != 11) {\n                      this.textStyle.fontWeight = FontWeight.Bolder\n                    } else {\n                      this.textStyle.fontWeight = FontWeight.Normal\n                    }\n                    this.controller.updateSpanStyle({\n                      start: offset + start,\n                      end: offset + end,\n                      textStyle: this.textStyle\n                    })\n                  }\n                })\n              }\n            } else if (index as number == 1) {\n              this.sliderShow = false\n              if (this.controller) {\n                let selection = this.controller.getSelection();\n                let spans = selection.spans\n                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {\n                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {\n                    let span = item as RichEditorTextSpanResult\n                    this.textStyle = span.textStyle\n                    let start = span.offsetInSpan[0]\n                    let end = span.offsetInSpan[1]\n                    let offset = span.spanPosition.spanRange[0]\n                    if (this.textStyle.fontStyle == FontStyle.Italic) {\n                      this.textStyle.fontStyle = FontStyle.Normal\n                    } else {\n                      this.textStyle.fontStyle = FontStyle.Italic\n                    }\n                    this.controller.updateSpanStyle({\n                      start: offset + start,\n                      end: offset + end,\n                      textStyle: this.textStyle\n                    })\n                  }\n                })\n              }\n            } else if (index as number == 2) {\n              this.sliderShow = false\n              if (this.controller) {\n                let selection = this.controller.getSelection();\n                let spans = selection.spans\n                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {\n                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {\n                    let span = item as RichEditorTextSpanResult\n                    this.textStyle = span.textStyle\n                    let start = span.offsetInSpan[0]\n                    let end = span.offsetInSpan[1]\n                    let offset = span.spanPosition.spanRange[0]\n                    if (this.textStyle.decoration) {\n                      if (this.textStyle.decoration.type == TextDecorationType.Underline) {\n                        this.textStyle.decoration.type = TextDecorationType.None\n                      } else {\n                        this.textStyle.decoration.type = TextDecorationType.Underline\n                      }\n                    } else {\n                      this.textStyle.decoration = { type: TextDecorationType.Underline, color: Color.Black, style: TextDecorationStyle.SOLID }\n                    }\n                    this.controller.updateSpanStyle({\n                      start: offset + start,\n                      end: offset + end,\n                      textStyle: this.textStyle\n                    })\n                  }\n                })\n              }\n            } else if (index as number == 3) {\n              this.sliderShow = !this.sliderShow\n            } else if (index as number == 4) {\n              this.sliderShow = false\n              if (this.controller) {\n                let selection = this.controller.getSelection();\n                let spans = selection.spans\n                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {\n                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {\n                    let span = item as RichEditorTextSpanResult\n                    this.textStyle = span.textStyle\n                    let start = span.offsetInSpan[0]\n                    let end = span.offsetInSpan[1]\n                    let offset = span.spanPosition.spanRange[0]\n                    if (this.textStyle.fontColor == Color.Orange || this.textStyle.fontColor == '#FFFFA500') {\n                      this.textStyle.fontColor = Color.Black\n                    } else {\n                      this.textStyle.fontColor = Color.Orange\n                    }\n                    this.controller.updateSpanStyle({\n                      start: offset + start,\n                      end: offset + end,\n                      textStyle: this.textStyle\n                    })\n                  }\n                })\n              }\n            }\n          })\n          .onTouch((event?: TouchEvent | undefined) => {\n            if(event != undefined){\n              if (event.type === TouchType.Down) {\n                this.iconBgColor[index as number] = $r('sys.color.ohos_id_color_click_effect')\n              }\n              if (event.type === TouchType.Up) {\n                this.iconBgColor[index as number] = this.colorTransparent\n              }\n            }\n          })\n          .onHover((isHover?: boolean, event?: HoverEvent) => {\n            this.iconBgColor.forEach((icon:ResourceColor, index1) => {\n              this.iconBgColor[index1] = this.colorTransparent\n            })\n            if(isHover != undefined) {\n              this.iconBgColor[index as number] = $r('sys.color.ohos_id_color_hover')\n            }\n          })\n          .backgroundColor(this.iconBgColor[index as number])\n        })\n      }\n    }\n    .clip(true)\n    .width(this.theme.defaultMenuWidth)\n    .padding(this.theme.expandedOptionPadding)\n    .borderRadius(this.theme.containerBorderRadius)\n    .margin({ bottom: this.theme.menuSpacing })\n    .backgroundColor(this.theme.backGroundColor)\n    .shadow(this.theme.iconPanelShadowStyle)\n  }\n\n  @Builder\n  SystemMenu() {\n    Column() {\n      Menu() {\n        if (this.controller) {\n          MenuItemGroup() {\n            MenuItem({ startIcon: this.theme.cutIcon, content: "剪切", labelInfo: "Ctrl+X" })\n              .onClick(() => {\n                if (!this.controller) {\n                  return\n                }\n                let richEditorSelection = this.controller.getSelection()\n                this.PushDataToPasteboard(richEditorSelection);\n                this.controller.deleteSpans({\n                  start: richEditorSelection.selection[0],\n                  end: richEditorSelection.selection[1]\n                })\n              })\n            MenuItem({ startIcon: this.theme.copyIcon, content: "复制", labelInfo: "Ctrl+C" })\n              .onClick(() => {\n                if (!this.controller) {\n                  return\n                }\n                let richEditorSelection = this.controller.getSelection()\n                this.PushDataToPasteboard(richEditorSelection);\n                this.controller.closeSelectionMenu()\n              })\n            MenuItem({ startIcon: this.theme.pasteIcon, content: "粘贴", labelInfo: "Ctrl+V" })\n              .enabled(this.pasteEnable)\n              .onClick(() => {\n                if (!this.controller) {\n                  return\n                }\n                let richEditorSelection = this.controller.getSelection()\n                this.PopDataFromPasteboard(richEditorSelection)\n              })\n            MenuItem({ startIcon: this.theme.selectAllIcon, content: "全选", labelInfo: "Ctrl+A" })\n              .visibility(this.visibilityValue)\n              .onClick(() => {\n                if (!this.controller) {\n                  return\n                }\n                this.controller.setSelection(-1, -1)\n                this.visibilityValue = Visibility.None\n              })\n            MenuItem({ startIcon: this.theme.shareIcon, content: "分享", labelInfo: "" })\n              .enabled(false)\n            MenuItem({ startIcon: this.theme.translateIcon, content: "翻译", labelInfo: "" })\n              .enabled(false)\n            MenuItem({ startIcon: this.theme.searchIcon, content: "搜索", labelInfo: "" })\n              .enabled(false)\n          }\n        }\n      }\n      .onVisibleAreaChange([0.0, 1.0], () => {\n        if (!this.controller) {\n          return\n        }\n        let richEditorSelection = this.controller.getSelection()\n        let start = richEditorSelection.selection[0]\n        let end = richEditorSelection.selection[1]\n        if (start === 0 && this.controller.getSpans({ start: end + 1, end: end + 1 }).length === 0) {\n          this.visibilityValue = Visibility.None\n        } else {\n          this.visibilityValue = Visibility.Visible\n        }\n      })\n      .radius(this.theme.containerBorderRadius)\n      .clip(true)\n      .backgroundColor(Color.White)\n      .width(this.theme.defaultMenuWidth)\n    }\n    .width(this.theme.defaultMenuWidth)\n  }\n\n  @Builder sliderPanel() {\n    Column() {\n      Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {\n        Text('A').fontSize(15)\n        Slider({ value: this.textSize, step: 10, style: SliderStyle.InSet })\n          .width(210)\n          .onChange((value: number, mode: SliderChangeMode) => {\n            if (this.controller) {\n              let selection = this.controller.getSelection();\n              if (mode == SliderChangeMode.End) {\n                if (this.textSize == undefined) {\n                  this.textSize = 0\n                }\n                let spans = selection.spans\n                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {\n                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {\n                    this.textSize = Math.max(this.textSize, (item as RichEditorTextSpanResult).textStyle.fontSize)\n                  }\n                })\n              }\n              if (mode == SliderChangeMode.Moving || mode == SliderChangeMode.Click) {\n                this.start = selection.selection[0]\n                this.end = selection.selection[1]\n                this.textSize = value\n                this.controller.updateSpanStyle({\n                  start: this.start,\n                  end: this.end,\n                  textStyle: { fontSize: this.textSize }\n                })\n              }\n            }\n          })\n        Text('A').fontSize(20).fontWeight(FontWeight.Medium)\n      }.borderRadius(this.theme.containerBorderRadius)\n    }\n    .shadow(ShadowStyle.OUTER_DEFAULT_MD)\n    .backgroundColor(Color.White)\n    .borderRadius(this.theme.containerBorderRadius)\n    .padding(15)\n    .height(48)\n  }\n}"""
            """// xxx.ets\n\n// 定义一个名为Index的结构体，作为入口组件\n@Entry\n@Component\nstruct Index {\n  // 创建一个富文本编辑器控制器实例\n  controller: RichEditorController = new RichEditorController();\n  // 设置富文本编辑器选项，关联控制器\n  options: RichEditorOptions = { controller: this.controller };\n  // 定义私有变量start和end，用于记录选择文本的起始和结束位置\n  private start: number = -1;\n  private end: number = -1;\n  // 定义状态变量message、content、paddingVal和borderRad\n  @State message: string = "[-1, -1]"\n  @State content: string = ""\n  @State paddingVal: number = 5\n  @State borderRad: number = 4\n\n  // 构建UI界面\n  build() {\n    // 第一个功能块：显示选择范围和内容\n    Column() {\n      Column() {\n        Text("selection range:").width("100%")\n        Text() {\n          Span(this.message)\n        }.width("100%")\n        Text("selection content:").width("100%")\n        Text() {\n          Span(this.content)\n        }.width("100%")\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("20%")\n\n      // 第二个功能块：更新文本样式\n      Row() {\n        // 按钮1：更新文本样式1\n        Button("updateSpanStyle1")\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.updateSpanStyle({\n              start: this.start,\n              textStyle:\n              {\n                fontWeight: FontWeight.Bolder\n              },\n              imageStyle: {\n                size: ["80px", "80px"],\n                layoutStyle: {\n                  borderRadius: undefined,\n                  margin: undefined\n                }\n              }\n            })\n          })\n\n        // 按钮2：更新文本样式2\n        Button("updateSpanStyle2")\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.updateSpanStyle({\n              start: this.start,\n              textStyle:\n              {\n                fontWeight: FontWeight.Bolder\n              },\n              imageStyle: {\n                size: ["70px", "70px"],\n                layoutStyle: {\n                  borderRadius: { topLeft: '100px', topRight: '20px', bottomLeft: '100px', bottomRight: '20px' },\n                  margin: { left: '30px', top: '20px', right: '20px', bottom: '20px' }\n                }\n              }\n            })\n          })\n\n        // 按钮3：更新文本样式3\n        Button("updateSpanStyle3")\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.updateSpanStyle({\n              start: this.start,\n              textStyle:\n              {\n                fontWeight: FontWeight.Bolder\n              },\n              imageStyle: {\n                size: ["60px", "60px"],\n                layoutStyle: {\n                  borderRadius: '-10px',\n                  margin: '-10px'\n                }\n              }\n            })\n          })\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("10%")\n\n      // 第三个功能块：添加图片样式\n      Row() {\n        // 按钮1：添加图片样式1\n        Button('addImageSpan1')\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.addImageSpan($r('app.media.app_icon'), {\n              imageStyle: {\n                size: ["80px", "80px"],\n                layoutStyle: {\n                  borderRadius: '50px',\n                  margin: '40px'\n                }\n              }\n            })\n          })\n\n        // 按钮2：添加图片样式2\n        Button('addImageSpan2')\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.addImageSpan($r('app.media.app_icon'), {\n              imageStyle: {\n                size: ["100px", "100px"],\n                verticalAlign: ImageSpanAlignment.BOTTOM,\n                layoutStyle: {\n                  borderRadius: undefined,\n                  margin: undefined\n                }\n              }\n            })\n          })\n\n        // 按钮3：添加图片样式3\n        Button('addImageSpan3')\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.addImageSpan($r('app.media.app_icon'), {\n              imageStyle: {\n                size: ["60px", "60px"],\n                verticalAlign: ImageSpanAlignment.BOTTOM,\n                layoutStyle: {\n                  borderRadius: { topLeft: '10px', topRight: '20px', bottomLeft: '30px', bottomRight: '40px' },\n                  margin: { left: '10px', top: '20px', right: '30px', bottom: '40px' }\n                }\n              }\n            })\n          })\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("10%")\n\n      // 第四个功能块：富文本编辑器\n      Column() {\n        // 富文本编辑器组件\n        RichEditor(this.options)\n          .onReady(() => {\n            // 添加文本样式\n            this.controller.addTextSpan("0123456789",\n              {\n                style:\n                {\n                  fontColor: Color.Orange,\n                  fontSize: 30\n                }\n              })\n\n            // 添加图片样式\n            this.controller.addImageSpan($r("app.media.app_icon"),\n              {\n                imageStyle:\n                {\n                  size: ["60px", "60px"],\n                  verticalAlign: ImageSpanAlignment.BOTTOM,\n                  layoutStyle: {\n                    borderRadius: { topLeft: '10px', topRight: '20px', bottomLeft: '30px', bottomRight: '40px' },\n                    margin: { left: '10px', top: '20px', right: '30px', bottom: '40px' }\n                  }\n                }\n              })\n\n            // 添加文本样式\n            this.controller.addTextSpan("0123456789",\n              {\n                style:\n                {\n                  fontColor: Color.Black,\n                  fontSize: 30\n                }\n              })\n          })\n          .onSelect((value: RichEditorSelection) => {\n            // 监听选择文本事件\n            this.start = value.selection[0];\n            this.end = value.selection[1];\n            this.message = "[" + this.start + ", " + this.end + "]"\n          })\n          .aboutToIMEInput((value: RichEditorInsertValue) => {\n            // 准备输入IME事件\n            console.log("---------------------- aboutToIMEInput ----------------------")\n            console.log("insertOffset:" + value.insertOffset)\n            console.log("insertValue:" + value.insertValue)\n            return true;\n          })\n          .onIMEInputComplete((value: RichEditorTextSpanResult) => {\n            // 输入IME完成事件\n            console.log("---------------------- onIMEInputComplete ---------------------")\n            console.log("spanIndex:" + value.spanPosition.spanIndex)\n            console.log("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]")\n            console.log("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]")\n            console.log("value:" + value.value)\n          })\n          .aboutToDelete((value: RichEditorDeleteValue) => {\n            // 准备删除事件\n            console.log("---------------------- aboutToDelete --------------------------")\n            console.log("offset:" + value.offset)\n            console.log("direction:" + value.direction)\n            console.log("length:" + value.length)\n            value.richEditorDeleteSpans.forEach(item => {\n              console.log("---------------------- item --------------------------")\n              console.log("spanIndex:" + item.spanPosition.spanIndex)\n              console.log("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]")\n              console.log("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]")\n              if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {\n                console.log("image:" + (item as RichEditorImageSpanResult).valueResourceStr)\n              } else {\n                console.log("text:" + (item as RichEditorTextSpanResult).value)\n              }\n            })\n            return true;\n          })\n          .onDeleteComplete(() => {\n            // 删除完成事件\n            console.log("---------------------- onDeleteComplete ------------------------")\n          })\n          .borderWidth(1)\n          .borderColor(Color.Green)\n          .width("100%")\n          .height('80.00%')\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("70%")\n    }\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  controller: RichEditorController = new RichEditorController();\n  options: RichEditorOptions = { controller: this.controller };\n  private start: number = -1;\n  private end: number = -1;\n  @State message: string = "[-1, -1]"\n  @State content: string = ""\n  @State paddingVal: number = 5\n  @State borderRad: number = 4\n\n  build() {\n    Column() {\n      Column() {\n        Text("selection range:").width("100%")\n        Text() {\n          Span(this.message)\n        }.width("100%")\n        Text("selection content:").width("100%")\n        Text() {\n          Span(this.content)\n        }.width("100%")\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("20%")\n\n      Row() {\n        Button("updateSpanStyle1")\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.updateSpanStyle({\n              start: this.start,\n              textStyle:\n              {\n                fontWeight: FontWeight.Bolder\n              },\n              imageStyle: {\n                size: ["80px", "80px"],\n                layoutStyle: {\n                  borderRadius: undefined,\n                  margin: undefined\n                }\n              }\n            })\n          })\n\n        Button("updateSpanStyle2")\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.updateSpanStyle({\n              start: this.start,\n              textStyle:\n              {\n                fontWeight: FontWeight.Bolder\n              },\n              imageStyle: {\n                size: ["70px", "70px"],\n                layoutStyle: {\n                  borderRadius: { topLeft: '100px', topRight: '20px', bottomLeft: '100px', bottomRight: '20px' },\n                  margin: { left: '30px', top: '20px', right: '20px', bottom: '20px' }\n                }\n              }\n            })\n          })\n\n        Button("updateSpanStyle3")\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.updateSpanStyle({\n              start: this.start,\n              textStyle:\n              {\n                fontWeight: FontWeight.Bolder\n              },\n              imageStyle: {\n                size: ["60px", "60px"],\n                layoutStyle: {\n                  borderRadius: '-10px',\n                  margin: '-10px'\n                }\n              }\n            })\n          })\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("10%")\n\n      Row() {\n        Button('addImageSpan1')\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.addImageSpan($r('app.media.app_icon'), {\n              imageStyle: {\n                size: ["80px", "80px"],\n                layoutStyle: {\n                  borderRadius: '50px',\n                  margin: '40px'\n                }\n              }\n            })\n          })\n\n        Button('addImageSpan2')\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.addImageSpan($r('app.media.app_icon'), {\n              imageStyle: {\n                size: ["100px", "100px"],\n                verticalAlign: ImageSpanAlignment.BOTTOM,\n                layoutStyle: {\n                  borderRadius: undefined,\n                  margin: undefined\n                }\n              }\n            })\n          })\n\n        Button('addImageSpan3')\n          .fontSize(12)\n          .onClick(() => {\n            this.controller.addImageSpan($r('app.media.app_icon'), {\n              imageStyle: {\n                size: ["60px", "60px"],\n                verticalAlign: ImageSpanAlignment.BOTTOM,\n                layoutStyle: {\n                  borderRadius: { topLeft: '10px', topRight: '20px', bottomLeft: '30px', bottomRight: '40px' },\n                  margin: { left: '10px', top: '20px', right: '30px', bottom: '40px' }\n                }\n              }\n            })\n          })\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("10%")\n\n      Column() {\n        RichEditor(this.options)\n          .onReady(() => {\n            this.controller.addTextSpan("0123456789",\n              {\n                style:\n                {\n                  fontColor: Color.Orange,\n                  fontSize: 30\n                }\n              })\n\n            this.controller.addImageSpan($r("app.media.app_icon"),\n              {\n                imageStyle:\n                {\n                  size: ["60px", "60px"],\n                  verticalAlign: ImageSpanAlignment.BOTTOM,\n                  layoutStyle: {\n                    borderRadius: { topLeft: '10px', topRight: '20px', bottomLeft: '30px', bottomRight: '40px' },\n                    margin: { left: '10px', top: '20px', right: '30px', bottom: '40px' }\n                  }\n                }\n              })\n\n            this.controller.addTextSpan("0123456789",\n              {\n                style:\n                {\n                  fontColor: Color.Black,\n                  fontSize: 30\n                }\n              })\n          })\n          .onSelect((value: RichEditorSelection) => {\n            this.start = value.selection[0];\n            this.end = value.selection[1];\n            this.message = "[" + this.start + ", " + this.end + "]"\n          })\n          .aboutToIMEInput((value: RichEditorInsertValue) => {\n            console.log("---------------------- aboutToIMEInput ----------------------")\n            console.log("insertOffset:" + value.insertOffset)\n            console.log("insertValue:" + value.insertValue)\n            return true;\n          })\n          .onIMEInputComplete((value: RichEditorTextSpanResult) => {\n            console.log("---------------------- onIMEInputComplete ---------------------")\n            console.log("spanIndex:" + value.spanPosition.spanIndex)\n            console.log("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]")\n            console.log("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]")\n            console.log("value:" + value.value)\n          })\n          .aboutToDelete((value: RichEditorDeleteValue) => {\n            console.log("---------------------- aboutToDelete --------------------------")\n            console.log("offset:" + value.offset)\n            console.log("direction:" + value.direction)\n            console.log("length:" + value.length)\n            value.richEditorDeleteSpans.forEach(item => {\n              console.log("---------------------- item --------------------------")\n              console.log("spanIndex:" + item.spanPosition.spanIndex)\n              console.log("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]")\n              console.log("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]")\n              if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {\n                console.log("image:" + (item as RichEditorImageSpanResult).valueResourceStr)\n              } else {\n                console.log("text:" + (item as RichEditorTextSpanResult).value)\n              }\n            })\n            return true;\n          })\n          .onDeleteComplete(() => {\n            console.log("---------------------- onDeleteComplete ------------------------")\n          })\n          .borderWidth(1)\n          .borderColor(Color.Green)\n          .width("100%")\n          .height('80.00%')\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("70%")\n    }\n  }\n}"""
            """// xxx.ets\n\n// 首页组件，包含富文本编辑器和相关操作按钮\n@Entry\n@Component\nstruct Index {\n  controller: RichEditorController = new RichEditorController(); // 富文本编辑器控制器\n  private spanParagraphs: RichEditorParagraphResult[] = []; // 富文本段落数组\n\n  build() {\n    Column() {\n      // 创建富文本编辑器\n      RichEditor({ controller: this.controller })\n        .onReady(() => {\n          // 添加文本段落1\n          this.controller.addTextSpan("0123456789", {\n            style: {\n              fontColor: Color.Pink, // 设置字体颜色为粉色\n              fontSize: "32", // 设置字体大小为32\n            },\n            paragraphStyle: {\n              textAlign: TextAlign.Start, // 设置段落左对齐\n              leadingMargin: 16 // 设置段落首行缩进\n            }\n          })\n          // 添加文本段落2\n          this.controller.addTextSpan("0123456789")\n        })\n        .width("80%") // 设置宽度为80%\n        .height("30%") // 设置高度为30%\n        .border({ width: 1, radius: 5 }) // 设置边框宽度和圆角半径\n        .draggable(false) // 设置不可拖拽\n\n      Column({ space: 5 }) {\n        // 按钮：段落左对齐\n        Button("段落左对齐").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              textAlign: TextAlign.Start, // 设置段落左对齐\n            }\n          })\n        })\n\n        // 按钮：段落右对齐\n        Button("段落右对齐").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              textAlign: TextAlign.End, // 设置段落右对齐\n            }\n          })\n        })\n\n        // 按钮：段落居中\n        Button("段落居中").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              textAlign: TextAlign.Center, // 设置段落居中\n            }\n          })\n        })\n        Divider() // 添加分割线\n        // 按钮：获取段落信息\n        Button("getParagraphs").onClick(() => {\n          this.spanParagraphs = this.controller.getParagraphs({ start: -1, end: -1 })\n          console.log("RichEditor getParagraphs:" + JSON.stringify(this.spanParagraphs))\n        })\n\n        // 按钮：更新文本样式1\n        Button("UpdateSpanStyle1").onClick(() => {\n          this.controller.updateSpanStyle({ start: -1, end: -1,\n            textStyle: {\n              fontColor: Color.Brown, // 设置字体颜色为棕色\n              fontSize: 20 // 设置字体大小为20\n            }\n          })\n        })\n\n        // 按钮：更新文本样式2\n        Button("UpdateSpanStyle2").onClick(() => {\n          this.controller.updateSpanStyle({ start: -1, end: -1,\n            textStyle: {\n              fontColor: Color.Green, // 设置字体颜色为绿色\n              fontSize: 30 // 设置字体大小为30\n            }\n          })\n        })\n      }\n    }\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  controller: RichEditorController = new RichEditorController();\n  private spanParagraphs: RichEditorParagraphResult[] = [];\n\n  build() {\n    Column() {\n      RichEditor({ controller: this.controller })\n        .onReady(() => {\n          this.controller.addTextSpan("0123456789\\n", {\n            style: {\n              fontColor: Color.Pink,\n              fontSize: "32",\n            },\n            paragraphStyle: {\n              textAlign: TextAlign.Start,\n              leadingMargin: 16\n            }\n          })\n          this.controller.addTextSpan("0123456789")\n        })\n        .width("80%")\n        .height("30%")\n        .border({ width: 1, radius: 5 })\n        .draggable(false)\n\n      Column({ space: 5 }) {\n        Button("段落左对齐").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              textAlign: TextAlign.Start,\n            }\n          })\n        })\n\n        Button("段落右对齐").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              textAlign: TextAlign.End,\n            }\n          })\n        })\n\n        Button("段落居中").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              textAlign: TextAlign.Center,\n            }\n          })\n        })\n        Divider()\n        Button("getParagraphs").onClick(() => {\n          this.spanParagraphs = this.controller.getParagraphs({ start: -1, end: -1 })\n          console.log("RichEditor getParagraphs:" + JSON.stringify(this.spanParagraphs))\n        })\n\n        Button("UpdateSpanStyle1").onClick(() => {\n          this.controller.updateSpanStyle({ start: -1, end: -1,\n            textStyle: {\n              fontColor: Color.Brown,\n              fontSize: 20\n            }\n          })\n        })\n\n        Button("UpdateSpanStyle2").onClick(() => {\n          this.controller.updateSpanStyle({ start: -1, end: -1,\n            textStyle: {\n              fontColor: Color.Green,\n              fontSize: 30\n            }\n          })\n        })\n      }\n    }\n  }\n}"""
            """// 为placeholderBuilder2函数编写功能与效果描述注释\n// 创建一个包含图像和文本的行布局，设置图像宽高为24，24，左边距为-5，文本字体大小为10\n// 设置该行布局的宽度为20%，高度为50，内边距为10，背景颜色为红色\n@Builder\nfunction placeholderBuilder2() {\n  Row({ space: 2 }) {\n    Image($r("app.media.icon")).width(24).height(24).margin({ left: -5 })\n    Text('okokokok').fontSize(10)\n  }.width('20%').height(50).padding(10).backgroundColor(Color.Red)\n}\n\n// 为Index结构体中的placeholderBuilder3函数编写功能与效果描述注释\n// 创建一个包含文本"hello"的元素，设置内边距为20，边框宽度为1，宽度为100%\n@Builder\nplaceholderBuilder3() {\n  Text("hello").padding('20').borderWidth(1).width('100%')\n}\n\n// 为Index结构体中的placeholderBuilder4函数编写功能与效果描述注释\n// 创建包含多个行布局的列布局，展示不同方向的子组件布局效果\n@Builder\nplaceholderBuilder4() {\n  Column() {\n    Column({ space: 5 }) {\n      // 显示子组件在容器主轴上行布局的效果\n      // 包含四个文本元素，每个宽度为20%，高度为50，背景颜色不同\n      Flex({ direction: FlexDirection.Row }) {\n        Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n        Text('1').width('20%').height(50).backgroundColor(0xD2B48C)\n        Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n        Text('1').width('20%').height(50).backgroundColor(0xD2B48C)\n      }\n      .height(70)\n      .width('90%')\n      .padding(10)\n      .backgroundColor(0xAFEEEE)\n\n      // 显示子组件在容器主轴上反向行布局的效果\n      // 同上，但子组件排列方向为反向\n      Flex({ direction: FlexDirection.RowReverse }) {\n        Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n        Text('1').width('20%').height(50).backgroundColor(0xD2B48C)\n        Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n        Text('1').width('20%').height(50).backgroundColor(0xD2B48C)\n      }\n      .height(70)\n      .width('90%')\n      .padding(10)\n      .backgroundColor(0xAFEEEE)\n\n      // 显示子组件在容器主轴上列布局的效果\n      // 包含四个文本元素，每个宽度为20%，高度为40，背景颜色不同\n      Flex({ direction: FlexDirection.Column }) {\n        Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)\n        Text('1').width('20%').height(40).backgroundColor(0xD2B48C)\n        Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)\n        Text('1').width('20%').height(40).backgroundColor(0xD2B48C)\n      }\n      .height(160)\n      .width('90%')\n      .padding(10)\n      .backgroundColor(0xAFEEEE)\n\n      // 显示子组件在容器主轴上反向列布局的效果\n      // 同上，但子组件排列方向为反向\n      Flex({ direction: FlexDirection.ColumnReverse }) {\n        Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)\n        Text('1').width('20%').height(40).backgroundColor(0xD2B48C)\n        Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)\n        Text('1').width('20%').height(40).backgroundColor(0xD2B48C)\n      }\n      .height(160)\n      .width('90%')\n      .padding(10)\n      .backgroundColor(0xAFEEEE)\n    }.width('100%').margin({ top: 5 })\n  }.width('100%')\n}\n\n// 为Index结构体中的MyMenu函数编写功能与效果描述注释\n// 创建一个菜单组件，包含两个菜单项，其中第二个菜单项不可用\n@Builder\nMyMenu() {\n  Menu() {\n    MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项1" })\n    MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项2" })\n      .enabled(false)\n  }\n}\n```\n@Builder\nfunction placeholderBuilder2() {\n  Row({ space: 2 }) {\n    Image($r("app.media.icon")).width(24).height(24).margin({ left: -5 })\n    Text('okokokok').fontSize(10)\n  }.width('20%').height(50).padding(10).backgroundColor(Color.Red)\n}\n\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  controller: RichEditorController = new RichEditorController();\n  option: RichEditorOptions = { controller: this.controller };\n  private start: number = 2;\n  private end: number = 4;\n  @State message: string = "[-1, -1]"\n  @State content: string = ""\n  private my_offset: number | undefined = undefined\n  private my_builder: CustomBuilder = undefined\n\n  @Builder\n  placeholderBuilder() {\n    Row({ space: 2 }) {\n      Image($r("app.media.icon")).width(24).height(24).margin({ left: -5 })\n      Text('Custom Popup').fontSize(10)\n    }.width(100).height(50).padding(5)\n  }\n\n  @Builder\n  placeholderBuilder3() {\n    Text("hello").padding('20').borderWidth(1).width('100%')\n  }\n\n  @Builder\n  placeholderBuilder4() {\n    Column() {\n      Column({ space: 5 }) {\n        Text('direction:Row').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({ direction: FlexDirection.Row }) { // 子组件在容器主抽上行布局\n          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n          Text('1').width('20%').height(50).backgroundColor(0xD2B48C)\n          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n          Text('1').width('20%').height(50).backgroundColor(0xD2B48C)\n        }\n        .height(70)\n        .width('90%')\n        .padding(10)\n        .backgroundColor(0xAFEEEE)\n\n        Text('direction:RowReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({ direction: FlexDirection.RowReverse }) { // 子组件在容器主抽上反向行布局\n          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n          Text('1').width('20%').height(50).backgroundColor(0xD2B48C)\n          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n          Text('1').width('20%').height(50).backgroundColor(0xD2B48C)\n        }\n        .height(70)\n        .width('90%')\n        .padding(10)\n        .backgroundColor(0xAFEEEE)\n\n        Text('direction:Column').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({ direction: FlexDirection.Column }) { // 子组件在容器主抽上列布局\n          Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)\n          Text('1').width('20%').height(40).backgroundColor(0xD2B48C)\n          Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)\n          Text('1').width('20%').height(40).backgroundColor(0xD2B48C)\n        }\n        .height(160)\n        .width('90%')\n        .padding(10)\n        .backgroundColor(0xAFEEEE)\n\n        Text('direction:ColumnReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({ direction: FlexDirection.ColumnReverse }) { // 子组件在容器主抽上反向列布局\n          Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)\n          Text('1').width('20%').height(40).backgroundColor(0xD2B48C)\n          Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)\n          Text('1').width('20%').height(40).backgroundColor(0xD2B48C)\n        }\n        .height(160)\n        .width('90%')\n        .padding(10)\n        .backgroundColor(0xAFEEEE)\n      }.width('100%').margin({ top: 5 })\n    }.width('100%')\n  }\n\n  @Builder\n  MyMenu() {\n    Menu() {\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项1" })\n      MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项2" })\n        .enabled(false)\n    }\n  }\n\n  build() {\n    Column() {\n      Column() {\n        Text("selection range:").width("100%")\n        Text() {\n          Span(this.message)\n        }.width("100%")\n\n        Text("selection content:").width("100%")\n        Text() {\n          Span(this.content)\n        }.width("100%")\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("20%")\n\n      Row() {\n        Button("获取选择内容 getSpans").onClick(() => {\n          console.info('getSpans='+JSON.stringify(this.controller.getSpans({ start:1, end:5 })))\n          console.info('getParagraphs='+JSON.stringify(this.controller.getParagraphs({ start:1, end:5 })))\n          this.content = ""\n          this.controller.getSpans({\n            start: this.start,\n            end: this.end\n          }).forEach(item => {\n            if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {\n              if ((item as RichEditorImageSpanResult).valueResourceStr == "") {\n                console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +\n                  (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])\n              } else {\n                console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +\n                  (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +\n                  (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])\n              }\n            } else {\n              this.content += (item as RichEditorTextSpanResult).value;\n              this.content += "\\n"\n              console.info("text span: " + (item as RichEditorTextSpanResult).value)\n            }\n          })\n        })\n        Button("获取选择内容 getSelection").onClick(() => {\n          this.content = "";\n          let select = this.controller.getSelection()\n          console.info("selection start " + select.selection[0] + " end " + select.selection[1])\n          select.spans.forEach(item => {\n            if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {\n              if ((item as RichEditorImageSpanResult).valueResourceStr == "") {\n                console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +\n                  (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])\n              } else {\n                console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +\n                  (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +\n                  (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])\n              }\n            } else {\n              this.content += (item as RichEditorTextSpanResult).value;\n              this.content += "\\n"\n              console.info("text span: " + (item as RichEditorTextSpanResult).value)\n            }\n          })\n        })\n        Button("删除选择内容").onClick(() => {\n          this.controller.deleteSpans({\n            start: this.start,\n            end: this.end\n          })\n        })\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("10%")\n\n      Column() {\n        RichEditor(this.option)\n          .onReady(() => {\n            this.controller.addTextSpan("0123456789",\n              {\n                style:\n                {\n                  fontColor: Color.Orange,\n                  fontSize: 30\n                }\n              })\n            this.controller.addImageSpan($r("app.media.icon"),\n              {\n                imageStyle:\n                {\n                  size: ["57px", "57px"]\n                }\n              })\n          })\n          .onSelect((value: RichEditorSelection) => {\n            this.start = value.selection[0];\n            this.end = value.selection[1];\n            this.message = "[" + this.start + ", " + this.end + "]"\n            console.info("onSelect="+JSON.stringify(value))\n          })\n          .aboutToIMEInput((value: RichEditorInsertValue) => {\n            console.log("---------------------- aboutToIMEInput --------------------")\n            console.info("aboutToIMEInput="+JSON.stringify(value))\n            console.log("insertOffset:" + value.insertOffset)\n            console.log("insertValue:" + value.insertValue)\n            return true;\n          })\n          .onIMEInputComplete((value: RichEditorTextSpanResult) => {\n            console.log("---------------------- onIMEInputComplete --------------------")\n            console.info("onIMEInputComplete="+JSON.stringify(value))\n            console.log("spanIndex:" + value.spanPosition.spanIndex)\n            console.log("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]")\n            console.log("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]")\n            console.log("value:" + value.value)\n          })\n          .aboutToDelete((value: RichEditorDeleteValue) => {\n            value.richEditorDeleteSpans.forEach(item => {\n              console.log("---------------------- item --------------------")\n              console.info("spanIndex=" + item.spanPosition.spanIndex)\n              console.log("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]")\n              console.log("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]")\n              if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {\n                if ((item as RichEditorImageSpanResult).valueResourceStr == "") {\n                  console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +\n                  (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])\n                } else {\n                  console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +\n                  (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +\n                  (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])\n                }\n              } else {\n                console.info("delete text: " + (item as RichEditorTextSpanResult).value)\n              }\n            })\n            return true;\n          })\n          .borderWidth(1)\n          .borderColor(Color.Green)\n          .width("100%")\n          .height("30%")\n\n        Button("add span")\n          .onClick(() => {\n            let num = this.controller.addBuilderSpan(this.my_builder, { offset: this.my_offset })\n            console.info('addBuilderSpan return ' + num)\n          })\n        Button("add image")\n          .onClick(() => {\n            let num = this.controller.addImageSpan($r("app.media.icon"), {\n              imageStyle: {\n                size: ["50px", "50px"],\n                verticalAlign: ImageSpanAlignment.BOTTOM,\n                layoutStyle: {\n                  borderRadius: undefined,\n                  margin: undefined\n                }\n              }\n            })\n            console.info('addImageSpan return' + num)\n          })\n        Row() {\n          Button('builder1').onClick(() => {\n            this.my_builder = () => {\n              this.placeholderBuilder()\n            }\n          })\n          Button('builder2').onClick(() => {\n            this.my_builder = placeholderBuilder2.bind(this)\n          })\n          Button('builder3').onClick(() => {\n            this.my_builder = () => {\n              this.placeholderBuilder3()\n            }\n          })\n          Button('builder4').onClick(() => {\n            this.my_builder = () => {\n              this.placeholderBuilder4()\n            }\n          })\n        }\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("70%")\n    }\n  }\n}"""
            """@Entry\n@Component\nstruct TextExample7 {\n  controller: RichEditorController = new RichEditorController(); // 创建富文本编辑器控制器\n  options: RichEditorOptions = { controller: this.controller }; // 设置富文本编辑器选项\n  @State phoneNumber: string = '(86) (755) ********'; // 手机号码\n  @State url: string = 'www.********.com'; // 网址\n  @State email: string = '***@example.com'; // 电子邮件地址\n  @State address: string = 'XX省XX市XX区XXXX'; // 地址\n  @State enableDataDetector: boolean = true; // 是否启用数据检测\n  @State enablePreviewText: boolean = false; // 是否启用预览文本\n  @State types: TextDataDetectorType[] = []; // 数据检测类型数组\n\n  build() {\n    Row() {\n      Column() {\n        RichEditor(this.options) // 使用富文本编辑器\n          .onReady(() => {\n            this.controller.addTextSpan('电话号码：' + this.phoneNumber + '\n', // 添加电话号码文本\n              {\n                style:\n                {\n                  fontSize: 30 // 设置字体大小\n                }\n              })\n            this.controller.addTextSpan('链接：' + this.url + '\n', // 添加链接文本\n              {\n                style:\n                {\n                  fontSize: 30 // 设置字体大小\n                }\n              })\n            this.controller.addTextSpan('邮箱：' + this.email + '\n', // 添加邮箱文本\n              {\n                style:\n                {\n                  fontSize: 30 // 设置字体大小\n                }\n              })\n            this.controller.addTextSpan('地址：' + this.address, // 添加地址文本\n              {\n                style:\n                {\n                  fontSize: 30 // 设置字体大小\n                }\n              })\n          })\n          .copyOptions(CopyOptions.InApp) // 复制选项设置为应用内复制\n          .enableDataDetector(this.enableDataDetector) // 启用数据检测\n          .dataDetectorConfig({types : this.types, onDetectResultUpdate: (result: string)=>{}}) // 数据检测配置\n          .enablePreviewText(this.enablePreviewText) // 启用预览文本\n          .borderWidth(1) // 设置边框宽度\n          .padding(10) // 设置内边距\n          .width('100%') // 设置宽度为100%\n      }\n      .width('100%') // 设置宽度为100%\n    }\n  }\n}\n```\n@Entry\n@Component\nstruct TextExample7 {\n  controller: RichEditorController = new RichEditorController();\n  options: RichEditorOptions = { controller: this.controller };\n  @State phoneNumber: string = '(86) (755) ********';\n  @State url: string = 'www.********.com';\n  @State email: string = '***@example.com';\n  @State address: string = 'XX省XX市XX区XXXX';\n  @State enableDataDetector: boolean = true;\n  @State enablePreviewText: boolean = false;\n  @State types: TextDataDetectorType[] = [];\n\n  build() {\n    Row() {\n      Column() {\n        RichEditor(this.options)\n          .onReady(() => {\n            this.controller.addTextSpan('电话号码：' + this.phoneNumber + '\\n',\n              {\n                style:\n                {\n                  fontSize: 30\n                }\n              })\n            this.controller.addTextSpan('链接：' + this.url + '\\n',\n              {\n                style:\n                {\n                  fontSize: 30\n                }\n              })\n            this.controller.addTextSpan('邮箱：' + this.email + '\\n',\n              {\n                style:\n                {\n                  fontSize: 30\n                }\n              })\n            this.controller.addTextSpan('地址：' + this.address,\n              {\n                style:\n                {\n                  fontSize: 30\n                }\n              })\n          })\n          .copyOptions(CopyOptions.InApp)\n          .enableDataDetector(this.enableDataDetector)\n          .dataDetectorConfig({types : this.types, onDetectResultUpdate: (result: string)=>{}})\n          .enablePreviewText(this.enablePreviewText)\n          .borderWidth(1)\n          .padding(10)\n          .width('100%')\n      }\n      .width('100%')\n    }\n  }\n}"""
            """@Entry\n@Component\nstruct RichEditorDemo {\n  @State color: Color|string = ""  // 定义状态变量color，用于存储颜色信息\n  controller: RichEditorController = new RichEditorController();  // 实例化富文本编辑器控制器\n  build() {\n    Column() {\n      Row(){\n        Button("改为红色").onClick(() => {\n          this.color = Color.Red  // 点击按钮后将color状态设置为红色\n        })\n      }.margin({top:50})  // 设置按钮距离顶部的间距为50\n      RichEditor({ controller: this.controller })  // 创建富文本编辑器组件并传入控制器\n        .onReady(()=>{\n          this.controller.addTextSpan('测试文字测试文字测试文字测试文字测试文字测试文字')  // 在富文本编辑器准备就绪时添加文本段落\n        })\n        .width("100%")  // 设置富文本编辑器宽度为100%\n        .border({ width: 1, radius: 5 })  // 设置边框宽度为1，圆角半径为5\n        .key('RichEditor')  // 设置组件的唯一标识为'RichEditor'\n        .caretColor(this.color)  // 设置光标颜色为当前color状态值，用于展示光标颜色变化\n        .selectedBackgroundColor(this.color)  // 设置选中文本背景色为当前color状态值，用于展示选中文本背景色变化\n        .margin({top:50})  // 设置富文本编辑器距离顶部的间距为50\n    }\n    .width('100%')  // 设置整体布局宽度为100%\n  }\n}\n```\n\n在上述示例代码中，主要实现了一个富文本编辑器的演示界面，用户可以通过按钮切换光标颜色和选中文本背景色。具体描述如下：\n\n1. 定义了一个状态变量`color`，用于存储颜色信息。\n2. 实例化了一个富文本编辑器控制器`controller`。\n3. 创建了一个按钮，点击按钮后将`color`状态设置为红色。\n4. 创建了一个富文本编辑器组件，设置了宽度、边框样式、唯一标识等属性。\n5. 在富文本编辑器准备就绪时，添加了一个测试文本段落。\n6. 使用`caretColor`方法设置光标颜色为当前`color`状态值，展示光标颜色的变化。\n7. 使用`selectedBackgroundColor`方法设置选中文本背景色为当前`color`状态值，展示选中文本背景色的变化。\n8. 最后设置了整体布局的宽度为100%。\n@Entry\n@Component\nstruct RichEditorDemo {\n  @State color: Color|string = ""\n  controller: RichEditorController = new RichEditorController();\n  build() {\n    Column() {\n      Row(){\n        Button("改为红色").onClick(() => {\n          this.color = Color.Red\n        })\n      }.margin({top:50})\n      RichEditor({ controller: this.controller })\n        .onReady(()=>{\n          this.controller.addTextSpan('测试文字测试文字测试文字测试文字测试文字测试文字')\n        })\n        .width("100%")\n        .border({ width: 1, radius: 5 })\n        .key('RichEditor')\n        .caretColor(this.color)  //光标颜色\n        .selectedBackgroundColor(this.color)  //选中背景色\n        .margin({top:50})\n    }\n    .width('100%')\n  }\n}"""
            """// 在这个示例中，展示了如何使用lineHeight和letterSpacing属性来控制文本的行高和字符间距。\n// 用户可以通过点击按钮增加或减少行高和字符间距，同时实时更新RichEditor中的文本样式。\n// 通过滚动显示区域展示当前的行高和字符间距数值。\n\n@Entry\n@Component\nstruct RichEditorDemo03 {\n  controller: RichEditorController = new RichEditorController(); // 创建RichEditorController实例\n  options: RichEditorOptions = { controller: this.controller }; // 设置RichEditorOptions参数\n\n  @State start: number = -1; // 定义起始位置状态\n  @State end: number = -1; // 定义结束位置状态\n  @State LH:number = 50 // 定义行高状态\n  @State LS:number = 20 // 定义字符间距状态\n\n  build() {\n    Column() {\n      Scroll(){\n        Column(){\n          Row() {\n            // 按钮功能：增加行高\n            Button("行高++").onClick(()=>{\n              this.LH = this.LH + 5\n              this.controller.updateSpanStyle({\n                start: this.start,\n                end: this.end,\n                textStyle:\n                {\n                  lineHeight: this.LH\n                }\n              })\n            })\n            // 按钮功能：减少行高\n            Button("行高--").onClick(()=>{\n              this.LH = this.LH - 5\n              this.controller.updateSpanStyle({\n                start: this.start,\n                end: this.end,\n                textStyle:\n                {\n                  lineHeight: this.LH\n                }\n              })\n            })\n            // 按钮功能：增加字符间距\n            Button("字符间距++").onClick(()=>{\n              this.LS = this.LS + 5\n              this.controller.updateSpanStyle({\n                start: this.start,\n                end: this.end,\n                textStyle:\n                {\n                  letterSpacing: this.LS\n                }\n              })\n            })\n            // 按钮功能：减少字符间距\n            Button("字符间距--").onClick(()=>{\n              this.LS = this.LS - 5\n              this.controller.updateSpanStyle({\n                start: this.start,\n                end: this.end,\n                textStyle:\n                {\n                  letterSpacing: this.LS\n                }\n              })\n            })\n          }\n        }\n      }.borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("20%")\n      .margin({top: 20})\n\n      Scroll(){\n        Column() {\n          // 显示当前行高数值\n          Text("LineHeight:" + this.LH).width("100%")\n          // 显示当前字符间距数值\n          Text("LetterSpacing:" + this.LS).width("100%")\n        }\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("20%")\n      .margin({bottom: 20})\n\n      Column() {\n        // 创建RichEditor组件并设置样式\n        RichEditor(this.options).clip(true).padding(10)\n          .onReady(() => {\n            // 添加文本段落1\n            this.controller.addTextSpan("012345",\n              {\n                style:\n                {\n                  fontColor: Color.Orange,\n                  fontSize: 30,\n                  lineHeight: this.LH,\n                  letterSpacing: this.LS\n                }\n              })\n            // 添加文本段落2\n            this.controller.addTextSpan("6789",\n              {\n                style:\n                {\n                  fontColor: Color.Black,\n                  fontSize: 30,\n                  lineHeight: this.LH,\n                  letterSpacing: this.LS\n                }\n              })\n          })\n          .borderWidth(1)\n          .borderColor(Color.Green)\n          .width(400)\n          .height(400)\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("60%")\n    }\n  }\n}\n```\n@Entry\n@Component\nstruct RichEditorDemo03 {\n  controller: RichEditorController = new RichEditorController();\n  options: RichEditorOptions = { controller: this.controller };\n  @State start: number = -1;\n  @State end: number = -1;\n  @State LH:number = 50\n  @State LS:number = 20\n\n  build() {\n    Column() {\n      Scroll(){\n        Column(){\n          Row() {\n            Button("行高++").onClick(()=>{\n              this.LH = this.LH + 5\n              this.controller.updateSpanStyle({\n                start: this.start,\n                end: this.end,\n                textStyle:\n                {\n                  lineHeight: this.LH\n                }\n              })\n            })\n            Button("行高--").onClick(()=>{\n              this.LH = this.LH - 5\n              this.controller.updateSpanStyle({\n                start: this.start,\n                end: this.end,\n                textStyle:\n                {\n                  lineHeight: this.LH\n                }\n              })\n            })\n            Button("字符间距++").onClick(()=>{\n              this.LS = this.LS + 5\n              this.controller.updateSpanStyle({\n                start: this.start,\n                end: this.end,\n                textStyle:\n                {\n                  letterSpacing: this.LS\n                }\n              })\n            })\n            Button("字符间距--").onClick(()=>{\n              this.LS = this.LS - 5\n              this.controller.updateSpanStyle({\n                start: this.start,\n                end: this.end,\n                textStyle:\n                {\n                  letterSpacing: this.LS\n                }\n              })\n            })\n          }\n        }\n      }.borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("20%")\n      .margin({top: 20})\n\n      Scroll(){\n        Column() {\n          Text("LineHeight:" + this.LH).width("100%")\n          Text("LetterSpacing:" + this.LS).width("100%")\n        }\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("20%")\n      .margin({bottom: 20})\n\n      Column() {\n        RichEditor(this.options).clip(true).padding(10)\n          .onReady(() => {\n            this.controller.addTextSpan("012345",\n              {\n                style:\n                {\n                  fontColor: Color.Orange,\n                  fontSize: 30,\n                  lineHeight: this.LH,\n                  letterSpacing: this.LS\n                }\n              })\n            this.controller.addTextSpan("6789",\n              {\n                style:\n                {\n                  fontColor: Color.Black,\n                  fontSize: 30,\n                  lineHeight: this.LH,\n                  letterSpacing: this.LS\n                }\n              })\n          })\n          .borderWidth(1)\n          .borderColor(Color.Green)\n          .width(400)\n          .height(400)\n      }\n      .borderWidth(1)\n      .borderColor(Color.Red)\n      .width("100%")\n      .height("60%")\n    }\n  }\n}"""
            """preventDefault使用示例\n\n@Entry\n@Component\nstruct RichEditorDemo {\n  controller: RichEditorController = new RichEditorController();\n  options: RichEditorOptions = { controller: this.controller };\n\n  build() {\n    Column({ space: 2 }) {\n      RichEditor(this.options)\n        .onReady(() => {\n          this.controller.addTextSpan('RichEditor preventDefault')\n        })\n        .onPaste((event?: PasteEvent) => {\n          if (event != undefined && event.preventDefault) {\n            event.preventDefault(); // 阻止默认粘贴行为\n          }\n        })\n        .borderWidth(1) // 设置边框宽度为1\n        .borderColor(Color.Green) // 设置边框颜色为绿色\n        .width('100%') // 设置宽度为100%\n        .height('40%') // 设置高度为40%\n    }\n  }\n}\n```\n\n在上述示例代码中：\n- `RichEditorDemo` 结构体包含了 `controller` 和 `options` 两个属性，分别用于控制富文本编辑器和设置编辑器选项。\n- `build()` 方法用于构建富文本编辑器组件。\n- `RichEditor` 组件使用传入的 `options` 进行初始化，并设置了一系列属性和事件监听。\n- `onReady` 事件在编辑器准备就绪时触发，向编辑器添加文本片段 'RichEditor preventDefault'。\n- `onPaste` 事件监听粘贴操作，当事件存在且支持 `preventDefault` 方法时，阻止默认粘贴行为。\n- `borderWidth(1)` 设置边框宽度为1。\n- `borderColor(Color.Green)` 设置边框颜色为绿色。\n- `width('100%')` 设置宽度为100%。\n- `height('40%')` 设置高度为40%。\n@Entry\n@Component\nstruct RichEditorDemo {\n  controller: RichEditorController = new RichEditorController();\n  options: RichEditorOptions = { controller: this.controller };\n\n  build() {\n    Column({ space: 2 }) {\n      RichEditor(this.options)\n        .onReady(() => {\n          this.controller.addTextSpan('RichEditor preventDefault')\n        })\n        .onPaste((event?: PasteEvent) => {\n          if (event != undefined && event.preventDefault) {\n            event.preventDefault();\n          }\n        })\n        .borderWidth(1)\n        .borderColor(Color.Green)\n        .width('100%')\n        .height('40%')\n    }\n  }\n}"""
            """:@Entry\n@Component\nstruct SoftKeyboardEnterTypeExample {\n  controller: RichEditorController = new RichEditorController()\n\n    build() {\n    Column() {\n      // 创建一个富文本编辑器，设置高度为200，边距为10，边框宽度为1，边框颜色为红色，宽度为100%\n      Button("停止编辑").onClick(()=>{\n        this.controller.stopEditing()\n      })\n      RichEditor({ controller: this.controller })\n        .margin(10)\n        .border({ width: 1 })\n        .height(200)\n        .borderWidth(1)\n        .borderColor(Color.Red)\n        .width("100%")\n        // 设置软键盘的回车键类型为搜索\n        .enterKeyType(EnterKeyType.Search)\n        // 当用户点击软键盘的提交按钮时触发的事件\n        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {\n          console.log("trigger richeditor onsubmit" + enterKey);\n          // 在富文本编辑器中添加文本片段，显示触发的回车键类型\n          this.controller.addTextSpan(" type["+ enterKey +"] triggerred")\n          // 保持编辑状态，不清空输入框内容\n          event.keepEditableState();\n        })\n    }.height("100%").justifyContent(FlexAlign.Center)\n  }\n}\n```\n\n在上面的示例代码中：\n\n1. `Button("停止编辑")`：创建一个按钮，点击按钮时调用`this.controller.stopEditing()`方法停止编辑。\n\n2. `RichEditor({ controller: this.controller })`：创建一个富文本编辑器，设置相关样式属性。\n\n3. `enterKeyType(EnterKeyType.Search)`：设置软键盘的回车键类型为搜索，用户在输入时按下回车键会触发搜索功能。\n\n4. `onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => { ... })`：当用户点击软键盘的提交按钮时触发的事件，可以获取到触发事件的回车键类型和提交事件对象。\n@Entry\n@Component\nstruct SoftKeyboardEnterTypeExample {\n  controller: RichEditorController = new RichEditorController()\n\n    build() {\n    Column() {\n      Button("停止编辑").onClick(()=>{\n        this.controller.stopEditing()\n      })\n      RichEditor({ controller: this.controller })\n        .margin(10)\n        .border({ width: 1 })\n        .height(200)\n        .borderWidth(1)\n        .borderColor(Color.Red)\n        .width("100%")\n        .enterKeyType(EnterKeyType.Search)\n        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {\n          console.log("trigger richeditor onsubmit" + enterKey);\n          this.controller.addTextSpan(" type["+ enterKey +"] triggerred")\n          event.keepEditableState();\n        })\n    }.height("100%").justifyContent(FlexAlign.Center)\n  }\n}"""
            """// lineBreakStrategy属性值设置、更新、查询使用示例\n\n// RichEditorController用于控制富文本编辑器的操作\n// LineBreakStrategyExample结构体包含了对lineBreakStrategy属性值的设置、更新和查询功能\n\n// 设置初始状态下的富文本编辑器内容，并设置lineBreakStrategy为GREEDY\n// 效果：在富文本编辑器中显示一段文本，采用GREEDY的折行策略\nthis.controller.addTextSpan(this.testStr, {\n  style: {\n    fontColor: Color.Black,\n    fontSize: "32",\n  },\n  paragraphStyle: {\n    textAlign: TextAlign.Start,\n    lineBreakStrategy: LineBreakStrategy.GREEDY\n  }\n})\n\n// 点击按钮设置折行类型为GREEDY\n// 效果：点击按钮后，将富文本编辑器当前段落的折行策略设置为GREEDY\nButton("设置折行类型GREEDY").onClick(() => {\n  this.controller.updateParagraphStyle({ start: -1, end: -1,\n    style: {\n      lineBreakStrategy: LineBreakStrategy.GREEDY,\n    }\n  })\n})\n\n// 点击按钮设置折行类型为HIGH_QUALITY\n// 效果：点击按钮后，将富文本编辑器当前段落的折行策略设置为HIGH_QUALITY\nButton("设置折行类型HIGH_QUALITY").onClick(() => {\n  this.controller.updateParagraphStyle({ start: -1, end: -1,\n    style: {\n      lineBreakStrategy: LineBreakStrategy.HIGH_QUALITY,\n    }\n  })\n})\n\n// 点击按钮设置折行类型为BALANCED\n// 效果：点击按钮后，将富文本编辑器当前段落的折行策略设置为BALANCED\nButton("设置折行类型BALANCED").onClick(() => {\n  this.controller.updateParagraphStyle({ start: -1, end: -1,\n    style: {\n      lineBreakStrategy: LineBreakStrategy.BALANCED,\n    }\n  })\n})\n\n// 点击按钮获取当前段落的lineBreakStrategy属性值\n// 效果：点击按钮后，获取富文本编辑器当前段落的折行策略属性值，并显示在界面上\nButton("获取linebreak属性值").onClick(() => {\n  this.spanParagraphs = this.controller.getParagraphs({ start: -1, end: -1 })\n  console.log("RichEditor getParagraphs:" + JSON.stringify(this.spanParagraphs))\n  this.spanParagraphs.forEach(item => {\n    if (typeof(item as RichEditorParagraphResult)['style'] != 'undefined') {\n      this.attributeValue = ""\n      console.info('lineBreakStrategy:' + JSON.stringify((item as RichEditorParagraphResult)['style']))\n      this.attributeValue += this.lineBreakOptionStr[Number((item as RichEditorParagraphResult)['style'].lineBreakStrategy)];\n    }\n  })\n})\n```\n@Entry\n@Component\nstruct LineBreakStrategyExample {\n  controller: RichEditorController = new RichEditorController();\n  private spanParagraphs: RichEditorParagraphResult[] = [];\n  @State lineBreakOptionStr: string[] = ['GREEDY', 'HIGH_QUALITY', 'BALANCED']\n  @State attributeValue: string = ""\n  @State testStr: string = "0123456789,0123456789,0123456789,0123456789,0123456789."\n  build() {\n    Column() {\n      RichEditor({ controller: this.controller })\n        .onReady(() => {\n          this.controller.addTextSpan(this.testStr, {\n            style: {\n              fontColor: Color.Black,\n              fontSize: "32",\n            },\n            paragraphStyle: {\n              textAlign: TextAlign.Start,\n              lineBreakStrategy: LineBreakStrategy.GREEDY\n            }\n          })\n        })\n        .width(400)\n        .height(300)\n        .margin({bottom:20})\n        .draggable(false)\n      Column(){\n        Text('linebreak属性值为：' + this.attributeValue).fontSize(20).fontColor(Color.Black)\n      }.margin({bottom: 10})\n      Column({ space: 10 }) {\n        Button("设置折行类型GREEDY").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              lineBreakStrategy: LineBreakStrategy.GREEDY,\n            }\n          })\n        })\n        Button("设置折行类型HIGH_QUALITY").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              lineBreakStrategy: LineBreakStrategy.HIGH_QUALITY,\n            }\n          })\n        })\n        Button("设置折行类型BALANCED").onClick(() => {\n          this.controller.updateParagraphStyle({ start: -1, end: -1,\n            style: {\n              lineBreakStrategy: LineBreakStrategy.BALANCED,\n            }\n          })\n        })\n        Divider()\n        Row(){\n          Button("获取linebreak属性值").onClick(() => {\n            this.spanParagraphs = this.controller.getParagraphs({ start: -1, end: -1 })\n            console.log("RichEditor getParagraphs:" + JSON.stringify(this.spanParagraphs))\n            this.spanParagraphs.forEach(item => {\n              if(typeof(item as RichEditorParagraphResult)['style'] != 'undefined'){\n                this.attributeValue = ""\n                console.info('lineBreakStrategy:'+ JSON.stringify((item as RichEditorParagraphResult)['style']))\n                this.attributeValue += this.lineBreakOptionStr[Number((item as RichEditorParagraphResult)['style'].lineBreakStrategy)];\n              }\n            })\n          })\n        }\n      }\n    }\n  }\n}"""
            """// 导入所需的组件和模块\nimport { LengthMetrics } from '@kit.ArkUI'\nimport { image } from '@kit.ImageKit'\n\n// 定义示例组件 Index\n@Entry\n@Component\nstruct Index {\n  // 初始化属性\n  stringLength: number = 0;\n  imagePixelMap: image.PixelMap | undefined = undefined;\n  @State selection: string = "";\n  @State content: string = "";\n  @State range: string = "";\n  @State replaceString: string = "";\n  @State rangeBefore: string = "";\n  @State rangeAfter: string = "";\n  \n  // 定义样式\n  richEditorStyledString: MutableStyledString = new MutableStyledString("");\n  textStyle: TextStyle = new TextStyle({\n    fontWeight: FontWeight.Lighter,\n    fontFamily: 'HarmonyOS Sans',\n    fontColor: Color.Green,\n    fontSize: LengthMetrics.vp(30),\n    fontStyle: FontStyle.Normal\n  })\n  fontStyle1: TextStyle = new TextStyle({ fontColor: Color.Blue });\n  fontStyle2: TextStyle = new TextStyle({\n    fontWeight: FontWeight.Bolder,\n    fontFamily: 'Arial',\n    fontColor: Color.Orange,\n    fontSize: LengthMetrics.vp(30),\n    fontStyle: FontStyle.Italic\n  })\n  \n  // 创建属性字符串对象\n  mutableStyledString: MutableStyledString = new MutableStyledString("初始属性字符串",\n    [{ start: 0, length: 5, styledKey: StyledStringKey.FONT, styledValue: this.fontStyle1 }]);\n  styledString: StyledString = new StyledString("插入属性字符串",\n    [{ start: 2, length: 4, styledKey: StyledStringKey.FONT, styledValue: this.fontStyle2 }]);\n  \n  // 控制器和选项\n  controller: RichEditorStyledStringController = new RichEditorStyledStringController();\n  options: RichEditorStyledStringOptions = {controller: this.controller};\n  \n  // 文本内容变化回调\n  contentChangedListener: StyledStringChangedListener = {\n    onWillChange: (value: StyledStringChangeValue) => {\n      this.range = '[ ' + value.range.start + ' , ' + value.range.end + ' ]';\n      this.replaceString = value.replacementString.getString();\n      return true;\n    },\n    onDidChange: (rangeBefore, rangeAfter) => {\n      this.rangeBefore = '[ ' + rangeBefore.start + ' , ' + rangeBefore.end + ' ]';\n      this.rangeAfter = '[ ' + rangeAfter.start + ' , ' + rangeAfter.end + ' ]';\n    }\n  }\n\n  // 异步方法，准备展示时初始化图片像素映射\n  async aboutToAppear() {\n    console.info("aboutToAppear initial imagePixelMap");\n    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.icon'));\n  }\n\n  // 从资源获取像素映射\n  private async getPixmapFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    })\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength))\n    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    })\n    await imageSource.release()\n    return createPixelMap\n  }\n\n  // 构建组件\n  build() {\n    Column() {\n      // 选中区信息展示\n      Column() {\n        Text("选中区信息")\n          .fontSize(20)\n          .width("100%")\n        Text("selection range: " + this.selection).width("100%")\n        Text("selection content: " + this.content).width("100%")\n      }\n      .borderWidth(1)\n      .borderColor(Color.Black)\n      .width("100%")\n      .height("10%")\n\n      // onWillChange回调信息展示\n      Column() {\n        Text("onWillChange回调信息")\n          .fontSize(20)\n          .width("100%")\n        Text("range: " + this.range).width("100%")\n        Text("replacementString: " + this.replaceString).width("100%")\n        Text("onWillChange回调信息")\n          .fontSize(20)\n          .width("100%")\n        Text("rangeBefore: " + this.rangeBefore).width("100%")\n        Text("rangeAfter: " + this.rangeAfter).width("100%")\n      }\n      .borderWidth(1)\n      .borderColor(Color.Black)\n      .width("100%")\n      .height("20%")\n\n      // 富文本编辑器\n      RichEditor(this.options)\n        .onReady(() => {\n          // 注册文本变化回调\n          this.controller.onContentChanged(this.contentChangedListener);\n          // 设定组件展示的属性字符串\n          this.controller.setStyledString(this.mutableStyledString);\n        })\n        .height("20%")\n        .width("100%")\n        .borderWidth(1)\n        .borderColor(Color.Black)\n\n      // 插入图片和文本按钮\n      Column() {\n        Row() {\n          Button("插入图片").onClick(() => {\n            if (this.imagePixelMap !== undefined) {\n              let imageStyledString = new MutableStyledString(new ImageAttachment({\n                value: this.imagePixelMap,\n                size: { width: 50, height: 50 },\n                layoutStyle: { borderRadius: LengthMetrics.vp(10) },\n                verticalAlign: ImageSpanAlignment.BASELINE,\n                objectFit: ImageFit.Contain\n              }))\n              this.richEditorStyledString = this.controller.getStyledString();\n              this.richEditorStyledString.appendStyledString(imageStyledString);\n              this.controller.setStyledString(this.richEditorStyledString);\n              this.controller.setCaretOffset(this.richEditorStyledString.length);\n            }\n          })\n          Button("插入文本").onClick(() => {\n              this.richEditorStyledString = this.controller.getStyledString();\n              this.richEditorStyledString.appendStyledString(this.styledString);\n              this.controller.setStyledString(this.richEditorStyledString);\n              this.controller.setCaretOffset(this.richEditorStyledString.length);\n          })\n        }\n        Row() {\n          Button("获取选中内容").onClick(() => {\n            let richEditorSelection = this.controller.getSelection();\n            let start = richEditorSelection.start ? richEditorSelection.start : 0;\n            let end = richEditorSelection.end ? richEditorSelection.end : 0;\n            this.richEditorStyledString = this.controller.getStyledString();\n            this.selection = '[ ' + start + ' , ' + end + ' ]';\n            if (start == end) {\n              this.content = "";\n            } else {\n              this.content = this.richEditorStyledString.subStyledString(start, end - start).getString();\n            }\n          })\n          Button("更新选中样式").onClick(() => {\n            let richEditorSelection = this.controller.getSelection();\n            let start = richEditorSelection.start ? richEditorSelection.start : 0;\n            let end = richEditorSelection.end ? richEditorSelection.end : 0;\n            this.richEditorStyledString = this.controller.getStyledString();\n            this.richEditorStyledString.setStyle({\n              start: start,\n              length: end - start,\n              styledKey: StyledStringKey.FONT,\n              styledValue: this.textStyle\n            })\n            this.controller.setStyledString(this.richEditorStyledString);\n          })\n          Button("删除选中内容").onClick(() => {\n            let richEditorSelection = this.controller.getSelection();\n            let start = richEditorSelection.start ? richEditorSelection.start : 0;\n            let end = richEditorSelection.end ? richEditorSelection.end : 0;\n            this.richEditorStyledString = this.controller.getStyledString();\n            this.richEditorStyledString.removeString(start, end - start);\n            this.controller.setStyledString(this.richEditorStyledString);\n          })\n        }\n      }\n      .width("100%")\n    }\n  }\n}\n```\nimport { LengthMetrics } from '@kit.ArkUI'\nimport { image } from '@kit.ImageKit'\n\n@Entry\n@Component\nstruct Index {\n  stringLength: number = 0;\n  imagePixelMap: image.PixelMap | undefined = undefined;\n  @State selection: string = "";\n  @State content: string = "";\n  @State range: string = "";\n  @State replaceString: string = "";\n  @State rangeBefore: string = "";\n  @State rangeAfter: string = "";\n  richEditorStyledString: MutableStyledString = new MutableStyledString("");\n  textStyle: TextStyle = new TextStyle({\n    fontWeight: FontWeight.Lighter,\n    fontFamily: 'HarmonyOS Sans',\n    fontColor: Color.Green,\n    fontSize: LengthMetrics.vp(30),\n    fontStyle: FontStyle.Normal\n  })\n  fontStyle1: TextStyle = new TextStyle({ fontColor: Color.Blue });\n  fontStyle2: TextStyle = new TextStyle({\n    fontWeight: FontWeight.Bolder,\n    fontFamily: 'Arial',\n    fontColor: Color.Orange,\n    fontSize: LengthMetrics.vp(30),\n    fontStyle: FontStyle.Italic\n  })\n  // 创建属性字符串对象\n  mutableStyledString: MutableStyledString = new MutableStyledString("初始属性字符串",\n    [{ start: 0, length: 5, styledKey: StyledStringKey.FONT, styledValue: this.fontStyle1 }]);\n  styledString: StyledString = new StyledString("插入属性字符串",\n    [{ start: 2, length: 4, styledKey: StyledStringKey.FONT, styledValue: this.fontStyle2 }]);\n  controller: RichEditorStyledStringController = new RichEditorStyledStringController();\n  options: RichEditorStyledStringOptions = {controller: this.controller};\n  // 文本内容变化回调\n  contentChangedListener: StyledStringChangedListener = {\n    onWillChange: (value: StyledStringChangeValue) => {\n      this.range = '[ ' + value.range.start + ' , ' + value.range.end + ' ]';\n      this.replaceString = value.replacementString.getString();\n      return true;\n    },\n    onDidChange: (rangeBefore, rangeAfter) => {\n      this.rangeBefore = '[ ' + rangeBefore.start + ' , ' + rangeBefore.end + ' ]';\n      this.rangeAfter = '[ ' + rangeAfter.start + ' , ' + rangeAfter.end + ' ]';\n    }\n  }\n\n  async aboutToAppear() {\n    console.info("aboutToAppear initial imagePixelMap");\n    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.icon'));\n  }\n\n  private async getPixmapFromMedia(resource: Resource) {\n    let unit8Array = await getContext(this)?.resourceManager?.getMediaContent({\n      bundleName: resource.bundleName,\n      moduleName: resource.moduleName,\n      id: resource.id\n    })\n    let imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength))\n    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({\n      desiredPixelFormat: image.PixelMapFormat.RGBA_8888\n    })\n    await imageSource.release()\n    return createPixelMap\n  }\n\n\n\n  build() {\n    Column() {\n      Column() {\n        Text("选中区信息")\n          .fontSize(20)\n          .width("100%")\n        Text("selection range: " + this.selection).width("100%")\n        Text("selection content: " + this.content).width("100%")\n      }\n      .borderWidth(1)\n      .borderColor(Color.Black)\n      .width("100%")\n      .height("10%")\n\n      Column() {\n        Text("onWillChange回调信息")\n          .fontSize(20)\n          .width("100%")\n        Text("range: " + this.range).width("100%")\n        Text("replacementString: " + this.replaceString).width("100%")\n        Text("onWillChange回调信息")\n          .fontSize(20)\n          .width("100%")\n        Text("rangeBefore: " + this.rangeBefore).width("100%")\n        Text("rangeAfter: " + this.rangeAfter).width("100%")\n      }\n      .borderWidth(1)\n      .borderColor(Color.Black)\n      .width("100%")\n      .height("20%")\n\n      RichEditor(this.options)\n        .onReady(() => {\n          // 注册文本变化回调\n          this.controller.onContentChanged(this.contentChangedListener);\n          // 设定组件展示的属性字符串\n          this.controller.setStyledString(this.mutableStyledString);\n        })\n        .height("20%")\n        .width("100%")\n        .borderWidth(1)\n        .borderColor(Color.Black)\n\n      Column() {\n        Row() {\n          Button("插入图片").onClick(() => {\n            if (this.imagePixelMap !== undefined) {\n              let imageStyledString = new MutableStyledString(new ImageAttachment({\n                value: this.imagePixelMap,\n                size: { width: 50, height: 50 },\n                layoutStyle: { borderRadius: LengthMetrics.vp(10) },\n                verticalAlign: ImageSpanAlignment.BASELINE,\n                objectFit: ImageFit.Contain\n              }))\n              // 获取组件展示的属性字符串\n              this.richEditorStyledString = this.controller.getStyledString();\n              this.richEditorStyledString.appendStyledString(imageStyledString);\n              // 使插入图片后的属性字符串展示在组件上\n              this.controller.setStyledString(this.richEditorStyledString);\n              this.controller.setCaretOffset(this.richEditorStyledString.length);\n            }\n          })\n          Button("插入文本").onClick(() => {\n              // 获取组件展示的属性字符串\n              this.richEditorStyledString = this.controller.getStyledString();\n              this.richEditorStyledString.appendStyledString(this.styledString);\n              // 使插入文本后的属性字符串展示在组件上\n              this.controller.setStyledString(this.richEditorStyledString);\n              this.controller.setCaretOffset(this.richEditorStyledString.length);\n          })\n        }\n        Row() {\n          Button("获取选中内容").onClick(() => {\n            // 获取选中范围\n            let richEditorSelection = this.controller.getSelection();\n            let start = richEditorSelection.start ? richEditorSelection.start : 0;\n            let end = richEditorSelection.end ? richEditorSelection.end : 0;\n            // 获取组件展示的属性字符串\n            this.richEditorStyledString = this.controller.getStyledString();\n            this.selection = '[ ' + start + ' , ' + end + ' ]';\n            if (start == end) {\n              this.content = "";\n            } else {\n              this.content = this.richEditorStyledString.subStyledString(start, end - start).getString();\n            }\n          })\n          Button("更新选中样式").onClick(() => {\n            // 获取选中范围\n            let richEditorSelection = this.controller.getSelection();\n            let start = richEditorSelection.start ? richEditorSelection.start : 0;\n            let end = richEditorSelection.end ? richEditorSelection.end : 0;\n            // 获取组件展示的属性字符串\n            this.richEditorStyledString = this.controller.getStyledString();\n            this.richEditorStyledString.setStyle({\n              start: start,\n              length: end - start,\n              styledKey: StyledStringKey.FONT,\n              styledValue: this.textStyle\n            })\n            // 使变更样式后的属性字符串展示在组件上\n            this.controller.setStyledString(this.richEditorStyledString);\n          })\n          Button("删除选中内容").onClick(() => {\n            // 获取选中范围\n            let richEditorSelection = this.controller.getSelection();\n            let start = richEditorSelection.start ? richEditorSelection.start : 0;\n            let end = richEditorSelection.end ? richEditorSelection.end : 0;\n            // 获取组件展示的属性字符串\n            this.richEditorStyledString = this.controller.getStyledString();\n            this.richEditorStyledString.removeString(start, end - start);\n            // 使删除内容后的属性字符串展示在组件上\n            this.controller.setStyledString(this.richEditorStyledString);\n          })\n        }\n      }\n      .width("100%")\n    }\n  }\n}"""
            """LayoutManager使用示例\n\n// 导入必要的组件和库\n@Entry\n@Component\nexport struct Index {\n  // 定义状态变量\n  @State lineCount: string = ""\n  @State glyphPositionAtCoordinate: string = ""\n  @State lineMetrics: string = ""\n  controller: RichEditorController = new RichEditorController();\n  @State textStr: string =\n    'Hello World! 你好，世界！'\n\n  // 构建UI界面\n  build() {\n    Scroll() {\n      Column() {\n        // 显示文本说明RichEditor组件getLayoutManager接口获取相对于组件的布局信息\n        Text('RichEditor组件getLayoutManager接口获取相对于组件的布局信息')\n          .fontSize(9)\n          .fontColor(0xCCCCCC)\n          .width('90%')\n          .padding(10)\n\n        // 创建RichEditor组件并设置边框样式，监听onReady事件\n        RichEditor({ controller: this.controller })\n          .borderColor(Color.Red)\n          .borderWidth(1)\n          .onReady(() => {\n            this.controller.addTextSpan(this.textStr)\n          })\n          .onAreaChange(() => {\n            // 获取LayoutManager实例并更新显示的行数信息\n            let layoutManager = this.controller.getLayoutManager();\n            this.lineCount = "LineCount: " + layoutManager.getLineCount()\n          })\n\n        // 显示当前行数信息\n        Text('LineCount').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n        Text(this.lineCount)\n\n        // 显示GlyphPositionAtCoordinate相关信息\n        Text('GlyphPositionAtCoordinate').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n        Button("相对组件坐标[150,50]字形信息")\n          .onClick(() => {\n            // 获取指定坐标处的字形信息并更新显示\n            let layoutManager: LayoutManager = this.controller.getLayoutManager()\n            let position = layoutManager.getGlyphPositionAtCoordinate(150, 50)\n            this.glyphPositionAtCoordinate =\n            "相对组件坐标[150,50] glyphPositionAtCoordinate position: " + position.position + " affinity: " +\n            position.affinity\n          })\n          .margin({ bottom: 20, top: 10 })\n        Text(this.glyphPositionAtCoordinate)\n\n        // 显示LineMetrics相关信息\n        Text('LineMetrics').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n        Button("首行行信息、文本样式信息、以及字体属性信息")\n          .onClick(() => {\n            // 获取指定行的文本样式信息并更新显示\n            let layoutManager: LayoutManager = this.controller.getLayoutManager()\n            let lineMetrics = layoutManager.getLineMetrics(0)\n            this.lineMetrics = "lineMetrics is " + JSON.stringify(lineMetrics) + '\n\n'\n            let runMetrics = lineMetrics.runMetrics\n            runMetrics.forEach((value, key) => {\n              this.lineMetrics += "runMetrics key is " + key + " " + JSON.stringify(value) + "\n\n"\n            });\n          })\n          .margin({ bottom: 20, top: 10 })\n        Text(this.lineMetrics)\n      }\n      .margin({ top: 100, left: 8, right: 8 })\n    }\n  }\n}\n```\n@Entry\n@Component\nexport struct Index {\n  @State lineCount: string = ""\n  @State glyphPositionAtCoordinate: string = ""\n  @State lineMetrics: string = ""\n  controller: RichEditorController = new RichEditorController();\n  @State textStr: string =\n    'Hello World! 你好，世界！'\n\n  build() {\n    Scroll() {\n      Column() {\n        Text('RichEditor组件getLayoutManager接口获取相对于组件的布局信息')\n          .fontSize(9)\n          .fontColor(0xCCCCCC)\n          .width('90%')\n          .padding(10)\n        RichEditor({ controller: this.controller })\n          .borderColor(Color.Red)\n          .borderWidth(1)\n          .onReady(() => {\n            this.controller.addTextSpan(this.textStr)\n          })\n          .onAreaChange(() => {\n            let layoutManager = this.controller.getLayoutManager();\n            this.lineCount = "LineCount: " + layoutManager.getLineCount()\n          })\n\n        Text('LineCount').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n        Text(this.lineCount)\n\n        Text('GlyphPositionAtCoordinate').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n        Button("相对组件坐标[150,50]字形信息")\n          .onClick(() => {\n            let layoutManager: LayoutManager = this.controller.getLayoutManager()\n            let position = layoutManager.getGlyphPositionAtCoordinate(150, 50)\n            this.glyphPositionAtCoordinate =\n            "相对组件坐标[150,50] glyphPositionAtCoordinate position: " + position.position + " affinity: " +\n            position.affinity\n          })\n          .margin({ bottom: 20, top: 10 })\n        Text(this.glyphPositionAtCoordinate)\n\n        Text('LineMetrics').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n        Button("首行行信息、文本样式信息、以及字体属性信息")\n          .onClick(() => {\n            let layoutManager: LayoutManager = this.controller.getLayoutManager()\n            let lineMetrics = layoutManager.getLineMetrics(0)\n            this.lineMetrics = "lineMetrics is " + JSON.stringify(lineMetrics) + '\\n\\n'\n            let runMetrics = lineMetrics.runMetrics\n            runMetrics.forEach((value, key) => {\n              this.lineMetrics += "runMetrics key is " + key + " " + JSON.stringify(value) + "\\n\\n"\n            });\n          })\n          .margin({ bottom: 20, top: 10 })\n        Text(this.lineMetrics)\n      }\n      .margin({ top: 100, left: 8, right: 8 })\n    }\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "RichText": {
        "description": "富文本组件，解析并显示HTML格式文本。",
        "interfaces": [
            {
                "description": "RichText(content: string)",
                "params": {
                    "content": {
                        "type": "string",
                        "required": True,
                        "description": "表示HTML格式的字符串。"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {
            "onStart": {
                "description": "onStart(callback: () => void)\n加载网页时触发。",
                "params": {}
            },
            "onComplete": {
                "description": "onComplete(callback: () => void)\n网页加载结束时触发。",
                "params": {}
            }
        },
        "examples": [
            """// RichTextExample.ets\n\n/**\n * 定义一个展示富文本内容的组件示例，包含不同样式的文本内容和布局。\n */\n@Entry\n@Component\nstruct RichTextExample {\n  @State data: string = '<h1 style="text-align: center;">h1标题</h1>' +\n    '<h1 style="text-align: center;"><i>h1斜体</i></h1>' +\n    '<h1 style="text-align: center;"><u>h1下划线</u></h1>' +\n    '<h2 style="text-align: center;">h2标题</h2>' +\n    '<h3 style="text-align: center;">h3标题</h3>' +\n    '<p style="text-align: center;">p常规</p><hr/>' +\n    '<div style="width: 500px;height: 500px;border: 1px solid;margin: 0 auto;">' +\n    '<p style="font-size: 35px;text-align: center;font-weight: bold; color: rgb(24,78,228)">字体大小35px,行高45px</p>' +\n    '<p style="background-color: #e5e5e5;line-height: 45px;font-size: 35px;text-indent: 2em;">' +\n    '<p>这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字</p>';\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center,\n      justifyContent: FlexAlign.Center }) {\n      // 创建第一个 RichText 组件\n      RichText(this.data)\n        .onStart(() => {\n          console.info('RichText onStart');\n        })\n        .onComplete(() => {\n          console.info('RichText onComplete');\n        })\n        .width(500) // 设置宽度为500\n        .height(500) // 设置高度为500\n        .backgroundColor(0XBDDB69) // 设置背景颜色为浅绿色\n\n      // 创建第二个 RichText 组件\n      RichText('layoutWeight(1)')\n        .onStart(() => {\n          console.info('RichText onStart');\n        })\n        .onComplete(() => {\n          console.info('RichText onComplete');\n        })\n        .size({ width: '100%', height: 110 }) // 设置宽度为100%，高度为110\n        .backgroundColor(0X92D6CC) // 设置背景颜色为浅蓝色\n        .layoutWeight(1) // 设置布局权重为1\n\n      // 创建第三个 RichText 组件\n      RichText('layoutWeight(2)')\n        .onStart(() => {\n          console.info('RichText onStart');\n        })\n        .onComplete(() => {\n          console.info('RichText onComplete');\n        })\n        .size({ width: '100%', height: 110 }) // 设置宽度为100%，高度为110\n        .backgroundColor(0X92C48D) // 设置背景颜色为深绿色\n        .layoutWeight(2) // 设置布局权重为2\n    }\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct RichTextExample {\n  @State data: string = '<h1 style="text-align: center;">h1标题</h1>' +\n  '<h1 style="text-align: center;"><i>h1斜体</i></h1>' +\n  '<h1 style="text-align: center;"><u>h1下划线</u></h1>' +\n  '<h2 style="text-align: center;">h2标题</h2>' +\n  '<h3 style="text-align: center;">h3标题</h3>' +\n  '<p style="text-align: center;">p常规</p><hr/>' +\n  '<div style="width: 500px;height: 500px;border: 1px solid;margin: 0 auto;">' +\n  '<p style="font-size: 35px;text-align: center;font-weight: bold; color: rgb(24,78,228)">字体大小35px,行高45px</p>' +\n  '<p style="background-color: #e5e5e5;line-height: 45px;font-size: 35px;text-indent: 2em;">' +\n  '<p>这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字</p>';\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center,\n      justifyContent: FlexAlign.Center }) {\n      RichText(this.data)\n        .onStart(() => {\n          console.info('RichText onStart');\n        })\n        .onComplete(() => {\n          console.info('RichText onComplete');\n        })\n        .width(500)\n        .height(500)\n        .backgroundColor(0XBDDB69)\n      RichText('layoutWeight(1)')\n        .onStart(() => {\n          console.info('RichText onStart');\n        })\n        .onComplete(() => {\n          console.info('RichText onComplete');\n        })\n        .size({ width: '100%', height: 110 })\n        .backgroundColor(0X92D6CC)\n        .layoutWeight(1)\n      RichText('layoutWeight(2)')\n        .onStart(() => {\n          console.info('RichText onStart');\n        })\n        .onComplete(() => {\n          console.info('RichText onComplete');\n        })\n        .size({ width: '100%', height: 110 })\n        .backgroundColor(0X92C48D)\n        .layoutWeight(2)\n    }\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "ScrollBar": {
        "description": "滚动条组件ScrollBar，用于配合可滚动组件使用，如List、Grid、Scroll。",
        "interfaces": [
            {
                "description": "ScrollBar(value: ScrollBarOptions)",
                "params": {
                    "value": {
                        "type": "ScrollBarOptions",
                        "required": True,
                        "description": "滚动条组件参数。"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {},
        "examples": [
            """// ScrollBarExample.ets\n\n@Entry\n@Component\nstruct ScrollBarExample {\n  private scroller: Scroller = new Scroller() // 创建一个滚动器实例\n\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] // 创建一个包含数字的数组\n\n  build() {\n    Column() {\n      Stack({ alignContent: Alignment.End }) {\n        Scroll(this.scroller) {\n          Flex({ direction: FlexDirection.Column }) {\n            ForEach(this.arr, (item: number) => {\n              Row() {\n                Text(item.toString()) // 在每行显示数组中的数字\n                  .width('80%')\n                  .height(60)\n                  .backgroundColor('#3366CC')\n                  .borderRadius(15)\n                  .fontSize(16)\n                  .textAlign(TextAlign.Center)\n                  .margin({ top: 5 })\n              }\n            }, (item:number) => item.toString())\n          }.margin({ right: 15 }) // 设置 Flex 组件的右边距\n        }\n        .width('90%')\n        .scrollBar(BarState.Off) // 关闭滚动条\n        .scrollable(ScrollDirection.Vertical) // 设置垂直滚动\n\n        ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {\n          Text() // 滚动条的样式\n            .width(20)\n            .height(100)\n            .borderRadius(10)\n            .backgroundColor('#C0C0C0')\n        }.width(20).backgroundColor('#ededed') // 设置滚动条的宽度和背景颜色\n      }\n    }\n  }\n}\n```\n\n在这个示例代码中，主要功能块为展示带有子节点的滚动条样式。具体描述如下：\n\n1. 创建滚动器实例 `scroller` 和包含数字的数组 `arr`。\n2. 在 `build()` 方法中，构建了一个垂直滚动的 Column 布局。\n3. 使用 Stack 组件对子组件进行对齐，设置为底部对齐。\n4. 在 Scroll 组件中，展示 Flex 布局，根据数组中的数字动态生成行，每行显示一个数字。\n5. 设置每个数字显示的样式，包括宽度、高度、背景颜色、圆角、字体大小、文本对齐和上边距。\n6. 设置 Flex 布局的右边距为 15。\n7. 在 Scroll 组件中关闭滚动条，设置为垂直滚动。\n8. 创建垂直滚动条，样式为灰色背景，圆角矩形，宽度为 20。\n9. 设置滚动条组件的宽度和背景颜色。\n// xxx.ets\n@Entry\n@Component\nstruct ScrollBarExample {\n  private scroller: Scroller = new Scroller()\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]\n\n  build() {\n    Column() {\n      Stack({ alignContent: Alignment.End }) {\n        Scroll(this.scroller) {\n          Flex({ direction: FlexDirection.Column }) {\n            ForEach(this.arr, (item: number) => {\n              Row() {\n                Text(item.toString())\n                  .width('80%')\n                  .height(60)\n                  .backgroundColor('#3366CC')\n                  .borderRadius(15)\n                  .fontSize(16)\n                  .textAlign(TextAlign.Center)\n                  .margin({ top: 5 })\n              }\n            }, (item:number) => item.toString())\n          }.margin({ right: 15 })\n        }\n        .width('90%')\n        .scrollBar(BarState.Off)\n        .scrollable(ScrollDirection.Vertical)\n        ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical,state: BarState.Auto }) {\n          Text()\n            .width(20)\n            .height(100)\n            .borderRadius(10)\n            .backgroundColor('#C0C0C0')\n        }.width(20).backgroundColor('#ededed')\n      }\n    }\n  }\n}"""
            """@Entry\n@Component\nstruct ScrollBarExample {\n  private scroller: Scroller = new Scroller()\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]\n\n  build() {\n    Column() {\n      Stack({ alignContent: Alignment.End }) {\n        // 创建一个垂直滚动视图\n        Scroll(this.scroller) {\n          Flex({ direction: FlexDirection.Column }) {\n            // 遍历数组，为每个元素创建一个文本行\n            ForEach(this.arr, (item: number) => {\n              Row() {\n                Text(item.toString())\n                  .width('80%')\n                  .height(60)\n                  .backgroundColor('#3366CC')\n                  .borderRadius(15)\n                  .fontSize(16)\n                  .textAlign(TextAlign.Center)\n                  .margin({ top: 5 })\n              }\n            }, (item:number) => item.toString())\n          }.margin({ right: 15 })\n        }\n        // 设置滚动视图的属性\n        .width('90%')\n        .scrollBar(BarState.Off) // 关闭滚动条显示\n        .scrollable(ScrollDirection.Vertical) // 设置垂直滚动\n        // 添加垂直滚动条\n        ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto })\n      }\n    }\n  }\n}\n```\n\n在以上代码中，主要实现了一个包含滚动条的垂直滚动视图。具体功能与效果描述如下：\n\n1. 创建垂直滚动视图：通过`Scroll(this.scroller)`创建了一个垂直滚动视图，用于展示一列文本行。\n2. 遍历数组创建文本行：通过`ForEach`遍历数组`arr`，为每个元素创建一个文本行，显示相应的数字。\n3. 设置文本行样式：对每个文本行设置了宽度、高度、背景颜色、圆角、字体大小、文本对齐方式和外边距。\n4. 设置滚动视图属性：设置了滚动视图的宽度、关闭了滚动条显示、并设置了垂直滚动。\n5. 添加垂直滚动条：通过`ScrollBar`添加了一个垂直滚动条，与滚动视图关联，且滚动条状态为自动。\n@Entry\n@Component\nstruct ScrollBarExample {\n  private scroller: Scroller = new Scroller()\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]\n\n  build() {\n    Column() {\n      Stack({ alignContent: Alignment.End }) {\n        Scroll(this.scroller) {\n          Flex({ direction: FlexDirection.Column }) {\n            ForEach(this.arr, (item: number) => {\n              Row() {\n                Text(item.toString())\n                  .width('80%')\n                  .height(60)\n                  .backgroundColor('#3366CC')\n                  .borderRadius(15)\n                  .fontSize(16)\n                  .textAlign(TextAlign.Center)\n                  .margin({ top: 5 })\n              }\n            }, (item:number) => item.toString())\n          }.margin({ right: 15 })\n        }\n        .width('90%')\n        .scrollBar(BarState.Off)\n        .scrollable(ScrollDirection.Vertical)\n        ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical,state: BarState.Auto })\n      }\n    }\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Search": {
        "description": "搜索框组件，适用于浏览器的搜索内容输入框等应用场景。可以包含单个子组件。",
        "interfaces": [
            {
                "description": "创建搜索框组件。",
                "params": {
                    "options": {
                        "type": "object",
                        "required": False,
                        "description": "搜索框的配置选项。",
                        "properties": {
                            "value": {
                                "type": "string",
                                "required": False,
                                "description": "设置当前显示的搜索文本内容。"
                            },
                            "placeholder": {
                                "type": "ResourceStr",
                                "required": False,
                                "description": "设置无输入时的提示文本。"
                            },
                            "icon": {
                                "type": "string",
                                "required": False,
                                "description": "设置搜索图标路径，默认使用系统搜索图标。"
                            },
                            "controller": {
                                "type": "SearchController",
                                "required": False,
                                "description": "设置Search组件控制器。"
                            }
                        }
                    }
                }
            }
        ],
        "attributes": {
            "searchButton": {
                "description": "设置搜索框末尾搜索按钮。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "搜索框末尾搜索按钮文本内容。"
                    },
                    "option": {
                        "type": "SearchButtonOptions",
                        "required": False,
                        "description": "配置搜索框文本样式。"
                    }
                }
            },
            "placeholderColor": {
                "description": "设置placeholder文本颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "placeholder文本颜色。"
                    }
                }
            },
            "placeholderFont": {
                "description": "设置placeholder文本样式，包括字体大小，字体粗细，字体族，字体风格。目前仅支持默认字体族。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": False,
                        "description": "placeholder文本样式。"
                    }
                }
            },
            "textFont": {
                "description": "设置搜索框内输入文本样式，包括字体大小，字体粗细，字体族，字体风格。目前仅支持默认字体族。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": False,
                        "description": "搜索框内输入文本样式。"
                    }
                }
            },
            "textAlign": {
                "description": "设置文本在搜索框中的对齐方式。目前支持的对齐方式有：Start、Center、End。",
                "params": {
                    "value": {
                        "type": "TextAlign",
                        "required": True,
                        "description": "文本在搜索框中的对齐方式。"
                    }
                }
            },
            "copyOption": {
                "description": "设置输入的文本是否可复制。设置CopyOptions.None时，当前Search中的文字无法被复制或剪切，仅支持粘贴。",
                "params": {
                    "value": {
                        "type": "CopyOptions",
                        "required": True,
                        "description": "输入的文本是否可复制。"
                    }
                }
            },
            "searchIcon": {
                "description": "设置左侧搜索图标样式。",
                "params": {
                    "value": {
                        "type": "IconOptions",
                        "required": True,
                        "description": "左侧搜索图标样式。"
                    }
                }
            },
            "cancelButton": {
                "description": "设置右侧清除按钮样式。",
                "params": {
                    "value": {
                        "type": "object",
                        "required": True,
                        "description": "右侧清除按钮样式。",
                        "properties": {
                            "style": {
                                "type": "CancelButtonStyle",
                                "required": False,
                                "description": "右侧图标显示状态。"
                            },
                            "icon": {
                                "type": "IconOptions",
                                "required": False,
                                "description": "右侧图标。"
                            }
                        }
                    }
                }
            },
            "fontColor": {
                "description": "设置输入文本的字体颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "输入文本的字体颜色。"
                    }
                }
            },
            "caretStyle": {
                "description": "设置光标样式。",
                "params": {
                    "value": {
                        "type": "CaretStyle",
                        "required": True,
                        "description": "光标样式。"
                    }
                }
            },
            "enableKeyboardOnFocus": {
                "description": "设置Search通过点击以外的方式获焦时，是否绑定输入法。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "Search获焦时，是否绑定输入法。"
                    }
                }
            },
            "selectionMenuHidden": {
                "description": "设置长按输入框或者右键输入框时，是否弹出文本选择菜单。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "长按输入框或者右键输入框时，是否弹出文本选择菜单。"
                    }
                }
            },
            "customKeyboard": {
                "description": "设置自定义键盘。",
                "params": {
                    "value": {
                        "type": "CustomBuilder",
                        "required": True,
                        "description": "自定义键盘。"
                    },
                    "options": {
                        "type": "KeyboardOptions",
                        "required": False,
                        "description": "自定义键盘的配置选项。"
                    }
                }
            },
            "type": {
                "description": "设置输入框类型。",
                "params": {
                    "value": {
                        "type": "SearchType",
                        "required": True,
                        "description": "输入框类型。"
                    }
                }
            },
            "maxLength": {
                "description": "设置文本的最大输入字符数。默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "文本的最大输入字符数。"
                    }
                }
            },
            "enterKeyType": {
                "description": "设置输入法回车键类型。",
                "params": {
                    "value": {
                        "type": "EnterKeyType",
                        "required": True,
                        "description": "输入法回车键类型。"
                    }
                }
            },
            "lineHeight": {
                "description": "设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本的文本行高。"
                    }
                }
            },
            "decoration": {
                "description": "设置文本装饰线类型样式及其颜色。",
                "params": {
                    "value": {
                        "type": "TextDecorationOptions",
                        "required": True,
                        "description": "文本装饰线对象。"
                    }
                }
            },
            "letterSpacing": {
                "description": "设置文本字符间距。设置该值为百分比时，按默认值显示。设置该值为0时，按默认值显示。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本字符间距。"
                    }
                }
            },
            "selectedBackgroundColor": {
                "description": "设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "文本选中底板颜色。"
                    }
                }
            },
            "inputFilter": {
                "description": "通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。仅支持单个字符匹配，不支持字符串匹配。",
                "params": {
                    "value": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "正则表达式。"
                    },
                    "error": {
                        "type": "Callback<string>",
                        "required": False,
                        "description": "正则匹配失败时，返回被过滤的内容。"
                    }
                }
            },
            "textIndent": {
                "description": "设置首行文本缩进。",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "首行文本缩进。"
                    }
                }
            },
            "minFontSize": {
                "description": "设置文本最小显示字号。需配合maxFontSize以及布局大小限制使用，单独设置不生效。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本最小显示字号。"
                    }
                }
            },
            "maxFontSize": {
                "description": "设置文本最大显示字号。需配合minFontSize以及布局大小限制使用，单独设置不生效。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本最大显示字号。"
                    }
                }
            },
            "editMenuOptions": {
                "description": "设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。",
                "params": {
                    "editMenu": {
                        "type": "EditMenuOptions",
                        "required": True,
                        "description": "自定义菜单扩展项。"
                    }
                }
            },
            "enablePreviewText": {
                "description": "设置是否开启输入预上屏。",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启输入预上屏。"
                    }
                }
            }
        },
        "events": {
            "onSubmit": {
                "description": "点击搜索图标、搜索按钮或者按下软键盘搜索按钮时触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前搜索框中输入的文本内容。"
                    }
                }
            },
            "onChange": {
                "description": "输入内容发生变化时，触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前搜索框中输入的文本内容。"
                    }
                }
            },
            "onCopy": {
                "description": "长按搜索框弹出剪切板之后，点击剪切板的复制按钮触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "复制的文本内容。"
                    }
                }
            },
            "onCut": {
                "description": "长按搜索框弹出剪切板之后，点击剪切板的剪切按钮触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "剪切的文本内容。"
                    }
                }
            },
            "onPaste": {
                "description": "长按搜索框弹出剪切板之后，点击剪切板的粘贴按钮触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "粘贴的文本内容。"
                    },
                    "event": {
                        "type": "PasteEvent",
                        "required": False,
                        "description": "用户自定义的粘贴事件。"
                    }
                }
            },
            "onTextSelectionChange": {
                "description": "文本选择的位置发生变化时，触发该回调。",
                "params": {
                    "selectionStart": {
                        "type": "number",
                        "required": True,
                        "description": "文本选择区域起始位置，文本框中文字的起始位置为0。"
                    },
                    "selectionEnd": {
                        "type": "number",
                        "required": False,
                        "description": "文本选择区域结束位置。"
                    }
                }
            },
            "onContentScroll": {
                "description": "文本内容滚动时，触发该回调。",
                "params": {
                    "totalOffsetX": {
                        "type": "number",
                        "required": True,
                        "description": "文本在内容区的横坐标偏移，单位px。"
                    },
                    "totalOffsetY": {
                        "type": "number",
                        "required": False,
                        "description": "文本在内容区的纵坐标偏移，单位px。"
                    }
                }
            },
            "onEditChange": {
                "description": "输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。isEditing为true表示正在输入。",
                "params": {
                    "isEditing": {
                        "type": "Callback<boolean>",
                        "required": True,
                        "description": "为true表示正在输入。"
                    }
                }
            },
            "onWillInsert": {
                "description": "在将要输入时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<InsertValue, boolean>",
                        "required": True,
                        "description": "在将要输入时调用的回调。在返回true时，表示正常插入，返回false时，表示不插入。在预上屏操作时，该回调不触发。仅支持系统输入法输入的场景。"
                    }
                }
            },
            "onDidInsert": {
                "description": "在输入完成时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<InsertValue>",
                        "required": True,
                        "description": "在输入完成时调用的回调。仅支持系统输入法输入的场景。"
                    }
                }
            },
            "onWillDelete": {
                "description": "在将要删除时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<DeleteValue, boolean>",
                        "required": True,
                        "description": "在将要删除时调用的回调。在返回true时，表示正常删除，返回false时，表示不删除。在预上屏删除操作时，该回调不触发。仅支持系统输入法输入的场景。"
                    }
                }
            },
            "onDidDelete": {
                "description": "在删除完成时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<DeleteValue>",
                        "required": True,
                        "description": "在删除完成时调用的回调。仅支持系统输入法输入的场景。"
                    }
                }
            }
        },
        "examples": [
            "/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中创建一个搜索组件，并实现输入内容的变化监听和提交事件处理。同时，通过按钮控制光标位置和获取光标偏移信息。\n*/\n// SearchExample.ets\n@Entry\n@Component\nstruct SearchExample {\n  @State changeValue: string = '' // 存储搜索框的当前输入值\n  @State submitValue: string = '' // 存储搜索框提交的值\n  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 } // 存储光标位置信息\n  controller: SearchController = new SearchController() // 搜索框的控制器\n\n  build() {\n    Column({space: 10}) {\n      Text('onSubmit:' + this.submitValue).fontSize(18).margin(15) // 显示提交的搜索值\n      Text('onChange:' + this.changeValue).fontSize(18).margin(15) // 显示当前的搜索输入值\n      Search({ value: this.changeValue, placeholder: 'Type to search...', controller: this.controller })\n        .searchButton('SEARCH') // 设置搜索按钮的文本\n        .width('95%') // 设置搜索框的宽度\n        .height(40) // 设置搜索框的高度\n        .backgroundColor('#F5F5F5') // 设置搜索框的背景颜色\n        .placeholderColor(Color.Grey) // 设置占位符文本颜色\n        .placeholderFont({ size: 14, weight: 400 }) // 设置占位符文本字体样式\n        .textFont({ size: 14, weight: 400 }) // 设置输入文本字体样式\n        .onSubmit((value: string) => {\n          this.submitValue = value // 处理搜索框提交事件，更新提交值\n        })\n        .onChange((value: string) => {\n          this.changeValue = value // 处理搜索框输入变化事件，更新当前输入值\n        })\n        .margin(20) // 设置搜索框的外边距\n      Button('Set caretPosition 1')\n        .onClick(() => {\n          // 设置光标位置到输入的第一个字符后\n          this.controller.caretPosition(1)\n        })\n      Button('Get CaretOffset')\n        .onClick(() => {\n          this.positionInfo = this.controller.getCaretOffset() // 获取并更新光标位置信息\n        })\n    }.width('100%')\n  }\n}",
            "/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中创建一个带有搜索图标和取消按钮的搜索组件，并实现输入内容的变化监听和提交事件处理。搜索框的样式和行为通过各种属性进行定制。\n*/\n// SearchExample.ets\n@Entry\n@Component\nstruct SearchExample {\n  @State changeValue: string = '' // 存储搜索框的当前输入值\n  @State submitValue: string = '' // 存储搜索框提交的值\n\n  build() {\n    Column() {\n      Text('onSubmit:' + this.submitValue).fontSize(18).margin(15) // 显示提交的搜索值\n      Search({ value: this.changeValue, placeholder: 'Type to search...' })\n        .searchButton('SEARCH') // 设置搜索按钮的文本\n        .searchIcon({\n          src: $r('app.media.search') // 设置搜索图标的资源路径\n        })\n        .cancelButton({\n          style: CancelButtonStyle.CONSTANT, // 设置取消按钮的样式为常驻显示\n          icon: {\n            src: $r('app.media.cancel') // 设置取消按钮图标的资源路径\n          }\n        })\n        .width('90%') // 设置搜索框的宽度\n        .height(40) // 设置搜索框的高度\n        .maxLength(20) // 设置输入字符的最大长度\n        .backgroundColor('#F5F5F5') // 设置搜索框的背景颜色\n        .placeholderColor(Color.Grey) // 设置占位符文本颜色\n        .placeholderFont({ size: 14, weight: 400 }) // 设置占位符文本字体样式\n        .textFont({ size: 14, weight: 400 }) // 设置输入文本字体样式\n        .onSubmit((value: string) => {\n          this.submitValue = value // 处理搜索框提交事件，更新提交值\n        })\n        .onChange((value: string) => {\n          this.changeValue = value // 处理搜索框输入变化事件，更新当前输入值\n        })\n        .margin(20) // 设置搜索框的外边距\n    }.width('100%')\n  }\n}"
        ]
    },
    "Select": {
        "description": "提供下拉选择菜单，可以让用户在多个选项之间选择。可以包含单个子组件。",
        "interfaces": [
            {
                "description": "创建Select组件。",
                "params": {
                    "options": {
                        "type": "Array<SelectOption>",
                        "required": True,
                        "description": "下拉菜单的选项数组。"
                    }
                }
            }
        ],
        "attributes": {
            "selected": {
                "description": "设置下拉菜单初始选项的索引，第一项的索引为0。",
                "params": {
                    "value": {
                        "type": ["number", "Resource"],
                        "required": True,
                        "description": "下拉菜单初始选项的索引。",
                        "default": -1
                    }
                }
            },
            "value": {
                "description": "设置下拉按钮本身的文本内容。当菜单选中时默认会替换为菜单项文本内容。",
                "params": {
                    "value": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "下拉按钮本身的文本内容。"
                    }
                }
            },
            "controlSize": {
                "description": "设置Select组件的尺寸。",
                "params": {
                    "value": {
                        "type": "ControlSize",
                        "required": True,
                        "description": "Select组件的尺寸。",
                        "default": "ControlSize.NORMAL"
                    }
                }
            },
            "menuItemContentModifier": {
                "description": "定制Select下拉菜单项内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<MenuItemConfiguration>",
                        "required": True,
                        "description": "用于定制菜单项内容的修饰符。"
                    }
                }
            },
            "divider": {
                "description": "设置分割线样式。",
                "params": {
                    "options": {
                        "type": ["Optional<DividerOptions>", "null"],
                        "required": True,
                        "description": "分割线的样式选项。",
                        "default": {
                            "strokeWidth": "1px",
                            "color": "#33182431"
                        }
                    }
                }
            },
            "font": {
                "description": "设置下拉按钮本身的文本样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "下拉按钮本身的文本样式。",
                        "default": {
                            "size": "16fp",
                            "weight": "FontWeight.Medium"
                        }
                    }
                }
            },
            "fontColor": {
                "description": "设置下拉按钮本身的文本颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "下拉按钮本身的文本颜色。"
                    }
                }
            },
            "selectedOptionBgColor": {
                "description": "设置下拉菜单选中项的背景色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "下拉菜单选中项的背景色。"
                    }
                }
            },
            "selectedOptionFont": {
                "description": "设置下拉菜单选中项的文本样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "下拉菜单选中项的文本样式。",
                        "default": {
                            "size": "16fp",
                            "weight": "FontWeight.Regular"
                        }
                    }
                }
            },
            "selectedOptionFontColor": {
                "description": "设置下拉菜单选中项的文本颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "下拉菜单选中项的文本颜色。"
                    }
                }
            },
            "optionBgColor": {
                "description": "设置下拉菜单项的背景色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "下拉菜单项的背景色。"
                    }
                }
            },
            "optionFont": {
                "description": "设置下拉菜单项的文本样式。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "下拉菜单项的文本样式。",
                        "default": {
                            "size": "16fp",
                            "weight": "FontWeight.Regular"
                        }
                    }
                }
            },
            "optionFontColor": {
                "description": "设置下拉菜单项的文本颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "下拉菜单项的文本颜色。"
                    }
                }
            },
            "space": {
                "description": "设置下拉菜单项的文本与箭头之间的间距。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "下拉菜单项的文本与箭头之间的间距。",
                        "default": 8
                    }
                }
            },
            "arrowPosition": {
                "description": "设置下拉菜单项的文本与箭头之间的对齐方式。",
                "params": {
                    "value": {
                        "type": "ArrowPosition",
                        "required": True,
                        "description": "下拉菜单项的文本与箭头之间的对齐方式。",
                        "default": "ArrowPosition.END"
                    }
                }
            },
            "menuAlign": {
                "description": "设置下拉按钮与下拉菜单间的对齐方式。",
                "params": {
                    "alignType": {
                        "type": "MenuAlignType",
                        "required": True,
                        "description": "对齐方式类型。",
                        "default": "MenuAlignType.START"
                    },
                    "offset": {
                        "type": "Offset",
                        "required": False,
                        "description": "按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。",
                        "default": {"dx": 0, "dy": 0}
                    }
                }
            },
            "optionWidth": {
                "description": "设置下拉菜单项的宽度，不支持设置百分比。",
                "params": {
                    "value": {
                        "type": ["Dimension", "OptionWidthMode"],
                        "required": True,
                        "description": "下拉菜单项的宽度。"
                    }
                }
            },
            "optionHeight": {
                "description": "设置下拉菜单显示的最大高度，不支持设置百分比。",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "下拉菜单显示的最大高度。"
                    }
                }
            },
            "menuBackgroundColor": {
                "description": "设置下拉菜单的背景色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "下拉菜单的背景色。",
                        "default": "Color.Transparent"
                    }
                }
            },
            "menuBackgroundBlurStyle": {
                "description": "设置下拉菜单的背景模糊材质。",
                "params": {
                    "value": {
                        "type": "BlurStyle",
                        "required": True,
                        "description": "下拉菜单的背景模糊材质。",
                        "default": "BlurStyle.COMPONENT_ULTRA_THICK"
                    }
                }
            }
        },
        "events": {
            "onSelect": {
                "description": "下拉菜单选中某一项的回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "选中项的索引。"
                    },
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "选中项的值。"
                    }
                }
            }
        },
        "examples": [
            """示例1:/**\n * 该代码定义了一个名为 SelectExample 的组件结构体，用于创建一个自定义样式的下拉选择框。\n * 组件包含了多个状态变量，如文本内容、索引、间距和箭头位置等。\n * 通过 build 方法构建了一个包含多个选项的下拉选择框，并设置了各种样式属性和事件监听。\n * 当选择框的选项发生变化时，会触发 onSelect 事件，更新选中的索引和文本内容。\n * 通过设置不同的属性，可以自定义下拉选择框的外观和行为。\n */\n// xxx.ets\n@Entry\n@Component\nstruct SelectExample {\n  @State text: string = "TTTTT"\n  @State index: number = 2\n  @State space: number = 8\n  @State arrowPosition: ArrowPosition = ArrowPosition.END\n  build() {\n    Column() {\n      Select([{ value: 'aaa', icon: $r("app.media.selecticon") },\n        { value: 'bbb', icon: $r("app.media.selecticon") },\n        { value: 'ccc', icon: $r("app.media.selecticon") },\n        { value: 'ddd', icon: $r("app.media.selecticon") }])\n        .selected(this.index)\n        .value(this.text)\n        .font({ size: 16, weight: 500 })\n        .fontColor('#182431')\n        .selectedOptionFont({ size: 16, weight: 400 })\n        .optionFont({ size: 16, weight: 400 })\n        .space(this.space)\n        .arrowPosition(this.arrowPosition)\n        .menuAlign(MenuAlignType.START, {dx:0, dy:0})\n        .optionWidth(200)\n        .optionHeight(300)\n        .onSelect((index:number, text?: string | undefined)=>{\n          console.info('Select:' + index)\n          this.index = index;\n          if(text){\n            this.text = text;\n          }\n        })\n    }.width('100%')\n  }\n}"""
            """示例2:/**\n * 该代码实现了一个自定义的菜单项内容修改器，用于定制菜单项的展示样式和行为。\n * MyMenuItemContentModifier 类用于设置菜单项的文本内容，并提供了应用内容修改器的方法。\n * MenuItemBuilder 函数定义了菜单项的展示结构，包括文本、图标、自定义修改器文本和路径等元素，并设置了点击事件处理逻辑。\n * SelectExample 结构体展示了如何使用自定义的菜单项内容修改器，通过 Select 组件展示菜单项列表，并应用 MyMenuItemContentModifier 修改器。\n * MyMenuItemContentModifier 类和 MenuItemBuilder 函数共同实现了菜单项的展示和交互逻辑，为菜单项提供了个性化定制的功能。\n */\n**/\nimport { MenuItemModifier } from '@kit.ArkUI'\n\nclass MyMenuItemContentModifier implements ContentModifier<MenuItemConfiguration> {\n  modifierText: string = ""\n  constructor(text: string) {\n    this.modifierText = text;\n  }\n  applyContent(): WrappedBuilder<[MenuItemConfiguration]> {\n    return wrapBuilder(MenuItemBuilder)\n  }\n}\n\n@Builder\nfunction MenuItemBuilder(configuration: MenuItemConfiguration) {\n  Row() {\n    Text(configuration.value)\n    Blank()\n    Image(configuration.icon).size({ width: 40, height: 40 })\n    Blank(30)\n    Text((configuration.contentModifier as MyMenuItemContentModifier).modifierText)\n    Path()\n      .width('100px')\n      .height('150px')\n      .commands('M40 0 L80 100 L0 100 Z')\n      .fillOpacity(0)\n      .stroke(Color.Black)\n      .strokeWidth(3)\n  }\n  .onClick(() => {\n    configuration.triggerSelect(configuration.index, configuration.value.valueOf().toString())\n  })\n}\n\n@Entry\n@Component\nstruct SelectExample {\n  @State text: string = "有modifier"\n  build() {\n    Column() {\n      Row() {\n        Select([{ value: 'item1', icon: $r("app.media.icon") },\n          { value: 'item2', icon: $r("app.media.icon") }])\n          .value(this.text)\n          .onSelect((index:number, text?: string)=>{\n            console.info('Select index:' + index)\n            console.info('Select text:' + text)\n          })\n          .menuItemContentModifier(new MyMenuItemContentModifier("我来自Modifier"))\n\n      }.alignItems(VerticalAlign.Center).height("50%")\n    }\n  }\n}"""
            """示例3:/**\n * 该代码实现了一个选择组件示例，包括自定义的符号图标和样式。选择组件显示了几个选项，每个选项包含一个符号图标和对应的数值。\n * 用户可以通过点击选项来选择不同的数值，并相应地更新显示的文本内容。用户还可以设置选项之间的间距、箭头位置等样式属性。\n * 当用户选择不同的选项时，会触发 onSelect 事件，记录选择的索引和文本内容，并更新组件的状态。\n * 通过定义不同的 SymbolGlyphModifier 对象和设置不同的符号图标和颜色，实现了每个选项的个性化显示效果。\n * 通过构建 Column 和调用 Select 方法来创建选择组件，设置各种样式属性，并处理用户的选择事件。\n */\n        \n/**\n * 该例子展示了一个自定义样式的按钮组件，按钮显示为“OK”，并包含一个开关控件用于启用或禁用按钮。\n * 点击按钮会记录点击位置的坐标，并在按钮上显示这些坐标。按钮的按压状态和启用状态也会在按钮上显示。\n * 通过 MyButtonStyle 类和 buildButton1 函数进行自定义按钮的样式和行为。\n * 当按钮被按压时，圆圈会变成红色，标题会显示按压字样；未按压时，圆圈会变成黑色，标题会显示非按压字样。\n * MyButtonStyle 类用于定义按钮的样式属性，buildButton1 函数用于构建按钮的内容。\n * 通过设置按钮的启用状态、点击位置坐标等属性，并根据按压状态设置圆圈的颜色和透明度，实现了按钮的个性化显示效果。\n */\n // xxx.ets\nimport { SymbolGlyphModifier } from '@kit.ArkUI'\n\n@Entry\n@Component\nstruct SelectExample {\n  @State text: string = "TTTTT"\n  @State index: number = 2\n  @State space: number = 8\n  @State arrowPosition: ArrowPosition = ArrowPosition.END\n  @State symbolModifier1: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontColor([Color.Green]);\n  @State symbolModifier2: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]);\n  @State symbolModifier3: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontColor([Color.Gray]);\n  @State symbolModifier4: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor([Color.Gray]);\n  build() {\n    Column() {\n      Select([{ value: 'aaa', symbolIcon: this.symbolModifier1 },\n        { value: 'bbb', symbolIcon: this.symbolModifier2 },\n        { value: 'ccc', symbolIcon: this.symbolModifier3 },\n        { value: 'ddd', symbolIcon: this.symbolModifier4 }])\n        .selected(this.index)\n        .value(this.text)\n        .font({ size: 16, weight: 500 })\n        .fontColor('#182431')\n        .selectedOptionFont({ size: 16, weight: 400 })\n        .optionFont({ size: 16, weight: 400 })\n        .space(this.space)\n        .arrowPosition(this.arrowPosition)\n        .menuAlign(MenuAlignType.START, {dx:0, dy:0})\n        .onSelect((index:number, text?: string | undefined)=>{\n          console.info('Select:' + index)\n          this.index = index;\n          if(text){\n            this.text = text;\n          }\n        })\n    }.width('100%')\n  }\n}"""
            """示例4:# 功能注释：\n# 该代码实现了一个选择示例组件，包含一个自定义的菜单项内容修饰器和一个按钮构建器，用于创建带有图标和文本的菜单项。\n# MyMenuItemContentModifier类用于定义菜单项内容的修饰器，包括文本内容和应用内容的方法。\n# MenuItemBuilder函数用于构建菜单项，根据配置信息显示文本、图标或符号图标，并设置点击事件处理逻辑。\n# SelectExample结构体作为入口组件，展示了一个选择示例，包含一个选择框和自定义菜单项内容修饰器。\n# 选择框的值可以通过点击选择项进行更改，同时会触发相应的选择事件并显示选择的索引和文本。\nimport { MenuItemModifier, SymbolGlyphModifier } from '@kit.ArkUI'\n\nclass MyMenuItemContentModifier implements ContentModifier<MenuItemConfiguration> {\n  modifierText: string = ""\n  constructor(text: string) {\n    this.modifierText = text;\n  }\n  applyContent(): WrappedBuilder<[MenuItemConfiguration]> {\n    return wrapBuilder(MenuItemBuilder)\n  }\n}\n\n@Builder\nfunction MenuItemBuilder(configuration: MenuItemConfiguration) {\n  Row() {\n    Text(configuration.value)\n    Blank()\n    if (configuration.symbolIcon) {\n      SymbolGlyph().attributeModifier(configuration.symbolIcon).fontSize(24)\n    } else if (configuration.icon) {\n      Image(configuration.icon).size({ width: 24, height: 24 })\n    }\n    Blank(30)\n    Text((configuration.contentModifier as MyMenuItemContentModifier).modifierText)\n    Blank(30)\n    Path()\n      .width('100px')\n      .height('150px')\n      .commands('M40 0 L80 100 L0 100 Z')\n      .fillOpacity(0)\n      .stroke(Color.Black)\n      .strokeWidth(3)\n  }\n  .onClick(() => {\n    configuration.triggerSelect(configuration.index, configuration.value.valueOf().toString())\n  })\n}\n\n@Entry\n@Component\nstruct SelectExample {\n  @State text: string = "Content Modifier Select"\n  @State symbolModifier1: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontColor([Color.Gray]);\n  @State symbolModifier2: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor([Color.Gray]);\n  build() {\n    Column() {\n      Row() {\n        Select([{ value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier1 },\n          { value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier2 }])\n          .value(this.text)\n          .onSelect((index:number, text?: string)=>{\n            console.info('Select index:' + index)\n            console.info('Select text:' + text)\n          })\n          .menuItemContentModifier(new MyMenuItemContentModifier("Content Modifier"))\n\n      }.alignItems(VerticalAlign.Center).height('50%')\n    }\n  }\n}"""
            """示例5:/**\n * 该代码实现了一个自定义的下拉选择组件，包含了选择项、图标、字体样式等属性的设置。\n * 通过构建 SelectExample 结构体，可以生成一个下拉选择框，其中包含了多个选项和相应的操作逻辑。\n * 通过设置不同的属性，可以自定义下拉选择框的外观和行为，如选择项、字体样式、箭头位置等。\n * 当用户选择某一项时，会触发 onSelect 事件，记录选择的索引和文本，并更新相应的状态。\n * 通过该组件可以实现灵活的下拉选择功能，并根据需要进行定制化的样式和行为设置。\n */\n// xxx.ets\n@Entry\n@Component\nstruct SelectExample {\n  @State text: string = "TTTTT"\n  @State index: number = -1\n  @State arrowPosition: ArrowPosition = ArrowPosition.END\n  build() {\n    Column() {\n      Select([{ value: 'aaa', icon: $r("app.media.icon") },\n        { value: 'bbb', icon: $r("app.media.icon") },\n        { value: 'ccc', icon: $r("app.media.icon") },\n        { value: 'ddd', icon: $r("app.media.icon") }])\n        .selected(this.index)\n        .value(this.text)\n        .font({ size: 16, weight: 500 })\n        .fontColor('#182431')\n        .selectedOptionFont({ size: 16, weight: 400 })\n        .optionFont({ size: 16, weight: 400 })\n        .arrowPosition(this.arrowPosition)\n        .menuAlign(MenuAlignType.START, {dx:0, dy:0})\n        .optionWidth(200)\n        .optionHeight(300)\n        .divider( { strokeWidth: 5, color: Color.Blue, startMargin: 10, endMargin: 10 })\n        .onSelect((index:number, text?: string | undefined)=>{\n          console.info('Select:' + index)\n          this.index = index;\n          if(text){\n            this.text = text;\n          }\n        })\n    }.width('100%')\n  }\n}"""
            """示例6:// SelectExample结构体定义了一个选择组件，包含文本、索引和箭头位置等状态信息，通过build方法构建选择组件的UI。\n// 选择组件展示了一个下拉菜单，用户可以从预定义的选项中选择一个值，同时可以设置字体样式、颜色、选中项字体样式等属性。\n// 用户选择某一项后，会触发onSelect事件，更新选择的索引和文本内容。\n// 通过设置menuAlign、optionWidth、optionHeight等属性，可以对下拉菜单的展示进行定制。\n// 该组件的宽度设置为100%。\n// xxx.ets\n@Entry\n@Component\nstruct SelectExample {\n  @State text: string = "TTTTT"\n  @State index: number = -1\n  @State arrowPosition: ArrowPosition = ArrowPosition.END\n  build() {\n    Column() {\n      Select([{ value: 'aaa', icon: $r("app.media.icon") },\n        { value: 'bbb', icon: $r("app.media.icon") },\n        { value: 'ccc', icon: $r("app.media.icon") },\n        { value: 'ddd', icon: $r("app.media.icon") }])\n        .selected(this.index)\n        .value(this.text)\n        .font({ size: 16, weight: 500 })\n        .fontColor('#182431')\n        .selectedOptionFont({ size: 16, weight: 400 })\n        .optionFont({ size: 16, weight: 400 })\n        .arrowPosition(this.arrowPosition)\n        .menuAlign(MenuAlignType.START, {dx:0, dy:0})\n        .optionWidth(200)\n        .optionHeight(300)\n        .divider( null )\n        .onSelect((index:number, text?: string | undefined)=>{\n          console.info('Select:' + index)\n          this.index = index;\n          if(text){\n            this.text = text;\n          }\n        })\n    }.width('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Slider": {
        "description": "滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。",
        "interfaces": [
            {
                "description": "创建一个滑动条组件。",
                "params": {
                    "options": {
                        "type": "SliderOptions",
                        "required": False,
                        "description": "滑动条的选项。"
                    }
                }
            }
        ],
        "attributes": {
            "blockColor": {
                "description": "设置滑块的颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "滑块的颜色。"
                    }
                }
            },
            "trackColor": {
                "description": "设置滑轨的背景颜色。",
                "params": {
                    "value": {
                        "type": ["ResourceColor", "LinearGradient"],
                        "required": True,
                        "description": "滑轨的背景颜色。"
                    }
                }
            },
            "selectedColor": {
                "description": "设置滑轨的已滑动部分颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "滑轨的已滑动部分颜色。"
                    }
                }
            },
            "showSteps": {
                "description": "设置当前是否显示步长刻度值。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "当前是否显示步长刻度值。",
                        "default": "false"
                    }
                }
            },
            "showTips": {
                "description": "设置滑动时是否显示气泡提示。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "滑动时是否显示气泡提示。",
                        "default": "false"
                    },
                    "content": {
                        "type": "ResourceStr",
                        "required": False,
                        "description": "气泡提示的文本内容，默认显示当前百分比。"
                    }
                }
            },
            "trackThickness": {
                "description": "设置滑轨的粗细。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "滑轨的粗细。"
                    }
                }
            },
            "blockBorderColor": {
                "description": "设置滑块描边颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "滑块描边颜色。"
                    }
                }
            },
            "blockBorderWidth": {
                "description": "设置滑块描边粗细。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "滑块描边粗细。"
                    }
                }
            },
            "stepColor": {
                "description": "设置刻度颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "刻度颜色。"
                    }
                }
            },
            "trackBorderRadius": {
                "description": "设置底板圆角半径。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "底板圆角半径。",
                        "default": "2vp"
                    }
                }
            },
            "selectedBorderRadius": {
                "description": "设置已滑动部分（高亮）圆角半径。",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "已选择部分圆角半径。"
                    }
                }
            },
            "blockSize": {
                "description": "设置滑块大小。",
                "params": {
                    "value": {
                        "type": "SizeOptions",
                        "required": True,
                        "description": "滑块大小。"
                    }
                }
            },
            "blockStyle": {
                "description": "设置滑块形状参数。",
                "params": {
                    "value": {
                        "type": "SliderBlockStyle",
                        "required": True,
                        "description": "滑块形状参数。"
                    }
                }
            },
            "stepSize": {
                "description": "设置刻度大小（直径）。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "刻度大小（直径）。",
                        "default": "4vp"
                    }
                }
            },
            "minLabel": {
                "description": "设置最小值。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "最小值。"
                    }
                }
            },
            "maxLabel": {
                "description": "设置最大值。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "最大值。"
                    }
                }
            },
            "sliderInteractionMode": {
                "description": "设置用户与滑动条组件交互方式。",
                "params": {
                    "value": {
                        "type": "SliderInteraction",
                        "required": True,
                        "description": "用户与滑动条组件交互方式。",
                        "default": "SliderInteraction.SLIDE_AND_CLICK"
                    }
                }
            },
            "minResponsiveDistance": {
                "description": "设置滑动响应的最小距离。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "设置滑动响应的最小距离。",
                        "default": 0
                    }
                }
            },
            "contentModifier": {
                "description": "定制Slider内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<SliderConfiguration>",
                        "required": True,
                        "description": "定制Slider内容区的方法。"
                    }
                }
            },
            "slideRange": {
                "description": "设置有效滑动区间。",
                "params": {
                    "value": {
                        "type": "SlideRange",
                        "required": True,
                        "description": "设置有效滑动区间。"
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "Slider拖动或点击时触发事件回调。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "当前滑动进度值。"
                    },
                    "mode": {
                        "type": "SliderChangeMode",
                        "required": True,
                        "description": "事件触发的相关状态值。"
                    }
                }
            }
        },
        "examples": [
            "// xxx.ets\n/*\n实现思路：\n本示例展示了不同样式的滑动条（Slider）组件的使用，包括水平和垂直方向的OutSet、InSet和None样式。每个滑动条都有不同的配置，如最小值、最大值、步长、颜色等，并且可以显示提示和步长标记。通过滑动条的onChange事件，可以实时获取滑动条的值和变化模式，并更新状态变量。\n\n总体功能与效果描述：\n1. 展示了三种不同样式的水平滑动条：OutSet、InSet和None。\n2. 每个滑动条都可以显示提示和步长标记，并且可以通过滑动改变其值。\n3. 展示了两种不同样式的垂直滑动条：OutSet和InSet，支持垂直方向的滑动。\n4. 通过滑动条的onChange事件，实时更新滑动条的值，并在控制台输出当前值和变化模式。\n*/\n\n@Entry\n@Component\nstruct SliderExample {\n  @State outSetValueOne: number = 40 // 初始化OutSet样式滑动条的值\n  @State inSetValueOne: number = 40 // 初始化InSet样式滑动条的值\n  @State noneValueOne: number = 40 // 初始化None样式滑动条的值\n  @State outSetValueTwo: number = 40 // 初始化OutSet样式滑动条的值，带有步长\n  @State inSetValueTwo: number = 40 // 初始化InSet样式滑动条的值，带有步长\n  @State vOutSetValueOne: number = 40 // 初始化垂直OutSet样式滑动条的值\n  @State vInSetValueOne: number = 40 // 初始化垂直InSet样式滑动条的值\n  @State vOutSetValueTwo: number = 40 // 初始化垂直OutSet样式滑动条的值，带有步长\n  @State vInSetValueTwo: number = 40 // 初始化垂直InSet样式滑动条的值，带有步长\n\n  build() {\n    Column({ space: 8 }) {\n      Text('outset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)\n      Row() {\n        Slider({\n          value: this.outSetValueOne,\n          min: 0,\n          max: 100,\n          style: SliderStyle.OutSet\n        })\n          .showTips(true) // 显示滑动条的值提示\n          .onChange((value: number, mode: SliderChangeMode) => {\n            this.outSetValueOne = value\n            console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n          })\n        Text(this.outSetValueOne.toFixed(0)).fontSize(12) // 显示滑动条的当前值\n      }\n      .width('80%')\n      Row() {\n        Slider({\n          value: this.outSetValueTwo,\n          step: 10,\n          style: SliderStyle.OutSet\n        })\n          .showSteps(true) // 显示滑动条的步长标记\n          .onChange((value: number, mode: SliderChangeMode) => {\n            this.outSetValueTwo = value\n            console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n          })\n        Text(this.outSetValueTwo.toFixed(0)).fontSize(12) // 显示滑动条的当前值\n      }\n      .width('80%')\n\n      Text('inset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)\n      Row() {\n        Slider({\n          value: this.inSetValueOne,\n          min: 0,\n          max: 100,\n          style: SliderStyle.InSet\n        })\n          .blockColor('#191970') // 设置滑动块的颜色\n          .trackColor('#ADD8E6') // 设置未选中轨道颜色\n          .selectedColor('#4169E1') // 设置选中轨道颜色\n          .showTips(true) // 显示滑动条的值提示\n          .onChange((value: number, mode: SliderChangeMode) => {\n            this.inSetValueOne = value\n            console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n          })\n        Text(this.inSetValueOne.toFixed(0)).fontSize(12) // 显示滑动条的当前值\n      }\n      .width('80%')\n      Row() {\n        Slider({\n          value: this.inSetValueTwo,\n          step: 10,\n          style: SliderStyle.InSet\n        })\n          .blockColor('#191970') // 设置滑动块的颜色\n          .trackColor('#ADD8E6') // 设置未选中轨道颜色\n          .selectedColor('#4169E1') // 设置选中轨道颜色\n          .showSteps(true) // 显示滑动条的步长标记\n          .onChange((value: number, mode: SliderChangeMode) => {\n            this.inSetValueTwo = value\n            console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n          })\n        Text(this.inSetValueTwo.toFixed(0)).fontSize(12) // 显示滑动条的当前值\n      }\n      .width('80%')\n\n      Text('none slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)\n      Row() {\n        Slider({\n          value: this.noneValueOne,\n          min: 0,\n          max: 100,\n          style: SliderStyle.NONE\n        })\n          .blockColor('#191970') // 设置滑动块的颜色\n          .trackColor('#ADD8E6') // 设置未选中轨道颜色\n          .selectedColor('#4169E1') // 设置选中轨道颜色\n          .showTips(true) // 显示滑动条的值提示\n          .onChange((value: number, mode: SliderChangeMode) => {\n            this.noneValueOne = value\n            console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n          })\n        Text(this.noneValueOne.toFixed(0)).fontSize(12) // 显示滑动条的当前值\n      }\n      .width('80%')\n\n      Row() {\n        Column() {\n          Text('vertical outset slider').fontSize(9).fontColor(0xCCCCCC).width('50%').margin(15)\n          Row() {\n            Text().width('10%')\n            Slider({\n              value: this.vOutSetValueOne,\n              style: SliderStyle.OutSet,\n              direction: Axis.Vertical\n            })\n              .blockColor('#191970') // 设置滑动块的颜色\n              .trackColor('#ADD8E6') // 设置未选中轨道颜色\n              .selectedColor('#4169E1') // 设置选中轨道颜色\n              .showTips(true) // 显示滑动条的值提示\n              .onChange((value: number, mode: SliderChangeMode) => {\n                this.vOutSetValueOne = value\n                console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n              })\n            Slider({\n              value: this.vOutSetValueTwo,\n              step: 10,\n              style: SliderStyle.OutSet,\n              direction: Axis.Vertical\n            })\n              .blockColor('#191970') // 设置滑动块的颜色\n              .trackColor('#ADD8E6') // 设置未选中轨道颜色\n              .selectedColor('#4169E1') // 设置选中轨道颜色\n              .showSteps(true) // 显示滑动条的步长标记\n              .onChange((value: number, mode: SliderChangeMode) => {\n                this.vOutSetValueTwo = value\n                console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n              })\n          }\n        }.width('50%').height(300)\n\n        Column() {\n          Text('vertical inset slider').fontSize(9).fontColor(0xCCCCCC).width('50%').margin(15)\n          Row() {\n            Slider({\n              value: this.vInSetValueOne,\n              style: SliderStyle.InSet,\n              direction: Axis.Vertical,\n              reverse: true // 竖向的Slider默认是上端是min值，下端是max值，因此想要从下往上滑动，需要设置reverse为true\n            })\n              .showTips(true) // 显示滑动条的值提示\n              .onChange((value: number, mode: SliderChangeMode) => {\n                this.vInSetValueOne = value\n                console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n              })\n            Slider({\n              value: this.vInSetValueTwo,\n              step: 10,\n              style: SliderStyle.InSet,\n              direction: Axis.Vertical,\n              reverse: true\n            })\n              .showSteps(true) // 显示滑动条的步长标记\n              .onChange((value: number, mode: SliderChangeMode) => {\n                this.vInSetValueTwo = value\n                console.info('value:' + value + 'mode:' + mode.toString()) // 输出当前值和变化模式\n              })\n          }\n        }.width('50%').height(300)\n      }\n    }.width('100%')\n  }\n}",
            "// xxx.ets\n/*\n实现思路：\n本示例展示了滑动条（Slider）组件的各种自定义样式和功能，包括滑动块（block）、步长（step）、轨道（track）、选中区域（selected）、滑动块样式（blockStyle）和提示（tips）的自定义设置。通过这些设置，可以创建具有不同视觉效果和交互行为的滑动条。\n\n总体功能与效果描述：\n1. 展示了如何自定义滑动块的大小、边框颜色和宽度。\n2. 展示了如何设置滑动条的步长、步长标记的大小和颜色。\n3. 展示了如何自定义轨道的边框圆角。\n4. 展示了如何自定义选中区域的边框圆角。\n5. 展示了如何设置滑动块的样式，包括默认样式、图片样式和自定义形状样式。\n6. 展示了如何显示滑动条的值提示，并在滑动时动态更新提示内容。\n*/\n\n@Entry\n@Component\nstruct SliderExample {\n  @State tipsValue: number = 40 // 初始化滑动条的值，用于显示提示\n\n  build() {\n    Column({ space: 8 }) {\n      Text('block').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')\n      // 自定义滑动块的大小、边框颜色和宽度\n      Slider({ style: SliderStyle.OutSet, value: 40 })\n        .blockSize({ width: 40, height: 40 }) // 设置滑动块的大小\n        .blockBorderColor(Color.Red) // 设置滑动块边框颜色\n        .blockBorderWidth(5) // 设置滑动块边框宽度\n      Divider()\n      Text('step').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')\n      // 设置滑动条的步长、步长标记的大小和颜色\n      Slider({ style: SliderStyle.InSet, value: 40, step: 10 })\n        .showSteps(true) // 显示步长标记\n        .stepSize(8) // 设置步长标记的大小\n        .stepColor(Color.Yellow) // 设置步长标记的颜色\n      Divider()\n      Text('track').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')\n      // 自定义轨道的边框圆角\n      Slider({ style: SliderStyle.InSet, value: 40 })\n        .trackBorderRadius(2) // 设置轨道的边框圆角\n      Divider()\n      Text('selected').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')\n      // 自定义选中区域的边框圆角\n      Slider({ style: SliderStyle.InSet, value: 40 })\n        .selectedBorderRadius(2) // 设置选中区域的边框圆角\n      Divider()\n      Text('blockStyle').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')\n      // 设置滑动块的默认样式\n      Slider({ style: SliderStyle.OutSet, value: 40 })\n        .blockStyle({ type: SliderBlockType.DEFAULT }) // 设置滑动块为默认样式\n      // 设置滑动块为图片样式\n      Slider({ style: SliderStyle.OutSet, value: 40 })\n        .blockStyle({ type: SliderBlockType.IMAGE, image: $r('sys.media.ohos_app_icon') }) // 设置滑动块为图片样式\n      // 设置滑动块为自定义形状样式\n      Slider({ style: SliderStyle.OutSet, value: 40 })\n        .blockSize({ width: '60px', height: '60px' }) // 设置滑动块的大小\n        .blockColor(Color.Red) // 设置滑动块的颜色\n        .blockStyle({ type: SliderBlockType.SHAPE, shape: new Path({ commands: 'M60 60 M30 30 L15 56 L45 56 Z' }) }) // 设置滑动块为自定义形状样式\n      Divider()\n      Text('tips').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')\n      // 显示滑动条的值提示，并在滑动时动态更新提示内容\n      Slider({ style: SliderStyle.InSet, value: this.tipsValue })\n        .showTips(true, this.tipsValue.toFixed()) // 显示滑动条的值提示\n        .onChange(value => {\n          this.tipsValue = value // 更新滑动条的值\n        })\n    }\n  }\n}",
            "// xxx.ets\n/*\n该示例实现了Slider组件通过样式Builder定制内容区。点击增加按钮，进度条会按照原Slider设置的步长增加，反之点减少按钮进度条会减少，并触发原组件的onChange事件。\n实现思路：\n本示例展示了如何通过自定义Builder函数和ContentModifier接口来定制Slider组件的内容区。通过点击“增加”和“减少”按钮，可以按照Slider设置的步长增加或减少进度条的值，并触发Slider的onChange事件。此外，还展示了如何根据自定义的ContentModifier来控制Slider的显示状态和滑动模式。\n\n总体功能与效果描述：\n1. 通过自定义Builder函数`buildSlider`，实现了Slider组件的内容区定制，包括进度环、增加按钮、减少按钮、Slider本身以及相关文本信息的显示。\n2. 通过点击“增加”和“减少”按钮，可以按照Slider设置的步长增加或减少进度条的值，并触发Slider的onChange事件。\n3. 通过自定义的ContentModifier接口`MySliderStyle`，实现了对Slider显示状态和滑动模式的控制。\n4. 在Slider的onChange事件中，更新Slider的值和滑动模式，并在控制台输出相关信息。\n*/\n\n@Builder function buildSlider(config: SliderConfiguration) {\n  Row() {\n    Column({space: 30}) {\n      // 显示进度环\n      Progress({value: config.value, total: config.max, type:ProgressType.Ring})\n        .margin({ top:20 })\n\n      // 增加按钮，点击时增加Slider的值\n      Button('增加').onClick(() => {\n        config.value = config.value + config.step\n        config.triggerChange(config.value, SliderChangeMode.Click)\n      })\n        .width(100)\n        .height(25)\n        .fontSize(10)\n        .enabled(config.value < config.max) // 仅当Slider的值小于最大值时启用\n\n      // 减少按钮，点击时减少Slider的值\n      Button('减少').onClick(() => {\n        config.value = config.value - config.step\n        config.triggerChange(config.value, SliderChangeMode.Click)\n      })\n        .width(100)\n        .height(25)\n        .fontSize(10)\n        .enabled(config.value > config.min) // 仅当Slider的值大于最小值时启用\n\n      // Slider组件，显示步长标记\n      Slider({\n        value: config.value,\n        min: config.min,\n        max: config.max,\n        step: config.step,\n      })\n        .width(config.max)\n        .visibility((config.contentModifier as MySliderStyle).showSlider ? Visibility.Visible : Visibility.Hidden) // 根据ContentModifier控制Slider的显示状态\n        .showSteps(true)\n        .onChange((value: number, mode: SliderChangeMode) => {\n          config.triggerChange(value, mode)\n        })\n\n      // 显示当前滑动模式\n      Text('当前状态：' + ((config.contentModifier as MySliderStyle).sliderChangeMode == 0 ? \"Begin\"\n        : ((config.contentModifier as MySliderStyle).sliderChangeMode == 1 ? \"Moving\"\n          : ((config.contentModifier as MySliderStyle).sliderChangeMode == 2 ? \"End\"\n            : ((config.contentModifier as MySliderStyle).sliderChangeMode == 3 ? \"Click\" : \"无\")))))\n        .fontSize(10)\n\n      // 显示Slider的当前值\n      Text('进度值：' + config.value)\n        .fontSize(10)\n\n      // 显示Slider的最小值\n      Text('最小值：' + config.min)\n        .fontSize(10)\n\n      // 显示Slider的最大值\n      Text('最大值：' + config.max)\n        .fontSize(10)\n\n      // 显示Slider的步长\n      Text('步长：' + config.step)\n        .fontSize(10)\n    }\n    .width('80%')\n  }\n  .width('100%')\n}\n\n// 自定义ContentModifier接口实现\nclass MySliderStyle implements ContentModifier<SliderConfiguration> {\n  showSlider: boolean = true\n  sliderChangeMode: number = 0\n\n  constructor(showSlider: boolean, sliderChangeMode: number) {\n    this.showSlider = showSlider\n    this.sliderChangeMode = sliderChangeMode\n  }\n\n  applyContent(): WrappedBuilder<[SliderConfiguration]> {\n    return wrapBuilder(buildSlider)\n  }\n}\n\n@Entry\n@Component\nstruct SliderExample {\n  @State showSlider: boolean = true\n  @State sliderValue: number = 0\n  @State sliderMin: number = 10\n  @State sliderMax: number = 100\n  @State sliderStep: number = 20\n  @State sliderChangeMode: number = 0\n\n  build() {\n    Column({ space: 8 }) {\n      Row() {\n        Slider({\n          value: this.sliderValue,\n          min: this.sliderMin,\n          max: this.sliderMax,\n          step: this.sliderStep,\n        })\n          .showSteps(true)\n          .onChange((value: number, mode: SliderChangeMode) => {\n            this.sliderValue = value\n            this.sliderChangeMode = mode\n            console.info('【SliderLog】value:' + value + 'mode:' + mode.toString())\n          })\n          .contentModifier(new MySliderStyle(this.showSlider, this.sliderChangeMode)) // 应用自定义的ContentModifier\n      }\n      .width('100%')\n    }\n    .width('100%')\n  }\n}"
        ],
        "is_common_attrs": True
    },
    "Span": {
        "description": "作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。",
        "interfaces": [
            {
                "description": "Span(value: string | Resource)",
                "params": {
                    "value": {
                        "type": ["string", "Resource"],
                        "required": True,
                        "description": "文本内容。"
                    }
                }
            }
        ],
        "attributes": {
            "decoration": {
                "description": "decoration(value: DecorationStyleInterface)",
                "params": {
                    "value": {
                        "type": "DecorationStyleInterface12+",
                        "required": True,
                        "description": "文本装饰线样式对象。",
                        "default": {
                            "type": "TextDecorationType.None",
                            "color": "Color.Black",
                            "style": "TextDecorationStyle.SOLID"
                        }
                    }
                }
            },
            "letterSpacing": {
                "description": "letterSpacing(value: number | string)",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "文本字符间距。"
                    }
                }
            },
            "textCase": {
                "description": "textCase(value: TextCase)",
                "params": {
                    "value": {
                        "type": "TextCase",
                        "required": True,
                        "description": "文本大小写。",
                        "default": "TextCase.Normal"
                    }
                }
            },
            "lineHeight": {
                "description": "lineHeight(value: Length)",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "文本行高。"
                    }
                }
            },
            "font": {
                "description": "font(value: Font)",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "文本样式。"
                    }
                }
            },
            "textShadow": {
                "description": "textShadow(value: ShadowOptions | Array<ShadowOptions>)",
                "params": {
                    "value": {
                        "type": ["ShadowOptions", "Array<ShadowOptions>"],
                        "required": True,
                        "description": "文字阴影效果。"
                    }
                }
            }
        },
        "events": {
            "onClick": {
                "description": "通用事件仅支持点击事件。",
                "params": {}
            }
        },
        "examples": [
            """// xxx.ets\n@Entry\n@Component\nstruct SpanExample {\n  build() {\n    // 创建一个垂直方向的 Flex 布局，子元素垂直从头部对齐，间距均匀分布\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {\n      \n      // 基本用法示例\n      Text('Basic Usage').fontSize(9).fontColor(0xCCCCCC)\n      Text() {\n        Span('In Line')\n        Span(' Component')\n        Span(' !')\n      }\n\n      // Span 组件示例，设置文本大小写为正常，去除装饰线，字体颜色为红色\n      Text() {\n        Span('This is the Span component').fontSize(12).textCase(TextCase.Normal)\n          .decoration({ type: TextDecorationType.None, color: Color.Red })\n      }\n\n      // 文本添加下划线，样式为波浪线\n      Text('Text Decoration').fontSize(9).fontColor(0xCCCCCC)\n      Text() {\n        Span('I am Underline-WAVY-span').decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY }).fontSize(12)\n      }\n\n      // 文本添加删除线，样式为点状\n      Text() {\n        Span('I am LineThrough-DOTTED-span')\n          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red, style: TextDecorationStyle.DOTTED })\n          .fontSize(12)\n      }\n\n      // 文本添加上划线，样式为虚线\n      Text() {\n        Span('I am Overline-DASHED-span').decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED }).fontSize(12)\n      }\n\n      // 文本字符间距示例\n      Text('LetterSpacing').fontSize(9).fontColor(0xCCCCCC)\n      Text() {\n        Span('span letter spacing')\n          .letterSpacing(0)\n          .fontSize(12)\n      }\n\n      Text() {\n        Span('span letter spacing')\n          .letterSpacing(-2)\n          .fontSize(12)\n      }\n\n      Text() {\n        Span('span letter spacing')\n          .letterSpacing(3)\n          .fontSize(12)\n      }\n\n      // 文本大小写展示设置示例\n      Text('Text Case').fontSize(9).fontColor(0xCCCCCC)\n      Text() {\n        Span('I am Lower-span').fontSize(12)\n          .textCase(TextCase.LowerCase)\n          .decoration({ type: TextDecorationType.None })\n      }\n\n      Text() {\n        Span('I am Upper-span').fontSize(12)\n          .textCase(TextCase.UpperCase)\n          .decoration({ type: TextDecorationType.None })\n      }\n    }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct SpanExample {\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {\n      Text('Basic Usage').fontSize(9).fontColor(0xCCCCCC)\n      Text() {\n        Span('In Line')\n        Span(' Component')\n        Span(' !')\n      }\n\n      Text() {\n        Span('This is the Span component').fontSize(12).textCase(TextCase.Normal)\n          .decoration({ type: TextDecorationType.None, color: Color.Red })\n      }\n\n      // 文本横线添加\n      Text('Text Decoration').fontSize(9).fontColor(0xCCCCCC)\n      Text() {\n        Span('I am Underline-WAVY-span').decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY }).fontSize(12)\n      }\n\n      Text() {\n        Span('I am LineThrough-DOTTED-span')\n          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red, style: TextDecorationStyle.DOTTED })\n          .fontSize(12)\n      }\n\n      Text() {\n        Span('I am Overline-DASHED-span').decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED }).fontSize(12)\n      }\n\n      // 文本字符间距\n      Text('LetterSpacing').fontSize(9).fontColor(0xCCCCCC)\n      Text() {\n        Span('span letter spacing')\n          .letterSpacing(0)\n          .fontSize(12)\n      }\n\n      Text() {\n        Span('span letter spacing')\n          .letterSpacing(-2)\n          .fontSize(12)\n      }\n\n      Text() {\n        Span('span letter spacing')\n          .letterSpacing(3)\n          .fontSize(12)\n      }\n\n\n\n      // 文本大小写展示设置\n      Text('Text Case').fontSize(9).fontColor(0xCCCCCC)\n      Text() {\n        Span('I am Lower-span').fontSize(12)\n          .textCase(TextCase.LowerCase)\n          .decoration({ type: TextDecorationType.None })\n      }\n\n      Text() {\n        Span('I am Upper-span').fontSize(12)\n          .textCase(TextCase.UpperCase)\n          .decoration({ type: TextDecorationType.None })\n      }\n    }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })\n  }\n}"""
            """@Entry\n@Component\nstruct TextSpanExample {\n  @State textShadows : ShadowOptions | Array<ShadowOptions> = [{ radius: 10, color: Color.Red, offsetX: 10, offsetY: 0 },{ radius: 10, color: Color.Black, offsetX: 20, offsetY: 0 },\n      { radius: 10, color: Color.Brown, offsetX: 30, offsetY: 0 },{ radius: 10, color: Color.Green, offsetX: 40, offsetY: 0 },\n      { radius: 10, color: Color.Yellow, offsetX: 100, offsetY: 0 }]\n  build() {\n    Column({ space: 8 }) {\n      Text() {\n        // 创建一个文本组件，显示文本 '123456789'，设置字体大小为50，并应用指定的文本阴影效果\n        Span('123456789').fontSize(50).textShadow(this.textShadows)\n      }\n      Text() {\n        // 创建另一个文本组件，显示文本 '123456789'，该文本继承外部文本的字体大小和文本阴影效果\n        Span('123456789') // span can inherit text shadow & font size from outer text\n      }.fontSize(50).textShadow(this.textShadows)\n    }\n  }\n}\n```\n\n在上面的示例代码中：\n- `textShadows` 是一个状态变量，用于存储文本阴影的配置信息。\n- `build()` 方法用于构建界面布局。\n- 第一个 `Text` 组件显示文本 '123456789'，设置字体大小为50，并应用指定的文本阴影效果。\n- 第二个 `Text` 组件显示文本 '123456789'，该文本继承外部文本的字体大小和文本阴影效果。\n@Entry\n@Component\nstruct TextSpanExample {\n  @State textShadows : ShadowOptions | Array<ShadowOptions> = [{ radius: 10, color: Color.Red, offsetX: 10, offsetY: 0 },{ radius: 10, color: Color.Black, offsetX: 20, offsetY: 0 },\n      { radius: 10, color: Color.Brown, offsetX: 30, offsetY: 0 },{ radius: 10, color: Color.Green, offsetX: 40, offsetY: 0 },\n      { radius: 10, color: Color.Yellow, offsetX: 100, offsetY: 0 }]\n  build() {\n    Column({ space: 8 }) {\n      Text() {\n        Span('123456789').fontSize(50).textShadow(this.textShadows)\n      }\n      Text() {\n        Span('123456789') // span can inherit text shadow & font size from outer text\n      }.fontSize(50).textShadow(this.textShadows)\n    }\n  }\n}"""
            """// xxx.ets\n\n@Component\n@Entry\nstruct Index {\n  build() {\n    // 创建一个包含文本的列，文本内容为"Hello World !"\n    Column() {\n      // 创建一个文本组件，显示"Hello World !"，设置字体大小为20fp，背景颜色为紫色，圆角半径为5vp，字体颜色为白色\n      Text() {\n        Span('   Hello World !   ')\n          .fontSize('20fp')\n          .textBackgroundStyle({color: "#7F007DFF", radius: "5vp"})\n          .fontColor(Color.White)\n      }\n    }\n    // 设置列的宽度为100%，底部外边距为5vp，水平居中对齐\n    .width('100%').margin({bottom: '5vp'}).alignItems(HorizontalAlign.Center)\n  }\n}\n```\n\n```java\n// 功能与效果描述：\n// 1. 创建了一个包含文本的列，文本内容为"Hello World !"\n// 2. 在列中创建了一个文本组件，显示"Hello World !"，设置了字体大小、背景颜色、圆角半径和字体颜色\n// 3. 设置了列的宽度为100%，底部外边距为5vp，水平居中对齐\n```\n// xxx.ets\n@Component\n@Entry\nstruct Index {\n  build() {\n    Column() {\n      Text() {\n        Span('   Hello World !   ')\n          .fontSize('20fp')\n          .textBackgroundStyle({color: "#7F007DFF", radius: "5vp"})\n          .fontColor(Color.White)\n      }\n    }.width('100%').margin({bottom: '5vp'}).alignItems(HorizontalAlign.Center)\n  }\n}"""
            """// 该示例实现了如何设置Span基线的偏移量。\n\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    Row() {\n      Column() {\n        Text(){\n          // 设置第一个Span的基线偏移量为20VP\n          Span('word1')\n            .baselineOffset(new LengthMetrics(20,LengthUnit.VP))\n          // 设置第二个Span的基线偏移量为0VP，即不偏移\n          Span('word2')\n            .baselineOffset(new LengthMetrics(0,LengthUnit.VP))\n          // 设置ImageSpan的基线偏移量为-20VP，向上偏移\n          ImageSpan($r("app.media.icon"))\n            .width('45px')\n            .baselineOffset(new LengthMetrics(-20,LengthUnit.VP))\n        }\n        .backgroundColor(Color.Gray) // 设置Column的背景颜色为灰色\n      }\n      .width('100%') // 设置Column的宽度为100%\n    }\n    .height('100%') // 设置Row的高度为100%\n  }\n}\n```\n\n在上述代码中：\n- 第一个Span 'word1' 的基线偏移量被设置为20VP，使得该文本向下偏移了20VP。\n- 第二个Span 'word2' 的基线偏移量为0VP，未偏移，保持默认位置。\n- ImageSpan 使用了一个图标，并设置了宽度为45px，同时基线偏移量为-20VP，使得图标向上偏移了20VP。\n- Column 的背景颜色被设置为灰色。\n- Column 的宽度被设置为100%。\n- Row 的高度被设置为100%。\nimport { LengthUnit, LengthMetrics } from '@kit.ArkUI';\n\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    Row() {\n      Column() {\n        Text(){\n          Span('word1')\n            .baselineOffset(new LengthMetrics(20,LengthUnit.VP))\n          Span('word2')\n            .baselineOffset(new LengthMetrics(0,LengthUnit.VP))\n          ImageSpan($r("app.media.icon"))\n            .width('45px')\n            .baselineOffset(new LengthMetrics(-20,LengthUnit.VP))\n        }\n        .backgroundColor(Color.Gray)\n      }\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Stepper": {
        "description": "步骤导航器组件，适用于引导用户按照步骤完成任务的导航场景。",
        "interfaces": [
            {
                "description": "Stepper(value?: { index?: number })",
                "params": {
                    "value": {
                        "type": {
                            "index": "number"
                        },
                        "required": False,
                        "description": "设置步骤导航器当前显示StepperItem的索引值。",
                        "default": {
                            "index": 0
                        }
                    }
                }
            }
        ],
        "attributes": {},
        "events": {
            "onFinish": {
                "description": "步骤导航器最后一个StepperItem的nextLabel被点击时，并且ItemState属性为Normal时，触发该回调。",
                "params": {}
            },
            "onSkip": {
                "description": "当前显示的StepperItem状态为ItemState.Skip时，nextLabel被点击时触发该回调。",
                "params": {}
            },
            "onChange": {
                "description": "点击当前StepperItem的prevLabel进行步骤切换时触发该回调；或点击当前StepperItem的nextLabel，当前页面不为步骤导航器最后一个StepperItem且ItemState属性为Normal时，触发该回调。",
                "params": {
                    "prevIndex": {
                        "type": "number",
                        "required": True,
                        "description": "切换前的步骤页索引值。"
                    },
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "切换后的步骤页（前一页或者下一页）索引值。"
                    }
                }
            },
            "onNext": {
                "description": "点击StepperItem的nextLabel切换下一步骤时，当前页面不为步骤导航器最后一个StepperItem且ItemState属性为Normal时，触发该回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前步骤页索引值。"
                    },
                    "pendingIndex": {
                        "type": "number",
                        "required": True,
                        "description": "下一步骤页索引值。"
                    }
                }
            },
            "onPrevious": {
                "description": "点击StepperItem的prevLabel切换上一步骤时触发该回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前步骤页索引值。"
                    },
                    "pendingIndex": {
                        "type": "number",
                        "required": True,
                        "description": "上一步骤页索引值。"
                    }
                }
            }
        },
        "examples": [
            """// xxx.ets\n\n// 定义itemStyle函数，设置Item的样式属性\n@Styles function itemStyle () {\n  .width(336) // 设置宽度为336\n  .height(621) // 设置高度为621\n  .margin({ top: 48, left: 12 }) // 设置上边距为48，左边距为12\n  .borderRadius(24) // 设置圆角半径为24\n  .backgroundColor('#FFFFFF') // 设置背景颜色为白色\n}\n\n// 定义itemTextStyle函数，扩展Text组件的样式属性\n@Extend(Text) function itemTextStyle () {\n  .fontColor('#182431') // 设置字体颜色为深蓝色\n  .fontSize(36) // 设置字体大小为36\n  .fontWeight(500) // 设置字体粗细为500\n  .opacity(0.4) // 设置透明度为0.4\n  .margin({ top: 82, bottom: 40 }) // 设置上边距为82，下边距为40\n}\n\n// 定义StepperExample结构体，实现多步骤展示功能\n@Entry\n@Component\nstruct StepperExample {\n  @State currentIndex: number = 0 // 当前步骤索引\n  @State firstState: ItemState = ItemState.Normal // 第一个步骤的状态\n  @State secondState: ItemState = ItemState.Normal // 第二个步骤的状态\n  @State thirdState: ItemState = ItemState.Normal // 第三个步骤的状态\n\n  build() {\n    Stepper({\n      index: this.currentIndex // 设置当前步骤索引\n    }) {\n      // 第一个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page One')\n            .itemTextStyle() // 应用itemTextStyle样式\n          Button('change status:' + this.firstState)\n            .backgroundColor('#007dFF') // 设置背景颜色为蓝色\n            .onClick(() => {\n              this.firstState = this.firstState === ItemState.Skip ? ItemState.Normal : ItemState.Skip\n            })\n        }.itemStyle() // 应用itemStyle样式\n      }\n      .nextLabel('Next') // 设置下一步按钮文本\n      .status(this.firstState) // 设置步骤状态\n\n      // 第二个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Two')\n            .itemTextStyle() // 应用itemTextStyle样式\n          Button('change status:' + this.secondState)\n            .backgroundColor('#007dFF') // 设置背景颜色为蓝色\n            .onClick(() => {\n              this.secondState = this.secondState === ItemState.Disabled ? ItemState.Normal : ItemState.Disabled\n            })\n        }.itemStyle() // 应用itemStyle样式\n      }\n      .nextLabel('Next') // 设置下一步按钮文本\n      .prevLabel('Previous') // 设置上一步按钮文本\n      .status(this.secondState) // 设置步骤状态\n\n      // 第三个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Three')\n            .itemTextStyle() // 应用itemTextStyle样式\n          Button('change status:' + this.thirdState)\n            .backgroundColor('#007dFF') // 设置背景颜色为蓝色\n            .onClick(() => {\n              this.thirdState = this.thirdState === ItemState.Waiting ? ItemState.Normal : ItemState.Waiting\n            })\n        }.itemStyle() // 应用itemStyle样式\n      }\n      .status(this.thirdState) // 设置步骤状态\n\n      // 第四个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Four')\n            .itemTextStyle() // 应用itemTextStyle样式\n        }.itemStyle() // 应用itemStyle样式\n      }\n    }\n    .backgroundColor('#F1F3F5') // 设置背景颜色为灰色\n    .onFinish(() => {\n      // 处理点击最后一页的Finish时的逻辑\n      console.info('onFinish')\n    })\n    .onSkip(() => {\n      // 处理点击跳过时的逻辑\n      console.info('onSkip')\n    })\n    .onChange((prevIndex?: number, index?: number) => {\n      if(index){\n        this.currentIndex = index // 更新当前步骤索引\n      }\n    })\n  }\n}\n```\n// xxx.ets\n@Styles function itemStyle () {\n  .width(336)\n  .height(621)\n  .margin({ top: 48, left: 12 })\n  .borderRadius(24)\n  .backgroundColor('#FFFFFF')\n}\n\n@Extend(Text) function itemTextStyle () {\n  .fontColor('#182431')\n  .fontSize(36)\n  .fontWeight(500)\n  .opacity(0.4)\n  .margin({ top: 82, bottom: 40 })\n}\n\n@Entry\n@Component\nstruct StepperExample {\n  @State currentIndex: number = 0\n  @State firstState: ItemState = ItemState.Normal\n  @State secondState: ItemState = ItemState.Normal\n  @State thirdState: ItemState = ItemState.Normal\n\n  build() {\n    Stepper({\n      index: this.currentIndex\n    }) {\n      // 第一个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page One')\n            .itemTextStyle()\n          Button('change status:' + this.firstState)\n            .backgroundColor('#007dFF')\n            .onClick(() => {\n              this.firstState = this.firstState === ItemState.Skip ? ItemState.Normal : ItemState.Skip\n            })\n        }.itemStyle()\n      }\n      .nextLabel('Next')\n      .status(this.firstState)\n      // 第二个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Two')\n            .itemTextStyle()\n          Button('change status:' + this.secondState)\n            .backgroundColor('#007dFF')\n            .onClick(() => {\n              this.secondState = this.secondState === ItemState.Disabled ? ItemState.Normal : ItemState.Disabled\n            })\n        }.itemStyle()\n      }\n      .nextLabel('Next')\n      .prevLabel('Previous')\n      .status(this.secondState)\n      // 第三个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Three')\n            .itemTextStyle()\n          Button('change status:' + this.thirdState)\n            .backgroundColor('#007dFF')\n            .onClick(() => {\n              this.thirdState = this.thirdState === ItemState.Waiting ? ItemState.Normal : ItemState.Waiting\n            })\n        }.itemStyle()\n      }\n      .status(this.thirdState)\n      // 第四个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Four')\n            .itemTextStyle()\n        }.itemStyle()\n      }\n    }\n    .backgroundColor('#F1F3F5')\n    .onFinish(() => {\n      // 此处可处理点击最后一页的Finish时的逻辑，例如路由跳转等\n      console.info('onFinish')\n    })\n    .onSkip(() => {\n      // 此处可处理点击跳过时的逻辑，例如动态修改Stepper的index值使其跳转到某一步骤页等\n      console.info('onSkip')\n    })\n    .onChange((prevIndex?: number, index?: number) => {\n      if(index){\n        this.currentIndex = index\n      }\n    })\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "StepperItem": {
        "description": "用作Stepper组件的页面子组件。",
        "interfaces": [
            {
                "description": "StepperItem()",
                "params": {}
            }
        ],
        "attributes": {
            "prevLabel": {
                "description": "prevLabel(value: string)",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "左侧文本按钮内容。"
                    }
                }
            },
            "nextLabel": {
                "description": "nextLabel(value: string)",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "右侧文本按钮内容。"
                    }
                }
            },
            "status": {
                "description": "status(value?: ItemState)",
                "params": {
                    "value": {
                        "type": "ItemState",
                        "required": False,
                        "description": "步骤导航器nextLabel的显示状态。",
                        "default": "ItemState.Normal"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """"示// xxx.ets\n\n// 定义itemStyle函数，设置Item的样式属性\n@Styles function itemStyle () {\n  .width(336) // 设置宽度为336\n  .height(621) // 设置高度为621\n  .margin({ top: 48, left: 12 }) // 设置上边距为48，左边距为12\n  .borderRadius(24) // 设置圆角半径为24\n  .backgroundColor('#FFFFFF') // 设置背景颜色为白色\n}\n\n// 定义itemTextStyle函数，扩展Text组件的样式属性\n@Extend(Text) function itemTextStyle () {\n  .fontColor('#182431') // 设置字体颜色为深蓝色\n  .fontSize(36) // 设置字体大小为36\n  .fontWeight(500) // 设置字体粗细为500\n  .opacity(0.4) // 设置透明度为0.4\n  .margin({ top: 82, bottom: 40 }) // 设置上边距为82，下边距为40\n}\n\n// 定义StepperExample结构体，实现多步骤展示功能\n@Entry\n@Component\nstruct StepperExample {\n  @State currentIndex: number = 0 // 当前步骤索引\n  @State firstState: ItemState = ItemState.Normal // 第一个步骤的状态\n  @State secondState: ItemState = ItemState.Normal // 第二个步骤的状态\n  @State thirdState: ItemState = ItemState.Normal // 第三个步骤的状态\n\n  build() {\n    Stepper({\n      index: this.currentIndex // 设置当前步骤索引\n    }) {\n      // 第一个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page One')\n            .itemTextStyle() // 应用itemTextStyle样式\n          Button('change status:' + this.firstState)\n            .backgroundColor('#007dFF') // 设置背景颜色为蓝色\n            .onClick(() => {\n              this.firstState = this.firstState === ItemState.Skip ? ItemState.Normal : ItemState.Skip\n            })\n        }.itemStyle() // 应用itemStyle样式\n      }\n      .nextLabel('Next') // 设置下一步按钮文本\n      .status(this.firstState) // 设置步骤状态\n\n      // 第二个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Two')\n            .itemTextStyle() // 应用itemTextStyle样式\n          Button('change status:' + this.secondState)\n            .backgroundColor('#007dFF') // 设置背景颜色为蓝色\n            .onClick(() => {\n              this.secondState = this.secondState === ItemState.Disabled ? ItemState.Normal : ItemState.Disabled\n            })\n        }.itemStyle() // 应用itemStyle样式\n      }\n      .nextLabel('Next') // 设置下一步按钮文本\n      .prevLabel('Previous') // 设置上一步按钮文本\n      .status(this.secondState) // 设置步骤状态\n\n      // 第三个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Three')\n            .itemTextStyle() // 应用itemTextStyle样式\n          Button('change status:' + this.thirdState)\n            .backgroundColor('#007dFF') // 设置背景颜色为蓝色\n            .onClick(() => {\n              this.thirdState = this.thirdState === ItemState.Waiting ? ItemState.Normal : ItemState.Waiting\n            })\n        }.itemStyle() // 应用itemStyle样式\n      }\n      .status(this.thirdState) // 设置步骤状态\n\n      // 第四个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Four')\n            .itemTextStyle() // 应用itemTextStyle样式\n        }.itemStyle() // 应用itemStyle样式\n      }\n    }\n    .backgroundColor('#F1F3F5') // 设置背景颜色为灰色\n    .onFinish(() => {\n      // 处理点击最后一页的Finish时的逻辑\n      console.info('onFinish')\n    })\n    .onSkip(() => {\n      // 处理点击跳过时的逻辑\n      console.info('onSkip')\n    })\n    .onChange((prevIndex?: number, index?: number) => {\n      if(index){\n        this.currentIndex = index // 更新当前步骤索引\n      }\n    })\n  }\n}\n```\n// xxx.ets\n@Styles function itemStyle () {\n  .width(336)\n  .height(621)\n  .margin({ top: 48, left: 12 })\n  .borderRadius(24)\n  .backgroundColor('#FFFFFF')\n}\n\n@Extend(Text) function itemTextStyle () {\n  .fontColor('#182431')\n  .fontSize(36)\n  .fontWeight(500)\n  .opacity(0.4)\n  .margin({ top: 82, bottom: 40 })\n}\n\n@Entry\n@Component\nstruct StepperExample {\n  @State currentIndex: number = 0\n  @State firstState: ItemState = ItemState.Normal\n  @State secondState: ItemState = ItemState.Normal\n  @State thirdState: ItemState = ItemState.Normal\n\n  build() {\n    Stepper({\n      index: this.currentIndex\n    }) {\n      // 第一个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page One')\n            .itemTextStyle()\n          Button('change status:' + this.firstState)\n            .backgroundColor('#007dFF')\n            .onClick(() => {\n              this.firstState = this.firstState === ItemState.Skip ? ItemState.Normal : ItemState.Skip\n            })\n        }.itemStyle()\n      }\n      .nextLabel('Next')\n      .status(this.firstState)\n      // 第二个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Two')\n            .itemTextStyle()\n          Button('change status:' + this.secondState)\n            .backgroundColor('#007dFF')\n            .onClick(() => {\n              this.secondState = this.secondState === ItemState.Disabled ? ItemState.Normal : ItemState.Disabled\n            })\n        }.itemStyle()\n      }\n      .nextLabel('Next')\n      .prevLabel('Previous')\n      .status(this.secondState)\n      // 第三个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Three')\n            .itemTextStyle()\n          Button('change status:' + this.thirdState)\n            .backgroundColor('#007dFF')\n            .onClick(() => {\n              this.thirdState = this.thirdState === ItemState.Waiting ? ItemState.Normal : ItemState.Waiting\n            })\n        }.itemStyle()\n      }\n      .status(this.thirdState)\n      // 第四个步骤页\n      StepperItem() {\n        Column() {\n          Text('Page Four')\n            .itemTextStyle()\n        }.itemStyle()\n      }\n    }\n    .backgroundColor('#F1F3F5')\n    .onFinish(() => {\n      // 此处可处理点击最后一页的Finish时的逻辑，例如路由跳转等\n      console.info('onFinish')\n    })\n    .onSkip(() => {\n      // 此处可处理点击跳过时的逻辑，例如动态修改Stepper的index值使其跳转到某一步骤页等\n      console.info('onSkip')\n    })\n    .onChange((prevIndex?: number, index?: number) => {\n      if(index){\n        this.currentIndex = index\n      }\n    })\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "SymbolSpan": {
        "description": "作为Text组件的子组件，用于显示图标小符号的组件。",
        "interfaces": [
            {
                "description": "SymbolSpan(value: Resource)",
                "params": {
                    "value": {
                        "type": "Resource",
                        "required": True,
                        "description": "SymbolSpan组件的资源名，如 $r('sys.symbol.ohos_wifi')。"
                    }
                }
            }
        ],
        "attributes": {
            "fontColor": {
                "description": "fontColor(value: Array<ResourceColor>)",
                "params": {
                    "value": {
                        "type": ["Array", "ResourceColor"],
                        "required": True,
                        "description": "SymbolSpan组件颜色。"
                    }
                }
            },
            "fontSize": {
                "description": "fontSize(value: number | string | Resource)",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "SymbolSpan组件大小。"
                    }
                }
            },
            "fontWeight": {
                "description": "fontWeight(value: number | FontWeight | string)",
                "params": {
                    "value": {
                        "type": ["number", "FontWeight", "string"],
                        "required": True,
                        "description": "SymbolSpan组件粗细。",
                        "default": "FontWeight.Normal"
                    }
                }
            },
            "renderingStrategy": {
                "description": "renderingStrategy(value: SymbolRenderingStrategy)",
                "params": {
                    "value": {
                        "type": "SymbolRenderingStrategy",
                        "required": True,
                        "description": "SymbolSpan渲染策略。",
                        "default": "SymbolRenderingStrategy.SINGLE"
                    }
                }
            },
            "effectStrategy": {
                "description": "effectStrategy(value: SymbolEffectStrategy)",
                "params": {
                    "value": {
                        "type": "SymbolEffectStrategy",
                        "required": True,
                        "description": "SymbolSpan动效策略。",
                        "default": "SymbolEffectStrategy.NONE"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """// xxx.ets\n\n// 创建一个页面入口组件\n@Entry\n@Component\nstruct Index {\n  build() {\n    // 创建一个垂直布局容器\n    Column() {\n      // 第一行展示不同字重的文字和对应的图标\n      Row() {\n        Column() {\n          // 显示"Light"文字\n          Text("Light")\n          // 显示轻字重的垃圾桶图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_trash'))\n              .fontWeight(FontWeight.Lighter) // 设置字体轻字重\n              .fontSize(96) // 设置字体大小\n          }\n        }\n\n        Column() {\n          // 显示"Normal"文字\n          Text("Normal")\n          // 显示普通字重的垃圾桶图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_trash'))\n              .fontWeight(FontWeight.Normal) // 设置字体普通字重\n              .fontSize(96) // 设置字体大小\n          }\n        }\n\n        Column() {\n          // 显示"Bold"文字\n          Text("Bold")\n          // 显示粗字重的垃圾桶图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_trash'))\n              .fontWeight(FontWeight.Bold) // 设置字体粗字重\n              .fontSize(96) // 设置字体大小\n          }\n        }\n      }\n\n      // 第二行展示不同的图标渲染策略\n      Row() {\n        Column() {\n          // 显示"单色"文字\n          Text("单色")\n          // 显示单色渲染策略的文件夹加徽章图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))\n              .fontSize(96) // 设置字体大小\n              .renderingStrategy(SymbolRenderingStrategy.SINGLE) // 设置单色渲染策略\n              .fontColor([Color.Black, Color.Green, Color.White]) // 设置字体颜色\n          }\n        }\n\n        Column() {\n          // 显示"多色"文字\n          Text("多色")\n          // 显示多色渲染策略的文件夹加徽章图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))\n              .fontSize(96) // 设置字体大小\n              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR) // 设置多色渲染策略\n              .fontColor([Color.Black, Color.Green, Color.White]) // 设置字体颜色\n          }\n        }\n\n        Column() {\n          // 显示"分层"文字\n          Text("分层")\n          // 显示分层渲染策略的文件夹加徽章图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))\n              .fontSize(96) // 设置字体大小\n              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY) // 设置分层渲染策略\n              .fontColor([Color.Black, Color.Green, Color.White]) // 设置字体颜色\n          }\n        }\n      }\n\n      // 第三行展示不同的图标动效策略\n      Row() {\n        Column() {\n          // 显示"无动效"文字\n          Text("无动效")\n          // 显示无动效的Wi-Fi图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_wifi'))\n              .fontSize(96) // 设置字体大小\n              .effectStrategy(SymbolEffectStrategy.NONE) // 设置无动效策略\n          }\n        }\n\n        Column() {\n          // 显示"整体缩放动效"文字\n          Text("整体缩放动效")\n          // 显示整体缩放动效的Wi-Fi图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_wifi'))\n              .fontSize(96) // 设置字体大小\n              .effectStrategy(1) // 设置整体缩放动效策略\n          }\n        }\n\n        Column() {\n          // 显示"层级动效"文字\n          Text("层级动效")\n          // 显示层级动效的Wi-Fi图标\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_wifi'))\n              .fontSize(96) // 设置字体大小\n              .effectStrategy(2) // 设置层级动效策略\n          }\n        }\n      }\n    }\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  build() {\n    Column() {\n      Row() {\n        Column() {\n          Text("Light")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_trash'))\n              .fontWeight(FontWeight.Lighter)\n              .fontSize(96)\n          }\n        }\n\n        Column() {\n          Text("Normal")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_trash'))\n              .fontWeight(FontWeight.Normal)\n              .fontSize(96)\n          }\n        }\n\n        Column() {\n          Text("Bold")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_trash'))\n              .fontWeight(FontWeight.Bold)\n              .fontSize(96)\n          }\n        }\n      }\n\n      Row() {\n        Column() {\n          Text("单色")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))\n              .fontSize(96)\n              .renderingStrategy(SymbolRenderingStrategy.SINGLE)\n              .fontColor([Color.Black, Color.Green, Color.White])\n          }\n        }\n\n        Column() {\n          Text("多色")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))\n              .fontSize(96)\n              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)\n              .fontColor([Color.Black, Color.Green, Color.White])\n          }\n        }\n\n        Column() {\n          Text("分层")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))\n              .fontSize(96)\n              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)\n              .fontColor([Color.Black, Color.Green, Color.White])\n          }\n        }\n      }\n\n      Row() {\n        Column() {\n          Text("无动效")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_wifi'))\n              .fontSize(96)\n              .effectStrategy(SymbolEffectStrategy.NONE)\n          }\n        }\n\n        Column() {\n          Text("整体缩放动效")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_wifi'))\n              .fontSize(96)\n              .effectStrategy(1)\n          }\n        }\n\n        Column() {\n          Text("层级动效")\n          Text() {\n            SymbolSpan($r('sys.symbol.ohos_wifi'))\n              .fontSize(96)\n              .effectStrategy(2)\n          }\n        }\n      }\n    }\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "SymbolGlyph": {
        "description": "显示图标小符号的组件。",
        "interfaces": [
            {
                "description": "SymbolGlyph(value: Resource)",
                "params": {
                    "value": {
                        "type": "Resource",
                        "required": True,
                        "description": "SymbolGlyph组件的资源名,如 $r('sys.symbol.ohos_wifi')。"
                    }
                }
            }
        ],
        "attributes": {
            "fontColor": {
                "description": "fontColor(value: Array<ResourceColor>)",
                "params": {
                    "value": {
                        "type": ["Array", "ResourceColor"],
                        "required": True,
                        "description": "SymbolGlyph组件颜色。",
                    }
                }
            },
            "fontSize": {
                "description": "fontSize(value: number | string | Resource)",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "SymbolGlyph组件大小。"
                    }
                }
            },
            "fontWeight": {
                "description": "fontWeight(value: number | FontWeight | string)",
                "params": {
                    "value": {
                        "type": ["number", "FontWeight", "string"],
                        "required": True,
                        "description": "SymbolGlyph组件粗细。",
                        "default": "FontWeight.Normal"
                    }
                }
            },
            "renderingStrategy": {
                "description": "renderingStrategy(value: SymbolRenderingStrategy)",
                "params": {
                    "value": {
                        "type": "SymbolRenderingStrategy",
                        "required": True,
                        "description": "SymbolGlyph组件渲染策略。",
                        "default": "SymbolRenderingStrategy.SINGLE"
                    }
                }
            },
            "effectStrategy": {
                "description": "effectStrategy(value: SymbolEffectStrategy)",
                "params": {
                    "value": {
                        "type": "SymbolEffectStrategy",
                        "required": True,
                        "description": "SymbolGlyph组件动效策略。",
                        "default": "SymbolEffectStrategy.NONE"
                    }
                }
            },
            "symbolEffect": {
                "description": "symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number)",
                "params": {
                    "symbolEffect": {
                        "type": ["SymbolEffect", "ScaleSymbolEffect", "HierarchicalSymbolEffect", "AppearSymbolEffect",
                                 "DisappearSymbolEffect", "BounceSymbolEffect", "ReplaceSymbolEffect",
                                 "PulseSymbolEffect"],
                        "required": True,
                        "description": "SymbolGlyph组件动效策略。",
                        "default": "SymbolEffect"
                    },
                    "triggerValue": {
                        "type": "number",
                        "required": False,
                        "description": "SymbolGlyph组件动效播放触发器，在数值变更时触发动效。如果首次不希望触发动效，设置-1。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            """// xxx.ets\n\n@Entry\n@Component\nstruct Index {\n  build() {\n    // 创建包含不同字体粗细和效果的文本和符号的布局\n    Column() {\n      // 第一行展示不同字体粗细的符号\n      Row() {\n        Column() {\n          // 显示轻字体重量的文本和符号\n          Text("Light")\n          SymbolGlyph($r('sys.symbol.ohos_trash'))\n            .fontWeight(FontWeight.Lighter)\n            .fontSize(96)\n        }\n\n        Column() {\n          // 显示正常字体重量的文本和符号\n          Text("Normal")\n          SymbolGlyph($r('sys.symbol.ohos_trash'))\n            .fontWeight(FontWeight.Normal)\n            .fontSize(96)\n        }\n\n        Column() {\n          // 显示粗字体重量的文本和符号\n          Text("Bold")\n          SymbolGlyph($r('sys.symbol.ohos_trash'))\n            .fontWeight(FontWeight.Bold)\n            .fontSize(96)\n        }\n      }\n\n      // 第二行展示不同符号渲染策略\n      Row() {\n        Column() {\n          // 单色渲染策略的符号\n          Text("单色")\n          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))\n            .fontSize(96)\n            .renderingStrategy(SymbolRenderingStrategy.SINGLE)\n            .fontColor([Color.Black, Color.Green, Color.White])\n        }\n\n        Column() {\n          // 多色渲染策略的符号\n          Text("多色")\n          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))\n            .fontSize(96)\n            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)\n            .fontColor([Color.Black, Color.Green, Color.White])\n        }\n\n        Column() {\n          // 分层渲染策略的符号\n          Text("分层")\n          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))\n            .fontSize(96)\n            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)\n            .fontColor([Color.Black, Color.Green, Color.White])\n        }\n      }\n\n      // 第三行展示不同符号动效策略\n      Row() {\n        Column() {\n          // 无动效的符号\n          Text("无动效")\n          SymbolGlyph($r('sys.symbol.ohos_wifi'))\n            .fontSize(96)\n            .effectStrategy(SymbolEffectStrategy.NONE)\n        }\n\n        Column() {\n          // 整体缩放动效的符号\n          Text("整体缩放动效")\n          SymbolGlyph($r('sys.symbol.ohos_wifi'))\n            .fontSize(96)\n            .effectStrategy(1)\n        }\n\n        Column() {\n          // 层级动效的符号\n          Text("层级动效")\n          SymbolGlyph($r('sys.symbol.ohos_wifi'))\n            .fontSize(96)\n            .effectStrategy(2)\n        }\n      }\n    }\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  build() {\n    Column() {\n      Row() {\n        Column() {\n          Text("Light")\n          SymbolGlyph($r('sys.symbol.ohos_trash'))\n            .fontWeight(FontWeight.Lighter)\n            .fontSize(96)\n        }\n\n        Column() {\n          Text("Normal")\n          SymbolGlyph($r('sys.symbol.ohos_trash'))\n            .fontWeight(FontWeight.Normal)\n            .fontSize(96)\n        }\n\n        Column() {\n          Text("Bold")\n          SymbolGlyph($r('sys.symbol.ohos_trash'))\n            .fontWeight(FontWeight.Bold)\n            .fontSize(96)\n        }\n      }\n\n      Row() {\n        Column() {\n          Text("单色")\n          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))\n            .fontSize(96)\n            .renderingStrategy(SymbolRenderingStrategy.SINGLE)\n            .fontColor([Color.Black, Color.Green, Color.White])\n        }\n\n        Column() {\n          Text("多色")\n          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))\n            .fontSize(96)\n            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)\n            .fontColor([Color.Black, Color.Green, Color.White])\n        }\n\n        Column() {\n          Text("分层")\n          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))\n            .fontSize(96)\n            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)\n            .fontColor([Color.Black, Color.Green, Color.White])\n        }\n      }\n\n      Row() {\n        Column() {\n          Text("无动效")\n          SymbolGlyph($r('sys.symbol.ohos_wifi'))\n            .fontSize(96)\n            .effectStrategy(SymbolEffectStrategy.NONE)\n        }\n\n        Column() {\n          Text("整体缩放动效")\n          SymbolGlyph($r('sys.symbol.ohos_wifi'))\n            .fontSize(96)\n            .effectStrategy(1)\n        }\n\n        Column() {\n          Text("层级动效")\n          SymbolGlyph($r('sys.symbol.ohos_wifi'))\n            .fontSize(96)\n            .effectStrategy(2)\n        }\n      }\n    }\n  }\n}"""
            """SymbolGlyph使用symbolEffect属性实现可变颜色动效和替换动效。\n\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  @State isActive: boolean = true; // 用于控制可变颜色动效的激活状态\n  @State triggerValueReplace: number = 0; // 触发替换动效的值\n  replaceFlag: boolean = true; // 用于控制替换动效的标志位\n\n  build() {\n    Column() {\n      Row() {\n        Column() {\n          Text("可变颜色动效") // 显示文本：可变颜色动效\n          SymbolGlyph($r('sys.symbol.ohos_wifi')) // 使用系统图标'ohos_wifi'\n            .fontSize(96) // 设置图标字体大小为96\n            .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive) // 使用HierarchicalSymbolEffect实现可变颜色动效\n          Button(this.isActive ? '关闭' : '播放').onClick(() => { // 根据isActive状态显示不同文本的按钮\n            this.isActive = !this.isActive; // 切换isActive状态\n          })\n        }.margin({right:20})\n\n        Column() {\n          Text("替换动效") // 显示文本：替换动效\n          SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1')) // 根据replaceFlag选择不同的系统图标\n            .fontSize(96) // 设置图标字体大小为96\n            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace) // 使用ReplaceSymbolEffect实现替换动效\n          Button('trigger').onClick(() => { // 触发替换动效的按钮\n            this.replaceFlag = !this.replaceFlag; // 切换replaceFlag状态\n            this.triggerValueReplace = this.triggerValueReplace + 1; // 触发替换动效\n          })\n        }\n      }\n    }.margin({\n      left:30,\n      top:50\n    })\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  @State isActive: boolean = true;\n  @State triggerValueReplace: number = 0;\n  replaceFlag: boolean = true;\n\n  build() {\n    Column() {\n      Row() {\n        Column() {\n          Text("可变颜色动效")\n          SymbolGlyph($r('sys.symbol.ohos_wifi'))\n            .fontSize(96)\n            .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)\n          Button(this.isActive ? '关闭' : '播放').onClick(() => {\n            this.isActive = !this.isActive;\n          })\n        }.margin({right:20})\n\n        Column() {\n          Text("替换动效")\n          SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))\n            .fontSize(96)\n            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)\n          Button('trigger').onClick(() => {\n            this.replaceFlag = !this.replaceFlag;\n            this.triggerValueReplace = this.triggerValueReplace + 1;\n          })\n        }\n      }\n    }.margin({\n      left:30,\n      top:50\n    })\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "Text": {
        "description": "显示一段文本的组件，可以包含Span、ImageSpan、SymbolSpan和ContainerSpan子组件。",
        "interfaces": [
            {
                "description": "Text组件的接口定义。",
                "params": {
                    "Text": {
                        "type": ["string", "Resource"],
                        "required": False,
                        "description": "文本内容。包含子组件Span且未设置属性字符串时不生效，显示Span内容，并且此时text组件的样式不生效。",
                        "default": " "
                    },
                    "value": {
                        "type": "TextOptions",
                        "required": False,
                        "description": "文本组件初始化选项。"
                    }
                }
            }
        ],
        "attributes": {
            "textAlign": {
                "description": "设置文本段落在水平方向的对齐方式。",
                "params": {
                    "value": {
                        "type": "TextAlign",
                        "required": True,
                        "description": "文本段落在水平方向的对齐方式。",
                        "default": "TextAlign.Start"
                    }
                }
            },
            "textOverflow": {
                "description": "设置文本超长时的显示方式。",
                "params": {
                    "value": {
                        "type": {
                            "overflow": "TextOverflow"
                        },
                        "required": True,
                        "description": "文本超长时的显示方式。",
                        "default": {
                            "overflow": "TextOverflow.Clip"
                        }
                    }
                }
            },
            "maxLines": {
                "description": "设置文本的最大行数。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "文本的最大行数。"
                    }
                }
            },
            "lineHeight": {
                "description": "设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本的文本行高。"
                    }
                }
            },
            "decoration": {
                "description": "设置文本装饰线样式及其颜色。",
                "params": {
                    "value": {
                        "type": "DecorationStyleInterface",
                        "required": True,
                        "description": "文本装饰线样式对象。",
                        "default": {
                            "type": "TextDecorationType.None",
                            "color": "Color.Black",
                            "style": "TextDecorationStyle.SOLID"
                        }
                    }
                }
            },
            "baselineOffset": {
                "description": "设置文本基线的偏移量，设置该值为百分比时，按默认值显示。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "文本基线的偏移量。",
                        "default": 0
                    }
                }
            },
            "letterSpacing": {
                "description": "设置文本字符间距。设置该值为百分比时，按默认值显示。设置该值为0时，按默认值显示。",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "文本字符间距。"
                    }
                }
            },
            "minFontSize": {
                "description": "设置文本最小显示字号。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本最小显示字号。"
                    }
                }
            },
            "maxFontSize": {
                "description": "设置文本最大显示字号。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本最大显示字号。"
                    }
                }
            },
            "textCase": {
                "description": "设置文本大小写。",
                "params": {
                    "value": {
                        "type": "TextCase",
                        "required": True,
                        "description": "文本大小写。",
                        "default": "TextCase.Normal"
                    }
                }
            },
            "copyOption": {
                "description": "设置组件是否支持文本可复制粘贴。",
                "params": {
                    "value": {
                        "type": "CopyOptions",
                        "required": True,
                        "description": "组件是否支持文本可复制粘贴。",
                        "default": "CopyOptions.None"
                    }
                }
            },
            "draggable": {
                "description": "设置选中文本拖拽效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "选中文本拖拽效果。",
                        "default": False
                    }
                }
            },
            "font": {
                "description": "设置文本样式。包括字体大小、字体粗细、字体族和字体风格。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "文本样式。"
                    }
                }
            },
            "textShadow": {
                "description": "设置文字阴影效果。",
                "params": {
                    "value": {
                        "type": ["ShadowOptions", "Array<ShadowOptions>"],
                        "required": True,
                        "description": "文字阴影效果。"
                    }
                }
            },
            "heightAdaptivePolicy": {
                "description": "设置文本自适应高度的方式。",
                "params": {
                    "value": {
                        "type": "TextHeightAdaptivePolicy",
                        "required": True,
                        "description": "文本自适应高度的方式。"
                    }
                }
            },
            "textIndent": {
                "description": "设置首行文本缩进。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "首行文本缩进。",
                        "default": 0
                    }
                }
            },
            "wordBreak": {
                "description": "设置断行规则。",
                "params": {
                    "value": {
                        "type": "WordBreak",
                        "required": True,
                        "description": "断行规则。",
                        "default": "WordBreak.BREAK_WORD"
                    }
                }
            },
            "selection": {
                "description": "设置选中区域。选中区域高亮且显示手柄和文本选择菜单。",
                "params": {
                    "selectionStart": {
                        "type": "number",
                        "required": True,
                        "description": "所选文本的起始位置。",
                        "default": -1
                    },
                    "selectionEnd": {
                        "type": "number",
                        "required": True,
                        "description": "所选文本的结束位置。",
                        "default": -1
                    }
                }
            },
            "ellipsisMode": {
                "description": "设置省略位置。",
                "params": {
                    "value": {
                        "type": "EllipsisMode",
                        "required": True,
                        "description": "省略位置。",
                        "default": "EllipsisMode.END"
                    }
                }
            },
            "enableDataDetector": {
                "description": "设置使能文本识别。",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "required": True,
                        "description": "使能文本识别。",
                        "default": False
                    }
                }
            },
            "dataDetectorConfig": {
                "description": "设置文本识别配置。",
                "params": {
                    "config": {
                        "type": "TextDataDetectorConfig",
                        "required": True,
                        "description": "文本识别配置。"
                    }
                }
            },
            "bindSelectionMenu": {
                "description": "设置自定义选择菜单。",
                "params": {
                    "spanType": {
                        "type": "TextSpanType",
                        "required": True,
                        "description": "文本范围类型。"
                    },
                    "content": {
                        "type": "CustomBuilder",
                        "required": True,
                        "description": "自定义菜单内容。"
                    },
                    "responseType": {
                        "type": "TextResponseType",
                        "required": True,
                        "description": "响应类型。"
                    },
                    "options": {
                        "type": "SelectionMenuOptions",
                        "required": False,
                        "description": "选择菜单选项。"
                    }
                }
            },
            "fontFeature": {
                "description": "设置文字特性效果，比如数字等宽的特性。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "文字特性效果。"
                    }
                }
            },
            "lineSpacing": {
                "description": "设置文本的行间距，设置值不大于0时，取默认值0。",
                "params": {
                    "value": {
                        "type": "LengthMetrics",
                        "required": True,
                        "description": "文本的行间距。"
                    }
                }
            },
            "privacySensitive": {
                "description": "设置是否支持卡片敏感隐私信息。",
                "params": {
                    "supported": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否支持卡片敏感隐私信息。",
                        "default": False
                    }
                }
            },
            "lineBreakStrategy": {
                "description": "设置折行规则。",
                "params": {
                    "strategy": {
                        "type": "LineBreakStrategy",
                        "required": True,
                        "description": "折行规则。"
                    }
                }
            },
            "textSelectable": {
                "description": "设置是否支持文本可选择、可获焦以及Touch后能否获取焦点。",
                "params": {
                    "value": {
                        "type": "TextSelectableMode",
                        "required": True,
                        "description": "文本是否支持可选择、可获焦。",
                        "default": "TextSelectableMode.SELECTABLE_UNFOCUSABLE"
                    }
                }
            }
        },
        "events": {
            "onCopy": {
                "description": "长按文本内部区域弹出剪贴板后，点击剪切板复制按钮，触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "复制的文本内容。"
                    }
                }
            },
            "onTextSelectionChange": {
                "description": "文本选择的位置发生变化时，触发该回调。",
                "params": {
                    "selectionStart": {
                        "type": "number",
                        "required": True,
                        "description": "所选文本的起始位置。"
                    },
                    "selectionEnd": {
                        "type": "number",
                        "required": True,
                        "description": "所选文本的结束位置。"
                    }
                }
            }
        },
        "is_common_attrs": True
    },
    "TextArea": {
        "description": "多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。",
        "interfaces": [
            {
                "description": "TextArea(value?: TextAreaOptions)",
                "params": {
                    "value": {
                        "type": "TextAreaOptions",
                        "required": False,
                        "description": "TextAreaOptions对象，用于配置文本选择器的选项。"
                    }
                }
            }
        ],
        "attributes": {
            "placeholderColor": {
                "description": "placeholderColor(value: ResourceColor)",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "设置placeholder文本颜色。"
                    }
                }
            },
            "placeholderFont": {
                "description": "placeholderFont(value: Font)",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": True,
                        "description": "设置placeholder文本样式，包括字体大小，字体粗细，字体族，字体风格。目前仅支持默认字体族。"
                    }
                }
            },
            "textAlign": {
                "description": "textAlign(value: TextAlign)",
                "params": {
                    "value": {
                        "type": "TextAlign",
                        "required": True,
                        "description": "设置文本在输入框中的水平对齐方式。",
                        "default": "TextAlign.Start"
                    }
                }
            },
            "caretColor": {
                "description": "caretColor(value: ResourceColor)",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "设置输入框光标颜色。"
                    }
                }
            },
            "inputFilter": {
                "description": "inputFilter(value: ResourceStr, error?: (value: string) => void)",
                "params": {
                    "value": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "正则表达式。"
                    },
                    "error": {
                        "type": "(value: string) => void",
                        "required": False,
                        "description": "正则匹配失败时，返回被过滤的内容。"
                    }
                }
            },
            "copyOption": {
                "description": "copyOption(value: CopyOptions)",
                "params": {
                    "value": {
                        "type": "CopyOptions",
                        "required": True,
                        "description": "输入的文本是否可复制。",
                        "default": "CopyOptions.LocalDevice"
                    }
                }
            },
            "maxLength": {
                "description": "maxLength(value: number)",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "设置文本的最大输入字符数。"
                    }
                }
            },
            "showCounter": {
                "description": "showCounter(value: boolean, options?: InputCounterOptions)",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "设置当通过InputCounterOptions输入的字符数超过阈值时显示计数器。"
                    },
                    "options": {
                        "type": "InputCounterOptions",
                        "required": False,
                        "description": "选中文字时的配置。"
                    }
                }
            },
            "style": {
                "description": "style(value: TextContentStyle)",
                "params": {
                    "value": {
                        "type": "TextContentStyle",
                        "required": True,
                        "description": "设置文本框多态样式，内联输入风格只支持TextAreaType.Normal类型。"
                    }
                }
            },
            "enableKeyboardOnFocus": {
                "description": "enableKeyboardOnFocus(value: boolean)",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "设置TextArea通过点击以外的方式获焦时，是否绑定输入法。",
                        "default": True
                    }
                }
            },
            "selectionMenuHidden": {
                "description": "selectionMenuHidden(value: boolean)设置长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。",
                        "default": False
                    }
                }
            },
            "barState": {
                "description": "barState(value: BarState)",
                "params": {
                    "value": {
                        "type": "BarState",
                        "required": True,
                        "description": "设置输入框编辑态时滚动条的显示模式。",
                        "default": "BarState.Auto"
                    }
                }
            },
            "maxLines": {
                "description": "maxLines(value: number)",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "配置textOverflow一起使用时，maxlines为可显示行数，超出截断；未配置textOverflow时，内联模式获焦状态下内容超出maxlines时，文本可滚动显示，内联模式非获焦状态下不生效maxlines，非内联模式按行截断。",
                        "default": 3
                    }
                }
            },
            "customKeyboard": {
                "description": "customKeyboard(value: CustomBuilder, options?: KeyboardOptions)",
                "params": {
                    "value": {
                        "type": "CustomBuilder",
                        "required": True,
                        "description": "设置自定义键盘。"
                    },
                    "options": {
                        "type": "KeyboardOptions",
                        "required": False,
                        "description": "设置自定义键盘是否支持避让功能。"
                    }
                }
            },
            "type": {
                "description": "type(value: TextAreaType)",
                "params": {
                    "value": {
                        "type": "TextAreaType",
                        "required": True,
                        "description": "设置输入框类型。",
                        "default": "TextAreaType.Normal"
                    }
                }
            },
            "enableAutoFill": {
                "description": "enableAutoFill(value: boolean)",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "设置是否启用自动填充。",
                        "default": True
                    }
                }
            },
            "contentType": {
                "description": "contentType(contentType: ContentType)",
                "params": {
                    "contentType": {
                        "type": "ContentType",
                        "required": True,
                        "description": "设置自动填充类型。"
                    }
                }
            },
            "enterKeyType": {
                "description": "enterKeyType(value: EnterKeyType)",
                "params": {
                    "value": {
                        "type": "EnterKeyType",
                        "required": True,
                        "description": "设置输入法回车键类型。",
                        "default": "EnterKeyType.NEW_LINE"
                    }
                }
            },
            "lineHeight": {
                "description": "lineHeight(value: number | string | Resource)",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。"
                    }
                }
            },
            "decoration": {
                "description": "decoration(value: TextDecorationOptions)",
                "params": {
                    "value": {
                        "type": "TextDecorationOptions",
                        "required": True,
                        "description": "设置文本装饰线类型样式及其颜色。",
                        "default": {
                            "type": "TextDecorationType.None",
                            "color": "Color.Black",
                            "style": "TextDecorationStyle.SOLID"
                        }
                    }
                }
            },
            "letterSpacing": {
                "description": "letterSpacing(value: number | string | Resource)",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "设置文本字符间距。设置该值为百分比时，按默认值显示。设置该值为0时，按默认值显示。"
                    }
                }
            },
            "wordBreak": {
                "description": "wordBreak(value: WordBreak)",
                "params": {
                    "value": {
                        "type": "WordBreak",
                        "required": True,
                        "description": "设置文本断行规则。该属性对placeholder文本无效。",
                        "default": "WordBreak.BREAK_WORD"
                    }
                }
            },
            "selectedBackgroundColor": {
                "description": "selectedBackgroundColor(value: ResourceColor)",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。"
                    }
                }
            },
            "caretStyle": {
                "description": "caretStyle(value: CaretStyle)",
                "params": {
                    "value": {
                        "type": "CaretStyle",
                        "required": True,
                        "description": "设置光标风格。"
                    }
                }
            },
            "textIndent": {
                "description": "textIndent(value: Dimension)",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "设置首行文本缩进。"
                    }
                }
            },
            "textOverflow": {
                "description": "textOverflow(value: TextOverflow)",
                "params": {
                    "value": {
                        "type": "TextOverflow",
                        "required": True,
                        "description": "设置文本超长时的显示方式。",
                        "default": "TextOverflow.Clip"
                    }
                }
            },
            "minFontSize": {
                "description": "minFontSize(value: number | string | Resource)",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "设置文本最小显示字号。"
                    }
                }
            },
            "maxFontSize": {
                "description": "maxFontSize(value: number | string | Resource)",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "设置文本最大显示字号。"
                    }
                }
            },
            "heightAdaptivePolicy": {
                "description": "heightAdaptivePolicy(value: TextHeightAdaptivePolicy)",
                "params": {
                    "value": {
                        "type": "TextHeightAdaptivePolicy",
                        "required": True,
                        "description": "设置文本自适应高度的方式。"
                    }
                }
            },
            "lineSpacing": {
                "description": "lineSpacing(value: LengthMetrics)",
                "params": {
                    "value": {
                        "type": "LengthMetrics",
                        "required": True,
                        "description": "设置文本的行间距，设置值不大于0时，取默认值0。"
                    }
                }
            },
            "lineBreakStrategy": {
                "description": "lineBreakStrategy(strategy: LineBreakStrategy)",
                "params": {
                    "strategy": {
                        "type": "LineBreakStrategy",
                        "required": True,
                        "description": "设置折行规则。该属性在wordBreak不等于breakAll的时候生效，不支持连词符。"
                    }
                }
            },
            "editMenuOptions": {
                "description": "editMenuOptions12+(value: EditMenuOptions)",
                "params": {
                    "value": {
                        "type": "EditMenuOptions",
                        "required": True,
                        "description": "设置编辑菜单选项。"
                    }
                }
            },
            "enablePreviewText": {
                "description": "enablePreviewText12+(value: boolean)",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "设置是否启用预览文本。",
                        "default": True
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "onChange(callback: (value: string) => void)",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前输入的文本内容。"
                    }
                }
            },
            "onEditChange": {
                "description": "onEditChange(callback: (isEditing: boolean) => void)",
                "params": {
                    "isEditing": {
                        "type": "boolean",
                        "required": True,
                        "description": "为true表示正在输入。"
                    }
                }
            },
            "onCopy": {
                "description": "onCopy(callback: (value: string) => void)",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "复制的文本内容。"
                    }
                }
            },
            "onCut": {
                "description": "onCut(callback: (value: string) => void)",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "剪切的文本内容。"
                    }
                }
            },
            "onPaste": {
                "description": "onPaste(callback: (value: string, event: PasteEvent) => void)",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "粘贴的文本内容。"
                    },
                    "event": {
                        "type": "PasteEvent",
                        "required": False,
                        "description": "用户自定义的粘贴事件。"
                    }
                }
            },
            "onTextSelectionChange": {
                "description": "onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void)",
                "params": {
                    "selectionStart": {
                        "type": "number",
                        "required": True,
                        "description": "所选文本的起始位置，文字的起始位置为0。"
                    },
                    "selectionEnd": {
                        "type": "number",
                        "required": True,
                        "description": "所选文本的结束位置。"
                    }
                }
            },
            "onContentScroll": {
                "description": "onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void)",
                "params": {
                    "totalOffsetX": {
                        "type": "number",
                        "required": True,
                        "description": "文本在内容区的横坐标偏移，单位px。"
                    },
                    "totalOffsetY": {
                        "type": "number",
                        "required": True,
                        "description": "文本在内容区的纵坐标偏移，单位px。"
                    }
                }
            },
            "onSubmit": {
                "description": "onSubmit(callback: (enterKey: EnterKeyType) => void)",
                "params": {
                    "enterKey": {
                        "type": "EnterKeyType",
                        "required": True,
                        "description": "输入法回车键类型，类型为EnterKeyType.NEW_LINE时不触发onSubmit。"
                    }
                }
            },
            "onWillInsert": {
                "description": "onWillInsert(callback: Callback<InsertValue, boolean>)",
                "params": {
                    "callback": {
                        "type": "Callback<InsertValue, boolean>",
                        "required": True,
                        "description": "在将要输入时调用的回调。在返回true时，表示正常插入，返回false时，表示不插入。在预上屏操作时，该回调不触发。仅支持系统输入法输入的场景。"
                    }
                }
            },
            "onDidInsert": {
                "description": "onDidInsert(callback: Callback<InsertValue>)",
                "params": {
                    "callback": {
                        "type": "Callback<InsertValue>",
                        "required": True,
                        "description": "在输入完成时调用的回调。仅支持系统输入法输入的场景。"
                    }
                }
            },
            "onWillDelete": {
                "description": "onWillDelete(callback: Callback<DeleteValue, boolean>)",
                "params": {
                    "callback": {
                        "type": "Callback<DeleteValue, boolean>",
                        "required": True,
                        "description": "在将要删除时调用的回调。在返回true时，表示正常删除，返回false时，表示不删除。在预上屏删除操作时，该回调不触发。仅支持系统输入法输入的场景。"
                    }
                }
            },
            "onDidDelete": {
                "description": "onDidDelete(callback: Callback<DeleteValue>)",
                "params": {
                    "callback": {
                        "type": "Callback<DeleteValue>",
                        "required": True,
                        "description": "在删除完成时调用的回调。仅支持系统输入法输入的场景。"
                    }
                }
            }
        },
        "examples": [
            """// TextArea基本使用示例\n\n// 定义一个TextAreaExample结构体，展示TextArea的基本用法\n@Entry\n@Component\nstruct TextAreaExample {\n  // 定义状态变量text，用于存储TextArea中的文本内容\n  @State text: string = ''\n  // 定义状态变量positionInfo，用于存储光标位置信息\n  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 }\n  // 创建TextAreaController实例，用于控制TextArea\n  controller: TextAreaController = new TextAreaController()\n\n  // 构建TextAreaExample的UI界面\n  build() {\n    // 创建一个Column布局\n    Column() {\n      // 创建一个TextArea组件\n      TextArea({\n        text: this.text, // 绑定TextArea的文本内容\n        placeholder: 'The text area can hold an unlimited amount of text. input your word...', // 设置TextArea的占位符文本\n        controller: this.controller // 绑定TextArea的控制器\n      })\n        .placeholderFont({ size: 16, weight: 400 }) // 设置占位符文本的字体样式\n        .width(336) // 设置TextArea的宽度\n        .height(56) // 设置TextArea的高度\n        .margin(20) // 设置TextArea的外边距\n        .fontSize(16) // 设置文本字体大小\n        .fontColor('#182431') // 设置文本字体颜色\n        .backgroundColor('#FFFFFF') // 设置背景颜色\n        .onChange((value: string) => {\n          this.text = value // 当TextArea内容发生变化时，更新状态变量text的值\n        })\n      // 显示当前TextArea的文本内容\n      Text(this.text)\n      // 创建一个按钮，点击后将光标位置设置到第一个字符后\n      Button('Set caretPosition 1')\n        .backgroundColor('#007DFF')\n        .margin(15)\n        .onClick(() => {\n          // 设置光标位置到第一个字符后\n          this.controller.caretPosition(1)\n        })\n      // 创建一个按钮，点击后获取光标位置信息\n      Button('Get CaretOffset')\n        .backgroundColor('#007DFF')\n        .margin(15)\n        .onClick(() => {\n          this.positionInfo = this.controller.getCaretOffset() // 获取光标位置信息并存储到positionInfo变量中\n        })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5') // 设置Column布局的宽度、高度和背景颜色\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct TextAreaExample {\n  @State text: string = ''\n  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 }\n  controller: TextAreaController = new TextAreaController()\n\n  build() {\n    Column() {\n      TextArea({\n        text: this.text,\n        placeholder: 'The text area can hold an unlimited amount of text. input your word...',\n        controller: this.controller\n      })\n        .placeholderFont({ size: 16, weight: 400 })\n        .width(336)\n        .height(56)\n        .margin(20)\n        .fontSize(16)\n        .fontColor('#182431')\n        .backgroundColor('#FFFFFF')\n        .onChange((value: string) => {\n          this.text = value\n        })\n      Text(this.text)\n      Button('Set caretPosition 1')\n        .backgroundColor('#007DFF')\n        .margin(15)\n        .onClick(() => {\n          // 设置光标位置到第一个字符后\n          this.controller.caretPosition(1)\n        })\n      Button('Get CaretOffset')\n        .backgroundColor('#007DFF')\n        .margin(15)\n        .onClick(() => {\n          this.positionInfo = this.controller.getCaretOffset()\n        })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            """// TextArea绑定自定义键盘使用示例\n\n// TextAreaExample结构体定义\n@Entry\n@Component\nstruct TextAreaExample {\n  // TextArea控制器\n  controller: TextAreaController = new TextAreaController()\n  // 输入值\n  @State inputValue: string = ""\n\n  // 自定义键盘组件构建器\n  @Builder CustomKeyboardBuilder() {\n    // 自定义键盘布局\n    Column() {\n      // 关闭键盘按钮\n      Button('x').onClick(() => {\n        // 关闭自定义键盘\n        this.controller.stopEditing()\n      })\n      // 数字和符号键盘\n      Grid() {\n        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {\n          GridItem() {\n            Button(item + "")\n              .width(110).onClick(() => {\n              // 点击键盘按钮，更新输入值\n              this.inputValue += item\n            })\n          }\n        })\n      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)\n    }.backgroundColor(Color.Gray)\n  }\n\n  // 构建函数\n  build() {\n    // 主布局\n    Column() {\n      // 文本输入框，绑定控制器和输入值\n      TextArea({ controller: this.controller, text: this.inputValue})\n        // 绑定自定义键盘\n        .customKeyboard(this.CustomKeyboardBuilder()).margin(10).border({ width: 1 })\n        .height(200)\n    }\n  }\n}\n```\n\n在上述代码中：\n- `TextAreaExample`结构体定义了一个示例，展示了如何使用自定义键盘绑定到文本输入框。\n- `controller`是TextArea的控制器，用于控制文本输入框的行为。\n- `inputValue`是文本输入框的值，用于存储用户输入的内容。\n- `CustomKeyboardBuilder`是自定义键盘组件的构建器，包含关闭键盘按钮和数字/符号键盘布局。\n- 点击数字/符号键盘按钮会将对应的数字或符号追加到输入值中。\n- `build`函数构建了整体布局，包括TextArea和自定义键盘的绑定。\n// xxx.ets\n@Entry\n@Component\nstruct TextAreaExample {\n  controller: TextAreaController = new TextAreaController()\n  @State inputValue: string = ""\n\n  // 自定义键盘组件\n  @Builder CustomKeyboardBuilder() {\n    Column() {\n      Button('x').onClick(() => {\n        // 关闭自定义键盘\n        this.controller.stopEditing()\n      })\n      Grid() {\n        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {\n          GridItem() {\n            Button(item + "")\n              .width(110).onClick(() => {\n              this.inputValue += item\n            })\n          }\n        })\n      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)\n    }.backgroundColor(Color.Gray)\n  }\n\n  build() {\n    Column() {\n      TextArea({ controller: this.controller, text: this.inputValue})\n        // 绑定自定义键盘\n        .customKeyboard(this.CustomKeyboardBuilder()).margin(10).border({ width: 1 })\n        .height(200)\n    }\n  }\n}"""
            """// TextArea计数器使用示例\n\n// TextAreaExample结构体定义了一个TextArea示例，包括文本输入框和字符计数器功能。\n// 用户可以输入文本，并根据设定的最大字符限制数进行计数显示。\n// 当输入字符数达到最大字符限制数的50%时，字符计数器会显示。\n// 用户可以选择是否高亮显示超出字符限制的文本框边框。\n// 文本框内容变化时，会触发onChange事件，更新text变量的值。\n\n@Entry\n@Component\nstruct TextAreaExample {\n  @State text: string = '' // 用于存储文本框中的文本内容\n  controller: TextAreaController = new TextAreaController() // 创建一个文本框控制器\n\n  build() {\n    Column() {\n      TextArea({ text: this.text, controller: this.controller }) // 创建一个文本输入框\n        .placeholderFont({ size: 16, weight: 400 }) // 设置文本框的占位字体大小和粗细\n        .width(336) // 设置文本框宽度\n        .height(56) // 设置文本框高度\n        .maxLength(6) // 设置文本框最大字符限制数为6\n        .showCounter(true, { thresholdPercentage: 50, highlightBorder: true })\n        // 显示字符计数器，当输入字符数达到最大字符限制数的50%时显示，可选择是否高亮显示超出字符限制的文本框边框\n        .onChange((value: string) => {\n          this.text = value // 文本框内容变化时更新text变量的值\n        })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5') // 设置Column的宽度、高度和背景颜色\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct TextAreaExample {\n  @State text: string = ''\n  controller: TextAreaController = new TextAreaController()\n\n  build() {\n    Column() {\n      TextArea({ text: this.text, controller: this.controller })\n        .placeholderFont({ size: 16, weight: 400 })\n        .width(336)\n        .height(56)\n        .maxLength(6)\n        .showCounter(true, { thresholdPercentage: 50, highlightBorder: true })\n        //计数器显示效果为用户当前输入字符数/最大字符限制数。最大字符限制数通过maxLength()接口设置。\n        //如果用户当前输入字符数达到最大字符限制乘50%（thresholdPercentage）。字符计数器显示。\n        //用户设置highlightBorder为false时，配置取消红色边框。不设置此参数时，默认为true。\n        .onChange((value: string) => {\n          this.text = value\n        })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            """fontFeature属性使用示例，对比了fontFeature使用ss01属性和不使用ss01属性的效果。\n\n@Entry\n@Component\nstruct textArea {\n  @State text1: string = 'This is ss01 on : 0123456789'\n  @State text2: string = 'This is ss01 off: 0123456789'\n\n  build() {\n    Column(){\n      // 创建一个文本区域，展示启用ss01属性的效果\n      TextArea({text: this.text1})\n        .fontSize(20)\n        .margin({top:200})\n        .fontFeature(""ss01" on") // 启用ss01属性，展示效果\n      // 创建另一个文本区域，展示禁用ss01属性的效果\n      TextArea({text : this.text2})\n        .margin({top:10})\n        .fontSize(20)\n        .fontFeature(""ss01" off") // 禁用ss01属性，展示效果\n    }\n    .width("90%")\n    .margin("5%")\n  }\n}\n```\n\n```java\n// 创建一个文本区域，展示启用ss01属性的效果\n// 设置字体大小为20，上边距为200\n// 启用ss01属性，展示效果为"This is ss01 on : 0123456789"\nTextArea({text: this.text1})\n  .fontSize(20)\n  .margin({top:200})\n  .fontFeature(""ss01" on")\n\n// 创建另一个文本区域，展示禁用ss01属性的效果\n// 上边距为10，字体大小为20\n// 禁用ss01属性，展示效果为"This is ss01 off: 0123456789"\nTextArea({text : this.text2})\n  .margin({top:10})\n  .fontSize(20)\n  .fontFeature(""ss01" off")\n```\n@Entry\n@Component\nstruct textArea {\n  @State text1: string = 'This is ss01 on : 0123456789'\n  @State text2: string = 'This is ss01 off: 0123456789'\n\n  build() {\n    Column(){\n      TextArea({text: this.text1})\n        .fontSize(20)\n        .margin({top:200})\n        .fontFeature("\\"ss01\\" on")\n      TextArea({text : this.text2})\n        .margin({top:10})\n        .fontSize(20)\n        .fontFeature("\\"ss01\\" off")\n    }\n    .width("90%")\n    .margin("5%")\n  }\n}"""
            """// 自定义键盘弹出避让示例\n// 该示例展示了如何实现自定义键盘的弹出并避让输入框的功能\n\n// TextAreaExample结构体定义\n@Entry\n@Component\nstruct TextAreaExample {\n  controller: TextAreaController = new TextAreaController() // TextArea控制器\n  @State inputValue: string = "" // 输入框的值\n  @State height1:string|number = '80%' // 高度1\n  @State height2:number = 100 // 高度2\n  @State supportAvoidance:boolean = true; // 是否支持避让\n\n  // 自定义键盘组件\n  @Builder CustomKeyboardBuilder() {\n    Column() {\n      Row(){\n        Button('x').onClick(() => {\n          // 关闭自定义键盘\n          this.controller.stopEditing()\n        }).margin(10)\n      }\n      Grid() {\n        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {\n          GridItem() {\n            Button(item + "")\n              .width(110).onClick(() => {\n              this.inputValue += item\n            })\n          }\n        })\n      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)\n    }.backgroundColor(Color.Gray)\n  }\n\n  // 构建函数\n  build() {\n    Column() {\n      Row(){\n        Button("20%")\n          .fontSize(24)\n          .onClick(()=>{\n            this.height1 = "20%"\n          })\n        Button("80%")\n          .fontSize(24)\n          .margin({left:20})\n          .onClick(()=>{\n            this.height1 = "80%"\n          })\n      }\n      .justifyContent(FlexAlign.Center)\n      .alignItems(VerticalAlign.Bottom)\n      .height(this.height1)\n      .width("100%")\n      .padding({bottom:50})\n      TextArea({ controller: this.controller, text: this.inputValue})\n        .height(100)\n        // 绑定自定义键盘，支持避让\n        .customKeyboard(this.CustomKeyboardBuilder(),{ supportAvoidance: this.supportAvoidance }).margin(10).border({ width: 1 })\n        // .height(200)\n    }\n  }\n}\n```\n@Entry\n@Component\nstruct TextAreaExample {\n  controller: TextAreaController = new TextAreaController()\n  @State inputValue: string = ""\n  @State height1:string|number = '80%'\n  @State height2:number = 100\n  @State supportAvoidance:boolean = true;\n\n  // 自定义键盘组件\n  @Builder CustomKeyboardBuilder() {\n    Column() {\n      Row(){\n        Button('x').onClick(() => {\n          // 关闭自定义键盘\n          this.controller.stopEditing()\n        }).margin(10)\n      }\n      Grid() {\n        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {\n          GridItem() {\n            Button(item + "")\n              .width(110).onClick(() => {\n              this.inputValue += item\n            })\n          }\n        })\n      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)\n    }.backgroundColor(Color.Gray)\n  }\n\n  build() {\n    Column() {\n      Row(){\n        Button("20%")\n          .fontSize(24)\n          .onClick(()=>{\n            this.height1 = "20%"\n          })\n        Button("80%")\n          .fontSize(24)\n          .margin({left:20})\n          .onClick(()=>{\n            this.height1 = "80%"\n          })\n      }\n      .justifyContent(FlexAlign.Center)\n      .alignItems(VerticalAlign.Bottom)\n      .height(this.height1)\n      .width("100%")\n      .padding({bottom:50})\n      TextArea({ controller: this.controller, text: this.inputValue})\n        .height(100)\n        // 绑定自定义键盘\n        .customKeyboard(this.CustomKeyboardBuilder(),{ supportAvoidance: this.supportAvoidance }).margin(10).border({ width: 1 })\n        // .height(200)\n    }\n  }\n}"""
            """// 示例代码展示了使用不同的LineBreakStrategy设置对文本显示效果的影响\n\n// 定义一个结构体TextExample1，包含了三个TextArea组件，分别展示了不同的LineBreakStrategy效果\n@Entry\n@Component\nstruct TextExample1 {\n  // 初始化一个长文本内容\n  @State message1: string = "They can be classified as built-in components–those directly provided by the ArkUI framework and custom components – those defined by developers" +\n    "The built-in components include buttons radio buttonsprogress indicators and text You can set the rendering effectof thesecomponents in method chaining mode," +\n    "page components are divided into independent UI units to implementindependent creation development and reuse of different units on pages making pages more engineering-oriented.";\n\n  // 构建UI界面\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {\n      // 第一个TextArea展示LineBreakStrategy.GREEDY效果\n      Text('LineBreakStrategy.GREEDY').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextArea({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .lineBreakStrategy(LineBreakStrategy.GREEDY) // 设置为GREEDY模式，文本显示效果为贪婪模式换行\n      // 第二个TextArea展示LineBreakStrategy.HIGH_QUALITY效果\n      Text('LineBreakStrategy.HIGH_QUALITY').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextArea({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .lineBreakStrategy(LineBreakStrategy.HIGH_QUALITY) // 设置为HIGH_QUALITY模式，文本显示效果为高质量换行\n      // 第三个TextArea展示LineBreakStrategy.BALANCED效果\n      Text('LineBreakStrategy.BALANCED').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextArea({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .lineBreakStrategy(LineBreakStrategy.BALANCED) // 设置为BALANCED模式，文本显示效果为平衡换行\n    }.height(700).width(370).padding({ left: 35, right: 35, top: 35 }) // 设置整体布局样式\n  }\n}\n```\n@Entry\n@Component\nstruct TextExample1 {\n  @State message1: string = "They can be classified as built-in components–those directly provided by the ArkUI framework and custom components – those defined by developers" +\n    "The built-in components include buttons radio buttonsprogress indicators and text You can set the rendering effectof thesecomponents in method chaining mode," +\n    "page components are divided into independent UI units to implementindependent creation development and reuse of different units on pages making pages more engineering-oriented.";\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {\n      Text('LineBreakStrategy.GREEDY').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextArea({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .lineBreakStrategy(LineBreakStrategy.GREEDY)\n      Text('LineBreakStrategy.HIGH_QUALITY').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextArea({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .lineBreakStrategy(LineBreakStrategy.HIGH_QUALITY)\n      Text('LineBreakStrategy.BALANCED').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextArea({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .lineBreakStrategy(LineBreakStrategy.BALANCED)\n    }.height(700).width(370).padding({ left: 35, right: 35, top: 35 })\n  }\n}"""
            """// 该示例展示输入框支持插入和删除回调功能\n\n// 定义TextAreaExample组件\n@Entry\n@Component\nstruct TextAreaExample {\n  // 定义状态变量\n  @State insertValue: string = "" // 用于存储插入的文本值\n  @State deleteValue: string = "" // 用于存储删除的文本值\n  @State insertOffset: number = 0 // 用于存储插入文本的偏移量\n  @State deleteOffset: number = 0 // 用于存储删除文本的偏移量\n  @State deleteDirection: number = 0 // 用于存储删除文本的方向\n\n  // 构建TextAreaExample组件\n  build() {\n    Row() {\n      Column() {\n        // 创建支持插入回调的TextArea组件\n        TextArea({ text: "TextArea支持插入回调文本" })\n          .width(300)\n          .height(60)\n          // 插入文本前的回调函数\n          .onWillInsert((info: InsertValue) => {\n            this.insertValue = info.insertValue\n            return true;\n          })\n          // 插入文本后的回调函数\n          .onDidInsert((info: InsertValue) => {\n            this.insertOffset = info.insertOffset\n          })\n\n        // 显示插入文本和偏移量信息\n        Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(30)\n\n        // 创建支持删除回调的TextArea组件\n        TextArea({ text: "TextArea支持删除回调文本b" })\n          .width(300)\n          .height(60)\n          // 删除文本前的回调函数\n          .onWillDelete((info: DeleteValue) => {\n            this.deleteValue = info.deleteValue\n            info.direction\n            return true;\n          })\n          // 删除文本后的回调函数\n          .onDidDelete((info: DeleteValue) => {\n            this.deleteOffset = info.deleteOffset\n            this.deleteDirection = info.direction\n          })\n\n        // 显示删除文本、偏移量和方向信息\n        Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(30)\n        Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(30)\n\n      }.width('100%')\n    }\n    .height('100%')\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct TextAreaExample {\n  @State insertValue: string = ""\n  @State deleteValue: string = ""\n  @State insertOffset: number = 0\n  @State deleteOffset: number = 0\n  @State deleteDirection: number = 0\n\n  build() {\n    Row() {\n      Column() {\n        TextArea({ text: "TextArea支持插入回调文本" })\n          .width(300)\n          .height(60)\n          .onWillInsert((info: InsertValue) => {\n            this.insertValue = info.insertValue\n            return true;\n          })\n          .onDidInsert((info: InsertValue) => {\n            this.insertOffset = info.insertOffset\n          })\n\n        Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(30)\n\n        TextArea({ text: "TextArea支持删除回调文本b" })\n          .width(300)\n          .height(60)\n          .onWillDelete((info: DeleteValue) => {\n            this.deleteValue = info.deleteValue\n            info.direction\n            return true;\n          })\n          .onDidDelete((info: DeleteValue) => {\n            this.deleteOffset = info.deleteOffset\n            this.deleteDirection = info.direction\n          })\n\n        Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(30)\n        Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(30)\n\n      }.width('100%')\n    }\n    .height('100%')\n  }\n}"""
            """// xxx.ets\n@Entry\n@Component\nstruct TextAreaExample {\n  @State text: string = 'TextArea editMenuOptions'\n\n  // 创建自定义菜单项的文本内容、图标、回调方法\n  onCreateMenu(menuItems: Array<TextMenuItem>) {\n    menuItems.forEach((value, index) => {\n      value.icon = $r('app.media.startIcon')\n      if (value.id.equals(TextMenuItemId.COPY)) {\n        value.content = "复制change"\n      }\n      if (value.id.equals(TextMenuItemId.SELECT_ALL)) {\n        value.content = "全选change"\n      }\n    })\n    let item1: TextMenuItem = {\n      content: 'custom1',\n      icon: $r('app.media.startIcon'),\n      id: TextMenuItemId.of('custom1'),\n    }\n    let item2: TextMenuItem = {\n      content: 'custom2',\n      id: TextMenuItemId.of('custom2'),\n      icon: $r('app.media.startIcon'),\n    }\n    menuItems.push(item1)\n    menuItems.unshift(item2)\n    return menuItems\n  }\n\n  // 构建TextArea组件及设置自定义菜单扩展项的效果\n  build() {\n    Column() {\n      TextArea({ text: this.text })\n        .width('95%')\n        .height(56)\n        .editMenuOptions({\n          onCreateMenu: this.onCreateMenu, onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {\n            // 拦截自定义菜单项custom2的点击事件\n            if (menuItem.id.equals(TextMenuItemId.of("custom2"))) {\n              console.log("拦截 id: custom2 start:" + textRange.start + "; end:" + textRange.end)\n              return true;\n            }\n            // 拦截复制操作的点击事件\n            if (menuItem.id.equals(TextMenuItemId.COPY)) {\n              console.log("拦截 COPY start:" + textRange.start + "; end:" + textRange.end)\n              return true;\n            }\n            // 不拦截全选操作的点击事件\n            if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {\n              console.log("不拦截 SELECT_ALL start:" + textRange.start + "; end:" + textRange.end)\n              return false;\n            }\n            return false;\n          }\n        })\n        .margin({ top: 100 })\n    }\n    .width("90%")\n    .margin("5%")\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct TextAreaExample {\n  @State text: string = 'TextArea editMenuOptions'\n\n  onCreateMenu(menuItems: Array<TextMenuItem>) {\n    menuItems.forEach((value, index) => {\n      value.icon = $r('app.media.startIcon')\n      if (value.id.equals(TextMenuItemId.COPY)) {\n        value.content = "复制change"\n      }\n      if (value.id.equals(TextMenuItemId.SELECT_ALL)) {\n        value.content = "全选change"\n      }\n    })\n    let item1: TextMenuItem = {\n      content: 'custom1',\n      icon: $r('app.media.startIcon'),\n      id: TextMenuItemId.of('custom1'),\n    }\n    let item2: TextMenuItem = {\n      content: 'custom2',\n      id: TextMenuItemId.of('custom2'),\n      icon: $r('app.media.startIcon'),\n    }\n    menuItems.push(item1)\n    menuItems.unshift(item2)\n    return menuItems\n  }\n\n  build() {\n    Column() {\n      TextArea({ text: this.text })\n        .width('95%')\n        .height(56)\n        .editMenuOptions({\n          onCreateMenu: this.onCreateMenu, onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {\n            if (menuItem.id.equals(TextMenuItemId.of("custom2"))) {\n              console.log("拦截 id: custom2 start:" + textRange.start + "; end:" + textRange.end)\n              return true;\n            }\n            if (menuItem.id.equals(TextMenuItemId.COPY)) {\n              console.log("拦截 COPY start:" + textRange.start + "; end:" + textRange.end)\n              return true;\n            }\n            if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {\n              console.log("不拦截 SELECT_ALL start:" + textRange.start + "; end:" + textRange.end)\n              return false;\n            }\n            return false;\n          }\n        })\n        .margin({ top: 100 })\n    }\n    .width("90%")\n    .margin("5%")\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "TextClock": {
        "description": "TextClock组件通过文本将当前系统时间显示在设备上。支持不同时区的时间显示，最高精度到秒级。",
        "interfaces": [
            {
                "description": "TextClock(options?: { timeZoneOffset?: number, controller?: TextClockController })",
                "params": {
                    "timeZoneOffset": {
                        "type": "number",
                        "required": False,
                        "description": "设置时区偏移量。取值范围为[-14, 12]，表示东十二区到西十二区，其中负值表示东时区，正值表示西时区。"
                    },
                    "controller": {
                        "type": "TextClockController",
                        "required": False,
                        "description": "绑定一个控制器，用来控制文本时钟的状态。"
                    }
                }
            }
        ],
        "attributes": {
            "format": {
                "description": "设置显示时间格式。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "显示时间格式。"
                    }
                }
            },
            "textShadow": {
                "description": "设置文字阴影效果。",
                "params": {
                    "value": {
                        "type": "ShadowOptions | Array<ShadowOptions>",
                        "required": True,
                        "description": "文字阴影效果参数。"
                    }
                }
            },
            "fontFeature": {
                "description": "设置文字特性效果。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "文字特性效果参数。"
                    }
                }
            },
            "contentModifier": {
                "description": "定制TextClock内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<TextClockConfiguration>",
                        "required": True,
                        "description": "在TextClock组件上，定制内容区的方法。\nmodifier: 内容修改器，开发者需要自定义class实现ContentModifier接口。"
                    }
                }
            }
        },
        "events": {
            "onDateChange": {
                "description": "提供时间变化回调，该事件回调间隔为秒。组件不可见时不回调。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "Unix Time Stamp，即自1970年1月1日（UTC）起经过的秒数。"
                    }
                }
            }
        },
        "examples": [
            "/*\n实现思路：\n本示例代码展示了如何使用鸿蒙ArkUI框架创建一个简单的文本时钟应用。应用包含一个文本显示当前累积时间，一个文本时钟显示当前系统时间（东八区，12小时制，精确到秒），以及两个按钮分别用于启动和停止文本时钟。\n\n总体功能与效果描述：\n用户界面包含一个文本显示累积时间，一个文本时钟显示当前时间，以及两个按钮分别用于控制文本时钟的启动和停止。\n*/\n\n@Entry\n@Component\nstruct Second {\n  @State accumulateTime: number = 0\n  // 导入对象，用于控制文本时钟的启动和停止\n  controller: TextClockController = new TextClockController()\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\n      // 显示当前累积时间\n      Text('Current milliseconds is ' + this.accumulateTime)\n        .fontSize(20)\n      \n      // 以12小时制显示东八区的系统时间，精确到秒。\n      TextClock({ timeZoneOffset: -8, controller: this.controller })\n        .format('aa hh:mm:ss')\n        .onDateChange((value: number) => {\n          // 每当时间变化时，更新累积时间\n          this.accumulateTime = value\n        })\n        .margin(20)\n        .fontSize(30)\n      \n      // 启动文本时钟的按钮\n      Button(\"start TextClock\")\n        .margin({ bottom: 10 })\n        .onClick(() => {\n          // 启动文本时钟\n          this.controller.start()\n        })\n      \n      // 停止文本时钟的按钮\n      Button(\"stop TextClock\")\n        .onClick(() => {\n          // 停止文本时钟\n          this.controller.stop()\n        })\n    }\n    .width('100%')\n    .height('100%')\n  }\n}",
            "/*\n实现思路：\n本示例展示了如何使用TextClock组件，并通过设置多个阴影效果来增强文本的视觉效果。通过@State装饰器管理阴影选项的状态，确保在状态变化时能够动态更新UI。\n\n总体功能与效果描述：\n该代码定义了一个TextClock组件，通过设置多个不同颜色和偏移量的阴影，使得文本显示时具有丰富的层次感。\n*/\n\n// TextClockExample.ets\n@Entry\n@Component\nstruct TextClockExample {\n  // 使用@State装饰器定义一个状态变量textShadows，用于存储多个阴影选项\n  @State textShadows : ShadowOptions | Array<ShadowOptions> = [\n    { radius: 10, color: Color.Red, offsetX: 10, offsetY: 0 },\n    { radius: 10, color: Color.Black, offsetX: 20, offsetY: 0 },\n    { radius: 10, color: Color.Brown, offsetX: 30, offsetY: 0 },\n    { radius: 10, color: Color.Green, offsetX: 40, offsetY: 0 },\n    { radius: 10, color: Color.Yellow, offsetX: 100, offsetY: 0 }\n  ]\n\n  build() {\n    Column({ space: 8 }) {\n      // 创建一个TextClock组件，设置字体大小为50，并应用定义的阴影效果\n      TextClock().fontSize(50).textShadow(this.textShadows)\n    }\n  }\n}",
            "/*\n该示例实现了自定义文本时钟样式的功能，自定义样式实现了一个时间选择器组件：通过文本时钟的时区偏移量与UTC秒数，来动态改变时间选择器的选中值，实现时钟效果。同时，根据文本时钟的启动状态，实现文本选择器的12小时制与24小时制的切换。\n实现思路：\n本示例通过定义一个自定义的文本时钟样式类MyTextClockStyle，实现了对TextClock组件的个性化配置。通过使用@Builder装饰器定义构建函数buildTextClock，动态生成包含标题和时间选择器的UI布局。在主组件TextClockExample中，通过@State装饰器管理状态变量，实现对文本时钟的启动和停止控制。\n\n总体功能与效果描述：\n该代码展示了如何使用TextClock组件，并通过自定义样式和控制器实现对文本时钟的个性化配置和操作。用户可以通过按钮控制文本时钟的启动和停止，同时显示当前的时间毫秒数。\n*/\n\n// MyTextClockStyle.ets\nclass MyTextClockStyle implements ContentModifier<TextClockConfiguration> {\n  // 当前时区偏移量，单位为小时\n  currentTimeZoneOffset: number = new Date().getTimezoneOffset() / 60\n  // 标题文本\n  title: string = ''\n\n  // 构造函数，初始化标题文本\n  constructor(title: string) {\n    this.title = title\n  }\n\n  // 应用内容修改器，返回包装的构建函数\n  applyContent(): WrappedBuilder<[TextClockConfiguration]> {\n    return wrapBuilder(buildTextClock)\n  }\n}\n\n// 构建函数，生成包含标题和时间选择器的UI布局\n@Builder\nfunction buildTextClock(config: TextClockConfiguration) {\n  Row() {\n    Column() {\n      // 显示标题文本\n      Text((config.contentModifier as MyTextClockStyle).title)\n        .fontSize(20)\n        .margin(20)\n      // 时间选择器，根据当前时区和配置的时区偏移量计算选中时间\n      TimePicker({\n        selected: (new Date(config.timeValue * 1000 + ((config.contentModifier as MyTextClockStyle).currentTimeZoneOffset - config.timeZoneOffset) * 60 * 60 * 1000)),\n        format: TimePickerFormat.HOUR_MINUTE_SECOND\n      })\n        .useMilitaryTime(!config.started)\n    }\n  }\n}\n\n// TextClockExample.ets\n@Entry\n@Component\nstruct TextClockExample {\n  // 累积时间，单位为秒\n  @State accumulateTime1: number = 0\n  // 时区偏移量，单位为小时\n  @State timeZoneOffset: number = -8\n  // 文本时钟控制器\n  controller1: TextClockController = new TextClockController()\n  controller2: TextClockController = new TextClockController()\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\n      // 显示当前累积时间\n      Text('Current milliseconds is ' + this.accumulateTime1)\n        .fontSize(20)\n        .margin({ top: 20 })\n      // 第一个文本时钟，显示当前时间，并绑定控制器和时区偏移量\n      TextClock({ timeZoneOffset: this.timeZoneOffset, controller: this.controller1 })\n        .format('aa hh:mm:ss')\n        .onDateChange((value: number) => {\n          this.accumulateTime1 = value\n        })\n        .margin(20)\n        .fontSize(30)\n      // 第二个文本时钟，使用自定义样式，并绑定控制器和时区偏移量\n      TextClock({ timeZoneOffset: this.timeZoneOffset, controller: this.controller2 })\n        .format('aa hh:mm:ss')\n        .fontSize(30)\n        .contentModifier(new MyTextClockStyle('ContentModifier:'))\n      // 启动文本时钟的按钮\n      Button(\"start TextClock\")\n        .margin({ top: 20, bottom: 10 })\n        .onClick(() => {\n          this.controller1.start()\n          this.controller2.start()\n        })\n      // 停止文本时钟的按钮\n      Button(\"stop TextClock\")\n        .margin({ bottom: 30 })\n        .onClick(() => {\n          this.controller1.stop()\n          this.controller2.stop()\n        })\n    }\n    .width('100%')\n    .height('100%')\n  }\n}",
            "/*\n该示例演示了dateTimeOptions属性为小时字段增加或去除前导0的功能。24小时制的小时字段默认带有前导0，可通过dateTimeOptions属性去除前导0，12小时制的小时字段默认不带有前导0，可通过dateTimeOptions属性增加前导0。\n实现思路：\n本示例展示了如何使用TextClock组件来显示不同格式的时间。通过设置不同的格式字符串和日期时间选项，实现了24小时制和12小时制的时间显示，并且分别去除了24小时制的前导0和增加了12小时制的前导0。\n\n总体功能与效果描述：\n该代码定义了一个TextClockExample组件，通过两个Row容器分别展示了24小时制和12小时制的时间显示效果。每个Row容器包含一个描述文本和一个TextClock组件，通过设置不同的格式和选项，实现了所需的时间显示效果。\n*/\n\n// TextClockExample.ets\n@Entry\n@Component\nstruct TextClockExample {\n  build() {\n    Column({ space: 8 }) {\n      Row() {\n        // 描述文本，说明显示效果\n        Text(\"24小时制去除前导0：\")\n          .fontSize(20)\n        // TextClock组件，显示24小时制时间，去除前导0\n        TextClock()\n          .fontSize(20)\n          .format(\"HH:mm:ss\")\n          .dateTimeOptions({hour: \"numeric\"})\n      }\n      Row() {\n        // 描述文本，说明显示效果\n        Text(\"12小时制增加前导0：\")\n          .fontSize(20)\n        // TextClock组件，显示12小时制时间，增加前导0\n        TextClock()\n          .fontSize(20)\n          .format(\"aa hh:mm:ss\")\n          .dateTimeOptions({hour: \"2-digit\"})\n      }\n    }\n    .alignItems(HorizontalAlign.Start)\n  }\n}"
        ]

    },
    "TextPicker": {
        "description": "根据range指定的选择范围创建文本选择器。",
        "interfaces": [
            {
                "description": "TextPicker(options?: TextPickerOptions)",
                "params": {
                    "options": {
                        "type": "TextPickerOptions",
                        "required": False,
                        "description": "TextPickerOptions对象，用于配置文本选择器的选项。"
                    }
                }
            }
        ],
        "attributes": {
            "defaultPickerItemHeight": {
                "description": "defaultPickerItemHeight(value: number | string)",
                "params": {
                    "value": {
                        "type": ["number", "string"],
                        "required": True,
                        "description": "Picker各选择项的高度。"
                    }
                }
            },
            "disappearTextStyle": {
                "description": "disappearTextStyle(value: PickerTextStyle)",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。",
                        "default": {
                            "color": "#ff182431",
                            "font": {
                                "size": "14fp",
                                "weight": "FontWeight.Regular"
                            }
                        }
                    }
                }
            },
            "textStyle": {
                "description": "textStyle(value: PickerTextStyle)",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。",
                        "default": {
                            "color": "#ff182431",
                            "font": {
                                "size": "16fp",
                                "weight": "FontWeight.Regular"
                            }
                        }
                    }
                }
            },
            "selectedTextStyle": {
                "description": "selectedTextStyle(value: PickerTextStyle)",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "选中项的文本颜色、字号、字体粗细。",
                        "default": {
                            "color": "#ff007dff",
                            "font": {
                                "size": "20vp",
                                "weight": "FontWeight.Medium"
                            }
                        }
                    }
                }
            },
            "selectedIndex": {
                "description": "selectedIndex(value: number | number[])",
                "params": {
                    "value": {
                        "type": ["number", "number[]"],
                        "required": True,
                        "description": "默认选中项在数组中的索引值。",
                        "default": 0
                    }
                }
            },
            "canLoop": {
                "description": "canLoop(value: boolean)",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否可循环滚动。",
                        "default": True
                    }
                }
            },
            "divider": {
                "description": "divider(value: DividerOptions | null)",
                "params": {
                    "value": {
                        "type": ["DividerOptions", "null"],
                        "required": True,
                        "description": "设置分割线样式，不设置该属性则按“默认值”展示分割线。",
                        "default": {
                            "strokeWidth": "2px",
                            "startMargin": 0,
                            "endMargin": 0,
                            "color": "#33000000"
                        }
                    }
                }
            },
            "gradientHeight": {
                "description": "gradientHeight(value: Dimension)",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "设置渐隐效果高度，不设置该属性则显示默认渐隐效果。",
                        "default": "36vp"
                    }
                }
            }
        },
        "events": {

            "onChange": {
                "description": "onChange(callback: (value: string | string[], index: number | number[]) => void)",
                "params": {
                    "value": {
                        "type": ["string", "string[]"],
                        "required": True,
                        "description": "当前选中项的文本。多列的情况，value为数组类型。"
                    },
                    "index": {
                        "type": ["number", "number[]"],
                        "required": True,
                        "description": "当前选中项的索引值。多列的情况，index为数组类型。"
                    }
                }
            }
        },
        "examples": [
            """// xxx.ets\n\n// 定义一个名为bottom的类，包含一个number类型的属性bottom，初始值为50\nclass bottom {\n  bottom:number = 50\n}\n\n// 创建一个bottom类的实例bott\nlet bott:bottom = new bottom()\n\n// 定义一个名为TextPickerExample的结构体，作为示例代码的入口和组件\n@Entry\n@Component\nstruct TextPickerExample {\n  // 私有属性select，初始化为1\n  private select: number = 1\n  // 不同种类水果的数组\n  private apfruits: string[] = ['apple1', 'apple2', 'apple3', 'apple4']\n  private orfruits: string[] = ['orange1', 'orange2', 'orange3', 'orange4']\n  private pefruits: string[] = ['peach1', 'peach2', 'peach3', 'peach4']\n  // 将不同种类水果数组组合成一个二维数组\n  private multi: string[][] = [this.apfruits, this.orfruits, this.pefruits]\n  // 级联选择器的数据结构\n  private cascade: TextCascadePickerRangeContent[] = [\n    {\n      text: '辽宁省',\n      children: [{ text: '沈阳市', children: [{ text: '沈河区' }, { text: '和平区' }, { text: '浑南区' }] },\n        { text: '大连市', children: [{ text: '中山区' }, { text: '金州区' }, { text: '长海县' }] }]\n    },\n    {\n      text: '吉林省',\n      children: [{ text: '长春市', children: [{ text: '南关区' }, { text: '宽城区' }, { text: '朝阳区' }] },\n        { text: '四平市', children: [{ text: '铁西区' }, { text: '铁东区' }, { text: '梨树县' }] }]\n    },\n    {\n      text: '黑龙江省',\n      children: [{ text: '哈尔滨市', children: [{ text: '道里区' }, { text: '道外区' }, { text: '南岗区' }] },\n        { text: '牡丹江市', children: [{ text: '东安区' }, { text: '西安区' }, { text: '爱民区' }] }]\n    }\n  ]\n\n  // 构建函数，用于创建组件结构\n  build() {\n    Column() {\n\n      // 创建一个文本选择器，传入苹果数组和初始选中索引\n      TextPicker({ range: this.apfruits, selected: this.select })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('Picker item changed, value: ' + value + ', index: ' + index)\n        }).margin(bott) // 设置边距为bottom类的实例bott\n\n      // 创建一个文本选择器，传入多列数据\n      TextPicker({ range: this.multi })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('TextPicker 多列:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index))\n        }).margin(bott) // 设置边距为bottom类的实例bott\n\n      // 创建一个文本选择器，传入级联数据\n      TextPicker({ range: this.cascade })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('TextPicker 多列联动:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index))\n        })\n    }\n  }\n}\n```\n// xxx.ets\nclass bottom {\n  bottom:number = 50\n}\nlet bott:bottom = new bottom()\n@Entry\n@Component\nstruct TextPickerExample {\n  private select: number = 1\n  private apfruits: string[] = ['apple1', 'apple2', 'apple3', 'apple4']\n  private orfruits: string[] = ['orange1', 'orange2', 'orange3', 'orange4']\n  private pefruits: string[] = ['peach1', 'peach2', 'peach3', 'peach4']\n  private multi: string[][] = [this.apfruits, this.orfruits, this.pefruits]\n  private cascade: TextCascadePickerRangeContent[] = [\n    {\n      text: '辽宁省',\n      children: [{ text: '沈阳市', children: [{ text: '沈河区' }, { text: '和平区' }, { text: '浑南区' }] },\n        { text: '大连市', children: [{ text: '中山区' }, { text: '金州区' }, { text: '长海县' }] }]\n    },\n    {\n      text: '吉林省',\n      children: [{ text: '长春市', children: [{ text: '南关区' }, { text: '宽城区' }, { text: '朝阳区' }] },\n        { text: '四平市', children: [{ text: '铁西区' }, { text: '铁东区' }, { text: '梨树县' }] }]\n    },\n    {\n      text: '黑龙江省',\n      children: [{ text: '哈尔滨市', children: [{ text: '道里区' }, { text: '道外区' }, { text: '南岗区' }] },\n        { text: '牡丹江市', children: [{ text: '东安区' }, { text: '西安区' }, { text: '爱民区' }] }]\n    }\n  ]\n\n  build() {\n    Column() {\n\n      TextPicker({ range: this.apfruits, selected: this.select })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('Picker item changed, value: ' + value + ', index: ' + index)\n        }).margin(bott)\n\n      TextPicker({ range: this.multi })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('TextPicker 多列:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index))\n        }).margin(bott)\n\n      TextPicker({ range: this.cascade })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('TextPicker 多列联动:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index))\n        })\n    }\n  }\n}"""
            """// xxx.ets\n@Entry\n@Component\nstruct TextPickerExample {\n  private select: number = 1 // 初始化选择项为第2个水果\n  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'] // 水果列表\n\n  build() {\n    Column() {\n      // 创建一个文本选择器，显示水果列表，初始选择项为第2个水果\n      TextPicker({ range: this.fruits, selected: this.select })\n        // 当选择项改变时，输出选择的值和索引\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('Picker item changed, value: ' + value + ', index: ' + index)\n        })\n        // 设置选择项消失时的文本样式为红色，字体大小15，字重较轻\n        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})\n        // 设置文本样式为黑色，字体大小20，字重正常\n        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})\n        // 设置选择项文本样式为蓝色，字体大小30，字重较粗\n        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})\n    }.width('100%').height('100%') // 设置Column组件宽度和高度均为100%\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct TextPickerExample {\n  private select: number = 1\n  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4']\n\n  build() {\n    Column() {\n      TextPicker({ range: this.fruits, selected: this.select })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('Picker item changed, value: ' + value + ', index: ' + index)\n        })\n        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})\n        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})\n        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})\n    }.width('100%').height('100%')\n  }\n}"""
            """// TextPicker示例代码注释\n\n// TextPickerExample结构体，包含select和fruits两个私有属性\n// select: 当前选中的水果索引，默认为1\n// fruits: 水果数组，包含'apple1', 'orange2', 'peach3', 'grape4'\n@Entry\n@Component\nstruct TextPickerExample {\n  private select: number = 1\n  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4']\n\n  // 构建TextPicker组件\n  build() {\n    // 创建一个Column布局\n    Column() {\n      // 创建TextPicker组件，传入水果数组和当前选中索引\n      TextPicker({ range: this.fruits, selected: this.select })\n        // 当选择项改变时触发onChange事件，打印选中项的值和索引\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('Picker item changed, value: ' + value + ', index: ' + index)\n        })\n        // 设置选中项消失时的文本样式，颜色为红色，字体大小为15，字重为Lighter\n        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})\n        // 设置文本样式，颜色为黑色，字体大小为20，字重为Normal\n        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})\n        // 设置选中文本样式，颜色为蓝色，字体大小为30，字重为Bolder\n        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})\n        // 不显示分割线\n        .divider(null)\n    }.width('100%').height('100%') // 设置Column布局的宽度和高度均为100%\n  }\n}\n```\n// xxx.ets\n@Entry\n@Component\nstruct TextPickerExample {\n  private select: number = 1\n  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4']\n\n  build() {\n    Column() {\n      TextPicker({ range: this.fruits, selected: this.select })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('Picker item changed, value: ' + value + ', index: ' + index)\n        })\n        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})\n        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})\n        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})\n        .divider(null)\n    }.width('100%').height('100%')\n  }\n}"""
            """// TextPickerExample.ets\n@Entry\n@Component\nstruct TextPickerExample {\n  private select: number = 1 // 初始化选中项为1\n  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'] // 水果列表\n\n  build() {\n    Column() {\n      TextPicker({ range: this.fruits, selected: this.select }) // 创建文本选择器，传入水果列表和初始选中项\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('Picker item changed, value: ' + value + ', index: ' + index) // 当选择项改变时打印选择的值和索引\n        })\n        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}}) // 设置消失时的文本样式为红色\n        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}}) // 设置文本样式为黑色\n        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}}) // 设置选中文本样式为蓝色\n        .divider({\n          strokeWidth: 10,\n          color: Color.Red,\n          startMargin: 10,\n          endMargin: 20\n        } as DividerOptions) // 设置分隔线样式\n    }.width('100%').height('100%') // 设置列的宽度和高度为100%\n  }\n}\n```\n\n在上面的代码中：\n- 初始化了选中项为1和水果列表。\n- 创建了一个文本选择器(TextPicker)，传入水果列表和初始选中项。\n- 当选择项改变时，会打印选择的值和索引。\n- 设置了消失时的文本样式为红色，文本样式为黑色，选中文本样式为蓝色。\n- 设置了分隔线的样式，包括线宽、颜色以及起始和结束边距。\n// xxx.ets\n@Entry\n@Component\nstruct TextPickerExample {\n  private select: number = 1\n  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4']\n\n  build() {\n    Column() {\n      TextPicker({ range: this.fruits, selected: this.select })\n        .onChange((value: string | string[], index: number | number[]) => {\n          console.info('Picker item changed, value: ' + value + ', index: ' + index)\n        })\n        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})\n        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})\n        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})\n        .divider({\n          strokeWidth: 10,\n          color: Color.Red,\n          startMargin: 10,\n          endMargin: 20\n        } as DividerOptions)\n    }.width('100%').height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "TextTimer": {
        "description": "通过文本显示计时信息并控制其计时器状态的组件。",
        "interfaces": [
            {
                "description": "TextTimer(options?: TextTimerOptions)",
                "params": {
                    "options": {
                        "type": "TextTimerOptions",
                        "required": False,
                        "description": "TextTimer的选项参数。"
                    }
                }
            }
        ],
        "attributes": {
            "format": {
                "description": "设置自定义格式，需至少包含一个HH、mm、ss、SS中的关键字。如使用yy、MM、dd等日期格式，则使用默认值。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "自定义格式。",
                        "default": "HH:mm:ss.SS"
                    }
                }
            },
            "textShadow": {
                "description": "设置文字阴影效果。该接口支持以数组形式入参，实现多重文字阴影。不支持fill字段, 不支持智能取色模式。",
                "params": {
                    "value": {
                        "type": ["ShadowOptions", "Array<ShadowOptions>"],
                        "required": True,
                        "description": "文字阴影效果。"
                    }
                }
            },
            "contentModifier": {
                "description": "定制TextTimer内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<TextTimerConfiguration>",
                        "required": True,
                        "description": "内容区定制方法。"
                    }
                }
            }
        },
        "events": {
            "onTimer": {
                "description": "时间文本发生变化时触发。锁屏状态和应用后台状态下不会触发该事件。",
                "params": {
                    "utc": {
                        "type": "number",
                        "required": True,
                        "description": "Linux时间戳，即自1970年1月1日起经过的时间，单位为设置格式的最小单位。"
                    },
                    "elapsedTime": {
                        "type": "number",
                        "required": True,
                        "description": "计时器经过的时间，单位为设置格式的最小单位。"
                    }
                }
            }
        },
        "examples": [
            "// xxx.ets\n/*\n实现思路：\n本示例展示了如何使用TextTimer组件实现一个倒计时器，并提供了开始、暂停和重置按钮来控制倒计时的行为。通过TextTimerController来管理倒计时的状态，并使用format属性来定义倒计时显示的格式。\n总体功能与效果描述：\n1. 创建一个倒计时器，初始倒计时时间为30000毫秒（30秒）。\n2. 提供开始、暂停和重置按钮来控制倒计时的运行状态。\n3. 倒计时器显示格式为\"mm:ss.SS\"，即分钟:秒.毫秒。\n4. 当倒计时进行时，会在控制台输出当前的UTC时间和已流逝的时间。\n*/\n\n@Entry\n@Component\nstruct TextTimerExample {\n  // 创建一个TextTimerController实例，用于控制倒计时器\n  textTimerController: TextTimerController = new TextTimerController()\n  // 定义倒计时显示的格式，初始值为\"mm:ss.SS\"\n  @State format: string = 'mm:ss.SS'\n\n  build() {\n    Column() {\n      // 创建一个TextTimer组件，设置为倒计时模式，初始倒计时时间为30000毫秒，并绑定控制器\n      TextTimer({ isCountDown: true, count: 30000, controller: this.textTimerController })\n        .format(this.format) // 设置倒计时显示的格式\n        .fontColor(Color.Black) // 设置倒计时文本颜色为黑色\n        .fontSize(50) // 设置倒计时文本字体大小为50\n        .onTimer((utc: number, elapsedTime: number) => {\n          // 当倒计时进行时，输出当前的UTC时间和已流逝的时间\n          console.info('textTimer notCountDown utc is：' + utc + ', elapsedTime: ' + elapsedTime)\n        })\n      Row() {\n        // 创建开始按钮，点击时启动倒计时\n        Button(\"start\").onClick(() => {\n          this.textTimerController.start()\n        })\n        // 创建暂停按钮，点击时暂停倒计时\n        Button(\"pause\").onClick(() => {\n          this.textTimerController.pause()\n        })\n        // 创建重置按钮，点击时重置倒计时\n        Button(\"reset\").onClick(() => {\n          this.textTimerController.reset()\n        })\n      }\n    }\n  }\n}",
            "// xxx.ets\n/*\n实现思路：\n本示例展示了如何使用TextTimer组件并为其添加多个文本阴影效果。通过@State装饰器定义一个包含多个ShadowOptions对象的数组，每个ShadowOptions对象定义了一个阴影的半径、颜色和偏移量。在TextTimer组件中使用textShadow属性来应用这些阴影效果。\n总体功能与效果描述：\n1. 创建一个TextTimer组件，显示一个计时器。\n2. 为TextTimer组件添加多个文本阴影效果，每个阴影具有不同的颜色、半径和水平偏移量。\n3. 通过设置textShadow属性，使每个阴影效果叠加，形成一种渐变的多重阴影效果。\n*/\n\n@Entry\n@Component\nstruct TextTimerExample {\n  // 定义一个状态变量textShadows，包含多个ShadowOptions对象，每个对象定义了一个阴影的半径、颜色和偏移量\n  @State textShadows : ShadowOptions | Array<ShadowOptions> = [{ radius: 10, color: Color.Red, offsetX: 10, offsetY: 0 },\n      { radius: 10, color: Color.Black, offsetX: 20, offsetY: 0 },\n      { radius: 10, color: Color.Brown, offsetX: 30, offsetY: 0 },\n      { radius: 10, color: Color.Green, offsetX: 40, offsetY: 0 },\n      { radius: 10, color: Color.Yellow, offsetX: 100, offsetY: 0 }]\n\n  build() {\n    Column({ space: 8 }) {\n      // 创建一个TextTimer组件，设置字体大小为50，并应用定义的文本阴影效果\n      TextTimer().fontSize(50).textShadow(this.textShadows)\n    }\n  }\n}",
            "// xxx.ets\n/*\n该示例实现了两个简易秒表，使用浅灰色背景。计时器开始后，会实时显示时间变化。倒计时器开始后，背景会变成黑色，正计时器开始后，背景会变成灰色。\n实现思路：\n本示例展示了如何自定义TextTimer组件的显示内容，并通过实现ContentModifier接口来应用这些自定义内容。通过创建一个MyTextTimerModifier类，重写applyContent方法来返回一个自定义的TextTimer构建器。在构建器中，使用Stack和Circle组件来创建一个圆形计时器显示，并根据计时器的运行状态和倒计时/正计时模式来动态更新显示内容。\n总体功能与效果描述：\n1. 创建一个自定义的TextTimer显示内容，包括一个圆形进度条和计时文本。\n2. 通过实现ContentModifier接口，将自定义内容应用到TextTimer组件。\n3. 提供开始、暂停和重置按钮来控制两个TextTimer组件（一个倒计时器和一个正计时器）的运行状态。\n4. 根据计时器的运行状态和倒计时/正计时模式，动态更新圆形进度条的颜色和计时文本的内容。\n*/\n\n// 定义一个自定义的TextTimer修饰器类，实现ContentModifier接口\nclass MyTextTimerModifier implements ContentModifier<TextTimerConfiguration> {\n  constructor() {\n  }\n  // 重写applyContent方法，返回一个自定义的TextTimer构建器\n  applyContent() : WrappedBuilder<[TextTimerConfiguration]>\n  {\n      return wrapBuilder(buildTextTimer)\n  }\n}\n\n// 定义一个构建器函数，用于构建自定义的TextTimer显示内容\n@Builder function buildTextTimer(config: TextTimerConfiguration) {\n  Column() {\n     Stack({ alignContent: Alignment.Center }) {\n       // 创建一个圆形进度条，根据计时器的运行状态和倒计时/正计时模式设置填充颜色\n       Circle({ width: 150, height: 150 }).fill(config.started ? (config.isCountDown ? 0xFF232323 : 0xFF717171) : 0xFF929292)\n       Column(){\n         // 显示倒计时或正计时的文本\n         Text(config.isCountDown ? \"倒计时\" : \"正计时\").fontColor(Color.White)\n         Text(\n           (config.isCountDown ? \"剩余\" : \"已经过去了\") + (config.isCountDown?\n             (Math.max((config.count - config.elapsedTime) / 1000,0)).toFixed(1) + \"/\" + (config.count / 1000).toFixed(0)\n             :((config.elapsedTime / 1000).toFixed(0))\n           ) + \"秒\"\n         ).fontColor(Color.White)\n       }\n     }\n  }\n}\n\n@Entry\n@Component\nstruct Index {\n  // 定义倒计时器的初始时间\n  @State count: number = 10000\n  // 创建一个自定义的TextTimer修饰器实例\n  @State myTimerModifier: MyTextTimerModifier = new MyTextTimerModifier()\n  // 创建两个TextTimerController实例，分别用于控制倒计时器和正计时器\n  countDownTextTimerController: TextTimerController = new TextTimerController()\n  countUpTextTimerController: TextTimerController = new TextTimerController()\n\n  build() {\n    Row() {\n      Column() {\n        // 创建一个倒计时TextTimer组件，应用自定义修饰器，并绑定控制器\n        TextTimer({isCountDown: true, count: this.count, controller: this.countDownTextTimerController})\n          .contentModifier(this.myTimerModifier)\n          .onTimer((utc: number, elapsedTime: number) => {\n            console.info('textTimer onTimer utc is：' + utc + ', elapsedTime: ' + elapsedTime)\n          })\n          .margin(10)\n        // 创建一个正计时TextTimer组件，应用自定义修饰器，并绑定控制器\n        TextTimer({isCountDown: false, controller: this.countUpTextTimerController})\n          .contentModifier(this.myTimerModifier)\n          .onTimer((utc: number, elapsedTime: number) => {\n            console.info('textTimer onTimer utc is：' + utc + ', elapsedTime: ' + elapsedTime)\n          })\n        Row() {\n          // 创建开始按钮，点击时启动两个计时器\n          Button(\"start\").onClick(()=>{\n            this.countDownTextTimerController.start()\n            this.countUpTextTimerController.start()\n          }).margin(10)\n          // 创建暂停按钮，点击时暂停两个计时器\n          Button(\"pause\").onClick(()=>{\n            this.countDownTextTimerController.pause()\n            this.countUpTextTimerController.pause()\n          }).margin(10)\n          // 创建重置按钮，点击时重置两个计时器\n          Button(\"reset\").onClick(()=>{\n            this.countDownTextTimerController.reset()\n            this.countUpTextTimerController.reset()\n          }).margin(10)\n        }.margin(20)\n      }.width('100%')\n    }.height('100%')\n  }\n}"
        ],
        "is_common_attrs": True
    },
    "TimePicker": {
        "description": "时间选择组件，根据指定参数创建选择器，支持选择小时及分钟。",
        "interfaces": [
            {
                "description": "TimePicker(options?: TimePickerOptions)\n\n默认以24小时的时间区间创建滑动选择器。",
                "params": {
                    "options": {
                        "type": "TimePickerOptions",
                        "required": False,
                        "description": "配置时间选择组件的参数。"
                    }
                }
            }
        ],
        "attributes": {
            "useMilitaryTime": {
                "description": "设置展示时间是否为24小时制。当展示时间为12小时制时，上下午与小时无联动关系。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "展示时间是否为24小时制。",
                        "default": False
                    }
                }
            },
            "disappearTextStyle": {
                "description": "设置所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。",
                        "default": {
                            "color": "#ff182431",
                            "font": {
                                "size": "14fp",
                                "weight": "FontWeight.Regular"
                            }
                        }
                    }
                }
            },
            "textStyle": {
                "description": "设置所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。",
                        "default": {
                            "color": "#ff182431",
                            "font": {
                                "size": "16fp",
                                "weight": "FontWeight.Regular"
                            }
                        }
                    }
                }
            },
            "selectedTextStyle": {
                "description": "设置选中项的文本颜色、字号、字体粗细。",
                "params": {
                    "value": {
                        "type": "PickerTextStyle",
                        "required": True,
                        "description": "选中项的文本颜色、字号、字体粗细。",
                        "default": {
                            "color": "#ff007dff",
                            "font": {
                                "size": "20vp",
                                "weight": "FontWeight.Medium"
                            }
                        }
                    }
                }
            },
            "loop": {
                "description": "设置是否启用循环模式。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否启用循环模式。",
                        "default": True
                    }
                }
            },
            "dateTimeOptions": {
                "description": "设置时分秒是否显示前置0。",
                "params": {
                    "value": {
                        "type": "DateTimeOptions",
                        "required": True,
                        "description": "设置时分秒是否显示前置0，目前只支持设置hour、minute和second参数。",
                        "default": {
                            "hour": "24小时制默认为'2-digit'，即有前置0；12小时制默认为'numeric'，即没有前置0。",
                            "minute": "默认为'2-digit'，即有前置0。",
                            "second": "默认为'2-digit'，即有前置0。"
                        }
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "选择时间时触发该事件。",
                "params": {
                    "value": {
                        "type": "TimePickerResult",
                        "required": True,
                        "description": "24小时制时间。"
                    }
                }
            }
        },
        "examples": [
            "/*\n实现思路：\n本示例展示了如何使用TimePicker组件来选择时间，并支持切换12小时制和24小时制显示。通过一个按钮来切换时间显示模式，并在时间选择变化时更新选中的时间。\n*/\n// TimePickerExample.ets\n@Entry\n@Component\nstruct TimePickerExample {\n  @State isMilitaryTime: boolean = false // 用于控制时间显示模式，初始为12小时制\n  private selectedTime: Date = new Date('2022-07-22T08:00:00') // 初始选中的时间\n\n  build() {\n    Column() {\n      Button('切换12小时制/24小时制')\n        .margin(30) // 设置按钮的上下边距\n        .onClick(() => {\n          this.isMilitaryTime = !this.isMilitaryTime // 切换时间显示模式\n        })\n      TimePicker({\n        selected: this.selectedTime, // 当前选中的时间\n      })\n        .useMilitaryTime(this.isMilitaryTime) // 根据isMilitaryTime状态切换12小时制或24小时制显示\n        .onChange((value: TimePickerResult) => {\n          if(value.hour >= 0) {\n            this.selectedTime.setHours(value.hour, value.minute) // 更新选中的时间\n            console.info('select current date is: ' + JSON.stringify(value)) // 输出当前选中的时间\n          }\n        })\n        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}}) // 设置不可见文本的样式\n        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}}) // 设置普通文本的样式\n        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}}) // 设置选中时间的文本样式\n    }.width('100%')\n  }\n}"
        ],
        "is_common_attrs": True
    },
    "Toggle": {
        "description": "组件提供勾选框样式、状态按钮样式及开关样式。",
        "details": None,
        "interfaces": [
            {
                "description": "Toggle(options: { type: ToggleType, isOn?: boolean })",
                "params": {
                    "type": {
                        "type": "ToggleType",
                        "required": False,
                        "description": "开关的样式。",
                        "default": None
                    },
                    "isOn": {
                        "type": "boolean",
                        "required": False,
                        "description": "开关是否打开，true：打开，false：关闭。",
                        "default": False
                    }
                }
            }
        ],
        "attributes": {
            "selectedColor": {
                "description": "设置组件打开状态的背景颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "组件打开状态的背景颜色。",
                        "default": None
                    }
                }
            },
            "switchPointColor": {
                "description": "设置Switch类型的圆形滑块颜色。仅对type为ToggleType.Switch生效。",
                "params": {
                    "color": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "Switch类型的圆形滑块颜色。",
                        "default": "#ffffffff"
                    }
                }
            },
            "switchStyle": {
                "description": "设置Switch类型的样式。仅对type为ToggleType.Switch生效。",
                "params": {
                    "value": {
                        "type": "SwitchStyle",
                        "required": False,
                        "description": "Switch类型的样式配置。",
                        "default": None
                    }
                }
            },
            "contentModifier": {
                "description": "定制Toggle内容区的方法。",
                "params": {
                    "modifier": {
                        "type": "ContentModifier<ToggleConfiguration>",
                        "required": False,
                        "description": "定制Toggle内容区的方法。",
                        "default": None
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "开关状态切换时触发该事件。",
                "params": {
                    "isOn": {
                        "type": "boolean",
                        "required": False,
                        "description": "为true时，代表状态从关切换为开。false时，代表状态从开切换为关。",
                        "default": None
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\n实现思路：\n本示例展示了Toggle组件在不同类型（Switch、Checkbox、Button）下的使用方法和效果。通过设置不同的类型和状态，展示Toggle组件在UI上的不同表现和交互行为。\n总体功能与效果描述：\nToggle组件可以作为开关、复选框和按钮使用，通过切换状态来触发相应的事件处理函数，并在控制台输出当前组件的状态。\n*/\n\n// ToggleExample.ets\n@Entry\n@Component\nstruct ToggleExample {\n  build() {\n    Column({ space: 10 }) {\n      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')\n      // 使用Flex布局，使两个Switch类型的Toggle组件在水平方向上均匀分布\n      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {\n        // 第一个Switch类型的Toggle组件，初始状态为关闭\n        Toggle({ type: ToggleType.Switch, isOn: false })\n          .selectedColor('#007DFF') // 设置选中状态的颜色\n          .switchPointColor('#FFFFFF') // 设置开关点颜色\n          .onChange((isOn: boolean) => {\n            console.info('Component status:' + isOn) // 当状态改变时，输出当前状态\n          })\n\n        // 第二个Switch类型的Toggle组件，初始状态为开启\n        Toggle({ type: ToggleType.Switch, isOn: true })\n          .selectedColor('#007DFF') // 设置选中状态的颜色\n          .switchPointColor('#FFFFFF') // 设置开关点颜色\n          .onChange((isOn: boolean) => {\n            console.info('Component status:' + isOn) // 当状态改变时，输出当前状态\n          })\n      }\n\n      Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')\n      // 使用Flex布局，使两个Checkbox类型的Toggle组件在水平方向上均匀分布\n      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {\n        // 第一个Checkbox类型的Toggle组件，初始状态为关闭\n        Toggle({ type: ToggleType.Checkbox, isOn: false })\n          .size({ width: 20, height: 20 }) // 设置组件的大小\n          .selectedColor('#007DFF') // 设置选中状态的颜色\n          .onChange((isOn: boolean) => {\n            console.info('Component status:' + isOn) // 当状态改变时，输出当前状态\n          })\n\n        // 第二个Checkbox类型的Toggle组件，初始状态为开启\n        Toggle({ type: ToggleType.Checkbox, isOn: true })\n          .size({ width: 20, height: 20 }) // 设置组件的大小\n          .selectedColor('#007DFF') // 设置选中状态的颜色\n          .onChange((isOn: boolean) => {\n            console.info('Component status:' + isOn) // 当状态改变时，输出当前状态\n          })\n      }\n\n      Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')\n      // 使用Flex布局，使两个Button类型的Toggle组件在水平方向上均匀分布\n      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {\n        // 第一个Button类型的Toggle组件，初始状态为关闭\n        Toggle({ type: ToggleType.Button, isOn: false }) {\n          Text('status button').fontColor('#182431').fontSize(12) // 设置按钮上的文本\n        }.width(106) // 设置组件的宽度\n        .selectedColor('rgba(0,125,255,0.20)') // 设置选中状态的颜色\n        .onChange((isOn: boolean) => {\n          console.info('Component status:' + isOn) // 当状态改变时，输出当前状态\n        })\n\n        // 第二个Button类型的Toggle组件，初始状态为开启\n        Toggle({ type: ToggleType.Button, isOn: true }) {\n          Text('status button').fontColor('#182431').fontSize(12) // 设置按钮上的文本\n        }.width(106) // 设置组件的宽度\n        .selectedColor('rgba(0,125,255,0.20)') // 设置选中状态的颜色\n        .onChange((isOn: boolean) => {\n          console.info('Component status:' + isOn) // 当状态改变时，输出当前状态\n        })\n      }\n    }.width('100%').padding(24) // 设置列的宽度和内边距\n  }\n}",
            "该示例实现了自定义设置Toggle组件Switch样式的圆形滑块半径、关闭状态的背景颜色、圆形滑块颜色、滑轨的圆角。\n/*\n实现思路：\n本示例展示了Toggle组件在Switch类型下的自定义样式设置。通过设置不同的样式属性，如点半径、轨道边框半径、点颜色和未选中颜色，展示Toggle组件在UI上的个性化表现和交互行为。\n总体功能与效果描述：\nToggle组件可以作为开关使用，通过切换状态来触发相应的事件处理函数，并在控制台输出当前组件的状态。同时，通过自定义样式属性，使Toggle组件的外观更加个性化。\n*/\n\n// ToggleExample.ets\n@Entry\n@Component\nstruct ToggleExample {\n  build() {\n    Column({ space: 10 }) {\n      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')\n      // 使用Flex布局，使两个Switch类型的Toggle组件在水平方向上均匀分布\n      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {\n        // 第一个Switch类型的Toggle组件，初始状态为关闭\n        Toggle({ type: ToggleType.Switch, isOn: false })\n          .selectedColor('#007DFF') // 设置选中状态的颜色\n          .switchStyle({\n            pointRadius: 15, // 设置开关点的半径\n            trackBorderRadius: 10, // 设置轨道边框的半径\n            pointColor: '#D2B48C', // 设置开关点的颜色\n            unselectedColor: Color.Pink // 设置未选中状态的颜色\n          })\n          .onChange((isOn: boolean) => {\n            console.info('Component status:' + isOn) // 当状态改变时，输出当前状态\n          })\n\n        // 第二个Switch类型的Toggle组件，初始状态为开启\n        Toggle({ type: ToggleType.Switch, isOn: true })\n          .selectedColor('#007DFF') // 设置选中状态的颜色\n          .switchStyle({\n            pointRadius: 15, // 设置开关点的半径\n            trackBorderRadius: 10, // 设置轨道边框的半径\n            pointColor: '#D2B48C', // 设置开关点的颜色\n            unselectedColor: Color.Pink // 设置未选中状态的颜色\n          })\n          .onChange((isOn: boolean) => {\n            console.info('Component status:' + isOn) // 当状态改变时，输出当前状态\n          })\n      }\n    }.width('100%').padding(24) // 设置列的宽度和内边距\n  }\n}",
            "该示例实现了自定义Toggle样式的功能。自定义样式实现了通过按钮切换圆形颜色的功能：点击蓝圆按钮，圆形背景变蓝色，点击黄圆按钮，圆形背景变黄色。\n/*\n实现思路：\n本示例展示了如何通过自定义样式类和Builder函数来创建一个具有自定义外观和交互行为的Toggle组件。通过定义一个自定义样式类`MySwitchStyle`，并在Toggle组件中应用该样式，实现了一个具有圆形指示灯和两个按钮的开关组件。\n总体功能与效果描述：\nToggle组件可以作为开关使用，通过点击不同的按钮来切换状态，并在控制台输出当前组件的状态。同时，通过自定义样式类和Builder函数，使Toggle组件的外观和交互行为更加个性化。\n*/\n\n// MySwitchStyle.ets\nclass MySwitchStyle implements ContentModifier<ToggleConfiguration> {\n  selectedColor: Color = Color.White; // 默认选中颜色\n  lamp: string = 'string'; // 默认灯的标识\n\n  constructor(selectedColor: Color, lamp: string) {\n    this.selectedColor = selectedColor; // 初始化选中颜色\n    this.lamp = lamp; // 初始化灯的标识\n  }\n\n  applyContent(): WrappedBuilder<[ToggleConfiguration]> {\n    return wrapBuilder(buildSwitch); // 应用Builder函数\n  }\n}\n\n// Builder函数，用于构建Toggle组件的内容\n@Builder function buildSwitch(config: ToggleConfiguration) {\n  Column({ space: 50 }) {\n    Circle({ width: 150, height: 150 }) // 创建一个圆形指示灯\n      .fill(config.isOn ? (config.contentModifier as MySwitchStyle).selectedColor : Color.Blue) // 根据状态设置颜色\n    Row() {\n      Button('蓝' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp)) // 创建一个蓝色按钮\n        .onClick(() => {\n          config.triggerChange(false); // 点击按钮时触发状态改变\n        })\n      Button('黄' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp)) // 创建一个黄色按钮\n        .onClick(() => {\n          config.triggerChange(true); // 点击按钮时触发状态改变\n        })\n    }\n  }\n}\n\n// Index.ets\n@Entry\n@Component\nstruct Index {\n  build() {\n    Column({ space: 50 }) {\n      Toggle({ type: ToggleType.Switch }) // 创建一个Switch类型的Toggle组件\n        .enabled(true) // 设置组件为启用状态\n        .contentModifier(new MySwitchStyle(Color.Yellow, '灯')) // 应用自定义样式\n        .onChange((isOn: boolean) => {\n          console.info('Switch Log:' + isOn); // 当状态改变时，输出当前状态\n        })\n    }.height('100%').width('100%') // 设置列的高度和宽度\n  }\n}"
        ],
        "is_common_attrs": True
    },
    "TextInput": {
        "description": "单行文本输入框组件。",
        "interfaces": [
            {
                "description": "TextInput(value?: TextInputOptions)",
                "params": {
                    "value": {
                        "type": "TextInputOptions",
                        "required": False,
                        "description": "TextInput组件的初始化选项。"
                    }
                }
            }
        ],
        "attributes": {
            "placeholder": {
                "description": "设置无输入时的提示文本。",
                "params": {
                    "value": {
                        "type": "ResourceStr",
                        "required": False,
                        "description": "提示文本内容。"
                    }
                }
            },
            "text": {
                "description": "设置输入框当前的文本内容。建议通过onChange事件将状态变量与文本实时绑定，避免组件刷新时TextInput中的文本内容异常。",
                "params": {
                    "value": {
                        "type": "ResourceStr",
                        "required": False,
                        "description": "输入框的文本内容。"
                    }
                }
            },
            "controller": {
                "description": "设置TextInput控制器。",
                "params": {
                    "value": {
                        "type": "TextInputController",
                        "required": False,
                        "description": "TextInput组件的控制器。"
                    }
                }
            },
            "type": {
                "description": "设置输入框类型。",
                "params": {
                    "value": {
                        "type": "InputType",
                        "required": True,
                        "description": "输入框类型。",
                        "default": "InputType.Normal"
                    }
                }
            },
            "contentType": {
                "description": "设置自动填充类型。",
                "params": {
                    "value": {
                        "type": "ContentType",
                        "required": True,
                        "description": "自动填充类型。"
                    }
                }
            },
            "placeholderColor": {
                "description": "设置placeholder文本颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "placeholder文本颜色。"
                    }
                }
            },
            "placeholderFont": {
                "description": "设置placeholder文本样式，包括字体大小，字体粗细，字体族，字体风格。目前仅支持默认字体族。",
                "params": {
                    "value": {
                        "type": "Font",
                        "required": False,
                        "description": "placeholder文本样式。"
                    }
                }
            },
            "enterKeyType": {
                "description": "设置输入法回车键类型。",
                "params": {
                    "value": {
                        "type": "EnterKeyType",
                        "required": True,
                        "description": "输入法回车键类型。",
                        "default": "EnterKeyType.Done"
                    }
                }
            },
            "caretColor": {
                "description": "设置输入框光标颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "输入框光标颜色。"
                    }
                }
            },
            "maxLength": {
                "description": "设置文本的最大输入字符数。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "文本的最大输入字符数。",
                        "default": "Infinity"
                    }
                }
            },
            "inputFilter": {
                "description": "通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。仅支持单个字符匹配，不支持字符串匹配。",
                "params": {
                    "value": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "正则表达式。"
                    },
                    "error": {
                        "type": "(value: string) => void",
                        "required": False,
                        "description": "正则匹配失败时，返回被过滤的内容。"
                    }
                }
            },
            "copyOption": {
                "description": "设置输入的文本是否可复制。设置CopyOptions.None时，当前TextInput中的文字无法被复制或剪切，仅支持粘贴。",
                "params": {
                    "value": {
                        "type": "CopyOptions",
                        "required": True,
                        "description": "输入的文本是否可复制。",
                        "default": "CopyOptions.LocalDevice"
                    }
                }
            },
            "showPasswordIcon": {
                "description": "设置当密码输入模式时，输入框末尾的图标是否显示。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "密码输入模式时，输入框末尾的图标是否显示。",
                        "default": True
                    }
                }
            },
            "style": {
                "description": "设置输入框为默认风格或内联输入风格，内联输入风格只支持InputType.Normal类型。",
                "params": {
                    "value": {
                        "type": "TextInputStyle",
                        "required": True,
                        "description": "输入框风格。"
                    }
                }
            },
            "textAlign": {
                "description": "设置文本在输入框中的水平对齐方式。",
                "params": {
                    "value": {
                        "type": "TextAlign",
                        "required": True,
                        "description": "文本在输入框中的水平对齐方式。",
                        "default": "TextAlign.Start"
                    }
                }
            },
            "selectedBackgroundColor": {
                "description": "设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "文本选中底板颜色。"
                    }
                }
            },
            "caretStyle": {
                "description": "设置光标风格。",
                "params": {
                    "value": {
                        "type": "CaretStyle",
                        "required": True,
                        "description": "光标风格。"
                    }
                }
            },
            "caretPosition": {
                "description": "设置光标位置。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "光标的位置。"
                    }
                }
            },
            "showUnit": {
                "description": "设置控件作为文本框单位。需搭配showUnderline使用，当showUnderline为True时生效。",
                "params": {
                    "value": {
                        "type": "CustomBuilder",
                        "required": True,
                        "description": "控件作为文本框单位。"
                    }
                }
            },
            "showError": {
                "description": "设置错误状态下提示的错误文本或者不显示错误状态。",
                "params": {
                    "value": {
                        "type": ["ResourceStr", "undefined"],
                        "required": False,
                        "description": "错误状态下提示的错误文本或者不显示错误状态。",
                        "default": "undefined"
                    }
                }
            },
            "showUnderline": {
                "description": "设置是否开启下划线。下划线默认颜色为'#33182431'，默认粗细为1px，文本框尺寸48vp，下划线只支持InputType.Normal类型。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启下划线。",
                        "default": False
                    }
                }
            },
            "underlineColor": {
                "description": "开启下划线时，支持配置下划线颜色。",
                "params": {
                    "value": {
                        "type": ["ResourceColor", "UnderlineColor", "undefined"],
                        "required": True,
                        "description": "设置下划线颜色。",
                        "default": "主题配置的下划线颜色"
                    }
                }
            },
            "passwordIcon": {
                "description": "设置当密码输入模式时，输入框末尾的图标。",
                "params": {
                    "value": {
                        "type": "PasswordIcon",
                        "required": True,
                        "description": "密码输入模式时，输入框末尾的图标。",
                        "default": "系统提供的密码图标"
                    }
                }
            },
            "enableKeyboardOnFocus": {
                "description": "设置TextInput通过点击以外的方式获焦时，是否绑定输入法。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "通过点击以外的方式获焦时，是否绑定输入法。",
                        "default": True
                    }
                }
            },
            "selectionMenuHidden": {
                "description": "设置长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。",
                        "default": False
                    }
                }
            },
            "barState": {
                "description": "设置内联输入风格编辑态时滚动条的显示模式。",
                "params": {
                    "value": {
                        "type": "BarState",
                        "required": True,
                        "description": "内联输入风格编辑态时滚动条的显示模式。",
                        "default": "BarState.Auto"
                    }
                }
            },
            "maxLines": {
                "description": "设置内联输入风格编辑态时文本可显示的最大行数。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "内联输入风格编辑态时文本可显示的最大行数。",
                        "default": 3
                    }
                }
            },
            "customKeyboard": {
                "description": "设置自定义键盘。",
                "params": {
                    "value": {
                        "type": "CustomBuilder",
                        "required": True,
                        "description": "自定义键盘。"
                    },
                    "options": {
                        "type": "KeyboardOptions",
                        "required": False,
                        "description": "自定义键盘的选项。"
                    }
                }
            },
            "enableAutoFill": {
                "description": "设置是否启用自动填充。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否启用自动填充。",
                        "default": True
                    }
                }
            },
            "passwordRules": {
                "description": "定义生成密码的规则。在触发自动填充时，所设置的密码规则会透传给密码保险箱，用于新密码的生成。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "定义生成密码的规则。"
                    }
                }
            },
            "cancelButton": {
                "description": "设置右侧清除按钮样式。不支持内联模式。",
                "params": {
                    "value": {
                        "type": {
                            "style": "CancelButtonStyle",
                            "icon": "IconOptions"
                        },
                        "required": True,
                        "description": "右侧清除按钮样式。"
                    }
                }
            },
            "selectAll": {
                "description": "设置当初始状态，是否全选文本。不支持内联模式。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否全选文本。",
                        "default": False
                    }
                }
            },
            "showCounter": {
                "description": "设置当通过InputCounterOptions输入的字符数超过阈值时显示计数器。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否显示计数器。"
                    },
                    "options": {
                        "type": "InputCounterOptions",
                        "required": False,
                        "description": "计数器的选项。"
                    }
                }
            },
            "lineHeight": {
                "description": "设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本的文本行高。"
                    }
                }
            },
            "decoration": {
                "description": "设置文本装饰线类型样式及其颜色。密码模式不生效。",
                "params": {
                    "value": {
                        "type": "TextDecorationOptions",
                        "required": True,
                        "description": "文本装饰线对象。",
                        "default": {
                            "type": "TextDecorationType.None",
                            "color": "Color.Black",
                            "style": "TextDecorationStyle.SOLID"
                        }
                    }
                }
            },
            "letterSpacing": {
                "description": "设置文本字符间距。设置该值为百分比时，按默认值显示。设置该值为0时，按默认值显示。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本字符间距。"
                    }
                }
            },
            "fontFeature": {
                "description": "设置文字特性效果，比如数字等宽的特性。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "文字特性效果。"
                    }
                }
            },
            "wordBreak": {
                "description": "设置文本断行规则。该属性在组件设置内联模式时样式生效，但对placeholder文本无效。",
                "params": {
                    "value": {
                        "type": "WordBreak",
                        "required": True,
                        "description": "内联输入风格编辑态时断行规则。",
                        "default": "WordBreak.BREAK_WORD"
                    }
                }
            },
            "textOverflow": {
                "description": "设置文本超长时的显示方式。仅在内联模式的编辑态、非编辑态下支持。",
                "params": {
                    "value": {
                        "type": "TextOverflow",
                        "required": True,
                        "description": "文本超长时的显示方式。",
                        "default": {
                            "非编辑态": "TextOverflow.Ellipsis",
                            "编辑态": "TextOverflow.Clip"
                        }
                    }
                }
            },
            "textIndent": {
                "description": "设置首行文本缩进。",
                "params": {
                    "value": {
                        "type": "Dimension",
                        "required": True,
                        "description": "首行文本缩进。"
                    }
                }
            },
            "minFontSize": {
                "description": "设置文本最小显示字号。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本最小显示字号。"
                    }
                }
            },
            "maxFontSize": {
                "description": "设置文本最大显示字号。",
                "params": {
                    "value": {
                        "type": ["number", "string", "Resource"],
                        "required": True,
                        "description": "文本最大显示字号。"
                    }
                }
            },
            "heightAdaptivePolicy": {
                "description": "组件设置为内联输入风格时，设置文本自适应高度的方式。",
                "params": {
                    "value": {
                        "type": "TextHeightAdaptivePolicy",
                        "required": True,
                        "description": "文本自适应高度的方式。"
                    }
                }
            },
            "showPassword": {
                "description": "设置密码的显隐状态。",
                "params": {
                    "visible": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否显示密码。",
                        "default": False
                    }
                }
            },
            "lineBreakStrategy": {
                "description": "设置折行规则。该属性在wordBreak不等于breakAll的时候生效，不支持连词符。",
                "params": {
                    "strategy": {
                        "type": "LineBreakStrategy",
                        "required": True,
                        "description": "文本的折行规则。",
                        "default": "LineBreakStrategy.GREEDY"
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "输入内容发生变化时，触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前输入的文本内容。"
                    }
                }
            },
            "onSubmit": {
                "description": "按下输入法回车键触发该回调。",
                "params": {
                    "enterKey": {
                        "type": "EnterKeyType",
                        "required": True,
                        "description": "输入法回车键类型。"
                    },
                    "event": {
                        "type": "SubmitEvent",
                        "required": True,
                        "description": "回车键事件。"
                    }
                }
            },
            "onEditChanged": {
                "description": "输入状态变化时，触发该回调。",
                "params": {
                    "isEditing": {
                        "type": "boolean",
                        "required": True,
                        "description": "为True表示正在输入。"
                    }
                }
            },
            "onEditChange": {
                "description": "输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。isEditing为True表示正在输入。",
                "params": {
                    "isEditing": {
                        "type": "boolean",
                        "required": True,
                        "description": "为True表示正在输入。"
                    }
                }
            },
            "onCopy": {
                "description": "长按输入框内部区域弹出剪贴板后，点击剪切板复制按钮，触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "复制的文本内容。"
                    }
                }
            },
            "onCut": {
                "description": "长按输入框内部区域弹出剪贴板后，点击剪切板剪切按钮，触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "剪切的文本内容。"
                    }
                }
            },
            "onPaste": {
                "description": "长按输入框内部区域弹出剪贴板后，点击剪切板粘贴按钮，触发该回调。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "粘贴的文本内容。"
                    },
                    "event": {
                        "type": "PasteEvent",
                        "required": False,
                        "description": "用户自定义的粘贴事件。"
                    }
                }
            },
            "onTextSelectionChange": {
                "description": "文本选择的位置发生变化时，触发该回调。",
                "params": {
                    "selectionStart": {
                        "type": "number",
                        "required": True,
                        "description": "所选文本的起始位置，文字的起始位置为0。"
                    },
                    "selectionEnd": {
                        "type": "number",
                        "required": True,
                        "description": "所选文本的结束位置。"
                    }
                }
            },
            "onContentScroll": {
                "description": "文本内容滚动时，触发该回调。",
                "params": {
                    "totalOffsetX": {
                        "type": "number",
                        "required": True,
                        "description": "文本在内容区的横坐标偏移，单位px。"
                    },
                    "totalOffsetY": {
                        "type": "number",
                        "required": True,
                        "description": "文本在内容区的纵坐标偏移，单位px。"
                    }
                }
            },
            "onSecurityStateChange": {
                "description": "密码显隐状态切换时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<boolean>",
                        "required": True,
                        "description": "回调函数。"
                    }
                }
            },
            "onWillInsert": {
                "description": "在将要输入时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<InsertValue, boolean>",
                        "required": True,
                        "description": "在将要输入时调用的回调。在返回True时，表示正常插入，返回False时，表示不插入。"
                    }
                }
            },
            "onDidInsert": {
                "description": "在输入完成时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<InsertValue>",
                        "required": True,
                        "description": "在输入完成时调用的回调。"
                    }
                }
            },
            "onWillDelete": {
                "description": "在将要删除时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<DeleteValue, boolean>",
                        "required": True,
                        "description": "在将要删除时调用的回调。在返回True时，表示正常删除，返回False时，表示不删除。"
                    }
                }
            },
            "onDidDelete": {
                "description": "在删除完成时，触发该回调。",
                "params": {
                    "callback": {
                        "type": "Callback<DeleteValue>",
                        "required": True,
                        "description": "在删除完成时调用的回调。"
                    }
                }
            }
        },
        "examples": [
            # """示例1: TextInput基本使用示例。该结构体实现了一个文本输入示例，包括文本输入框、密码输入框、邮箱地址输入框和内联风格输入框等功能。\n\n- text: 用于存储文本输入框中的文本内容\n- positionInfo: 用于存储光标位置信息\n- passwordState: 用于控制密码输入框的显示状态\n- controller: 文本输入控制器\n\n主要功能包括：\n1. 构建文本输入框，设置样式和事件处理：\n   - 设置文本内容、占位符、控制器等属性\n   - 设置样式包括占位符颜色、字体大小、光标颜色等\n   - 添加输入过滤器和内容改变事件处理\n2. 设置按钮，实现光标位置移动和获取光标位置功能\n3. 构建密码输入框，设置样式和密码显示状态切换事件处理\n4. 构建邮箱地址输入框，设置样式和内容类型\n5. 构建内联风格输入框，设置样式和内容\n// xxx.ets\n@Entry\n@Component\nstruct TextInputExample {\n  @State text: string = ''\n  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 }\n  @State passwordState: boolean = false\n  controller: TextInputController = new TextInputController()\n\n  build() {\n    Column() {\n      TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })\n        .placeholderColor(Color.Grey)\n        .placeholderFont({ size: 14, weight: 400 })\n        .caretColor(Color.Blue)\n        .width('95%')\n        .height(40)\n        .margin(20)\n        .fontSize(14)\n        .fontColor(Color.Black)\n        .inputFilter('[a-z]', (e) => {\n          console.log(JSON.stringify(e))\n        })\n        .onChange((value: string) => {\n          this.text = value\n        })\n      Text(this.text)\n      Button('Set caretPosition 1')\n        .margin(15)\n        .onClick(() => {\n          // 将光标移动至第一个字符后\n          this.controller.caretPosition(1)\n        })\n      Button('Get CaretOffset')\n        .margin(15)\n        .onClick(() => {\n          this.positionInfo = this.controller.getCaretOffset()\n        })\n      // 密码输入框\n      TextInput({ placeholder: 'input your password...' })\n        .width('95%')\n        .height(40)\n        .margin(20)\n        .type(InputType.Password)\n        .maxLength(9)\n        .showPasswordIcon(true)\n        .showPassword(this.passwordState)\n        .onSecurityStateChange(((isShowPassword: boolean) => {\n          // 更新密码显示状态\n          console.info('isShowPassword',isShowPassword)\n          this.passwordState = isShowPassword\n        }))\n      // 邮箱地址自动填充类型\n      TextInput({ placeholder: 'input your email...' })\n        .width('95%')\n        .height(40)\n        .margin(20)\n        .contentType(ContentType.EMAIL_ADDRESS)\n        .maxLength(9)\n      // 内联风格输入框\n      TextInput({ text: 'inline style' })\n        .width('95%')\n        .height(50)\n        .margin(20)\n        .borderRadius(0)\n        .style(TextInputStyle.Inline)\n    }.width('100%')\n  }\n}"""
            # """示例2: passwordIcon、showUnderline、showUnit、showError属性接口使用示例。/**\n * TextInputExample是一个文本输入示例组件，包含了自定义密码显示图标、下划线模式、用户名输入等功能。\n * \n * 属性：\n * - PassWordSrc1: 密码显示图标资源1\n * - PassWordSrc2: 密码显示图标资源2\n * - TextError: 错误提示文本\n * - Text: 文本输入内容\n * - NameText: 默认用户名\n * \n * 方法：\n * - itemEnd(): 构建下拉选择框\n * - build(): 构建整体布局，包括自定义密码显示图标、下划线模式、用户名输入等功能\n * \n * TextInputExample组件实现了用户输入密码、显示错误提示、自定义样式等功能。\n */\n**/\n@Entry\n@Component\nstruct TextInputExample {\n  @State PassWordSrc1: Resource = $r('app.media.onIcon')\n  @State PassWordSrc2: Resource = $r('app.media.offIcon')\n  @State TextError: string = ''\n  @State Text: string = ''\n  @State NameText: string = 'test'\n\n  @Builder itemEnd() {\n    Select([{ value: 'KB' },\n      { value: 'MB' },\n      { value: 'GB' },\n      { value: 'TB', }])\n      .height("48vp")\n      .borderRadius(0)\n      .selected(2)\n      .align(Alignment.Center)\n      .value('MB')\n      .font({ size: 20, weight: 500 })\n      .fontColor('#182431')\n      .selectedOptionFont({ size: 20, weight: 400 })\n      .optionFont({ size: 20, weight: 400 })\n      .backgroundColor(Color.Transparent)\n      .responseRegion({ height: "40vp", width: "80%", x: '10%', y: '6vp' })\n      .onSelect((index: number) => {\n        console.info('Select:' + index)\n      })\n  }\n\n  build() {\n    Column({ space: 20 }) {\n      // 自定义密码显示图标\n      TextInput({ placeholder: 'user define password icon' })\n        .type(InputType.Password)\n        .width(380)\n        .height(60)\n        .passwordIcon({ onIconSrc: this.PassWordSrc1, offIconSrc: this.PassWordSrc2 })\n      // 下划线模式\n      TextInput({ placeholder: 'underline style' })\n        .showUnderline(true)\n        .width(380)\n        .height(60)\n        .showError('Error')\n        .showUnit(this.itemEnd)\n\n      Text(`用户名：${this.Text}`)\n        .width('95%')\n      TextInput({ placeholder: '请输入用户名', text: this.Text })\n        .showUnderline(true)\n        .width(380)\n        .showError(this.TextError)\n        .onChange((value: string) => {\n          this.Text = value\n        })\n        .onSubmit(() => { // 用户名不正确会清空输入框和用户名并提示错误文本\n          if (this.Text == this.NameText) {\n            this.TextError = ''\n          } else {\n            this.TextError = '用户名输入错误'\n            this.Text = ''\n          }\n        })\n\n    }.width('100%')\n  }\n}"""
            # """示例3: TextInput绑定自定义键盘使用示例。整体功能注释：\n\nTextInputExample结构体定义了一个文本输入示例组件，包含自定义键盘功能。通过TextInputController控制文本输入和自定义键盘的交互。用户可以点击自定义键盘上的按钮来输入文本内容，同时可以关闭自定义键盘。整体界面以灰色背景为主题，包括文本输入框和自定义键盘。\n\n功能包括：\n1. 初始化文本输入控制器和输入值\n2. 自定义键盘组件的构建，包括按钮和布局\n3. 绑定自定义键盘到文本输入框\n4. 实现按钮点击事件，更新输入值\n5. 控制自定义键盘的显示和关闭\n// xxx.ets\n@Entry\n@Component\nstruct TextInputExample {\n  controller: TextInputController = new TextInputController()\n  @State inputValue: string = ""\n\n  // 自定义键盘组件\n  @Builder CustomKeyboardBuilder() {\n    Column() {\n      Button('x').onClick(() => {\n        // 关闭自定义键盘\n        this.controller.stopEditing()\n      })\n      Grid() {\n        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item:number|string) => {\n          GridItem() {\n            Button(item + "")\n              .width(110).onClick(() => {\n              this.inputValue += item\n            })\n          }\n        })\n      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)\n    }.backgroundColor(Color.Gray)\n  }\n\n  build() {\n    Column() {\n      TextInput({ controller: this.controller, text: this.inputValue })\n        // 绑定自定义键盘\n        .customKeyboard(this.CustomKeyboardBuilder()).margin(10).border({ width: 1 }).height('48vp')\n    }\n  }\n}"""
            # """示例4: cancelButton属性接口使用示例。这段代码展示了一个自定义的清除节点示例，包括一个输入框和一个清除按钮。用户可以在输入框中输入文本，清除按钮可以清除输入框中的内容。输入框的宽度为380，高度为60，具有取消按钮功能，点击取消按钮可以清空输入框内容。输入框的文本内容会实时更新到状态变量中。\n\n另外，还提供了一个按钮示例，展示了一个自定义样式的按钮组件。按钮显示为“OK”，并包含一个开关控件用于启用或禁用按钮。按钮点击时会记录点击位置的坐标，并在按钮上显示这些坐标。按钮的按压状态和启用状态也会在按钮上显示。用户可以根据按钮的状态进行相应的操作，如启用或禁用按钮。\n// xxx.ets\n@Entry\n@Component\nstruct ClearNodeExample {\n  @State text: string = ''\n  controller: TextInputController = new TextInputController()\n\n  build() {\n    Column() {\n      TextInput({ placeholder: 'input ...', controller: this.controller })\n        .width(380)\n        .height(60)\n        .cancelButton({\n          style: CancelButtonStyle.CONSTANT,\n          icon: {\n            size: 45,\n            src: $r('app.media.icon'),\n            color: Color.Blue\n          }\n        })\n        .onChange((value: string) => {\n          this.text = value\n        })\n    }\n  }\n}"""
            # """示例5: TextInput计数器使用示例。TextInputExample结构体定义了一个文本输入示例组件，用于展示一个可输入文本的框，并实现了字符计数器功能。用户可以输入文本内容，同时会显示当前输入字符数和最大字符限制数的比例，当输入字符数达到最大字符限制的50%时，字符计数器会显示。用户还可以自定义是否显示红色边框。当文本内容发生改变时，会更新文本状态。\n\nButtonExample结构体定义了一个按钮示例组件，包含一个按钮和一个开关控件。按钮显示为“OK”，点击按钮会记录点击位置的坐标并显示在按钮上。按钮的样式和行为通过MyButtonStyle类和buildButton1函数进行自定义。按钮的按压状态和启用状态也会在按钮上显示。用户可以通过开关控件启用或禁用按钮，同时按钮的样式会根据按压状态和启用状态进行相应的变化。\n```\n// xxx.ets\n@Entry\n@Component\nstruct TextInputExample {\n  @State text: string = ''\n  controller: TextInputController = new TextInputController()\n\n  build() {\n    Column() {\n      TextInput({ text: this.text, controller: this.controller })\n        .placeholderFont({ size: 16, weight: 400 })\n        .width(336)\n        .height(56)\n        .maxLength(6)\n        .showUnderline(true)\n        .showCounter(true, { thresholdPercentage: 50, highlightBorder: true })\n        //计数器显示效果为用户当前输入字符数/最大字符限制数。最大字符限制数通过maxLength()接口设置。\n        //如果用户当前输入字符数达到最大字符限制乘50%（thresholdPercentage）。字符计数器显示。\n        //用户设置highlightBorder为false时，配置取消红色边框。不设置此参数时，默认为true。\n        .onChange((value: string) => {\n          this.text = value\n        })\n    }.width('100%').height('100%').backgroundColor('#F1F3F5')\n  }\n}"""
            # """示例6: 本示例展示如何在TextInput上将电话号码格式化为XXX XXXX XXXX。# 功能注释\n\n该代码实现了一个电话号码输入组件，用户可以输入电话号码并根据一定规则格式化显示。具体功能如下：\n\n1. `phone_example` 结构体定义了电话号码输入组件，包括状态变量、方法和构建函数。\n2. `isEmpty` 方法用于判断字符串是否为空或只包含空格。\n3. `checkNeedNumberSpace` 方法用于检查电话号码是否需要添加空格。\n4. `removeSpace` 方法用于移除字符串中的空格。\n5. `setCaret` 方法用于设置光标位置。\n6. `calcCaretPosition` 方法用于计算光标位置的变化。\n7. `build` 方法构建了电话号码输入组件的外观和行为，包括文本输入、格式化显示、光标位置记录等功能。\n\n在 `build` 方法中：\n- 使用 `TextInput` 组件接收用户输入，并根据一定规则格式化显示电话号码。\n- 监听用户输入变化，根据输入内容调整光标位置。\n- 记录光标位置的变化，以便在用户操作时保持正确的光标位置。\n@Entry\n@Component\nstruct phone_example {\n  @State submitValue: string = ''\n  @State text: string = ''\n  public readonly NUM_TEXT_MAXSIZE_LENGTH = 13\n  @State teleNumberNoSpace: string = ""\n  @State nextCaret: number = -1 // 用于记录下次光标设置的位置\n  @State actualCh: number = -1 // 用于记录光标在第i个数字后插入或者第i个数字前删除\n  @State lastCaretPosition: number = 0\n  @State lastCaretPositionEnd: number = 0\n  controller: TextInputController = new TextInputController()\n\n  isEmpty(str?: string): boolean {\n    return str == 'undefined' || !str || !new RegExp("[^\\\\s]").test(str)\n  }\n\n  checkNeedNumberSpace(numText: string) {\n    let isSpace: RegExp = new RegExp('[\\\\+;,#\\\\*]', 'g')\n    let isRule: RegExp = new RegExp('^\\\\+.*')\n\n    if (isSpace.test(numText)) {\n      // 如果电话号码里有特殊字符，就不加空格\n      if (isRule.test(numText)) {\n        return true\n      } else {\n        return false\n      }\n    }\n    return true;\n  }\n\n  removeSpace(str: string): string {\n    if (this.isEmpty(str)) {\n      return ''\n    }\n    return str.replace(new RegExp("[\\\\s]", "g"), '')\n  }\n\n  setCaret() {\n    if (this.nextCaret != -1) {\n      console.log("to keep caret position right, change caret to", this.nextCaret)\n      this.controller.caretPosition(this.nextCaret)\n      this.nextCaret = -1\n    }\n  }\n\n  calcCaretPosition(nextText: string) {\n    let befNumberNoSpace: string = this.removeSpace(this.text)\n    this.actualCh = 0\n    if (befNumberNoSpace.length < this.teleNumberNoSpace.length) { // 插入场景\n      for (let i = 0; i < this.lastCaretPosition; i++) {\n        if (this.text[i] != ' ') {\n          this.actualCh += 1\n        }\n      }\n      this.actualCh += this.teleNumberNoSpace.length - befNumberNoSpace.length\n      console.log("actualCh: " + this.actualCh)\n      for (let i = 0; i < nextText.length; i++) {\n        if (nextText[i] != ' ') {\n          this.actualCh -= 1\n          if (this.actualCh <= 0) {\n            this.nextCaret = i + 1\n            break;\n          }\n        }\n      }\n    } else if (befNumberNoSpace.length > this.teleNumberNoSpace.length) { // 删除场景\n      if (this.lastCaretPosition === this.text.length) {\n        console.log("Caret at last, no need to change")\n      } else if (this.lastCaretPosition === this.lastCaretPositionEnd) {\n        // 按键盘上回退键一个一个删的情况\n        for (let i = this.lastCaretPosition; i < this.text.length; i++) {\n          if (this.text[i] != ' ') {\n            this.actualCh += 1\n          }\n        }\n        for (let i = nextText.length - 1; i >= 0; i--) {\n          if (nextText[i] != ' ') {\n            this.actualCh -= 1\n            if (this.actualCh <= 0) {\n              this.nextCaret = i\n              break;\n            }\n          }\n        }\n      } else {\n        // 剪切/手柄选择 一次删多个字符\n        this.nextCaret = this.lastCaretPosition // 保持光标位置\n      }\n    }\n  }\n\n  build() {\n    Column() {\n      Row() {\n        TextInput({ text: `${this.text}`, controller: this.controller }).type(InputType.PhoneNumber).height('48vp')\n          .onChange((number: string) => {\n            this.teleNumberNoSpace = this.removeSpace(number);\n            let nextText: string = ""\n            if (this.teleNumberNoSpace.length > this.NUM_TEXT_MAXSIZE_LENGTH - 2) {\n              nextText = this.teleNumberNoSpace\n            } else if (this.checkNeedNumberSpace(number)) {\n              if (this.teleNumberNoSpace.length <= 3) {\n                nextText = this.teleNumberNoSpace\n              } else {\n                let split1: string = this.teleNumberNoSpace.substring(0, 3)\n                let split2: string = this.teleNumberNoSpace.substring(3)\n                nextText = split1 + ' ' + split2\n                if (this.teleNumberNoSpace.length > 7) {\n                  split2 = this.teleNumberNoSpace.substring(3, 7)\n                  let split3: string = this.teleNumberNoSpace.substring(7)\n                  nextText = split1 + ' ' + split2 + ' ' + split3\n                }\n              }\n            } else {\n              nextText = number\n            }\n            console.log("onChange Triggered:" + this.text + "|" + nextText + "|" + number)\n            if (this.text === nextText && nextText === number) {\n              // 此时说明数字已经格式化完成了 在这个时候改变光标位置不会被重置掉\n              this.setCaret()\n            } else {\n              this.calcCaretPosition(nextText)\n            }\n            this.text = nextText\n          })\n          .onTextSelectionChange((selectionStart, selectionEnd) => {\n            // 记录光标位置\n            console.log("selection change: ", selectionStart, selectionEnd)\n            this.lastCaretPosition = selectionStart\n            this.lastCaretPositionEnd = selectionEnd\n          })\n      }\n    }\n    .width('100%')\n    .height("100%")\n  }\n}"""
            # """示例7: 本示例展示如何在下划线开启时，设置下划线颜色。/**\n * 该代码定义了一个名为Index的组件，用于构建一个界面布局，包含两个TextInput组件，每个组件具有不同的提示文本内容和下划线颜色。\n * 通过build方法构建界面布局，其中包含一个Row和一个Column，Row占据100%宽度，Column包含两个TextInput组件，设置下划线颜色和显示下划线。\n * TextInput组件可以根据不同状态显示不同颜色的下划线，如正常、输入中、错误和禁用状态。\n */\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    Row() {\n      Column() {\n        TextInput({placeholder:'提示文本内容'})\n          .showUnderline(true)\n          .underlineColor({normal:Color.Orange,typing:Color.Green,error:Color.Red,disable:Color.Gray});\n        TextInput({placeholder:'提示文本内容'})\n          .showUnderline(true)\n          .underlineColor(Color.Gray);\n      }\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"""
            # """示例8: 示例展示设置不同wordBreak属性的TextInput样式。/**\n * TextInputExample 是一个展示不同样式和属性的文本输入组件的结构体。\n * 该结构体包含了多个示例，展示了不同的文本输入情况：\n * 1. TextInput为inline模式，WordBreakType属性为NORMAL的样式；\n * 2. TextInput为inline模式，英文文本，WordBreakType属性为BREAK_ALL的样式；\n * 3. TextInput为inline模式，中文文本，WordBreakType属性为BREAK_ALL的样式；\n * 4. TextInput为inline模式，WordBreakType属性为BREAK_WORD的样式。\n * 每个示例包含了设置文本内容、字体大小、样式和WordBreakType属性的操作。\n */\n// xxx.ets\n@Entry\n@Component\nstruct TextInputExample {\n  build() {\n    Column() {\n      Text("TextInput为inline模式，WordBreakType属性为NORMAL的样式：").fontSize(16).fontColor(0xFF0000)\n      TextInput({\n        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'\n      })\n        .fontSize(16)\n        .style(TextInputStyle.Inline) // Inline模式\n        .wordBreak(WordBreak.NORMAL) // 非Inline模式该属性无效\n\n      Text("TextInput为inline模式，英文文本，WordBreakType属性为BREAK_ALL的样式：").fontSize(16).fontColor(0xFF0000)\n      TextInput({\n        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'\n      })\n        .fontSize(16)\n        .style(TextInputStyle.Inline)\n        .wordBreak(WordBreak.BREAK_ALL)\n\n      Text("TextInput为inline模式，中文文本，WordBreakType属性为BREAK_ALL的样式：").fontSize(16).fontColor(0xFF0000)\n      TextInput({\n        text: '多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。\\n高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。'\n      })\n        .fontSize(16)\n        .style(TextInputStyle.Inline)\n        .wordBreak(WordBreak.BREAK_ALL)\n\n      Text("TextInput为inline模式，WordBreakType属性为BREAK_WORD的样式：").fontSize(16).fontColor(0xFF0000)\n      TextInput({\n        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'\n      })\n        .fontSize(16)\n        .style(TextInputStyle.Inline)\n        .wordBreak(WordBreak.BREAK_WORD)\n    }\n  }\n}"""
            # """示例9: 该示例实现了使用lineHeight设置文本的文本行高，使用letterSpacing设置文本字符间距，使用decoration设置文本装饰线样式。/**\n * TextInputExample 结构体定义了一个文本输入示例组件，用于展示不同文本样式的输入框。\n * 该组件包含了设置行高、字母间距和装饰样式的功能。\n * \n * 功能包括：\n * - 展示不同行高的文本输入框\n * - 展示不同字母间距的文本输入框\n * - 展示不同装饰样式（删除线、上划线、下划线）的文本输入框\n * \n * 通过设置不同的属性，可以自定义文本输入框的外观和样式。\n * \n * 注意：该组件需要在合适的容器中进行渲染，以展示其功能和效果。\n */\n@Entry\n@Component\nstruct TextInputExample {\n  build() {\n    Row() {\n      Column() {\n        Text('lineHeight').fontSize(9).fontColor(0xCCCCCC)\n        TextInput({text: 'lineHeight unset'})\n          .border({ width: 1 }).padding(10).margin(5)\n        TextInput({text: 'lineHeight 15'})\n          .border({ width: 1 }).padding(10).margin(5).lineHeight(15)\n        TextInput({text: 'lineHeight 30'})\n          .border({ width: 1 }).padding(10).margin(5).lineHeight(30)\n\n        Text('letterSpacing').fontSize(9).fontColor(0xCCCCCC)\n        TextInput({text: 'letterSpacing 0'})\n          .border({ width: 1 }).padding(5).margin(5).letterSpacing(0)\n        TextInput({text: 'letterSpacing 3'})\n          .border({ width: 1 }).padding(5).margin(5).letterSpacing(3)\n        TextInput({text: 'letterSpacing -1'})\n          .border({ width: 1 }).padding(5).margin(5).letterSpacing(-1)\n\n        Text('decoration').fontSize(9).fontColor(0xCCCCCC)\n        TextInput({text: 'LineThrough, Red'})\n          .border({ width: 1 }).padding(5).margin(5)\n          .decoration({type: TextDecorationType.LineThrough, color: Color.Red})\n        TextInput({text: 'Overline, Red, DASHED'})\n          .border({ width: 1 }).padding(5).margin(5)\n          .decoration({type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED})\n        TextInput({text: 'Underline, Red, WAVY'})\n          .border({ width: 1 }).padding(5).margin(5)\n          .decoration({type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY})\n      }.height('90%')\n    }\n    .width('90%')\n    .margin(10)\n  }\n}"""
            # """示例10: fontFeature属性使用示例，对比了fontFeature使用ss01属性和不使用ss01属性的效果。/**\n * 该代码定义了一个名为textInput的组件结构体，包含两个文本输入框，分别显示不同的文本内容，并设置了特定的样式。\n * text1显示为'This is ss01 on : 0123456789'，text2显示为'This is ss01 off: 0123456789'。\n * 通过build方法构建了一个Column布局，包含两个TextInput组件，分别显示text1和text2的内容。\n * text1的样式设置为fontSize为20，顶部margin为200，字体特性为"ss01 on"；text2的样式设置为顶部margin为10，fontSize为20，字体特性为"ss01 off"。\n * 整体布局的宽度设置为"90%"，外边距设置为"5%"。\n */\n@Entry\n@Component\nstruct textInput {\n  @State text1: string = 'This is ss01 on : 0123456789'\n  @State text2: string = 'This is ss01 off: 0123456789'\n\n\n\n  build() {\n    Column(){\n      TextInput({text: this.text1})\n        .fontSize(20)\n        .margin({top:200})\n        .fontFeature("\\"ss01\\" on")\n      TextInput({text : this.text2})\n        .margin({top:10})\n        .fontSize(20)\n        .fontFeature("\\"ss01\\" off")\n    }\n    .width("90%")\n    .margin("5%")\n  }\n}"""
            # """示例11: 自定义键盘弹出发生避让示例。/**\n * 该代码定义了一个输入组件，包括文本输入框、自定义键盘和按钮功能。\n * 输入组件包含一个文本输入控制器、输入值、高度、支持避让等状态。\n * 自定义键盘组件包括关闭键盘按钮和数字/符号按钮，点击按钮会更新输入值。\n * 可以通过按钮切换输入框高度，并绑定自定义键盘到文本输入框。\n * \n * @Entry - 标记为入口组件\n * @Component - 标记为组件\n * struct Input - 定义输入组件结构\n * TextInputController - 文本输入控制器\n * inputValue - 输入值状态\n * height1 - 高度状态\n * supportAvoidance - 支持避让状态\n * CustomKeyboardBuilder - 自定义键盘构建器\n * build - 构建输入组件\n * Button - 按钮组件\n * Row - 水平布局\n * Column - 垂直布局\n * Grid - 网格布局\n * ForEach - 遍历数组\n * GridItem - 网格项\n * TextInput - 文本输入框组件\n * backgroundColor - 背景颜色\n * fontSize - 字体大小\n * justifyContent - 主轴对齐方式\n...\n * columnsGap - 列间距\n * rowsGap - 行间距\n * customKeyboard - 绑定自定义键盘\n */\n@Entry\n@Component\nstruct Input {\n  controller: TextInputController = new TextInputController()\n  @State inputValue: string = ""\n  @State height1:string|number = '80%'\n  @State supportAvoidance:boolean = true;\n  // 自定义键盘组件\n  @Builder CustomKeyboardBuilder() {\n    Column() {\n      Row(){\n        Button('x').onClick(() => {\n          // 关闭自定义键盘\n          this.controller.stopEditing()\n        }).margin(10)\n      }\n      Grid() {\n        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item:number|string) => {\n          GridItem() {\n            Button(item + "")\n              .width(110).onClick(() => {\n              this.inputValue += item\n            })\n          }\n        })\n      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)\n    }.backgroundColor(Color.Gray)\n  }\n  build() {\n    Column() {\n      Row(){\n        Button("20%")\n          .fontSize(24)\n          .onClick(()=>{\n            this.height1 = "20%"\n          })\n        Button("80%")\n          .fontSize(24)\n          .margin({left:20})\n          .onClick(()=>{\n            this.height1 = "80%"\n          })\n      }\n      .justifyContent(FlexAlign.Center)\n      .alignItems(VerticalAlign.Bottom)\n      .height(this.height1)\n      .width("100%")\n      .padding({bottom:50})\n      TextInput({ controller: this.controller, text: this.inputValue })\n        // 绑定自定义键盘\n        .customKeyboard(this.CustomKeyboardBuilder(),{ supportAvoidance: this.supportAvoidance }).margin(10).border({ width: 1 })\n\n    }\n  }\n}"""
            # """示例12: 该示例实现了使用minFontSize，maxFontSize及heightAdaptivePolicy设置文本自适应字号。**\n * TextInputExample结构体实现了一个文本输入示例，包括设置不同的高度自适应策略。\n * 通过构建不同的TextInput组件展示文本，并设置不同的属性，如宽度、高度、边框宽度、边距、最小字体大小、最大字体大小、最大行数以及高度自适应策略。\n * 高度自适应策略包括MAX_LINES_FIRST（最大行数优先）、MIN_FONT_SIZE_FIRST（最小字体大小优先）和LAYOUT_CONSTRAINT_FIRST（布局约束优先）。\n * 该示例展示了如何使用TextInput组件以及设置不同的属性和高度自适应策略。\n */\n \n/**\n * MyButtonStyle类实现了自定义按钮样式，包括记录点击位置的坐标、设置选中颜色等属性。\n * 通过applyContent方法应用buildButton1函数来自定义按钮的样式和行为。\n */\n \n/**\n * buildButton1函数用于构建按钮的内容，包括显示按钮是否启用、按钮按压状态、点击位置坐标等信息。\n * 通过传入ButtonConfiguration配置参数，展示按钮的状态和样式。\n */\n\n/**\n * ButtonExample结构体实现了一个按钮示例，包括自定义按钮样式、记录点击位置坐标、按钮启用状态等功能。\n * 通过构建按钮和开关控件展示按钮的样式和行为，包括启用状态、点击位置坐标等信息。\n */\n@Entry\n@Component\nstruct TextInputExample {\n  build() {\n    Row() {\n      Column() {\n        Text('heightAdaptivePolicy').fontSize(9).fontColor(0xCCCCCC)\n        TextInput({text: 'This is the text without the height adaptive policy set'})\n          .width('80%').height(50).borderWidth(1).margin(1)\n        TextInput({text: 'This is the text with the height adaptive policy set'})\n          .width('80%').height(50).borderWidth(1).margin(1)\n          .minFontSize(4)\n          .maxFontSize(40)\n          .maxLines(3)\n          .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX_LINES_FIRST)\n        TextInput({text: 'This is the text with the height adaptive policy set'})\n          .width('80%').height(50).borderWidth(1).margin(1)\n          .minFontSize(4)\n          .maxFontSize(40)\n          .maxLines(3)\n          .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST)\n        TextInput({text: 'This is the text with the height adaptive policy set'})\n          .width('80%').height(50).borderWidth(1).margin(1)\n          .minFontSize(4)\n          .maxFontSize(40)\n          .maxLines(3)\n          .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)\n      }.height('90%')\n    }\n    .width('90%')\n    .margin(10)\n  }\n}"""
            # """示例13: lineBreakStrategy使用示例，对比了不设置lineBreakStrategy与lineBreakStrategy设置不同挡位的效果。/**\n * 该代码定义了一个名为 TextExample1 的组件，包含一个默认文本消息和一个构建方法 build()。\n * 文本消息可以通过 TextInput 组件进行展示和编辑，支持不同的换行策略。\n * 构建方法 build() 中使用了 Flex 布局，依次展示了三个文本输入框，每个文本输入框对应不同的换行策略。\n * 组件整体高度为 700，宽度为 370，设置了一定的内边距。\n */\n@Entry\n@Component\nstruct TextExample1 {\n  @State message1: string = "They can be classified as built-in components–those directly provided by the ArkUI framework and custom components – those defined by developers" +\n    "The built-in components include buttons radio buttonsprogress indicators and text You can set the rendering effectof thesecomponents in method chaining mode," +\n    "page components are divided into independent UI units to implementindependent creation development and reuse of different units on pages making pages more engineering-oriented.";\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {\n      Text('LineBreakStrategy.GREEDY').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextInput({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .maxLines(5)\n        .style(TextInputStyle.Inline)\n        .lineBreakStrategy(LineBreakStrategy.GREEDY)\n      Text('LineBreakStrategy.HIGH_QUALITY').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextInput({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .maxLines(5)\n        .style(TextInputStyle.Inline)\n        .lineBreakStrategy(LineBreakStrategy.HIGH_QUALITY)\n      Text('LineBreakStrategy.BALANCED').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)\n      TextInput({text: this.message1})\n        .fontSize(12)\n        .border({ width: 1 })\n        .padding(10)\n        .width('100%')\n        .maxLines(5)\n        .style(TextInputStyle.Inline)\n        .lineBreakStrategy(LineBreakStrategy.BALANCED)\n    }.height(700).width(370).padding({ left: 35, right: 35, top: 35 })\n  }\n}"""
            # """示例14: 该实例展示输入框支持插入和删除回调。/**\n * TextInputExample是一个组件，用于展示TextInput的插入和删除回调功能。\n * 用户可以在输入框中插入文本并触发插入回调，也可以删除文本并触发删除回调。\n * 组件包含两个TextInput，分别用于展示插入回调和删除回调的功能。\n * 用户可以看到插入的文本值、插入的偏移量、删除的文本值、删除的偏移量以及删除的方向。\n * 当用户操作输入框时，相应的回调函数会更新组件状态并显示在界面上。\n */\n        \n/**\n * ButtonExample是一个展示自定义按钮样式和行为的组件。\n * 用户可以点击按钮，记录点击位置的坐标并在按钮上显示。\n * 按钮的按压状态和启用状态也会在按钮上显示。\n * 用户可以通过按钮控制按钮的启用状态，并根据按压状态改变按钮的样式。\n * 组件包含一个按钮和一个开关控件，用于启用或禁用按钮。\n * 当用户点击按钮时，按钮的样式和状态会相应改变。\n */\n **/\n// xxx.ets\n@Entry\n@Component\nstruct TextInputExample {\n  @State insertValue: string = ""\n  @State deleteValue: string = ""\n  @State insertOffset: number = 0\n  @State deleteOffset: number = 0\n  @State deleteDirection: number = 0\n\n  build() {\n    Row() {\n      Column() {\n        TextInput({ text: "TextInput支持插入回调文本" })\n          .height(60)\n          .onWillInsert((info: InsertValue) => {\n            this.insertValue = info.insertValue\n            return true;\n          })\n          .onDidInsert((info: InsertValue) => {\n            this.insertOffset = info.insertOffset\n          })\n\n        Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(30)\n\n        TextInput({ text: "TextInput支持删除回调文本b" })\n          .height(60)\n          .onWillDelete((info: DeleteValue) => {\n            this.deleteValue = info.deleteValue\n            info.direction\n            return true;\n          })\n          .onDidDelete((info: DeleteValue) => {\n            this.deleteOffset = info.deleteOffset\n            this.deleteDirection = info.direction\n          })\n\n        Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(30)\n        Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(30)\n\n      }.width('100%')\n    }\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    },
    "XComponent": {
        "description": "可用于EGL/OpenGLES和媒体数据写入，并显示在XComponent组件。",
        "interfaces": [
            {
                "description": "XComponent(value: {id: string, type: string, libraryname?: string, controller?: XComponentController})",
                "params": {
                    "id": {
                        "type": "string",
                        "required": True,
                        "description": "组件的唯一标识，支持最大的字符串长度128。"
                    },
                    "type": {
                        "type": "string",
                        "required": True,
                        "description": "用于指定XComponent组件类型，可选值仅有两个为：\n- 'surface'：用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容单独展示到屏幕上。\n- 'component'9+ ：XComponent将变成一个容器组件，并可在其中执行非UI逻辑以动态加载显示内容。\n其他值均会被视为'surface'类型"
                    },
                    "libraryname": {
                        "type": "string",
                        "required": False,
                        "description": "应用Native层编译输出动态库名称，仅XComponent类型为'surface'时有效。"
                    },
                    "controller": {
                        "type": "XComponentController",
                        "required": False,
                        "description": "给组件绑定一个控制器，通过控制器调用组件方法，仅XComponent类型为'surface'时有效。"
                    }
                }
            },
            {
                "description": "XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})",
                "params": {
                    "id": {
                        "type": "string",
                        "required": True,
                        "description": "组件的唯一标识，支持最大的字符串长度128。"
                    },
                    "type": {
                        "type": "XComponentType",
                        "required": True,
                        "description": "用于指定XComponent组件类型。"
                    },
                    "libraryname": {
                        "type": "string",
                        "required": False,
                        "description": "用Native层编译输出动态库名称，仅类型为SURFACE或TEXTURE时有效。"
                    },
                    "controller": {
                        "type": "XComponentController",
                        "required": False,
                        "description": "给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。"
                    }
                }
            },
            {
                "description": "XComponent(value: {id: string, type: XComponentType, imageAIOptions: ImageAIOptions, libraryname?: string, controller?: XComponentController})",
                "params": {
                    "id": {
                        "type": "string",
                        "required": True,
                        "description": "组件的唯一标识，支持最大的字符串长度128。"
                    },
                    "type": {
                        "type": "XComponentType",
                        "required": True,
                        "description": "用于指定XComponent组件类型。"
                    },
                    "imageAIOptions": {
                        "type": "ImageAIOptions",
                        "required": True,
                        "description": "给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。"
                    },
                    "libraryname": {
                        "type": "string",
                        "required": False,
                        "description": "用Native层编译输出动态库名称，仅类型为SURFACE或TEXTURE时有效。"
                    },
                    "controller": {
                        "type": "XComponentController",
                        "required": False,
                        "description": "给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。"
                    }
                }
            }
        ],
        "attributes": {
            "enableAnalyzer": {
                "description": "enableAnalyzer(enable: boolean)",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否启用图像分析功能"
                    }
                }
            }
        },
        "events": {
            "onLoad": {
                "description": "onLoad(callback: (event?: object) => void )",
                "params": {
                    "event": {
                        "type": "object",
                        "required": False,
                        "description": "获取XComponent实例对象的context，context上挂载的方法由开发者在c++层定义。"
                    }
                }
            },
            "onDestroy": {
                "description": "onDestroy(event: () => void )",
                "params": {}
            }
        },
        "examples": [
            """// 图像分析功能使用示例\n\n// 自定义XComponentController类，实现对Surface生命周期的监听\n// 当Surface被创建时触发\n// 参数surfaceId: Surface的唯一标识符\n// 输出日志记录Surface创建信息\nonSurfaceCreated(surfaceId: string): void {\n  console.log(`onSurfaceCreated surfaceId: ${surfaceId}`)\n}\n\n// 当Surface尺寸改变时触发\n// 参数surfaceId: Surface的唯一标识符, rect: Surface的矩形信息\n// 输出日志记录Surface尺寸变化信息\nonSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {\n  console.log(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`)\n}\n\n// 当Surface被销毁时触发\n// 参数surfaceId: Surface的唯一标识符\n// 输出日志记录Surface销毁信息\nonSurfaceDestroyed(surfaceId: string): void {\n  console.log(`onSurfaceDestroyed surfaceId: ${surfaceId}`)\n}\n\n// XComponentExample结构体，展示图像分析功能的使用示例\n// 包含图像分析配置、控制器、选项等属性\n@Entry\n@Component\nstruct XComponentExample {\n  xComponentController: XComponentController = new CustomXComponentController() // 实例化自定义XComponentController\n\n  private config: ImageAnalyzerConfig = {\n    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT] // 图像分析配置，包含主体和文本类型\n  }\n\n  private aiController: ImageAnalyzerController = new ImageAnalyzerController() // 图像分析控制器实例化\n\n  private options: ImageAIOptions = {\n    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT], // 图像分析选项，包含主体和文本类型\n    aiController: this.aiController // 关联图像分析控制器\n  }\n\n  @State xcWidth: string = "320px" // XComponent宽度状态\n  @State xcHeight: string = "480px" // XComponent高度状态\n\n  // 构建函数，定义XComponentExample的UI结构\n  build() {\n    Column({ space: 5 }) {\n      // 按钮：改变尺寸\n      // 点击按钮后，修改XComponent的宽度和高度\n      Button("change size")\n        .onClick(() => {\n          this.xcWidth = "640px"\n          this.xcHeight = "720px"\n        })\n\n      // 按钮：启动AI分析\n      // 点击按钮后，调用XComponentController的startImageAnalyzer方法启动图像分析\n      // 输出日志记录分析完成信息或错误信息\n      Button('start AI analyze')\n        .onClick(() => {\n          this.xComponentController.startImageAnalyzer(this.config)\n            .then(() => {\n              console.log("analysis complete")\n            })\n            .catch((error: BusinessError) => {\n              console.log("error code: " + error.code)\n            })\n        })\n\n      // 按钮：停止AI分析\n      // 点击按钮后，调用XComponentController的stopImageAnalyzer方法停止图像分析\n      Button('stop AI analyze')\n        .onClick(() => {\n          this.xComponentController.stopImageAnalyzer()\n        })\n\n      // 按钮：获取分析器类型\n      // 点击按钮后，调用ImageAnalyzerController的getImageAnalyzerSupportTypes方法获取支持的分析器类型\n      Button('get analyzer types')\n        .onClick(() => {\n          this.aiController.getImageAnalyzerSupportTypes()\n        })\n\n      // XComponent实例化\n      // 设置类型为SURFACE，关联控制器和选项\n      // 设置宽度和高度为状态值\n      XComponent({\n        type: XComponentType.SURFACE,\n        controller: this.xComponentController,\n        imageAIOptions: this.options\n      })\n        .width(this.xcWidth)\n        .height(this.xcHeight)\n    }\n    .width("100%") // 设置Column的宽度为100%\n  }\n}\n```\n// xxx.ets\nimport { BusinessError } from '@kit.BasicServicesKit';\n\nclass CustomXComponentController extends XComponentController {\n  onSurfaceCreated(surfaceId: string): void {\n    console.log(`onSurfaceCreated surfaceId: ${surfaceId}`)\n  }\n\n  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {\n    console.log(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`)\n  }\n\n  onSurfaceDestroyed(surfaceId: string): void {\n    console.log(`onSurfaceDestroyed surfaceId: ${surfaceId}`)\n  }\n}\n\n@Entry\n@Component\nstruct XComponentExample {\n  xComponentController: XComponentController = new CustomXComponentController()\n  private config: ImageAnalyzerConfig = {\n    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]\n  }\n  private aiController: ImageAnalyzerController = new ImageAnalyzerController()\n  private options: ImageAIOptions = {\n    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],\n    aiController: this.aiController\n  }\n  @State xcWidth: string = "320px"\n  @State xcHeight: string = "480px"\n\n  build() {\n    Column({ space: 5 }) {\n      Button("change size")\n        .onClick(() => {\n          this.xcWidth = "640px"\n          this.xcHeight = "720px"\n        })\n      Button('start AI analyze')\n        .onClick(() => {\n          this.xComponentController.startImageAnalyzer(this.config)\n            .then(() => {\n              console.log("analysis complete")\n            })\n            .catch((error: BusinessError) => {\n              console.log("error code: " + error.code)\n            })\n        })\n      Button('stop AI analyze')\n        .onClick(() => {\n          this.xComponentController.stopImageAnalyzer()\n        })\n      Button('get analyzer types')\n        .onClick(() => {\n          this.aiController.getImageAnalyzerSupportTypes()\n        })\n      XComponent({\n        type: XComponentType.SURFACE,\n        controller: this.xComponentController,\n        imageAIOptions: this.options\n      })\n        .width(this.xcWidth)\n        .height(this.xcHeight)\n    }\n    .width("100%")\n  }\n}"""
            """surface旋转过程中锁定功能使用示例。\n\n// xxx.ets\n@Entry\n@Component\nstruct Index{\n  @State isLock: boolean = true; // 控制是否锁定surface旋转的状态，初始值为true表示锁定\n  @State xc_width: number = 500; // surface的宽度\n  @State xc_height: number = 700; // surface的高度\n  myXComponentController: XComponentController = new XComponentController(); // 创建XComponentController实例\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {\n      XComponent({\n        id: 'xComponentId',\n        type: XComponentType.SURFACE,\n        libraryname: 'nativerender',\n        controller: this.myXComponentController\n      })\n      .width(this.xc_width) // 设置surface的宽度\n      .height(this.xc_height) // 设置surface的高度\n      .onLoad(() => {\n        let surfaceRotation: SurfaceRotationOptions = { lock: this.isLock }; // 创建surface旋转选项对象，包括锁定状态\n        this.myXComponentController.setXComponentSurfaceRotation(surfaceRotation); // 设置surface的旋转选项\n        console.log("Surface getXComponentSurfaceRotation lock = " +\n          this.myXComponentController.getXComponentSurfaceRotation().lock); // 打印当前surface的锁定状态\n      })\n    }\n    .width('100%') // 设置Flex容器的宽度为100%\n    .height('100%') // 设置Flex容器的高度为100%\n  }\n}\n```\n\n在以上示例代码中，展示了如何在鸿蒙ArkUI开发中实现surface旋转过程中锁定功能的使用。具体功能与效果描述如下：\n1. `isLock: boolean`：用于控制surface旋转时是否锁定的状态变量，初始值为true表示锁定。\n2. `xc_width: number`、`xc_height: number`：分别表示surface的宽度和高度。\n3. `myXComponentController: XComponentController`：创建了XComponentController实例用于控制XComponent组件。\n4. `build()`方法：构建UI界面的方法，包括Flex布局和XComponent组件的加载。\n5. `onLoad()`方法：在XComponent加载完成后的回调函数中，设置了surface的旋转选项，包括锁定状态，并打印当前surface的锁定状态。\n6. 整体布局：Flex容器设置为垂直方向居中对齐、左对齐，并且XComponent组件的宽度和高度分别使用`xc_width`和`xc_height`变量设置，Flex容器的宽高均为100%。\n// xxx.ets\n@Entry\n@Component\nstruct Index{\n  @State isLock: boolean = true;\n  @State xc_width: number = 500;\n  @State xc_height: number = 700;\n  myXComponentController: XComponentController = new XComponentController();\n\n  build() {\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {\n      XComponent({\n        id: 'xComponentId',\n        type: XComponentType.SURFACE,\n        libraryname: 'nativerender',\n        controller: this.myXComponentController\n      })\n      .width(this.xc_width)\n      .height(this.xc_height)\n      .onLoad(() => {\n        let surfaceRotation: SurfaceRotationOptions = { lock: this.isLock };\n        this.myXComponentController.setXComponentSurfaceRotation(surfaceRotation);\n        console.log("Surface getXComponentSurfaceRotation lock = " +\n          this.myXComponentController.getXComponentSurfaceRotation().lock);\n      })\n    }\n    .width('100%')\n    .height('100%')\n  }\n}"""
        ],
        "is_common_attrs": True
    }
}
