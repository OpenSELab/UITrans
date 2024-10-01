CONTAINER_COMPONENT = {
    "Badge": {
        "description": "可以附加在单个组件上用于信息标记的容器组件。",
        "interfaces": [
            {
                "description": "创建数字标记组件。",
                "params": {
                    "value": {
                        "type": "BadgeParamWithNumber",
                        "required": True,
                        "description": "用于创建数字标记组件的参数。"
                    }
                }
            },
            {
                "description": "根据字符串创建标记组件。",
                "params": {
                    "value": {
                        "type": "BadgeParamWithString",
                        "required": True,
                        "description": "用于创建字符串标记组件的参数。"
                    }
                }
            }
        ],
        "attributes": {
            "position": {
                "description": "设置提示点显示位置。",
                "params": {
                    "value": {
                        "type": "BadgePosition",
                        "required": False,
                        "description": "提示点显示位置。",
                        "default": "BadgePosition.RightTop"
                    }
                }
            },
            "style": {
                "description": "Badge组件可设置样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。",
                "params": {
                    "color": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "文本颜色。",
                        "default": "Color.White"
                    },
                    "fontSize": {
                        "type": ["number", "string"],
                        "required": False,
                        "description": "文本大小。单位：vp",
                        "default": 10
                    },
                    "badgeSize": {
                        "type": ["number", "string"],
                        "required": False,
                        "description": "Badge的大小。单位：vp",
                        "default": 16
                    },
                    "badgeColor": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "Badge的颜色。",
                        "default": "Color.Red"
                    },
                    "fontWeight": {
                        "type": ["number", "FontWeight", "string"],
                        "required": False,
                        "description": "设置文本的字体粗细。",
                        "default": "FontWeight.Normal"
                    },
                    "borderColor": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "底板描边颜色。",
                        "default": "Color.Red"
                    },
                    "borderWidth": {
                        "type": "Length",
                        "required": False,
                        "description": "底板描边粗细。单位：vp",
                        "default": 1
                    }
                }
            },
            "count": {
                "description": "设置提醒消息数。小于等于0时不显示信息标记。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "提醒消息数。取值范围：[-2147483648,2147483647]"
                    }
                }
            },
            "maxCount": {
                "description": "最大消息数，超过最大消息时仅显示maxCount+。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": False,
                        "description": "最大消息数。取值范围：[-2147483648,2147483647]",
                        "default": 99
                    }
                }
            },
            "value": {
                "description": "提示内容的文本字符串。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "提示内容的文本字符串。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            "这段代码实现了一个徽章示例组件 BadgeExample，展示了如何在不同的 UI 元素上使用徽章（Badge）进行标记。组件主要包括三个部分：Tab 徽章、字符串徽章和数字徽章。\n\nTab 徽章：在第三个 Tab 项上显示一个带有红色小圆点的徽章，其他 Tab 项则只显示一个图标和文字。\n字符串徽章：在列表项 list2 上显示一个带有  标记的徽章，并设置了徽章的大小和颜色。\n数字徽章：在列表项 list2 上显示一个带有数字 "'1" 的徽章，徽章位置在右侧，且徽章样式和背景颜色均可自定义。\n组件通过使用 Flex 布局、Tabs 组件以及 List 列表来组织内容，提供了一个直观的方式来展示徽章的不同用法和样式。\n// xxx.ets\n@Entry\n@Component\nstruct BadgeExample {\n  @Builder tabBuilder(index: number) {\n    Column() {\n      if (index === 2) {\n        Badge({\n          value: '',\n          style: { badgeSize: 6, badgeColor: '  # FA2A2D' }\n        }) {\n          Image('/common/public_icon_off.svg')\n            .width(24)\n            .height(24)\n        }\n        .width(24)\n        .height(24)\n        .margin({ bottom: 4 })\n      } else {\n        Image('/common/public_icon_off.svg')\n          .width(24)\n          .height(24)\n          .margin({ bottom: 4 })\n      }\n      Text('Tab')\n        .fontColor('#182431')\n        .fontSize(10)\n        .fontWeight(500)\n        .lineHeight(14)\n    }.width('100%').height('100%').justifyContent(FlexAlign.Center)\n  }\n\n  @Builder itemBuilder(value: string) {\n    Row() {\n      Image('common/public_icon.svg').width(32).height(32).opacity(0.6)\n      Text(value)\n        .width(177)\n        .height(21)\n        .margin({ left: 15, right: 76 })\n        .textAlign(TextAlign.Start)\n        .fontColor('#182431')\n        .fontWeight(500)\n        .fontSize(16)\n        .opacity(0.9)\n      Image('common/public_icon_arrow_right.svg').width(12).height(24).opacity(0.6)\n    }.width('100%').padding({ left: 12, right: 12 }).height(56)\n  }\n\n  build() {\n    Column() {\n      Text('dotsBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)\n      Tabs() {\n        TabContent()\n          .tabBar(this.tabBuilder(0))\n        TabContent()\n          .tabBar(this.tabBuilder(1))\n        TabContent()\n          .tabBar(this.tabBuilder(2))\n        TabContent()\n          .tabBar(this.tabBuilder(3))\n      }\n      .width(360)\n      .height(56)\n      .backgroundColor('#F1F3F5')\n\n      Column() {\n        Text('stringBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)\n        List({ space: 12 }) {\n          ListItem() {\n            Text('list1').fontSize(14).fontColor('#182431').margin({ left: 12 })\n          }\n          .width('100%')\n          .height(56)\n          .backgroundColor('#FFFFFF')\n          .borderRadius(24)\n          .align(Alignment.Start)\n\n          ListItem() {\n            Badge({\n              value: 'New',\n              position: BadgePosition.Right,\n              style: { badgeSize: 16, badgeColor: '#FA2A2D' }\n            }) {\n              Text('list2').width(27).height(19).fontSize(14).fontColor('#182431')\n            }.width(49.5).height(19)\n            .margin({ left: 12 })\n          }\n          .width('100%')\n          .height(56)\n          .backgroundColor('#FFFFFF')\n          .borderRadius(24)\n          .align(Alignment.Start)\n        }.width(336)\n\n        Text('numberBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)\n        List() {\n          ListItem() {\n            this.itemBuilder('list1')\n          }\n\n          ListItem() {\n            Row() {\n              Image('common/public_icon.svg').width(32).height(32).opacity(0.6)\n              Badge({\n                count: 1,\n                position: BadgePosition.Right,\n                style: { badgeSize: 16, badgeColor: '#FA2A2D' }\n              }) {\n                Text('list2')\n                  .width(177)\n                  .height(21)\n                  .textAlign(TextAlign.Start)\n                  .fontColor('#182431')\n                  .fontWeight(500)\n                  .fontSize(16)\n                  .opacity(0.9)\n              }.width(240).height(21).margin({ left: 15, right: 11 })\n\n              Image('common/public_icon_arrow_right.svg').width(12).height(24).opacity(0.6)\n            }.width('100%').padding({ left: 12, right: 12 }).height(56)\n          }\n\n          ListItem() {\n            this.itemBuilder('list3')\n          }\n\n          ListItem() {\n            this.itemBuilder('list4')\n          }\n        }\n        .width(336)\n        .height(232)\n        .backgroundColor('#FFFFFF')\n        .borderRadius(24)\n        .padding({ top: 4, bottom: 4 })\n        .divider({ strokeWidth: 0.5, color: 'rgba(0,0,0,0.1)', startMargin: 60, endMargin: 12 })\n      }.width('100%').backgroundColor('#F1F3F5').padding({ bottom: 12 })\n    }.width('100%')\n  }\n}",
            "\n这段代码实现了一个带有徽章的图标组件，并通过按钮控制徽章的显隐效果。具体功能如下：\n\n徽章显示：在图标右上角显示一个徽章，徽章显示的内容为 badgeCount 的值。\n按钮控制：通过两个按钮可以控制 badgeCount 的值，当点击 "'count 0" 按钮时，徽章隐藏；当点击 "count 1" 按钮时，徽章显示，且徽章内容为 1。\n布局：组件采用列布局，内容之间有一定的间隔，并设置了上边距。\n此示例展示了如何通过状态管理来动态控制徽章的显隐，从而实现不同的视觉效果。\n// 该示例实现了Badge组件显隐时缩放\n@Entry\n@Component\nstruct Index {\n  @State badgeCount: number = 1\n\n  build() {\n    Column({ space: 40 }) {\n      Badge({\n        count: this.badgeCount,\n        style: {},\n        position: BadgePosition.RightTop,\n      }) {\n        Image($r("app.media.icon"))\n        .width(50)\n        .height(50)\n      }\n      .width(55)\n      Button(''0'').onClick(() => {\n        this.badgeCount = 0\n      })\n      Button(''count 1'').onClick(() => {\n        this.badgeCount = 1\n      })\n    }\n    .margin({top: 20})\n  }\n}\n\n\n\n\n\n"'
        ],
        "is_common_attrs": True
    },
    "Column": {
        "description": "沿垂直方向布局的容器组件，可以包含子组件。",
        "interfaces": [
            {
                "description": "Column(value?: {space?: string | number})",
                "params": {
                    "space": {
                        "type": ["string", "number"],
                        "description": "纵向布局元素垂直方向间距。从API version 9开始，space为负数或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。",
                        "default": 0
                    }
                }
            }
        ],
        "attributes": {
            "alignItems": {
                "description": "设置子组件在水平方向上的对齐格式。",
                "params": {
                    "value": {
                        "type": "HorizontalAlign",
                        "required": True,
                        "description": "子组件在水平方向上的对齐格式。",
                        "default": "HorizontalAlign.Center"
                    }
                }
            },
            "justifyContent": {
                "description": "设置子组件在垂直方向上的对齐格式。",
                "params": {
                    "value": {
                        "type": "FlexAlign",
                        "required": True,
                        "description": "子组件在垂直方向上的对齐格式。",
                        "default": "FlexAlign.Start"
                    }
                }
            }
        },
        "events": {
            "generalEvents": {
                "description": "支持通用事件。",
                "params": {}
            }
        },
        "is_common_attrs": True
    },
    "ColumnSplit": {
        "description": "将子组件纵向布局，并在每个子组件之间插入一根横向的分割线。",
        "interfaces": [
            {
                "description": "ColumnSplit()",
                "params": {}
            }
        ],
        "attributes": {
            "resizeable": {
                "description": "设置分割线是否可拖拽。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "分割线是否可拖拽。",
                        "default": "False"
                    }
                }
            },
            "divider": {
                "description": "设置分割线的margin。",
                "params": {
                    "value": {
                        "type": "[ColumnSplitDividerStyle, null]",
                        "required": True,
                        "description": "分割线的margin。",
                        "default": "null"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            "这段代码实现了一个带有可拖动分割线的列布局示例。具体功能如下：\n\n- **文本描述**：在顶部显示一行提示文本，说明下方的分割线可以拖动。\n- **可拖动列布局**：使用 `ColumnSplit` 组件创建了一个垂直排列的文本块，每个文本块都有不同的背景颜色和相同的高度，文本居中显示。\n- **拖动调整大小**：用户可以通过拖动分割线来动态调整文本块的高度比例，提供了灵活的布局体验。\n- **布局设置**：整体布局的宽度为页面宽度的 90%，高度为页面高度的 60%，并且具有 1 像素的边框。\n\n此示例展示了如何使用 `ColumnSplit` 组件实现可拖动的列布局，使得用户可以通过交互来调整界面布局的比例。\n// xxx.ets\n@Entry\n@Component\nstruct ColumnSplitExample {\n  build() {\n    Column(){\n      Text('The secant line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')\n      ColumnSplit() {\n        Text('1').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)\n        Text('2').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)\n        Text('3').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)\n        Text('4').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)\n        Text('5').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)\n      }\n      .borderWidth(1)\n      .resizeable(true) // 可拖动\n      .width('90%').height('60%')\n    }.width('100%')\n  }\n}"
        ],
    },
    "Counter": {
        "description": "计数器组件，提供相应的增加或者减少的计数操作。",
        "interfaces": [
            {
                "description": "Counter()\n\n**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。",
                "params": {}
            }
        ],
        "attributes": {
            "enableInc": {
                "description": "enableInc(value: boolean)\n\n设置增加按钮禁用或使能。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "增加按钮禁用或使能。",
                        "default": "True"
                    }
                }
            },
            "enableDec": {
                "description": "enableDec(value: boolean)\n\n设置减少按钮禁用或使能。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "减少按钮禁用或使能。",
                        "default": "True"
                    }
                }
            }
        },
        "events": {
            "onInc": {
                "description": "onInc(event: () => void)\n\n监听数值增加事件。\n\n**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {}
            },
            "onDec": {
                "description": "onDec(event: () => void)\n\n监听数值减少事件。\n\n**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。\n\n**元服务API：** 从API version 11开始，该接口支持在元服务中使用。\n\n**系统能力：** SystemCapability.ArkUI.ArkUI.Full",
                "params": {}
            }
        },
        "examples": [
            "这段代码实现了一个简单的计数器组件示例。主要功能如下：\n\n计数器显示：在界面上显示一个计数器的当前值，初始值为0。\n增减功能：用户可以通过交互增加或减少计数器的值。每次点击增加按钮时，计数器的值会加1；每次点击减少按钮时，计数器的值会减1。\n布局：计数器组件居中显示，并且具有100的外边距，使其与周围内容保持一定的距离。\n此示例展示了如何使用 Counter 组件来创建一个简单的增减计数器，并通过按钮点击事件动态更新计数值。\n// xxx.ets\n@Entry\n@Component\nstruct CounterExample {\n  @State value: number = 0\n\n  build() {\n    Column() {\n      Counter() {\n        Text(this.value.toString())\n      }.margin(100)\n      .onInc(() => {\n        this.value++\n      })\n      .onDec(() => {\n        this.value--\n      })\n    }.width("'100%'")\n  }\n}\n\n\n\n\n\n"
        ],
    },
    "EmbeddedComponent": {
        "description": "用于支持在当前页面嵌入本应用内其他EmbeddedUIExtensionAbility提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，完成页面布局和渲染。通常用于有进程隔离诉求的模块化开发场景。",
        "interfaces": [
            {
                "description": "用于创建EmbeddedComponent组件。",
                "params": {
                    "loader": {
                        "type": "Want",
                        "required": True,
                        "description": "要加载的EmbeddedUIExtensionAbility。"
                    },
                    "type": {
                        "type": "EmbeddedType",
                        "required": True,
                        "description": "提供方的类型。"
                    }
                }
            }
        ],
        "attributes": {
            "general": {
                "description": "支持通用属性。",
                "params": {}
            },
            "size": {
                "description": "EmbeddedComponent组件宽高默认值和最小值均为10vp, 不支持如下与宽高相关的属性：\"constraintSize\"、\"aspectRatio\"、\"layoutWeight\"、\"flexBasis\"、\"flexGrow\"和\"flexShrink\"。",
                "params": {}
            }
        },
        "events": {
            "onTerminated": {
                "description": "被拉起的EmbeddedUIExtensionAbility通过调用terminateSelfWithResult或者terminateSelf正常退出时，触发本回调函数。",
                "params": {
                    "callback": {
                        "type": "Callback<TerminationInfo>",
                        "required": True,
                        "description": "回调函数，携带TerminationInfo信息。"
                    }
                }
            },
            "onError": {
                "description": "被拉起的EmbeddedUIExtensionAbility在运行过程中发生异常时触发本回调。",
                "params": {
                    "callback": {
                        "type": "ErrorCallback",
                        "required": True,
                        "description": "回调函数，携带错误信息。"
                    }
                }
            }
        },
        "examples": [
            "这段代码实现了一个页面，其中嵌入了一个外部能力的UI组件，并处理其终止和错误事件。具体功能如下：\n\n- **页面初始化**：当UIAbility启动时，加载此页面，并初始化 `message` 状态变量用于显示消息。\n- **嵌入外部能力**：通过 `EmbeddedComponent` 组件嵌入了一个外部能力（`ExampleEmbeddedAbility`），并设置了它的显示区域和高度、宽度。\n- **事件处理**：\n  - **终止事件**：当嵌入的能力被终止时，触发 `onTerminated` 事件，并更新页面上的 `message` 显示终止代码和对应的Want信息。\n  - **错误事件**：当发生错误时，触发 `onError` 事件，并更新 `message` 显示错误代码。\n- **布局**：页面使用 `Row` 和 `Column` 布局，确保嵌入的组件占据页面的绝大部分区域。\n\n此代码展示了如何在页面中嵌入其他能力的UI，并通过事件处理机制响应其终止或错误情况。\n// pages/Index.ets -- UIAbility启动时加载此页面\nimport { Want } from '@kit.AbilityKit';\n\n@Entry\n@Component\nstruct Index {\n  @State message: string = 'Message: '\n  private want: Want = {\n    bundleName: '''com.example.embeddeddem,\n    abilityName: '''ExampleEmbeddedAbility''',\n  }\n\n  build() {\n    Row() {\n      Column() {\n        Text(this.message).fontSize(30)\n        EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)\n          .width('100%')\n          .height('90%')\n          .onTerminated((info)=>{\n            this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);\n          })\n          .onError((error)=>{\n            this.message = 'Error: code = ' + error.code;\n          })\n      }\n      .width('100%')\n    }\n    .height('100%')\n  }\n}"
            "这段代码实现了一个嵌入式UI扩展能力（EmbeddedUIExtensionAbility）的生命周期管理和内容加载功能。具体功能如下：\n\n生命周期管理：\n\nonCreate：在能力创建时触发，用于初始化资源或状态。\nonForeground：当能力从后台切换到前台时触发，通常用于恢复UI状态或刷新数据。\nonBackground：当能力切换到后台时触发，用于保存状态或释放资源。\nonDestroy：在能力销毁时触发，进行清理工作。\n会话管理：\n\nonSessionCreate：当嵌入式UI扩展会话创建时触发，接收 Want 对象和 UIExtensionContentSession 会话对象。此时，可以初始化会话并加载指定的内容页面（'pages/extension'）。\nonSessionDestroy：当会话销毁时触发，用于清理会话相关的资源。\n内容加载：\n\n在会话创建时，通过 session.loadContent 方法加载指定路径的内容页面，同时可以传递自定义存储对象（LocalStorage），以便在页面中使用。\n此代码展示了如何在嵌入式UI扩展能力中处理生命周期事件和会话管理，以及如何加载和管理嵌入的UI内容。\nimport { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';\n\nconst TAG: string = '[ExampleEmbeddedAbility]'\nexport default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {\n  \n  onCreate() {\n    console.log(TAG, `onCreate`);\n  }\n\n  onForeground() {\n    console.log(TAG, `onForeground`);\n  }\n\n  onBackground() {\n    console.log(TAG, `onBackground`);\n  }\n\n  onDestroy() {\n    console.log(TAG, `onDestroy`);\n  }\n\n  onSessionCreate(want: Want, session: UIExtensionContentSession) {\n    console.log(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);\n    let param: Record<string, UIExtensionContentSession> = {\n      'session': session\n    };\n    let storage: LocalStorage = new LocalStorage(param);\n    session.loadContent('pages/extension', storage);\n  }\n\n  onSessionDestroy(session: UIExtensionContentSession) {\n    console.log(TAG, `onSessionDestroy`);\n  }\n}"
        ],
    },
    "Flex": {
        "description": "以弹性方式布局子组件的容器组件。",
        "interfaces": [
            {
                "description": "标准Flex布局容器。具体指南请参考[弹性布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/arkts-layout-development-flex-layout-V5)。",
                "params": {
                    "value": {
                        "type": "FlexOptions",
                        "required": False,
                        "description": "Flex布局的配置选项。"
                    }
                }
            }
        ],
        "attributes": {
            "direction": {
                "description": "子组件在Flex容器上排列的方向，即主轴的方向。",
                "params": {
                    "value": {
                        "type": "FlexDirection",
                        "required": False,
                        "description": "子组件排列方向。",
                        "default": "FlexDirection.Row"
                    }
                }
            },
            "wrap": {
                "description": "Flex容器是单行/列还是多行/列排列。在多行布局时，通过交叉轴方向，确认新行堆叠方向。",
                "params": {
                    "value": {
                        "type": "FlexWrap",
                        "required": False,
                        "description": "容器排列方式。",
                        "default": "FlexWrap.NoWrap"
                    }
                }
            },
            "justifyContent": {
                "description": "所有子组件在Flex容器主轴上的对齐格式。",
                "params": {
                    "value": {
                        "type": "FlexAlign",
                        "required": False,
                        "description": "主轴对齐格式。",
                        "default": "FlexAlign.Start"
                    }
                }
            },
            "alignItems": {
                "description": "所有子组件在Flex容器交叉轴上的对齐格式。",
                "params": {
                    "value": {
                        "type": "ItemAlign",
                        "required": False,
                        "description": "交叉轴对齐格式。",
                        "default": "ItemAlign.Start"
                    }
                }
            },
            "alignContent": {
                "description": "交叉轴中有额外的空间时，多行内容的对齐方式。仅在wrap为Wrap或WrapReverse下生效。",
                "params": {
                    "value": {
                        "type": "FlexAlign",
                        "required": False,
                        "description": "多行内容对齐方式。",
                        "default": "FlexAlign.Start"
                    }
                }
            },
            "space": {
                "description": "所有子组件在Flex容器主轴或交叉轴的space。space为负数、百分比或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。可选值为大于等于0的数字，或者可以转换为数字的字符串。",
                "params": {
                    "value": {
                        "type": "FlexSpaceOptions",
                        "required": False,
                        "description": "主轴或交叉轴的space。",
                        "default": "{main: LengthMetrics.px(0), cross: LengthMetrics.px(0)}"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            "这段代码实现了一个用于展示Flex布局的示例组件`FlexExample1`，演示了不同方向的Flex布局方式。具体功能如下：\n\n- **布局结构**：\n  - 使用`Column`组件将内容垂直排列，其中包含多个子`Column`和`Flex`组件，每个`Flex`组件展示了不同的布局方向。\n\n- **Flex布局方向演示**：\n  - `Row`方向：子组件在容器的主轴上从左到右水平排列。\n  - `RowReverse`方向：子组件在容器的主轴上从右到左反向水平排列。\n  - `Column`方向：子组件在容器的主轴上从上到下垂直排列。\n  - `ColumnReverse`方向：子组件在容器的主轴上从下到上反向垂直排列。\n\n- **视觉效果**：\n  - 每个`Text`组件用于标注当前Flex布局的方向，并通过`Flex`组件内的`Text`子组件展示具体的布局效果。\n  - 每个`Flex`布局的子组件宽度、高度和背景颜色有所不同，方便视觉区分和理解布局效果。\n  - 通过设置`padding`、`margin`、`backgroundColor`等属性，使得每个布局区域在界面上更加清晰和美观。\n\n此代码通过简单直观的方式展示了Flex布局的不同方向排列效果，适合用于学习和理解Flex布局在实际开发中的应用。\n// xxx.ets\n@Entry\n@Component\nstruct FlexExample1 {\n  build() {\n    Column() {\n      Column({ space: 5 }) {\n        Text('direction:Row').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({ direction: FlexDirection.Row }) { // 子组件在容器主轴上行布局\n          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n          Text('2').width('20%').height(50).backgroundColor(0xD2B48C)\n          Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)\n          Text('4').width('20%').height(50).backgroundColor(0xD2B48C)\n        }\n        .height(70)\n        .width('90%')\n        .padding(10)\n        .backgroundColor(0xAFEEEE)\n\n        Text('direction:RowReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({ direction: FlexDirection.RowReverse }) { // 子组件在容器主轴上反向行布局\n          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n          Text('2').width('20%').height(50).backgroundColor(0xD2B48C)\n          Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)\n          Text('4').width('20%').height(50).backgroundColor(0xD2B48C)\n        }\n        .height(70)\n        .width('90%')\n        .padding(10)\n        .backgroundColor(0xAFEEEE)\n\n        Text('direction:Column').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({ direction: FlexDirection.Column }) { // 子组件在容器主轴上列布局\n          Text('1').width('100%').height(40).backgroundColor(0xF5DEB3)\n          Text('2').width('100%').height(40).backgroundColor(0xD2B48C)\n          Text('3').width('100%').height(40).backgroundColor(0xF5DEB3)\n          Text('4').width('100%').height(40).backgroundColor(0xD2B48C)\n        }\n        .height(160)\n        .width('90%')\n        .padding(10)\n        .backgroundColor(0xAFEEEE)\n\n        Text('direction:ColumnReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({ direction: FlexDirection.ColumnReverse }) { // 子组件在容器主轴上反向列布局\n          Text('1').width('100%').height(40).backgroundColor(0xF5DEB3)\n          Text('2').width('100%').height(40).backgroundColor(0xD2B48C)\n          Text('3').width('100%').height(40).backgroundColor(0xF5DEB3)\n          Text('4').width('100%').height(40).backgroundColor(0xD2B48C)\n        }\n        .height(160)\n        .width('90%')\n        .padding(10)\n        .backgroundColor(0xAFEEEE)\n      }.width('100%').margin({ top: 5 })\n    }.width('100%')\n  }\n}"
            "这段代码实现了一个名为`JustifyContentFlex`的组件，该组件演示了在`Flex`布局中使用`justifyContent`属性来控制子组件在主轴（水平轴）上的对齐方式。主要功能如下：\n\n- **`JustifyContentFlex`组件**：\n  - 接受`justifyContent`属性，决定子组件在`Flex`容器主轴上的对齐方式。\n  - 内含三个`Text`子组件，宽度为容器的20%，高度为50像素，并设定了不同的背景颜色。\n  - `Flex`容器宽度设为90%，添加了10像素的内边距，并设置背景颜色。\n\n- **`FlexExample3`组件**：\n  - 演示不同`justifyContent`属性值对子组件布局的影响。\n  - 包含多个`JustifyContentFlex`组件，分别使用以下`justifyContent`属性值：\n    - `FlexAlign.Start`：子组件在容器主轴上首端对齐。\n    - `FlexAlign.Center`：子组件在容器主轴上居中对齐。\n    - `FlexAlign.End`：子组件在容器主轴上尾端对齐。\n    - `FlexAlign.SpaceBetween`：子组件在主轴上均分，首个子组件与行首对齐，最后一个与行尾对齐。\n    - `FlexAlign.SpaceAround`：子组件在主轴上均分，首个子组件与行首和最后一个与行尾的距离是相邻子组件间距的一半。\n    - `FlexAlign.SpaceEvenly`：子组件在主轴上均分，子组件之间的距离以及它们与行首、行尾的距离相等。\n\n此代码通过多个`Flex`容器示例，直观地展示了`justifyContent`属性在`Flex`布局中的不同对齐效果，帮助理解如何控制子组件在主轴上的排列方式。\n// xxx.ets\n@Component\nstruct JustifyContentFlex {\n  justifyContent : number = 0;\n\n  build() {\n    Flex({ justifyContent: this.justifyContent }) {\n      Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)\n      Text('2').width('20%').height(50).backgroundColor(0xD2B48C)\n      Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)\n    }\n    .width('90%')\n    .padding(10)\n    .backgroundColor(0xAFEEEE)\n  }\n}\n\n@Entry\n@Component\nstruct FlexExample3 {\n  build() {\n    Column() {\n      Column({ space: 5 }) {\n        Text('justifyContent:Start').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        JustifyContentFlex({ justifyContent: FlexAlign.Start }) // 子组件在容器主轴上首端对齐\n\n        Text('justifyContent:Center').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        JustifyContentFlex({ justifyContent: FlexAlign.Center }) // 子组件在容器主轴上居中对齐\n\n        Text('justifyContent:End').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        JustifyContentFlex({ justifyContent: FlexAlign.End }) // 子组件在容器主轴上尾端对齐\n\n        Text('justifyContent:SpaceBetween').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        JustifyContentFlex({ justifyContent: FlexAlign.SpaceBetween }) // 子组件在容器主轴上均分容器布局，第一个子组件与行首对齐，最后一个子组件与行尾对齐。\n\n        Text('justifyContent:SpaceAround').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        JustifyContentFlex({ justifyContent: FlexAlign.SpaceAround }) // 子组件在容器主轴上均分容器布局，第一个子组件到行首的距离和最后一个子组件到行尾的距离是相邻子组件之间距离的一半。\n\n        Text('justifyContent:SpaceEvenly').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        JustifyContentFlex({ justifyContent: FlexAlign.SpaceEvenly }) // 子组件在容器主轴上均分容器布局，子组件之间的距离与第一子组件到行首、最后一个子组件到行尾的距离相等\n      }.width('100%').margin({ top: 5 })\n    }.width('100%')\n  }\n}"
            "这段代码实现了一个名为`AlignContentFlex`的组件，以及一个`FlexExample5`的示例组件，展示了`Flex`布局中的`alignContent`属性在多行布局中的不同对齐方式。主要功能如下：\n\n- **`AlignContentFlex`组件**：\n  - 接受`alignContent`属性，控制多行`Flex`布局中各行的对齐方式。\n  - 容器内包含三个`Text`子组件，每个子组件的宽度为容器的50%，高度为20像素，并设置不同的背景颜色。\n  - `Flex`容器启用了换行（`wrap`），宽度设置为90%，高度为90像素，内边距为10像素，并设置背景颜色。\n\n- **`FlexExample5`组件**：\n  - 演示了`alignContent`属性在多行`Flex`布局中的不同对齐效果。\n  - 包含多个`AlignContentFlex`组件，分别使用以下`alignContent`属性值：\n    - `FlexAlign.Start`：多行布局下，子组件在首行对齐。\n    - `FlexAlign.Center`：多行布局下，子组件在中间行对齐。\n    - `FlexAlign.End`：多行布局下，子组件在末行对齐。\n    - `FlexAlign.SpaceBetween`：多行布局下，第一行子组件与列首对齐，最后一行子组件与列尾对齐。\n    - `FlexAlign.SpaceAround`：多行布局下，第一行子组件到列首的距离和最后一行子组件到列尾的距离是相邻行之间距离的一半。\n    - `FlexAlign.SpaceEvenly`：多行布局下，子组件行之间的距离与第一行到列首的距离、最后一行到列尾的距离相等。\n\n此代码通过多个`Flex`容器示例，展示了`alignContent`属性在多行布局中的不同对齐方式，帮助理解如何在多行布局中控制子组件的排列和分布。\n// xxx.ets\n@Component\nstruct AlignContentFlex {\n  alignContent: number = 0;\n\n  build() {\n    Flex({ wrap: FlexWrap.Wrap, alignContent: this.alignContent }) {\n      Text('1').width('50%').height(20).backgroundColor(0xF5DEB3)\n      Text('2').width('50%').height(20).backgroundColor(0xD2B48C)\n      Text('3').width('50%').height(20).backgroundColor(0xD2B48C)\n    }\n    .size({ width: '90%', height: 90 })\n    .padding(10)\n    .backgroundColor(0xAFEEEE)\n  }\n}\n\n@Entry\n@Component\nstruct FlexExample5 {\n  build() {\n    Column() {\n      Column({ space: 5 }) {\n        Text('alignContent:Start').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        AlignContentFlex({ alignContent: FlexAlign.Start }) // 多行布局下子组件首部对齐\n\n        Text('alignContent:Center').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        AlignContentFlex({ alignContent: FlexAlign.Center }) // 多行布局下子组件居中对齐\n\n        Text('alignContent:End').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        AlignContentFlex({ alignContent: FlexAlign.End }) // 多行布局下子组件尾部对齐\n\n        Text('alignContent:SpaceBetween').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        AlignContentFlex({ alignContent: FlexAlign.SpaceBetween }) // 多行布局下第一行子组件与列首对齐，最后一行子组件与列尾对齐\n\n        Text('alignContent:SpaceAround').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        AlignContentFlex({ alignContent: FlexAlign.SpaceAround }) // 多行布局下第一行子组件到列首的距离和最后一行子组件到列尾的距离是相邻行之间距离的一半\n\n        Text('alignContent:SpaceEvenly').fontSize(9).fontColor(0xCCCCCC).width('90%')\n        Flex({\n          wrap: FlexWrap.Wrap,\n          alignContent: FlexAlign.SpaceEvenly\n        }) { // 多行布局下相邻行之间的距离与第一行子组件到列首的距离、最后一行子组件到列尾的距离完全一样\n          Text('1').width('50%').height(20).backgroundColor(0xF5DEB3)\n          Text('2').width('50%').height(20).backgroundColor(0xD2B48C)\n          Text('3').width('50%').height(20).backgroundColor(0xF5DEB3)\n          Text('4').width('50%').height(20).backgroundColor(0xD2B48C)\n          Text('5').width('50%').height(20).backgroundColor(0xF5DEB3)\n        }\n        .size({ width: '90%', height: 100 })\n        .padding({ left: 10, right: 10 })\n        .backgroundColor(0xAFEEEE)\n      }.width('100%').margin({ top: 5 })\n    }.width('100%')\n  }\n}"
        ],
    },
    "FlowItem": {"description": "瀑布流组件的子组件，用来展示瀑布流具体item，支持单个子组件。"},
    "FolderStack": {
        "description": "FolderStack继承于Stack(层叠布局)控件，新增了折叠屏悬停能力，通过识别upperItems自动避让折叠屏折痕区后移到上半屏，可以包含多个子组件。"},
    "FormLink": {
        "description": "提供静态卡片交互组件，用于静态卡片内部和提供方应用间的交互，当前支持router、message和call三种类型的事件，支持单个子组件。"},
    "GridCol": {
        "description": "栅格子组件，必须作为栅格容器组件(GridRow)的子组件使用。可以包含单个子组件。",
        "details": None,
        "interfaces": [
            {
                "description": "GridCol(option?: GridColOptions)",
                "params": {
                    "option": {
                        "type": "GridColOptions",
                        "required": False,
                        "description": "栅格布局子组件参数。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "span": {
                "description": "设置占用列数。span为0，意味着该元素不参与布局计算，即不会被渲染。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "GridColColumnOption"
                        ],
                        "required": True,
                        "description": "占用列数。",
                        "default": 1
                    }
                }
            },
            "gridColOffset": {
                "description": "设置相对于前一个栅格子组件偏移的列数。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "GridColColumnOption"
                        ],
                        "required": True,
                        "description": "相对于前一个栅格子组件偏移的列数。",
                        "default": 0
                    }
                }
            },
            "order": {
                "description": "设置元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "GridColColumnOption"
                        ],
                        "required": True,
                        "description": "元素的序号。",
                        "default": 0
                    }
                }
            }
        },
        "events": {},
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何使用GridRow组件来创建一个栅格布局，通过设置不同的属性来调整栅格的列数、间距和对齐方式。\\n总体功能与效果描述：\\n通过GridRow和GridCol组件的组合，实现了一个响应式的栅格布局，能够根据屏幕宽度自动调整列的显示。\\n*/\\n\\n// GridRowExample.ets\\n@Entry\\n@Component\\nstruct GridRowExample {\\n  build() {\\n    Column({ space: 5 }) {\\n      // 创建一个GridRow容器，设置列数为3，列间距为10，内容水平和垂直居中对齐\\n      GridRow({ columns: 3, gutter: 10, alignContent: FlexAlign.Center, alignItems: VerticalAlign.Center }) {\\n        // 第一个栅格列，设置背景色为蓝色，宽度为100，高度为50\\n        GridCol() {\\n          Text('Column 1')\\n            .fontSize(16)\\n            .fontColor(Color.White)\\n        }\\n        .backgroundColor(Color.Blue)\\n        .width(100)\\n        .height(50)\\n\\n        // 第二个栅格列，设置背景色为绿色，宽度为100，高度为50\\n        GridCol() {\\n          Text('Column 2')\\n            .fontSize(16)\\n            .fontColor(Color.White)\\n        }\\n        .backgroundColor(Color.Green)\\n        .width(100)\\n        .height(50)\\n\\n        // 第三个栅格列，设置背景色为红色，宽度为100，高度为50\\n        GridCol() {\\n          Text('Column 3')\\n            .fontSize(16)\\n            .fontColor(Color.White)\\n        }\\n        .backgroundColor(Color.Red)\\n        .width(100)\\n        .height(50)\\n      }\\n      .width('100%')\\n      .height(100)\\n      .backgroundColor(Color.Gray)\\n\\n      // 创建另一个GridRow容器，设置列数为2，列间距为5，内容水平和垂直居中对齐\\n      GridRow({ columns: 2, gutter: 5, alignContent: FlexAlign.Center, alignItems: VerticalAlign.Center }) {\\n        // 第一个栅格列，设置背景色为黄色，宽度为100，高度为50\\n        GridCol() {\\n          Text('Column 1')\\n            .fontSize(16)\\n            .fontColor(Color.Black)\\n        }\\n        .backgroundColor(Color.Yellow)\\n        .width(100)\\n        .height(50)\\n\\n        // 第二个栅格列，设置背景色为紫色，宽度为100，高度为50\\n        GridCol() {\\n          Text('Column 2')\\n            .fontSize(16)\\n            .fontColor(Color.White)\\n        }\\n        .backgroundColor(Color.Purple)\\n        .width(100)\\n        .height(50)\\n      }\\n      .width('100%')\\n      .height(100)\\n      .backgroundColor(Color.Gray)\\n    }\\n    .width('100%')\\n    .height('100%')\\n    .padding(10)\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "GridRow": {
        "description": "栅格容器组件，仅可以和栅格子组件(GridCol)在栅格布局场景中使用。",
        "details": "栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题，保证不同设备上各个模块的布局一致性。",
        "interfaces": [
            {
                "description": "GridRow(option?: GridRowOptions)",
                "params": {
                    "option": {
                        "type": "GridRowOptions",
                        "required": False,
                        "description": "栅格布局子组件参数。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "alignItems10+": {
                "description": "设置GridRow中的GridCol垂直主轴方向对齐方式。",
                "params": {
                    "value": {
                        "type": "ItemAlign",
                        "required": True,
                        "description": "GridRow中的GridCol垂直主轴方向对齐方式。",
                        "default": "ItemAlign.Start"
                    }
                }
            }
        },
        "events": {
            "onBreakpointChange": {
                "description": "断点发生变化时触发回调。",
                "params": {
                    "breakpoints": {
                        "type": "string",
                        "required": False,
                        "description": "取值为\"xs\"、\"sm\"、\"md\"、\"lg\"、\"xl\"、\"xxl\"。",
                        "default": None
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何使用GridRow和GridCol组件创建一个响应式的网格布局。通过设置不同的断点和列宽，实现根据窗口大小调整布局的效果。同时，通过监听断点变化事件，实时更新当前断点状态。\\n\\n总体功能与效果描述：\\n1. 创建一个包含多个颜色块的网格布局。\\n2. 根据窗口大小调整网格列的宽度。\\n3. 监听窗口断点变化，实时更新当前断点状态。\\n*/\\n\\n// GridRowExample.ets\\n@Entry\\n@Component\\nstruct GridRowExample {\\n  // 定义颜色数组，用于网格列的背景色\\n  @State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown]\\n  // 当前断点状态，初始为'unknown'\\n  @State currentBp: string = 'unknown'\\n\\n  build() {\\n    Column() {\\n      // 创建一个GridRow组件，设置列数、间距、断点和方向\\n      GridRow({\\n        columns: 5, // 网格列数\\n        gutter: { x: 5, y: 10 }, // 列间距\\n        breakpoints: { value: [\"400vp\", \"600vp\", \"800vp\"], reference: BreakpointsReference.WindowSize }, // 断点设置\\n        direction: GridRowDirection.Row // 网格方向\\n      }) {\\n        // 遍历颜色数组，为每个颜色创建一个GridCol组件\\n        ForEach(this.bgColors, (color: Color) => {\\n          GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 }, offset: 0, order: 0 }) {\\n            // 创建一个Row组件，设置宽度和高度\\n            Row().width(\"100%\").height(\"20vp\")\\n          }.borderColor(color).borderWidth(2) // 设置边框颜色和宽度\\n        })\\n      }.width(\"100%\").height(\"100%\") // 设置GridRow的宽度和高度\\n      .onBreakpointChange((breakpoint) => {\\n        // 监听断点变化事件，更新当前断点状态\\n        this.currentBp = breakpoint\\n      })\\n    }.width('80%').margin({ left: 10, top: 5, bottom: 5 }).height(200) // 设置Column的宽度、外边距和高度\\n    .border({ color: '#880606', width: 2 }) // 设置边框颜色和宽度\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "Grid": {
        "description": "网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。",
        "details": "该组件从API Version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。",
        "interfaces": [
            {
                "description": "Grid(scroller?: Scroller, layoutOptions?: GridLayoutOptions)",
                "params": {
                    "scroller": {
                        "type": "Scroller",
                        "required": False,
                        "description": "可滚动组件的控制器。用于与可滚动组件进行绑定。",
                        "default": None
                    },
                    "layoutOptions": {
                        "type": "GridLayoutOptions",
                        "required": False,
                        "description": "布局选项。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "columnsTemplate": {
                "description": "设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前网格布局列的数量或最小列宽值。",
                        "default": None
                    }
                }
            },
            "rowsTemplate": {
                "description": "设置当前网格布局行的数量、固定行高或最小行高值，不设置时默认1行。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前网格布局行的数量或最小行高值。",
                        "default": None
                    }
                }
            },
            "columnsGap": {
                "description": "设置列与列的间距。设置为小于0的值时，按默认值显示。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "列与列的间距。",
                        "default": "0"
                    }
                }
            },
            "rowsGap": {
                "description": "设置行与行的间距。设置为小于0的值时，按默认值显示。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "行与行的间距。",
                        "default": "0"
                    }
                }
            },
            "scrollBar": {
                "description": "设置滚动条状态。",
                "params": {
                    "value": {
                        "type": "BarState",
                        "required": True,
                        "description": "滚动条状态。",
                        "default": "BarState.Auto"
                    }
                }
            },
            "scrollBarColor": {
                "description": "设置滚动条的颜色。",
                "params": {
                    "value": {
                        "type": [
                            "Color",
                            "number",
                            "string"
                        ],
                        "required": True,
                        "description": "滚动条的颜色。",
                        "default": "'#182431'（40%不透明度）"
                    }
                }
            },
            "scrollBarWidth": {
                "description": "设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Grid组件主轴方向的高度，则滚动条的宽度会变为默认值。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "string"
                        ],
                        "required": True,
                        "description": "滚动条的宽度。",
                        "default": "4"
                    }
                }
            },
            "cachedCount": {
                "description": "设置预加载的GridItem的数量，只在LazyForEach和开启了virtualScroll开关的Repeat中生效。设置为小于0的值时，按默认值显示。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "预加载的GridItem的数量。",
                        "default": "1"
                    }
                }
            },
            "editMode": {
                "description": "设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "Grid是否进入编辑模式。",
                        "default": "false"
                    }
                }
            },
            "layoutDirection": {
                "description": "设置布局的主轴方向。",
                "params": {
                    "value": {
                        "type": "GridDirection",
                        "required": True,
                        "description": "布局的主轴方向。",
                        "default": "GridDirection.Row"
                    }
                }
            },
            "maxCount": {
                "description": "设置可显示的最大行数或列数。设置为小于1的值时，按默认值显示。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "可显示的最大行数或列数。",
                        "default": "Infinity"
                    }
                }
            },
            "minCount": {
                "description": "设置可显示的最小行数或列数。设置为小于1的值时，按默认值显示。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "可显示的最小行数或列数。",
                        "default": "1"
                    }
                }
            },
            "cellLength": {
                "description": "设置一行的高度或者一列的宽度。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "一行的高度或者一列的宽度。",
                        "default": "第一个元素的大小"
                    }
                }
            },
            "multiSelectable": {
                "description": "设置是否开启鼠标框选。开启框选后，可以配合Griditem的selected属性和onSelect事件获取GridItem的选中状态，还可以设置选中态样式（无默认选中样式）。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启鼠标框选。",
                        "default": "false"
                    }
                }
            },
            "supportAnimation": {
                "description": "设置是否支持动画。当前支持GridItem拖拽动画。仅在滚动模式下（只设置rowsTemplate、columnsTemplate其中一个）支持动画。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否支持动画。",
                        "default": "false"
                    }
                }
            },
            "edgeEffect": {
                "description": "设置边缘滑动效果。",
                "params": {
                    "value": {
                        "type": "EdgeEffect",
                        "required": True,
                        "description": "Grid组件的边缘滑动效果，支持弹簧效果和阴影效果。",
                        "default": "EdgeEffect.None"
                    },
                    "options": {
                        "type": "EdgeEffectOptions",
                        "required": False,
                        "description": "组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。",
                        "default": "{ alwaysEnabled: false }"
                    }
                }
            },
            "enableScrollInteraction": {
                "description": "设置是否支持滚动手势，当设置为false时，无法通过手指或者鼠标滚动，但不影响控制器的滚动接口。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否支持滚动手势。",
                        "default": "true"
                    }
                }
            },
            "nestedScroll": {
                "description": "设置嵌套滚动选项。设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。",
                "params": {
                    "value": {
                        "type": "NestedScrollOptions",
                        "required": True,
                        "description": "嵌套滚动选项。",
                        "default": None
                    }
                }
            },
            "friction": {
                "description": "设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。设置为小于等于0的值时，按默认值处理。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "Resource"
                        ],
                        "required": True,
                        "description": "摩擦系数。",
                        "default": "非可穿戴设备为0.75，可穿戴设备为0.9。"
                    }
                }
            }
        },
        "events": {
            "onScrollIndex": {
                "description": "当前网格显示的起始位置/终止位置的item发生变化时触发。网格初始化时会触发一次。Grid显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。",
                "params": {
                    "first": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示的网格起始位置的索引值。",
                        "default": None
                    },
                    "last": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示的网格终止位置的索引值。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDragStart": {
                "description": "开始拖拽网格元素时触发。返回void表示不能拖拽。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    },
                    "itemIndex": {
                        "type": "number",
                        "required": True,
                        "description": "被拖拽网格元素索引值。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDragEnter": {
                "description": "拖拽进入网格元素范围内时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDragMove": {
                "description": "拖拽在网格元素范围内移动时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    },
                    "itemIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽起始位置。",
                        "default": None
                    },
                    "insertIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽插入位置。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDragLeave": {
                "description": "拖拽离开网格元素时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    },
                    "itemIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽离开的网格元素索引值。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDrop": {
                "description": "绑定该事件的网格元素可作为拖拽释放目标，当在网格元素内停止拖拽时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    },
                    "itemIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽起始位置。",
                        "default": None
                    },
                    "insertIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽插入位置。",
                        "default": None
                    },
                    "isSuccess": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否成功释放。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onScrollBarUpdate": {
                "description": "当前网格显示的起始位置item发生变化时触发，可通过该回调设置滚动条的位置及长度。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示的网格起始位置的索引值。",
                        "default": None
                    },
                    "offset": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示的网格起始位置元素相对网格显示起始位置的偏移，单位vp。",
                        "default": None
                    }
                },
                "returns": {
                    "type": "ComputedBarAttribute",
                    "description": "滚动条的位置及长度。"
                }
            },
            "onReachStart": {
                "description": "网格到达起始位置时触发。",
                "params": {},
                "returns": None
            },
            "onReachEnd": {
                "description": "网格到达末尾位置时触发。",
                "params": {},
                "returns": None
            },
            "onScrollFrameBegin": {
                "description": "网格开始滑动时触发，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，网格将按照返回值的实际滑动量进行滑动。",
                "params": {
                    "offset": {
                        "type": "number",
                        "required": True,
                        "description": "即将发生的滑动量，单位vp。",
                        "default": None
                    },
                    "state": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滑动状态。",
                        "default": None
                    }
                },
                "returns": {
                    "type": "{ offsetRemain: number }",
                    "description": "实际滑动量，单位vp。"
                }
            },
            "onScrollStart": {
                "description": "网格滑动开始时触发。手指拖动网格或网格的滚动条触发的滑动开始时，会触发该事件。使用Scroller滑动控制器触发的带动画的滑动，动画开始时会触发该事件。",
                "params": {},
                "returns": None
            },
            "onScrollStop": {
                "description": "网格滑动停止时触发。手指拖动网格或网格的滚动条触发的滑动，手指离开屏幕并且滑动停止时会触发该事件。使用Scroller滑动控制器触发的带动画的滑动，动画停止会触发该事件。",
                "params": {},
                "returns": None
            },
            "onScroll": {
                "description": "网格滑动时触发。",
                "params": {
                    "scrollOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动的偏移量，Grid的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。",
                        "default": None
                    },
                    "scrollState": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滑动状态。",
                        "default": None
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何使用Grid组件的layoutDirection、maxCount、minCount、cellLength属性来控制网格的布局和显示。通过设置这些属性，可以灵活地调整网格的排列方式和显示数量。\\n\\n总体功能与效果描述：\\n- layoutDirection属性用于设置网格的布局方向。\\n- maxCount属性用于限制每行最多显示的网格项数量。\\n- minCount属性用于设置每行最少显示的网格项数量。\\n- cellLength属性用于设置网格单元的长度。\\n*/\\n\\n// GridExample.ets\\n@Entry\\n@Component\\nstruct GridExample {\\n  @State numbers: string[] = []\\n\\n  // 组件初始化时填充数据\\n  aboutToAppear() {\\n    for (let i = 1; i <= 30; i++) {\\n      this.numbers.push(i + '')\\n    }\\n  }\\n\\n  build() {\\n    Scroll() {\\n      Column({ space: 5 }) {\\n        Blank()\\n        Text('rowsTemplate、columnsTemplate都不设置layoutDirection、maxcount、minCount、cellLength才生效')\\n          .fontSize(15).fontColor(0xCCCCCC).width('90%')\\n        \\n        Grid() {\\n          ForEach(this.numbers, (day: string) => {\\n            GridItem() {\\n              Text(day).fontSize(16).backgroundColor(0xF9CF93)\\n            }.width(40).height(80).borderWidth(2).borderColor(Color.Red)\\n          }, (day: string) => day)\\n        }\\n        .height(300) // 设置网格高度\\n        .columnsGap(10) // 设置列间距\\n        .rowsGap(10) // 设置行间距\\n        .backgroundColor(0xFAEEE0) // 设置背景颜色\\n        .maxCount(6) // 设置每行最多显示6个网格项\\n        .minCount(2) // 设置每行最少显示2个网格项\\n        .cellLength(0) // 设置网格单元长度为0，表示不限制\\n        .layoutDirection(GridDirection.Row) // 设置网格布局方向为行优先\\n      }\\n      .width('90%').margin({ top: 5, left: 5, right: 5 })\\n      .align(Alignment.Center)\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n1. 使用@State装饰器管理Grid的列数和数据列表。\\n2. 在aboutToAppear生命周期函数中，从AppStorage中读取上次的列数设置。\\n3. 在build方法中，构建UI界面，包括一个文本提示和一个Grid组件。\\n4. Grid组件使用双指缩放手势来动态调整列数。\\n5. 通过PinchGesture的onActionEnd事件处理缩放结束时的逻辑，调整列数并保存到AppStorage。\\n总体功能与效果描述：\\n该示例展示了如何通过双指缩放手势动态调整Grid组件的列数，并在应用重启时恢复上次的列数设置。\\n*/\\n\\n// GridExample.ets\\n@Entry\\n@Component\\nstruct GridExample {\\n  @State numbers: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']\\n  @State columns: number = 2\\n\\n  aboutToAppear() {\\n    let lastCount = AppStorage.get<number>('columnsCount')\\n    if (typeof lastCount != 'undefined') {\\n      this.columns = lastCount\\n    }\\n  }\\n\\n  build() {\\n    Column({ space: 5 }) {\\n      Row() {\\n        Text('双指缩放改变列数')\\n          .height('5%')\\n          .margin({ top: 10, left: 20 })\\n      }\\n\\n      Grid() {\\n        ForEach(this.numbers, (day: string) => {\\n          ForEach(this.numbers, (day: string) => {\\n            GridItem() {\\n              Text(day)\\n                .fontSize(16)\\n                .backgroundColor(0xF9CF93)\\n                .width('100%')\\n                .height(80)\\n                .textAlign(TextAlign.Center)\\n            }\\n          }, (day: string) => day)\\n        }, (day: string) => day)\\n      }\\n      .columnsTemplate('1fr '.repeat(this.columns))\\n      .columnsGap(10)\\n      .rowsGap(10)\\n      .width('90%')\\n      .scrollBar(BarState.Off)\\n      .backgroundColor(0xFAEEE0)\\n      .height('100%')\\n      .cachedCount(3)\\n\\n      .animation({\\n        duration: 300,\\n        curve: Curve.Smooth\\n      })\\n      .priorityGesture(\\n        PinchGesture()\\n          .onActionEnd((event: GestureEvent) => {\\n            console.info('end scale:' + event.scale)\\n\\n            if (event.scale > 2) {\\n              this.columns--\\n            } else if (event.scale < 0.6) {\\n              this.columns++\\n            }\\n\\n            this.columns = Math.min(4, Math.max(1, this.columns));\\n            AppStorage.setOrCreate<number>('columnsCount', this.columns)\\n          })\\n      )\\n    }.width('100%').margin({ top: 5 })\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用Grid组件实现拖拽排序功能。通过设置Grid的editMode属性为true，使Grid进入编辑模式，允许内部GridItem被拖拽。在onItemDragStart回调中设置拖拽过程中显示的图片，在onItemDrop回调中处理拖拽完成后的数据交换逻辑。\\n\\n总体功能与效果描述：\\n用户可以通过拖拽Grid中的GridItem来改变它们的排列顺序。拖拽过程中会显示一个自定义的拖拽图片，拖拽完成后，数据数组中的元素会根据新的位置进行交换。\\n*/\\n\\n// GridExample.ets\\n@Entry\\n@Component\\nstruct GridExample {\\n  @State numbers: string[] = [] // 存储GridItem显示的数字\\n  scroller: Scroller = new Scroller() // 用于Grid的滚动控制\\n  @State text: string = 'drag' // 拖拽过程中显示的文本\\n\\n  // 构建拖拽过程中显示的图片\\n  @Builder pixelMapBuilder() { \\n    Column() {\\n      Text(this.text)\\n        .fontSize(16)\\n        .backgroundColor(0xF9CF93)\\n        .width(80)\\n        .height(80)\\n        .textAlign(TextAlign.Center)\\n    }\\n  }\\n\\n  // 组件初始化时填充numbers数组\\n  aboutToAppear() {\\n    for (let i = 1; i <= 15; i++) {\\n      this.numbers.push(i + '')\\n    }\\n  }\\n\\n  // 交换数组中两个元素的位置\\n  changeIndex(index1: number, index2: number) { \\n    let temp: string;\\n    temp = this.numbers[index1];\\n    this.numbers[index1] = this.numbers[index2];\\n    this.numbers[index2] = temp;\\n  }\\n\\n  // 构建Grid组件\\n  build() {\\n    Column({ space: 5 }) {\\n      Grid(this.scroller) {\\n        ForEach(this.numbers, (day: string) => {\\n          GridItem() {\\n            Text(day)\\n              .fontSize(16)\\n              .backgroundColor(0xF9CF93)\\n              .width(80)\\n              .height(80)\\n              .textAlign(TextAlign.Center)\\n          }\\n        })\\n      }\\n      .columnsTemplate('1fr 1fr 1fr') // 设置列模板\\n      .columnsGap(10) // 设置列间距\\n      .rowsGap(10) // 设置行间距\\n      .width('90%') // 设置宽度\\n      .backgroundColor(0xFAEEE0) // 设置背景颜色\\n      .height(300) // 设置高度\\n      .editMode(true) // 设置Grid进入编辑模式\\n      .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { \\n        this.text = this.numbers[itemIndex] // 设置拖拽过程中显示的文本\\n        return this.pixelMapBuilder() // 返回拖拽过程中显示的图片\\n      })\\n      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => { \\n        if (!isSuccess || insertIndex >= this.numbers.length) {\\n          return\\n        }\\n        console.info('beixiang' + itemIndex + '', insertIndex + '') \\n        this.changeIndex(itemIndex, insertIndex) // 交换数组中两个元素的位置\\n      })\\n    }.width('100%').margin({ top: 5 })\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何在Grid组件中使用columnsTemplate属性，通过auto-fill、auto-fit和auto-stretch三种不同的方式来动态调整列的数量和宽度。\\n总体功能与效果描述：\\n通过三个不同的Grid示例，分别展示了auto-fill、auto-fit和auto-stretch的效果，使得用户可以根据不同的需求选择合适的列布局方式。\\n*/\\n\\n// GridColumnsTemplate.ets\\n@Entry\\n@Component\\nstruct GridColumnsTemplate {\\n  data: number[] = [0, 1, 2, 3, 4, 5]\\n  data1: number[] = [0, 1, 2, 3, 4, 5]\\n  data2: number[] = [0, 1, 2, 3, 4, 5]\\n\\n  build() {\\n    Column({ space: 10 }) {\\n      Text('auto-fill 根据设定的列宽自动计算列数').width('90%')\\n      // 使用auto-fill模式，根据设定的列宽自动计算列数\\n      Grid() {\\n        ForEach(this.data, (item: number) => {\\n          GridItem() {\\n            Text('N' + item).height(80)\\n          }\\n          .backgroundColor(Color.Orange)\\n        })\\n      }\\n      .width('90%')\\n      .border({ width: 1, color: Color.Black })\\n      .columnsTemplate('repeat(auto-fill, 70)') // 设置列模板为auto-fill，每列宽度为70\\n      .columnsGap(10) // 设置列间距\\n      .rowsGap(10) // 设置行间距\\n      .height(150)\\n\\n      Text('auto-fit 先根据设定的列宽计算列数，余下的空间会均分到每一列中').width('90%')\\n      // 使用auto-fit模式，先根据设定的列宽计算列数，余下的空间会均分到每一列中\\n      Grid() {\\n        ForEach(this.data1, (item: number) => {\\n          GridItem() {\\n            Text('N' + item).height(80)\\n          }\\n          .backgroundColor(Color.Orange)\\n        })\\n      }\\n      .width('90%')\\n      .border({ width: 1, color: Color.Black })\\n      .columnsTemplate('repeat(auto-fit, 70)') // 设置列模板为auto-fit，每列宽度为70\\n      .columnsGap(10) // 设置列间距\\n      .rowsGap(10) // 设置行间距\\n      .height(150)\\n\\n      Text('auto-stretch 先根据设定的列宽计算列数，余下的空间会均分到每个列间距中').width('90%')\\n      // 使用auto-stretch模式，先根据设定的列宽计算列数，余下的空间会均分到每个列间距中\\n      Grid() {\\n        ForEach(this.data2, (item: number) => {\\n          GridItem() {\\n            Text('N' + item).height(80)\\n          }\\n          .backgroundColor(Color.Orange)\\n        })\\n      }\\n      .width('90%')\\n      .border({ width: 1, color: Color.Black })\\n      .columnsTemplate('repeat(auto-stretch, 70)') // 设置列模板为auto-stretch，每列宽度为70\\n      .columnsGap(10) // 设置列间距\\n      .rowsGap(10) // 设置行间距\\n      .height(150)\\n    }\\n    .width('100%')\\n    .height('100%')\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用GridLayoutOptions的irregularIndexes和onGetIrregularSizeByIndex属性来创建一个具有不规则大小的网格布局。通过设置不同的布局选项，可以实现不同的网格布局效果。\\n\\n总体功能与效果描述：\\n1. 第一个Grid组件使用layoutOptions1，其中设置了两个不规则索引，但未定义具体的不规则大小。\\n2. 第二个Grid组件使用layoutOptions2，其中不仅设置了不规则索引，还通过onGetIrregularSizeByIndex回调函数动态计算每个不规则索引的大小。\\n*/\\n\\n// GridExample.ets\\n@Entry\\n@Component\\nstruct GridExample {\\n  @State numbers: String[] = ['0', '1', '2', '3', '4']\\n  scroller: Scroller = new Scroller()\\n\\n  // 定义第一个网格布局选项，设置不规则索引但不定义具体大小\\n  layoutOptions1: GridLayoutOptions = {\\n    regularSize: [1, 1],        \\n    irregularIndexes: [0, 6],   \\n  }\\n\\n  // 定义第二个网格布局选项，设置不规则索引并通过回调函数定义具体大小\\n  layoutOptions2: GridLayoutOptions = {\\n    regularSize: [1, 1],\\n    irregularIndexes: [0, 7],   \\n    onGetIrregularSizeByIndex: (index: number) => {\\n      if (index === 0) {\\n        return [1, 5] // 第一个不规则索引的大小\\n      }\\n      return [1, index % 6 + 1] // 其他不规则索引的大小\\n    }\\n  }\\n\\n  build() {\\n    Column({ space: 5 }) {\\n      // 第一个Grid组件，使用layoutOptions1\\n      Grid(this.scroller, this.layoutOptions1) {\\n        ForEach(this.numbers, (day: string) => {\\n          ForEach(this.numbers, (day: string) => {\\n            GridItem() {\\n              Text(day)\\n                .fontSize(16)\\n                .backgroundColor(0xF9CF93)\\n                .width('100%')\\n                .height(80)\\n                .textAlign(TextAlign.Center)\\n            }.selectable(false)\\n          }, (day: string) => day)\\n        }, (day: string) => day)\\n      }\\n      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')\\n      .columnsGap(10)\\n      .rowsGap(10)\\n      .multiSelectable(true)\\n      .scrollBar(BarState.Off)\\n      .width('90%')\\n      .backgroundColor(0xFAEEE0)\\n      .height(300)\\n\\n      Text('scroll').fontColor(0xCCCCCC).fontSize(9).width('90%')\\n\\n      // 第二个Grid组件，使用layoutOptions2\\n      Grid(undefined, this.layoutOptions2) {\\n        ForEach(this.numbers, (day: string) => {\\n          ForEach(this.numbers, (day: string) => {\\n            GridItem() {\\n              Text(day)\\n                .fontSize(16)\\n                .backgroundColor(0xF9CF93)\\n                .width('100%')\\n                .height(80)\\n                .textAlign(TextAlign.Center)\\n            }\\n          }, (day: string) => day)\\n        }, (day: string) => day)\\n      }\\n      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')\\n      .columnsGap(10)\\n      .rowsGap(10)\\n      .scrollBar(BarState.Off)\\n      .width('90%')\\n      .backgroundColor(0xFAEEE0)\\n      .height(300)\\n    }.width('100%').margin({ top: 5 })\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用鸿蒙ArkUI框架创建一个可滚动的网格组件。通过Grid组件和Scroller对象，实现了网格的滚动功能，并监听了滚动事件。\\n\\n总体功能与效果描述：\\n- 创建一个包含多个GridItem的网格组件。\\n- 设置网格的列模板、列间距、行间距等属性。\\n- 启用滚动交互，并设置滚动效果、滚动条样式。\\n- 监听滚动事件，如滚动开始、滚动停止、滚动到边缘等，并在控制台输出相关信息。\\n- 提供一个按钮，用于触发下一页的滚动。\\n*/\\n\\n// GridExample.ets\\n@Entry\\n@Component\\nstruct GridExample {\\n  @State numbers: String[] = ['0', '1', '2', '3', '4'] // 定义网格中显示的数字\\n  scroller: Scroller = new Scroller() // 创建一个Scroller对象，用于控制滚动\\n  @State gridPosition: number = 0 // 记录网格当前位置\\n\\n  build() {\\n    Column({ space: 5 }) {\\n      Text('scroll').fontColor(0xCCCCCC).fontSize(9).width('90%') // 显示一个文本标签\\n\\n      Grid(this.scroller) {\\n        ForEach(this.numbers, (day: string) => {\\n          ForEach(this.numbers, (day: string) => {\\n            GridItem() {\\n              Text(day)\\n                .fontSize(16)\\n                .backgroundColor(0xF9CF93)\\n                .width('100%')\\n                .height(80)\\n                .textAlign(TextAlign.Center)\\n            }\\n          }, (day: string) => day)\\n        }, (day: string) => day)\\n      }\\n      .columnsTemplate('1fr 1fr 1fr 1fr 1fr') // 设置网格的列模板\\n      .columnsGap(10) // 设置列间距\\n      .rowsGap(10) // 设置行间距\\n      .friction(0.6) // 设置滚动摩擦系数\\n      .enableScrollInteraction(true) // 启用滚动交互\\n      .supportAnimation(false) // 禁用滚动动画\\n      .multiSelectable(false) // 禁用多选\\n      .edgeEffect(EdgeEffect.Spring) // 设置边缘效果为弹性\\n      .scrollBar(BarState.On) // 显示滚动条\\n      .scrollBarColor(Color.Grey) // 设置滚动条颜色\\n      .scrollBarWidth(4) // 设置滚动条宽度\\n      .width('90%') // 设置网格宽度\\n      .backgroundColor(0xFAEEE0) // 设置背景颜色\\n      .height(300) // 设置网格高度\\n      .onScrollIndex((first: number, last: number) => {\\n        console.info(first.toString())\\n        console.info(last.toString())\\n      })\\n      .onScrollBarUpdate((index: number, offset: number) => {\\n        console.info(\"XXX\" + 'Grid onScrollBarUpdate,index : ' + index.toString() + \",offset\" + offset.toString())\\n        return { totalOffset: (index / 5) * (80 + 10) - offset, totalLength: 80 * 5 + 10 * 4 }\\n      })\\n      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {\\n        console.info(scrollOffset.toString())\\n        console.info(scrollState.toString())\\n      })\\n      .onScrollStart(() => {\\n        console.info(\"XXX\" + \"Grid onScrollStart\")\\n      })\\n      .onScrollStop(() => {\\n        console.info(\"XXX\" + \"Grid onScrollStop\")\\n      })\\n      .onReachStart(() => {\\n        this.gridPosition = 0\\n        console.info(\"XXX\" + \"Grid onReachStart\")\\n      })\\n      .onReachEnd(() => {\\n        this.gridPosition = 2\\n        console.info(\"XXX\" + \"Grid onReachEnd\")\\n      })\\n\\n      Button('next page')\\n        .onClick(() => { \\n          this.scroller.scrollPage({ next: true })\\n        })\\n    }.width('100%').margin({ top: 5 })\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用Grid组件和GridLayoutOptions中的onGetRectByIndex属性来实现固定行列的Grid布局，并自定义每个GridItem的位置和大小。\\n总体功能与效果描述：\\n示例包含两个Grid布局，第一个Grid布局使用默认的行列模板，第二个Grid布局使用自定义的onGetRectByIndex属性来指定每个GridItem的位置和大小。\\n*/\\n\\n// GridExample.ets\\n@Entry\\n@Component\\nstruct GridExample {\\n  @State numbers1: String[] = ['0', '1', '2', '3', '4']\\n  @State numbers2: String[] = ['0', '1', '2', '3', '4', '5']\\n\\n  // 定义GridLayoutOptions，使用onGetRectByIndex方法自定义每个GridItem的位置和大小\\n  layoutOptions3: GridLayoutOptions = {\\n    regularSize: [1, 1],\\n    onGetRectByIndex: (index: number) => {\\n      if (index == 0)\\n        return [0, 0, 1, 1] // 第一个GridItem的位置和大小\\n      else if (index == 1)\\n        return [0, 1, 2, 2] // 第二个GridItem的位置和大小\\n      else if (index == 2)\\n        return [0, 3, 3, 3] // 第三个GridItem的位置和大小\\n      else if (index == 3)\\n        return [3, 0, 3, 3] // 第四个GridItem的位置和大小\\n      else if (index == 4)\\n        return [4, 3, 2, 2] // 第五个GridItem的位置和大小\\n      else\\n        return [5, 5, 1, 1] // 第六个GridItem的位置和大小\\n    }\\n  }\\n\\n  build() {\\n    Column({ space: 5 }) {\\n      // 第一个Grid布局，使用默认的行列模板\\n      Grid() {\\n        ForEach(this.numbers1, (day: string) => {\\n          ForEach(this.numbers1, (day: string) => {\\n            GridItem() {\\n              Text(day)\\n                .fontSize(16)\\n                .backgroundColor(0xF9CF93)\\n                .width('100%')\\n                .height('100%')\\n                .textAlign(TextAlign.Center)\\n            }\\n          }, (day: string) => day)\\n        }, (day: string) => day)\\n      }\\n      .columnsTemplate('1fr 1fr 1fr 1fr 1fr') // 定义列模板\\n      .rowsTemplate('1fr 1fr 1fr 1fr 1fr') // 定义行模板\\n      .columnsGap(10) // 列间距\\n      .rowsGap(10) // 行间距\\n      .width('90%')\\n      .backgroundColor(0xFAEEE0)\\n      .height(300)\\n\\n      Text('GridLayoutOptions的使用：onGetRectByIndex。').fontColor(0xCCCCCC).fontSize(9).width('90%')\\n\\n      // 第二个Grid布局，使用自定义的GridLayoutOptions\\n      Grid(undefined, this.layoutOptions3) {\\n        ForEach(this.numbers2, (day: string) => {\\n          GridItem() {\\n            Text(day)\\n              .fontSize(16)\\n              .backgroundColor(0xF9CF93)\\n              .width('100%')\\n              .height(\"100%\")\\n              .textAlign(TextAlign.Center)\\n          }\\n          .height(\"100%\")\\n          .width('100%')\\n        }, (day: string) => day)\\n      }\\n      .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr') // 定义列模板\\n      .rowsTemplate('1fr 1fr 1fr 1fr 1fr 1fr') // 定义行模板\\n      .columnsGap(10) // 列间距\\n      .rowsGap(10) // 行间距\\n      .width('90%')\\n      .backgroundColor(0xFAEEE0)\\n      .height(300)\\n    }.width('100%').margin({ top: 5 })\\n  }\\n}",
            "/*\\n实现思路：\\n1. 创建一个包含多个组件的页面，包括头部、商品类型列表和数字列表。\\n2. 使用Grid和List组件来布局和展示数据。\\n3. 实现嵌套滚动功能，使得在滚动外部列表时，内部列表也能相应滚动。\\n4. 使用onScrollFrameBegin事件来控制滚动的细节，确保滚动效果平滑。\\n5. 提供一个按钮，用于快速返回页面顶部。\\n\\n总体功能与效果描述：\\n- 页面包含一个头部、商品类型列表和数字列表。\\n- 商品类型列表使用Grid组件展示，数字列表使用List组件展示。\\n- 实现嵌套滚动，外部列表滚动时，内部列表也能滚动。\\n- 使用onScrollFrameBegin事件处理滚动细节，确保滚动效果平滑。\\n- 提供一个按钮，点击后页面快速返回顶部。\\n*/\\n\\n// GridExample.ets\\n@Entry\\n@Component\\nstruct GridExample {\\n  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]\\n  @State numbers: number[] = []\\n  @State translateY: number = 0\\n  private scroller: Scroller = new Scroller()\\n  private gridScroller: Scroller = new Scroller()\\n  private touchDown: boolean = false\\n  private listTouchDown: boolean = false\\n  private scrolling: boolean = false\\n\\n  // 初始化数据，生成100个数字\\n  aboutToAppear() {\\n    for (let i = 0; i < 100; i++) {\\n      this.numbers.push(i)\\n    }\\n  }\\n\\n  build() {\\n    Stack() {\\n      Column() {\\n        Row() {\\n          Text('Head')\\n        }\\n\\n        Column() {\\n          List({ scroller: this.scroller }) {\\n            ListItem() {\\n              Grid() {\\n                GridItem() {\\n                  Text('GoodsTypeList1')\\n                }\\n                .backgroundColor(this.colors[0])\\n                .columnStart(0)\\n                .columnEnd(1)\\n\\n                GridItem() {\\n                  Text('GoodsTypeList2')\\n                }\\n                .backgroundColor(this.colors[1])\\n                .columnStart(0)\\n                .columnEnd(1)\\n\\n                GridItem() {\\n                  Text('GoodsTypeList3')\\n                }\\n                .backgroundColor(this.colors[2])\\n                .columnStart(0)\\n                .columnEnd(1)\\n\\n                GridItem() {\\n                  Text('GoodsTypeList4')\\n                }\\n                .backgroundColor(this.colors[3])\\n                .columnStart(0)\\n                .columnEnd(1)\\n\\n                GridItem() {\\n                  Text('GoodsTypeList5')\\n                }\\n                .backgroundColor(this.colors[4])\\n                .columnStart(0)\\n                .columnEnd(1)\\n              }\\n              .scrollBar(BarState.Off)\\n              .columnsGap(15)\\n              .rowsGap(10)\\n              .rowsTemplate('1fr 1fr 1fr 1fr 1fr')\\n              .columnsTemplate('1fr')\\n              .width('100%')\\n              .height(200)\\n            }\\n\\n            ListItem() {\\n              Grid(this.gridScroller) {\\n                ForEach(this.numbers, (item: number) => {\\n                  GridItem() {\\n                    Text(item + '')\\n                      .fontSize(16)\\n                      .backgroundColor(0xF9CF93)\\n                      .width('100%')\\n                      .height('100%')\\n                      .textAlign(TextAlign.Center)\\n                  }\\n                  .width('100%')\\n                  .height(40)\\n                  .shadow({ radius: 10, color: '#909399', offsetX: 1, offsetY: 1 })\\n                  .borderRadius(10)\\n                  .translate({ x: 0, y: this.translateY })\\n                }, (item: string) => item)\\n              }\\n              .columnsTemplate('1fr 1fr')\\n              .friction(0.3)\\n              .columnsGap(15)\\n              .rowsGap(10)\\n              .scrollBar(BarState.Off)\\n              .width('100%')\\n              .height('100%')\\n              .layoutDirection(GridDirection.Column)\\n              .nestedScroll({\\n                scrollForward: NestedScrollMode.PARENT_FIRST,\\n                scrollBackward: NestedScrollMode.SELF_FIRST\\n              })\\n              .onTouch((event: TouchEvent) => {\\n                if (event.type == TouchType.Down) {\\n                  this.listTouchDown = true\\n                } else if (event.type == TouchType.Up) {\\n                  this.listTouchDown = false\\n                }\\n              })\\n            }\\n          }\\n          .scrollBar(BarState.Off)\\n          .edgeEffect(EdgeEffect.None)\\n          .onTouch((event: TouchEvent) => {\\n            if (event.type == TouchType.Down) {\\n              this.touchDown = true\\n            } else if (event.type == TouchType.Up) {\\n              this.touchDown = false\\n            }\\n          })\\n          .onScrollFrameBegin((offset: number, state: ScrollState) => {\\n            if (this.scrolling && offset > 0) {\\n              let newOffset = this.scroller.currentOffset().yOffset\\n              if (newOffset >= 590) {\\n                this.gridScroller.scrollBy(0, offset)\\n                return { offsetRemain: 0 }\\n              } else if (newOffset + offset > 590) {\\n                this.gridScroller.scrollBy(0, newOffset + offset - 590)\\n                return { offsetRemain: 590 - newOffset }\\n              }\\n            }\\n            return { offsetRemain: offset }\\n          })\\n          .onScrollStart(() => {\\n            if (this.touchDown && !this.listTouchDown) {\\n              this.scrolling = true\\n            }\\n          })\\n          .onScrollStop(() => {\\n            this.scrolling = false\\n          })\\n        }\\n        .width('100%')\\n        .height('100%')\\n        .padding({ left: 10, right: 10 })\\n      }\\n\\n      Row() {\\n        Text('Top')\\n          .width(30)\\n          .height(30)\\n          .borderRadius(50)\\n      }\\n      .padding(5)\\n      .borderRadius(50)\\n      .backgroundColor('#ffffff')\\n      .shadow({ radius: 10, color: '#909399', offsetX: 1, offsetY: 1 })\\n      .margin({ right: 22, bottom: 15 })\\n      .onClick(() => {\\n        this.scroller.scrollTo({ xOffset: 0, yOffset: 0 })\\n        this.gridScroller.scrollTo({ xOffset: 0, yOffset: 0 })\\n      })\\n    }\\n    .align(Alignment.BottomEnd)\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "GridItem": {
        "description": "网格容器中单项内容容器，仅支持作为Grid组件的子组件使用。",
        "details": None,
        "interfaces": [
            {
                "description": "GridItem(value?: GridItemOptions)",
                "params": {
                    "value": {
                        "type": "GridItemOptions",
                        "required": False,
                        "description": "可选参数，用于设置GridItem的选项。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "rowStart": {
                "description": "设置当前元素起始行号。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "当前元素起始行号。",
                        "default": None
                    }
                }
            },
            "rowEnd": {
                "description": "设置当前元素终点行号。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "当前元素终点行号。",
                        "default": None
                    }
                }
            },
            "columnStart": {
                "description": "设置当前元素起始列号。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "当前元素起始列号。",
                        "default": None
                    }
                }
            },
            "columnEnd": {
                "description": "设置当前元素终点列号。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "当前元素终点列号。",
                        "default": None
                    }
                }
            },
            "selectable": {
                "description": "设置当前GridItem元素是否可以被鼠标框选。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "当前GridItem元素是否可以被鼠标框选。",
                        "default": True
                    }
                }
            },
            "selected": {
                "description": "设置当前GridItem选中状态。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "当前GridItem选中状态。",
                        "default": False
                    }
                }
            }
        },
        "events": {
            "onSelect": {
                "description": "GridItem元素被鼠标框选的状态改变时触发回调。",
                "params": {
                    "isSelected": {
                        "type": "boolean",
                        "required": True,
                        "description": "进入鼠标框选范围即被选中返回true，移出鼠标框选范围即未被选中返回false。",
                        "default": None
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何使用Grid和GridItem组件来创建一个网格布局，并在网格中动态显示文本内容。通过设置不同的行列起始和结束位置，可以控制GridItem在网格中的具体位置。\\n\\n总体功能与效果描述：\\n该示例创建了一个5x5的网格布局，其中包含静态和动态的GridItem。静态GridItem显示固定的文本内容，而动态GridItem则根据数组中的数据动态生成。每个GridItem中的文本内容居中显示，并具有不同的背景颜色。\\n*/\\n\\n// GridItemExample.ets\\n@Entry\\n@Component\\nstruct GridItemExample {\\n  @State numbers: string[] = [\"0\", \"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\", \"11\", \"12\", \"13\", \"14\", \"15\"]\\n\\n  build() {\\n    Column() {\\n      Grid() {\\n        // 静态GridItem，显示文本'4'，位于第1行第1列\\n        GridItem() {\\n          Text('4')\\n            .fontSize(16)\\n            .backgroundColor(0xFAEEE0)\\n            .width('100%')\\n            .height('100%')\\n            .textAlign(TextAlign.Center)\\n        }.rowStart(1).rowEnd(2).columnStart(1).columnEnd(2)\\n\\n        // 动态GridItem，根据numbers数组动态生成\\n        ForEach(this.numbers, (item: string) => {\\n          GridItem() {\\n            Text(item)\\n              .fontSize(16)\\n              .backgroundColor(0xF9CF93)\\n              .width('100%')\\n              .height('100%')\\n              .textAlign(TextAlign.Center)\\n          }\\n        }, (item: string) => item)\\n\\n        // 静态GridItem，显示文本'5'，占据第1列到第4列\\n        GridItem() {\\n          Text('5')\\n            .fontSize(16)\\n            .backgroundColor(0xDBD0C0)\\n            .width('100%')\\n            .height('100%')\\n            .textAlign(TextAlign.Center)\\n        }.columnStart(1).columnEnd(4)\\n      }\\n      .columnsTemplate('1fr 1fr 1fr 1fr 1fr') // 设置5列，每列宽度相等\\n      .rowsTemplate('1fr 1fr 1fr 1fr 1fr') // 设置5行，每行高度相等\\n      .width('90%').height(300) // 设置网格的宽度和高度\\n      .width('100%').margin({ top: 5 }) // 设置外层Column的宽度和上边距\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用Grid组件和GridItem组件来创建一个网格布局，并通过不同的GridItemStyle来设置不同的网格项样式。\\n总体功能与效果描述：\\n示例中包含两个Grid组件，每个Grid组件内部嵌套了两个ForEach循环来生成网格项。每个网格项包含一个Text组件，用于显示数字。通过设置不同的GridItemStyle，可以观察到网格项的不同样式效果。\\n*/\\n\\n// GridItemExample.ets\\n@Entry\\n@Component\\nstruct GridItemExample {\\n  @State numbers: String[] = ['0', '1', '2']\\n\\n  build() {\\n    Column({ space: 5 }) {\\n      // 第一个Grid组件，使用GridItemStyle.NONE\\n      Grid() {\\n        ForEach(this.numbers, (day: string) => {\\n          ForEach(this.numbers, (day: string) => {\\n            GridItem({style:GridItemStyle.NONE}) {\\n              Text(day)\\n                .fontSize(16)\\n                .width('100%')\\n                .height('100%')\\n                .textAlign(TextAlign.Center)\\n                .focusable(true)\\n              // 设置文本内容、字体大小、宽度、高度、对齐方式和可聚焦性\\n            }\\n            .backgroundColor(0xF9CF93)\\n            // 设置网格项的背景颜色\\n          }, (day: string) => day)\\n        }, (day: string) => day)\\n      }\\n      .columnsTemplate('1fr 1fr 1fr')\\n      // 设置列模板，每列宽度相等\\n      .rowsTemplate('1fr 1fr')\\n      // 设置行模板，每行高度相等\\n      .columnsGap(4)\\n      // 设置列间距\\n      .rowsGap(4)\\n      // 设置行间距\\n      .width('60%')\\n      // 设置Grid组件的宽度\\n      .backgroundColor(0xFAEEE0)\\n      // 设置Grid组件的背景颜色\\n      .height(150)\\n      // 设置Grid组件的高度\\n      .padding('4vp')\\n      // 设置Grid组件的内边距\\n\\n      // 第二个Grid组件，使用GridItemStyle.PLAIN\\n      Grid() {\\n        ForEach(this.numbers, (day: string) => {\\n          ForEach(this.numbers, (day: string) => {\\n            GridItem({style:GridItemStyle.PLAIN}) {\\n              Text(day)\\n                .fontSize(16)\\n                .width('100%')\\n                .height('100%')\\n                .textAlign(TextAlign.Center)\\n                .focusable(true)\\n              // 设置文本内容、字体大小、宽度、高度、对齐方式和可聚焦性\\n            }\\n            .backgroundColor(0xF9CF93)\\n            // 设置网格项的背景颜色\\n          }, (day: string) => day)\\n        }, (day: string) => day)\\n      }\\n      .columnsTemplate('1fr 1fr 1fr')\\n      // 设置列模板，每列宽度相等\\n      .rowsTemplate('1fr 1fr')\\n      // 设置行模板，每行高度相等\\n      .columnsGap(4)\\n      // 设置列间距\\n      .rowsGap(4)\\n      // 设置行间距\\n      .width('60%')\\n      // 设置Grid组件的宽度\\n      .backgroundColor(0xFAEEE0)\\n      // 设置Grid组件的背景颜色\\n      .height(150)\\n      // 设置Grid组件的高度\\n      .padding('4vp')\\n      // 设置Grid组件的内边距\\n    }.width('100%').margin({ top: 5 })\\n    // 设置Column组件的宽度和上边距\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "Hyperlink": {"description": "超链接组件，组件宽高范围内点击实现跳转，可以包含Image子组件。"},
    "List": {
        "description": "列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。可以包含ListItem、ListItemGroup子组件，支持渲染控制类型（if/else、ForEach、LazyForEach和Repeat）。",
        "details": None,
        "interfaces": [
            {
                "description": "List(value?:{space?: number | string, initialIndex?: number, scroller?: Scroller})",
                "params": {
                    "space": {
                        "type": [
                            "number",
                            "string"
                        ],
                        "required": False,
                        "description": "子组件主轴方向的间隔。默认值：0。参数类型为number时单位为vp。设置为负数或者大于等于List内容区长度时，按默认值显示。space参数值小于List分割线宽度时，子组件主轴方向的间隔取分割线宽度。",
                        "default": None
                    },
                    "initialIndex": {
                        "type": "number",
                        "required": False,
                        "description": "设置当前List初次加载时视口起始位置显示的item的索引值。默认值：0。设置为负数或超过了当前List最后一个item的索引值时视为无效取值，无效取值按默认值显示。",
                        "default": None
                    },
                    "scroller": {
                        "type": "Scroller",
                        "required": False,
                        "description": "可滚动组件的控制器。用于与可滚动组件进行绑定。不允许和其他滚动类组件绑定同一个滚动控制对象。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "listDirection": {
                "description": "设置List组件排列方向。",
                "params": {
                    "value": {
                        "type": "Axis",
                        "required": True,
                        "description": "组件的排列方向。默认值：Axis.Vertical",
                        "default": None
                    }
                }
            },
            "divider": {
                "description": "设置ListItem分割线样式，默认无分割线。",
                "params": {
                    "value": {
                        "type": {
                            "strokeWidth": "Length",
                            "color": "ResourceColor",
                            "startMargin": "Length",
                            "endMargin": "Length"
                        },
                        "required": True,
                        "description": "ListItem分割线样式。strokeWidth: 分割线的线宽。color: 分割线的颜色。默认值：0x08000000。startMargin: 分割线与列表侧边起始端的距离。默认值：0，单位：vp。endMargin: 分割线与列表侧边结束端的距离。默认值：0，单位：vp。",
                        "default": None
                    }
                }
            },
            "scrollBar": {
                "description": "设置滚动条状态。",
                "params": {
                    "value": {
                        "type": "BarState",
                        "required": True,
                        "description": "滚动条状态。默认值：BarState.Auto",
                        "default": None
                    }
                }
            },
            "cachedCount": {
                "description": "设置列表中ListItem/ListItemGroup的预加载数量，懒加载场景只会预加载List显示区域外cachedCount的内容，非懒加载场景会全部加载。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "ListItem/ListItemGroup的预加载数量。默认值：1",
                        "default": None
                    }
                }
            },
            "editMode": {
                "description": "设置当前List组件是否处于可编辑模式。从API version9开始废弃不再使用，无替代接口。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "当前List组件是否处于可编辑模式。默认值：false",
                        "default": None
                    }
                }
            },
            "edgeEffect": {
                "description": "设置边缘滑动效果。",
                "params": {
                    "value": {
                        "type": "EdgeEffect",
                        "required": True,
                        "description": "List组件的边缘滑动效果，支持弹簧效果和阴影效果。默认值：EdgeEffect.Spring",
                        "default": None
                    },
                    "options": {
                        "type": {
                            "alwaysEnabled": "boolean"
                        },
                        "required": False,
                        "description": "组件内容大小小于组件自身时，是否开启滑动效果。默认值：{ alwaysEnabled: false }",
                        "default": None
                    }
                }
            },
            "chainAnimation": {
                "description": "设置当前List是否启用链式联动动效，开启后列表滑动以及顶部和底部拖拽时会有链式联动的效果。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否启用链式联动动效。默认值：false，不启用链式联动。true，启用链式联动。",
                        "default": None
                    }
                }
            },
            "multiSelectable": {
                "description": "设置是否开启鼠标框选。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否开启鼠标框选。默认值：false，关闭框选。true，开启框选。",
                        "default": None
                    }
                }
            },
            "lanes": {
                "description": "设置List组件的布局列数或行数。gutter为列间距，当列数大于1时生效。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            {
                                "minLength": "number",
                                "maxLength": "number"
                            }
                        ],
                        "required": True,
                        "description": "List组件的布局列数或行数。",
                        "default": None
                    },
                    "gutter": {
                        "type": "Dimension",
                        "required": False,
                        "description": "列间距。",
                        "default": None
                    }
                }
            },
            "alignListItem": {
                "description": "设置List交叉轴方向宽度大于ListItem交叉轴宽度 * lanes时，ListItem在List交叉轴方向的布局方式。",
                "params": {
                    "value": {
                        "type": "ListItemAlign",
                        "required": True,
                        "description": "交叉轴方向的布局方式。默认值：ListItemAlign.Start",
                        "default": None
                    }
                }
            },
            "sticky": {
                "description": "配合ListItemGroup组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底。sticky属性可以设置为 StickyStyle.Header | StickyStyle.Footer 以同时支持header吸顶和footer吸底。",
                "params": {
                    "value": {
                        "type": "StickyStyle",
                        "required": True,
                        "description": "ListItemGroup吸顶或吸底效果。默认值：StickyStyle.None",
                        "default": None
                    }
                }
            },
            "scrollSnapAlign": {
                "description": "设置列表项滚动结束对齐效果。只支持ListItem等高情况下，设置列表项滚动结束对齐效果。触控板和鼠标滑动List结束后不支持对齐效果。",
                "params": {
                    "value": {
                        "type": "ScrollSnapAlign",
                        "required": True,
                        "description": "列表项滚动结束对齐效果。",
                        "default": None
                    }
                }
            },
            "enableScrollInteraction": {
                "description": "设置是否支持滚动手势，当设置为false时，无法通过手指或者鼠标滚动，但不影响控制器的滚动接口。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否支持滚动手势。默认值：true",
                        "default": None
                    }
                }
            },
            "nestedScroll": {
                "description": "设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。",
                "params": {
                    "value": {
                        "type": {
                            "forward": "NestedScrollOptions",
                            "backward": "NestedScrollOptions"
                        },
                        "required": True,
                        "description": "向前向后两个方向上的嵌套滚动模式。",
                        "default": None
                    }
                }
            },
            "friction": {
                "description": "设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。设置为小于等于0的值时，按默认值处理。",
                "params": {
                    "value": {
                        "type": [
                            "number",
                            "Resource"
                        ],
                        "required": True,
                        "description": "摩擦系数。默认值：非可穿戴设备为0.75，可穿戴设备为0.9。",
                        "default": None
                    }
                }
            },
            "contentStartOffset": {
                "description": "设置内容区域起始偏移量。列表滚动到起始位置时，列表内容与列表显示区域边界保留指定距离。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "内容区域起始偏移量。默认值：0。单位：vp",
                        "default": None
                    }
                }
            },
            "contentEndOffset": {
                "description": "设置内容区末尾偏移量。列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "内容区末尾偏移量。默认值：0。单位：vp",
                        "default": None
                    }
                }
            },
            "childrenMainSize": {
                "description": "设置List组件的子组件在主轴方向的大小信息。",
                "params": {
                    "value": {
                        "type": "ChildrenMainSize",
                        "required": True,
                        "description": "通过ChildrenMainSize对象向List组件准确提供所有子组件在主轴方向的大小信息，能够使List组件在子组件的主轴大小不一致、增删子组件、使用scrollToIndex等场景也能维护自己准确的滑动位置，进而使scrollTo能跳转到准确的指定位置，currentOffset能够获取到当前准确的滑动位置，内置滚动条能够平滑移动无跳变。",
                        "default": None
                    }
                }
            }
        },
        "events": {
            "onItemDelete": {
                "description": "当List组件在编辑模式时，点击ListItem右边出现的删除按钮时触发。从API version9开始废弃不再使用，无替代接口。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "被删除的列表项的索引值。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onScrollIndex": {
                "description": "有子组件划入或划出List显示区域时触发。计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。",
                "params": {
                    "start": {
                        "type": "number",
                        "required": True,
                        "description": "List显示区域内第一个子组件的索引值",
                        "default": None
                    },
                    "end": {
                        "type": "number",
                        "required": True,
                        "description": "List显示区域内最后一个子组件的索引值。",
                        "default": None
                    },
                    "center": {
                        "type": "number",
                        "required": True,
                        "description": "List显示区域内中间位置子组件的索引值。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onReachStart": {
                "description": "列表到达起始位置时触发。",
                "params": {},
                "returns": None
            },
            "onReachEnd": {
                "description": "列表到底末尾位置时触发。",
                "params": {},
                "returns": None
            },
            "onScrollFrameBegin": {
                "description": "列表开始滑动时触发，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，列表将按照返回值的实际滑动量进行滑动。",
                "params": {
                    "offset": {
                        "type": "number",
                        "required": True,
                        "description": "即将发生的滑动量，单位vp。",
                        "default": None
                    },
                    "state": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滑动状态。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onScrollStart": {
                "description": "列表滑动开始时触发。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用Scroller滑动控制器触发的带动画的滑动，动画开始时会触发该事件",
                "params": {},
                "returns": None
            },
            "onScrollStop": {
                "description": "列表滑动停止时触发。手拖动列表或列表的滚动条触发的滑动，手离开屏幕并且滑动停止时会触发该事件。使用Scroller滑动控制器触发的带动画的滑动，动画停止会触发该事件。",
                "params": {},
                "returns": None
            },
            "onItemMove": {
                "description": "列表元素发生移动时触发。",
                "params": {
                    "from": {
                        "type": "number",
                        "required": True,
                        "description": "移动前索引值。",
                        "default": None
                    },
                    "to": {
                        "type": "number",
                        "required": True,
                        "description": "移动后索引值。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDragStart": {
                "description": "开始拖拽列表元素时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    },
                    "itemIndex": {
                        "type": "number",
                        "required": True,
                        "description": "被拖拽列表元素索引值。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDragEnter": {
                "description": "拖拽进入列表元素范围内时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDragMove": {
                "description": "拖拽在列表元素范围内移动时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    },
                    "itemIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽起始位置。",
                        "default": None
                    },
                    "insertIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽插入位置。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDragLeave": {
                "description": "拖拽离开列表元素时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    },
                    "itemIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽离开的列表元素索引值。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onItemDrop": {
                "description": "绑定该事件的列表元素可作为拖拽释放目标，当在列表元素内停止拖拽时触发。",
                "params": {
                    "event": {
                        "type": "ItemDragInfo",
                        "required": True,
                        "description": "拖拽点的信息。",
                        "default": None
                    },
                    "itemIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽起始位置。",
                        "default": None
                    },
                    "insertIndex": {
                        "type": "number",
                        "required": True,
                        "description": "拖拽插入位置。",
                        "default": None
                    },
                    "isSuccess": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否成功释放",
                        "default": None
                    }
                },
                "returns": None
            },
            "onScroll": {
                "description": "列表滑动时触发。从API version 12开始废弃不再使用，推荐使用onDidScroll事件替代。",
                "params": {
                    "scrollOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动的偏移量，List的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。",
                        "default": None
                    },
                    "scrollState": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滑动状态。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onWillScroll": {
                "description": "列表滑动前触发。回调当前帧将要滑动的偏移量，当前滑动状态和滑动操作来源，其中回调的偏移量为计算得到的将要滑动的偏移量值，并非最终实际滑动偏移。可以通过该回调返回值指定列表将要滑动的偏移。",
                "params": {
                    "handler": {
                        "type": "OnWillScrollCallback",
                        "required": True,
                        "description": "列表滑动前触发的回调函数。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onDidScroll": {
                "description": "列表滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。",
                "params": {
                    "handler": {
                        "type": "OnScrollCallback",
                        "required": True,
                        "description": "列表滑动时触发的回调函数。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onScrollVisibleContentChange": {
                "description": "有子组件划入或划出List显示区域时触发。计算触发条件时，每一个ListItem/ListItemGroup中的header/ListItemGroup中的footer都算一个子组件。",
                "params": {
                    "handler": {
                        "type": "OnScrollVisibleContentChangeCallback",
                        "required": True,
                        "description": "有子组件划入或划出List显示区域时触发的回调函数。",
                        "default": None
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例通过使用鸿蒙ArkUI框架中的List组件和相关事件回调，实现了一个纵向滚动的列表。列表中的每一项是一个简单的文本显示，同时监听了列表的滚动事件，并在控制台输出相关索引信息。\\n\\n总体功能与效果描述：\\n1. 创建一个包含数字的数组，并将其显示为纵向列表。\\n2. 列表项之间有20像素的间距，初始显示第一个列表项。\\n3. 列表的滚动条被隐藏，滚动摩擦系数为0.6。\\n4. 列表项之间有分隔线，分隔线的颜色和宽度可配置。\\n5. 当列表滚动时，会触发滚动索引回调，输出当前显示的第一个和最后一个列表项的索引。\\n6. 当列表可见内容发生变化时，输出可见内容的起始和结束信息。\\n7. 当列表实际滚动时，输出滚动偏移量和滚动状态。\\n*/\\n\\n// ListExample.ets\\n@Entry\\n@Component\\nstruct ListExample {\\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] // 定义一个包含数字的数组\\n\\n  build() {\\n    Column() {\\n      List({ space: 20, initialIndex: 0 }) { // 创建一个列表，设置项间距为20，初始显示第一个项\\n        ForEach(this.arr, (item: number) => { // 遍历数组，生成列表项\\n          ListItem() {\\n            Text('' + item) // 显示数组中的数字\\n              .width('100%').height(100).fontSize(16) // 设置文本的宽度、高度和字体大小\\n              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF) // 设置文本居中对齐、圆角和背景颜色\\n          }\\n        }, (item: string) => item) // 定义列表项的唯一键\\n      }\\n      .listDirection(Axis.Vertical) // 设置列表为纵向滚动\\n      .scrollBar(BarState.Off) // 隐藏滚动条\\n      .friction(0.6) // 设置滚动摩擦系数\\n      .divider({ strokeWidth: 2, color: 0xFFFFFF, startMargin: 20, endMargin: 20 }) // 设置列表项之间的分隔线\\n      .edgeEffect(EdgeEffect.Spring) // 设置边缘效果为弹性效果\\n      .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => { // 监听滚动索引变化\\n        console.info('first' + firstIndex) // 输出第一个可见项的索引\\n        console.info('last' + lastIndex) // 输出最后一个可见项的索引\\n        console.info('center' + centerIndex) // 输出中间可见项的索引\\n      })\\n      .onScrollVisibleContentChange((start: VisibleListContentInfo, end: VisibleListContentInfo) => { // 监听可见内容变化\\n        console.log(' start index: ' + start.index + // 输出起始可见内容的索引\\n                    ' start item group area: ' + start.itemGroupArea + // 输出起始可见内容的项目组区域\\n                    ' start index in group: ' + start.itemIndexInGroup) // 输出起始可见内容在组中的索引\\n        console.log(' end index: ' + end.index + // 输出结束可见内容的索引\\n                    ' end item group area: ' + end.itemGroupArea + // 输出结束可见内容的项目组区域\\n                    ' end index in group: ' + end.itemIndexInGroup) // 输出结束可见内容在组中的索引\\n      })\\n      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => { // 监听实际滚动事件\\n        console.info(`onScroll scrollState = ScrollState` + scrollState + `, scrollOffset = ` + scrollOffset) // 输出滚动状态和滚动偏移量\\n      })\\n      .width('90%') // 设置列表宽度为父容器的90%\\n    }\\n    .width('100%') // 设置列的宽度为父容器的100%\\n    .height('100%') // 设置列的高度为父容器的100%\\n    .backgroundColor(0xDCDCDC) // 设置背景颜色\\n    .padding({ top: 5 }) // 设置顶部内边距\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用List组件和ListItem组件来创建一个可滚动的列表，并动态改变列表项的对齐方式。通过点击按钮，可以循环切换列表项的对齐方式（Start、Center、End）。\\n\\n总体功能与效果描述：\\n1. 创建一个包含20个项目的列表，每个项目显示一个数字。\\n2. 列表项具有固定的宽度和高度，并带有边框和背景色。\\n3. 列表具有固定的宽度和高度，并带有边框和滚动条。\\n4. 通过点击按钮，可以切换列表项的对齐方式。\\n*/\\n\\n// ListLanesExample.ets\\n@Entry\\n@Component\\nstruct ListLanesExample {\\n  @State arr: string[] = [\"0\", \"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\", \"11\", \"12\", \"13\", \"14\", \"15\", \"16\", \"17\", \"18\", \"19\"]\\n  @State alignListItem: ListItemAlign = ListItemAlign.Start\\n\\n  build() {\\n    Column() {\\n      List({ space: 20, initialIndex: 0 }) {\\n        ForEach(this.arr, (item: string) => {\\n          ListItem() {\\n            Text('' + item)\\n              .width('100%') // 设置文本宽度为100%\\n              .height(100) // 设置文本高度为100\\n              .fontSize(16) // 设置字体大小为16\\n              .textAlign(TextAlign.Center) // 设置文本居中对齐\\n              .borderRadius(10) // 设置边框圆角\\n              .backgroundColor(0xFFFFFF) // 设置背景颜色为白色\\n          }\\n          .border({ width: 2, color: Color.Green }) // 设置列表项的边框\\n        }, (item: string) => item)\\n      }\\n      .height(300) // 设置列表高度为300\\n      .width(\"90%\") // 设置列表宽度为90%\\n      .friction(0.6) // 设置列表的摩擦系数\\n      .border({ width: 3, color: Color.Red }) // 设置列表的边框\\n      .lanes({ minLength: 40, maxLength: 40 }) // 设置列表的行数\\n      .alignListItem(this.alignListItem) // 设置列表项的对齐方式\\n      .scrollBar(BarState.Off) // 关闭滚动条\\n\\n      Button(\"点击更改alignListItem:\" + this.alignListItem).onClick(() => {\\n        if (this.alignListItem == ListItemAlign.Start) {\\n          this.alignListItem = ListItemAlign.Center // 切换到中心对齐\\n        } else if (this.alignListItem == ListItemAlign.Center) {\\n          this.alignListItem = ListItemAlign.End // 切换到尾部对齐\\n        } else {\\n          this.alignListItem = ListItemAlign.Start // 切换到头部对齐\\n        }\\n      })\\n    }\\n    .width('100%') // 设置列的宽度为100%\\n    .height('100%') // 设置列的高度为100%\\n    .backgroundColor(0xDCDCDC) // 设置背景颜色为灰色\\n    .padding({ top: 5 }) // 设置顶部内边距\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中创建一个可编辑的列表组件。列表中的每个项包含一个文本和一个删除按钮。通过点击“edit list”按钮，用户可以切换编辑模式，从而显示或隐藏删除按钮。点击删除按钮可以移除对应的列表项。\\n\\n总体功能与效果描述：\\n1. 显示一个包含数字的列表。\\n2. 提供一个按钮来切换编辑模式。\\n3. 在编辑模式下，每个列表项旁边显示一个删除按钮。\\n4. 点击删除按钮可以移除对应的列表项。\\n*/\\n\\n// ListExample.ets\\n@Entry\\n@Component\\nstruct ListExample {\\n  @State arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] // 初始化列表数据\\n  @State editFlag: boolean = false // 控制编辑模式的标志\\n\\n  build() {\\n    Stack({ alignContent: Alignment.TopStart }) {\\n      Column() {\\n        List({ space: 20, initialIndex: 0 }) {\\n          ForEach(this.arr, (item: number, index?: number) => {\\n            ListItem() {\\n              Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {\\n                Text('' + item) // 显示列表项的文本\\n                  .width('100%')\\n                  .height(80)\\n                  .fontSize(20)\\n                  .textAlign(TextAlign.Center)\\n                  .borderRadius(10)\\n                  .backgroundColor(0xFFFFFF)\\n                  .flexShrink(1)\\n                if (this.editFlag) {\\n                  Button() {\\n                    Text(\"delete\").fontSize(16) // 显示删除按钮的文本\\n                  }.width('30%').height(40)\\n                  .onClick(() => {\\n                    if (index != undefined) {\\n                      console.info(this.arr[index] + 'Delete') // 打印删除信息\\n                      this.arr.splice(index, 1) // 移除对应的列表项\\n                      console.info(JSON.stringify(this.arr)) // 打印更新后的列表数据\\n                      this.editFlag = false // 退出编辑模式\\n                    }\\n                  }).stateEffect(true) // 启用按钮的状态效果\\n                }\\n              }\\n            }\\n          }, (item: string) => item) // 使用item作为唯一键\\n        }.width('90%')\\n        .scrollBar(BarState.Off) // 禁用滚动条\\n        .friction(0.6) // 设置列表的摩擦系数\\n      }.width('100%')\\n\\n      Button('edit list') // 显示编辑列表按钮\\n        .onClick(() => {\\n          this.editFlag = !this.editFlag // 切换编辑模式\\n        }).margin({ top: 5, left: 20 })\\n    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中创建一个水平滚动的列表组件。通过使用List组件和ForEach循环，动态生成列表项，并设置列表的滚动效果和样式。\\n\\n总体功能与效果描述：\\n该组件在页面加载时生成一个包含20个数字的水平滚动列表。列表项具有圆角边框和居中对齐的文本，列表本身具有弹性边缘效果和居中对齐的滚动吸附效果。\\n*/\\n\\n// ListExample.ets\\n@Entry\\n@Component\\nstruct ListExample {\\n  // 定义一个数组用于存储列表数据\\n  private arr: number[] = [];\\n  // 定义一个Scroller对象用于控制列表的滚动\\n  private scrollerForList: Scroller = new Scroller();\\n\\n  // 组件即将显示时，初始化数组数据\\n  aboutToAppear() {\\n    for (let i = 0; i < 20; i++) {\\n      this.arr.push(i); // 向数组中添加数字\\n    }\\n  }\\n\\n  build() {\\n    Column() {\\n      Row() {\\n        List({ space: 20, initialIndex: 3, scroller: this.scrollerForList }) {\\n          // 使用ForEach循环生成列表项\\n          ForEach(this.arr, (item: number) => {\\n            ListItem() {\\n              Text('' + item) // 显示列表项的文本\\n                .width('100%').height(100).fontSize(16)\\n                .textAlign(TextAlign.Center) // 文本居中对齐\\n            }\\n            .borderRadius(10).backgroundColor(0xFFFFFF) // 设置列表项的圆角边框和背景色\\n            .width('60%')\\n            .height('80%')\\n          }, (item: number) => JSON.stringify(item)) // 使用JSON.stringify作为键值生成器\\n        }\\n        .chainAnimation(true) // 启用列表项的链式动画\\n        .edgeEffect(EdgeEffect.Spring) // 设置列表的弹性边缘效果\\n        .listDirection(Axis.Horizontal) // 设置列表为水平方向\\n        .height('100%')\\n        .width('100%')\\n        .scrollSnapAlign(ScrollSnapAlign.CENTER) // 设置滚动吸附效果为居中对齐\\n        .borderRadius(10) // 设置列表的圆角边框\\n        .backgroundColor(0xDCDCDC) // 设置列表的背景色\\n      }\\n      .width('100%')\\n      .height('100%')\\n      .backgroundColor(0xDCDCDC) // 设置容器的背景色\\n      .padding({ top: 10 }) // 设置容器的顶部内边距\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用List组件，并通过设置childrenMainSize属性来确保在子组件高度不一致时，调用scrollTo接口也能准确跳转到指定位置。示例中还包含了动态调整子组件尺寸和滚动到指定位置的功能。\\n\\n总体功能与效果描述：\\n1. 创建一个包含不同高度的子组件的List。\\n2. 通过按钮动态调整子组件的默认尺寸。\\n3. 通过按钮调用scrollTo接口，实现滚动到指定位置。\\n*/\\n\\n// ListExample.ets\\n@Entry\\n@Component\\nstruct ListExample {\\n  // 定义一个数组用于存储列表项的索引\\n  private arr: number[] = []\\n  // 创建一个ListScroller实例，用于滚动操作\\n  private scroller: ListScroller = new ListScroller()\\n  // 定义列表项之间的间距\\n  @State listSpace: number = 10\\n  // 定义子组件的主尺寸，初始值为100\\n  @State listChildrenSize: ChildrenMainSize = new ChildrenMainSize(100)\\n\\n  // 组件初始化时执行的操作\\n  aboutToAppear() {\\n    // 填充数组，包含0到9的数字\\n    for (let i = 0; i < 10; i++) {\\n      this.arr.push(i)\\n    }\\n    // 设置前5个子组件的高度为300\\n    this.listChildrenSize.splice(0, 5, [300, 300, 300, 300, 300])\\n  }\\n\\n  build() {\\n    Column() {\\n      // 创建一个List组件，设置间距、初始索引和滚动控制器\\n      List({ space: this.listSpace, initialIndex: 4, scroller: this.scroller }) {\\n        // 使用ForEach循环生成列表项\\n        ForEach(this.arr, (item: number) => {\\n          ListItem() {\\n            // 创建文本组件，显示列表项的索引\\n            Text('item-' + item)\\n              .height(item < 5 ? 300 : this.listChildrenSize.childDefaultSize) // 设置高度，前5项为300，其余为默认尺寸\\n              .width('90%') // 设置宽度\\n              .fontSize(16) // 设置字体大小\\n              .textAlign(TextAlign.Center) // 设置文本对齐方式\\n              .borderRadius(10) // 设置边框圆角\\n              .backgroundColor(0xFFFFFF) // 设置背景颜色\\n          }\\n        }, (item: string) => item) // 指定键值生成函数\\n      }\\n      .backgroundColor(Color.Gray) // 设置列表背景颜色\\n      .layoutWeight(1) // 设置布局权重\\n      .scrollBar(BarState.On) // 显示滚动条\\n      .childrenMainSize(this.listChildrenSize) // 设置子组件的主尺寸\\n      .alignListItem(ListItemAlign.Center) // 设置列表项对齐方式\\n\\n      // 创建一行按钮，用于调整子组件尺寸和滚动到指定位置\\n      Row() {\\n        Button() { Text('item size + 50') }\\n          .onClick(() => {\\n            this.listChildrenSize.childDefaultSize += 50 // 增加子组件默认尺寸\\n          })\\n          .height('50%') // 设置按钮高度\\n          .width('30%') // 设置按钮宽度\\n        Button() { Text('item size - 50') }\\n          .onClick(() => {\\n            if (this.listChildrenSize.childDefaultSize === 0) {\\n              return // 如果默认尺寸为0，则不执行减小操作\\n            }\\n            this.listChildrenSize.childDefaultSize -= 50 // 减小子组件默认尺寸\\n          })\\n          .height('50%') // 设置按钮高度\\n          .width('30%') // 设置按钮宽度\\n        Button() { Text('scrollTo (0, 310)') }\\n          .onClick(() => {\\n            this.scroller.scrollTo({ xOffset: 0, yOffset: 310 }) // 滚动到指定位置\\n          })\\n          .height('50%') // 设置按钮高度\\n          .width('30%') // 设置按钮宽度\\n      }\\n      .height('20%') // 设置行的高度\\n    }\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "ListItem": {
        "description": "用来展示列表具体item，必须配合List来使用。",
        "details": "该组件从API Version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。该组件的父组件只能是List或者ListItemGroup。当ListItem配合LazyForEach使用时，ListItem子组件在ListItem创建时创建。配合if/else、ForEach使用时，或父组件为List/ListItemGroup时，ListItem子组件在ListItem布局时创建。",
        "interfaces": [
            {
                "description": "ListItem(value?: ListItemOptions)",
                "params": {
                    "value": {
                        "type": "ListItemOptions",
                        "required": False,
                        "description": "为ListItem提供可选参数, 该对象内含有ListItemStyle枚举类型的style参数。",
                        "default": None
                    }
                }
            },
            {
                "description": "ListItem(value?: string)",
                "params": {
                    "value": {
                        "type": "string",
                        "required": False,
                        "description": "无",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "selectable": {
                "description": "设置当前ListItem元素是否可以被鼠标框选。外层List容器的鼠标框选开启时，ListItem的框选才生效。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "ListItem元素是否可以被鼠标框选。",
                        "default": True
                    }
                }
            },
            "selected": {
                "description": "设置当前ListItem选中状态。该属性支持$$双向绑定变量。该属性需要在设置选中态样式前使用才能生效选中态样式。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "当前ListItem选中状态。",
                        "default": False
                    }
                }
            },
            "swipeAction": {
                "description": "用于设置ListItem的划出组件。",
                "params": {
                    "value": {
                        "type": "SwipeActionOptions",
                        "required": True,
                        "description": "ListItem的划出组件选项。",
                        "default": None
                    }
                }
            }
        },
        "events": {
            "onSelect": {
                "description": "ListItem元素被鼠标框选的状态改变时触发回调。",
                "params": {
                    "isSelected": {
                        "type": "boolean",
                        "required": True,
                        "description": "进入鼠标框选范围即被选中返回true， 移出鼠标框选范围即未被选中返回false。",
                        "default": None
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用List组件和ListItem组件来创建一个具有不同样式的列表项。通过使用ForEach循环来动态生成列表项，并设置不同的样式和属性，以实现多样化的列表展示效果。\\n\\n总体功能与效果描述：\\n该示例创建了一个包含多个列表项的列表，每个列表项具有不同的样式（CARD或NONE）。列表项可以多选，并且整个列表具有特定的背景颜色。\\n*/\\n\\n// ListItemExample3.ets\\n@Entry\\n@Component\\nstruct ListItemExample3 {\\n  build() {\\n    Column() {\\n      // 创建一个列表，设置项之间的间距和初始索引\\n      List({ space: \"4vp\", initialIndex: 0 }) {\\n        // 创建一个列表项组，设置样式为CARD\\n        ListItemGroup({ style: ListItemGroupStyle.CARD }) {\\n          // 使用ForEach循环生成多个列表项，每个列表项具有不同的样式\\n          ForEach([ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE], (itemStyle: number, index?: number) => {\\n            // 创建一个列表项，设置样式\\n            ListItem({ style: itemStyle }) {\\n              // 创建一个文本组件，显示当前列表项的索引\\n              Text(\"\" + index)\\n                .width(\"100%\") // 设置文本宽度为100%\\n                .textAlign(TextAlign.Center) // 设置文本居中对齐\\n            }\\n          })\\n        }\\n        // 使用ForEach循环生成多个列表项，每个列表项具有不同的样式\\n        ForEach([ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE], (itemStyle: number, index?: number) => {\\n          // 创建一个列表项，设置样式\\n          ListItem({ style: itemStyle }) {\\n            // 创建一个文本组件，显示当前列表项的索引\\n            Text(\"\" + index)\\n              .width(\"100%\") // 设置文本宽度为100%\\n              .textAlign(TextAlign.Center) // 设置文本居中对齐\\n          }\\n        })\\n      }\\n      .width('100%') // 设置列表宽度为100%\\n      .multiSelectable(true) // 设置列表项可以多选\\n      .backgroundColor(0xDCDCDC) // 设置列表背景颜色\\n    }\\n    .width('100%') // 设置列宽度为100%\\n    .padding({ top: 5 }) // 设置顶部内边距\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用鸿蒙ArkUI框架创建一个简单的列表组件。通过定义一个数字数组，并使用ForEach组件遍历数组生成列表项，每个列表项包含一个文本组件显示数组元素。列表组件设置了间距、初始索引和滚动条状态。\\n\\n总体功能与效果描述：\\n该示例呈现一个垂直排列的列表，列表项之间有20像素的间距，每个列表项显示一个数字，背景为白色，文本居中对齐。列表宽度为屏幕宽度的90%，高度自适应，背景为灰色，顶部有5像素的内边距。\\n*/\\n\\n// ListItemExample.ets\\n@Entry\\n@Component\\nstruct ListItemExample {\\n  // 定义一个数字数组，用于生成列表项\\n  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n\\n  build() {\\n    Column() {\\n      // 创建一个列表组件，设置项之间的间距为20像素，初始显示索引为0\\n      List({ space: 20, initialIndex: 0 }) {\\n        // 使用ForEach组件遍历数组，生成列表项\\n        ForEach(this.arr, (item: number) => {\\n          ListItem() {\\n            // 创建一个文本组件，显示数组元素\\n            Text('' + item)\\n              .width('100%') // 设置文本组件宽度为100%\\n              .height(100) // 设置文本组件高度为100像素\\n              .fontSize(16) // 设置文本字体大小为16像素\\n              .textAlign(TextAlign.Center) // 设置文本居中对齐\\n              .borderRadius(10) // 设置文本组件的边框圆角为10像素\\n              .backgroundColor(0xFFFFFF) // 设置文本组件的背景颜色为白色\\n          }\\n        }, (item: string) => item) // 定义ForEach的键生成函数\\n      }\\n      .width('90%') // 设置列表宽度为屏幕宽度的90%\\n      .scrollBar(BarState.Off) // 关闭滚动条显示\\n    }\\n    .width('100%') // 设置列组件宽度为100%\\n    .height('100%') // 设置列组件高度为100%\\n    .backgroundColor(0xDCDCDC) // 设置列组件的背景颜色为灰色\\n    .padding({ top: 5 }) // 设置列组件顶部内边距为5像素\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用List组件和SwipeAction功能，实现一个带有滑动删除和设置按钮的列表项。通过@State装饰器管理列表数据和状态字符串，使用@Builder装饰器定义可重用的UI组件，以及通过swipeAction接口实现滑动操作。\\n\\n总体功能与效果描述：\\n- 显示一个包含多个列表项的列表，每个列表项可以滑动以显示删除和设置按钮。\\n- 滑动到特定区域时，更新状态字符串以反映当前操作状态。\\n- 点击删除按钮时，从列表中移除对应的列表项，并带有动画效果。\\n*/\\n\\n// ListItemExample2.ets\\n@Entry\\n@Component\\nstruct ListItemExample2 {\\n  @State arr: number[] = [0, 1, 2, 3, 4]; // 初始化列表数据\\n  @State enterEndDeleteAreaString: string = \"not enterEndDeleteArea\"; // 初始化进入删除区域的状态字符串\\n  @State exitEndDeleteAreaString: string = \"not exitEndDeleteArea\"; // 初始化离开删除区域的状态字符串\\n\\n  // 定义一个可重用的UI组件，包含两个按钮：删除和设置\\n  @Builder itemEnd() {\\n    Row() {\\n      Button(\"Delete\").margin(\"4vp\") // 删除按钮\\n      Button(\"Set\").margin(\"4vp\") // 设置按钮\\n    }.padding(\"4vp\").justifyContent(FlexAlign.SpaceEvenly) // 设置布局和对齐方式\\n  }\\n\\n  build() {\\n    Column() {\\n      List({ space: 10 }) { // 创建一个列表，设置项间距\\n        ForEach(this.arr, (item: number) => { // 遍历列表数据\\n          ListItem() {\\n            Text(\"item\" + item) // 显示列表项文本\\n              .width('100%')\\n              .height(100)\\n              .fontSize(16)\\n              .textAlign(TextAlign.Center)\\n              .borderRadius(10)\\n              .backgroundColor(0xFFFFFF)\\n          }\\n          .transition({ type: TransitionType.Delete, opacity: 0 }) // 设置删除动画\\n          .swipeAction({\\n            end: {\\n              builder: () => { this.itemEnd() }, // 滑动时显示的UI组件\\n              onAction: () => {\\n                animateTo({ duration: 1000 }, () => { // 执行删除动画\\n                  let index = this.arr.indexOf(item); // 获取当前项的索引\\n                  this.arr.splice(index, 1); // 从列表中移除当前项\\n                })\\n              },\\n              actionAreaDistance: 56, // 设置滑动区域距离\\n              onEnterActionArea: () => { // 进入滑动区域时的回调\\n                this.enterEndDeleteAreaString = \"enterEndDeleteArea\"; // 更新状态字符串\\n                this.exitEndDeleteAreaString = \"not exitEndDeleteArea\";\\n              },\\n              onExitActionArea: () => { // 离开滑动区域时的回调\\n                this.enterEndDeleteAreaString = \"not enterEndDeleteArea\";\\n                this.exitEndDeleteAreaString = \"exitEndDeleteArea\"; // 更新状态字符串\\n              }\\n            }\\n          })\\n        }, (item: string) => item)\\n      }\\n      Text(this.enterEndDeleteAreaString).fontSize(20) // 显示进入删除区域的状态字符串\\n      Text(this.exitEndDeleteAreaString).fontSize(20) // 显示离开删除区域的状态字符串\\n    }\\n    .padding(10)\\n    .backgroundColor(0xDCDCDC)\\n    .width('100%')\\n    .height('100%')\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "ListItemGroup": {
        "description": "该组件用来展示列表item分组，宽度默认充满List组件，必须配合List组件来使用。",
        "details": None,
        "interfaces": [
            {
                "description": "ListItemGroup(options?: ListItemGroupOptions)",
                "params": {
                    "options": {
                        "type": "ListItemGroupOptions",
                        "required": False,
                        "description": "ListItemGroup的配置选项。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "divider": {
                "description": "设置ListItem分割线样式，默认无分割线。",
                "params": {
                    "value": {
                        "type": {
                            "strokeWidth": "Length",
                            "color": "ResourceColor",
                            "startMargin": "Length",
                            "endMargin": "Length"
                        },
                        "required": True,
                        "description": "ListItem分割线样式。",
                        "default": None
                    }
                }
            },
            "childrenMainSize": {
                "description": "设置ListItemGroup组件的子组件在主轴方向的大小信息。",
                "params": {
                    "value": {
                        "type": "ChildrenMainSize",
                        "required": True,
                        "description": "子组件在主轴方向的大小信息。",
                        "default": None
                    }
                }
            }
        },
        "events": {},
        "rules": [
            "该组件的父组件只能是List。",
            "ListItemGroup组件不支持设置通用属性aspectRatio。",
            "当ListItemGroup的父组件List的listDirection属性为Axis.Vertical时，设置通用属性height属性不生效。",
            "当父组件List的listDirection属性为Axis.Horizontal时，设置通用属性width属性不生效。",
            "当前ListItemGroup内部的ListItem组件不支持编辑、拖拽功能，即ListItem组件的editable属性不生效。"
        ],
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何使用List、ListItemGroup和ListItem组件来创建一个具有不同样式和布局的列表。通过定义一个包含不同样式组合的数组，动态生成列表项组和列表项，并为其添加文本内容。\\n\\n总体功能与效果描述：\\n该示例创建了一个包含多个列表项组的列表，每个列表项组包含不同样式的列表项。列表项组和列表项的样式通过数组动态配置，实现了灵活的布局和样式控制。\\n*/\\n\\n// ListItemGroupExample2.ets\\n@Entry\\n@Component\\nstruct ListItemGroupExample2 {\\n  // 定义一个数组，包含多个对象，每个对象表示一个列表项组的样式和其内部列表项的样式\\n  private arr: ArrObject[] = [\\n    {\\n      style: ListItemGroupStyle.CARD, // 列表项组的样式为CARD\\n      itemStyles: [ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.CARD] // 列表项的样式均为CARD\\n    },\\n    {\\n      style: ListItemGroupStyle.CARD, // 列表项组的样式为CARD\\n      itemStyles: [ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE] // 列表项的样式分别为CARD、CARD、NONE\\n    },\\n    {\\n      style: ListItemGroupStyle.CARD, // 列表项组的样式为CARD\\n      itemStyles: [ListItemStyle.CARD, ListItemStyle.NONE, ListItemStyle.CARD] // 列表项的样式分别为CARD、NONE、CARD\\n    },\\n    {\\n      style: ListItemGroupStyle.NONE, // 列表项组的样式为NONE\\n      itemStyles: [ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE] // 列表项的样式分别为CARD、CARD、NONE\\n    }\\n  ]\\n\\n  build() {\\n    Column() {\\n      List({ space: \"4vp\", initialIndex: 0 }) { // 创建一个列表，设置项之间的间距和初始索引\\n        ForEach(this.arr, (item: ArrObject, index?: number) => { // 遍历数组，生成列表项组\\n          ListItemGroup({ style: item.style }) { // 创建列表项组，设置样式\\n            ForEach(item.itemStyles, (itemStyle: number, itemIndex?: number) => { // 遍历列表项组的样式数组，生成列表项\\n              ListItem({ style: itemStyle }) { // 创建列表项，设置样式\\n                if (index != undefined && itemIndex != undefined) {\\n                  Text(\"第\" + (index + 1) + \"个Group中第\" + (itemIndex + 1) + \"个item\") // 显示文本内容\\n                    .width(\"100%\")\\n                    .textAlign(TextAlign.Center) // 文本居中对齐\\n                }\\n              }\\n            }, (item: string) => item) // 使用item作为键\\n          }\\n        })\\n      }\\n      .width('100%') // 设置列表宽度为100%\\n      .multiSelectable(true) // 启用多选功能\\n      .backgroundColor(0xDCDCDC) // 设置背景颜色\\n    }\\n    .width('100%') // 设置列宽度为100%\\n    .padding({ top: 5 }) // 设置顶部内边距\\n  }\\n}\\n\\n// 定义一个接口，描述数组中对象的结构\\ninterface ArrObject {\\n  style: number; // 列表项组的样式\\n  itemStyles: number[]; // 列表项的样式数组\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用鸿蒙ArkUI框架创建一个包含多个列表项组（ListItemGroup）的列表（List）。每个列表项组包含一个标题（header）和底部信息（footer），以及多个列表项（ListItem）。通过使用@Builder装饰器，可以方便地定义列表项组的头部和底部内容。\\n\\n总体功能与效果描述：\\n该组件展示了一个时间表，其中每个时间表项包含一个标题（如星期一）和对应的项目列表（如语文、数学、英语）。每个列表项组都有一个自定义的头部和底部，头部显示标题，底部显示该天的课程总数。列表项组之间有分隔线，整个列表具有粘性头部和底部，且不显示滚动条。\\n*/\\n\\n// ListItemGroupExample.ets\\n@Entry\\n@Component\\nstruct ListItemGroupExample {\\n  private timeTable: TimeTable[] = [\\n    {\\n      title: '星期一',\\n      projects: ['语文', '数学', '英语']\\n    },\\n    {\\n      title: '星期二',\\n      projects: ['物理', '化学', '生物']\\n    },\\n    {\\n      title: '星期三',\\n      projects: ['历史', '地理', '政治']\\n    },\\n    {\\n      title: '星期四',\\n      projects: ['美术', '音乐', '体育']\\n    }\\n  ]\\n\\n  @Builder\\n  itemHead(text: string) {\\n    // 创建列表项组的头部，显示标题，设置字体大小、背景颜色、宽度和内边距\\n    Text(text)\\n      .fontSize(20)\\n      .backgroundColor(0xAABBCC)\\n      .width(\"100%\")\\n      .padding(10)\\n  }\\n\\n  @Builder\\n  itemFoot(num: number) {\\n    // 创建列表项组的底部，显示课程总数，设置字体大小、背景颜色、宽度和内边距\\n    Text('共' + num + \"节课\")\\n      .fontSize(16)\\n      .backgroundColor(0xAABBCC)\\n      .width(\"100%\")\\n      .padding(5)\\n  }\\n\\n  build() {\\n    Column() {\\n      List({ space: 20 }) {\\n        ForEach(this.timeTable, (item: TimeTable) => {\\n          // 创建列表项组，设置头部和底部，并在其中添加项目列表\\n          ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {\\n            ForEach(item.projects, (project: string) => {\\n              ListItem() {\\n                // 创建列表项，显示项目名称，设置宽度、高度、字体大小、文本对齐方式和背景颜色\\n                Text(project)\\n                  .width(\"100%\")\\n                  .height(100)\\n                  .fontSize(20)\\n                  .textAlign(TextAlign.Center)\\n                  .backgroundColor(0xFFFFFF)\\n              }\\n            }, (item: string) => item)\\n          }\\n          .divider({ strokeWidth: 1, color: Color.Blue }) // 设置列表项组之间的分隔线\\n        })\\n      }\\n      .width('90%')\\n      .sticky(StickyStyle.Header | StickyStyle.Footer) // 设置列表的头部和底部为粘性\\n      .scrollBar(BarState.Off) // 不显示滚动条\\n    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })\\n  }\\n}\\n\\ninterface TimeTable {\\n  title: string;\\n  projects: string[];\\n}"
        ],
        "is_common_attrs": False
    },
    "Navigator": {"description": "路由容器组件，提供路由跳转能力，可以包含子组件。"},
    "Refresh": {"description": "可以进行页面下拉操作并显示刷新动效的容器组件，支持单个子组件。"},
    "RelativeContainer": {
    "description": "相对布局组件，用于复杂场景中元素对齐的布局。",
    "details": "该组件从API Version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。",
    "interfaces": [
        {
            "description": "RelativeContainer()",
            "params": {}
        },
        {
            "description": "guideLine(value: Array<GuideLineStyle>)",
            "params": {
                "value": {
                    "type": "Array<GuideLineStyle>",
                    "required": True,
                    "description": "设置RelativeContainer容器内的辅助线，Array中每个项目即为一条guideline。",
                    "default": None
                }
            }
        },
        {
            "description": "barrier(value: Array<BarrierStyle>)",
            "params": {
                "value": {
                    "type": "Array<BarrierStyle>",
                    "required": True,
                    "description": "设置RelativeContainer容器内的屏障，Array中每个项目即为一条barrier。",
                    "default": None
                }
            }
        }
    ],
    "attributes": {
        "alignRules": {
            "description": "子组件可以将容器、guideline、barrier或者其他子组件设为锚点。",
            "params": {
                "top": {
                    "type": "AlignRule",
                    "required": False,
                    "description": "垂直方向的顶部对齐规则。",
                    "default": None
                },
                "center": {
                    "type": "AlignRule",
                    "required": False,
                    "description": "垂直方向的中心对齐规则。",
                    "default": None
                },
                "bottom": {
                    "type": "AlignRule",
                    "required": False,
                    "description": "垂直方向的底部对齐规则。",
                    "default": None
                },
                "left": {
                    "type": "AlignRule",
                    "required": False,
                    "description": "水平方向的左侧对齐规则。",
                    "default": None
                },
                "middle": {
                    "type": "AlignRule",
                    "required": False,
                    "description": "水平方向的中间对齐规则。",
                    "default": None
                },
                "right": {
                    "type": "AlignRule",
                    "required": False,
                    "description": "水平方向的右侧对齐规则。",
                    "default": None
                },
                "bias": {
                    "type": "Bias",
                    "required": False,
                    "description": "对齐后的额外偏移。",
                    "default": None
                }
            }
        },
        "margin": {
            "description": "子组件的margin含义不同于通用属性的margin，其含义为到该方向上的锚点的距离。若该方向上没有锚点，则该方向的margin不生效。",
            "params": {
                "value": {
                    "type": "number",
                    "required": True,
                    "description": "margin值。",
                    "default": None
                }
            }
        },
        "width": {
            "description": "设置容器的宽度。",
            "params": {
                "value": {
                    "type": "string",
                    "required": True,
                    "description": "宽度值，可以为具体数值或'auto'。",
                    "default": None
                }
            }
        },
        "height": {
            "description": "设置容器的高度。",
            "params": {
                "value": {
                    "type": "string",
                    "required": True,
                    "description": "高度值，可以为具体数值或'auto'。",
                    "default": None
                }
            }
        }
    },
    "events": {},
    "rules": [
        "容器内子组件区分水平方向，垂直方向。",
        "子组件可以将容器、guideline、barrier或者其他子组件设为锚点。",
        "当同时存在前端页面设置的子组件尺寸和相对布局规则时，子组件的绘制尺寸取决于约束规则。",
        "对齐后需要额外偏移可设置offset。",
        "当width设置auto时，如果水平方向上子组件以容器作为锚点，则auto不生效，垂直方向上同理。",
        "相对布局容器内的子组件的margin含义不同于通用属性的margin，其含义为到该方向上的锚点的距离。",
        "guideline的位置在不声明或者声明异常值(如undefined)时，取start：0的位置。",
        "当容器在某个方向的size声明为“auto”时，该方向上guideline的位置只能使用start的方式声明(不可使用百分比)。",
        "垂直方向的guideline和barrier只能作为组件水平方向的锚点，作为垂直方向的锚点时取0；水平方向的guideline和barrier只能作为组件垂直方向的锚点，作为水平方向的锚点时取0。",
        "链的形成依靠组件间的依赖关系。",
        "链的方向和格式声明在链头组件的chainMode接口；链内元素的bias属性全部失效，链头元素的bias作为整个链的bias生效。",
        "链内所有元素的size如果超出链的锚点约束，超出的部分将均分在链的两侧。",
        "特殊情况：根据约束条件和子组件本身的size属性无法确定子组件大小，则子组件不绘制。",
        "互相依赖、环形依赖时容器内子组件全部不绘制。",
        "同方向上两个及以上位置设置锚点但锚点位置逆序时此子组件大小为0，即不绘制。"
    ],
    "examples": [
        "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用Guideline组件来定位其他组件。通过定义垂直和水平方向的Guideline，并将其作为其他组件的锚点，可以精确控制组件的位置。\\n总体功能与效果描述：\\n示例中创建了一个RelativeContainer，并在其中定义了两个Guideline（一个垂直，一个水平）。一个红色的Row组件通过这些Guideline进行定位，使其左边缘和上边缘分别与Guideline对齐。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 创建一个红色的Row组件，宽度为100，高度为100\\n        Row().width(100).height(100)\\n          .backgroundColor(\"#FF3333\")\\n          // 设置Row组件的定位规则\\n          .alignRules({\\n            // 左边缘与guideline1的末端对齐\\n            left: {anchor: \"guideline1\", align: HorizontalAlign.End},\\n            // 上边缘与guideline2的顶部对齐\\n            top: {anchor: \"guideline2\", align: VerticalAlign.Top}\\n          })\\n          .id(\"row1\")\\n      }\\n      // 设置RelativeContainer的宽度和高度，并添加边框\\n      .width(300).height(300)\\n      .margin({left: 50})\\n      .border({width:2, color: \"#6699FF\"})\\n      // 定义两个Guideline，一个垂直，一个水平，分别位于容器的50像素处\\n      .guideLine([\\n        {id:\"guideline1\", direction: Axis.Vertical, position:{start:50}},\\n        {id:\"guideline2\", direction: Axis.Horizontal, position:{start:50}}\\n      ])\\n    }\\n    .height('100%')\\n  }\\n}",
        "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用RelativeContainer组件的bias属性来控制子组件的垂直偏移。通过设置bias属性，可以使子组件相对于其父容器的顶部和底部进行偏移，从而实现更灵活的布局效果。\\n\\n总体功能与效果描述：\\n该示例创建了一个包含红色矩形的RelativeContainer，并通过bias属性将其垂直偏移到父容器的30%位置。矩形的其他对齐规则（如顶部、底部、左侧、右侧）也进行了设置，以确保其在父容器中的位置。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 创建一个宽度为100，高度为100的红色矩形\\n        Row().width(100).height(100)\\n          .backgroundColor(\"#FF3333\")\\n          .alignRules({\\n            // 矩形的顶部与父容器的顶部对齐\\n            top: {anchor: \"__container__\", align: VerticalAlign.Top},\\n            // 矩形的底部与父容器的底部对齐\\n            bottom: {anchor: \"__container__\", align: VerticalAlign.Bottom},\\n            // 矩形的左侧与父容器的左侧对齐\\n            left: {anchor: \"__container__\", align: HorizontalAlign.Start},\\n            // 矩形的右侧与父容器的右侧对齐\\n            right: {anchor: \"__container__\", align: HorizontalAlign.End},\\n            // 设置矩形的垂直偏移，使其相对于父容器的顶部和底部偏移30%\\n            bias: {vertical: 0.3}\\n          })\\n          .id(\"row1\")\\n      }\\n      .width(300).height(300)\\n      .margin({left: 50}) // 设置RelativeContainer的左边距为50\\n      .border({width:2, color: \"#6699FF\"}) // 为RelativeContainer添加一个宽度为2的蓝色边框\\n    }\\n    .height('100%') // 设置Row的高度为100%\\n  }\\n}",
        "/*\\n实现思路：\\n本示例展示了如何在容器内为子组件设置margin，并通过RelativeContainer组件实现子组件的相对定位。通过设置不同的alignRules，子组件可以在容器内以不同的方式排列。\\n总体功能与效果描述：\\n该示例展示了四个不同颜色的矩形（Row组件）在RelativeContainer内的布局。每个矩形都有不同的背景颜色，并且通过margin属性设置了外边距。通过alignRules属性，矩形之间实现了相对定位，形成了一个复杂的布局效果。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 第一个矩形，红色背景，位于容器的左上角，设置了10像素的margin\\n        Row(){Text('row1')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF3333\")\\n          .alignRules({\\n            top: {anchor: \"__container__\", align: VerticalAlign.Top}, // 顶部对齐容器顶部\\n            left: {anchor: \"__container__\", align: HorizontalAlign.Start} // 左侧对齐容器左侧\\n          })\\n          .id(\"row1\")\\n          .margin(10) // 设置外边距为10像素\\n\\n        // 第二个矩形，黄色背景，位于第一个矩形的右侧\\n        Row(){Text('row2')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FFCC00\")\\n          .alignRules({\\n            left: {anchor: \"row1\", align: HorizontalAlign.End}, // 左侧对齐第一个矩形的右侧\\n            top: {anchor: \"row1\", align: VerticalAlign.Top} // 顶部对齐第一个矩形的顶部\\n          })\\n          .id(\"row2\")\\n\\n        // 第三个矩形，橙色背景，位于第一个矩形的下方\\n        Row(){Text('row3')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF6633\")\\n          .alignRules({\\n            left: {anchor: \"row1\", align: HorizontalAlign.Start}, // 左侧对齐第一个矩形的左侧\\n            top: {anchor: \"row1\", align: VerticalAlign.Bottom} // 顶部对齐第一个矩形的底部\\n          })\\n          .id(\"row3\")\\n\\n        // 第四个矩形，浅橙色背景，位于第三个矩形的右侧，第二个矩形的下方，设置了10像素的margin\\n        Row(){Text('row4')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF9966\")\\n          .alignRules({\\n            left: {anchor: \"row3\", align: HorizontalAlign.End}, // 左侧对齐第三个矩形的右侧\\n            top: {anchor: \"row2\", align: VerticalAlign.Bottom} // 顶部对齐第二个矩形的底部\\n          })\\n          .id(\"row4\")\\n          .margin(10) // 设置外边距为10像素\\n      }\\n      .width(300).height(300) // 设置RelativeContainer的宽度和高度\\n      .margin({left: 50}) // 设置RelativeContainer的左侧外边距为50像素\\n      .border({width:2, color: \"#6699FF\"}) // 设置RelativeContainer的边框\\n    }\\n    .height('100%') // 设置Row的高度为100%\\n  }\\n}",
        "/*\\n实现思路：\\n本示例通过使用RelativeContainer组件和Row组件，结合chainMode和bias接口，实现了水平方向的带bias的PACKED链布局。通过设置不同的alignRules，控制子组件在容器中的相对位置和对齐方式。\\n总体功能与效果描述：\\n该示例展示了如何在RelativeContainer中使用chainMode和bias属性，实现水平方向的PACKED链布局。每个Row组件通过设置alignRules来定义其在容器中的相对位置和对齐方式，最终形成一个水平排列的布局效果。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 第一个Row组件，包含文本'row1'，设置为居中对齐，宽度80，高度80，背景色为红色\\n        Row(){Text('row1')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FF3333\")\\n          // 设置alignRules，定义组件的相对位置和对齐方式\\n          .alignRules({\\n            left: {anchor: \"__container__\", align: HorizontalAlign.Start}, // 左对齐到容器左侧\\n            right: {anchor: \"row2\", align : HorizontalAlign.Start}, // 右对齐到row2的左侧\\n            center: {anchor: \"__container__\", align: VerticalAlign.Center}, // 垂直居中对齐到容器\\n            bias : {horizontal : 0} // 水平方向的bias值为0\\n          })\\n          .id(\"row1\") // 设置组件ID为row1\\n          .chainMode(Axis.Horizontal, ChainStyle.PACKED) // 设置水平方向的链模式为PACKED\\n\\n        // 第二个Row组件，包含文本'row2'，设置为居中对齐，宽度80，高度80，背景色为黄色\\n        Row(){Text('row2')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FFCC00\")\\n          // 设置alignRules，定义组件的相对位置和对齐方式\\n          .alignRules({\\n            left: {anchor: \"row1\", align: HorizontalAlign.End}, // 左对齐到row1的右侧\\n            right: {anchor: \"row3\", align : HorizontalAlign.Start}, // 右对齐到row3的左侧\\n            top: {anchor: \"row1\", align: VerticalAlign.Top} // 顶部对齐到row1的顶部\\n          })\\n          .id(\"row2\") // 设置组件ID为row2\\n\\n        // 第三个Row组件，包含文本'row3'，设置为居中对齐，宽度80，高度80，背景色为橙色\\n        Row(){Text('row3')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FF6633\")\\n          // 设置alignRules，定义组件的相对位置和对齐方式\\n          .alignRules({\\n            left: {anchor: \"row2\", align: HorizontalAlign.End}, // 左对齐到row2的右侧\\n            right: {anchor: \"__container__\", align : HorizontalAlign.End}, // 右对齐到容器右侧\\n            top: {anchor: \"row1\", align: VerticalAlign.Top} // 顶部对齐到row1的顶部\\n          })\\n          .id(\"row3\") // 设置组件ID为row3\\n      }\\n      .width(300).height(300) // 设置RelativeContainer的宽度和高度\\n      .margin({left: 50}) // 设置左侧外边距\\n      .border({width:2, color: \"#6699FF\"}) // 设置边框宽度和颜色\\n    }\\n    .height('100%') // 设置Row的高度为100%\\n  }\\n}",
        "/*\\n实现思路：\\n本示例展示了如何使用RelativeContainer组件来实现容器内子组件的相对定位。通过设置子组件的alignRules属性，可以指定子组件相对于其他子组件的位置。整个RelativeContainer的大小会根据其内容自动调整，即设置width和height为\"auto\"。\\n\\n总体功能与效果描述：\\n1. 创建一个RelativeContainer，其中包含四个Row组件，每个Row组件内有一个Text组件。\\n2. 每个Row组件通过alignRules属性相对于其他Row组件进行定位。\\n3. RelativeContainer的大小会根据其内容自动调整，并且有一个蓝色的边框。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 第一个Row组件，包含一个Text组件，内容为'row1'，宽度为100，高度为100，背景颜色为红色，居中对齐\\n        Row(){Text('row1')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF3333\")\\n          .id(\"row1\") // 设置id为\"row1\"，用于后续的相对定位\\n\\n        // 第二个Row组件，包含一个Text组件，内容为'row2'，宽度为100，高度为100，背景颜色为黄色，相对于\"row1\"进行定位\\n        Row(){Text('row2')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FFCC00\")\\n          .alignRules({\\n            left: {anchor: \"row1\", align: HorizontalAlign.End}, // 相对于\"row1\"的右边\\n            top: {anchor: \"row1\", align: VerticalAlign.Top} // 相对于\"row1\"的顶部\\n          })\\n          .id(\"row2\") // 设置id为\"row2\"，用于后续的相对定位\\n\\n        // 第三个Row组件，包含一个Text组件，内容为'row3'，宽度为100，高度为100，背景颜色为橙色，相对于\"row1\"进行定位\\n        Row(){Text('row3')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF6633\")\\n          .alignRules({\\n            left: {anchor: \"row1\", align: HorizontalAlign.Start}, // 相对于\"row1\"的左边\\n            top: {anchor: \"row1\", align: VerticalAlign.Bottom} // 相对于\"row1\"的底部\\n          })\\n          .id(\"row3\") // 设置id为\"row3\"，用于后续的相对定位\\n\\n        // 第四个Row组件，包含一个Text组件，内容为'row4'，宽度为100，高度为100，背景颜色为浅橙色，相对于\"row3\"和\"row2\"进行定位\\n        Row(){Text('row4')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF9966\")\\n          .alignRules({\\n            left: {anchor: \"row3\", align: HorizontalAlign.End}, // 相对于\"row3\"的右边\\n            top: {anchor: \"row2\", align: VerticalAlign.Bottom} // 相对于\"row2\"的底部\\n          })\\n          .id(\"row4\") // 设置id为\"row4\"，用于后续的相对定位\\n      }\\n      .width(\"auto\").height(\"auto\") // 设置RelativeContainer的宽度和高度为\"auto\"，使其大小适应内容\\n      .margin({left: 50}) // 设置左边距为50\\n      .border({width:2, color: \"#6699FF\"}) // 设置边框宽度为2，颜色为蓝色\\n    }\\n    .height('100%') // 设置Row的高度为100%\\n  }\\n}",
        "/*\\n实现思路：\\n本示例展示了如何使用RelativeContainer和barrier来实现复杂的布局。通过定义多个Row组件，并使用alignRules和barrier来控制它们的位置关系，实现了一种灵活的布局方式。\\n\\n总体功能与效果描述：\\n示例展示了四个Row组件在RelativeContainer中的布局。通过barrier定义了两个虚拟的边界线，这些边界线作为锚点，帮助其他组件进行定位。最终效果是四个不同颜色的矩形在容器中以特定的相对位置排列。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 第一个Row组件，显示文本'row1'，背景色为红色，宽度高度均为100，居中对齐\\n        Row(){Text('row1')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF3333\")\\n          .id(\"row1\") // 为该组件设置ID，方便后续组件引用\\n\\n        // 第二个Row组件，显示文本'row2'，背景色为黄色，宽度高度均为100，相对于row1进行定位\\n        Row(){Text('row2')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FFCC00\")\\n          .alignRules({\\n            middle: {anchor: \"row1\", align: HorizontalAlign.End}, // 水平方向上与row1的右边缘对齐\\n            top: {anchor: \"row1\", align: VerticalAlign.Bottom} // 垂直方向上与row1的底边缘对齐\\n          })\\n          .id(\"row2\") // 为该组件设置ID，方便后续组件引用\\n\\n        // 第三个Row组件，显示文本'row3'，背景色为橙色，宽度高度均为100，相对于barrier1进行定位\\n        Row(){Text('row3')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF6633\")\\n          .alignRules({\\n            left: {anchor: \"barrier1\", align: HorizontalAlign.End}, // 水平方向上与barrier1的右边缘对齐\\n            top: {anchor: \"row1\", align: VerticalAlign.Top} // 垂直方向上与row1的顶边缘对齐\\n          })\\n          .id(\"row3\") // 为该组件设置ID，方便后续组件引用\\n\\n        // 第四个Row组件，显示文本'row4'，背景色为浅橙色，宽度高度均为50，相对于row1和barrier2进行定位\\n        Row(){Text('row4')}.justifyContent(FlexAlign.Center)\\n          .width(50).height(50)\\n          .backgroundColor(\"#FF9966\")\\n          .alignRules({\\n            left: {anchor: \"row1\", align: HorizontalAlign.Start}, // 水平方向上与row1的左边缘对齐\\n            top: {anchor: \"barrier2\", align: VerticalAlign.Bottom} // 垂直方向上与barrier2的底边缘对齐\\n          })\\n          .id(\"row4\") // 为该组件设置ID，方便后续组件引用\\n      }\\n      .width(300).height(300) // 设置RelativeContainer的宽度和高度\\n      .margin({left: 50}) // 设置左边距\\n      .border({width:2, color: \"#6699FF\"}) // 设置边框\\n      .barrier([\\n        {id: \"barrier1\", direction: BarrierDirection.RIGHT, referencedId:[\"row1\", \"row2\"]}, // 定义barrier1，方向为右，参考row1和row2的右边缘\\n        {id: \"barrier2\", direction: BarrierDirection.BOTTOM, referencedId:[\"row1\", \"row2\"]} // 定义barrier2，方向为下，参考row1和row2的底边缘\\n      ])\\n    }\\n    .height('100%') // 设置Row的高度为100%\\n  }\\n}",
        "/*\\n实现思路：\\n本示例展示了如何使用RelativeContainer组件进行相对布局。通过设置不同的alignRules，我们可以将子组件相对于容器或其他子组件进行定位。每个Row组件代表一个子组件，通过id属性进行标识，并在alignRules中引用这些id来定义相对位置。\\n\\n总体功能与效果描述：\\n该示例展示了五个不同颜色的Row组件，它们在RelativeContainer中以不同的相对位置进行布局。每个Row组件通过alignRules属性定义了相对于容器或其他Row组件的位置，从而实现复杂的相对布局效果。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 第一个Row组件，位于容器的左上角\\n        Row(){Text('row1')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF3333\")\\n          .alignRules({\\n            top: {anchor: \"__container__\", align: VerticalAlign.Top}, // 顶部与容器顶部对齐\\n            left: {anchor: \"__container__\", align: HorizontalAlign.Start} // 左侧与容器左侧对齐\\n          })\\n          .id(\"row1\") // 设置id以便在其他组件中引用\\n\\n        // 第二个Row组件，位于容器的右上角\\n        Row(){Text('row2')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FFCC00\")\\n          .alignRules({\\n            top: {anchor: \"__container__\", align: VerticalAlign.Top}, // 顶部与容器顶部对齐\\n            right: {anchor: \"__container__\", align: HorizontalAlign.End} // 右侧与容器右侧对齐\\n          })\\n          .id(\"row2\") // 设置id以便在其他组件中引用\\n\\n        // 第三个Row组件，位于row1的右下角，并且与row2的左侧对齐\\n        Row(){Text('row3')}.justifyContent(FlexAlign.Center)\\n          .height(100)\\n          .backgroundColor(\"#FF6633\")\\n          .alignRules({\\n            top: {anchor: \"row1\", align: VerticalAlign.Bottom}, // 顶部与row1的底部对齐\\n            left: {anchor: \"row1\", align: HorizontalAlign.End}, // 左侧与row1的右侧对齐\\n            right: {anchor: \"row2\", align: HorizontalAlign.Start} // 右侧与row2的左侧对齐\\n          })\\n          .id(\"row3\") // 设置id以便在其他组件中引用\\n\\n        // 第四个Row组件，位于row3的下方，并且与容器的左下角和row1的右侧对齐\\n        Row(){Text('row4')}.justifyContent(FlexAlign.Center)\\n          .backgroundColor(\"#FF9966\")\\n          .alignRules({\\n            top: {anchor: \"row3\", align: VerticalAlign.Bottom}, // 顶部与row3的底部对齐\\n            bottom: {anchor: \"__container__\", align: VerticalAlign.Bottom}, // 底部与容器底部对齐\\n            left: {anchor: \"__container__\", align: HorizontalAlign.Start}, // 左侧与容器左侧对齐\\n            right: {anchor: \"row1\", align: HorizontalAlign.End} // 右侧与row1的右侧对齐\\n          })\\n          .id(\"row4\") // 设置id以便在其他组件中引用\\n\\n        // 第五个Row组件，位于row3的下方，并且与row2的左侧和容器的右下角对齐\\n        Row(){Text('row5')}.justifyContent(FlexAlign.Center)\\n          .backgroundColor(\"#FF66FF\")\\n          .alignRules({\\n            top: {anchor: \"row3\", align: VerticalAlign.Bottom}, // 顶部与row3的底部对齐\\n            bottom: {anchor: \"__container__\", align: VerticalAlign.Bottom}, // 底部与容器底部对齐\\n            left: {anchor: \"row2\", align: HorizontalAlign.Start}, // 左侧与row2的左侧对齐\\n            right: {anchor: \"__container__\", align: HorizontalAlign.End} // 右侧与容器右侧对齐\\n          })\\n          .id(\"row5\") // 设置id以便在其他组件中引用\\n      }\\n      .width(300).height(300) // 设置RelativeContainer的宽度和高度\\n      .margin({left: 50}) // 设置左侧外边距\\n      .border({width:2, color: \"#6699FF\"}) // 设置边框\\n    }\\n    .height('100%') // 设置Row的高度为100%\\n  }\\n}",
        "/*\\n实现思路：\\n本示例展示了在RTL（Right-to-Left）模式下，使用RelativeContainer组件来实现多个Row组件的对齐布局。通过设置LocalizedAlignRuleOptions和LocalizedBarrierDirection，我们可以灵活地控制组件的对齐方式和锚点。示例中使用了barrier作为锚点，并通过alignRules属性来指定每个Row组件的对齐规则。\\n\\n总体功能与效果描述：\\n1. 创建一个RelativeContainer组件，并在其中放置四个Row组件。\\n2. 每个Row组件通过alignRules属性设置其相对于其他组件或barrier的对齐方式。\\n3. 使用barrier来定义两个虚拟的锚点，分别用于水平和垂直方向的对齐。\\n4. 设置RelativeContainer的方向为RTL，以展示在RTL模式下的布局效果。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 第一个Row组件，显示文本'row1'，并设置其宽度和高度为100，背景颜色为红色\\n        Row(){Text('row1')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF3333\")\\n          .id(\"row1\") // 设置组件的id为\"row1\"，用于后续的对齐规则引用\\n\\n        // 第二个Row组件，显示文本'row2'，并设置其宽度和高度为100，背景颜色为黄色\\n        Row(){Text('row2')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FFCC00\")\\n          .alignRules({\\n            middle: {anchor: \"row1\", align: HorizontalAlign.End}, // 水平方向上，row2相对于row1的右侧对齐\\n            top: {anchor: \"row1\", align: VerticalAlign.Bottom} // 垂直方向上，row2相对于row1的底部对齐\\n          })\\n          .id(\"row2\") // 设置组件的id为\"row2\"，用于后续的对齐规则引用\\n\\n        // 第三个Row组件，显示文本'row3'，并设置其宽度和高度为100，背景颜色为橙色\\n        Row(){Text('row3')}.justifyContent(FlexAlign.Center)\\n          .width(100).height(100)\\n          .backgroundColor(\"#FF6633\")\\n          .alignRules({\\n            start: {anchor: \"barrier1\", align: HorizontalAlign.End}, // 水平方向上，row3相对于barrier1的右侧对齐\\n            top: {anchor: \"row1\", align: VerticalAlign.Top} // 垂直方向上，row3相对于row1的顶部对齐\\n          })\\n          .id(\"row3\") // 设置组件的id为\"row3\"，用于后续的对齐规则引用\\n\\n        // 第四个Row组件，显示文本'row4'，并设置其宽度和高度为50，背景颜色为浅橙色\\n        Row(){Text('row4')}.justifyContent(FlexAlign.Center)\\n          .width(50).height(50)\\n          .backgroundColor(\"#FF9966\")\\n          .alignRules({\\n            start: {anchor: \"row1\", align: HorizontalAlign.Start}, // 水平方向上，row4相对于row1的左侧对齐\\n            top: {anchor: \"barrier2\", align: VerticalAlign.Bottom} // 垂直方向上，row4相对于barrier2的底部对齐\\n          })\\n          .id(\"row4\") // 设置组件的id为\"row4\"，用于后续的对齐规则引用\\n      }\\n      .direction(Direction.Rtl) // 设置RelativeContainer的方向为RTL，即从右到左布局\\n      .width(300).height(300) // 设置RelativeContainer的宽度和高度为300\\n      .margin({left: 50}) // 设置RelativeContainer的左边距为50\\n      .border({width:2, color: \"#6699FF\"}) // 设置RelativeContainer的边框宽度和颜色\\n      .barrier([\\n        {id: \"barrier1\", localizedDirection: LocalizedBarrierDirection.END, referencedId:[\"row1\", \"row2\"]}, // 定义barrier1，水平方向上位于row1和row2的右侧\\n        {id: \"barrier2\", localizedDirection: LocalizedBarrierDirection.BOTTOM, referencedId:[\"row1\", \"row2\"]} // 定义barrier2，垂直方向上位于row1和row2的底部\\n      ])\\n    }\\n    .height('100%') // 设置Row组件的高度为100%\\n  }\\n}",
        "/*\\n实现思路：\\n本示例通过使用RelativeContainer组件和chainMode接口，展示了如何在水平方向上实现不同的链布局效果。具体来说，示例中分别实现了SPREAD链、SPREAD_INSIDE链和PACKED链。每个链布局通过设置不同的alignRules和chainMode来实现。\\n\\n总体功能与效果描述：\\n该示例展示了三种不同的水平链布局效果：SPREAD、SPREAD_INSIDE和PACKED。每个链布局由多个Row组件组成，每个Row组件通过设置alignRules来确定其在容器中的位置，并通过chainMode来定义链的布局方式。最终效果是三个不同布局的链在同一个容器中展示。\\n*/\\n\\n// Index.ets\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Row() {\\n      RelativeContainer() {\\n        // 第一个链布局：SPREAD\\n        Row(){Text('row1')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FF3333\")\\n          .alignRules({\\n            left: {anchor: \"__container__\", align: HorizontalAlign.Start}, // 左对齐容器\\n            right: {anchor: \"row2\", align : HorizontalAlign.Start}, // 右对齐row2的左侧\\n            top: {anchor: \"__container__\", align: VerticalAlign.Top} // 顶部对齐容器\\n          })\\n          .id(\"row1\")\\n          .chainMode(Axis.Horizontal, ChainStyle.SPREAD) // 设置水平方向的SPREAD链布局\\n\\n        Row(){Text('row2')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FFCC00\")\\n          .alignRules({\\n            left: {anchor: \"row1\", align: HorizontalAlign.End}, // 左对齐row1的右侧\\n            right: {anchor: \"row3\", align : HorizontalAlign.Start}, // 右对齐row3的左侧\\n            top: {anchor: \"row1\", align: VerticalAlign.Top} // 顶部对齐row1的顶部\\n          })\\n          .id(\"row2\")\\n\\n        Row(){Text('row3')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FF6633\")\\n          .alignRules({\\n            left: {anchor: \"row2\", align: HorizontalAlign.End}, // 左对齐row2的右侧\\n            right: {anchor: \"__container__\", align : HorizontalAlign.End}, // 右对齐容器的右侧\\n            top: {anchor: \"row1\", align: VerticalAlign.Top} // 顶部对齐row1的顶部\\n          })\\n          .id(\"row3\")\\n\\n        // 第二个链布局：SPREAD_INSIDE\\n        Row(){Text('row4')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FF3333\")\\n          .alignRules({\\n            left: {anchor: \"__container__\", align: HorizontalAlign.Start}, // 左对齐容器\\n            right: {anchor: \"row5\", align : HorizontalAlign.Start}, // 右对齐row5的左侧\\n            center: {anchor: \"__container__\", align: VerticalAlign.Center} // 垂直居中对齐容器\\n          })\\n          .id(\"row4\")\\n          .chainMode(Axis.Horizontal, ChainStyle.SPREAD_INSIDE) // 设置水平方向的SPREAD_INSIDE链布局\\n\\n        Row(){Text('row5')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FFCC00\")\\n          .alignRules({\\n            left: {anchor: \"row4\", align: HorizontalAlign.End}, // 左对齐row4的右侧\\n            right: {anchor: \"row6\", align : HorizontalAlign.Start}, // 右对齐row6的左侧\\n            top: {anchor: \"row4\", align: VerticalAlign.Top} // 顶部对齐row4的顶部\\n          })\\n          .id(\"row5\")\\n\\n        Row(){Text('row6')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FF6633\")\\n          .alignRules({\\n            left: {anchor: \"row5\", align: HorizontalAlign.End}, // 左对齐row5的右侧\\n            right: {anchor: \"__container__\", align : HorizontalAlign.End}, // 右对齐容器的右侧\\n            top: {anchor: \"row4\", align: VerticalAlign.Top} // 顶部对齐row4的顶部\\n          })\\n          .id(\"row6\")\\n\\n        // 第三个链布局：PACKED\\n        Row(){Text('row7')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FF3333\")\\n          .alignRules({\\n            left: {anchor: \"__container__\", align: HorizontalAlign.Start}, // 左对齐容器\\n            right: {anchor: \"row8\", align : HorizontalAlign.Start}, // 右对齐row8的左侧\\n            bottom: {anchor: \"__container__\", align: VerticalAlign.Bottom} // 底部对齐容器\\n          })\\n          .id(\"row7\")\\n          .chainMode(Axis.Horizontal, ChainStyle.PACKED) // 设置水平方向的PACKED链布局\\n\\n        Row(){Text('row8')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FFCC00\")\\n          .alignRules({\\n            left: {anchor: \"row7\", align: HorizontalAlign.End}, // 左对齐row7的右侧\\n            right: {anchor: \"row9\", align : HorizontalAlign.Start}, // 右对齐row9的左侧\\n            top: {anchor: \"row7\", align: VerticalAlign.Top} // 顶部对齐row7的顶部\\n          })\\n          .id(\"row8\")\\n\\n        Row(){Text('row9')}.justifyContent(FlexAlign.Center)\\n          .width(80).height(80)\\n          .backgroundColor(\"#FF6633\")\\n          .alignRules({\\n            left: {anchor: \"row8\", align: HorizontalAlign.End}, // 左对齐row8的右侧\\n            right: {anchor: \"__container__\", align : HorizontalAlign.End}, // 右对齐容器的右侧\\n            top: {anchor: \"row7\", align: VerticalAlign.Top} // 顶部对齐row7的顶部\\n          })\\n          .id(\"row9\")\\n      }\\n      .width(300).height(300) // 设置RelativeContainer的宽度和高度\\n      .margin({left: 50}) // 设置左侧外边距\\n      .border({width:2, color: \"#6699FF\"}) // 设置边框\\n    }\\n    .height('100%') // 设置Row的高度为100%\\n  }\\n}"
    ],
    "is_common_attrs": True
},
    "Row": {
        "description": "沿水平方向布局容器，可以包含子组件。",
        "interfaces": [
            {
                "description": "Row(value?:{space?: number | string })",
                "params": {
                    "value": {
                        "type": "object",
                        "required": False,
                        "description": "包含space参数的对象。",
                        "properties": {
                            "space": {
                                "type": ["number", "string"],
                                "required": False,
                                "description": "横向布局元素间距。默认值：0，单位vp。可选值为大于等于0的数字，或者可以转换为数字的字符串。"
                            }
                        }
                    }
                }
            }
        ],
        "attributes": {
            "alignItems": {
                "description": "设置子组件在垂直方向上的对齐格式。",
                "params": {
                    "value": {
                        "type": "VerticalAlign",
                        "required": True,
                        "description": "子组件在垂直方向上的对齐格式。默认值：VerticalAlign.Center"
                    }
                }
            },
            "justifyContent": {
                "description": "设置子组件在水平方向上的对齐格式。",
                "params": {
                    "value": {
                        "type": "FlexAlign",
                        "required": True,
                        "description": "子组件在水平方向上的对齐格式。默认值：FlexAlign.Start"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            "// xxx.ets\n@Entry\n@Component\nstruct RowExample {\n  build() {\n    Column({ space: 5 }) {\n      // 设置子组件水平方向的间距为5\n      Text('space').width('90%')\n      Row({ space: 5 }) {\n        Row().width('30%').height(50).backgroundColor(0xAFEEEE)\n        Row().width('30%').height(50).backgroundColor(0x00FFFF)\n      }.width('90%').height(107).border({ width: 1 })\n\n      // 设置子元素垂直方向对齐方式\n      Text('alignItems(Bottom)').width('90%')\n      Row() {\n        Row().width('30%').height(50).backgroundColor(0xAFEEEE)\n        Row().width('30%').height(50).backgroundColor(0x00FFFF)\n      }.width('90%').alignItems(VerticalAlign.Bottom).height('15%').border({ width: 1 })\n\n      Text('alignItems(Center)').width('90%')\n      Row() {\n        Row().width('30%').height(50).backgroundColor(0xAFEEEE)\n        Row().width('30%').height(50).backgroundColor(0x00FFFF)\n      }.width('90%').alignItems(VerticalAlign.Center).height('15%').border({ width: 1 })\n\n      // 设置子元素水平方向对齐方式\n      Text('justifyContent(End)').width('90%')\n      Row() {\n        Row().width('30%').height(50).backgroundColor(0xAFEEEE)\n        Row().width('30%').height(50).backgroundColor(0x00FFFF)\n      }.width('90%').border({ width: 1 }).justifyContent(FlexAlign.End)\n\n      Text('justifyContent(Center)').width('90%')\n      Row() {\n        Row().width('30%').height(50).backgroundColor(0xAFEEEE)\n        Row().width('30%').height(50).backgroundColor(0x00FFFF)\n      }.width('90%').border({ width: 1 }).justifyContent(FlexAlign.Center)\n    }.width('100%')\n  }\n}"
        ],
        "is_common_attrs": True
    },
    "RowSplit": {"description": "将子组件横向布局，并在每个子组件之间插入一根纵向的分割线，可以包含子组件。"},
    "Scroll": {
        "description": "可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动，支持单个子组件。",
        "interfaces": [
            {
                "description": "Scroll(scroller?: Scroller)",
                "params": {
                    "scroller": {
                        "type": "Scroller",
                        "description": "可滚动组件的控制器。用于与可滚动组件进行绑定。"
                    }
                }
            }
        ],
        "attributes": {
            "scrollable": {
                "description": "设置滚动方向。",
                "params": {
                    "value": {
                        "type": "ScrollDirection",
                        "required": True,
                        "description": "滚动方向。",
                        "default": "ScrollDirection.Vertical"
                    }
                }
            },
            "scrollBar": {
                "description": "设置滚动条状态。如果容器组件无法滚动，则滚动条不显示。如果容器组件的子组件大小为无穷大，则滚动条不支持拖动和伴随滚动。\n从API version 10开始，当滚动组件存在圆角时，为避免滚动条被圆角截断，滚动条会自动计算距顶部和底部的避让距离。",
                "params": {
                    "barState": {
                        "type": "BarState",
                        "required": True,
                        "description": "滚动条状态。",
                        "default": "BarState.Auto"
                    }
                }
            },
            "scrollBarColor": {
                "description": "设置滚动条的颜色。",
                "params": {
                    "color": {
                        "type": ["Color", "number", "string"],
                        "required": True,
                        "description": "滚动条的颜色。",
                        "default": "'#182431'（40%不透明度）"
                    }
                }
            },
            "scrollBarWidth": {
                "description": "设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Scroll组件主轴方向的高度，则滚动条的宽度会变为默认值。",
                "params": {
                    "value": {
                        "type": ["string", "number"],
                        "required": True,
                        "description": "滚动条的宽度。",
                        "default": "4",
                        "unit": "vp"
                    }
                }
            },
            "scrollSnap": {
                "description": "设置Scroll组件的限位滚动模式。",
                "params": {
                    "value": {
                        "type": "ScrollSnapOptions",
                        "required": True,
                        "description": "Scroll组件的限位滚动模式。"
                    }
                }
            },
            "edgeEffect": {
                "description": "设置边缘滑动效果。",
                "params": {
                    "edgeEffect": {
                        "type": "EdgeEffect",
                        "required": True,
                        "description": "Scroll组件的边缘滑动效果，支持弹簧效果和阴影效果。",
                        "default": "EdgeEffect.None"
                    },
                    "options": {
                        "type": "EdgeEffectOptions",
                        "description": "组件内容大小小于组件自身时，是否开启滑动效果。",
                        "default": "True"
                    }
                }
            },
            "enableScrollInteraction": {
                "description": "设置是否支持滚动手势，当设置为false时，无法通过手指或者鼠标滚动，但不影响控制器的滚动接口。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否支持滚动手势。",
                        "default": "True"
                    }
                }
            },
            "nestedScroll": {
                "description": "设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。",
                "params": {
                    "value": {
                        "type": "NestedScrollOptions",
                        "required": True,
                        "description": "嵌套滚动模式。"
                    }
                }
            },
            "friction": {
                "description": "设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。设置为小于等于0的值时，按默认值处理。",
                "params": {
                    "value": {
                        "type": ["Resource", "number"],
                        "required": True,
                        "description": "摩擦系数。",
                        "default": "非可穿戴设备为0.6，可穿戴设备为0.9。从API version 11开始，非可穿戴设备默认值为0.7。"
                    }
                }
            },
            "enablePaging": {
                "description": "设置是否支持划动翻页。如果同时设置了划动翻页enablePaging和限位滚动scrollSnap，则scrollSnap优先生效，enablePaging不生效。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否支持划动翻页。",
                        "default": "false"
                    }
                }
            },
            "flingSpeedLimit": {
                "description": "限制跟手滑动结束后，Fling动效开始时的最大初始速度。单位是vp/s。",
                "params": {
                    "speedLimit": {
                        "type": "number",
                        "required": True,
                        "description": "Fling动效开始时的最大初始速度。"
                    }
                }
            },
            "initialOffset": {
                "description": "设置初始滚动偏移量。只在首次布局时生效，后续动态修改该属性值不生效。",
                "params": {
                    "value": {
                        "type": "OffsetOptions",
                        "required": True,
                        "description": "当输入的大小为百分比时，初始滚动偏移量为Scroll组件主轴方向大小与百分比数值之积。"
                    }
                }
            }
        },
        "events": {
            "onScrollFrameBegin": {
                "description": "onScrollFrameBegin(event: (offset: number, state: ScrollState) => { offsetRemain: number; })\n\n每帧开始滚动时触发，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。\n\n支持offsetRemain为负值。\n\n若通过onScrollFrameBegin事件和scrollBy方法实现容器嵌套滚动，需设置子滚动节点的EdgeEffect为None。如Scroll嵌套List滚动时，List组件的edgeEffect属性需设置为EdgeEffect.None。\n\n触发该事件的条件：\n\n1、滚动组件触发滚动时触发，包括键鼠操作等其他触发滚动的输入设置。\n\n2、调用控制器接口时不触发。\n\n3、越界回弹不触发。\n\n4、拖动滚动条不触发。",
                "params": {
                    "offset": {
                        "type": "number",
                        "required": True,
                        "description": "即将发生的滑动量，单位vp。"
                    },
                    "state": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滑动状态。"
                    }
                },
                "returns": {
                    "offsetRemain": {
                        "type": "number",
                        "description": "实际需要的滚动量，单位vp。"
                    }
                }
            },
            "onScroll": {
                "description": "滚动事件回调，返回滚动时水平、竖直方向偏移量，单位vp。\n\n触发该事件的条件 ：\n\n1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。\n\n2、通过滚动控制器API接口调用。\n\n3、越界回弹。\n\n从API version12开始废弃不再使用，推荐使用[onWillScroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-container-scroll-V5#onwillscroll12)事件替代。",
                "params": {
                    "xOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动时水平方向的偏移量，Scroll的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。"
                    },
                    "yOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动时竖直方向的偏移量，Scroll的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。"
                    }
                }
            },
            "onWillScroll": {
                "description": "滚动事件回调，Scroll滚动前触发。\n\n回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。\n\n触发该事件的条件 ：\n\n1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。\n\n2、通过滚动控制器API接口调用。\n\n3、越界回弹。",
                "params": {
                    "xOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。"
                    },
                    "yOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。"
                    },
                    "scrollState": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滚动状态。"
                    },
                    "scrollSource": {
                        "type": "ScrollSource",
                        "required": True,
                        "description": "当前滚动操作的来源。"
                    }
                }
            },
            "onDidScroll": {
                "description": "滚动事件回调，Scroll滚动时触发。\n\n返回当前帧滚动的偏移量和当前滚动状态。\n\n触发该事件的条件 ：\n\n1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。\n\n2、通过滚动控制器API接口调用。\n\n3、越界回弹。",
                "params": {
                    "xOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。"
                    },
                    "yOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。"
                    },
                    "scrollState": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滚动状态。"
                    }
                }
            },
            "ScrollOnWillScrollCallback": {
                "description": "type ScrollOnWillScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | OffsetResult",
                "params": {
                    "xOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负，单位vp。"
                    },
                    "yOffset": {
                        "type": "number",
                        "required": True,
                        "description": "每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负，单位vp。"
                    },
                    "scrollState": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滚动状态。"
                    },
                    "scrollSource": {
                        "type": "ScrollSource",
                        "required": True,
                        "description": "当前滚动操作的来源。"
                    }
                },
                "returns": {
                    "offsetResult": {
                        "type": "OffsetResult",
                        "description": "实际需要的滚动量。"
                    },
                    "void": {
                        "type": "void",
                        "description": "无返回值。"
                    }
                }
            },
            "onScrollEdge": {
                "description": "滚动到边缘事件回调。\n\n触发该事件的条件 ：\n\n1、滚动组件滚动到边缘时触发，支持键鼠操作等其他触发滚动的输入设置。\n\n2、通过滚动控制器API接口调用。\n\n3、越界回弹。",
                "params": {
                    "side": {
                        "type": "Edge",
                        "required": True,
                        "description": "滚动到的边缘位置。"
                    }
                }
            },
            "onScrollEnd": {
                "description": "滚动停止事件回调。\n\n触发该事件的条件 ：\n\n1、滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。\n\n2、通过滚动控制器API接口调用后停止，带过渡动效。\n\n该事件从API version 9开始废弃，使用onScrollStop事件替代。",
                "params": {}
            },
            "onScrollStart": {
                "description": "滚动开始时触发。手指拖动Scroll或拖动Scroll的滚动条触发的滚动开始时，会触发该事件。使用[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-container-scroll-V5#scroller)滚动控制器触发的带动画的滚动，动画开始时会触发该事件。\n\n触发该事件的条件 ：\n\n1、滚动组件开始滚动时触发，支持键鼠操作等其他触发滚动的输入设置。\n\n2、通过滚动控制器API接口调用后开始，带过渡动效。",
                "params": {}
            },
            "onScrollStop": {
                "description": "滚动停止时触发。手拖动Scroll或拖动Scroll的滚动条触发的滚动，手离开屏幕并且滚动停止时会触发该事件。使用[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-container-scroll-V5#scroller)滚动控制器触发的带动画的滚动，动画停止时会触发该事件。\n\n触发该事件的条件 ：\n\n1、滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。\n\n2、通过滚动控制器API接口调用后开始，带过渡动效。",
                "params": {}
            },
            "onReachStart": {
                "description": "Scroll到达起始位置时触发。\n\nScroll初始化时会触发一次，滚动到起始位置时触发一次。Scroll边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。",
                "params": {}
            },
            "onReachEnd": {
                "description": "Scroll到达末尾位置时触发。\n\nScroll边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。",
                "params": {}
            }
        },
        "examples": [
            """Scroll() {\n    // Scroll的唯一子组件不可以设置height("100%")，否则会导致无法滚动\n    Column() {\n    ...\n    }.width("100%")\n}"""
        ],
        "is_common_attrs": True
    },
    "SideBarContainer": {
        "description": "提供侧边栏可以显示和隐藏的侧边栏容器，通过子组件定义侧边栏和内容区，第一个子组件表示侧边栏，第二个子组件表示内容区，可以包含子组件。"},
    "Stack": {
        "description": "堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。可以包含多个子组件。",
        "interfaces": [
            {
                "description": "Stack(value?: { alignContent?: Alignment })",
                "params": {
                    "alignContent": {
                        "type": "Alignment",
                        "required": False,
                        "description": "设置子组件在容器内的对齐方式。"
                    }
                }
            }
        ],
        "attributes": {
            "alignContent": {
                "description": "设置所有子组件在容器内的对齐方式。该属性与通用属性align同时设置时，后设置的属性生效。",
                "params": {
                    "value": {
                        "type": "Alignment",
                        "required": True,
                        "description": "所有子组件在容器内的对齐方式。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            "/*\n实现思路：\n本示例通过使用Stack组件来展示两个Text子组件的堆叠效果。Stack组件允许子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。通过设置Stack的alignContent属性，可以控制子组件在容器内的对齐方式。每个Text组件通过设置width、height、backgroundColor和align属性来定义其尺寸、背景颜色和对齐方式。\n\n总体功能与效果描述：\n该示例展示了两个Text组件在Stack容器中的堆叠效果，其中第一个Text组件位于底部，第二个Text组件位于顶部并覆盖第一个组件。通过设置Stack的alignContent属性为Alignment.Bottom，使得所有子组件在容器底部对齐。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct StackExample {\n  build() {\n    // 创建一个Stack组件，设置alignContent属性为Alignment.Bottom，使得子组件在容器底部对齐\n    Stack({ alignContent: Alignment.Bottom }) {\n      // 第一个Text组件，设置宽度为90%，高度为100%，背景颜色为0xd2cab3，对齐方式为顶部对齐\n      Text('First child, show in bottom').width('90%').height('100%').backgroundColor(0xd2cab3).align(Alignment.Top)\n      // 第二个Text组件，设置宽度为70%，高度为60%，背景颜色为0xc1cbac，对齐方式为顶部对齐\n      Text('Second child, show in top').width('70%').height('60%').backgroundColor(0xc1cbac).align(Alignment.Top)\n    }.width('100%').height(150).margin({ top: 5 }) // 设置Stack组件的宽度为100%，高度为150，顶部外边距为5\n  }\n}"
        ],
        "is_common_attrs": True
    },
    "Swiper": {"description": "滑块视图容器，提供子组件滑动轮播显示的能力，可以包含子组件。"},
    "Tabs": {
        "description": "通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图，不支持自定义组件作为子组件， 仅可包含子组件TabContent。",
        "interfaces": [
            {
                "description": "Tabs(value?: {barPosition?: BarPosition, index?: number, controller?: TabsController})",
                "params": {
                    "barPosition": {
                        "type": "BarPosition",
                        "description": "设置Tabs的页签位置。",
                        "required": False,
                        "default": "BarPosition.Start"
                    },
                    "index": {
                        "type": "number",
                        "description": "设置当前显示页签的索引。",
                        "required": False,
                        "default": 0
                    },
                    "controller": {
                        "type": "TabsController",
                        "required": False,
                        "description": "设置Tabs控制器。"
                    }
                }
            }
        ],
        "attributes": {
            "vertical": {
                "description": "设置是否为纵向Tab。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否为纵向Tab。",
                        "default": False
                    }
                }
            },
            "scrollable": {
                "description": "设置是否可以通过滑动页面进行页面切换。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否可以通过滑动页面进行页面切换。",
                        "default": True
                    }
                }
            },
            "barMode": {
                "description": "设置TabBar布局模式。",
                "params": {
                    "value": {
                        "type": "BarMode",
                        "required": True,
                        "description": "TabBar布局模式。"
                    },
                    "options": {
                        "type": "ScrollableBarModeOptions",
                        "required": False,
                        "description": "滚动模式下的选项。"
                    }
                }
            },
            "barWidth": {
                "description": "设置TabBar的宽度值。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "TabBar的宽度值。默认值：未设置SubTabBarStyle和BottomTabBarStyle的TabBar且vertical属性为False时，默认值为Tabs的宽度。未设置SubTabBarStyle和BottomTabBarStyle的TabBar且vertical属性为True时，默认值为56vp。设置SubTabBarStyle样式且vertical属性为False时，默认值为Tabs的宽度。设置SubTabBarStyle样式且vertical属性为True时，默认值为56vp。设置BottomTabBarStyle样式且vertical属性为True时，默认值为96vp。设置BottomTabBarStyle样式且vertical属性为False时，默认值为Tabs的宽度。"
                    }
                }
            },
            "barHeight": {
                "description": "设置TabBar的高度值。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "TabBar的高度值。"
                    }
                }
            },
            "animationDuration": {
                "description": "设置点击TabBar页签和调用TabsController的changeIndex接口切换TabContent的动画时长。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "动画时长。",
                        "default": 300
                    }
                }
            },
            "animationMode": {
                "description": "设置点击TabBar页签时切换TabContent的动画形式。",
                "params": {
                    "mode": {
                        "type": "Optional<AnimationMode>",
                        "required": True,
                        "description": "动画形式。",
                        "default": "AnimationMode.CONTENT_FIRST"
                    }
                }
            },
            "barPosition": {
                "description": "设置Tabs的页签位置。",
                "params": {
                    "value": {
                        "type": "BarPosition",
                        "required": True,
                        "description": "设置Tabs的页签位置。",
                        "default": "BarPosition.Start"
                    }
                }
            },
            "divider": {
                "description": "设置区分TabBar和TabContent的分割线样式。",
                "params": {
                    "value": {
                        "type": ["DividerStyle", "null"],
                        "required": True,
                        "description": "分割线样式。"
                    }
                }
            },
            "fadingEdge": {
                "description": "设置页签超过容器宽度时是否渐隐消失。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否渐隐消失。",
                        "default": True
                    }
                }
            },
            "barOverlap": {
                "description": "设置TabBar是否背后变模糊并叠加在TabContent之上。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否背后变模糊并叠加。",
                        "default": False
                    }
                }
            },
            "barBackgroundColor": {
                "description": "设置TabBar的背景颜色。",
                "params": {
                    "value": {
                        "type": "ResourceColor",
                        "required": True,
                        "description": "背景颜色。",
                        "default": "Color.Transparent"
                    }
                }
            },
            "barBackgroundBlurStyle": {
                "description": "设置TabBar的背景模糊材质。",
                "params": {
                    "value": {
                        "type": "BlurStyle",
                        "required": True,
                        "description": "背景模糊材质。",
                        "default": "BlurStyle.NONE"
                    }
                }
            },
            "barGridAlign": {
                "description": "以栅格化方式设置TabBar的可见区域。",
                "params": {
                    "value": {
                        "type": "BarGridColumnOptions",
                        "required": True,
                        "description": "栅格化方式设置的选项。"
                    }
                }
            },
            "edgeEffect": {
                "description": "设置边缘回弹效果。",
                "params": {
                    "edgeEffect": {
                        "type": "Optional<EdgeEffect>",
                        "required": True,
                        "description": "边缘滑动效果。",
                        "default": "EdgeEffect.Spring"
                    }
                }
            },
        },
        "events": {
            "onChange": {
                "description": "Tab页签切换后触发的事件。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示的index索引，索引从0开始计算。"
                    }
                }
            },
            "onTabBarClick": {
                "description": "Tab页签点击后触发的事件。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "被点击的index索引，索引从0开始计算。"
                    }
                }
            },
            "onAnimationStart": {
                "description": "切换动画开始时触发该回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示元素的索引。"
                    },
                    "targetIndex": {
                        "type": "number",
                        "required": True,
                        "description": "切换动画目标元素的索引。"
                    },
                    "event": {
                        "type": "TabsAnimationEvent",
                        "required": True,
                        "description": "动画相关信息。"
                    }
                }
            },
            "onAnimationEnd": {
                "description": "切换动画结束时触发该回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示元素的索引。"
                    },
                    "event": {
                        "type": "TabsAnimationEvent",
                        "required": True,
                        "description": "动画相关信息。"
                    }
                }
            },
            "onGestureSwipe": {
                "description": "在页面跟手滑动过程中，逐帧触发该回调。",
                "params": {
                    "index": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示元素的索引。"
                    },
                    "event": {
                        "type": "TabsAnimationEvent",
                        "required": True,
                        "description": "动画相关信息。"
                    }
                }
            },
            "customContentTransition": {
                "description": "自定义Tabs页面切换动画。",
                "params": {
                    "from": {
                        "type": "number",
                        "required": True,
                        "description": "动画开始时，当前页面的index值。"
                    },
                    "to": {
                        "type": "number",
                        "required": True,
                        "description": "动画开始时，目标页面的index值。"
                    }
                },
                "returns": {
                    "type": "TabContentAnimatedTransition",
                    "description": "自定义切换动画相关信息。"
                }
            },
            "onContentWillChange": {
                "description": "自定义Tabs页面切换拦截事件能力，新页面即将显示时触发该回调。",
                "params": {
                    "currentIndex": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示页面的index索引，索引从0开始计算。"
                    },
                    "comingIndex": {
                        "type": "number",
                        "required": True,
                        "description": "将要显示的新页面的index索引。"
                    }
                },
                "returns": {
                    "type": "boolean",
                    "description": "当回调函数handler的返回值为True时，Tabs可以切换到新页面。当回调函数handler的返回值为False时，Tabs无法切换到新页面，仍然显示原来页面内容。"
                }
            }
        },
        "examples": [
            """/*\n实现思路：\n本示例展示了如何通过一个按钮控制TabBar是否背后变模糊并叠加在TabContent之上。通过@State装饰器管理barOverlap和barBackgroundColor的状态，并在按钮点击事件中切换barOverlap的状态。Tabs组件的barOverlap属性根据barOverlap状态进行更新，从而实现TabBar的模糊和叠加效果。\n\n总体功能与效果描述：\n用户可以通过点击按钮来切换TabBar的模糊和叠加效果。TabBar的颜色和TabContent的内容会根据barOverlap的状态进行相应的调整。\n*/\n\n// barBackgroundColorTest.ets\n@Entry\n@Component\nstruct barBackgroundColorTest {\n  private controller: TabsController = new TabsController()\n  @State barOverlap: boolean = True; // 管理TabBar是否背后变模糊并叠加在TabContent之上的状态\n  @State barBackgroundColor: string = '#88888888'; // 管理TabBar的背景颜色\n\n  build() {\n    Column() {\n      Button("barOverlap变化").width('100%').margin({ bottom: '12vp' })\n        .onClick((event?: ClickEvent) => {\n          // 点击按钮切换barOverlap的状态\n          if (this.barOverlap) {\n            this.barOverlap = False;\n          } else {\n            this.barOverlap = True;\n          }\n        })\n\n      Tabs({ barPosition: BarPosition.Start, index: 0, controller: this.controller }) {\n        TabContent() {\n          Column() {\n            Text(`barOverlap ${this.barOverlap}`).fontSize(16).margin({ top: this.barOverlap ? '56vp' : 0 })\n            Text(`barBackgroundColor ${this.barBackgroundColor}`).fontSize(16)\n          }.width('100%').height('100%')\n          .backgroundColor(Color.Pink)\n        }\n        .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), "1"))\n\n        TabContent() {\n          Column() {\n            Text(`barOverlap ${this.barOverlap}`).fontSize(16).margin({ top: this.barOverlap ? '56vp' : 0 })\n            Text(`barBackgroundColor ${this.barBackgroundColor}`).fontSize(16)\n          }.width('100%').height('100%')\n          .backgroundColor(Color.Yellow)\n        }\n        .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), "2"))\n\n        TabContent() {\n          Column() {\n            Text(`barOverlap ${this.barOverlap}`).fontSize(16).margin({ top: this.barOverlap ? '56vp' : 0 })\n            Text(`barBackgroundColor ${this.barBackgroundColor}`).fontSize(16)\n          }.width('100%').height('100%')\n          .backgroundColor(Color.Green)\n        }\n        .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), "3"))\n      }\n      .vertical(False)\n      .barMode(BarMode.Fixed)\n      .height('60%')\n      .barOverlap(this.barOverlap) // 根据barOverlap状态设置TabBar是否背后变模糊并叠加在TabContent之上\n      .scrollable(True)\n      .animationDuration(10)\n      .barBackgroundColor(this.barBackgroundColor) // 设置TabBar的背景颜色\n    }\n    .height(500)\n    .padding({ top: '24vp', left: '24vp', right: '24vp' })\n  }\n}""",
            """/*\n实现思路：\n本示例通过自定义TabBar和TabContent的联动，展示如何在切换Tab时动态改变TabBar的样式和内容。通过@State装饰器管理当前选中的Tab索引，并使用@Builder装饰器生成自定义的TabBar内容。\n\n总体功能与效果描述：\n示例展示了四个Tab，每个Tab有不同的背景颜色和标签名称。切换Tab时，TabBar的文本颜色和下划线会根据当前选中的Tab动态变化。\n*/\n\n// TabsExample.ets\n@Entry\n@Component\nstruct TabsExample {\n  @State fontColor: string = '#182431' // 默认字体颜色\n  @State selectedFontColor: string = '#007DFF' // 选中Tab的字体颜色\n  @State currentIndex: number = 0 // 当前选中的Tab索引\n  private controller: TabsController = new TabsController() // Tabs控制器\n\n  // 自定义TabBar构建器\n  @Builder tabBuilder(index: number, name: string) {\n    Column() {\n      Text(name)\n        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor) // 根据当前选中的Tab设置字体颜色\n        .fontSize(16)\n        .fontWeight(this.currentIndex === index ? 500 : 400) // 根据当前选中的Tab设置字体粗细\n        .lineHeight(22)\n        .margin({ top: 17, bottom: 7 })\n      Divider()\n        .strokeWidth(2)\n        .color('#007DFF')\n        .opacity(this.currentIndex === index ? 1 : 0) // 根据当前选中的Tab设置下划线的可见性\n    }.width('100%')\n  }\n\n  build() {\n    Column() {\n      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor('#00CB87') // 第一个Tab的内容，背景颜色为绿色\n        }.tabBar(this.tabBuilder(0, 'green'))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor('#007DFF') // 第二个Tab的内容，背景颜色为蓝色\n        }.tabBar(this.tabBuilder(1, 'blue'))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor('#FFBF00') // 第三个Tab的内容，背景颜色为黄色\n        }.tabBar(this.tabBuilder(2, 'yellow'))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor('#E67C92') // 第四个Tab的内容，背景颜色为粉色\n        }.tabBar(this.tabBuilder(3, 'pink'))\n      }\n      .vertical(False) // 设置TabBar为水平布局\n      .barMode(BarMode.Fixed) // 设置TabBar为固定模式\n      .barWidth(360) // 设置TabBar的宽度\n      .barHeight(56) // 设置TabBar的高度\n      .animationDuration(400) // 设置切换Tab时的动画持续时间\n      .onChange((index: number) => {\n        this.currentIndex = index // 更新当前选中的Tab索引\n      })\n      .width(360)\n      .height(296)\n      .margin({ top: 52 })\n      .backgroundColor('#F1F3F5') // 设置整体背景颜色\n    }.width('100%')\n  }\n}""",
            """/*\n实现思路：\n本示例通过使用Tabs组件和TabsController来实现一个具有多个标签页的界面，并利用preloadItems接口预加载指定的标签页内容，以优化用户体验。\n\n总体功能与效果描述：\n- 展示一个包含四个标签页的界面，每个标签页显示一个不同颜色的MyComponent组件。\n- 提供一个按钮，点击后预加载指定索引的标签页内容（索引为0、2、3的标签页）。\n- 通过TabsController的preloadItems方法实现预加载功能，并在控制台输出预加载成功或失败的信息。\n*/\n\n// TabsPreloadItems.ets\nimport { BusinessError } from '@kit.BasicServicesKit'\n\n@Entry\n@Component\nstruct TabsPreloadItems {\n  @State currentIndex: number = 1 // 当前选中的标签页索引，默认为1\n  private tabsController: TabsController = new TabsController() // 创建TabsController实例，用于控制标签页\n\n  build() {\n    Column() {\n      Tabs({ index: this.currentIndex, controller: this.tabsController }) {\n        TabContent() {\n          MyComponent({ color: '#00CB87' }) // 第一个标签页内容，显示绿色背景的MyComponent组件\n        }.tabBar(SubTabBarStyle.of('green')) // 设置标签页的样式为绿色\n\n        TabContent() {\n          MyComponent({ color: '#007DFF' }) // 第二个标签页内容，显示蓝色背景的MyComponent组件\n        }.tabBar(SubTabBarStyle.of('blue')) // 设置标签页的样式为蓝色\n\n        TabContent() {\n          MyComponent({ color: '#FFBF00' }) // 第三个标签页内容，显示黄色背景的MyComponent组件\n        }.tabBar(SubTabBarStyle.of('yellow')) // 设置标签页的样式为黄色\n\n        TabContent() {\n          MyComponent({ color: '#E67C92' }) // 第四个标签页内容，显示粉色背景的MyComponent组件\n        }.tabBar(SubTabBarStyle.of('pink')) // 设置标签页的样式为粉色\n      }\n      .width(360) // 设置Tabs组件的宽度\n      .height(296) // 设置Tabs组件的高度\n      .backgroundColor('#F1F3F5') // 设置Tabs组件的背景颜色\n      .onChange((index: number) => {\n        this.currentIndex = index // 当标签页切换时，更新当前选中的标签页索引\n      })\n\n      Button('preload items: [0, 2, 3]') // 创建一个按钮，点击后预加载指定索引的标签页内容\n        .margin(5) // 设置按钮的外边距\n        .onClick(() => {\n          this.tabsController.preloadItems([0, 2, 3]) // 调用preloadItems方法预加载索引为0、2、3的标签页内容\n            .then(() => {\n              console.info('preloadItems success.') // 预加载成功时在控制台输出信息\n            })\n            .catch((error: BusinessError) => {\n              console.error('preloadItems failed, error code: ' + error.code + ', error message: ' + error.message) // 预加载失败时在控制台输出错误信息\n            })\n        })\n    }\n  }\n}\n\n@Component\nstruct MyComponent {\n  private color: string = "" // 组件的背景颜色\n\n  aboutToAppear(): void {\n    console.info('aboutToAppear backgroundColor:' + this.color) // 组件即将显示时在控制台输出背景颜色\n  }\n\n  aboutToDisappear(): void {\n    console.info('aboutToDisappear backgroundColor:' + this.color) // 组件即将消失时在控制台输出背景颜色\n  }\n\n  build() {\n    Column()\n      .width('100%') // 设置组件的宽度为100%\n      .height('100%') // 设置组件的高度为100%\n      .backgroundColor(this.color) // 设置组件的背景颜色\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何使用鸿蒙ArkUI框架创建一个带有自定义手势滑动切换拦截的Tabs组件。通过@State装饰器管理当前选中的Tab索引，使用@Builder装饰器创建TabBar的内容，并在Tabs组件上设置各种属性和事件处理器来实现功能。\n\n总体功能与效果描述：\n1. 创建一个包含四个Tab的Tabs组件，每个Tab显示不同的内容和背景颜色。\n2. 通过自定义的tabBuilder方法动态生成TabBar的内容，根据当前选中的Tab索引改变文本颜色。\n3. 实现手势滑动切换Tab的功能，并通过onContentWillChange事件拦截特定Tab的切换。\n4. 提供两个按钮，一个用于动态修改当前Tab索引，另一个用于通过TabsController控制Tab索引的切换。\n*/\n\n// TabsExample.ets\n@Entry\n@Component\nstruct TabsExample {\n  @State currentIndex: number = 2 // 初始化当前选中的Tab索引为2\n  private controller: TabsController = new TabsController() // 创建TabsController实例\n\n  // 定义一个Builder方法用于生成TabBar的内容\n  @Builder tabBuilder(title: string, targetIndex: number) {\n    Column() {\n      Text(title).fontColor(this.currentIndex === targetIndex ? '#1698CE' : '#6B6B6B') // 根据当前选中的Tab索引改变文本颜色\n    }.width('100%')\n     .height(50)\n     .justifyContent(FlexAlign.Center)\n  }\n\n  build() {\n    Column() {\n      Tabs({ barPosition: BarPosition.End, controller: this.controller, index: this.currentIndex }) {\n        TabContent() {\n          Column() {\n            Text('首页的内容')\n          }.width('100%').height('100%').backgroundColor('#00CB87').justifyContent(FlexAlign.Center)\n        }.tabBar(this.tabBuilder('首页', 0))\n\n        TabContent() {\n          Column() {\n            Text('发现的内容')\n          }.width('100%').height('100%').backgroundColor('#007DFF').justifyContent(FlexAlign.Center)\n        }.tabBar(this.tabBuilder('发现', 1))\n\n        TabContent() {\n          Column() {\n            Text('推荐的内容')\n          }.width('100%').height('100%').backgroundColor('#FFBF00').justifyContent(FlexAlign.Center)\n        }.tabBar(this.tabBuilder('推荐', 2))\n\n        TabContent() {\n          Column() {\n            Text('我的内容')\n          }.width('100%').height('100%').backgroundColor('#E67C92').justifyContent(FlexAlign.Center)\n        }.tabBar(this.tabBuilder('我的', 3))\n      }\n      .vertical(False) // 设置Tabs为水平布局\n      .barMode(BarMode.Fixed) // 设置TabBar为固定模式\n      .barWidth(360) // 设置TabBar的宽度\n      .barHeight(60) // 设置TabBar的高度\n      .animationDuration(0) // 禁用切换动画\n      .onChange((index: number) => {\n        this.currentIndex = index // 更新当前选中的Tab索引\n      })\n      .width(360) // 设置Tabs组件的宽度\n      .height(600) // 设置Tabs组件的高度\n      .backgroundColor('#F1F3F5') // 设置Tabs组件的背景颜色\n      .scrollable(True) // 设置Tabs组件可滚动\n      .onContentWillChange((currentIndex, comingIndex) => {\n        if (comingIndex == 2) {\n          return False // 拦截切换到索引为2的Tab\n        }\n        return True // 允许其他Tab的切换\n      })\n\n      Button('动态修改index').width('50%').margin({ top: 20 })\n        .onClick(() => {\n          this.currentIndex = (this.currentIndex + 1) % 4 // 动态修改当前选中的Tab索引\n        })\n\n      Button('changeIndex').width('50%').margin({ top: 20 })\n        .onClick(() => {\n          this.currentIndex = (this.currentIndex + 1) % 4 // 动态修改当前选中的Tab索引\n          this.controller.changeIndex(this.currentIndex) // 通过TabsController控制Tab索引的切换\n        })\n    }.width('100%')\n  }\n}""",
            """/*\n实现思路：\n本示例通过自定义的TabContentAnimatedTransition实现Tabs页面的切换动画。每个Tab页面的内容在切换时会有缩放和透明度的变化。通过设置不同的持续时间和延迟时间，实现渐进式的动画效果。\n\n总体功能与效果描述：\n示例展示了如何使用自定义的TabContentAnimatedTransition来实现Tabs页面的切换动画。每个Tab页面的内容在切换时会有缩放和透明度的变化，从而实现平滑的过渡效果。\n*/\n\n// TabsCustomAnimationExample.ets\n\n// 定义一个接口来描述Tab页面的数据结构\ninterface itemType {\n  text: string, // Tab页面的文本标签\n  backgroundColor: Color // Tab页面的背景颜色\n}\n\n@Entry\n@Component\nstruct TabsCustomAnimationExample {\n  @State data: itemType[] = [\n    {\n      text: 'Red',\n      backgroundColor: Color.Red\n    },\n    {\n      text: 'Yellow',\n      backgroundColor: Color.Yellow\n    },\n    {\n      text: 'Blue',\n      backgroundColor: Color.Blue\n    }\n  ]\n  @State opacityList: number[] = [] // 存储每个Tab页面的透明度值\n  @State scaleList: number[] = [] // 存储每个Tab页面的缩放值\n\n  private durationList: number[] = [] // 存储每个Tab页面的动画持续时间\n  private timeoutList: number[] = [] // 存储每个Tab页面的动画延迟时间\n\n  // 定义自定义的TabContentAnimatedTransition\n  private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition = (from: number, to: number) => {\n    let tabContentAnimatedTransition = {\n      timeout: this.timeoutList[from], // 设置动画延迟时间\n      transition: (proxy: TabContentTransitionProxy) => {\n        this.scaleList[from] = 1.0 // 设置起始Tab页面的初始缩放值\n        this.scaleList[to] = 0.5 // 设置目标Tab页面的初始缩放值\n        this.opacityList[from] = 1.0 // 设置起始Tab页面的初始透明度值\n        this.opacityList[to] = 0.5 // 设置目标Tab页面的初始透明度值\n        animateTo({\n          duration: this.durationList[from], // 设置动画持续时间\n          onFinish: () => {\n            proxy.finishTransition() // 动画完成后调用finishTransition方法\n          }\n        }, () => {\n          this.scaleList[from] = 0.5 // 设置起始Tab页面的最终缩放值\n          this.scaleList[to] = 1.0 // 设置目标Tab页面的最终缩放值\n          this.opacityList[from] = 0.5 // 设置起始Tab页面的最终透明度值\n          this.opacityList[to] = 1.0 // 设置目标Tab页面的最终透明度值\n        })\n      }\n    } as TabContentAnimatedTransition\n    return tabContentAnimatedTransition\n  }\n\n  // 组件初始化时设置动画参数\n  aboutToAppear(): void {\n    let duration = 1000\n    let timeout = 1000\n    for (let i = 1; i <= this.data.length; i++) {\n      this.opacityList.push(1.0) // 初始化透明度值\n      this.scaleList.push(1.0) // 初始化缩放值\n      this.durationList.push(duration * i) // 设置动画持续时间\n      this.timeoutList.push(timeout * i) // 设置动画延迟时间\n    }\n  }\n\n  build() {\n    Column() {\n      Tabs() {\n        ForEach(this.data, (item: itemType, index: number) => {\n          TabContent() {}\n            .tabBar(item.text) // 设置Tab页面的文本标签\n            .backgroundColor(item.backgroundColor) // 设置Tab页面的背景颜色\n            .opacity(this.opacityList[index]) // 设置Tab页面的透明度\n            .scale({ x: this.scaleList[index], y: this.scaleList[index] }) // 设置Tab页面的缩放\n        })\n      }\n      .backgroundColor(0xf1f3f5) // 设置Tabs组件的背景颜色\n      .width('100%') // 设置Tabs组件的宽度\n      .height(500) // 设置Tabs组件的高度\n      .customContentTransition(this.customContentTransition) // 设置自定义的TabContentAnimatedTransition\n    }\n  }\n}""",
            """/*\n实现思路：\n本示例通过创建一个包含多个Tab的Tabs组件，展示了如何通过按钮动态调整TabBar的栅格布局参数（如margin和gutter），以及如何响应TabBar的点击事件。\n\n总体功能与效果描述：\n1. 通过按钮调整TabBar的栅格布局参数（margin和gutter）。\n2. 通过按钮调整TabBar的栅格列数（sm）。\n3. 响应TabBar的点击事件，并在文本框中显示点击的Tab索引。\n*/\n\n// TabsExample5.ets\n@Entry\n@Component\nstruct TabsExample5 {\n  private controller: TabsController = new TabsController()\n  @State gridMargin: number = 10 // 初始化TabBar的margin值\n  @State gridGutter: number = 10 // 初始化TabBar的gutter值\n  @State sm: number = -2 // 初始化TabBar的栅格列数\n  @State clickedContent: string = "" // 用于存储TabBar点击事件的文本内容\n\n  build() {\n    Column() {\n      // 按钮组用于调整TabBar的margin值\n      Row() {\n        Button("gridMargin+10 " + this.gridMargin)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.gridMargin += 10 // 增加TabBar的margin值\n          })\n          .margin({ right: '6%', bottom: '12vp' })\n        Button("gridMargin-10 " + this.gridMargin)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.gridMargin -= 10 // 减少TabBar的margin值\n          })\n          .margin({ bottom: '12vp' })\n      }\n\n      // 按钮组用于调整TabBar的gutter值\n      Row() {\n        Button("gridGutter+10 " + this.gridGutter)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.gridGutter += 10 // 增加TabBar的gutter值\n          })\n          .margin({ right: '6%', bottom: '12vp' })\n        Button("gridGutter-10 " + this.gridGutter)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.gridGutter -= 10 // 减少TabBar的gutter值\n          })\n          .margin({ bottom: '12vp' })\n      }\n\n      // 按钮组用于调整TabBar的栅格列数\n      Row() {\n        Button("sm+2 " + this.sm)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.sm += 2 // 增加TabBar的栅格列数\n          })\n          .margin({ right: '6%' })\n        Button("sm-2 " + this.sm).width('47%').height(50).margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.sm -= 2 // 减少TabBar的栅格列数\n          })\n      }\n\n      // 显示TabBar点击事件的文本内容\n      Text("点击内容:" + this.clickedContent).width('100%').height(200).margin({ top: 5 })\n\n      // Tabs组件，包含三个TabContent\n      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Pink)\n        }.tabBar(BottomTabBarStyle.of($r("sys.media.ohos_app_icon"), "1"))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar(BottomTabBarStyle.of($r("sys.media.ohos_app_icon"), "2"))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Blue)\n        }.tabBar(BottomTabBarStyle.of($r("sys.media.ohos_app_icon"), "3"))\n      }\n      .width('350vp')\n      .animationDuration(300)\n      .height('60%')\n      .barGridAlign({ sm: this.sm, margin: this.gridMargin, gutter: this.gridGutter })\n      .backgroundColor(0xf1f3f5)\n      .onTabBarClick((index: number) => {\n        this.clickedContent += "now index " + index + " is clicked\n" // 响应TabBar点击事件，并更新文本内容\n      })\n    }\n    .width('100%')\n    .height(500)\n    .margin({ top: 5 })\n    .padding('10vp')\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中使用Tabs组件，并通过按钮控制Tabs的滚动边距和布局样式。主要功能包括：\n1. 通过按钮增加或减少滚动边距。\n2. 通过按钮改变文本内容。\n3. 通过按钮切换不同的布局样式。\n4. 使用Tabs组件展示不同内容的标签页。\n\n总体功能与效果描述：\n用户可以通过点击不同的按钮来动态调整Tabs组件的滚动边距和布局样式，同时可以改变标签页的文本内容。Tabs组件支持滚动模式，并可以根据设置的布局样式和滚动边距进行动态调整。\n*/\n\n// TabsExample6.ets\n@Entry\n@Component\nstruct TabsExample6 {\n  private controller: TabsController = new TabsController()\n  @State scrollMargin: number = 0 // 定义滚动边距的初始值\n  @State layoutStyle: LayoutStyle = LayoutStyle.ALWAYS_CENTER // 定义布局样式的初始值\n  @State text: string = "文本" // 定义文本内容的初始值\n\n  build() {\n    Column() {\n      Row() {\n        Button("scrollMargin+10 " + this.scrollMargin)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.scrollMargin += 10 // 点击按钮增加滚动边距\n          })\n          .margin({ right: '6%', bottom: '12vp' })\n        Button("scrollMargin-10 " + this.scrollMargin)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.scrollMargin -= 10 // 点击按钮减少滚动边距\n          })\n          .margin({ bottom: '12vp' })\n      }\n\n      Row() {\n        Button("文本增加 ")\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.text += '文本增加' // 点击按钮增加文本内容\n          })\n          .margin({ right: '6%', bottom: '12vp' })\n        Button("文本重置")\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.text = "文本" // 点击按钮重置文本内容\n          })\n          .margin({ bottom: '12vp' })\n      }\n\n      Row() {\n        Button("layoutStyle.ALWAYS_CENTER")\n          .width('100%')\n          .height(50)\n          .margin({ top: 5 })\n          .fontSize(15)\n          .onClick((event?: ClickEvent) => {\n            this.layoutStyle = LayoutStyle.ALWAYS_CENTER; // 点击按钮设置布局样式为中心对齐\n          })\n          .margin({ bottom: '12vp' })\n      }\n\n      Row() {\n        Button("layoutStyle.ALWAYS_AVERAGE_SPLIT")\n          .width('100%')\n          .height(50)\n          .margin({ top: 5 })\n          .fontSize(15)\n          .onClick((event?: ClickEvent) => {\n            this.layoutStyle = LayoutStyle.ALWAYS_AVERAGE_SPLIT; // 点击按钮设置布局样式为平均分割\n          })\n          .margin({ bottom: '12vp' })\n      }\n\n      Row() {\n        Button("layoutStyle.SPACE_BETWEEN_OR_CENTER")\n          .width('100%')\n          .height(50)\n          .margin({ top: 5 })\n          .fontSize(15)\n          .onClick((event?: ClickEvent) => {\n            this.layoutStyle = LayoutStyle.SPACE_BETWEEN_OR_CENTER; // 点击按钮设置布局样式为间距均匀或中心对齐\n          })\n          .margin({ bottom: '12vp' })\n      }\n\n      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Pink)\n        }.tabBar(SubTabBarStyle.of(this.text))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar(SubTabBarStyle.of(this.text))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Blue)\n        }.tabBar(SubTabBarStyle.of(this.text))\n      }\n      .animationDuration(300)\n      .height('60%')\n      .backgroundColor(0xf1f3f5)\n      .barMode(BarMode.Scrollable, { margin: this.scrollMargin, nonScrollableLayoutStyle: this.layoutStyle })\n      // 设置Tabs组件的滚动模式，并根据当前的滚动边距和布局样式进行配置\n    }\n    .width('100%')\n    .height(500)\n    .margin({ top: 5 })\n    .padding('24vp')\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何通过设置 `fadingEdge` 属性来控制 Tabs 组件在切换子页签时的渐隐效果。通过两个按钮来切换 `fadingEdge` 属性的值，从而实现子页签的渐隐和不渐隐效果。\n\n总体功能与效果描述：\n用户可以通过点击按钮来控制 Tabs 组件的子页签在切换时是否显示渐隐效果。Tabs 组件支持水平和垂直方向的滚动，并且可以设置不同的页签栏位置和样式。\n*/\n\n// TabsOpaque.ets\n@Entry\n@Component\nstruct TabsOpaque {\n  @State message: string = 'Hello World' // 初始化状态消息\n  private controller: TabsController = new TabsController() // 创建第一个 Tabs 控制器\n  private controller1: TabsController = new TabsController() // 创建第二个 Tabs 控制器\n  @State selfFadingFade: boolean = True; // 控制渐隐效果的状态变量\n\n  build() {\n    Column() {\n      Button('子页签设置渐隐').width('100%').margin({ bottom: '12vp' })\n        .onClick((event?: ClickEvent) => {\n          this.selfFadingFade = True; // 设置渐隐效果\n        })\n      Button('子页签设置不渐隐').width('100%').margin({ bottom: '12vp' })\n        .onClick((event?: ClickEvent) => {\n          this.selfFadingFade = False; // 取消渐隐效果\n        })\n      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Pink)\n        }.tabBar('pink')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Yellow)\n        }.tabBar('yellow')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Blue)\n        }.tabBar('blue')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar('green')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar('green')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar('green')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar('green')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar('green')\n      }\n      .vertical(False) // 设置 Tabs 水平方向\n      .scrollable(True) // 设置 Tabs 可滚动\n      .barMode(BarMode.Scrollable) // 设置页签栏可滚动\n      .barHeight(80) // 设置页签栏高度\n      .animationDuration(400) // 设置动画持续时间\n      .onChange((index: number) => {\n        console.info(index.toString()) // 打印当前选中的页签索引\n      })\n      .fadingEdge(this.selfFadingFade) // 设置渐隐效果\n      .height('30%') // 设置 Tabs 高度\n      .width('100%') // 设置 Tabs 宽度\n\n      Tabs({ barPosition: BarPosition.Start, controller: this.controller1 }) {\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Pink)\n        }.tabBar('pink')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Yellow)\n        }.tabBar('yellow')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Blue)\n        }.tabBar('blue')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar('green')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar('green')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar('green')\n      }\n      .vertical(True) // 设置 Tabs 垂直方向\n      .scrollable(True) // 设置 Tabs 可滚动\n      .barMode(BarMode.Scrollable) // 设置页签栏可滚动\n      .barHeight(200) // 设置页签栏高度\n      .barWidth(80) // 设置页签栏宽度\n      .animationDuration(400) // 设置动画持续时间\n      .onChange((index: number) => {\n        console.info(index.toString()) // 打印当前选中的页签索引\n      })\n      .fadingEdge(this.selfFadingFade) // 设置渐隐效果\n      .height('30%') // 设置 Tabs 高度\n      .width('100%') // 设置 Tabs 宽度\n    }\n    .padding({ top: '24vp', left: '24vp', right: '24vp' }) // 设置内边距\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何使用Tabs组件和Divider属性来创建一个具有多个标签页的应用，每个标签页包含不同颜色的内容，并且可以通过按钮动态调整分割线的属性。\n总体功能与效果描述：\n用户可以通过点击不同的按钮来改变分割线的颜色、宽度、上下边距，甚至隐藏分割线。每个标签页的内容颜色不同，且标签页可以垂直滚动。\n*/\n\n// TabsDivider1.ets\n@Entry\n@Component\nstruct TabsDivider1 {\n  private controller1: TabsController = new TabsController() // 创建一个Tabs控制器\n  @State dividerColor: string = 'red' // 分割线颜色状态变量，初始为红色\n  @State strokeWidth: number = 2 // 分割线宽度状态变量，初始为2\n  @State startMargin: number = 0 // 分割线上边距状态变量，初始为0\n  @State endMargin: number = 0 // 分割线下边距状态变量，初始为0\n  @State nullFlag: boolean = False // 是否隐藏分割线的标志状态变量，初始为False\n\n  build() {\n    Column() {\n      Tabs({ controller: this.controller1 }) { // 创建一个Tabs组件，使用controller1控制\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Pink) // 创建一个粉色背景的标签页内容\n        }.tabBar('pink') // 设置标签页的标题为'pink'\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Yellow) // 创建一个黄色背景的标签页内容\n        }.tabBar('yellow') // 设置标签页的标题为'yellow'\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Blue) // 创建一个蓝色背景的标签页内容\n        }.tabBar('blue') // 设置标签页的标题为'blue'\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green) // 创建一个绿色背景的标签页内容\n        }.tabBar('green') // 设置标签页的标题为'green'\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Red) // 创建一个红色背景的标签页内容\n        }.tabBar('red') // 设置标签页的标题为'red'\n      }\n      .vertical(True) // 设置Tabs为垂直布局\n      .scrollable(True) // 设置Tabs可滚动\n      .barMode(BarMode.Fixed) // 设置标签栏模式为固定\n      .barWidth(70) // 设置标签栏宽度为70\n      .barHeight(200) // 设置标签栏高度为200\n      .animationDuration(400) // 设置切换动画时长为400毫秒\n      .onChange((index: number) => { // 监听标签页切换事件\n        console.info(index.toString()) // 打印当前选中的标签页索引\n      })\n      .height('200vp') // 设置Tabs高度为200vp\n      .margin({ bottom: '12vp' }) // 设置Tabs底部外边距为12vp\n      .divider(this.nullFlag ? null : { // 设置分割线属性，如果nullFlag为True则隐藏分割线\n        strokeWidth: this.strokeWidth, // 分割线宽度\n        color: this.dividerColor, // 分割线颜色\n        startMargin: this.startMargin, // 分割线上边距\n        endMargin: this.endMargin // 分割线下边距\n      })\n\n      Button('常规Divider').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后恢复分割线的常规设置\n        .onClick(() => {\n          this.nullFlag = False; // 显示分割线\n          this.strokeWidth = 2; // 设置分割线宽度为2\n          this.dividerColor = 'red'; // 设置分割线颜色为红色\n          this.startMargin = 0; // 设置分割线上边距为0\n          this.endMargin = 0; // 设置分割线下边距为0\n        })\n      Button('空Divider').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后隐藏分割线\n        .onClick(() => {\n          this.nullFlag = True // 隐藏分割线\n        })\n      Button('颜色变为蓝色').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后将分割线颜色变为蓝色\n        .onClick(() => {\n          this.dividerColor = 'blue' // 设置分割线颜色为蓝色\n        })\n      Button('宽度增加').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后增加分割线宽度\n        .onClick(() => {\n          this.strokeWidth += 2 // 增加分割线宽度\n        })\n      Button('宽度减小').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后减少分割线宽度\n        .onClick(() => {\n          if (this.strokeWidth > 2) { // 如果分割线宽度大于2\n            this.strokeWidth -= 2 // 减少分割线宽度\n          }\n        })\n      Button('上边距增加').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后增加分割线上边距\n        .onClick(() => {\n          this.startMargin += 2 // 增加分割线上边距\n        })\n      Button('上边距减少').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后减少分割线上边距\n        .onClick(() => {\n          if (this.startMargin > 2) { // 如果分割线上边距大于2\n            this.startMargin -= 2 // 减少分割线上边距\n          }\n        })\n      Button('下边距增加').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后增加分割线下边距\n        .onClick(() => {\n          this.endMargin += 2 // 增加分割线下边距\n        })\n      Button('下边距减少').width('100%').margin({ bottom: '12vp' }) // 创建一个按钮，点击后减少分割线下边距\n        .onClick(() => {\n          if (this.endMargin > 2) { // 如果分割线下边距大于2\n            this.endMargin -= 2 // 减少分割线下边距\n          }\n        })\n    }.padding({ top: '24vp', left: '24vp', right: '24vp' }) // 设置整体布局的内边距\n  }\n}""",
            """/*\n实现思路：\n本示例通过自定义TabBar的切换动画，利用onChange、onAnimationStart、onAnimationEnd、onGestureSwipe等接口实现Tab切换时的动画效果。通过@State装饰器管理当前选中的Tab索引、动画持续时间、指示器的位置和宽度等状态。使用@Builder装饰器创建TabBar的构建器，动态更新TabBar的样式和位置。通过自定义方法处理动画和手势事件，实现平滑的Tab切换效果。\n\n总体功能与效果描述：\n本示例展示了一个自定义TabBar组件，支持Tab切换时的动画效果。TabBar包含四个Tab，每个Tab对应不同的背景颜色。切换Tab时，底部指示器会平滑移动到目标Tab的位置，并根据手势滑动调整指示器的位置和宽度。\n*/\n\n// TabsExample.ets\nimport { ComponentUtils } from '@kit.ArkUI'\n\n@Entry\n@Component\nstruct TabsExample {\n  @State currentIndex: number = 0 // 当前选中的Tab索引\n  @State animationDuration: number = 300 // 动画持续时间\n  @State indicatorLeftMargin: number = 0 // 指示器的左边距\n  @State indicatorWidth: number = 0 // 指示器的宽度\n  private tabsWidth: number = 0 // TabBar的总宽度\n  private componentUtils: ComponentUtils = this.getUIContext().getComponentUtils() // 获取组件工具实例\n\n  @Builder\n  tabBuilder(index: number, name: string) {\n    Column() {\n      Text(name)\n        .fontSize(16)\n        .fontColor(this.currentIndex === index ? '#007DFF' : '#182431') // 根据当前选中的Tab设置字体颜色\n        .fontWeight(this.currentIndex === index ? 500 : 400) // 根据当前选中的Tab设置字体粗细\n        .id(index.toString())\n        .onAreaChange((oldValue: Area,newValue: Area) => {\n          if (this.currentIndex === index && (this.indicatorLeftMargin === 0 || this.indicatorWidth === 0)){\n            if (newValue.position.x != undefined) {\n              let positionX = Number.parseFloat(newValue.position.x.toString())\n              this.indicatorLeftMargin = Number.isNaN(positionX) ? 0 : positionX // 更新指示器的左边距\n            }\n            let width = Number.parseFloat(newValue.width.toString())\n            this.indicatorWidth = Number.isNaN(width) ? 0 : width // 更新指示器的宽度\n          }\n        })\n    }.width('100%')\n  }\n\n  build() {\n    Stack({ alignContent: Alignment.TopStart }) {\n      Tabs({ barPosition: BarPosition.Start }) {\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor('#00CB87')\n        }.tabBar(this.tabBuilder(0, 'green'))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor('#007DFF')\n        }.tabBar(this.tabBuilder(1, 'blue'))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor('#FFBF00')\n        }.tabBar(this.tabBuilder(2, 'yellow'))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor('#E67C92')\n        }.tabBar(this.tabBuilder(3, 'pink'))\n      }\n      .onAreaChange((oldValue: Area,newValue: Area)=> {\n        let width = Number.parseFloat(newValue.width.toString())\n        this.tabsWidth = Number.isNaN(width) ? 0 : width // 更新TabBar的总宽度\n      })\n      .barWidth('100%')\n      .barHeight(56)\n      .width('100%')\n      .height(296)\n      .backgroundColor('#F1F3F5')\n      .animationDuration(this.animationDuration)\n      .onChange((index: number) => {\n        this.currentIndex = index  // 更新当前选中的Tab索引\n      })\n      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {\n        this.currentIndex = targetIndex\n        let targetIndexInfo = this.getTextInfo(targetIndex)\n        this.startAnimateTo(this.animationDuration, targetIndexInfo.left, targetIndexInfo.width) // 开始动画\n      })\n      .onAnimationEnd((index: number,event: TabsAnimationEvent) => {\n        let currentIndicatorInfo = this.getCurrentIndicatorInfo(index,event)\n        this.startAnimateTo(0,currentIndicatorInfo.left,currentIndicatorInfo.width) // 动画结束\n      })\n      .onGestureSwipe((index: number,event: TabsAnimationEvent) => {\n        let currentIndicatorInfo = this.getCurrentIndicatorInfo(index,event)\n        this.currentIndex = currentIndicatorInfo.index\n        this.indicatorLeftMargin = currentIndicatorInfo.left\n        this.indicatorWidth = currentIndicatorInfo.width // 处理手势滑动\n      })\n\n      Column()\n        .height(2)\n        .width(this.indicatorWidth)\n        .margin({ left: this.indicatorLeftMargin, top:48})\n        .backgroundColor('#007DFF') // 底部指示器\n    }.width('100%')\n  }\n\n  private getTextInfo(index: number): Record<string, number> {\n    let rectangle = this.componentUtils.getRectangleById(index.toString())\n    return { 'left': px2vp(rectangle.windowOffset.x), 'width': px2vp(rectangle.size.width) } // 获取Tab文本的位置和宽度信息\n  }\n\n  private getCurrentIndicatorInfo(index: number, event: TabsAnimationEvent): Record<string, number> {\n    let nextIndex = index\n    if (index > 0 && event.currentOffset > 0) {\n      nextIndex--\n    } else if (index < 3 && event.currentOffset < 0) {\n      nextIndex++\n    }\n    let indexInfo = this.getTextInfo(index)\n    let nextIndexInfo = this.getTextInfo(nextIndex)\n    let swipeRatio = Math.abs(event.currentOffset / this.tabsWidth)\n    let currentIndex = swipeRatio > 0.5 ? nextIndex : index \n    let currentLeft = indexInfo.left + (nextIndexInfo.left - indexInfo.left) * swipeRatio\n    let currentWidth = indexInfo.width + (nextIndexInfo.width - indexInfo.width) * swipeRatio\n    return { 'index': currentIndex, 'left': currentLeft, 'width': currentWidth } // 获取当前指示器的位置和宽度信息\n  }\n\n  private startAnimateTo(duration: number, leftMargin: number, width: number) {\n    animateTo({\n      duration: duration, \n      curve: Curve.Linear, \n      iterations: 1, \n      playMode: PlayMode.Normal, \n      onFinish: () => {\n        console.info('play end')\n      }\n    }, () => {\n      this.indicatorLeftMargin = leftMargin\n      this.indicatorWidth = width // 执行动画\n    })\n  }\n}"""
        ]
    },
    "TabContent": {
        "description": "仅在Tabs中使用，对应一个切换页签的内容视图，支持单个子组件。",
        "interfaces": [
            {
                "description": "TabContent()",
                "params": {}
            }
        ],
        "attributes": {
            "tabBar": {
                "description": "设置TabBar上显示内容。",
                "params": {
                    "value": {
                        "type": ["string", "Resource", "CustomBuilder", "object"],
                        "required": True,
                        "description": "TabBar上显示的内容。如果icon采用svg格式图源，则要求svg图源删除其自有宽高属性值。如采用带有自有宽高属性的svg图源，icon大小则是svg本身内置的宽高属性值大小。设置的内容超出tabbar页签时进行裁切。"
                    }
                }
            },

        },
        "events": {
            "onWillShow": {
                "description": "逻辑回调，TabContent将要显示的时候触发该回调。场景包括TabContent首次显示，TabContent切换，页面切换，窗口前后台切换。",
                "params": {}
            },
            "onWillHide": {
                "description": "逻辑回调，TabContent将要隐藏的时候触发该回调。场景包括TabContent切换，页面切换，窗口前后台切换。",
                "params": {}
            }
        },
        "examples": [
            """/*\n实现思路：\n本示例展示了如何使用鸿蒙ArkUI框架创建一个带有自定义标签栏的垂直选项卡组件。通过使用@State装饰器来管理标签栏的颜色和当前选中的索引，以及使用@Builder装饰器来动态生成标签栏的内容。Tabs组件用于创建选项卡界面，并通过TabsController来管理选项卡的状态。\n\n总体功能与效果描述：\n该组件实现了一个垂直的选项卡界面，每个选项卡包含一个图标和一个文本标签。当用户点击不同的选项卡时，图标和文本的颜色会根据选中状态进行变化，同时选项卡的内容区域会切换到相应的子页面。\n*/\n\n// TabContentExample.ets\n@Entry\n@Component\nstruct TabContentExample {\n  @State fontColor: string = '#182431' // 定义未选中标签的文本颜色\n  @State selectedFontColor: string = '#007DFF' // 定义选中标签的文本颜色\n  @State currentIndex: number = 0 // 定义当前选中的标签索引\n  private controller: TabsController = new TabsController() // 创建一个TabsController实例来管理选项卡状态\n\n  @Builder tabBuilder(index: number) {\n    Column() {\n      Image(this.currentIndex === index ? '/common/public_icon_on.svg' : '/common/public_icon_off.svg')\n        .width(24)\n        .height(24)\n        .margin({ bottom: 4 })\n        .objectFit(ImageFit.Contain)\n        // 根据当前选中的索引显示不同的图标\n      Text('Tab')\n        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)\n        .fontSize(10)\n        .fontWeight(500)\n        .lineHeight(14)\n        // 根据当前选中的索引设置文本颜色\n    }.width('100%').height('100%').justifyContent(FlexAlign.Center)\n  }\n\n  build() {\n    Column() {\n      Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {\n        TabContent()\n          .tabBar(this.tabBuilder(0))\n        TabContent()\n          .tabBar(this.tabBuilder(1))\n        TabContent()\n          .tabBar(this.tabBuilder(2))\n        TabContent()\n          .tabBar(this.tabBuilder(3))\n        // 创建四个选项卡，每个选项卡使用tabBuilder方法生成标签栏内容\n      }\n      .vertical(True) // 设置选项卡为垂直布局\n      .barWidth(96) // 设置标签栏宽度\n      .barHeight(414) // 设置标签栏高度\n      .onChange((index: number) => {\n        this.currentIndex = index\n        // 当选项卡切换时，更新当前选中的索引\n      })\n      .width(96)\n      .height(414)\n      .backgroundColor('#F1F3F5')\n      .margin({ top: 52 })\n    }.width('100%')\n  }\n}""",
            """/*\n实现思路：\n本示例通过使用鸿蒙ArkUI框架中的Tabs组件和BottomTabBarStyle样式，实现了一个底部标签栏，每个标签栏项使用不同的系统图标，并在标签切换时输出日志信息。\n\n总体功能与效果描述：\n该示例展示了如何在一个底部标签栏中使用系统图标作为标签的图标，并在标签切换时输出相应的日志信息。\n*/\n\n// Index.ets\nimport { SymbolGlyphModifier } from '@kit.ArkUI'\n\n@Entry\n@Component\nstruct Index {\n  // 定义四个状态变量，分别用于存储四个不同的系统图标\n  @State symbolModifier1: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi'));\n  @State symbolModifier2: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ellipsis_bubble'));\n  @State symbolModifier3: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.dot_video'));\n  @State symbolModifier4: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.exposure'));\n\n  build() {\n    Column({space: 5}) {\n      Text("底部页签样式")\n      Column(){\n        Tabs({barPosition: BarPosition.End}) {\n          // 第一个标签页，背景色为粉色\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Pink)\n          }.tabBar(new BottomTabBarStyle({\n            normal: this.symbolModifier1, // 使用第一个系统图标\n          }, 'Pink'))\n          .onWillShow(() => {\n            console.info("Pink will show") // 标签页即将显示时输出日志\n          })\n          .onWillHide(() => {\n            console.info("Pink will hide") // 标签页即将隐藏时输出日志\n          })\n\n          // 第二个标签页，背景色为橙色\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Orange)\n          }.tabBar(new BottomTabBarStyle({\n            normal: this.symbolModifier2, // 使用第二个系统图标\n          }, 'Orange'))\n          .onWillShow(() => {\n            console.info("Orange will show") // 标签页即将显示时输出日志\n          })\n          .onWillHide(() => {\n            console.info("Orange will hide") // 标签页即将隐藏时输出日志\n          })\n\n          // 第三个标签页，背景色为蓝色\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Blue)\n          }.tabBar(new BottomTabBarStyle({\n            normal: this.symbolModifier3, // 使用第三个系统图标\n          }, 'Blue'))\n          .onWillShow(() => {\n            console.info("Blue will show") // 标签页即将显示时输出日志\n          })\n          .onWillHide(() => {\n            console.info("Blue will hide") // 标签页即将隐藏时输出日志\n          })\n\n          // 第四个标签页，背景色为绿色\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Green)\n          }.tabBar(new BottomTabBarStyle({\n            normal: this.symbolModifier4, // 使用第四个系统图标\n          }, 'Green'))\n          .onWillShow(() => {\n            console.info("Green will show") // 标签页即将显示时输出日志\n          })\n          .onWillHide(() => {\n            console.info("Green will hide") // 标签页即将隐藏时输出日志\n          })\n        }\n        .vertical(False) // 设置标签栏为水平布局\n        .scrollable(True) // 设置标签栏可滚动\n        .barMode(BarMode.Fixed) // 设置标签栏为固定模式\n        .onChange((index:number)=>{\n          console.info(index.toString()) // 标签切换时输出当前标签的索引\n        })\n        .width('100%')\n        .backgroundColor(0xF1F3F5)\n      }.width('100%').height(200)\n    }\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何使用鸿蒙ArkUI框架创建一个带有自定义标签栏的选项卡组件。通过使用@State装饰器管理状态，以及@Builder装饰器创建可重用的UI组件，实现了动态切换标签内容和样式。\n\n总体功能与效果描述：\n该组件包含四个标签页，每个标签页显示不同的文本内容和分隔线。标签栏位于底部，每个标签项包含一个图标和文本，图标和文本的颜色会根据当前选中的标签页动态变化。\n*/\n\n// TabContentExample.ets\n@Entry\n@Component\nstruct TabContentExample {\n  @State fontColor: string = '#182431' // 默认字体颜色\n  @State selectedFontColor: string = '#007DFF' // 选中标签的字体颜色\n  @State currentIndex: number = 0 // 当前选中的标签索引\n  private controller: TabsController = new TabsController() // 标签控制器\n\n  // 构建标签栏项的Builder方法\n  @Builder tabBuilder(index: number) {\n    Column() {\n      Image(this.currentIndex === index ? '/common/public_icon_on.svg' : '/common/public_icon_off.svg')\n        .width(24)\n        .height(24)\n        .margin({ bottom: 4 })\n        .objectFit(ImageFit.Contain)\n      Text(`Tab${index + 1}`)\n        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)\n        .fontSize(10)\n        .fontWeight(500)\n        .lineHeight(14)\n    }.width('100%')\n  }\n\n  build() {\n    Column() {\n      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {\n        TabContent() {\n          Column() {\n            Text('Tab1')\n              .fontSize(36)\n              .fontColor('#182431')\n              .fontWeight(500)\n              .opacity(0.4)\n              .margin({ top: 30, bottom: 56.5 })\n            Divider()\n              .strokeWidth(0.5)\n              .color('#182431')\n              .opacity(0.05)\n          }.width('100%')\n        }.tabBar(this.tabBuilder(0))\n\n        TabContent() {\n          Column() {\n            Text('Tab2')\n              .fontSize(36)\n              .fontColor('#182431')\n              .fontWeight(500)\n              .opacity(0.4)\n              .margin({ top: 30, bottom: 56.5 })\n            Divider()\n              .strokeWidth(0.5)\n              .color('#182431')\n              .opacity(0.05)\n          }.width('100%')\n        }.tabBar(this.tabBuilder(1))\n\n        TabContent() {\n          Column() {\n            Text('Tab3')\n              .fontSize(36)\n              .fontColor('#182431')\n              .fontWeight(500)\n              .opacity(0.4)\n              .margin({ top: 30, bottom: 56.5 })\n            Divider()\n              .strokeWidth(0.5)\n              .color('#182431')\n              .opacity(0.05)\n          }.width('100%')\n        }.tabBar(this.tabBuilder(2))\n\n        TabContent() {\n          Column() {\n            Text('Tab4')\n              .fontSize(36)\n              .fontColor('#182431')\n              .fontWeight(500)\n              .opacity(0.4)\n              .margin({ top: 30, bottom: 56.5 })\n            Divider()\n              .strokeWidth(0.5)\n              .color('#182431')\n              .opacity(0.05)\n          }.width('100%')\n        }.tabBar(this.tabBuilder(3))\n      }\n      .vertical(False) // 设置标签栏为水平布局\n      .barHeight(56) // 设置标签栏高度\n      .onChange((index: number) => {\n        this.currentIndex = index // 更新当前选中的标签索引\n      })\n      .width(360)\n      .height(190)\n      .backgroundColor('#F1F3F5')\n      .margin({ top: 38 })\n    }.width('100%')\n  }\n}""",
            """/*\n实现思路：\n该示例展示了如何通过ComponentContent设置SubTabBarStyle，并实现动态更新TabBar的内容。通过定义一个Params类来传递文本内容，使用Builder装饰器来构建文本组件，然后在主组件中使用ComponentContent来创建TabBar的内容，并通过按钮点击事件来更新TabBar的文本内容。\n\n总体功能与效果描述：\n该示例创建了一个包含两个Tab的Tabs组件，每个Tab的内容是一个带有背景色的Column组件。每个Tab的TabBar内容是通过ComponentContent动态设置的文本。通过点击按钮，可以更新对应TabBar的文本内容。\n*/\n\n// Index.ets\nimport { ComponentContent, UIContext } from "@kit.ArkUI"\n\n// 定义一个Params类，用于传递文本内容\nclass Params {\n  text: string = ""\n\n  constructor(text: string) {\n    this.text = text;\n  }\n}\n\n// 使用Builder装饰器定义一个构建文本组件的函数\n@Builder\nfunction buildText(params: Params) {\n  Column() {\n    Text(params.text)\n      .fontSize(20) // 设置文本字体大小\n      .fontWeight(FontWeight.Bold) // 设置文本字体粗细\n      .margin(20) // 设置文本外边距\n  }\n}\n\n// 主组件Index，使用@Entry和@Component装饰器\n@Entry\n@Component\nstruct Index {\n  @State message1: string = "tabBar1" // 定义状态变量message1，初始值为"tabBar1"\n  @State message2: string = "tabBar2" // 定义状态变量message2，初始值为"tabBar2"\n  context: UIContext = this.getUIContext() // 获取UI上下文\n  private count1 = 0; // 定义私有变量count1，用于记录更新次数\n  private count2 = 0; // 定义私有变量count2，用于记录更新次数\n  private controller: TabsController = new TabsController(); // 创建Tabs控制器\n  tabBar1: ComponentContent<Params> = new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(buildText), new Params(this.message1)); // 创建ComponentContent实例tabBar1\n  tabBar2: ComponentContent<Params> = new ComponentContent<Params>(this.context, wrapBuilder<[Params]>(buildText), new Params(this.message2)); // 创建ComponentContent实例tabBar2\n\n  build() {\n    Row() {\n      Column() {\n        Button("更新tabBar1").width('90%').margin(20) // 创建按钮，点击时更新tabBar1的内容\n          .onClick((event?: ClickEvent) => {\n            this.count1 += 1; // 更新次数加1\n            const message1 = "Update 1_" + this.count1.toString(); // 生成新的文本内容\n            this.tabBar1.update(new Params(message1)); // 更新tabBar1的内容\n          })\n        Button("更新tabBar2").width('90%').margin(20) // 创建按钮，点击时更新tabBar2的内容\n          .onClick((event?: ClickEvent) => {\n            this.count2 += 1; // 更新次数加1\n            const message2 = "Update 2_" + this.count2.toString(); // 生成新的文本内容\n            this.tabBar2.update(new Params(message2)); // 更新tabBar2的内容\n          })\n        Tabs({ barPosition: BarPosition.Start, controller: this.controller }) { // 创建Tabs组件\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Pink).borderRadius('12vp') // 创建TabContent内容\n          }.tabBar(new SubTabBarStyle(this.tabBar1)) // 设置TabBar样式\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Blue).borderRadius('12vp') // 创建TabContent内容\n          }.tabBar(SubTabBarStyle.of(this.tabBar2)) // 设置TabBar样式\n        }\n        .vertical(False) // 设置Tabs为水平布局\n        .barWidth(414) // 设置TabBar宽度\n        .barHeight(96) // 设置TabBar高度\n        .width(414) // 设置Tabs宽度\n        .height(414) // 设置Tabs高度\n        .backgroundColor('#F1F3F5') // 设置Tabs背景颜色\n        .margin({ top: 20 }) // 设置Tabs外边距\n      }\n      .width('100%') // 设置Column宽度\n      .height('100%') // 设置Column高度\n    }\n    .height('100%') // 设置Row高度\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何通过自定义样式来改变Tabs组件中子页签和底部页签的文本颜色和图标颜色。通过设置labelStyle和iconStyle的unselectedColor和selectedColor属性，可以实现不同状态下的颜色变化。\n\n总体功能与效果描述：\n1. 子页签样式：通过SubTabBarStyle设置子页签的文本颜色，未选中时为红色，选中时为绿色。\n2. 底部页签样式：通过BottomTabBarStyle设置底部页签的文本和图标颜色，未选中时为红色，选中时为绿色。\n*/\n\n// TabBarStyleExample.ets\n@Entry\n@Component\nstruct TabBarStyleExample {\n  build() {\n    Column({ space: 5 }) {\n      Text("子页签样式")\n      Column() {\n        Tabs({ barPosition: BarPosition.Start }) {\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Pink)\n          }.tabBar(new SubTabBarStyle('Pink')\n            .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))\n          // 设置子页签的文本颜色，未选中时为红色，选中时为绿色\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Yellow)\n          }.tabBar(new SubTabBarStyle('Yellow')\n            .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))\n          // 设置子页签的文本颜色，未选中时为红色，选中时为绿色\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Blue)\n          }.tabBar(new SubTabBarStyle('Blue')\n            .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))\n          // 设置子页签的文本颜色，未选中时为红色，选中时为绿色\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Green)\n          }.tabBar(new SubTabBarStyle('Green')\n            .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))\n          // 设置子页签的文本颜色，未选中时为红色，选中时为绿色\n        }\n        .vertical(False)\n        .scrollable(True)\n        .barMode(BarMode.Fixed)\n        .onChange((index: number) => {\n          console.info(index.toString())\n        })\n        // 设置Tabs的垂直方向、可滚动、固定模式，并监听页签变化事件\n        .width('100%')\n        .backgroundColor(0xF1F3F5)\n      }.width('100%').height(200)\n\n      Text("底部页签样式")\n      Column() {\n        Tabs({ barPosition: BarPosition.End }) {\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Pink)\n          }.tabBar(new BottomTabBarStyle('/common/public_icon_off.svg', 'pink')\n            .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })\n            .iconStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))\n          // 设置底部页签的文本和图标颜色，未选中时为红色，选中时为绿色\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Yellow)\n          }.tabBar(new BottomTabBarStyle('/common/public_icon_off.svg', 'Yellow')\n            .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })\n            .iconStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))\n          // 设置底部页签的文本和图标颜色，未选中时为红色，选中时为绿色\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Blue)\n          }.tabBar(new BottomTabBarStyle('/common/public_icon_off.svg', 'Blue')\n            .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })\n            .iconStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))\n          // 设置底部页签的文本和图标颜色，未选中时为红色，选中时为绿色\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Green)\n          }.tabBar(new BottomTabBarStyle('/common/public_icon_off.svg', 'Green')\n            .labelStyle({ unselectedColor: Color.Red, selectedColor: Color.Green })\n            .iconStyle({ unselectedColor: Color.Red, selectedColor: Color.Green }))\n          // 设置底部页签的文本和图标颜色，未选中时为红色，选中时为绿色\n        }\n        .vertical(False)\n        .scrollable(True)\n        .barMode(BarMode.Fixed)\n        .onChange((index: number) => {\n          console.info(index.toString())\n        })\n        // 设置Tabs的垂直方向、可滚动、固定模式，并监听页签变化事件\n        .width('100%')\n        .backgroundColor(0xF1F3F5)\n      }.width('100%').height(200)\n    }\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中使用Tabs组件，并通过不同的文本溢出处理方式来展示Tab标签的内容。每个Tab标签的内容通过不同的文本处理策略（如单行省略号截断、先缩小再截断、先缩小再换行再截断、换行）来展示。\n总体功能与效果描述：\n用户可以通过切换不同的Tab来查看不同文本处理策略下的Tab标签内容展示效果。\n*/\n\n// TabsTextOverflow.ets\n@Entry\n@Component\nstruct TabsTextOverflow {\n  @State message: string = 'Hello World' // 初始化一个状态变量，用于显示消息\n  private controller: TabsController = new TabsController() // 创建一个Tabs控制器实例\n  @State subTabOverflowOpaque: boolean = True; // 初始化一个状态变量，用于控制子Tab的溢出透明度\n\n  build() {\n    Column() {\n      Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {\n        TabContent() {\n          Column() {\n            Text('单行省略号截断').fontSize(30).fontColor(0xFF000000) // 设置文本内容和样式\n          }.width('100%').height('100%').backgroundColor(Color.Pink) // 设置列的宽度和高度，并设置背景颜色\n        }\n        .tabBar(SubTabBarStyle.of('开始【单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断单行省略号截断】结束')\n          .labelStyle({\n            overflow: TextOverflow.Ellipsis, // 设置文本溢出处理方式为省略号\n            maxLines: 1, // 设置最大行数为1\n            minFontSize: 10, // 设置最小字体大小\n            heightAdaptivePolicy: TextHeightAdaptivePolicy.MAX_LINES_FIRST, // 设置高度自适应策略\n            font: { size: 20 } // 设置字体大小\n          }))\n\n        TabContent() {\n          Column() {\n            Text('先缩小再截断').fontSize(30).fontColor(0xFF000000) // 设置文本内容和样式\n          }.width('100%').height('100%').backgroundColor(Color.Pink) // 设置列的宽度和高度，并设置背景颜色\n        }\n        .tabBar(SubTabBarStyle.of('开始【先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断先缩小再截断】结束')\n          .labelStyle({\n            overflow: TextOverflow.Clip, // 设置文本溢出处理方式为剪切\n            maxLines: 1, // 设置最大行数为1\n            minFontSize: 15, // 设置最小字体大小\n            maxFontSize: 15, // 设置最大字体大小\n            heightAdaptivePolicy: TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST, // 设置高度自适应策略\n            font: { size: 20 } // 设置字体大小\n          }))\n\n        TabContent() {\n          Column() {\n            Text('先缩小再换行再截断').fontSize(30).fontColor(0xFF000000) // 设置文本内容和样式\n          }.width('100%').height('100%').backgroundColor(Color.Pink) // 设置列的宽度和高度，并设置背景颜色\n        }\n        .tabBar(SubTabBarStyle.of('开始【先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断先缩小再换行再截断】结束')\n          .labelStyle({\n            overflow: TextOverflow.Clip, // 设置文本溢出处理方式为剪切\n            maxLines: 2, // 设置最大行数为2\n            minFontSize: 15, // 设置最小字体大小\n            maxFontSize: 15, // 设置最大字体大小\n            heightAdaptivePolicy: TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST, // 设置高度自适应策略\n            font: { size: 20 } // 设置字体大小\n          }))\n\n        TabContent() {\n          Column() {\n            Text('换行').fontSize(30).fontColor(0xFF000000) // 设置文本内容和样式\n          }\n          .width('100%').height('100%').backgroundColor(Color.Pink) // 设置列的宽度和高度，并设置背景颜色\n        }.tabBar(SubTabBarStyle.of('开始【换行换行换行换行换行换行换行换行换行换行换行换行换行换行换行】结束')\n          .labelStyle({\n            overflow: TextOverflow.Clip, // 设置文本溢出处理方式为剪切\n            maxLines: 10, // 设置最大行数为10\n            minFontSize: 10, // 设置最小字体大小\n            heightAdaptivePolicy: TextHeightAdaptivePolicy.MAX_LINES_FIRST, // 设置高度自适应策略\n            font: { size: 20 } // 设置字体大小\n          }))\n      }\n      .vertical(True).scrollable(True) // 设置Tabs为垂直方向且可滚动\n      .barMode(BarMode.Fixed) // 设置Tab栏模式为固定\n      .barHeight(720) // 设置Tab栏高度\n      .barWidth(200).animationDuration(400) // 设置Tab栏宽度及动画持续时间\n      .onChange((index: number) => {\n        console.info(index.toString()) // 当Tab切换时，输出当前Tab的索引\n      })\n      .height('100%').width('100%') // 设置Tabs的宽度和高度\n    }\n    .height('100%') // 设置列的高度\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何使用鸿蒙ArkUI框架中的Tabs组件，并通过多个按钮来动态改变Tabs组件的样式和内容。具体包括改变Tab的padding、文本内容、布局模式、垂直对齐方式以及是否对称扩展等。\n\n总体功能与效果描述：\n用户可以通过点击不同的按钮来动态调整Tabs组件的样式和内容，包括改变Tab的padding、文本内容、布局模式、垂直对齐方式以及是否对称扩展。每个按钮点击后会触发相应的状态变量更新，从而实时改变Tabs组件的显示效果。\n*/\n\n// TabContentExample6.ets\n@Entry\n@Component\nstruct TabContentExample6 {\n  private controller: TabsController = new TabsController()\n  @State text: string = "2"\n  @State tabPadding: number = 0;\n  @State symmetricExtensible: boolean = False;\n  @State layoutMode: LayoutMode = LayoutMode.VERTICAL;\n  @State verticalAlign: VerticalAlign = VerticalAlign.Center;\n\n  build() {\n    Column() {\n      Row() {\n        Button("padding+10 " + this.tabPadding)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.tabPadding += 10\n          })\n          .margin({ right: '6%', bottom: '12vp' })\n        // 点击按钮增加Tab的padding值\n\n        Button("padding-10 " + this.tabPadding)\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.tabPadding -= 10\n          })\n          .margin({ bottom: '12vp' })\n        // 点击按钮减少Tab的padding值\n      }\n\n      Row() {\n        Button("文本增加 ")\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.text += '文本增加'\n          })\n          .margin({ right: '6%', bottom: '12vp' })\n        // 点击按钮增加Tab的文本内容\n\n        Button("文本重置")\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.text = "2"\n          })\n          .margin({ bottom: '12vp' })\n        // 点击按钮重置Tab的文本内容\n      }\n\n      Row() {\n        Button("symmetricExtensible改变 " + this.symmetricExtensible)\n          .width('100%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.symmetricExtensible = !this.symmetricExtensible\n          })\n          .margin({ bottom: '12vp' })\n        // 点击按钮切换Tab的对称扩展属性\n      }\n\n      Row() {\n        Button("layoutMode垂直 ")\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.layoutMode = LayoutMode.VERTICAL;\n          })\n          .margin({ right: '6%', bottom: '12vp' })\n        // 点击按钮将Tab的布局模式设置为垂直\n\n        Button("layoutMode水平 ")\n          .width('47%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.layoutMode = LayoutMode.HORIZONTAL;\n          })\n          .margin({ bottom: '12vp' })\n        // 点击按钮将Tab的布局模式设置为水平\n      }\n\n      Row() {\n        Button("verticalAlign朝上")\n          .width('100%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.verticalAlign = VerticalAlign.Top;\n          })\n          .margin({ bottom: '12vp' })\n        // 点击按钮将Tab的垂直对齐方式设置为朝上\n      }\n\n      Row() {\n        Button("verticalAlign居中")\n          .width('100%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.verticalAlign = VerticalAlign.Center;\n          })\n          .margin({ bottom: '12vp' })\n        // 点击按钮将Tab的垂直对齐方式设置为居中\n      }\n\n      Row() {\n        Button("verticalAlign朝下")\n          .width('100%')\n          .height(50)\n          .margin({ top: 5 })\n          .onClick((event?: ClickEvent) => {\n            this.verticalAlign = VerticalAlign.Bottom;\n          })\n          .margin({ bottom: '12vp' })\n        // 点击按钮将Tab的垂直对齐方式设置为朝下\n      }\n\n      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Pink)\n        }.tabBar(BottomTabBarStyle.of($r("sys.media.ohos_app_icon"), "1"))\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green)\n        }.tabBar(BottomTabBarStyle.of($r("sys.media.ohos_app_icon"), this.text)\n          .padding(this.tabPadding)\n          .verticalAlign(this.verticalAlign)\n          .layoutMode(this.layoutMode)\n          .symmetricExtensible(this.symmetricExtensible))\n        // 第二个Tab的内容和样式，根据状态变量动态调整\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Blue)\n        }.tabBar(BottomTabBarStyle.of($r("sys.media.ohos_app_icon"), "3"))\n      }\n      .animationDuration(300)\n      .height('60%')\n      .backgroundColor(0xf1f3f5)\n      .barMode(BarMode.Fixed)\n    }\n    .width('100%')\n    .height(500)\n    .margin({ top: 5 })\n    .padding('24vp')\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中使用Tabs组件，并通过不同的TabBar样式（子页签样式、底部页签样式、侧边页签样式）来切换不同的内容区域。每个TabContent包含一个具有不同背景颜色的Column组件，并通过tabBar属性设置不同的页签样式。此外，还通过onWillShow和onWillHide事件监听页签的显示和隐藏状态。\n\n总体功能与效果描述：\n1. 子页签样式：页签位于内容区域的上方，每个页签显示一个颜色名称，点击不同页签切换不同背景颜色的内容区域。\n2. 底部页签样式：页签位于内容区域的下方，每个页签显示一个图标和颜色名称，点击不同页签切换不同背景颜色的内容区域。\n3. 侧边页签样式：页签位于内容区域的左侧，每个页签显示一个图标和颜色名称，点击不同页签切换不同背景颜色的内容区域。\n*/\n\n// TabBarStyleExample.ets\n@Entry\n@Component\nstruct TabBarStyleExample {\n  build() {\n    Column({ space: 5 }) {\n      Text("子页签样式")\n      Column() {\n        Tabs({ barPosition: BarPosition.Start }) {\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Pink)\n          }.tabBar(new SubTabBarStyle('Pink'))\n          .onWillShow(() => {\n            console.info("Pink will show")\n          })\n          .onWillHide(() => {\n            console.info("Pink will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Yellow)\n          }.tabBar(new SubTabBarStyle('Yellow'))\n          .onWillShow(() => {\n            console.info("Yellow will show")\n          })\n          .onWillHide(() => {\n            console.info("Yellow will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Blue)\n          }.tabBar(new SubTabBarStyle('Blue'))\n          .onWillShow(() => {\n            console.info("Blue will show")\n          })\n          .onWillHide(() => {\n            console.info("Blue will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Green)\n          }.tabBar(new SubTabBarStyle('Green'))\n          .onWillShow(() => {\n            console.info("Green will show")\n          })\n          .onWillHide(() => {\n            console.info("Green will hide")\n          })\n        }\n        .vertical(False)\n        .scrollable(True)\n        .barMode(BarMode.Fixed)\n        .onChange((index: number) => {\n          console.info(index.toString())\n        })\n        .width('100%')\n        .backgroundColor(0xF1F3F5)\n      }.width('100%').height(200)\n\n      Text("底部页签样式")\n      Column() {\n        Tabs({ barPosition: BarPosition.End }) {\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Pink)\n          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Pink'))\n          .onWillShow(() => {\n            console.info("Pink will show")\n          })\n          .onWillHide(() => {\n            console.info("Pink will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Yellow)\n          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Yellow'))\n          .onWillShow(() => {\n            console.info("Yellow will show")\n          })\n          .onWillHide(() => {\n            console.info("Yellow will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Blue)\n          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))\n          .onWillShow(() => {\n            console.info("Blue will show")\n          })\n          .onWillHide(() => {\n            console.info("Blue will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Green)\n          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Green'))\n          .onWillShow(() => {\n            console.info("Green will show")\n          })\n          .onWillHide(() => {\n            console.info("Green will hide")\n          })\n        }\n        .vertical(False)\n        .scrollable(True)\n        .barMode(BarMode.Fixed)\n        .onChange((index: number) => {\n          console.info(index.toString())\n        })\n        .width('100%')\n        .backgroundColor(0xF1F3F5)\n      }.width('100%').height(200)\n\n      Text("侧边页签样式")\n      Column() {\n        Tabs({ barPosition: BarPosition.Start }) {\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Pink)\n          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Pink'))\n          .onWillShow(() => {\n            console.info("Pink will show")\n          })\n          .onWillHide(() => {\n            console.info("Pink will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Yellow)\n          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Yellow'))\n          .onWillShow(() => {\n            console.info("Yellow will show")\n          })\n          .onWillHide(() => {\n            console.info("Yellow will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Blue)\n          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))\n          .onWillShow(() => {\n            console.info("Blue will show")\n          })\n          .onWillHide(() => {\n            console.info("Blue will hide")\n          })\n\n          TabContent() {\n            Column().width('100%').height('100%').backgroundColor(Color.Green)\n          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Green'))\n          .onWillShow(() => {\n            console.info("Green will show")\n          })\n          .onWillHide(() => {\n            console.info("Green will hide")\n          })\n        }\n        .vertical(True)\n        .scrollable(True)\n        .barMode(BarMode.Fixed)\n        .onChange((index: number) => {\n          console.info(index.toString())\n        })\n        .width('100%')\n        .backgroundColor(0xF1F3F5)\n      }.width('100%').height(400)\n    }\n  }\n}""",
            """/*\n实现思路：\n本示例展示了如何使用Tabs组件及其相关属性来创建一个可定制的标签页界面。通过按钮点击事件，动态改变标签页的下划线指示器的颜色、高度、宽度、圆角半径和间距，从而实现丰富的交互效果。\n\n总体功能与效果描述：\n1. 通过按钮点击事件，动态改变标签页的下划线指示器的颜色、高度、宽度、圆角半径和间距。\n2. 使用Tabs组件创建一个包含多个标签页的界面，每个标签页具有不同的背景颜色和圆角边框。\n3. 标签页的切换效果和样式可以通过属性进行定制。\n*/\n\n// TabsAttr.ets\n@Entry\n@Component\nstruct TabsAttr {\n  private controller: TabsController = new TabsController()\n  @State indicatorColor: Color = Color.Blue; // 下划线指示器的颜色\n  @State indicatorWidth: number = 40; // 下划线指示器的宽度\n  @State indicatorHeight: number = 10; // 下划线指示器的高度\n  @State indicatorBorderRadius: number = 5; // 下划线指示器的圆角半径\n  @State indicatorSpace: number = 10; // 下划线指示器的间距\n  @State subTabBorderRadius: number = 20; // 子标签页的圆角半径\n  @State selectedMode: SelectedMode = SelectedMode.INDICATOR; // 选中模式\n  private colorFlag: boolean = True; // 颜色变化标志\n  private widthFlag: boolean = True; // 宽度变化标志\n  private heightFlag: boolean = True; // 高度变化标志\n  private borderFlag: boolean = True; // 圆角变化标志\n  private spaceFlag: boolean = True; // 间距变化标志\n\n  build() {\n    Column() {\n      Button("下划线颜色变化").width('100%').margin({ bottom: '12vp' })\n        .onClick((event?: ClickEvent) => {\n          // 点击按钮时，切换下划线指示器的颜色\n          if (this.colorFlag) {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorColor = Color.Red\n            })\n          } else {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorColor = Color.Yellow\n            })\n          }\n          this.colorFlag = !this.colorFlag\n        })\n      Button("下划线高度变化").width('100%').margin({ bottom: '12vp' })\n        .onClick((event?: ClickEvent) => {\n          // 点击按钮时，切换下划线指示器的高度\n          if (this.heightFlag) {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorHeight = 20\n            })\n          } else {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorHeight = 10\n            })\n          }\n          this.heightFlag = !this.heightFlag\n        })\n      Button("下划线宽度变化").width('100%').margin({ bottom: '12vp' })\n        .onClick((event?: ClickEvent) => {\n          // 点击按钮时，切换下划线指示器的宽度\n          if (this.widthFlag) {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorWidth = 30\n            })\n          } else {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorWidth = 50\n            })\n          }\n          this.widthFlag = !this.widthFlag\n        })\n      Button("下划线圆角半径变化").width('100%').margin({ bottom: '12vp' })\n        .onClick((event?: ClickEvent) => {\n          // 点击按钮时，切换下划线指示器的圆角半径\n          if (this.borderFlag) {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorBorderRadius = 0\n            })\n          } else {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorBorderRadius = 5\n            })\n          }\n          this.borderFlag = !this.borderFlag\n        })\n      Button("下划线间距变化").width('100%').margin({ bottom: '12vp' })\n        .onClick((event?: ClickEvent) => {\n          // 点击按钮时，切换下划线指示器的间距\n          if (this.spaceFlag) {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorSpace = 20\n            })\n          } else {\n            animateTo({\n              duration: 1000, \n              curve: Curve.Linear, \n              delay: 200, \n              iterations: 1, \n              playMode: PlayMode.Normal, \n              onFinish: () => {\n                console.info('play end')\n              }\n            }, () => {\n              this.indicatorSpace = 10\n            })\n          }\n          this.spaceFlag = !this.spaceFlag\n        })\n      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Pink).borderRadius('12vp')\n        }.tabBar(SubTabBarStyle.of('pink')\n          .indicator({\n            color: this.indicatorColor, \n            height: this.indicatorHeight, \n            width: this.indicatorWidth, \n            borderRadius: this.indicatorBorderRadius, \n            marginTop: this.indicatorSpace \n          })\n          .selectedMode(this.selectedMode)\n          .board({ borderRadius: this.subTabBorderRadius })\n          .labelStyle({})\n        )\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Yellow).borderRadius('12vp')\n        }.tabBar('yellow')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Blue).borderRadius('12vp')\n        }.tabBar('blue')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Green).borderRadius('12vp')\n        }.tabBar('green')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Gray).borderRadius('12vp')\n        }.tabBar('gray')\n\n        TabContent() {\n          Column().width('100%').height('100%').backgroundColor(Color.Orange).borderRadius('12vp')\n        }.tabBar('orange')\n      }\n      .vertical(False)\n      .scrollable(True)\n      .barMode(BarMode.Scrollable)\n      .barHeight(140)\n      .animationDuration(400)\n      .onChange((index: number) => {\n        console.info(index.toString())\n      })\n      .backgroundColor(0xF5F5F5)\n      .height(320)\n    }.width('100%').height(250).padding({ top: '24vp', left: '24vp', right: '24vp' })\n  }\n}"""
        ]
    },
    "WaterFlow": {
        "description": "瀑布流容器，由“行”和“列”分割的单元格所组成，通过容器自身的排列规则，将不同大小的“项目”自上而下，如瀑布般紧密布局。",
        "details": None,
        "interfaces": [
            {
                "description": "WaterFlow(options?: WaterFlowOptions)",
                "params": {
                    "options": {
                        "type": "WaterFlowOptions",
                        "required": False,
                        "description": "瀑布流选项。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "columnsTemplate": {
                "description": "设置当前瀑布流组件布局列的数量。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前瀑布流组件布局列的数量。",
                        "default": "1fr"
                    }
                }
            },
            "rowsTemplate": {
                "description": "设置当前瀑布流组件布局行的数量。",
                "params": {
                    "value": {
                        "type": "string",
                        "required": True,
                        "description": "当前瀑布流组件布局行的数量。",
                        "default": "1fr"
                    }
                }
            },
            "itemConstraintSize": {
                "description": "设置约束尺寸，子组件布局时，进行尺寸范围限制。",
                "params": {
                    "value": {
                        "type": "ConstraintSizeOptions",
                        "required": True,
                        "description": "约束尺寸。",
                        "default": None
                    }
                }
            },
            "columnsGap": {
                "description": "设置列与列的间距。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "列与列的间距。",
                        "default": 0
                    }
                }
            },
            "rowsGap": {
                "description": "设置行与行的间距。",
                "params": {
                    "value": {
                        "type": "Length",
                        "required": True,
                        "description": "行与行的间距。",
                        "default": 0
                    }
                }
            },
            "layoutDirection": {
                "description": "设置布局的主轴方向。",
                "params": {
                    "value": {
                        "type": "FlexDirection",
                        "required": True,
                        "description": "布局的主轴方向。",
                        "default": "FlexDirection.Column"
                    }
                }
            },
            "enableScrollInteraction": {
                "description": "设置是否支持滚动手势。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否支持滚动手势。",
                        "default": True
                    }
                }
            },
            "nestedScroll": {
                "description": "设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。",
                "params": {
                    "value": {
                        "type": "NestedScrollOptions",
                        "required": True,
                        "description": "嵌套滚动模式。",
                        "default": None
                    }
                }
            },
            "friction": {
                "description": "设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "摩擦系数。",
                        "default": 0.75
                    }
                }
            },
            "cachedCount": {
                "description": "设置预加载的FlowItem的数量，只在LazyForEach中生效。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "预加载的FlowItem的数量。",
                        "default": 1
                    }
                }
            }
        },
        "events": {
            "onReachStart": {
                "description": "瀑布流组件到达起始位置时触发。",
                "params": {},
                "returns": None
            },
            "onReachEnd": {
                "description": "瀑布流组件到底末尾位置时触发。",
                "params": {},
                "returns": None
            },
            "onScrollFrameBegin": {
                "description": "瀑布流开始滑动时触发，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，瀑布流将按照返回值的实际滑动量进行滑动。",
                "params": {
                    "offset": {
                        "type": "number",
                        "required": True,
                        "description": "即将发生的滑动量，单位vp。",
                        "default": None
                    },
                    "state": {
                        "type": "ScrollState",
                        "required": True,
                        "description": "当前滑动状态。",
                        "default": None
                    }
                },
                "returns": {
                    "offsetRemain": {
                        "type": "number",
                        "description": "实际滑动量，单位vp。"
                    }
                }
            },
            "onScrollIndex": {
                "description": "当前瀑布流显示的起始位置/终止位置的子组件发生变化时触发。",
                "params": {
                    "first": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示的瀑布流起始位置的索引值。",
                        "default": None
                    },
                    "last": {
                        "type": "number",
                        "required": True,
                        "description": "当前显示的瀑布流终止位置的索引值。",
                        "default": None
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何使用WaterFlow组件实现一个瀑布流布局，并通过随机生成的大小和颜色来动态填充每个FlowItem。\\n总体功能与效果描述：\\n该组件展示了100个不同大小和颜色的FlowItem，每个FlowItem包含一个文本和一个图片，布局采用瀑布流形式，自动填充列。\\n*/\\n\\n// WaterFlowDemo.ets\\nimport { WaterFlowDataSource } from './WaterFlowDataSource'\\n\\n@Entry\\n@Component\\nstruct WaterFlowDemo {\\n  @State minSize: number = 80 // 定义FlowItem的最小尺寸\\n  @State maxSize: number = 180 // 定义FlowItem的最大尺寸\\n  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F] // 定义FlowItem的背景颜色数组\\n  dataSource: WaterFlowDataSource = new WaterFlowDataSource() // 数据源实例\\n  private itemWidthArray: number[] = [] // 存储FlowItem宽度的数组\\n  private itemHeightArray: number[] = [] // 存储FlowItem高度的数组\\n\\n  // 获取随机尺寸\\n  getSize() {\\n    let ret = Math.floor(Math.random() * this.maxSize)\\n    return (ret > this.minSize ? ret : this.minSize) // 确保尺寸在最小和最大之间\\n  }\\n\\n  // 设置FlowItem的尺寸数组\\n  setItemSizeArray() {\\n    for (let i = 0; i < 100; i++) {\\n      this.itemWidthArray.push(this.getSize())\\n      this.itemHeightArray.push(this.getSize())\\n    }\\n  }\\n\\n  // 组件即将显示时调用，初始化尺寸数组\\n  aboutToAppear() {\\n    this.setItemSizeArray()\\n  }\\n\\n  build() {\\n    Column({ space: 2 }) {\\n      WaterFlow() {\\n        LazyForEach(this.dataSource, (item: number) => {\\n          FlowItem() {\\n            Column() {\\n              Text(\"N\" + item).fontSize(12).height('16') // 显示FlowItem的序号\\n              Image('res/waterFlowTest(' + item % 5 + ').jpg') // 显示FlowItem的图片\\n            }\\n          }\\n          .width('100%')\\n          .height(this.itemHeightArray[item % 100]) // 设置FlowItem的高度\\n          .backgroundColor(this.colors[item % 5]) // 设置FlowItem的背景颜色\\n        }, (item: string) => item)\\n      }\\n      .columnsTemplate('repeat(auto-fill,80)') // 设置列模板，自动填充列\\n      .columnsGap(10) // 设置列间距\\n      .rowsGap(5) // 设置行间距\\n      .padding({left:5}) // 设置左边距\\n      .backgroundColor(0xFAEEE0) // 设置背景颜色\\n      .width('100%') // 设置宽度\\n      .height('100%') // 设置高度\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n1. 创建一个可复用的组件 `ReusableFlowItem`，用于显示每个水流项的内容。\\n2. 创建一个主组件 `WaterFlowDemo`，用于管理水流布局和双指缩放功能。\\n3. 使用 `WaterFlow` 组件和 `LazyForEach` 循环生成水流项。\\n4. 通过双指缩放手势调整水流布局的列数。\\n\\n总体功能与效果描述：\\n- 显示一个水流布局，每个项包含一个文本和一个图片。\\n- 通过双指缩放手势动态调整水流布局的列数。\\n*/\\n\\n// ReusableFlowItem.ets\\n@Reusable\\n@Component\\nstruct ReusableFlowItem {\\n  @State item: number = 0\\n\\n  // 组件复用时调用，更新项的内容\\n  aboutToReuse(params: Record<string, number>) {\\n    this.item = params.item;\\n    console.info('Reuse item:' + this.item)\\n  }\\n\\n  // 组件首次出现时调用，输出项的内容\\n  aboutToAppear() {\\n    console.info('item:' + this.item)\\n  }\\n\\n  // 构建组件的UI\\n  build() {\\n    Column() {\\n      Text(\"N\" + this.item).fontSize(12).height('16')\\n      Image('res/waterFlow (' + this.item % 5 + ').JPG')\\n        .objectFit(ImageFit.Fill)\\n        .width('100%')\\n        .layoutWeight(1)\\n    }\\n  }\\n}\\n\\n// WaterFlowDemo.ets\\n@Entry\\n@Component\\nstruct WaterFlowDemo {\\n  minSize: number = 80\\n  maxSize: number = 180\\n  colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]\\n  @State columns: number = 2\\n  dataSource: WaterFlowDataSource = new WaterFlowDataSource()\\n  private itemWidthArray: number[] = []\\n  private itemHeightArray: number[] = []\\n\\n  // 获取随机大小\\n  getSize() {\\n    let ret = Math.floor(Math.random() * this.maxSize)\\n    return (ret > this.minSize ? ret : this.minSize)\\n  }\\n\\n  // 设置项的宽度和高度数组\\n  setItemSizeArray() {\\n    for (let i = 0; i < 100; i++) {\\n      this.itemWidthArray.push(this.getSize())\\n      this.itemHeightArray.push(this.getSize())\\n    }\\n  }\\n\\n  // 组件首次出现时调用，初始化列数和项的大小数组\\n  aboutToAppear() {\\n    let lastCount = AppStorage.get<number>('columnsCount')\\n    if (typeof lastCount != 'undefined') {\\n      this.columns = lastCount\\n    }\\n    this.setItemSizeArray()\\n  }\\n\\n  // 构建组件的UI\\n  build() {\\n    Column({ space: 2 }) {\\n      Row() {\\n        Text('双指缩放改变列数')\\n          .height('5%')\\n          .margin({ top: 10, left: 20 })\\n      }\\n\\n      WaterFlow() {\\n        LazyForEach(this.dataSource, (item: number) => {\\n          FlowItem() {\\n            ReusableFlowItem({ item: item })\\n          }\\n          .width('100%')\\n          .height(this.itemHeightArray[item % 100])\\n          .backgroundColor(this.colors[item % 5])\\n        }, (item: string) => item)\\n      }\\n      .columnsTemplate('1fr '.repeat(this.columns))\\n      .columnsGap(10)\\n      .rowsGap(5)\\n      .backgroundColor(0xFAEEE0)\\n      .width('100%')\\n      .height('100%')\\n      .layoutWeight(1)\\n\\n      .animation({\\n        duration: 300,\\n        curve: Curve.Smooth\\n      })\\n      .priorityGesture(\\n        PinchGesture()\\n          .onActionEnd((event: GestureEvent) => {\\n            console.info('end scale:' + event.scale)\\n\\n            if (event.scale > 2) {\\n              this.columns--\\n            } else if (event.scale < 0.6) {\\n              this.columns++\\n            }\\n\\n            this.columns = Math.min(4, Math.max(1, this.columns));\\n            AppStorage.setOrCreate<number>('columnsCount', this.columns)\\n          })\\n      )\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n1. 创建一个数据源类 `WaterFlowDataSource`，用于管理数据和通知数据变化。\\n2. 在 `WaterFlowDemo` 组件中使用 `WaterFlow` 组件展示数据，并实现动态加载和样式设置。\\n3. 使用 `LazyForEach` 循环渲染数据项，并在每个数据项中展示文本和图片。\\n4. 实现滚动事件监听和动态数据加载。\\n\\n总体功能与效果描述：\\n- 展示一个瀑布流布局，包含动态加载的数据项。\\n- 每个数据项包含文本和图片，并具有随机的大小和颜色。\\n- 支持滚动事件监听和动态数据加载。\\n*/\\n\\n// WaterFlowDataSource.ts\\nexport class WaterFlowDataSource implements IDataSource {\\n  private dataArray: number[] = []\\n  private listeners: DataChangeListener[] = []\\n\\n  constructor() {\\n    // 初始化数据数组，填充100个数字\\n    for (let i = 0; i < 100; i++) {\\n      this.dataArray.push(i)\\n    }\\n  }\\n\\n  // 获取指定索引的数据\\n  public getData(index: number): number {\\n    return this.dataArray[index]\\n  }\\n\\n  // 通知所有监听器数据重新加载\\n  notifyDataReload(): void {\\n    this.listeners.forEach(listener => {\\n      listener.onDataReloaded()\\n    })\\n  }\\n\\n  // 通知所有监听器数据添加\\n  notifyDataAdd(index: number): void {\\n    this.listeners.forEach(listener => {\\n      listener.onDataAdd(index)\\n    })\\n  }\\n\\n  // 通知所有监听器数据变化\\n  notifyDataChange(index: number): void {\\n    this.listeners.forEach(listener => {\\n      listener.onDataChange(index)\\n    })\\n  }\\n\\n  // 通知所有监听器数据删除\\n  notifyDataDelete(index: number): void {\\n    this.listeners.forEach(listener => {\\n      listener.onDataDelete(index)\\n    })\\n  }\\n\\n  // 通知所有监听器数据移动\\n  notifyDataMove(from: number, to: number): void {\\n    this.listeners.forEach(listener => {\\n      listener.onDataMove(from, to)\\n    })\\n  }\\n\\n  // 通知所有监听器数据集变化\\n  notifyDatasetChange(operations: DataOperation[]): void {\\n    this.listeners.forEach(listener => {\\n      listener.onDatasetChange(operations);\\n    })\\n  }\\n\\n  // 获取数据总数\\n  public totalCount(): number {\\n    return this.dataArray.length\\n  }\\n\\n  // 注册数据变化监听器\\n  registerDataChangeListener(listener: DataChangeListener): void {\\n    if (this.listeners.indexOf(listener) < 0) {\\n      this.listeners.push(listener)\\n    }\\n  }\\n\\n  // 注销数据变化监听器\\n  unregisterDataChangeListener(listener: DataChangeListener): void {\\n    const pos = this.listeners.indexOf(listener)\\n    if (pos >= 0) {\\n      this.listeners.splice(pos, 1)\\n    }\\n  }\\n\\n  // 在数据数组头部添加一个新项\\n  public add1stItem(): void {\\n    this.dataArray.splice(0, 0, this.dataArray.length)\\n    this.notifyDataAdd(0)\\n  }\\n\\n  // 在数据数组尾部添加一个新项\\n  public addLastItem(): void {\\n    this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length)\\n    this.notifyDataAdd(this.dataArray.length - 1)\\n  }\\n\\n  // 在指定索引位置添加一个新项\\n  public addItem(index: number): void {\\n    this.dataArray.splice(index, 0, this.dataArray.length)\\n    this.notifyDataAdd(index)\\n  }\\n\\n  // 删除数据数组头部的一个项\\n  public delete1stItem(): void {\\n    this.dataArray.splice(0, 1)\\n    this.notifyDataDelete(0)\\n  }\\n\\n  // 删除数据数组第二个项\\n  public delete2ndItem(): void {\\n    this.dataArray.splice(1, 1)\\n    this.notifyDataDelete(1)\\n  }\\n\\n  // 删除数据数组尾部的一个项\\n  public deleteLastItem(): void {\\n    this.dataArray.splice(-1, 1)\\n    this.notifyDataDelete(this.dataArray.length)\\n  }\\n\\n  // 删除指定索引位置的一个项\\n  public deleteItem(index: number): void {\\n    this.dataArray.splice(index, 1)\\n    this.notifyDataDelete(index)\\n  }\\n\\n  // 重新加载数据\\n  public reload(): void {\\n    this.dataArray.splice(1, 1)\\n    this.dataArray.splice(3, 2)\\n    this.notifyDataReload()\\n  }\\n}\\n\\n// WaterFlowDemo.ets\\nimport { WaterFlowDataSource } from './WaterFlowDataSource'\\n\\n@Entry\\n@Component\\nstruct WaterFlowDemo {\\n  @State minSize: number = 80\\n  @State maxSize: number = 180\\n  @State fontSize: number = 24\\n  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]\\n  scroller: Scroller = new Scroller()\\n  dataSource: WaterFlowDataSource = new WaterFlowDataSource()\\n  private itemWidthArray: number[] = []\\n  private itemHeightArray: number[] = []\\n\\n  // 获取随机大小\\n  getSize() {\\n    let ret = Math.floor(Math.random() * this.maxSize)\\n    return (ret > this.minSize ? ret : this.minSize)\\n  }\\n\\n  // 设置数据项的宽度和高度数组\\n  setItemSizeArray() {\\n    for (let i = 0; i < 100; i++) {\\n      this.itemWidthArray.push(this.getSize())\\n      this.itemHeightArray.push(this.getSize())\\n    }\\n  }\\n\\n  // 组件即将显示时调用，初始化数据项大小\\n  aboutToAppear() {\\n    this.setItemSizeArray()\\n  }\\n\\n  // 创建数据项的尾部组件\\n  @Builder\\n  itemFoot() {\\n    Column() {\\n      Text(`Footer`)\\n        .fontSize(10)\\n        .backgroundColor(Color.Red)\\n        .width(50)\\n        .height(50)\\n        .align(Alignment.Center)\\n        .margin({ top: 2 })\\n    }\\n  }\\n\\n  // 构建主界面\\n  build() {\\n    Column({ space: 2 }) {\\n      WaterFlow() {\\n        LazyForEach(this.dataSource, (item: number) => {\\n          FlowItem() {\\n            Column() {\\n              Text(\"N\" + item).fontSize(12).height('16')\\n\\n              Image('res/waterFlowTest(' + item % 5 + ').jpg')\\n                .objectFit(ImageFit.Fill)\\n                .width('100%')\\n                .layoutWeight(1)\\n            }\\n          }\\n          .onAppear(() => {\\n            // 当滚动到接近底部时，动态加载更多数据\\n            if (item + 20 == this.dataSource.totalCount()) {\\n              for (let i = 0; i < 100; i++) {\\n                this.dataSource.addLastItem()\\n              }\\n            }\\n          })\\n          .width('100%')\\n          .height(this.itemHeightArray[item % 100])\\n          .backgroundColor(this.colors[item % 5])\\n        }, (item: string) => item)\\n      }\\n      .columnsTemplate(\"1fr 1fr\")\\n      .columnsGap(10)\\n      .rowsGap(5)\\n      .backgroundColor(0xFAEEE0)\\n      .width('100%')\\n      .height('100%')\\n      .onReachStart(() => {\\n        console.info('waterFlow reach start')\\n      })\\n      .onScrollStart(() => {\\n        console.info('waterFlow scroll start')\\n      })\\n      .onScrollStop(() => {\\n        console.info('waterFlow scroll stop')\\n      })\\n      .onScrollFrameBegin((offset: number, state: ScrollState) => {\\n        console.info('waterFlow scrollFrameBegin offset: ' + offset + ' state: ' + state.toString())\\n        return { offsetRemain: offset }\\n      })\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n1. 创建一个可复用的组件 `ReusableFlowItem`，用于显示单个水流项。\\n2. 定义一个主组件 `WaterFlowDemo`，包含多个按钮用于操作水流布局的不同部分。\\n3. 使用 `WaterFlow` 组件来展示水流布局，并通过 `LazyForEach` 动态加载数据。\\n4. 实现按钮功能，包括添加、更新、删除和查看水流布局的各个部分。\\n5. 通过 `onScrollIndex` 事件处理滚动加载更多数据的功能。\\n\\n总体功能与效果描述：\\n该示例展示了如何使用 `WaterFlow` 组件来创建一个动态的水流布局，支持通过按钮进行布局的添加、更新、删除和查看操作，并实现滚动加载更多数据的功能。\\n*/\\n\\n// WaterFlowDemo.ets\\n\\nimport { WaterFlowDataSource } from './WaterFlowDataSource'\\n\\n@Reusable\\n@Component\\nstruct ReusableFlowItem {\\n  @State item: number = 0\\n\\n  // 当组件即将被复用时，更新组件的状态\\n  aboutToReuse(params: Record<string, number>) {\\n    this.item = params.item;\\n    console.info('Reuse item:' + this.item)\\n  }\\n\\n  // 当组件即将显示时，输出新项的信息\\n  aboutToAppear() {\\n    console.info('new item:' + this.item)\\n  }\\n\\n  // 构建组件的UI\\n  build() {\\n    Image('res/waterFlowTest(' + this.item % 5 + ').jpg')\\n      .overlay('N' + this.item, { align: Alignment.Top })\\n      .objectFit(ImageFit.Fill)\\n      .width('100%')\\n      .layoutWeight(1)\\n  }\\n}\\n\\n@Entry\\n@Component\\nstruct WaterFlowDemo {\\n  minSize: number = 80\\n  maxSize: number = 180\\n  fontSize: number = 24\\n  colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]\\n  scroller: Scroller = new Scroller()\\n  dataSource: WaterFlowDataSource = new WaterFlowDataSource()\\n  dataCount: number = this.dataSource.totalCount()\\n  private itemHeightArray: number[] = []\\n  @State sections: WaterFlowSections = new WaterFlowSections()\\n  sectionMargin: Margin = { top: 10, left: 5, bottom: 10, right: 5 }\\n  oneColumnSection: SectionOptions = {\\n    itemsCount: 4,\\n    crossCount: 1,\\n    columnsGap: '5vp',\\n    rowsGap: 10,\\n    margin: this.sectionMargin,\\n    onGetItemMainSizeByIndex: (index: number) => {\\n      return this.itemHeightArray[index % 100]\\n    }\\n  }\\n  twoColumnSection: SectionOptions = {\\n    itemsCount: 2,\\n    crossCount: 2,\\n    onGetItemMainSizeByIndex: (index: number) => {\\n      return 100\\n    }\\n  }\\n  lastSection: SectionOptions = {\\n    itemsCount: 20,\\n    crossCount: 2,\\n    onGetItemMainSizeByIndex: (index: number) => {\\n      return this.itemHeightArray[index % 100]\\n    }\\n  }\\n\\n  // 获取随机大小\\n  getSize() {\\n    let ret = Math.floor(Math.random() * this.maxSize)\\n    return (ret > this.minSize ? ret : this.minSize)\\n  }\\n\\n  // 设置项的大小数组\\n  setItemSizeArray() {\\n    for (let i = 0; i < 100; i++) {\\n      this.itemHeightArray.push(this.getSize())\\n    }\\n  }\\n\\n  // 当组件即将显示时，初始化数据\\n  aboutToAppear() {\\n    this.setItemSizeArray()\\n\\n    let sectionOptions: SectionOptions[] = []\\n    let count = 0\\n    let oneOrTwo = 0\\n    while (count < this.dataCount) {\\n      if (this.dataCount - count < 20) {\\n        this.lastSection.itemsCount = this.dataCount - count\\n        sectionOptions.push(this.lastSection)\\n        break;\\n      }\\n      if (oneOrTwo++ % 2 == 0) {\\n        sectionOptions.push(this.oneColumnSection)\\n        count += this.oneColumnSection.itemsCount\\n      } else {\\n        sectionOptions.push(this.twoColumnSection)\\n        count += this.twoColumnSection.itemsCount\\n      }\\n    }\\n    this.sections.splice(0, 0, sectionOptions)\\n  }\\n\\n  build() {\\n    Column({ space: 2 }) {\\n      Row() {\\n        Button('splice')\\n          .height('5%')\\n          .onClick(() => {\\n            let totalCount: number = this.dataSource.totalCount()\\n            let newSection: SectionOptions = {\\n              itemsCount: totalCount,\\n              crossCount: 2,\\n              onGetItemMainSizeByIndex: (index: number) => {\\n                return this.itemHeightArray[index % 100]\\n              }\\n            }\\n            let oldLength: number = this.sections.length()\\n            this.sections.splice(0, oldLength, [newSection])\\n          })\\n          .margin({ top: 10, left: 20 })\\n        Button('update')\\n          .height('5%')\\n          .onClick(() => {\\n            let newSection: SectionOptions = {\\n              itemsCount: 6,\\n              crossCount: 3,\\n              columnsGap: 5,\\n              rowsGap: 10,\\n              margin: this.sectionMargin,\\n              onGetItemMainSizeByIndex: (index: number) => {\\n                return this.itemHeightArray[index % 100]\\n              }\\n            }\\n            this.dataSource.addItem(this.oneColumnSection.itemsCount)\\n            this.dataSource.addItem(this.oneColumnSection.itemsCount + 1)\\n            this.dataSource.addItem(this.oneColumnSection.itemsCount + 2)\\n            this.dataSource.addItem(this.oneColumnSection.itemsCount + 3)\\n            const result: boolean = this.sections.update(1, newSection)\\n            console.info('update:' + result)\\n          })\\n          .margin({ top: 10, left: 20 })\\n        Button('delete')\\n          .height('5%')\\n          .onClick(() => {\\n            let newSection: SectionOptions = {\\n              itemsCount: 2,\\n              crossCount: 2,\\n              columnsGap: 5,\\n              rowsGap: 10,\\n              margin: this.sectionMargin,\\n              onGetItemMainSizeByIndex: (index: number) => {\\n                return this.itemHeightArray[index % 100]\\n              }\\n            }\\n            this.dataSource.deleteItem(this.oneColumnSection.itemsCount)\\n            this.dataSource.deleteItem(this.oneColumnSection.itemsCount)\\n            this.dataSource.deleteItem(this.oneColumnSection.itemsCount)\\n            this.dataSource.deleteItem(this.oneColumnSection.itemsCount)\\n            this.sections.update(1, newSection)\\n          })\\n          .margin({ top: 10, left: 20 })\\n        Button('values')\\n          .height('5%')\\n          .onClick(() => {\\n            const sections: Array<SectionOptions> = this.sections.values();\\n            for (const value of sections) {\\n              console.log(JSON.stringify(value));\\n            }\\n            console.info('count:' + this.sections.length())\\n          })\\n          .margin({ top: 10, left: 20 })\\n      }.margin({ bottom: 20 })\\n\\n      WaterFlow({ scroller: this.scroller, sections: this.sections }) {\\n        LazyForEach(this.dataSource, (item: number) => {\\n          FlowItem() {\\n            ReusableFlowItem({ item: item })\\n          }\\n          .width('100%')\\n          .backgroundColor(this.colors[item % 5])\\n        }, (item: string) => item)\\n      }\\n      .columnsTemplate('1fr 1fr')\\n      .columnsGap(10)\\n      .rowsGap(5)\\n      .backgroundColor(0xFAEEE0)\\n      .width('100%')\\n      .height('100%')\\n      .layoutWeight(1)\\n      .onScrollIndex((first: number, last: number) => {\\n        if (last + 20 >= this.dataSource.totalCount()) {\\n          for (let i = 0; i < 100; i++) {\\n            this.dataSource.addLastItem()\\n          }\\n          const sections: Array<SectionOptions> = this.sections.values();\\n          let newSection: SectionOptions = sections[this.sections.length() - 1];\\n          newSection.itemsCount += 100;\\n          this.sections.update(-1, newSection);\\n        }\\n      })\\n    }\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "WithTheme": {
        "description": "WithTheme组件用于设置应用局部页面自定义主题风格，可设置子组件深浅色模式和自定义配色。",
        "details": None,
        "interfaces": [
            {
                "description": "WithTheme(options: WithThemeOptions)",
                "params": {
                    "options": {
                        "type": "WithThemeOptions",
                        "required": False,
                        "description": "设置WithTheme作用域内组件缺省样式及深浅色模式。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "WithThemeOptions": {
                "description": "设置WithTheme作用域内组件缺省样式及深浅色模式。",
                "params": {
                    "theme": {
                        "type": "CustomTheme",
                        "required": False,
                        "description": "用于自定义WithTheme作用域内组件缺省配色。",
                        "default": None
                    },
                    "colorMode": {
                        "type": "ThemeColorMode",
                        "required": False,
                        "description": "用于指定WithTheme作用域内组件深浅色模式。",
                        "default": "ThemeColorMode.System"
                    }
                }
            }
        },
        "events": {},
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中设置局部深浅色模式。通过创建dark.json资源文件，并在代码中引用这些资源，实现深浅色模式的切换。\\n\\n总体功能与效果描述：\\n通过配置dark.json文件，使得应用在深色模式和浅色模式下显示不同的颜色和样式。用户可以根据系统或应用的设置，动态切换深浅色模式。\\n*/\\n\\n// main.ets\\n@Entry\\n@Component\\nstruct LocalDarkModeExample {\\n  @State isDarkMode: boolean = false; // 定义一个状态变量，用于控制深浅色模式\\n\\n  build() {\\n    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {\\n      Text('Hello World')\\n        .fontSize(50)\\n        .fontColor(this.isDarkMode ? Color.White : Color.Black) // 根据深浅色模式设置文本颜色\\n        .backgroundColor(this.isDarkMode ? Color.Black : Color.White) // 根据深浅色模式设置背景颜色\\n\\n      Button('Toggle Dark Mode')\\n        .onClick(() => {\\n          this.isDarkMode = !this.isDarkMode; // 切换深浅色模式\\n        })\\n    }\\n    .width('100%')\\n    .height('100%')\\n  }\\n}\\n\\n// dark.json\\n{\\n  \"color\": {\\n    \"background\": \"#000000\", // 深色模式下的背景颜色\\n    \"text\": \"#FFFFFF\" // 深色模式下的文本颜色\\n  }\\n}"
        ],
        "is_common_attrs": True
    }
}
