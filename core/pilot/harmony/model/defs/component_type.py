COMPONENT_TYPE = {
    "ToolBarOption": {
        "description": "ToolBar工具栏配置",
        "type": "object",
        "properties": {
            "content": {
                "type": "ResourceStr",
                "description": "工具栏子项的文本",
                "required": True,
            },
            "action": {
                "type": "() => void",
                "description": "工具栏子项的点击事件",
                "required": False,
            },
            "icon": {
                "type": "Resource",
                "description": "工具栏子项的图标",
                "required": False,
            },
            "state": {
                "type": "ItemState",
                "description": "工具栏子项的状态",
                "required": False,
                "default": "ItemState.ENABLE"
            }
        }
    },
    "ToolBarOptions": {
        "type": "Array<ToolBarOption>",
        "description": "多个ToolBar工具栏配置",
    },
    "ItemState": {
        "description": "工具栏子项的状态",
        "type": "enum",
        "enum": ["ENABLE", "DISABLE", "ACTIVATE"],
        "enumDescriptions": {
            "ENABLE": "工具栏子项为正常可点击状态",
            "DISABLE": "工具栏子项为不可点击状态",
            "ACTIVATE": "工具栏子项为激活状态，可点击"
        }
    },
    "ToggleType": {
        "description": "Toggle类型枚举",
        "type": "enum",
        "enum": ["Checkbox", "Button", "Switch"],
        "enumDescriptions": {
            "Checkbox": "提供单选框样式。通用属性margin的默认值为：{top: '14px',right: '14px',bottom: '14px',left: '14px'}。默认尺寸为:{width:'20vp', height:'20vp'}。",
            "Button": "提供状态按钮样式，如果子组件有文本设置，则相应的文本内容会显示在按钮内部。默认尺寸为:高为28vp，宽无默认值。",
            "Switch": "提供开关样式。通用属性margin默认值为：{top: '6px',right: '14px',bottom: '6px',left: '14px'}。默认尺寸为:{width:'36vp', height:'20vp'}。"
        }
    }
}