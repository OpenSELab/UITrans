FLEX_LAYOUT_ATTRIBUTE = {
    "flexBasis": {
        "description": "设置组件的基准尺寸。",
        "params": {
            "value": {
                "type": ["number", "string"],
                "required": True,
                "description": "设置组件在父容器主轴方向上的基准尺寸。不支持百分比设置。",
                "default": "auto"
            }
        }
    },
    "flexGrow": {
        "description": "设置组件在父容器的剩余空间所占比例。",
        "params": {
            "value": {
                "type": "number",
                "required": True,
                "description": "设置父容器在主轴方向上的剩余空间分配给此属性所在组件的比例。",
                "default": 0
            }
        }
    },
    "flexShrink": {
        "description": "设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。",
        "params": {
            "value": {
                "type": "number",
                "required": True,
                "description": "设置父容器压缩尺寸分配给此属性所在组件的比例。",
                "default": 0
            }
        }
    },
    "alignSelf": {
        "description": "子组件在父容器交叉轴的对齐格式。",
        "params": {
            "value": {
                "type": "ItemAlign",
                "required": True,
                "description": "子组件在父容器交叉轴的对齐格式，会覆盖Flex、Column、Row、GridRow布局容器中的alignItems设置。",
                "default": "ItemAlign.Auto"
            }
        }
    }
}