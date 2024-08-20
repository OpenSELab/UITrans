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
            "/*\nCheckbox仅仅包含一个多选框，如果需要实现多选框旁边显示文本，需要与Text组件进行组合。\n实现思路：\n本示例通过使用鸿蒙ArkUI框架，构建了一个包含两个Checkbox组件的界面。每个Checkbox组件都包含一个文本标签，用于标识不同的选项。通过Flex布局和Column、Row组件的使用，确保Checkbox组件在界面中居中显示，并且整个布局适应屏幕的大小。\n\n总体功能与效果描述：\n该界面展示了两个Checkbox组件，每个组件旁边都有一个文本标签。用户可以通过点击Checkbox来选择或取消选择某个选项。整个布局会根据屏幕大小自动调整，确保Checkbox组件始终居中显示。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    Row() {\n      Column() {\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建一个Checkbox组件，设置其宽度和高度\n          // 功能与效果描述：Checkbox组件用于用户选择或取消选择某个选项。设置宽度和高度以确保其显示效果。\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            .width(30)\n            .height(30)\n          // 创建一个文本标签，设置其字体大小\n          // 功能与效果描述：文本标签用于标识Checkbox组件，设置字体大小以确保文本清晰可读。\n          Text('Checkbox1').fontSize(20)\n        }\n\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建一个Checkbox组件，设置其宽度和高度\n          // 功能与效果描述：Checkbox组件用于用户选择或取消选择某个选项。设置宽度和高度以确保其显示效果。\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            .width(30)\n            .height(30)\n          // 创建一个文本标签，设置其字体大小\n          // 功能与效果描述：文本标签用于标识Checkbox组件，设置字体大小以确保文本清晰可读。\n          Text('Checkbox2').fontSize(20)\n        }\n      }\n      .width('100%') // 设置Column的宽度为100%\n    }\n    .height('100%') // 设置Row的高度为100%\n  }\n}",
            "/*\n实现思路：\n本示例通过使用Flex组件来布局复选框和文本，并利用@State装饰器来管理复选框的状态。用户可以通过点击文本来切换复选框的选中状态。\n\n总体功能与效果描述：\n该界面展示了一个复选框和一个文本，用户可以通过点击文本来切换复选框的选中状态。界面设计简洁，易于操作。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct CheckedTextView {\n  @State checked: boolean = false; // 使用@State装饰器来管理复选框的选中状态，初始值为false\n\n  build() {\n    Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\n      Checkbox()\n        .select($$this.checked) // 将复选框的选中状态绑定到@State变量checked\n        .width(30) // 设置复选框的宽度为30\n        .height(30) // 设置复选框的高度为30\n      Text('Click to check')\n        .fontSize(18) // 设置文本的字体大小为18\n        .textAlign(TextAlign.Center) // 设置文本的对齐方式为居中\n        .onClick(() => {\n          this.checked = !this.checked // 点击文本时切换复选框的选中状态\n        })\n    }\n    .width('100%') // 设置Flex组件的宽度为100%\n    .height('100%') // 设置Flex组件的高度为100%\n  }\n}"
            # "/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中使用Checkbox组件。通过创建两个Checkbox实例，并设置其样式和事件处理，展示了Checkbox的基本功能和自定义样式。每个Checkbox都有独立的选中状态和事件回调，用于处理用户交互。\n*/\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    Row() {\n      Column() {\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // Checkbox1组件，用于用户选择，自定义了选中颜色、形状和事件处理\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            .selectedColor(0x39a2db) // 设置选中时的颜色\n            .shape(CheckBoxShape.ROUNDED_SQUARE) // 设置Checkbox的形状为圆角方形\n            .onChange((value: boolean) => {\n              console.info('Checkbox1 change is'+ value) // 当Checkbox状态改变时，输出当前状态\n            })\n            .mark({\n              strokeColor:Color.Black, // 设置标记的颜色\n              size: 50, // 设置标记的大小\n              strokeWidth: 5 // 设置标记的线条宽度\n            })\n            .unselectedColor(Color.Red) // 设置未选中时的颜色\n            .width(30) // 设置Checkbox的宽度\n            .height(30) // 设置Checkbox的高度\n          Text('Checkbox1').fontSize(20) // 显示Checkbox的标签文本\n        }\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // Checkbox2组件，用于用户选择，自定义了选中颜色、形状和事件处理\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            .selectedColor(0x39a2db) // 设置选中时的颜色\n            .shape(CheckBoxShape.ROUNDED_SQUARE) // 设置Checkbox的形状为圆角方形\n            .onChange((value: boolean) => {\n              console.info('Checkbox2 change is' + value) // 当Checkbox状态改变时，输出当前状态\n            })\n            .width(30) // 设置Checkbox的宽度\n            .height(30) // 设置Checkbox的高度\n          Text('Checkbox2').fontSize(20) // 显示Checkbox的标签文本\n        }\n      }\n      .width('100%') // 设置列的宽度为100%\n    }\n    .height('100%') // 设置行的宽度为100%\n  }\n}",
            # "/*\n实现思路：\n本示例代码定义了一个自定义的复选框样式类 `MyCheckboxStyle`，并通过 `buildCheckbox` 函数构建复选框的UI。在主组件 `Index` 中，使用该自定义样式并实现了复选框的状态切换和启用/禁用功能。通过 `Toggle` 组件控制复选框的启用状态。\n该示例实现了自定义复选框样式的功能，自定义样式实现了一个五边形复选框，如果选中，内部会出现红色三角图案，标题会显示选中字样，如果取消选中，红色三角图案消失，标题会显示非选中字样。\n*/\n// xxx.ets\nclass MyCheckboxStyle implements ContentModifier<CheckBoxConfiguration> {\n  selectedColor: Color = Color.White\n  constructor(selectedColor: Color) {\n    this.selectedColor = selectedColor;\n  }\n  applyContent() : WrappedBuilder<[CheckBoxConfiguration]>\n  {\n    return wrapBuilder(buildCheckbox)\n  }\n}\n\n@Builder function buildCheckbox(config: CheckBoxConfiguration) {\n  Column({space:10}) {\n      // 显示复选框的名称和选中状态\n      Text(config.name  + (config.selected ? \"（ 选中 ）\" : \"（ 非选中 ）\")).margin({right : 70, top : 50})\n      // 显示复选框的启用状态\n      Text(config.enabled ? \"enabled true\" : \"enabled false\").margin({right : 110})\n      Shape() {\n        Path().width(100).height(100).commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z').fillOpacity(0).strokeWidth(3).onClick(()=>{\n          // 切换复选框的选中状态\n          if (config.selected) {\n            config.triggerChange(false)\n          } else {\n            config.triggerChange(true)\n          }\n        }).opacity(config.enabled ? 1 : 0.1)\n        Path().width(10).height(10).commands('M50 0 L100 100 L0 100 Z')\n          .visibility(config.selected ? Visibility.Visible : Visibility.Hidden)\n          .fill(config.selected ? (config.contentModifier as MyCheckboxStyle).selectedColor : Color.Black)\n          .stroke((config.contentModifier as MyCheckboxStyle).selectedColor)\n          .margin({left:11,top:10})\n          .opacity(config.enabled ? 1 : 0.1)\n      }\n      .width(300)\n      .height(200)\n      .viewPort({ x: 0, y: 0, width: 310, height: 310 })\n      .strokeLineJoin(LineJoinStyle.Miter)\n      .strokeMiterLimit(5)\n      .margin({left:50})\n  }\n}\n\n@Entry\n@Component\nstruct Index {\n  @State checkboxEnabled: boolean = true;\n  build() {\n    Column({ space: 100 }) {\n        // 使用自定义样式创建复选框，并监听状态变化\n        Checkbox({ name: '复选框状态', group: 'checkboxGroup' })\n        .contentModifier(new MyCheckboxStyle(Color.Red))\n        .onChange((value: boolean) => {\n          console.info('Checkbox change is' + value)\n        }).enabled(this.checkboxEnabled)\n\n      Row() {\n        // 使用Toggle组件控制复选框的启用状态\n        Toggle({ type: ToggleType.Switch, isOn: true }).onChange((value: boolean) => {\n          if (value) {\n            this.checkboxEnabled = true\n          } else {\n            this.checkboxEnabled = false\n          }\n        })\n      }\n    }.margin({top : 30})\n  }\n}",
            # "/*\n实现思路：\n本示例展示了如何使用ArkUI框架创建自定义样式的复选框组件。通过定义一个Builder函数来动态生成复选框的指示器，并根据不同的值显示不同的文本和字体大小。每个复选框都有自己的样式和事件处理逻辑。\n\n总体功能与效果描述：\n该示例包含两个复选框，每个复选框具有不同的形状和指示器样式。第一个复选框为圆形，第二个复选框为圆角矩形。每个复选框的指示器显示一个数字，如果数字大于99，则显示为“99+”。复选框的状态变化会通过控制台输出。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct CheckboxExample {\n  // 定义一个Builder函数，用于生成复选框的指示器\n  @Builder\n  indicatorBuilder(value: number) {\n    Column(){\n      // 根据值的大小显示不同的文本和字体大小\n      Text(value > 99 ? '99+': value.toString())\n        .textAlign(TextAlign.Center)\n        .fontSize(value > 99 ?  '16vp': '20vp')\n        .fontWeight(FontWeight.Medium)\n        .fontColor('#ffffffff')\n    }\n  }\n\n  build() {\n    Row() {\n      Column() {\n        // 第一个复选框，圆形形状\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center}) {\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup', indicatorBuilder:()=>{this.indicatorBuilder(9)}})\n            .shape(CheckBoxShape.CIRCLE) // 设置复选框形状为圆形\n            .onChange((value: boolean) => {\n              console.info('Checkbox1 change is'+ value) // 输出复选框状态变化\n            })\n            .mark({\n              strokeColor:Color.Black,\n              size: 50,\n              strokeWidth: 5\n            })\n            .width(30)\n            .height(30)\n          Text('Checkbox1').fontSize(20)\n        }.padding(15)\n\n        // 第二个复选框，圆角矩形形状\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup', indicatorBuilder:()=>{this.indicatorBuilder(100)}})\n            .shape(CheckBoxShape.ROUNDED_SQUARE) // 设置复选框形状为圆角矩形\n            .onChange((value: boolean) => {\n              console.info('Checkbox2 change is' + value) // 输出复选框状态变化\n            })\n            .width(30)\n            .height(30)\n          Text('Checkbox2').fontSize(20)\n        }\n      }\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"

        ],
        "is_common_attrs": True
    },
    "CheckboxGroup": {"description": "多选框群组，用于控制多选框全选或者不全选状态。"},
    "Component3D": {"description": "3D渲染组件，可以加载3D模型资源并做自定义渲染，通常用于3D动效场景。"},
    "ContainerSpan": {
        "description": "Text组件的子组件，用于统一管理多个Span、ImageSpan的背景色及圆角弧度，可以包含Span、ImageSpan子组件。"},
    "DataPanel": {"description": "数据面板组件，用于将多个数据占比情况使用占比图进行展示。"},
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
    "Divider": {"description": "提供分隔器组件，分隔不同内容块/内容元素。"},
    "Gauge": {"description": "数据量规图表组件，用于将数据展示为环形图表，可以包含单个子组件。"},
    "Image": {
        "description": "Image为图片组件，常用于在应用中显示图片。Image支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。"},
    "ImageAnimator": {
        "description": "提供帧动画组件来实现逐帧播放图片的能力，可以配置需要播放的图片列表，每张图片可以配置时长。"},
    "ImageSpan": {"description": "Text、ContainerSpan组件的子组件，用于显示行内图片。"},
    "LoadingProgress": {"description": "用于显示加载动效的组件。"},
    "Marquee": {
        "description": "跑马灯组件，用于滚动展示一段单行文本。仅当文本内容宽度超过跑马灯组件宽度时滚动，不超过时不滚动。为了不影响滚动帧率，建议在滚动类组件中Marquee的个数不超过4个，或者使用Text组件的TextOverflow.MARQUEE替代。"},
    "Menu": {"description": "以垂直列表形式显示的菜单，可以包含MenuItem、MenuItemGroup子组件。"},
    "MenuItem": {"description": "用来展示菜单Menu中具体的item菜单项。"},
    "MenuItemGroup": {"description": "该组件用来展示菜单MenuItem的分组，可以包含MenuItem子组件。"},
    "Navigation": {
        "description": "Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换，可以包含子组件，推荐与NavRouter组件搭配使用。"},
    "NavRouter": {
        "description": "导航组件，默认提供点击响应处理，不需要开发者自定义点击事件逻辑，必须包含两个子组件，其中第二个子组件必须为NavDestination。"},
    "NavDestination": {"description": "作为子页面的根容器，用于显示Navigation的内容区，可以包含多个子组件。"},
    "NodeContainer": {
        "description": "基础组件，不支持尾随添加子节点。组件接受一个NodeController的实例接口。需要NodeController组合使用，不支持子组件。"},
    "PatternLock": {
        "description": "图案密码锁组件，以九宫格图案的方式输入密码，用于密码验证场景。手指在PatternLock组件区域按下时开始进入输入状态，手指离开屏幕时结束输入状态完成密码输入。"},
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
    "QRCode": {"description": "用于显示单个二维码的组件。"},
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
            "/*\n设置开启状态底板颜色。\n实现思路：\n本示例通过使用鸿蒙ArkUI框架，构建了一个包含三个Radio组件的界面。每个Radio组件都包含一个文本标签，用于标识不同的选项。通过Flex布局和Column组件的使用，确保Radio组件在界面中水平排列，并且每个组件都有自己的列布局。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听。\n\n总体功能与效果描述：\n该界面展示了三个Radio组件，每个组件旁边都有一个文本标签。用户可以通过点击Radio来选择某个选项，同时其他选项会自动取消选中。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听，以便在用户选择时进行相应的处理。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct RadioExample {\n  build() {\n    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n      Column() {\n        Text('Radio1')\n        // 创建一个Radio组件，设置其初始选中状态和样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和样式以确保其显示效果。\n        Radio({ value: 'Radio1', group: 'radioGroup' }).checked(true)\n          .radioStyle({\n            checkedBackgroundColor: Color.Pink\n          })\n          .height(50)\n          .width(50)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio1 status is ' + isChecked)\n          })\n      }\n      Column() {\n        Text('Radio2')\n        // 创建一个Radio组件，设置其初始选中状态和样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和样式以确保其显示效果。\n        Radio({ value: 'Radio2', group: 'radioGroup' }).checked(false)\n          .radioStyle({\n            checkedBackgroundColor: Color.Pink\n          })\n          .height(50)\n          .width(50)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio2 status is ' + isChecked)\n          })\n      }\n      Column() {\n        Text('Radio3')\n        // 创建一个Radio组件，设置其初始选中状态和样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和样式以确保其显示效果。\n        Radio({ value: 'Radio3', group: 'radioGroup' }).checked(false)\n          .radioStyle({\n            checkedBackgroundColor: Color.Pink\n          })\n          .height(50)\n          .width(50)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio3 status is ' + isChecked)\n          })\n      }\n    }.padding({ top: 30 })\n  }\n}",
            "/*\n设置选中样式为图片。\n实现思路：\n本示例通过使用鸿蒙ArkUI框架，构建了一个包含三个Radio组件的界面。每个Radio组件都包含一个文本标签，用于标识不同的选项。通过Flex布局和Column组件的使用，确保Radio组件在界面中水平排列，并且每个组件都有自己的列布局。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听。此外，还使用了不同的指示器类型和自定义指示器来增强视觉效果。\n\n总体功能与效果描述：\n该界面展示了三个Radio组件，每个组件旁边都有一个文本标签。用户可以通过点击Radio来选择某个选项，同时其他选项会自动取消选中。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听，以便在用户选择时进行相应的处理。此外，还使用了不同的指示器类型和自定义指示器来增强视觉效果。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct RadioExample {\n  @Builder \n  indicatorBuilder() {\n    // 创建一个自定义的指示器，使用一个星形图标\n    // 功能与效果描述：自定义指示器用于在Radio组件选中时显示一个星形图标。\n    Image($r(\"app.media.star\"))\n  }\n  build() {\n    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n      Column() {\n        Text('Radio1')\n        // 创建一个Radio组件，设置其初始选中状态和指示器类型\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和指示器类型以确保其显示效果。\n        Radio({ value: 'Radio1', group: 'radioGroup',\n          indicatorType:RadioIndicatorType.TICK\n        }).checked(true)\n          .height(50)\n          .width(80)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio1 status is ' + isChecked)\n          })\n      }\n      Column() {\n        Text('Radio2')\n        // 创建一个Radio组件，设置其初始选中状态和指示器类型\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和指示器类型以确保其显示效果。\n        Radio({ value: 'Radio2', group: 'radioGroup',\n          indicatorType:RadioIndicatorType.DOT\n        }).checked(false)\n          .height(50)\n          .width(80)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio2 status is ' + isChecked)\n          })\n      }\n      Column() {\n        Text('Radio3')\n        // 创建一个Radio组件，设置其初始选中状态和自定义指示器\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和自定义指示器以确保其显示效果。\n        Radio({ value: 'Radio3', group: 'radioGroup',\n          indicatorType:RadioIndicatorType.CUSTOM,\n          indicatorBuilder:()=>{this.indicatorBuilder()}\n        }).checked(false)\n          .height(50)\n          .width(80)\n          .onChange((isChecked: boolean) => {\n            // 监听Radio组件的选中状态变化，并输出到控制台\n            // 功能与效果描述：监听Radio组件的选中状态变化，以便在用户选择时进行相应的处理。\n            console.log('Radio3 status is ' + isChecked)\n          })\n      }\n    }.padding({ top: 30 })\n  }\n}",
            "/*\n设置自定义单选样式\n实现思路：\n本示例通过使用鸿蒙ArkUI框架，构建了一个包含两个自定义样式的Radio组件的界面。每个Radio组件都包含一个自定义的样式类`MyRadioStyle`，用于设置Radio组件的选中颜色和类型。通过自定义的`buildRadio`函数，实现了Radio组件的布局和样式。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听。\n\n总体功能与效果描述：\n该界面展示了两个自定义样式的Radio组件。用户可以通过点击Radio来选择某个选项，同时其他选项会自动取消选中。每个Radio组件的选中状态和样式都可以通过代码进行设置和监听，以便在用户选择时进行相应的处理。自定义样式类`MyRadioStyle`用于设置Radio组件的选中颜色和类型，增强了视觉效果。\n*/\n\n// 定义一个自定义样式类，用于设置Radio组件的选中颜色和类型\n// 功能与效果描述：自定义样式类用于设置Radio组件的选中颜色和类型，以便在用户选择时进行相应的处理。\nclass MyRadioStyle implements ContentModifier<RadioConfiguration> {\n  type: number = 0\n  selectedColor: Color = Color.Black\n\n  constructor(numberType: number, colorType: Color) {\n    this.type = numberType\n    this.selectedColor = colorType\n  }\n\n  applyContent(): WrappedBuilder<[RadioConfiguration]> {\n    return wrapBuilder(buildRadio)\n  }\n}\n\n// 定义一个自定义的Radio组件布局和样式函数\n// 功能与效果描述：自定义的Radio组件布局和样式函数用于设置Radio组件的布局和样式，以便在用户选择时进行相应的处理。\n@Builder function buildRadio(config: RadioConfiguration) {\n  Row({ space: 30 }) {\n    Circle({ width: 50, height: 50 })\n      .stroke(Color.Black)\n      .fill(config.checked ? (config.contentModifier as MyRadioStyle).selectedColor : Color.White)\n    Button(config.checked ? \"off\" : \"on\")\n      .width(100)\n      .type(config.checked ? (config.contentModifier as MyRadioStyle).type : ButtonType.Normal)\n      .backgroundColor(0xAABBCC)\n      .onClick(() => {\n        if (config.checked) {\n          config.triggerChange(false)\n        } else {\n          config.triggerChange(true)\n        }\n      })\n  }\n}\n\n@Entry\n@Component\nstruct refreshExample {\n  build() {\n    Column({ space: 50 }) {\n      Row() {\n        // 创建一个Radio组件，设置其初始选中状态和自定义样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和自定义样式以确保其显示效果。\n        Radio({ value: 'Radio1', group: 'radioGroup' })\n          .contentModifier(new MyRadioStyle(1, Color.Red))\n          .checked(false)\n          .width(300)\n          .height(100)\n      }\n      Row() {\n        // 创建一个Radio组件，设置其初始选中状态和自定义样式\n        // 功能与效果描述：Radio组件用于用户选择某个选项。设置初始选中状态和自定义样式以确保其显示效果。\n        Radio({ value: 'Radio2', group: 'radioGroup' })\n          .checked(true)\n          .width(300)\n          .height(60)\n          .contentModifier(new MyRadioStyle(2, Color.Red))\n      }\n    }\n  }\n}"
        ]
    },
    "Rating": {"description": "提供在给定范围内选择评分的组件。"},
    "RichEditor": {"description": "支持图文混排和文本交互式编辑的组件，不包含子组件。"},
    "RichText": {"description": "富文本组件，解析并显示HTML格式文本，不包含子组件。"},
    "ScrollBar": {"description": "滚动条组件ScrollBar，用于配合可滚动组件使用，如List、Grid、Scroll，可以包含单个子组件。"},
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
    "Span": {"description": "作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。"},
    "Stepper": {"description": "步骤导航器组件，适用于引导用户按照步骤完成任务的导航场景，仅能包含子组件StepperItem。"},
    "StepperItem": {"description": "用作Stepper组件的页面子组件，支持单个子组件。"},
    "SymbolSpan": {"description": "作为Text组件的子组件，用于显示图标小符号的组件，不支持子组件。"},
    "SymbolGlyph": {"description": "显示图标小符号的组件，不支持子组件。"},
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
    }
    ,
    "TextArea": {"description": "多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。"},
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
    "TextPicker": {"description": "滑动选择文本内容的组件。"},
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
            "/*\\n实现思路：\\n本示例通过自定义Toggle样式实现了一个按钮切换圆形颜色的功能。用户可以通过点击不同的按钮来改变圆形的背景颜色。\\n总体功能与效果描述：\\n用户点击“蓝”按钮时，圆形背景变为蓝色；点击“黄”按钮时，圆形背景变为黄色。\\n*/\\n\\n// MySwitchStyle.ets\\nclass MySwitchStyle implements ContentModifier<ToggleConfiguration> {\\n  // 定义选中时的颜色\\n  selectedColor: Color = Color.White;\\n  // 定义灯的标识\\n  lamp: string = 'string';\\n\\n  // 构造函数，初始化选中颜色和灯的标识\\n  constructor(selectedColor: Color, lamp: string) {\\n    this.selectedColor = selectedColor;\\n    this.lamp = lamp;\\n  }\\n\\n  // 应用内容修饰器\\n  applyContent(): WrappedBuilder<[ToggleConfiguration]> {\\n    return wrapBuilder(buildSwitch);\\n  }\\n}\\n\\n// 构建开关的Builder函数\\n@Builder function buildSwitch(config: ToggleConfiguration) {\\n  Column({ space: 50 }) {\\n    // 创建一个圆形，根据Toggle状态设置填充颜色\\n    Circle({ width: 150, height: 150 })\\n      .fill(config.isOn ? (config.contentModifier as MySwitchStyle).selectedColor : Color.Blue)\\n    Row() {\\n      // 创建一个按钮，点击时触发Toggle状态改变为false\\n      Button('蓝' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))\\n        .onClick(() => {\\n          config.triggerChange(false);\\n        })\\n      // 创建一个按钮，点击时触发Toggle状态改变为true\\n      Button('黄' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))\\n        .onClick(() => {\\n          config.triggerChange(true);\\n        })\\n    }\\n  }\\n}\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Column({ space: 50 }) {\\n      // 创建一个Toggle组件，设置为Switch类型，启用状态，并应用自定义样式\\n      Toggle({ type: ToggleType.Switch })\\n        .enabled(true)\\n        .contentModifier(new MySwitchStyle(Color.Yellow, '灯'))\\n        .onChange((isOn: boolean) => {\\n          // 监听Toggle状态变化，输出日志\\n          console.info('Switch Log:' + isOn);\\n        })\\n    }.height('100%').width('100%')\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用Toggle组件来创建一个自定义样式的Switch开关。通过设置不同的属性，如滑块半径、滑轨圆角、滑块颜色和背景颜色，来实现自定义的Switch样式。同时，通过onChange事件监听开关状态的变化。\\n\\n总体功能与效果描述：\\n示例中包含两个Toggle组件，每个组件都是一个Switch开关。每个开关都可以通过点击来切换状态，并且具有自定义的样式，包括滑块的半径、滑轨的圆角、滑块颜色和关闭状态的背景颜色。\\n*/\\n\\n// ToggleExample.ets\\n@Entry\\n@Component\\nstruct ToggleExample {\\n  build() {\\n    Column({ space: 10 }) {\\n      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')\\n      // 创建一个Flex布局，用于均匀分布Toggle组件\\n      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {\\n        // 创建第一个Toggle组件，类型为Switch，初始状态为关闭\\n        Toggle({ type: ToggleType.Switch, isOn: false })\\n          .selectedColor('#007DFF') // 设置开关打开状态的背景颜色\\n          .switchStyle({\\n            pointRadius: 15, // 设置滑块的半径\\n            trackBorderRadius: 10, // 设置滑轨的圆角\\n            pointColor: '#D2B48C', // 设置滑块的颜色\\n            unselectedColor: Color.Pink // 设置开关关闭状态的背景颜色\\n          })\\n          .onChange((isOn: boolean) => {\\n            console.info('Component status:' + isOn) // 监听开关状态的变化并输出到控制台\\n          })\\n\\n        // 创建第二个Toggle组件，类型为Switch，初始状态为打开\\n        Toggle({ type: ToggleType.Switch, isOn: true })\\n          .selectedColor('#007DFF') // 设置开关打开状态的背景颜色\\n          .switchStyle({\\n            pointRadius: 15, // 设置滑块的半径\\n            trackBorderRadius: 10, // 设置滑轨的圆角\\n            pointColor: '#D2B48C', // 设置滑块的颜色\\n            unselectedColor: Color.Pink // 设置开关关闭状态的背景颜色\\n          })\\n          .onChange((isOn: boolean) => {\\n            console.info('Component status:' + isOn) // 监听开关状态的变化并输出到控制台\\n          })\\n      }\\n    }.width('100%').padding(24)\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用Toggle组件的不同类型（Switch、Checkbox、Button），并展示了如何设置其状态、颜色和大小，以及如何处理状态变化事件。\\n总体功能与效果描述：\\n该示例通过Toggle组件展示了三种不同类型的切换控件，并允许用户通过点击来切换它们的状态。每个Toggle组件的状态变化都会通过控制台输出其状态。\\n*/\\n\\n// ToggleExample.ets\\n@Entry\\n@Component\\nstruct ToggleExample {\\n  build() {\\n    Column({ space: 10 }) {\\n      // 显示文本，说明下面的Toggle组件类型为Switch\\n      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')\\n      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {\\n        // 创建一个类型为Switch的Toggle组件，初始状态为关闭\\n        Toggle({ type: ToggleType.Switch, isOn: false })\\n          .selectedColor('#007DFF') // 设置选中状态的颜色\\n          .switchPointColor('#FFFFFF') // 设置Switch滑块的颜色\\n          .onChange((isOn: boolean) => {\\n            console.info('Component status:' + isOn) // 输出Toggle组件的状态变化\\n          })\\n\\n        // 创建一个类型为Switch的Toggle组件，初始状态为开启\\n        Toggle({ type: ToggleType.Switch, isOn: true })\\n          .selectedColor('#007DFF') // 设置选中状态的颜色\\n          .switchPointColor('#FFFFFF') // 设置Switch滑块的颜色\\n          .onChange((isOn: boolean) => {\\n            console.info('Component status:' + isOn) // 输出Toggle组件的状态变化\\n          })\\n      }\\n\\n      // 显示文本，说明下面的Toggle组件类型为Checkbox\\n      Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')\\n      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {\\n        // 创建一个类型为Checkbox的Toggle组件，初始状态为关闭\\n        Toggle({ type: ToggleType.Checkbox, isOn: false })\\n          .size({ width: 20, height: 20 }) // 设置Checkbox的大小\\n          .selectedColor('#007DFF') // 设置选中状态的颜色\\n          .onChange((isOn: boolean) => {\\n            console.info('Component status:' + isOn) // 输出Toggle组件的状态变化\\n          })\\n\\n        // 创建一个类型为Checkbox的Toggle组件，初始状态为开启\\n        Toggle({ type: ToggleType.Checkbox, isOn: true })\\n          .size({ width: 20, height: 20 }) // 设置Checkbox的大小\\n          .selectedColor('#007DFF') // 设置选中状态的颜色\\n          .onChange((isOn: boolean) => {\\n            console.info('Component status:' + isOn) // 输出Toggle组件的状态变化\\n          })\\n      }\\n\\n      // 显示文本，说明下面的Toggle组件类型为Button\\n      Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')\\n      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {\\n        // 创建一个类型为Button的Toggle组件，初始状态为关闭\\n        Toggle({ type: ToggleType.Button, isOn: false }) {\\n          Text('status button').fontColor('#182431').fontSize(12) // 设置Button内的文本\\n        }.width(106) // 设置Button的宽度\\n        .selectedColor('rgba(0,125,255,0.20)') // 设置选中状态的颜色\\n        .onChange((isOn: boolean) => {\\n          console.info('Component status:' + isOn) // 输出Toggle组件的状态变化\\n        })\\n\\n        // 创建一个类型为Button的Toggle组件，初始状态为开启\\n        Toggle({ type: ToggleType.Button, isOn: true }) {\\n          Text('status button').fontColor('#182431').fontSize(12) // 设置Button内的文本\\n        }.width(106) // 设置Button的宽度\\n        .selectedColor('rgba(0,125,255,0.20)') // 设置选中状态的颜色\\n        .onChange((isOn: boolean) => {\\n          console.info('Component status:' + isOn) // 输出Toggle组件的状态变化\\n        })\\n      }\\n    }.width('100%').padding(24) // 设置Column的宽度和内边距\\n  }\\n}"
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
        "description": "可用于EGL/OpenGLES和媒体数据写入，并显示在XComponent组件，构造参数type为\"component\"时可以包含子组件。"}
}
