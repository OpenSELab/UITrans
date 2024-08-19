CONTAINER_COMPONENT = {
    "Badge": {"description": "可以附加在单个组件上用于信息标记的容器组件，支持单个子组件。"},
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
    "ColumnSplit": {"description": "将子组件纵向布局，并在每个子组件之间插入一根横向的分割线，可以包含子组件。"},
    "Counter": {"description": "计数器组件，提供相应的增加或者减少的计数操作，可以包含子组件。"},
    "EmbeddedComponent": {
        "description": "EmbeddedComponent用于支持在当前页面嵌入本应用内其他EmbeddedUIExtensionAbility提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，完成页面布局和渲染，通常用于有进程隔离诉求的模块化开发场景。"
    },
    "Flex": {"description": "以弹性方式布局子组件的容器组件，可以包含子组件。"},
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
        "description": "列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本，仅支持ListItem、ListItemGroup子组件。"},
    "ListItem": {"description": "用来展示列表具体item，必须配合List来使用，可以包含单个子组件。"},
    "ListItemGroup": {
        "description": "该组件用来展示列表item分组，宽度默认充满List组件，必须配合List组件来使用，包含ListItem子组件。"},
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
        "description": "瀑布流容器，由“行”和“列”分割的单元格所组成，通过容器自身的排列规则，将不同大小的“项目”自上而下，如瀑布般紧密布局，仅支持FlowItem子组件。"},
    "WithTheme": {
        "description": "WithTheme组件用于设置应用局部页面自定义主题风格，可设置子组件深浅色模式和自定义配色，支持单个子组件。"}
}
