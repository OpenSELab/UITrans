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
    "GridCol": {"description": "栅格子组件，必须作为栅格容器组件(GridRow)的子组件使用，可以包含单个子组件。"},
    "GridRow": {
        "description": "栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题，保证不同设备上各个模块的布局一致性，栅格容器组件，仅可以和栅格子组件(GridCol)在栅格布局场景中使用，可以包含GridCol子组件。"},
    "Grid": {
        "description": "网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局，仅支持GridItem子组件。"},
    "GridItem": {"description": "网格容器中单项内容容器，可以包含单个子组件。"},
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
        "该组件从API Version 9开始支持。",
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
        "description": "相对布局组件，用于复杂场景中元素对齐的布局，支持多个子组件。",
        "details": "规则说明\n----\n\n*   容器内子组件区分水平方向，垂直方向：\n    *   水平方向为left， middle， right，对应容器的HorizontalAlign.Start， HorizontalAlign.Center， HorizontalAlign.End。\n    *   垂直方向为top， center， bottom，对应容器的VerticalAlign.Top， VerticalAlign.Center， VerticalAlign.Bottom。\n*   子组件可以将容器、guideline、barrier或者其他子组件设为锚点：\n    *   参与相对布局的容器内组件，不设置id的组件能显示，但是不能被其他子组件作为锚点，相对布局容器会为其拼接id，此id的规律无法被应用感知；容器id固定为\_\_container\_\_；guideline和barrier的id不能与组件重复，重复的话按照组件 > guideline > barrier的优先级生效。\n    *   此子组件某一方向上的三个位置（水平方向为left、middle、right，垂直方向为top、center、bottom）可以指定容器或其他子组件同方向的三个位置（水平方向为HorizontalAlign.Start、HorizontalAlign.Center、HorizontalAlign.End，垂直方向为VerticalAlign.Top、VerticalAlign.Center、VerticalAlign.Bottom）为锚点。若同方向上设置两个以上锚点，水平方向Start和Center优先，垂直方向Top和Center优先。例如，水平方向上指定了left以容器的HorizontalAlign.Start为锚点，middle以容器的HorizontalAlign.Center为锚点，又指定right的锚点为容器的HorizontalAlign.End，当组件的width和容器的width不能同时满足3条约束规则时，优先取Start和Center的约束规则。\n    *   当同时存在前端页面设置的子组件尺寸和相对布局规则时，子组件的绘制尺寸取决于约束规则。从API Version 11开始，该规则发生变化，子组件绘制尺寸取决于前端页面设置的尺寸。\n    *   对齐后需要额外偏移可设置offset(API Version 11上新增了[bias](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-universal-attributes-location-V5#bias%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)， 不建议再使用offset)。\n    *   从API Version 11开始，在RelativeContainer组件中，width、height设置auto表示自适应子组件。\n    *   当width设置auto时，如果水平方向上子组件以容器作为锚点，则auto不生效，垂直方向上同理。\n    *   相对布局容器内的子组件的margin含义不同于通用属性的margin，其含义为到该方向上的锚点的距离。若该方向上没有锚点，则该方向的margin不生效。\n    *   guideline的位置在不声明或者声明异常值(如undefined)时，取start：0的位置；start和end两种方式声明一种即可，同时声明时仅start生效。\n    *   当容器在某个方向的size声明为“auto”时，该方向上guideline的位置只能使用start的方式声明(不可使用百分比)。\n    *   垂直方向的guideline和barrier只能作为组件水平方向的锚点，作为垂直方向的锚点时取0；水平方向的guideline和barrier只能作为组件垂直方向的锚点，作为水平方向的锚点时取0。\n    *   链的形成依靠组件间的依赖关系。以一个组件A、组件B组成的最小水平链为例，需要有锚点1 <-- 组件A <---> 组件B --> 锚点2的依赖关系，即A具有left锚点，B具有right锚点，同时A的right锚点是B的HorizontalAlign.Start，B的left锚点是A的HorizontalAlign.End。\n    *   链的方向和格式声明在链头组件的[chainMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-universal-attributes-location-V5#chainmode12)接口；链内元素的bias属性全部失效，链头元素的bias作为整个链的bias生效。\n    *   链内所有元素的size如果超出链的锚点约束，超出的部分将均分在链的两侧。在[Packed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-appendix-enums-V5#chainstyle12)链中，超出部分的分布可以通过[bias](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/ts-universal-attributes-location-V5#bias%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)来设置。\n*   特殊情况\n    *   根据约束条件和子组件本身的size属性无法确定子组件大小，则子组件不绘制。\n    *   互相依赖、环形依赖时容器内子组件全部不绘制。\n    *   同方向上两个及以上位置设置锚点但锚点位置逆序时此子组件大小为0，即不绘制。",
        "interfaces": [
            {
                "description": "创建RelativeContainer组件。",
                "params": {}
            }
        ],
        "attributes": {
            "guideLine": {
                "description": "设置RelativeContainer容器内的辅助线，Array中每个项目即为一条guideline。",
                "params": {
                    "value": {
                        "type": "Array<GuideLineStyle>",
                        "required": True,
                        "description": "RelativeContainer容器内的辅助线。"
                    }
                }
            },
            "barrier": {
                "description": "设置RelativeContainer容器内的屏障，Array中每个项目即为一条barrier。",
                "params": {
                    "value": {
                        "type": "Array<BarrierStyle>",
                        "required": True,
                        "description": "RelativeContainer容器内的屏障。"
                    }
                }
            }
        },
        "events": {},
        "examples": [
            "示例1：以容器和容器内组件作为锚点进行布局的用法。",
            "示例2：容器内子组件设置margin的用法。",
            "示例3：容器大小适应内容（声明size为\"auto\"）的用法。",
            "示例4：bias的用法。",
            "示例5：guideline的声明和以guideline为锚点的用法。",
            "示例6：barrier的声明和以barrier为锚点的用法。",
            "示例7：通过chainMode接口实现了水平方向的SPREAD链。",
            "示例8：通过chainMode接口实现了水平方向的SPREAD_INSIDE链。",
            "示例9：通过chainMode接口实现了水平方向的PACKED链。",
            "示例10：通过chainMode和bias接口实现了水平方向的带bias的PACKED链。",
            "示例11：在RTL模式下以barrier为锚点时使用LocalizedAlignRuleOptions和LocalizedBarrierDirection设置对齐方式的用法。"
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
        "description": "通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图，不支持自定义组件作为子组件， 仅可包含子组件TabContent。"},
    "TabContent": {"description": "仅在Tabs中使用，对应一个切换页签的内容视图，支持单个子组件。"},
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
