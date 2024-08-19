POSITION_COMMON_ATTRIBUTES = {
    "align": {
        "description": "设置容器元素绘制区域内的子元素的对齐方式。",
        "params": {
            "value": {
                "type": "Alignment",
                "required": True,
                "description": "设置容器元素绘制区域内的子元素的对齐方式。只在Stack、Button、Marquee、StepperItem、text、TextArea、TextInput、FolderStack中生效，其中和文本相关的组件Marquee、text、TextArea、TextInput的align结果参考textAlign。不支持textAlign属性的组件则无法设置水平方向的文字对齐。",
                "default": "Alignment.Center"
            }
        }
    },
    "direction": {
        "description": "设置容器元素内主轴方向上的布局。",
        "params": {
            "value": {
                "type": "Direction",
                "required": True,
                "description": "设置容器元素内主轴方向上的布局。属性配置为auto的时候，按照系统语言方向进行布局。该属性在Column组件上不生效。",
                "default": "Direction.Auto"
            }
        }
    },
    "position": {
        "description": "绝对定位，确定子组件相对父组件的位置。",
        "params": {
            "value": {
                "type": ["Position", "Edges", "LocalizedEdges"],
                "required": True,
                "description": "绝对定位，确定子组件相对父组件的位置。当父容器为Row/Column/Flex时，设置position的子组件不占位。Position类型基于父组件左上角确定位置;Edges类型基于父组件四边确定位置，top/left/right/bottom分别为组件各边距离父组件相应边的边距，通过边距来确定组件相对于父组件的位置;LocalizedEdges类型基于父组件四边确定位置，支持镜像模式。适用于置顶显示、悬浮按钮等组件在父容器中位置固定的场景。不支持在宽高为零的布局容器上设置。当父容器为RelativeContainer, 且子组件设置了alignRules属性, 则子组件的position属性不生效。"
            }
        }
    },
    "markAnchor": {
        "description": "设置子元素在位置定位时的锚点。",
        "params": {
            "value": {
                "type": ["Position", "LocalizedPosition"],
                "required": True,
                "description": "设置子元素在位置定位时的锚点，从position或offset的位置上，进一步偏移。设置.position({x: value1, y: value2}).markAnchor({x: value3, y: value4})，效果等于设置.position({x: value1 - value3, y: value2 - value4})，offset同理。单独使用markAnchor，设置.markAnchor({x: value1, y: value2})，效果等于设置.offset({x: -value1, y: -value2})。"
            }
        }
    },
    "offset": {
        "description": "相对偏移，组件相对原本的布局位置进行偏移。",
        "params": {
            "value": {
                "type": ["Position", "Edges", "LocalizedEdges"],
                "required": True,
                "description": "相对偏移，组件相对原本的布局位置进行偏移。offset属性不影响父容器布局，仅在绘制时调整位置。Position类型基于组件自身左上角偏移，Edges类型基于组件自身四边偏移。 offset属性设置 {x: x, y: y} 与设置 {left: x, top: y} 以及 {right: -x, bottom: -y} 效果相同, 类型LocalizedEdges支持镜像模式：LTR模式下start 等同于x，RTL模式下等同于-x"
            }
        }
    },
    "alignRules": {
        "description": "指定设置在相对容器中子组件的对齐规则，仅当父容器为RelativeContainer时生效。",
        "params": {
            "value": {
                "type": "AlignRuleOption",
                "required": True,
                "description": "指定设置在相对容器中子组件的对齐规则，仅当父容器为RelativeContainer时生效。该方法水平方向上以start和end分别替代原方法的left和right，以便在RTL模式下能镜像显示，建议使用该方法指定设置在相对容器中子组件的对齐规则。"
            }
        }
    },
    "chainMode": {
        "description": "指定以该组件为链头所构成的链的参数，仅当父容器为RelativeContainer时生效。",
        "params": {
            "direction": {
                "type": "Axis",
                "required": True,
                "description": "链的方向。"
            },
            "style": {
                "type": "ChainStyle",
                "required": True,
                "description": "链的样式。"
            }
        }
    }
}