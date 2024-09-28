ADVANCED_COMPONENT = {
    "ChipGroup": {
        "description": "ChipGroup高级组件，提供操作块群组，用于对文件或者资源内容进行分类等场景。",
        "details": None,
        "interfaces": [
            {
                "description": "ChipGroup({ items, itemStyle, selectedIndexes, multiple, chipGroupSpace, chipGroupPadding, onChange, suffix })",
                "params": {
                    "items": {
                        "type": "ChipGroupItemOptions[]",
                        "required": True,
                        "description": "定义每个chip的非共通属性。",
                        "default": None
                    },
                    "itemStyle": {
                        "type": "ChipItemStyle",
                        "required": False,
                        "description": "定义chip的共通属性。",
                        "default": None
                    },
                    "selectedIndexes": {
                        "type": "Array<number>",
                        "required": False,
                        "description": "选中的chip索引数组。",
                        "default": None
                    },
                    "multiple": {
                        "type": "boolean",
                        "required": False,
                        "description": "是否允许多选。",
                        "default": None
                    },
                    "chipGroupSpace": {
                        "type": "ChipGroupSpaceOptions",
                        "required": False,
                        "description": "定义chipGroup左右内边距，以及chip与chip之间的间距。",
                        "default": None
                    },
                    "chipGroupPadding": {
                        "type": "ChipGroupPaddingOptions",
                        "required": False,
                        "description": "定义chipGroup上下内边距，以便控制chipGroup的整体高度。",
                        "default": None
                    },
                    "onChange": {
                        "type": "(selectedIndexes: Array<number>) => void",
                        "required": False,
                        "description": "选中状态改变时的回调函数。",
                        "default": None
                    },
                    "suffix": {
                        "type": "Callback<void>",
                        "required": False,
                        "description": "suffix接口，使用时需要引入IconGroupSuffix接口，不传入的情况，没有suffix。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "ChipGroupItemOptions": {
                "description": "定义每个chip的非共通属性。",
                "params": {
                    "suffixIcon": {
                        "type": "IconOptions",
                        "required": False,
                        "description": "suffixIcon有传入参数时，allowClose不生效，suffixIcon没有传入参数时，allowClose决定是否显示删除图标。",
                        "default": None
                    }
                }
            },
            "ChipItemStyle": {
                "description": "定义chip的共通属性。",
                "params": {
                    "size": {
                        "type": "ChipSize",
                        "required": False,
                        "description": "chip尺寸，默认值：ChipSize.NORMAL。",
                        "default": None
                    },
                    "backgroundColor": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "chip背景颜色，默认值：$r('sys.color.ohos_id_color_button_normal')。",
                        "default": None
                    },
                    "fontColor": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "chip文字颜色，默认值：$r('sys.color.ohos_id_color_text_primary')。",
                        "default": None
                    },
                    "selectedFontColor": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "chip激活时的文字颜色，默认值：$r('sys.color.ohos_id_color_text_primary_contrary')。",
                        "default": None
                    },
                    "selectedBackgroundColor": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "chip激活时的背景颜色，默认值：$r('sys.color.ohos_id_color_emphasize')。",
                        "default": None
                    }
                }
            },
            "ChipGroupSpaceOptions": {
                "description": "定义chipGroup左右内边距，以及chip与chip之间的间距。",
                "params": {
                    "itemSpace": {
                        "type": [
                            "string",
                            "number"
                        ],
                        "required": False,
                        "description": "chip与chip之间的间距，默认值：8，单位：vp。",
                        "default": None
                    },
                    "startSpace": {
                        "type": "Length",
                        "required": False,
                        "description": "左侧内边距，默认值：16，单位：vp。",
                        "default": None
                    },
                    "endSpace": {
                        "type": "Length",
                        "required": False,
                        "description": "右侧内边距，默认值：16，单位：vp。",
                        "default": None
                    }
                }
            },
            "ChipGroupPaddingOptions": {
                "description": "定义chipGroup上下内边距，以便控制chipGroup的整体高度。",
                "params": {
                    "top": {
                        "type": "Length",
                        "required": False,
                        "description": "chipGroup的上方内边距，默认值：14，单位：vp。",
                        "default": None
                    },
                    "bottom": {
                        "type": "Length",
                        "required": False,
                        "description": "chipGroup的下方内边距，默认值：14，单位：vp。",
                        "default": None
                    }
                }
            }
        },
        "events": {
            "onChange": {
                "description": "选中状态改变时的回调函数。",
                "params": {
                    "selectedIndexes": {
                        "type": "Array<number>",
                        "required": False,
                        "description": "选中的chip索引数组。",
                        "default": None
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何使用ChipGroup组件来创建一组操作块（Chip），并配置其样式和行为。每个Chip可以包含前缀图标、标签、后缀图标，并支持关闭操作。ChipGroup支持单选和多选模式，并提供了样式和间距的自定义选项。\\n\\n总体功能与效果描述：\\n该示例创建了一个ChipGroup，包含六个Chip，每个Chip具有不同的前缀图标和标签。ChipGroup的样式和行为通过属性进行配置，包括大小、背景色、字体颜色、选中状态的样式、选择模式、间距和内边距等。ChipGroup还支持点击事件，可以在点击Chip时输出激活的Chip索引。\\n*/\\n\\n// Index.ets\\nimport { ChipSize, ChipGroup } from '@kit.ArkUI'\\n\\n@Entry\\n@Preview\\n@Component\\nstruct Index {\\n  @State selected_index: Array<number> = [0, 1, 2, 3, 4, 5, 6] // 初始选中Chip的索引数组\\n\\n  build() {\\n    Column() {\\n      ChipGroup({\\n        items: [\\n          {\\n            prefixIcon: { src: $r('app.media.icon') }, // 设置Chip的前缀图标\\n            label: { text: \"操作块1\" }, // 设置Chip的标签文本\\n            suffixIcon: { src: $r('sys.media.ohos_ic_public_cut') }, // 设置Chip的后缀图标\\n            allowClose: False // 禁止关闭Chip\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_copy') },\\n            label: { text: \"操作块2\" },\\n            allowClose: True // 允许关闭Chip\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },\\n            label: { text: \"操作块3\" },\\n            allowClose: True\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },\\n            label: { text: \"操作块4\" },\\n            allowClose: True\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },\\n            label: { text: \"操作块5\" },\\n            allowClose: True\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },\\n            label: { text: \"操作块6\" },\\n            allowClose: True\\n          },\\n        ],\\n        itemStyle: {\\n          size: ChipSize.SMALL, // 设置Chip的大小\\n          backgroundColor: $r('sys.color.ohos_id_color_button_normal'), // 设置Chip的背景色\\n          fontColor: $r('sys.color.ohos_id_color_text_primary'), // 设置Chip的字体颜色\\n          selectedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'), // 设置选中Chip的背景色\\n          selectedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'), // 设置选中Chip的字体颜色\\n        },\\n        selectedIndexes: this.selected_index, // 设置初始选中的Chip索引\\n        multiple: False, // 设置为单选模式\\n        chipGroupSpace: { itemSpace: 8, endSpace: 0 }, // 设置Chip之间的间距\\n        chipGroupPadding: { top: 10, bottom: 10 }, // 设置ChipGroup的内边距\\n        onChange: (activatedChipsIndex:Array<number>) => {\\n          console.log('chips on clicked, activated index ' + activatedChipsIndex) // 点击Chip时输出激活的Chip索引\\n        },\\n      })\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用ChipGroup和IconGroupSuffix组件，通过传入SymbolGlyph资源来实现带有图标的操作块组。\\n总体功能与效果描述：\\n该示例创建了一个包含多个操作块的ChipGroup，每个操作块可以有前缀和后缀图标，并且支持多选功能。同时，通过IconGroupSuffix组件实现了一个后缀图标组，点击后可以切换操作块的选择状态。\\n*/\\n\\n// Index.ets\\nimport { ChipSize, ChipGroup, IconGroupSuffix, SymbolGlyphModifier } from '@kit.ArkUI'\\n\\n@Entry\\n@Preview\\n@Component\\nstruct Index {\\n  @State selected_index: Array<number> = [0, 1, 2, 3, 4, 5, 6]; // 初始选中索引数组\\n  @State selected_state: boolean = true; // 初始选中状态\\n  @State prefixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star')); // 前缀图标正常状态\\n  @State prefixModifierActivated: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]); // 前缀图标激活状态\\n  @State suffixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')); // 后缀图标正常状态\\n  @State suffixModifierActivated: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontColor([Color.Red]); // 后缀图标激活状态\\n\\n  @LocalBuilder\\n  ChipGroupSuffix(): void {\\n    IconGroupSuffix({\\n      items: [\\n        new SymbolGlyphModifier($r('sys.symbol.magnifyingglass'))\\n          .onClick(() => {\\n            if (this.selected_state == False) {\\n              this.selected_index = [0, 1, 2, 3, 4, 5, 6]; // 切换选中状态，选中所有操作块\\n              this.selected_state = true;\\n            } else {\\n              this.selected_index = []; // 切换选中状态，取消所有操作块的选中\\n              this.selected_state = False;\\n            }\\n          })\\n      ]\\n    })\\n  }\\n\\n  build() {\\n    Column() {\\n      ChipGroup({\\n        items: [\\n          {\\n            prefixSymbol: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated }, // 操作块1的前缀图标\\n            label: { text: \"操作块1\" }, // 操作块1的标签\\n            suffixSymbol: { normal: this.suffixModifierNormal, activated: this.suffixModifierActivated }, // 操作块1的后缀图标\\n            allowClose: False, // 操作块1不允许关闭\\n          },\\n          {\\n            prefixSymbol: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated }, // 操作块2的前缀图标\\n            label: { text: \"操作块2\" }, // 操作块2的标签\\n            allowClose: True, // 操作块2允许关闭\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') }, // 操作块3的前缀图标\\n            label: { text: \"操作块3\" }, // 操作块3的标签\\n            allowClose: True, // 操作块3允许关闭\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') }, // 操作块4的前缀图标\\n            label: { text: \"操作块4\" }, // 操作块4的标签\\n            allowClose: True, // 操作块4允许关闭\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') }, // 操作块5的前缀图标\\n            label: { text: \"操作块5\" }, // 操作块5的标签\\n            allowClose: True, // 操作块5允许关闭\\n          },\\n          {\\n            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') }, // 操作块6的前缀图标\\n            label: { text: \"操作块6\" }, // 操作块6的标签\\n            allowClose: True, // 操作块6允许关闭\\n          },\\n        ],\\n        itemStyle: {\\n          size: ChipSize.NORMAL, // 操作块大小\\n          backgroundColor: $r('sys.color.ohos_id_color_button_normal'), // 操作块背景颜色\\n          fontColor: $r('sys.color.ohos_id_color_text_primary'), // 操作块文字颜色\\n          selectedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'), // 选中操作块背景颜色\\n          selectedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'), // 选中操作块文字颜色\\n        },\\n        selectedIndexes: this.selected_index, // 初始选中索引\\n        multiple: True, // 支持多选\\n        chipGroupSpace: { itemSpace: 8, endSpace: 0 }, // 操作块间距\\n        chipGroupPadding: { top: 10, bottom: 10 }, // 操作块组内边距\\n        onChange: (activatedChipsIndex: Array<number>) => {\\n          console.log('chips on clicked, activated index ' + activatedChipsIndex) // 点击操作块时的回调\\n        },\\n        suffix: this.ChipGroupSuffix // 操作块组的后缀图标组\\n      })\\n    }\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "Chip": {
        "description": "操作块组件，用于搜索框历史记录或者邮件发送列表等场景。",
        "details": None,
        "interfaces": [
            {
                "description": "Chip({options: ChipOptions})",
                "params": {
                    "options": {
                        "type": "ChipOptions",
                        "required": True,
                        "description": "定义chip组件的参数。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "size": {
                "description": "操作块尺寸。",
                "params": {
                    "size": {
                        "type": [
                            "ChipSize",
                            "SizeOptions"
                        ],
                        "required": False,
                        "description": "操作块尺寸。",
                        "default": "ChipSize.NORMAL"
                    }
                }
            },
            "enabled": {
                "description": "操作块是否可选中。",
                "params": {
                    "enabled": {
                        "type": "boolean",
                        "required": False,
                        "description": "操作块是否可选中。",
                        "default": True
                    }
                }
            },
            "activated": {
                "description": "操作块是否为激活态。",
                "params": {
                    "activated": {
                        "type": "boolean",
                        "required": False,
                        "description": "操作块是否为激活态。",
                        "default": False
                    }
                }
            },
            "prefixIcon": {
                "description": "前缀图标属性。",
                "params": {
                    "prefixIcon": {
                        "type": "PrefixIconOptions",
                        "required": False,
                        "description": "前缀图标属性。",
                        "default": None
                    }
                }
            },
            "prefixSymbol": {
                "description": "前缀图标属性，symbol类型。",
                "params": {
                    "prefixSymbol": {
                        "type": "ChipSymbolGlyphOptions",
                        "required": False,
                        "description": "前缀图标属性，symbol类型。",
                        "default": None
                    }
                }
            },
            "label": {
                "description": "文本属性。",
                "params": {
                    "label": {
                        "type": "LabelOptions",
                        "required": True,
                        "description": "文本属性。",
                        "default": None
                    }
                }
            },
            "suffixIcon": {
                "description": "后缀图标属性。",
                "params": {
                    "suffixIcon": {
                        "type": "SuffixIconOptions",
                        "required": False,
                        "description": "后缀图标属性。",
                        "default": None
                    }
                }
            },
            "suffixSymbol": {
                "description": "后缀图标属性，symbol类型。",
                "params": {
                    "suffixSymbol": {
                        "type": "ChipSymbolGlyphOptions",
                        "required": False,
                        "description": "后缀图标属性，symbol类型。",
                        "default": None
                    }
                }
            },
            "backgroundColor": {
                "description": "操作块背景颜色。",
                "params": {
                    "backgroundColor": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "操作块背景颜色。",
                        "default": "$r('sys.color.ohos_id_color_button_normal')"
                    }
                }
            },
            "activatedBackgroundColor": {
                "description": "操作块激活时的背景颜色。",
                "params": {
                    "activatedBackgroundColor": {
                        "type": "ResourceColor",
                        "required": False,
                        "description": "操作块激活时的背景颜色。",
                        "default": "$r('sys.color.ohos_id_color_emphasize')"
                    }
                }
            },
            "borderRadius": {
                "description": "操作块背景圆角半径大小，不支持百分比。",
                "params": {
                    "borderRadius": {
                        "type": "Dimension",
                        "required": False,
                        "description": "操作块背景圆角半径大小，不支持百分比。",
                        "default": "$r('sys.float.ohos_id_corner_radius_button')"
                    }
                }
            },
            "allowClose": {
                "description": "删除图标是否显示。",
                "params": {
                    "allowClose": {
                        "type": "boolean",
                        "required": False,
                        "description": "删除图标是否显示。",
                        "default": True
                    }
                }
            }
        },
        "events": {
            "onClose": {
                "description": "默认删除图标点击事件。",
                "params": {
                    "onClose": {
                        "type": "() => void",
                        "required": False,
                        "description": "默认删除图标点击事件。",
                        "default": None
                    }
                },
                "returns": None
            },
            "onClicked": {
                "description": "操作块点击事件。",
                "params": {
                    "onClicked": {
                        "type": "() => void",
                        "required": False,
                        "description": "操作块点击事件。",
                        "default": None
                    }
                },
                "returns": None
            },
            "direction": {
                "description": "布局方向。",
                "params": {
                    "direction": {
                        "type": "Direction",
                        "required": False,
                        "description": "布局方向。",
                        "default": "Direction.Auto"
                    }
                },
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何使用鸿蒙ArkUI的Chip组件创建一个不显示删除图标的操作块。通过设置Chip组件的属性，如prefixIcon、label、size等，来定制操作块的外观和行为。\\n\\n总体功能与效果描述：\\n该操作块显示一个带有蓝色图标和文本的Chip组件，文本为“操作块”，并且不显示删除图标。用户无法通过点击删除图标来移除该操作块。\\n*/\\n\\n// Index.ets\\nimport { Chip, ChipSize } from '@kit.ArkUI';\\n\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Column({ space: 10 }) {\\n      Chip({\\n        // 设置Chip的前缀图标\\n        prefixIcon: {\\n          src: $r('app.media.chips'), // 图标的资源路径\\n          size: { width: 16, height: 16 }, // 图标的尺寸\\n          fillColor: Color.Blue // 图标的填充颜色\\n        },\\n        // 设置Chip的标签文本\\n        label: {\\n          text: \"操作块\", // 标签文本内容\\n          fontSize: 12, // 文本字体大小\\n          fontColor: Color.Blue, // 文本颜色\\n          fontFamily: \"HarmonyOS Sans\", // 文本字体\\n          labelMargin: { left: 20, right: 30 } // 文本的左右边距\\n        },\\n        size: ChipSize.SMALL, // Chip的大小，这里设置为小尺寸\\n        allowClose: False, // 不允许显示删除图标\\n        enabled: True, // Chip是否启用\\n        backgroundColor: $r('sys.color.ohos_id_color_button_normal'), // Chip的背景颜色\\n        borderRadius: $r('sys.float.ohos_id_corner_radius_button'), // Chip的边框圆角\\n        onClose:()=>{\\n          console.log(\"chip on close\") // 当Chip被关闭时的回调函数\\n        }\\n      })\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用ArkUI的Chip组件创建一个带有默认删除图标的操作块。通过配置Chip组件的各个属性，如前缀图标、标签文本、尺寸、背景颜色等，实现一个可交互的操作块。\\n\\n总体功能与效果描述：\\n该示例创建了一个带有蓝色前缀图标和蓝色文本标签的操作块，支持关闭功能，且背景颜色和边框圆角根据系统主题进行设置。\\n*/\\n\\n// Index.ets\\nimport { Chip, ChipSize } from '@kit.ArkUI'; // 导入Chip组件及其尺寸枚举\\n\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Column({ space: 10 }) { // 创建一个垂直布局，组件间距为10\\n      Chip({\\n        prefixIcon: {\\n          src: $r('app.media.chips'), // 设置前缀图标的资源路径\\n          size: { width: 16, height: 16 }, // 设置前缀图标的尺寸\\n          fillColor: Color.Blue // 设置前缀图标的填充颜色为蓝色\\n        },\\n        label: {\\n          text: \"操作块\", // 设置标签文本内容\\n          fontSize: 12, // 设置标签文本的字体大小\\n          fontColor: Color.Blue, // 设置标签文本的颜色为蓝色\\n          fontFamily: \"HarmonyOS Sans\", // 设置标签文本的字体族\\n          labelMargin: { left: 20, right: 30 } // 设置标签文本的左右边距\\n        },\\n        size: ChipSize.NORMAL, // 设置Chip组件的尺寸为正常大小\\n        allowClose: True, // 允许Chip组件显示关闭图标\\n        enabled: True, // 启用Chip组件的交互功能\\n        backgroundColor: $r('sys.color.ohos_id_color_button_normal'), // 设置Chip组件的背景颜色\\n        borderRadius: $r('sys.float.ohos_id_corner_radius_button') // 设置Chip组件的边框圆角\\n      })\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用ArkUI的Chip组件创建一个自定义删除图标的操作块。通过配置Chip组件的各个属性，如前缀图标、标签、后缀图标、大小、背景颜色等，实现一个具有特定样式和功能的操作块。\\n\\n总体功能与效果描述：\\n该操作块包含一个前缀图标、文本标签和一个后缀删除图标。用户可以通过点击后缀图标来执行删除操作。操作块的样式和颜色可以根据需求进行自定义。\\n*/\\n\\n// Index.ets\\nimport { Chip, ChipSize } from '@kit.ArkUI';\\n\\n@Entry\\n@Component\\nstruct Index {\\n  build() {\\n    Column({ space: 10 }) {\\n      Chip({\\n        // 配置前缀图标\\n        prefixIcon: {\\n          src: $r('app.media.chips'), // 图标资源路径\\n          size: { width: 16, height: 16 }, // 图标大小\\n          fillColor: Color.Red // 图标填充颜色\\n        },\\n        // 配置标签文本\\n        label: {\\n          text: \"操作块\", // 标签文本内容\\n          fontSize: 12, // 字体大小\\n          fontColor: Color.Blue, // 字体颜色\\n          fontFamily: \"HarmonyOS Sans\", // 字体家族\\n          labelMargin: { left: 20, right: 30 } // 标签文本的左右边距\\n        },\\n        // 配置后缀图标\\n        suffixIcon: {\\n          src: $r('app.media.close'), // 图标资源路径\\n          size: { width: 16, height: 16 }, // 图标大小\\n          fillColor: Color.Red // 图标填充颜色\\n        },\\n        size: ChipSize.NORMAL, // 操作块的大小\\n        allowClose: False, // 是否允许关闭操作块\\n        enabled: True, // 操作块是否启用\\n        backgroundColor: $r('sys.color.ohos_id_color_button_normal'), // 背景颜色\\n        borderRadius: $r('sys.float.ohos_id_corner_radius_button') // 边框圆角\\n      })\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用Chip组件实现一个布局镜像化的操作块。通过设置Chip组件的direction属性为Direction.Rtl，实现从右到左的布局。同时，配置了前缀图标、标签、后缀图标以及各种样式属性，以展示一个完整的Chip组件。\\n\\n总体功能与效果描述：\\n该示例展示了一个从右到左布局的操作块，包含前缀图标、标签和后缀图标，并设置了相应的样式属性，如颜色、大小、边框半径等。\\n*/\\n\\n// ChipPage.ets\\nimport { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';\\n\\n@Entry\\n@Component\\nstruct ChipPage {\\n  @State message: string = 'Hello World';\\n\\n  build() {\\n    Column() {\\n      Chip({\\n        direction: Direction.Rtl, // 设置Chip组件的布局方向为从右到左\\n        prefixIcon: {\\n          src: $r('app.media.chips'), // 设置前缀图标的资源路径\\n          size: { width: 16, height: 16 }, // 设置前缀图标的大小\\n          fillColor: Color.Red, // 设置前缀图标的填充颜色\\n        },\\n        label: {\\n          text: \"操作块\", // 设置标签的文本内容\\n          fontSize: 12, // 设置标签的字体大小\\n          fontColor: Color.Blue, // 设置标签的字体颜色\\n          fontFamily: \"HarmonyOS Sans\", // 设置标签的字体家族\\n          localizedLabelMargin: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) }, // 设置标签的边距\\n        },\\n        suffixIcon: {\\n          src: $r('app.media.close'), // 设置后缀图标的资源路径\\n          size: { width: 16, height: 16 }, // 设置后缀图标的大小\\n          fillColor: Color.Red, // 设置后缀图标的填充颜色\\n        },\\n        size: ChipSize.NORMAL, // 设置Chip组件的大小\\n        allowClose: False, // 设置是否允许关闭Chip组件\\n        enabled: True, // 设置Chip组件是否启用\\n        backgroundColor: $r('sys.color.ohos_id_color_button_normal'), // 设置Chip组件的背景颜色\\n        borderRadius: $r('sys.float.ohos_id_corner_radius_button') // 设置Chip组件的边框半径\\n      })\\n    }.justifyContent(FlexAlign.Center) // 设置Column组件的内容对齐方式为居中\\n    .width('100%') // 设置Column组件的宽度为100%\\n    .height('100%') // 设置Column组件的高度为100%\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用ArkUI的Chip组件创建一个可激活的操作块，并通过按钮改变其激活状态。Chip组件支持自定义图标、文本样式、背景颜色等，并提供了点击和关闭事件的回调。\\n\\n总体功能与效果描述：\\n1. 创建一个Chip组件，显示一个带有图标和文本的操作块。\\n2. 通过按钮切换Chip组件的激活状态，激活状态下Chip的图标和文本颜色会发生变化。\\n3. Chip组件支持点击和关闭事件，点击和关闭时会在控制台输出相应信息。\\n*/\\n\\n// Index.ets\\nimport { Chip, ChipSize } from '@kit.ArkUI';\\n\\n@Entry\\n@Component\\nstruct Index {\\n  @State isActivated: boolean = False; // 定义一个状态变量，用于控制Chip的激活状态\\n\\n  build() {\\n    Column({ space: 10 }) {\\n      Chip({\\n        prefixIcon: {\\n          src: $r('app.media.chips'), // 设置Chip的前缀图标资源路径\\n          size: { width: 16, height: 16 }, // 设置图标的大小\\n          fillColor: Color.Blue, // 设置图标的填充颜色\\n          activatedFillColor: $r('sys.color.ohos_id_color_text_primary_contrary') // 设置激活状态下的图标填充颜色\\n        },\\n        label: {\\n          text: \"操作块\", // 设置Chip的文本内容\\n          fontSize: 12, // 设置文本的字体大小\\n          fontColor: Color.Blue, // 设置文本的颜色\\n          activatedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'), // 设置激活状态下的文本颜色\\n          fontFamily: \"HarmonyOS Sans\", // 设置文本的字体家族\\n          labelMargin: { left: 20, right: 30 } // 设置文本的左右边距\\n        },\\n        size: ChipSize.NORMAL, // 设置Chip的大小为正常尺寸\\n        allowClose: True, // 允许Chip显示关闭按钮\\n        enabled: True, // 启用Chip的交互功能\\n        activated: this.isActivated, // 根据状态变量设置Chip的激活状态\\n        backgroundColor: $r('sys.color.ohos_id_color_button_normal'), // 设置Chip的背景颜色\\n        activatedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'), // 设置激活状态下的背景颜色\\n        borderRadius: $r('sys.float.ohos_id_corner_radius_button'), // 设置Chip的边框圆角\\n        onClose:()=>{\\n          console.log(\"chip on close\") // 定义Chip关闭事件的回调函数\\n        },\\n        onClicked:()=>{\\n          console.log(\"chip on clicked\") // 定义Chip点击事件的回调函数\\n        }\\n      })\\n\\n      Button('改变激活状态').onClick(()=>{\\n        this.isActivated = !this.isActivated; // 定义按钮点击事件的回调函数，切换Chip的激活状态\\n      })\\n    }\\n  }\\n}",
            "/*\\n实现思路：\\n本示例展示了如何使用Chip组件，并通过前缀和后缀图标展示symbol类型资源。通过按钮改变Chip的激活状态，观察图标和文本颜色的变化。\\n\\n总体功能与效果描述：\\n- 展示一个带有前缀图标和后缀图标的Chip组件。\\n- 通过按钮改变Chip的激活状态，观察图标和文本颜色的变化。\\n- 实现Chip的关闭和点击事件。\\n*/\\n\\n// Index.ets\\nimport { Chip, ChipSize, SymbolGlyphModifier } from '@kit.ArkUI';\\n\\n@Entry\\n@Component\\nstruct Index {\\n  @State isActivated: boolean = False; // 定义一个状态变量，用于控制Chip的激活状态\\n\\n  build() {\\n    Column({ space: 10 }) {\\n      Chip({\\n        prefixIcon: {\\n          src: $r('app.media.chips'), // 设置前缀图标的资源路径\\n          size: { width: 16, height: 16 }, // 设置前缀图标的大小\\n          fillColor: Color.Blue, // 设置前缀图标的填充颜色\\n          activatedFillColor: $r('sys.color.ohos_id_color_text_primary_contrary') // 设置激活状态下的前缀图标填充颜色\\n        },\\n        prefixSymbol: {\\n          normal: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Green]), // 设置前缀symbol图标在正常状态下的样式\\n          activated: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Red]), // 设置前缀symbol图标在激活状态下的样式\\n        },\\n        label: {\\n          text: \"操作块\", // 设置Chip的标签文本\\n          fontSize: 12, // 设置标签文本的字体大小\\n          fontColor: Color.Blue, // 设置标签文本的颜色\\n          activatedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'), // 设置激活状态下的标签文本颜色\\n          fontFamily: \"HarmonyOS Sans\", // 设置标签文本的字体家族\\n          labelMargin: { left: 20, right: 30 }, // 设置标签文本的边距\\n        },\\n        size: ChipSize.NORMAL, // 设置Chip的大小\\n        allowClose: True, // 允许Chip关闭\\n        enabled: True, // 启用Chip\\n        activated: this.isActivated, // 设置Chip的激活状态\\n        backgroundColor: $r('sys.color.ohos_id_color_button_normal'), // 设置Chip的背景颜色\\n        activatedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'), // 设置激活状态下的Chip背景颜色\\n        borderRadius: $r('sys.float.ohos_id_corner_radius_button'), // 设置Chip的边框圆角\\n        onClose:()=>{\\n          console.log(\"chip on close\") // 定义Chip关闭事件的处理函数\\n        },\\n        onClicked:()=>{\\n          console.log(\"chip on clicked\") // 定义Chip点击事件的处理函数\\n        }\\n      })\\n\\n      Button('改变激活状态').onClick(()=>{\\n        this.isActivated = !this.isActivated; // 定义按钮点击事件，切换Chip的激活状态\\n      })\\n    }\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "ToolBar": {
        "description": "工具栏用于展示针对当前界面内容的操作选项，在界面底部显示。底部最多显示5个入口，超过则收纳入“更多”子项中，在最右侧显示。",
        "details": "该组件从API Version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。",
        "interfaces": [
            {
                "description": "Toolbar({toolBarList: ToolBarOptions, activateIndex?: number, controller: TabsController})",
                "params": {
                    "toolBarList": {
                        "type": "ToolBarOptions",
                        "required": True,
                        "description": "工具栏列表。",
                        "default": None
                    },
                    "activateIndex": {
                        "type": "number",
                        "required": False,
                        "description": "激活态的子项。",
                        "default": -1
                    },
                    "controller": {
                        "type": "TabsController",
                        "required": True,
                        "description": "筛选器的样式类型。",
                        "default": None
                    }
                }
            }
        ],
        "attributes": {
            "toolBarList": {
                "description": "工具栏列表。",
                "params": {
                    "content": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "工具栏子项的文本。",
                        "default": None
                    },
                    "action": {
                        "type": "() => void",
                        "required": False,
                        "description": "工具栏子项点击事件。",
                        "default": None
                    },
                    "icon": {
                        "type": "Resource",
                        "required": False,
                        "description": "工具栏子项的图标。",
                        "default": None
                    },
                    "state": {
                        "type": "ItemState",
                        "required": False,
                        "description": "工具栏子项的状态，默认为ENABLE。",
                        "default": None
                    }
                }
            }
        },
        "events": {
            "onToolBarItemClick": {
                "description": "工具栏子项点击事件。",
                "params": {},
                "returns": None
            }
        },
        "rules": None,
        "examples": [
            "/*\\n实现思路：\\n本示例展示了如何在鸿蒙ArkUI中使用ToolBar组件，通过动态添加工具栏项并设置不同的状态来实现一个功能丰富的工具栏。\\n总体功能与效果描述：\\n该示例创建了一个包含多个工具栏项的工具栏，每个工具栏项具有不同的状态（启用、禁用、激活），并设置了相应的图标和文本内容。\\n*/\\n\\n// Index.ets\\nimport { ToolBar, ToolBarOptions } from '@kit.ArkUI'\\n\\n// 定义工具栏项的状态枚举\\nenum ItemState {\\n  ENABLE = 1, // 启用状态\\n  DISABLE = 2, // 禁用状态\\n  ACTIVATE = 3 // 激活状态\\n}\\n\\n@Entry\\n@Component\\nstruct Index {\\n  @State toolbarList: ToolBarOptions = new ToolBarOptions() // 声明一个状态变量，用于存储工具栏项列表\\n\\n  // 组件即将出现时执行的初始化操作\\n  aboutToAppear() {\\n    // 添加第一个工具栏项\\n    this.toolbarList.push({\\n      content: '剪贴我是超超超超超超超超超长样式', // 工具栏项的文本内容\\n      icon: $r('sys.media.ohos_ic_public_share'), // 工具栏项的图标资源\\n      action: () => {\\n        // 工具栏项的点击事件处理逻辑\\n      },\\n    })\\n\\n    // 添加第二个工具栏项，并设置为禁用状态\\n    this.toolbarList.push({\\n      content: '拷贝', // 工具栏项的文本内容\\n      icon: $r('sys.media.ohos_ic_public_copy'), // 工具栏项的图标资源\\n      action: () => {\\n        // 工具栏项的点击事件处理逻辑\\n      },\\n      state: ItemState.DISABLE // 设置工具栏项的状态为禁用\\n    })\\n\\n    // 添加第三个工具栏项，并设置为激活状态\\n    this.toolbarList.push({\\n      content: '粘贴', // 工具栏项的文本内容\\n      icon: $r('sys.media.ohos_ic_public_paste'), // 工具栏项的图标资源\\n      action: () => {\\n        // 工具栏项的点击事件处理逻辑\\n      },\\n      state: ItemState.ACTIVATE // 设置工具栏项的状态为激活\\n    })\\n\\n    // 添加第四个工具栏项\\n    this.toolbarList.push({\\n      content: '全选', // 工具栏项的文本内容\\n      icon: $r('sys.media.ohos_ic_public_select_all'), // 工具栏项的图标资源\\n      action: () => {\\n        // 工具栏项的点击事件处理逻辑\\n      },\\n    })\\n\\n    // 添加第五个工具栏项\\n    this.toolbarList.push({\\n      content: '分享', // 工具栏项的文本内容\\n      icon: $r('sys.media.ohos_ic_public_share'), // 工具栏项的图标资源\\n      action: () => {\\n        // 工具栏项的点击事件处理逻辑\\n      },\\n    })\\n\\n    // 添加第六个工具栏项\\n    this.toolbarList.push({\\n      content: '分享', // 工具栏项的文本内容\\n      icon: $r('sys.media.ohos_ic_public_share'), // 工具栏项的图标资源\\n      action: () => {\\n        // 工具栏项的点击事件处理逻辑\\n      },\\n    })\\n  }\\n\\n  build() {\\n    Row() {\\n      Stack() {\\n        Column() {\\n          // 创建ToolBar组件，并设置激活索引和工具栏项列表\\n          ToolBar({\\n            activateIndex: 2, // 设置激活的工具栏项索引\\n            toolBarList: this.toolbarList, // 传递工具栏项列表\\n          })\\n        }\\n      }.align(Alignment.Bottom) // 将Stack组件对齐到屏幕底部\\n      .width('100%').height('100%') // 设置Stack组件的宽度和高度为全屏\\n    }\\n  }\\n}"
        ],
        "is_common_attrs": True
    },
    "ComposeTitleBar": {
        "description": "一种普通标题栏，支持设置标题、头像（可选）和副标题（可选），可用于一级页面、二级及其以上界面配置返回键。",
        "details": "该组件从API Version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。",
        "interfaces": [
            {
                "description": "ComposeTitleBar({item?: ComposeTitleBarMenuItem, title: ResourceStr, subtitle?: ResourceStr, menuItems?: Array<ComposeTitleBarMenuItem>})",
                "params": {
                    "item": {
                        "type": "ComposeTitleBarMenuItem",
                        "required": False,
                        "description": "用于左侧头像的单个菜单项目。"
                    },
                    "title": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "标题。"
                    },
                    "subtitle": {
                        "type": "ResourceStr",
                        "required": False,
                        "description": "副标题。"
                    },
                    "menuItems": {
                        "type": ["Array", "ComposeTitleBarMenuItem"],
                        "required": False,
                        "description": "右侧菜单项目列表。"
                    }
                }
            }
        ],
        "attributes": {
            "ComposeTitleBarMenuItem": {
                "description": "菜单项目的属性。",
                "params": {
                    "value": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "图标资源。"
                    },
                    "isEnabled": {
                        "type": "boolean",
                        "required": False,
                        "description": "是否启用，默认禁用。",
                        "default": False
                    },
                    "action": {
                        "type": "() => void",
                        "required": False,
                        "description": "触发时的动作闭包，item属性不支持触发action事件。"
                    }
                }
            }
        },
        "events": {},
        "rules": None,
        "examples": None,
        "is_common_attrs": False
    }
}
