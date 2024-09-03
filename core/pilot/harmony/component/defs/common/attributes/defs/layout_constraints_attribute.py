LAYOUT_CONSTRAINTS_ATTRIBUTE = {
    "aspectRatio": {
        "description": "指定当前组件的宽高比。",
        "params": {
            "value": {
                "type": "number",
                "required": True,
                "description": "指定当前组件的宽高比，aspectRatio = width/height。API version 9及以前，默认值为：1.0。API version 10：无默认值。该属性在不设置值或者设置非法值时不生效。例如，Row只设置宽度且没有子组件，aspectRatio不设置值或者设置成负数时，此时Row高度为0。"
            }
        }
    },
    "displayPriority": {
        "description": "设置当前组件在布局容器中显示的优先级。仅在Row/Column/Flex(单行)容器组件中生效。",
        "params": {
            "value": {
                "type": "number",
                "required": True,
                "description": "设置当前组件在布局容器中显示的优先级。默认值：1。小数点后的数字不作优先级区分，即区间为[x, x + 1)内的数字视为相同优先级。例如：1.0与1.9为同一优先级。子组件的displayPriority均为1时，优先级没有区别。当子组件的displayPriority大于1时，若父容器空间不足，隐藏低优先级节点。"
            }
        }
    },
    "pixelRound": {
        "description": "指定当前组件的像素级取整对齐方式。",
        "params": {
            "value": {
                "type": "PixelRoundPolicy",
                "required": True,
                "description": "指定当前组件的像素级取整对齐方式。"
            }
        }
    }
}