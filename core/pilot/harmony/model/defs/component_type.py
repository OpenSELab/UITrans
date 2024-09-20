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
    },
    "ButtonType": {
        "type": "enum",
        "enum": ["Capsule", "Circle", "Normal"],
        "description": "按钮类型枚举类，用于定义不同类型的按钮样式。",
        "enumDescriptions": {
            "Capsule": "胶囊型按钮（圆角默认为高度的一半）。当按钮类型为Capsule时，borderRadius设置不生效，按钮圆角始终为宽、高中较小值的一半。",
            "Circle": "圆形按钮。当按钮类型为Circle时，若同时设置了宽和高，则borderRadius不生效，且按钮半径为宽高中较小值的一半；若只设置宽、高中的一个，则borderRadius不生效，且按钮半径为所设宽或所设高值的一半；若不设置宽高，则borderRadius为按钮半径；若borderRadius的值为负，则borderRadius的值按照0处理。",
            "Normal": "普通按钮（默认不带圆角）。按钮圆角通过通用属性borderRadius设置。"
        }
    },
    "ButtonStyleMode": {
        "type": "enum",
        "enum": ["EMPHASIZED", "NORMAL", "TEXTUAL"],
        "description": "该枚举类定义了不同样式的按钮，包括强调按钮、普通按钮和文本按钮。",
        "enumDescriptions": {
            "EMPHASIZED": "强调按钮（用于强调当前操作）。",
            "NORMAL": "普通按钮（一般界面操作）。",
            "TEXTUAL": "文本按钮（纯文本，无背景颜色）。"
        }
    },
    "ControlSize": {
        "type": "enum",
        "enum": ["SMALL", "NORMAL"],
        "description": "该枚举类定义了按钮的尺寸类型",
        "enumDescriptions": {
            "SMALL": "小尺寸按钮",
            "NORMAL": "正常尺寸按钮"
        }
    },
    "ButtonRole": {
        "type": "enum",
        "enum": ["NORMAL", "ERROR"],
        "description": "从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "NORMAL": "正常按钮。",
            "ERROR": "警示按钮。"
        }
    },
    "ButtonConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。从API version 12开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "label": {
                "type": "string",
                "description": "Button的文本标签。",
                "required": True
            },
            "pressed": {
                "type": "boolean",
                "description": "指示是否按下Button。此属性指示的是原本Button是否被按压，而非build出来的新组件。若新build出来的组件超过原本组件的大小，那么超出部分按压不触发。",
                "required": True
            },
            "triggerClick": {
                "type": "ButtonTriggerClickCallback",
                "description": "使用builder新构建出来组件的点击事件。",
                "required": True
            }
        }
    },
    "ButtonTriggerClickCallback": {
        "type": "object",
        "description": "定义ButtonConfiguration中使用的回调类型。",
        "properties": {
            "xPos": {
                "type": "number",
                "description": "点击位置x的坐标。",
                "required": True
            },
            "yPos": {
                "type": "number",
                "description": "点击位置y的坐标。",
                "required": True
            }
        }
    },
    "CalendarOptions": {
        "type": "object",
        "description": "描述日期选中态底板样式。",
        "properties": {
            "hintRadius": {
                "type": ["number", "Resource"],
                "description": "描述日期选中态底板样式。hintRadius为0，底板样式为直角矩形。hintRadius为0 ~ 16，底板样式为圆角矩形。hintRadius>=16，底板样式为圆形",
                "required": False
            },
            "selected": {
                "type": "Date",
                "description": "设置选中项的日期。选中的日期未设置或日期格式不符合规范则为默认值。",
                "required": False
            }
        }
    },
    "CalendarAlign": {
        "type": "enum",
        "enum": ["START", "CENTER", "END"],
        "description": "设置选择器与入口组件的对齐方式。",
        "enumDescriptions": {
            "START": "设置选择器与入口组件左对齐的对齐方式。",
            "CENTER": "设置选择器与入口组件居中对齐的对齐方式。",
            "END": "设置选择器与入口组件右对齐的对齐方式。"
        }
    },
    "CheckboxOptions": {
        "type": "object",
        "description": "用于指定多选框名称。从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "name": {
                "type": "string",
                "description": "用于指定多选框名称。",
                "required": False
            },
            "group": {
                "type": "string",
                "description": "用于指定多选框所属群组的名称（即所属CheckboxGroup的名称）。未配合使用CheckboxGroup组件时，此值无用。",
                "required": False
            },
            "indicatorBuilder": {
                "type": "CustomBuilder",
                "description": "配置多选框的选中样式为自定义组件。自定义组件与Checkbox组件为中心点对齐显示。indicatorBuilder设置为undefined/null时，默认为indicatorBuilder未设置状态。",
                "required": False
            }
        }
    },
    "CheckBoxShape": {
        "type": "enum",
        "enum": ["CIRCLE", "ROUNDED_SQUARE"],
        "description": "该枚举类定义了两种形状：圆形和圆角方形",
        "enumDescriptions": {
            "CIRCLE": "圆形",
            "ROUNDED_SQUARE": "圆角方形"
        }
    },
    "CheckBoxConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。元服务API： 从API version 12开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "name": {
                "type": "string",
                "description": "当前多选框名称。",
                "required": True
            },
            "selected": {
                "type": "boolean",
                "description": "指示多选框是否被选中。",
                "default": False,
                "required": True
            },
            "triggerChange": {
                "type": "Callback<boolean>",
                "description": "触发多选框选中状态变化。",
                "required": True
            }
        }
    },
    "CheckboxGroupOptions": {
        "type": "object",
        "description": "CheckboxGroupOptions对象说明。卡片能力：从API version 9开始，该接口支持在ArkTS卡片中使用。元服务API：从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full。说明：多个相同群组名称的CheckboxGroup，仅第一个CheckboxGroup生效。",
        "properties": {
            "group": {
                "type": "string",
                "description": "群组名称。",
                "required": False
            }
        }
    },
    "CheckboxGroupResult": {
        "type": "object",
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "name": {
                "type": "Array<string>",
                "description": "群组内所有被选中的多选框名称。",
                "required": True
            },
            "status": {
                "type": "SelectStatus",
                "description": "选中状态。",
                "required": True
            }
        }
    },
    "SelectStatus": {
        "type": "enum",
        "enum": ["All", "Part", "None"],
        "description": "该枚举类用于表示群组多选择框的选择状态。",
        "enumDescriptions": {
            "All": "群组多选择框全部选择。",
            "Part": "群组多选择框部分选择。",
            "None": "群组多选择框全部没有选择。"
        }
    },
    "SceneOptions": {
        "type": "object",
        "description": "Component3D组件配置选项。",
        "properties": {
            "scene": {
                "type": ["Resource", "Scene"],
                "description": "3D模型资源文件或场景对象，默认值为undefined。目前仅支持GLTF格式资源。",
                "default": "undefined",
                "required": False
            },
            "modelType": {
                "type": "ModelType",
                "description": "3D场景显示合成方式。设置为ModelType.TEXTURE时通过GPU合成显示。设置为ModelType.SURFACE时通过专有硬件合成显示。一般开发者可以使用默认值而无需关心此项设置。",
                "default": "ModelType.SURFACE",
                "required": False
            }
        }
    },
    "ModelType": {
        "type": "enum",
        "enum": ["TEXTURE", "SURFACE"],
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "TEXTURE": "使用GPU合成显示3D场景。",
            "SURFACE": "使用专有硬件显示3D场景。"
        }
    },
    "DataPanelOptions": {
        "type": "object",
        "description": "DataPanelOptions对象说明",
        "properties": {
            "values": {
                "type": "number[]",
                "description": "数据值列表，最多包含9个数据，大于9个数据则取前9个数据。若数据值小于0则置为0。",
                "required": True
            },
            "max": {
                "type": "number",
                "description": "max大于0，表示数据的最大值。max小于等于0，max等于value数组各项的和，按比例显示。",
                "default": 100
            },
            "type": {
                "type": "DataPanelType",
                "description": "数据面板的类型（不支持动态修改）。",
                "default": "DataPanelType.Circle"
            }
        }
    },
    "DataPanelType": {
        "type": "enum",
        "enum": ["Line", "Circle"],
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。元服务API： 从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "Line": "线型数据面板。",
            "Circle": "环形数据面板。"
        }
    },
    "DataPanelShadowOptions": {
        "type": "object",
        "description": "DataPanelShadowOptions继承自MultiShadowOptions，具有MultiShadowOptions的全部属性。",
        "properties": {
            "colors": {
                "type": ["Array<ResourceColor", " LinearGradient>"],
                "description": "各数据段投影的颜色。若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色的个数和设置的投影颜色个数一致。若设置的投影颜色的个数多于数据段个数时，则显示的投影颜色的个数和数据段个数一致。",
                "required": False
            }
        }
    },
    "LinearGradient": {
        "type": "object",
        "description": "线性渐变颜色描述。",
        "properties": {
            "colorStops": {
                "type": "ColorStop[]",
                "description": "存储渐变颜色和渐变点。",
                "required": True
            }
        }
    },
    "ColorStop": {
        "type": "object",
        "description": "颜色断点类型，用于描述渐进色颜色断点。",
        "properties": {
            "color": {
                "type": "ResourceColor",
                "description": "颜色值。",
                "required": True
            },
            "offset": {
                "type": "Length",
                "description": "渐变色断点（0~1之间的比例值，若数据值小于0则置为0，若数据值大于1则置为1）。",
                "required": True
            }
        }
    },
    "DataPanelConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "values": {
                "type": "number[]",
                "description": "当前DataPanel的数据值，最大长度为9。",
                "required": True
            },
            "maxValue": {
                "type": "number",
                "description": "DataPanel显示的最大值。",
                "default": 100,
                "required": False
            }
        }
    },
    "DatePickerOptions": {
        "type": "object",
        "description": "DatePickerOptions对象说明",
        "properties": {
            "start": {
                "type": "Date",
                "description": "指定选择器的起始日期。",
                "default": "Date('1970-1-1')",
                "required": False
            },
            "end": {
                "type": "Date",
                "description": "指定选择器的结束日期。",
                "default": "Date('2100-12-31')",
                "required": False
            },
            "selected": {
                "type": "Date",
                "description": "设置选中项的日期。",
                "default": "当前系统日期",
                "required": False
            }
        }
    },
    "PickerTextStyle10": {
        "type": "object",
        "description": "文本样式，picker只支持字号、字体粗细的设置。",
        "properties": {
            "color": {
                "type": "ResourceColor",
                "description": "文本颜色。",
                "required": False
            },
            "font": {
                "type": "Font",
                "description": "文本样式，picker只支持字号、字体粗细的设置。",
                "required": False
            }
        }
    },
    "DatePickerResult": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "year": {
                "type": "number",
                "description": "选中日期的年。",
                "required": True
            },
            "month": {
                "type": "number",
                "description": "选中日期的月(0~11)，0表示1月，11表示12月。",
                "required": True
            },
            "day": {
                "type": "number",
                "description": "选中日期的日。",
                "required": True
            }
        }
    },
    "GaugeShadowOptions": {
        "type": "object",
        "description": "GaugeShadowOptions继承自MultiShadowOptions，具有MultiShadowOptions的全部属性。",
        "properties": {
            "radius": {
                "type": ["number", "Resource"],
                "description": "投影模糊半径。设置小于等于0的值时，按默认值显示。",
                "default": 20,
                "required": False
            },
            "offsetX": {
                "type": ["number", "Resource"],
                "description": "X轴的偏移量。",
                "default": 5,
                "required": False
            },
            "offsetY": {
                "type": ["number", "Resource"],
                "description": "Y轴的偏移量。",
                "default": 5,
                "required": False
            }
        }
    },
    "GaugeIndicatorOptions": {
        "type": "object",
        "description": "GaugeIndicatorOptions11+对象说明。元服务API：从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "icon": {
                "type": "Resource",
                "description": "图标资源路径。不配置则使用默认的三角形样式指针。支持使用svg格式的图标，若使用其他格式，则使用默认的三角形样式指针。",
                "required": False
            },
            "space": {
                "type": "Dimension",
                "description": "指针距离圆环外边的间距。(不支持百分比)。对于默认的三角形样式指针，间距为黑色三角形到圆环外边的间距。若设置值小于0，则使用默认值。若设置值大于圆环半径，则使用默认值。",
                "default": 8,
                "required": False
            }
        }
    },
    "ImageInterpolation": {
        "type": "object",
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "None": {
                "type": "string",
                "description": "最近邻插值。",
                "required": False
            },
            "High": {
                "type": "string",
                "description": "Cubic插值，插值质量最高，可能会影响图片渲染的速度。",
                "required": False
            },
            "Medium": {
                "type": "string",
                "description": "MipMap插值。",
                "required": False
            },
            "Low": {
                "type": "string",
                "description": "双线性插值。",
                "required": False
            }
        }
    },
    "ImageRenderMode": {
        "type": "object",
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "Original": {
                "type": "string",
                "description": "原色渲染模式。",
                "default": "Original",
                "required": False
            },
            "Template": {
                "type": "string",
                "description": "黑白渲染模式。",
                "default": "Template",
                "required": False
            }
        }
    },
    "ResizableOptions": {
        "type": "object",
        "description": "图像拉伸时可调整大小的图像选项。",
        "properties": {
            "slice": {
                "type": "EdgeWidths",
                "description": "边框宽度类型，用于描述组件边框不同方向的宽度。只有当bottom和right同时大于0时，该属性生效。",
                "required": True
            }
        }
    },
    "EdgeWidths": {
        "type": "object",
        "description": "EdgeWidths参数说明",
        "properties": {
            "top": {
                "type": "Length",
                "description": "图片顶部拉伸时保持不变距离。",
                "default": 0,
                "required": False
            },
            "right": {
                "type": "Length",
                "description": "图片右部拉伸时保持不变距离。",
                "default": 0,
                "required": False
            },
            "bottom": {
                "type": "Length",
                "description": "图片底部拉伸时保持不变距离。",
                "default": 0,
                "required": False
            },
            "left": {
                "type": "Length",
                "description": "图片左部拉伸时保持不变距离。",
                "default": 0,
                "required": False
            }
        }
    },
    "DynamicRangeMode": {
        "type": "object",
        "description": "期望展示的图像动态范围。",
        "properties": {
            "High": {
                "type": "string",
                "description": "不受限动态范围，最大限度进行图片提亮。",
                "default": "High",
                "required": False
            },
            "Constraint": {
                "type": "string",
                "description": "受限动态范围，受限进行图片提亮。",
                "default": "Constraint",
                "required": False
            },
            "Standard": {
                "type": "string",
                "description": "标准动态范围，不进行图片提亮。",
                "default": "Standard",
                "required": False
            }
        }
    },
    "ImageErrorCallback": {
        "type": "object",
        "description": "图片加载异常时触发的回调。当组件的参数类型为AnimatedDrawableDescriptor时该事件不触发。元服务API：从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "error": {
                "type": "ImageError",
                "description": "图片加载异常时触发回调的返回对象。",
                "required": True
            }
        }
    },
    "ImageError": {
        "type": "object",
        "description": "图片加载异常时触发回调的返回对象。当组件的参数类型为AnimatedDrawableDescriptor时该事件不触发。元服务API： 从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "componentWidth": {
                "type": "number",
                "description": "组件的宽。单位：像素",
                "required": True
            },
            "componentHeight": {
                "type": "number",
                "description": "组件的高。单位：像素",
                "required": True
            },
            "message": {
                "type": "string",
                "description": "报错信息。",
                "required": True
            }
        }
    },
    "ImageFrameInfo": {
        "type": "object",
        "description": "ImageFrameInfo对象说明",
        "properties": {
            "src": {
                "type": ["string", "Resource", "PixelMap"],
                "description": "图片路径，图片格式为svg，png和jpg，从API Version9开始支持Resource类型的路径，从API version 12开始支持PixelMap类型。",
                "required": True
            },
            "width": {
                "type": ["number", "string"],
                "description": "图片宽度。",
                "default": "0",
                "required": False
            },
            "height": {
                "type": ["number", "string"],
                "description": "图片高度。",
                "default": "0",
                "required": False
            },
            "top": {
                "type": ["number", "string"],
                "description": "图片相对于组件左上角的纵向坐标。",
                "default": "0",
                "required": False
            },
            "left": {
                "type": ["number", "string"],
                "description": "图片相对于组件左上角的横向坐标。",
                "default": "0",
                "required": False
            },
            "duration": {
                "type": "number",
                "description": "每一帧图片的播放时长，单位毫秒。",
                "default": "0",
                "required": False
            }
        }
    },
    "ImageCompleteCallback": {
        "type": "object",
        "description": "图片加载异常时触发的回调。",
        "properties": {
            "result": {
                "type": "ImageLoadResult",
                "description": "图片数据加载成功和解码成功触发回调时返回的对象。",
                "required": True
            }
        }
    },
    "ImageLoadResult": {
        "type": "object",
        "description": "图片数据加载成功和解码成功触发回调时返回的对象。",
        "properties": {
            "width": {
                "type": "number",
                "description": "图片的宽。单位：像素",
                "required": True
            },
            "height": {
                "type": "number",
                "description": "图片的高。单位：像素",
                "required": True
            },
            "componentWidth": {
                "type": "number",
                "description": "组件的宽。单位：像素",
                "required": True
            },
            "componentHeight": {
                "type": "number",
                "description": "组件的高。单位：像素",
                "required": True
            },
            "loadingStatus": {
                "type": "number",
                "description": "图片加载成功的状态值。返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。",
                "required": True
            },
            "contentWidth": {
                "type": "number",
                "description": "图片实际绘制的宽度。单位：像素。仅在loadingStatus返回1时有效。",
                "required": True
            },
            "contentHeight": {
                "type": "number",
                "description": "图片实际绘制的高度。单位：像素。仅在loadingStatus返回1时有效。",
                "required": True
            },
            "contentOffsetX": {
                "type": "number",
                "description": "实际绘制内容相对于组件自身的x轴偏移。单位：像素。仅在loadingStatus返回1时有效。",
                "required": True
            },
            "contentOffsetY": {
                "type": "number",
                "description": "实际绘制内容相对于组件自身的y轴偏移。单位：像素。仅在loadingStatus返回1时有效。",
                "required": True
            }
        }
    },
    "LoadingProgressConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "enableloading": {
                "type": "boolean",
                "description": "LoadingProgress动画是否显示。",
                "default": True,
                "required": False
            }
        }
    },
    "subMenuExpandingMode": {
        "type": "enum",
        "enum": ["SIDE_EXPAND", "EMBEDDED_EXPAND", "STACK_EXPAND"],
        "description": "Menu子菜单展开样式枚举。",
        "enumDescriptions": {
            "SIDE_EXPAND": "默认展开样式, 子菜单位于同一平面侧边展开。",
            "EMBEDDED_EXPAND": "直接展开样式, 子菜单嵌于主菜单内展开。",
            "STACK_EXPAND": "堆叠样式, 子菜单浮于主菜单上方展开。"
        }
    },
    "MenuItemOptions": {
        "type": "object",
        "description": "MenuItemOptions对象说明",
        "properties": {
            "startIcon": {
                "type": "ResourceStr",
                "description": "item中显示在左侧的图标信息路径。",
                "required": False
            },
            "content": {
                "type": "ResourceStr",
                "description": "item的内容信息。",
                "required": False
            },
            "endIcon": {
                "type": "ResourceStr",
                "description": "item中显示在右侧的图标信息路径。",
                "required": False
            },
            "labelInfo": {
                "type": "ResourceStr",
                "description": "定义结束标签信息，如快捷方式Ctrl+C等。",
                "required": False
            },
            "builder": {
                "type": "CustomBuilder",
                "description": "用于构建二级菜单。",
                "required": False
            },
            "symbolStartIcon": {
                "type": "SymbolGlyphModifier",
                "description": "item中显示在左侧的HMSymbol图标信息路径。配置该项时，原先startIcon图标不显示。",
                "required": False
            },
            "symbolEndIcon": {
                "type": "SymbolGlyphModifier",
                "description": "item中显示在右侧的HMSymbol图标信息路径。配置该项时，原先endIcon图标不显示。",
                "required": False
            }
        }
    },
    "MenuItemGroupOptions": {
        "type": "object",
        "description": "MenuItemGroupOptions对象说明",
        "properties": {
            "header": {
                "type": ["ResourceStr", "CustomBuilder"],
                "description": "设置对应group的标题显示信息。",
                "required": False
            },
            "footer": {
                "type": ["ResourceStr", "CustomBuilder"],
                "description": "设置对应group的尾部显示信息。",
                "required": False
            }
        }
    },
    "PopInfo": {
        "type": "object",
        "description": "下一个页面返回的回调信息载体。",
        "properties": {
            "info": {
                "type": "NavPathInfo",
                "description": "页面触发返回时的当前页面信息，系统自动获取填入，无需开发者传入。",
                "required": True
            },
            "result": {
                "type": "Object",
                "description": "页面触发返回时的结果，开发者自定义对象。",
                "required": True
            }
        }
    },
    "NavContentInfo": {
        "type": "object",
        "description": "跳转Destination信息。",
        "properties": {
            "name": {
                "type": "string",
                "description": "NavDestination名称，如果为根视图(NavBar)，则返回值为undefined。",
                "default": "undefined",
                "required": False
            },
            "index": {
                "type": "number",
                "description": "NavDestination在NavPathStack中的序号， 如果为根视图(NavBar)，则返回值为 -1。",
                "default": -1,
                "required": True
            },
            "mode": {
                "type": "NavDestinationMode",
                "description": "NavDestination的模式，如果是根视图(NavBar)，则返回值为undefined。",
                "default": "undefined",
                "required": False
            },
            "param": {
                "type": "Object",
                "description": "NavDestination页面加载的参数。",
                "required": False
            },
            "navDestinationId": {
                "type": "string",
                "description": "NavDestination的唯一标识符。",
                "required": False
            }
        }
    },
    "NavigationAnimatedTransition": {
        "type": "object",
        "description": "自定义转场动画协议，开发者需实现该协议来定义Navigation路由跳转的跳转动画。从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "timeout": {
                "type": "number",
                "description": "动画超时结束时间。单位：ms。",
                "default": 1000,
                "required": False
            },
            "transition": {
                "type": "function",
                "description": "自定义转场动画执行回调。transitionProxy: 自定义转场动画代理对象。",
                "required": True
            },
            "onTransitionEnd": {
                "type": "function",
                "description": "转场完成回调。success: 转场是否成功。",
                "required": False
            },
            "isInteractive": {
                "type": "boolean",
                "description": "本次转场动画是否为可交互转场。",
                "default": False,
                "required": False
            }
        }
    },
    "NavigationTransitionProxy": {
        "type": "object",
        "description": "自定义转场动画代理对象。",
        "properties": {
            "from": {
                "type": "NavContentInfo",
                "description": "退场页面信息。",
                "required": True
            },
            "to": {
                "type": "NavContentInfo",
                "description": "进场页面信息。",
                "required": True
            },
            "isInteractive": {
                "type": "boolean",
                "description": "是否为可交互转场动画。",
                "required": False
            }
        }
    },
    "NavigationInterception": {
        "type": "object",
        "description": "Navigation跳转拦截对象。",
        "properties": {
            "willShow": {
                "type": "InterceptionShowCallback",
                "description": "页面跳转前拦截，允许操作栈，在当前跳转中生效。",
                "required": False
            },
            "didShow": {
                "type": "InterceptionShowCallback",
                "description": "页面跳转后回调。在该回调中操作栈在下一次跳转中刷新。",
                "required": False
            },
            "modeChange": {
                "type": "InterceptionModeCallback",
                "description": "Navigation单双栏显示状态发生变更时触发该回调。",
                "required": False
            }
        }
    },
    "NavigationMenuItem": {
        "type": "object",
        "description": "显示菜单栏单个选项的文本。从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "value": {
                "type": "string",
                "description": "显示菜单栏单个选项的文本。API Version 9: 显示菜单栏单个选项的文本。API Version 10: 不显示菜单栏单个选项的文本。",
                "required": True
            },
            "icon": {
                "type": "string",
                "description": "菜单栏单个选项的图标资源路径。从API version 11开始，该接口支持在元服务中使用。",
                "required": False
            },
            "isEnabled": {
                "type": "boolean",
                "description": "使能状态，默认使能（False未使能，True使能）。从API version 12开始，该接口支持在元服务中使用。",
                "default": True,
                "required": False
            },
            "action": {
                "type": "() => void",
                "description": "当前选项被选中的事件回调。从API version 11开始，该接口支持在元服务中使用。",
                "required": False
            },
            "symbolIcon": {
                "type": "SymbolGlyphModifier",
                "description": "菜单栏单个选项的symbol资源（优先级高于icon）。",
                "required": False
            }
        }
    },
    "ToolbarItem": {
        "type": "object",
        "description": "工具栏单个选项的显示文本、图标资源路径、事件回调和状态。",
        "properties": {
            "value": {
                "type": "ResourceStr",
                "description": "工具栏单个选项的显示文本。",
                "required": True
            },
            "icon": {
                "type": "ResourceStr",
                "description": "工具栏单个选项的图标资源路径。",
                "required": False
            },
            "action": {
                "type": "() => void",
                "description": "当前选项被选中的事件回调。",
                "required": False
            },
            "status": {
                "type": "ToolbarItemStatus",
                "description": "工具栏单个选项的状态。",
                "default": "ToolbarItemStatus.NORMAL",
                "required": False
            },
            "activeIcon": {
                "type": "ResourceStr",
                "description": "工具栏单个选项处于ACTIVE态时的图标资源路径。",
                "required": False
            },
            "symbolIcon": {
                "type": "SymbolGlyphModifier",
                "description": "工具栏单个选项的symbol资源（优先级高于icon）。",
                "required": False
            },
            "activeSymbolIcon": {
                "type": "SymbolGlyphModifier",
                "description": "工具栏单个选项处于ACTIVE态时的symbol资源（优先级高于activeIcon）。",
                "required": False
            }
        }
    },
    "ToolbarItemStatus": {
        "type": "enum",
        "enum": ["NORMAL", "DISABLED", "ACTIVE"],
        "description": "设置工具栏单个选项的状态",
        "enumDescriptions": {
            "NORMAL": "设置工具栏单个选项为NORMAL态，该选项显示默认样式，可以触发Hover，Press，Focus事件并显示对应的多态样式。",
            "DISABLED": "设置工具栏单个选项为DISABLED态， 该选项显示DISABLED态样式，并且不可交互。",
            "ACTIVE": "设置工具栏单个选项为ACTIVE态， 该选项通过点击事件可以将icon图标更新为activeIcon对应的图片资源。"
        }
    },
    "NavigationTitleMode": {
        "type": "enum",
        "enum": ["Free", "Mini", "Full"],
        "description": "元服务API： 从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "Free": "当内容为满一屏的可滚动组件时，标题随着内容向上滚动而缩小（子标题的大小不变、淡出）。向下滚动内容到顶时则恢复原样。标题随着内容滚动大小联动的动效在title设置为ResourceStr和NavigationCommonTitle时生效，设置成其余自定义节点类型时字体样式无法变化，下拉时只影响标题栏偏移。可滚动组件不满一屏时，如果想使用联动效果，就要使用滚动组件提供的edgeEffect接口将options参数设置为True。未滚动状态，标题栏高度与Full模式一致；滚动时，标题栏的最小高度与Mini模式一致。",
            "Mini": "固定为小标题模式。默认值：API version 12之前，只有主标题时，标题栏高度为56vp；同时有主标题和副标题时，标题栏高度为82vp。从API version 12开始，该模式下标题栏高度为56vp。",
            "Full": "固定为大标题模式。默认值：只有主标题时，标题栏高度为112vp；同时有主标题和副标题时，标题栏高度为138vp。"
        }
    },
    "NavigationCommonTitle": {
        "type": "object",
        "description": "元服务API： 从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "main": {
                "type": "string",
                "description": "设置主标题。",
                "required": True
            },
            "sub": {
                "type": "string",
                "description": "设置副标题。",
                "required": True
            }
        }
    },
    "NavigationCustomTitle": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "builder": {
                "type": "CustomBuilder",
                "description": "设置标题栏内容。",
                "required": True
            },
            "height": {
                "type": ["TitleHeight", "Length"],
                "description": "设置标题栏高度。",
                "required": True
            }
        }
    },
    "NavBarPosition": {
        "type": "enum",
        "enum": ["Start", "End"],
        "description": "元服务API： 从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "Start": "双栏显示时，主列在主轴方向首部。",
            "End": "双栏显示时，主列在主轴方向尾部。"
        }
    },
    "NavigationMode": {
        "type": "enum",
        "enum": ["Stack", "Split", "Auto"],
        "description": "导航模式枚举类，定义了不同的导航栏与内容区显示方式。",
        "enumDescriptions": {
            "Stack": "导航栏与内容区独立显示，相当于两个页面。",
            "Split": "导航栏与内容区分两栏显示。",
            "Auto": "API version 9之前：窗口宽度>=520vp时，采用Split模式显示；窗口宽度<520vp时，采用Stack模式显示。API version 10及以上：窗口宽度>=600vp时，采用Split模式显示；窗口宽度<600vp时，采用Stack模式显示，600vp等于minNavBarWidth(240vp) + minContentWidth (360vp)。"
        }
    },
    "TitleHeight": {
        "type": "enum",
        "enum": ["MainOnly", "MainWithSub"],
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "MainOnly": "只有主标题时标题栏的推荐高度（56vp）。",
            "MainWithSub": "同时有主标题和副标题时标题栏的推荐高度（82vp）。"
        }
    },
    "NavigationOperation": {
        "type": "enum",
        "enum": ["PUSH", "POP", "REPLACE"],
        "description": "该枚举类用于描述页面转场的操作类型",
        "enumDescriptions": {
            "PUSH": "本次转场为页面进场。",
            "POP": "本次转场为页面退场。",
            "REPLACE": "本次转场为页面替换。"
        }
    },
    "BarStyle": {
        "type": "enum",
        "enum": ["STANDARD", "STACK"],
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "STANDARD": "标题栏与内容区采用上下布局。",
            "STACK": "标题栏与内容区采用层叠布局，标题栏布局在内容区上层。"
        }
    },
    "NavigationTitleOptions": {
        "type": "object",
        "description": "标题栏背景颜色，不设置时为系统默认颜色。元服务API： 从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "标题栏背景颜色，不设置时为系统默认颜色。",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "标题栏背景模糊样式，不设置时关闭背景模糊效果。",
                "required": False
            },
            "barStyle": {
                "type": "BarStyle",
                "description": "标题栏布局方式设置。",
                "default": "BarStyle.STANDARD",
                "required": False
            },
            "paddingStart": {
                "type": "LengthMetrics",
                "description": "标题栏起始端内间距。仅支持以下任一场景: 1. 显示返回图标，即hideBackButton为False； 2. 使用非自定义标题，即标题value类型为ResourceStr或NavigationCommonTitle。",
                "default": "LengthMetrics.resource($r('sys.float.margin_left'))",
                "required": False
            },
            "paddingEnd": {
                "type": "LengthMetrics",
                "description": "标题栏结束端内间距。仅支持以下任一场景: 1. 使用非自定义菜单，即菜单value为Array<NavigationMenuItem>； 2. 没有右上角菜单，且使用非自定义标题，即标题value类型为ResourceStr或NavigationCommonTitle。",
                "default": "LengthMetrics.resource($r('sys.float.margin_right'))",
                "required": False
            }
        }
    },
    "NavigationToolbarOptions": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "工具栏背景颜色",
                "default": "系统默认颜色",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "工具栏背景模糊样式",
                "default": "关闭背景模糊效果",
                "required": False
            }
        }
    },
    "LaunchMode": {
        "type": "enum",
        "enum": ["STANDARD", "MOVE_TO_TOP_SINGLETON", "POP_TO_SINGLETON", "NEW_INSTANCE"],
        "description": "元服务API： 从API version 12开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "STANDARD": "系统默认的栈操作模式。push操作会将指定的NavDestination入栈；replace操作会将当前栈顶NavDestination替换。",
            "MOVE_TO_TOP_SINGLETON": "从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶（replace操作会将最后的栈顶替换成指定的NavDestination），否则行为和STANDARD一致。",
            "POP_TO_SINGLETON": "从栈底向栈顶查找，如果指定的名称已经存在，则将其上方的NavDestination页面全部移除（replace操作会将最后的栈顶替换成指定的NavDestination），否则行为和STANDARD一致。",
            "NEW_INSTANCE": "创建新的NavDestination实例。与STANDARD模式相比，该方法不会复用栈中同名实例。"
        }
    },
    "NavigationOptions": {
        "type": "object",
        "description": "元服务API： 从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "launchMode": {
                "type": "LaunchMode",
                "description": "页面栈的操作模式。",
                "default": "LaunchMode.STANDARD",
                "required": False
            },
            "animated": {
                "type": "boolean",
                "description": "是否支持转场动画。",
                "default": True,
                "required": False
            }
        }
    },
    "RouteInfo": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "name": {
                "type": "string",
                "description": "点击NavRouter跳转到的NavDestination页面的名称。",
                "required": True
            },
            "param": {
                "type": "unknown",
                "description": "点击NavRouter跳转到NavDestination页面时，传递的参数。",
                "required": False
            }
        }
    },
    "NavRouteMode": {
        "type": "enum",
        "enum": ["PUSH_WITH_RECREATE", "PUSH", "REPLACE"],
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "PUSH_WITH_RECREATE": "跳转到新的NavDestination页面时，替换当前显示的NavDestination页面，页面销毁，但该页面信息仍保留在路由栈中。",
            "PUSH": "跳转到新的NavDestination页面时，覆盖当前显示的NavDestination页面，该页面不销毁，且页面信息保留在路由栈中。",
            "REPLACE": "跳转到新的NavDestination页面时，替换当前显示的NavDestination页面，页面销毁，且该页面信息从路由栈中清除。"
        }
    },
    "NavDestinationMode": {
        "type": "enum",
        "enum": ["STANDARD", "DIALOG"],
        "description": "元服务API： 从API version 12开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "STANDARD": "标准模式的NavDestination。",
            "DIALOG": "默认透明，进出页面栈不影响下层NavDestination的生命周期，不支持系统转场动画。"
        }
    },
    "NavDestinationCommonTitle": {
        "type": "object",
        "description": "设置主标题和副标题。",
        "properties": {
            "main": {
                "type": "string",
                "description": "设置主标题。",
                "required": True
            },
            "sub": {
                "type": "string",
                "description": "设置副标题。",
                "required": True
            }
        }
    },
    "NavDestinationCustomTitle": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "builder": {
                "type": "CustomBuilder",
                "description": "设置标题栏内容。",
                "required": True
            },
            "height": {
                "type": ["TitleHeight", "Length"],
                "description": "设置标题栏高度。",
                "required": True
            }
        }
    },
    "NavDestinationContext": {
        "type": "object",
        "description": "该类的描述",
        "properties": {
            "pathInfo": {
                "type": "NavPathInfo",
                "description": "跳转NavDestination时指定的参数。",
                "required": True
            },
            "pathStack": {
                "type": "NavPathStack",
                "description": "当前NavDestination所处的页面栈。",
                "required": True
            },
            "navDestinationId": {
                "type": "string",
                "description": "当前NavDestination的唯一ID，由系统自动生成，和组件通用属性id无关。",
                "required": False
            }
        }
    },
    "RouteMapConfig": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "name": {
                "type": "string",
                "description": "页面名称。",
                "required": True
            },
            "pageSourceFile": {
                "type": "string",
                "description": "页面在当前包中的路径。",
                "required": True
            },
            "data": {
                "type": "object",
                "description": "页面自定义字段信息。",
                "required": True
            }
        }
    },
    "CircleStyleOptions": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "color": {
                "type": "ResourceColor",
                "description": "背景圆环颜色。",
                "default": "与pathColor值相同",
                "required": False
            },
            "radius": {
                "type": "LengthMetrics",
                "description": "背景圆环的半径。",
                "default": "circleRadius的11/6",
                "required": False
            },
            "enableWaveEffect": {
                "type": "boolean",
                "description": "波浪效果开关。",
                "default": True,
                "required": False
            }
        }
    },
    "PatternLockChallengeResult": {
        "type": "enum",
        "enum": ["CORRECT", "WRONG"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "CORRECT": "图案密码正确。",
            "WRONG": "图案密码错误。"
        }
    },
    "ProgressOptions": {
        "type": "object",
        "description": "ProgressOptions<Type>对象说明。元服务API：从API version 11开始，该接口支持在元服务中使用。卡片能力：从API version 9开始，该接口支持在ArkTS卡片中使用。",
        "properties": {
            "value": {
                "type": "number",
                "description": "指定当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。",
                "default": 0,
                "required": True
            },
            "total": {
                "type": "number",
                "description": "指定进度总长。设置小于等于0的数值时置为100。",
                "default": 100,
                "required": False
            },
            "type": {
                "type": "ProgressType",
                "description": "指定进度条类型。",
                "default": "ProgressType.Linear",
                "required": False
            },
            "style": {
                "type": "ProgressStyle",
                "description": "指定进度条样式。该参数从API version8开始废弃，建议使用type替代。",
                "default": "ProgressStyle.Linear",
                "required": False
            }
        }
    },
    "ProgressType8": {
        "type": "enum",
        "enum": ["Linear", "Ring", "Eclipse", "ScaleRing", "Capsule"],
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "Linear": "线性样式。从API version 9开始，高度大于宽度的时候自适应垂直显示。",
            "Ring": "环形无刻度样式，环形圆环逐渐显示至完全填充效果。",
            "Eclipse": "圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。",
            "ScaleRing": "环形有刻度样式，显示类似时钟刻度形式的进度展示效果。从API version 9开始，刻度外圈出现重叠的时候自动转换为环形无刻度进度条。",
            "Capsule": "胶囊样式，头尾两端圆弧处的进度展示效果与Eclipse相同；中段处的进度展示效果与Linear相同。高度大于宽度的时候自适应垂直显示。"
        }
    },
    "ProgressStyle": {
        "type": "enum",
        "enum": ["Linear", "Ring", "Eclipse", "ScaleRing", "Capsule"],
        "description": "该枚举类定义了不同样式的进度展示效果",
        "enumDescriptions": {
            "Linear": "线性样式",
            "Ring": "环形无刻度样式，环形圆环逐渐显示至完全填充效果",
            "Eclipse": "圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月",
            "ScaleRing": "环形有刻度样式，显示类似时钟刻度形式的进度展示效果",
            "Capsule": "胶囊样式，头尾两端圆弧处的进度展示效果与Eclipse相同；中段处的进度展示效果与Linear相同。高度大于宽度的时候自适应垂直显示"
        }
    },
    "ProgressConfiguration": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "value": {
                "type": "number",
                "description": "当前进度值。",
                "required": True
            },
            "total": {
                "type": "number",
                "description": "进度总长。",
                "required": True
            }
        }
    },
    "ProgressStyleOptions": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "strokeWidth": {
                "type": "Length",
                "description": "设置进度条宽度（不支持百分比设置）。",
                "default": "4.0vp",
                "required": False
            },
            "scaleCount": {
                "type": "number",
                "description": "设置环形进度条总刻度数。",
                "default": 120,
                "required": False
            },
            "scaleWidth": {
                "type": "Length",
                "description": "设置环形进度条刻度粗细（不支持百分比设置），刻度粗细大于进度条宽度时，为系统默认粗细。",
                "default": "2.0vp",
                "required": False
            },
            "enableSmoothEffect": {
                "type": "boolean",
                "description": "进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。",
                "default": True,
                "required": False
            }
        }
    },
    "CapsuleStyleOptions": {
        "type": "object",
        "description": "该类的描述",
        "properties": {
            "borderColor": {
                "type": "ResourceColor",
                "description": "内描边颜色。",
                "default": "#33007dff",
                "required": False
            },
            "borderWidth": {
                "type": "Length",
                "description": "内描边宽度（不支持百分比设置）。",
                "default": "1vp",
                "required": False
            },
            "content": {
                "type": "string",
                "description": "文本内容，应用可自定义。",
                "required": False
            },
            "font": {
                "type": "Font",
                "description": "文本样式。",
                "default": {
                    "文本大小": "12fp",
                    "其他文本参数": "跟随text组件的主题值"
                },
                "required": False
            },
            "fontColor": {
                "type": "ResourceColor",
                "description": "文本颜色。",
                "default": "#ff182431",
                "required": False
            },
            "enableScanEffect": {
                "type": "boolean",
                "description": "扫光效果的开关。",
                "default": False,
                "required": False
            },
            "showDefaultPercentage": {
                "type": "boolean",
                "description": "显示百分比文本的开关，开启后会在进度条上显示当前进度的百分比。设置了content属性时该属性不生效。",
                "default": False,
                "required": False
            },
            "enableSmoothEffect": {
                "type": "boolean",
                "description": "进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。",
                "default": True,
                "required": False
            }
        }
    },
    "RingStyleOptions": {
        "type": "object",
        "description": "该类的描述",
        "properties": {
            "strokeWidth": {
                "type": "Length",
                "description": "设置进度条宽度（不支持百分比设置），宽度大于等于半径时，默认修改宽度至半径值的二分之一。",
                "default": "4.0vp",
                "required": False
            },
            "shadow": {
                "type": "boolean",
                "description": "进度条阴影开关。",
                "default": False,
                "required": False
            },
            "status": {
                "type": "ProgressStatus",
                "description": "进度条状态，当设置为LOADING时会开启检查更新动效，此时设置进度值不生效。当从LOADING设置为PROGRESSING，检查更新动效会执行到终点再停止。",
                "default": "ProgressStatus.PROGRESSING",
                "required": False
            },
            "enableScanEffect": {
                "type": "boolean",
                "description": "进度条扫光效果的开关。",
                "default": False,
                "required": False
            },
            "enableSmoothEffect": {
                "type": "boolean",
                "description": "进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。",
                "default": True,
                "required": False
            }
        }
    },
    "LinearStyleOptions": {
        "type": "object",
        "description": "设置进度条宽度（不支持百分比设置），线性进度条圆角半径，进度条扫光效果的开关，进度平滑动效的开关。",
        "properties": {
            "strokeWidth": {
                "type": "Length",
                "description": "设置进度条宽度（不支持百分比设置）。",
                "default": "4.0vp",
                "required": False
            },
            "strokeRadius": {
                "type": ["PX", "VP", "LPX", "Resource"],
                "description": "设置线性进度条圆角半径。取值范围[0, strokeWidth / 2]。",
                "default": "strokeWidth / 2",
                "required": False
            },
            "enableScanEffect": {
                "type": "boolean",
                "description": "进度条扫光效果的开关。",
                "default": False,
                "required": False
            },
            "enableSmoothEffect": {
                "type": "boolean",
                "description": "进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。",
                "default": True,
                "required": False
            }
        }
    },
    "ScaleRingStyleOptions": {
        "type": "object",
        "description": "设置环形进度条的样式选项。",
        "properties": {
            "strokeWidth": {
                "type": "Length",
                "description": "设置进度条宽度（不支持百分比设置）。",
                "default": "4.0vp",
                "required": False
            },
            "scaleCount": {
                "type": "number",
                "description": "设置环形进度条总刻度数。",
                "default": 120,
                "required": False
            },
            "scaleWidth": {
                "type": "Length",
                "description": "设置环形进度条刻度粗细（不支持百分比设置），刻度粗细大于进度条宽度时，为系统默认粗细。",
                "default": "2.0vp",
                "required": False
            },
            "enableSmoothEffect": {
                "type": "boolean",
                "description": "进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。",
                "default": True,
                "required": False
            }
        }
    },
    "EclipseStyleOptions": {
        "type": "object",
        "description": "该类的描述",
        "properties": {
            "enableSmoothEffect": {
                "type": "boolean",
                "description": "进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。",
                "default": True,
                "required": False
            }
        }
    },
    "ProgressStatus": {
        "type": "enum",
        "enum": ["LOADING", "PROGRESSING"],
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "LOADING": "加载中。",
            "PROGRESSING": "进度更新中。"
        }
    },
    "RadioOptions": {
        "type": "object",
        "description": "RadioOptions对象说明",
        "properties": {
            "value": {
                "type": "string",
                "description": "当前单选框的值。",
                "required": True
            },
            "group": {
                "type": "string",
                "description": "当前单选框的所属群组名称，相同group的Radio只能有一个被选中。",
                "required": True
            },
            "indicatorType": {
                "type": "RadioIndicatorType",
                "description": "配置单选框的选中样式。",
                "default": "RadioIndicatorType.TICK",
                "required": False
            },
            "indicatorBuilder": {
                "type": "CustomBuilder",
                "description": "配置单选框的选中样式为自定义组件。自定义组件与Radio组件为中心点对齐显示。indicatorBuilder设置为undefined时，按照RadioIndicatorType.TICK进行显示。",
                "required": False
            }
        }
    },
    "RadioIndicatorType": {
        "type": "enum",
        "enum": ["TICK", "DOT", "CUSTOM"],
        "description": "从API version 12开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "TICK": "选中样式为系统默认TICK图标。",
            "DOT": "选中样式为系统默认DOT图标。",
            "CUSTOM": "选中样式为indicatorBuilder中的内容。"
        }
    },
    "contentModifier": {
        "type": "object",
        "description": "定制Radio内容区的方法。",
        "properties": {
            "modifier": {
                "type": "ContentModifier<RadioConfiguration>",
                "description": "内容修改器，开发者需要自定义class实现ContentModifier接口。",
                "required": True
            }
        }
    },
    "RadioStyle": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "checkedBackgroundColor": {
                "type": "ResourceColor",
                "description": "开启状态底板颜色。",
                "default": "#007DFF",
                "required": False
            },
            "uncheckedBorderColor": {
                "type": "ResourceColor",
                "description": "关闭状态描边颜色。",
                "default": "#182431",
                "required": False
            },
            "indicatorColor": {
                "type": "ResourceColor",
                "description": "开启状态内部圆饼颜色。从API version 12开始，indicatorType设置为RadioIndicatorType.TICK和RadioIndicatorType.DOT时，支持修改内部颜色。indicatorType设置为RadioIndicatorType.CUSTOM时，不支持修改内部颜色。",
                "default": "#FFFFFF",
                "required": False
            }
        }
    },
    "RadioConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。元服务API：从API version 12开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "value": {
                "type": "string",
                "description": "当前单选框的值。",
                "required": True
            },
            "checked": {
                "type": "boolean",
                "description": "设置单选框的选中状态。",
                "default": False,
                "required": True
            },
            "triggerChange": {
                "type": "Callback<boolean>",
                "description": "触发单选框选中状态变化。",
                "required": True
            }
        }
    },
    "RatingConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。元服务API： 从API version 12开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "rating": {
                "type": "number",
                "description": "评分条当前评分数。",
                "default": 0,
                "required": True
            },
            "indicator": {
                "type": "boolean",
                "description": "评分条是否作为一个指示器。",
                "default": False,
                "required": True
            },
            "stars": {
                "type": "number",
                "description": "评分条的星级总数。",
                "default": 5,
                "required": True
            },
            "stepSize": {
                "type": "number",
                "description": "评分条的评分步长。",
                "default": 0.5,
                "required": True
            },
            "triggerChange": {
                "type": "Callback<number>",
                "description": "触发评分数量变化。",
                "required": True
            }
        }
    },
    "RichEditorInsertValue": {
        "type": "object",
        "description": "插入文本信息。",
        "properties": {
            "insertOffset": {
                "type": "number",
                "description": "插入的文本偏移位置。",
                "required": True
            },
            "insertValue": {
                "type": "string",
                "description": "插入的文本内容。",
                "required": True
            },
            "previewText": {
                "type": "string",
                "description": "插入的预上屏文本内容。",
                "required": False
            }
        }
    },
    "RichEditorDeleteValue": {
        "type": "object",
        "description": "删除操作的信息和被删除内容的信息。",
        "properties": {
            "offset": {
                "type": "number",
                "description": "删除内容的偏移位置。",
                "required": True
            },
            "direction": {
                "type": "RichEditorDeleteDirection",
                "description": "删除操作的方向。",
                "required": True
            },
            "length": {
                "type": "number",
                "description": "删除内容长度。",
                "required": True
            },
            "richEditorDeleteSpans": {
                "type": "Array<RichEditorTextSpanResult | RichEditorImageSpanResult>",
                "description": "删除的文本或者图片Span的具体信息。",
                "required": True
            }
        }
    },
    "RichEditorDeleteDirection": {
        "type": "object",
        "description": "删除操作的方向。",
        "properties": {
            "BACKWARD": {
                "type": "string",
                "description": "向后删除。",
                "required": True
            },
            "FORWARD": {
                "type": "string",
                "description": "向前删除。",
                "required": True
            }
        }
    },
    "RichEditorTextSpanResult": {
        "type": "object",
        "description": "文本Span信息。",
        "properties": {
            "spanPosition": {
                "type": "RichEditorSpanPosition",
                "description": "Span位置。",
                "required": True
            },
            "value": {
                "type": "string",
                "description": "文本Span内容。",
                "required": True
            },
            "textStyle": {
                "type": "RichEditorTextStyleResult",
                "description": "文本Span样式信息。",
                "required": True
            },
            "offsetInSpan": {
                "type": "array",
                "description": "文本Span内容里有效内容的起始和结束位置。",
                "required": True
            },
            "valueResource": {
                "type": "Resource",
                "description": "组件SymbolSpan内容。",
                "required": False
            },
            "symbolSpanStyle": {
                "type": "RichEditorSymbolSpanStyle",
                "description": "组件SymbolSpan样式信息。",
                "required": False
            },
            "paragraphStyle": {
                "type": "RichEditorParagraphStyle",
                "description": "段落样式。",
                "required": False
            },
            "previewText": {
                "type": "string",
                "description": "文本Span预上屏内容。",
                "required": False
            }
        }
    },
    "RichEditorSpanPosition": {
        "type": "object",
        "description": "Span位置信息。",
        "properties": {
            "spanIndex": {
                "type": "number",
                "description": "Span索引值。",
                "required": True
            },
            "spanRange": {
                "type": "array",
                "description": "Span内容在RichEditor内的起始和结束位置。",
                "required": True
            }
        }
    },
    "RichEditorSpanType": {
        "type": "object",
        "description": "Span类型信息。",
        "properties": {
            "TEXT": {
                "type": "number",
                "description": "Span为文字类型。",
                "default": 0,
                "required": False
            },
            "IMAGE": {
                "type": "number",
                "description": "Span为图像类型。",
                "default": 1,
                "required": False
            },
            "MIXED": {
                "type": "number",
                "description": "Span为图文混合类型。",
                "default": 2,
                "required": False
            }
        }
    },
    "RichEditorTextStyleResult": {
        "type": "object",
        "description": "后端返回的文本样式信息。",
        "properties": {
            "fontColor": {
                "type": "ResourceColor",
                "description": "文本颜色。",
                "required": True
            },
            "fontSize": {
                "type": "number",
                "description": "字体大小，默认单位为fp。",
                "required": True
            },
            "fontStyle": {
                "type": "FontStyle",
                "description": "字体样式。",
                "required": True
            },
            "fontWeight": {
                "type": "number",
                "description": "字体粗细。",
                "required": True
            },
            "fontFamily": {
                "type": "string",
                "description": "字体列表。",
                "required": True
            },
            "decoration": {
                "type": "DecorationStyleResult",
                "description": "文本装饰线样式信息。",
                "required": True
            },
            "textShadow": {
                "type": ["ShadowOptions", "Array<ShadowOptions>"],
                "description": "文字阴影效果。",
                "required": False
            },
            "lineHeight": {
                "type": "number",
                "description": "文本行高，默认单位为fp。",
                "required": False
            },
            "letterSpacing": {
                "type": "number",
                "description": "文本字符间距，默认单位为fp。",
                "required": False
            },
            "fontFeature": {
                "type": "string",
                "description": "文字特性效果。",
                "required": False
            }
        }
    },
    "RichEditorSymbolSpanStyleResult": {
        "type": "object",
        "description": "后端返回的SymbolSpan样式信息。",
        "properties": {
            "fontColor": {
                "type": "Array<ResourceColor>",
                "description": "SymbolSpan组件颜色。",
                "default": "不同渲染策略下默认值不同",
                "required": True
            },
            "fontSize": {
                "type": ["number", "string", "Resource"],
                "description": "SymbolSpan组件大小，默认单位为fp。",
                "default": "跟随主题",
                "required": True
            },
            "fontWeight": {
                "type": ["number", "FontWeight", "string"],
                "description": "SymbolSpan组件粗细。number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。",
                "default": "FontWeight.Normal",
                "required": True
            },
            "renderingStrategy": {
                "type": "SymbolRenderingStrategy",
                "description": "SymbolSpan组件渲染策略。",
                "default": "SymbolRenderingStrategy.SINGLE",
                "required": True
            },
            "effectStrategy": {
                "type": "SymbolEffectStrategy",
                "description": "SymbolSpan组件动效策略。",
                "default": "SymbolEffectStrategy.NONE",
                "required": True
            }
        }
    },
    "RichEditorImageSpanResult": {
        "type": "object",
        "description": "后端返回的图片信息。",
        "properties": {
            "spanPosition": {
                "type": "RichEditorSpanPosition",
                "description": "Span位置。",
                "required": True
            },
            "valuePixelMap": {
                "type": "PixelMap",
                "description": "图片内容。",
                "required": False
            },
            "valueResourceStr": {
                "type": "ResourceStr",
                "description": "图片资源id。",
                "required": False
            },
            "imageStyle": {
                "type": "RichEditorImageSpanStyleResult",
                "description": "图片样式。",
                "required": True
            },
            "offsetInSpan": {
                "type": "array",
                "description": "Span里图片的起始和结束位置。",
                "required": True
            }
        }
    },
    "RichEditorImageSpanStyleResult": {
        "type": "object",
        "description": "后端返回的图片样式信息。",
        "properties": {
            "size": {
                "type": ["number", "number"],
                "description": "图片的宽度和高度，单位为px。",
                "required": True
            },
            "verticalAlign": {
                "type": "ImageSpanAlignment",
                "description": "图片垂直对齐方式。",
                "required": True
            },
            "objectFit": {
                "type": "ImageFit",
                "description": "图片缩放类型。",
                "required": True
            },
            "layoutStyle": {
                "type": "RichEditorLayoutStyle",
                "description": "图片布局风格。",
                "required": False
            }
        }
    },
    "RichEditorLayoutStyle": {
        "type": "object",
        "description": "用于描述组件不同方向的外边距和边框圆角半径的类。",
        "properties": {
            "margin": {
                "type": ["Dimension", "Margin"],
                "description": "外边距类型，用于描述组件不同方向的外边距。参数为Dimension类型时，四个方向外边距同时生效。",
                "required": False
            },
            "borderRadius": {
                "type": ["Dimension", "BorderRadiuses"],
                "description": "圆角类型，用于描述组件边框圆角半径。参数为Dimension类型时，不支持以Percentage形式设置。",
                "required": False
            }
        }
    },
    "RichEditorOptions": {
        "type": "object",
        "description": "RichEditor初始化参数。",
        "properties": {
            "controller": {
                "type": "RichEditorController",
                "description": "富文本控制器。",
                "required": True
            }
        }
    },
    "RichEditorStyledStringOptions": {
        "type": "object",
        "description": "RichEditor初始化参数。",
        "properties": {
            "controller": {
                "type": "RichEditorStyledStringController",
                "description": "富文本控制器。",
                "required": True
            }
        }
    },
    "SelectionOptions": {
        "type": "object",
        "description": "setSelection的选择项配置。",
        "properties": {
            "menuPolicy": {
                "type": "MenuPolicy",
                "description": "菜单弹出的策略。",
                "required": False
            }
        }
    },
    "TextDataDetectorConfig": {
        "type": "object",
        "description": "文本识别配置参数。",
        "properties": {
            "types": {
                "type": "TextDataDetectorType[]",
                "description": "文本识别的实体类型。设置types为null或者[]时，识别所有类型的实体，否则只识别指定类型的实体。",
                "required": True
            },
            "onDetectResultUpdate": {
                "type": "(result: string) => void",
                "description": "文本识别成功后，触发onDetectResultUpdate回调。result：文本识别的结果，Json格式。",
                "required": False
            }
        }
    },
    "RichEditorChangeValue": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "rangeBefore": {
                "type": "TextRange",
                "description": "即将被替换内容的开始和结束索引。",
                "required": True
            },
            "replacedSpans": {
                "type": "Array<RichEditorTextSpanResult>",
                "description": "替换后文本Span的具体信息。",
                "required": True
            },
            "replacedImageSpans": {
                "type": "Array<RichEditorImageSpanResult>",
                "description": "替换后ImageSpan的具体信息。",
                "required": True
            },
            "replacedSymbolSpans": {
                "type": "Array<RichEditorTextSpanResult>",
                "description": "替换后SymbolSpan的具体信息。",
                "required": True
            }
        }
    },
    "RichEditorSelection": {
        "type": "object",
        "description": "选中内容信息。",
        "properties": {
            "selection": {
                "type": "array",
                "description": "选中范围。",
                "required": True
            },
            "spans": {
                "type": "array",
                "description": "span信息。",
                "required": True
            }
        }
    },
    "RichEditorUpdateTextSpanStyleOptions": {
        "type": "object",
        "description": "文本样式选项。",
        "properties": {
            "start": {
                "type": "number",
                "description": "需要更新样式的文本起始位置，省略或者设置负值时表示从0开始。",
                "default": 0,
                "required": False
            },
            "end": {
                "type": "number",
                "description": "需要更新样式的文本结束位置，省略或者超出文本范围时表示无穷大。",
                "default": "无穷大",
                "required": False
            },
            "textStyle": {
                "type": "RichEditorTextStyle",
                "description": "文本样式。",
                "required": True
            }
        }
    },
    "RichEditorUpdateImageSpanStyleOptions": {
        "type": "object",
        "description": "图片样式选项。",
        "properties": {
            "start": {
                "type": "number",
                "description": "需要更新样式的图片起始位置，省略或者设置负值时表示从0开始。",
                "default": 0,
                "required": False
            },
            "end": {
                "type": "number",
                "description": "需要更新样式的图片结束位置，省略或者超出所有内容范围时表示无穷大。",
                "default": "无穷大",
                "required": False
            },
            "imageStyle": {
                "type": "RichEditorImageSpanStyle",
                "description": "图片样式。",
                "required": True
            }
        }
    },
    "RichEditorUpdateSymbolSpanStyleOptions": {
        "type": "object",
        "description": "SymbolSpan样式选项。",
        "properties": {
            "start": {
                "type": "number",
                "description": "需要更新样式的symbol起始位置，省略或者设置负值时表示从0开始。",
                "default": 0,
                "required": False
            },
            "end": {
                "type": "number",
                "description": "需要更新样式的symbol结束位置，省略或者超出所有内容范围时表示无穷大。",
                "default": "无穷大",
                "required": False
            },
            "symbolStyle": {
                "type": "RichEditorSymbolSpanStyle",
                "description": "组件样式。",
                "required": True
            }
        }
    },
    "RichEditorParagraphStyleOptions": {
        "type": "object",
        "description": "段落样式选项",
        "properties": {
            "start": {
                "type": "number",
                "description": "需要更新样式的段落起始位置，省略或者设置负值时表示从0开始。",
                "default": 0,
                "required": False
            },
            "end": {
                "type": "number",
                "description": "需要更新样式的段落结束位置，省略、负数或者超出所有内容范围时表示无穷大。",
                "default": "无穷大",
                "required": False
            },
            "style": {
                "type": "RichEditorParagraphStyle",
                "description": "段落样式。接口作用的范围：设定的区间所涉及的段落。当start大于end时为异常情况，此时start为0，end为无穷大。",
                "required": True
            }
        }
    },
    "RichEditorParagraphStyle": {
        "type": "object",
        "description": "段落样式。",
        "properties": {
            "textAlign": {
                "type": "TextAlign",
                "description": "设置文本段落在水平方向的对齐方式。",
                "default": "TextAlign.START",
                "required": False
            },
            "leadingMargin": {
                "type": ["Dimension", "LeadingMarginPlaceholder"],
                "description": "设置文本段落缩进，当段落仅存在ImageSpan或BuilderSpan时，此属性值不生效。参数为Dimension类型时，不支持以Percentage形式设置。",
                "default": {"size": ["0.00px", "0.00px"]},
                "required": False
            },
            "wordBreak": {
                "type": "WordBreak",
                "description": "设置断行规则。",
                "default": "WordBreak.BREAK_WORD",
                "required": False
            },
            "lineBreakStrategy": {
                "type": "LineBreakStrategy",
                "description": "设置折行规则。在wordBreak不等于breakAll的时候生效，不支持连字符。",
                "default": "LineBreakStrategy.GREEDY",
                "required": False
            }
        }
    },
    "LeadingMarginPlaceholder": {
        "type": "object",
        "description": "前导边距占位符，用于表示文本段落左侧与组件边缘之间的距离。",
        "properties": {
            "pixelMap": {
                "type": "PixelMap",
                "description": "图片内容。",
                "required": True
            },
            "size": {
                "type": ["Dimension", "Dimension"],
                "description": "图片大小，不支持设置百分比。",
                "required": True
            }
        }
    },
    "RichEditorParagraphResult": {
        "type": "object",
        "description": "后端返回的段落信息。",
        "properties": {
            "style": {
                "type": "RichEditorParagraphStyle",
                "description": "段落样式。",
                "required": True
            },
            "range": {
                "type": "array",
                "description": "段落起始和结束位置。",
                "required": True
            }
        }
    },
    "RichEditorTextSpanOptions": {
        "type": "object",
        "description": "添加文本的偏移位置和文本样式信息。",
        "properties": {
            "offset": {
                "type": "number",
                "description": "添加文本的位置。省略时，添加到所有内容的最后。当值小于0时，放在所有内容最前面；当值大于所有内容长度时，放在所有内容最后面。",
                "default": "添加到所有内容的最后",
                "required": False
            },
            "style": {
                "type": "RichEditorTextStyle",
                "description": "文本样式信息。省略时，使用系统默认文本信息。",
                "default": "系统默认文本信息",
                "required": False
            },
            "paragraphStyle": {
                "type": "RichEditorParagraphStyle",
                "description": "段落样式。",
                "required": False
            },
            "gesture": {
                "type": "RichEditorGesture",
                "description": "行为触发回调。省略时，仅使用系统默认行为。",
                "default": "系统默认行为",
                "required": False
            }
        }
    },
    "PlaceholderStyle": {
        "type": "object",
        "description": "添加提示文本的字体样式。",
        "properties": {
            "font": {
                "type": "Font",
                "description": "设置placeholder文本样式。",
                "default": "跟随主题",
                "required": False
            },
            "fontColor": {
                "type": "ResourceColor",
                "description": "设置placeholder文本颜色。",
                "default": "跟随主题",
                "required": False
            }
        }
    },
    "RichEditorImageSpanOptions": {
        "type": "object",
        "description": "添加图片的偏移位置和图片样式信息。",
        "properties": {
            "offset": {
                "type": "number",
                "description": "添加图片的位置。省略时，添加到所有内容的最后。当值小于0时，放在所有内容最前面；当值大于所有内容长度时，放在所有内容最后面。",
                "default": "添加到所有内容的最后",
                "required": False
            },
            "imageStyle": {
                "type": "RichEditorImageSpanStyle",
                "description": "图片样式信息。省略时，使用系统默认图片信息。",
                "default": "系统默认图片信息",
                "required": False
            },
            "gesture": {
                "type": "RichEditorGesture",
                "description": "行为触发回调。省略时，仅使用系统默认行为。",
                "default": "系统默认行为",
                "required": False
            }
        }
    },
    "RichEditorImageSpanStyle": {
        "type": "object",
        "description": "图片样式。",
        "properties": {
            "size": {
                "type": ["Dimension", "Dimension"],
                "description": "图片宽度和高度。默认值：size的默认值与objectFit的值有关，不同的objectFit值对应的size默认值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。",
                "required": False
            },
            "verticalAlign": {
                "type": "ImageSpanAlignment",
                "description": "图片垂直对齐方式。",
                "default": "ImageSpanAlignment.BASELINE",
                "required": False
            },
            "objectFit": {
                "type": "ImageFit",
                "description": "图片缩放类型。",
                "default": "ImageFit.Cover",
                "required": False
            },
            "layoutStyle": {
                "type": "RichEditorLayoutStyle",
                "description": "图片布局风格。默认值：{\"borderRadius\":\"\",\"margin\":\"\"}",
                "required": False
            }
        }
    },
    "RichEditorSymbolSpanOptions": {
        "type": "object",
        "description": "添加SymbolSpan组件的偏移位置和SymbolSpan组件样式信息。",
        "properties": {
            "offset": {
                "type": "number",
                "description": "添加组件的位置。省略时，添加到所有内容的最后。当值小于0时，放在所有内容最前面；当值大于所有内容长度时，放在所有内容最后面。",
                "default": "添加到所有内容的最后",
                "required": False
            },
            "style": {
                "type": "RichEditorSymbolSpanStyle",
                "description": "组件样式信息。省略时，使用系统默认样式信息。",
                "default": "系统默认样式信息",
                "required": False
            }
        }
    },
    "RichEditorSymbolSpanStyle": {
        "type": "object",
        "description": "组件SymbolSpan样式信息。",
        "properties": {
            "fontColor": {
                "type": "Array<ResourceColor>",
                "description": "设置SymbolSpan组件颜色。",
                "required": False
            },
            "fontSize": {
                "type": ["number", "string", "Resource"],
                "description": "设置SymbolSpan组件大小，默认单位为fp。",
                "required": False
            },
            "fontWeight": {
                "type": ["number", "FontWeight", "string"],
                "description": "设置SymbolSpan组件粗细。number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。",
                "default": "FontWeight.Normal",
                "required": False
            },
            "renderingStrategy": {
                "type": "SymbolRenderingStrategy",
                "description": "设置SymbolSpan组件渲染策略。",
                "default": "SymbolRenderingStrategy.SINGLE",
                "required": False
            },
            "effectStrategy": {
                "type": "SymbolEffectStrategy",
                "description": "设置SymbolSpan组件动效策略。",
                "default": "SymbolEffectStrategy.NONE",
                "required": False
            }
        }
    },
    "RichEditorBuilderSpanOptions": {
        "type": "object",
        "description": "添加图片的偏移位置和图片样式信息。",
        "properties": {
            "offset": {
                "type": "number",
                "description": "添加builder的位置。省略或者为异常值时，添加到所有内容的最后。",
                "default": "添加到所有内容的最后",
                "required": False
            }
        }
    },
    "RichEditorSpan": {
        "type": "object",
        "description": "RichEditor span信息。",
        "properties": {
            "type": {
                "type": ["RichEditorImageSpanResult", "RichEditorTextSpanResult"],
                "description": "后端返回的图片信息或文本样式信息。",
                "required": True
            }
        }
    },
    "RichEditorRange": {
        "type": "object",
        "description": "范围信息。",
        "properties": {
            "start": {
                "type": "number",
                "description": "起始位置，省略或者设置负值时表示从0开始。",
                "default": 0,
                "required": False
            },
            "end": {
                "type": "number",
                "description": "结束位置，省略或者超出所有内容范围时表示无穷大。",
                "default": "无穷大",
                "required": False
            }
        }
    },
    "SelectionMenuOptions": {
        "type": "object",
        "description": "菜单的选项。",
        "properties": {
            "onAppear": {
                "type": "MenuOnAppearCallback",
                "description": "自定义选择菜单弹出时回调。",
                "required": False
            },
            "onDisappear": {
                "type": "Callback<void>",
                "description": "自定义选择菜单关闭时回调。",
                "required": False
            }
        }
    },
    "PasteEvent": {
        "type": "object",
        "description": "定义用户粘贴事件。",
        "properties": {
            "preventDefault": {
                "type": "Callback<void>",
                "description": "阻止系统默认粘贴事件。",
                "required": False
            }
        }
    },
    "CutEvent": {
        "type": "object",
        "description": "定义用户剪切事件。",
        "properties": {
            "preventDefault": {
                "type": "Callback<void>",
                "description": "阻止系统默认剪切事件。",
                "required": False
            }
        }
    },
    "CopyEvent": {
        "type": "object",
        "description": "定义用户拷贝事件。",
        "properties": {
            "preventDefault": {
                "type": "Callback<void>",
                "description": "阻止系统默认拷贝事件。",
                "required": False
            }
        }
    },
    "RichEditorGesture": {
        "type": "object",
        "description": "用户行为回调。",
        "properties": {
            "onClick": {
                "type": "Callback<ClickEvent>",
                "description": "ClickEvent为用户点击事件。点击完成时回调事件。双击时，第一次点击触发回调事件。",
                "required": False
            },
            "onLongPress": {
                "type": "Callback<GestureEvent>",
                "description": "GestureEvent为用户长按事件。长按完成时回调事件。",
                "required": False
            }
        }
    },
    "KeyboardOptions": {
        "type": "object",
        "description": "设置自定义键盘是否支持避让功能。",
        "properties": {
            "supportAvoidance": {
                "type": "boolean",
                "description": "设置自定义键盘是否支持避让功能",
                "default": False,
                "required": False
            }
        }
    },
    "SubmitCallback": {
        "type": "object",
        "description": "软键盘按下回车键时的回调事件。",
        "properties": {
            "enterKey": {
                "type": "EnterKeyType",
                "description": "软键盘输入法回车键类型。具体类型见EnterKeyType枚举说明。",
                "required": True
            },
            "event": {
                "type": "SubmitEvent",
                "description": "当提交的时候，提供保持RichEditor编辑状态的方法。",
                "required": True
            }
        }
    },
    "MenuOnAppearCallback": {
        "type": "object",
        "description": "自定义选择菜单弹出时触发的回调事件。",
        "properties": {
            "start": {
                "type": "number",
                "description": "选中内容的起始位置。",
                "required": True
            },
            "end": {
                "type": "number",
                "description": "选中内容的终止位置。",
                "required": True
            }
        }
    },
    "PasteEventCallback": {
        "type": "object",
        "description": "完成粘贴前，触发回调。",
        "properties": {
            "event": {
                "type": "PasteEvent",
                "description": "定义用户粘贴事件。",
                "required": False
            }
        }
    },
    "OnDidChangeCallback": {
        "type": "object",
        "description": "文本变换后回调。",
        "properties": {
            "rangeBefore": {
                "type": "TextRange",
                "description": "文本变化前将要被替换的文本范围。",
                "required": True
            },
            "rangeAfter": {
                "type": "TextRange",
                "description": "文本变化后新增内容的文本范围。",
                "required": True
            }
        }
    },
    "StyledStringChangedListener": {
        "type": "object",
        "description": "属性字符串的文本内容变化监听器。",
        "properties": {
            "onWillChange": {
                "type": "Callback<StyledStringChangeValue, boolean>",
                "description": "文本内容将要变化回调函数。",
                "required": False
            },
            "onDidChange": {
                "type": "OnDidChangeCallback",
                "description": "文本内容完成变化回调函数。",
                "required": False
            }
        }
    },
    "StyledStringChangeValue": {
        "type": "object",
        "description": "属性字符串的文本变化信息。",
        "properties": {
            "range": {
                "type": "TextRange",
                "description": "即将被替换的属性字符串子串在原字符串中的范围。",
                "required": True
            },
            "replacementString": {
                "type": "StyledString",
                "description": "用于替换的属性字符串。",
                "required": True
            }
        }
    },
    "ScrollBarOptions": {
        "type": "object",
        "description": "ScrollBar组件负责定义可滚动区域的行为样式，ScrollBar的子节点负责定义滚动条的行为样式。滚动条组件与可滚动组件通过Scroller进行绑定，且只有当两者方向相同时，才能联动，ScrollBar与可滚动组件仅支持一对一绑定。从API version 12开始，ScrollBar组件没有子节点时，支持显示默认样式的滚动条。",
        "properties": {
            "scroller": {
                "type": "Scroller",
                "description": "可滚动组件的控制器。用于与可滚动组件进行绑定。",
                "required": True
            },
            "direction": {
                "type": "ScrollBarDirection",
                "description": "滚动条的方向，控制可滚动组件对应方向的滚动。",
                "default": "ScrollBarDirection.Vertical"
            },
            "state": {
                "type": "BarState",
                "description": "滚动条状态。",
                "default": "BarState.Auto"
            }
        }
    },
    "ScrollBarDirection": {
        "type": "enum",
        "enum": ["Vertical", "Horizontal"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "Vertical": "纵向滚动条",
            "Horizontal": "横向滚动条"
        }
    },
    "IconOptions": {
        "type": "object",
        "description": "IconOptions10+对象说明",
        "properties": {
            "size": {
                "type": "Length",
                "description": "图标尺寸，不支持百分比。",
                "required": False
            },
            "color": {
                "type": "ResourceColor",
                "description": "图标颜色。",
                "required": False
            },
            "src": {
                "type": "ResourceStr",
                "description": "图标/图片源。",
                "required": False
            }
        }
    },
    "SearchButtonOptions": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "fontSize": {
                "type": "Length",
                "description": "文本按钮字体大小，不支持百分比。",
                "required": False
            },
            "fontColor": {
                "type": "ResourceColor",
                "description": "文本按钮字体颜色。",
                "required": False
            }
        }
    },
    "CancelButtonStyle": {
        "type": "enum",
        "enum": ["CONSTANT", "INVISIBLE", "INPUT"],
        "description": "清除按钮样式枚举类",
        "enumDescriptions": {
            "CONSTANT": "清除按钮常显样式",
            "INVISIBLE": "清除按钮常隐样式",
            "INPUT": "清除按钮输入样式"
        }
    },
    "SearchType": {
        "type": "enum",
        "enum": ["NORMAL", "NUMBER", "PHONE_NUMBER", "EMAIL", "NUMBER_DECIMAL", "URL"],
        "description": "该枚举类定义了不同的输入模式",
        "enumDescriptions": {
            "NORMAL": "基本输入模式。支持输入数字、字母、下划线、空格、特殊字符。",
            "NUMBER": "纯数字输入模式。",
            "PHONE_NUMBER": "电话号码输入模式。支持输入数字、空格、+ 、-、*、#、(、)，长度不限。",
            "EMAIL": "邮箱地址输入模式。支持数字，字母，下划线、小数点、!、#、$、%、&、'、*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。",
            "NUMBER_DECIMAL": "带小数点的数字输入模式。支持数字，小数点（只能存在一个小数点）。",
            "URL": "带URL的输入模式。"
        }
    },
    "CancelButtonOptions": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "style": {
                "type": "CancelButtonStyle",
                "description": "右侧清除按钮显示状态。",
                "required": False
            },
            "icon": {
                "type": "IconOptions",
                "description": "右侧清除按钮图标。",
                "required": False
            }
        }
    },
    "CancelButtonSymbolOptions": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "style": {
                "type": "CancelButtonStyle",
                "description": "右侧清除按钮显示状态。",
                "required": False
            },
            "icon": {
                "type": "SymbolGlyphModifier",
                "description": "右侧清除按钮Symbol图标。",
                "required": False
            }
        }
    },
    "SelectOption": {
        "type": "object",
        "description": "SelectOption对象说明",
        "properties": {
            "value": {
                "type": "ResourceStr",
                "description": "下拉选项内容。",
                "required": True
            },
            "icon": {
                "type": "ResourceStr",
                "description": "下拉选项图片。",
                "required": False
            },
            "symbolIcon": {
                "type": "SymbolGlyphModifier",
                "description": "下拉选项Symbol图片。symbolIcon优先级高于icon。",
                "required": False
            }
        }
    },
    "ArrowPosition": {
        "type": "enum",
        "enum": ["END", "START"],
        "description": "元服务API： 从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "END": "文字在前，箭头在后。",
            "START": "箭头在前，文字在后。"
        }
    },
    "MenuAlignType": {
        "type": "enum",
        "enum": ["START", "CENTER", "END"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "START": "按照语言方向起始端对齐。",
            "CENTER": "居中对齐。",
            "END": "按照语言方向末端对齐。"
        }
    },
    "MenuItemConfiguration": {
        "type": "object",
        "description": "MenuItemConfiguration对象说明，从API version 12开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "value": {
                "type": "ResourceStr",
                "description": "下拉菜单项的文本内容。",
                "required": True
            },
            "icon": {
                "type": "ResourceStr",
                "description": "下拉菜单项的图片内容。",
                "required": False
            },
            "symbolIcon": {
                "type": "SymbolGlyphModifier",
                "description": "下拉选项Symbol图片内容。",
                "required": False
            },
            "selected": {
                "type": "boolean",
                "description": "下拉菜单项是否被选中。",
                "default": False,
                "required": True
            },
            "index": {
                "type": "number",
                "description": "下拉菜单项的索引。",
                "required": True
            },
            "triggerSelect": {
                "type": "function",
                "description": "下拉菜单选中某一项的回调函数。index: 选中菜单项的索引。value: 选中菜单项的文本。说明: index会赋值给事件onSelect回调中的索引参数； value会返回给Select组件显示，同时会赋值给事件onSelect回调中的文本参数。",
                "required": True
            }
        }
    },
    "SliderOptions": {
        "type": "object",
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "value": {
                "type": "number",
                "description": "当前进度值。从API version 10开始，该参数支持$$双向绑定变量。",
                "default": "与参数min的取值一致",
                "required": False
            },
            "min": {
                "type": "number",
                "description": "设置最小值。min >= max异常情况，min取默认值0，max取默认值100。value不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。",
                "default": 0,
                "required": False
            },
            "max": {
                "type": "number",
                "description": "设置最大值。min >= max异常情况，min取默认值0，max取默认值100。value不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。",
                "default": 100,
                "required": False
            },
            "step": {
                "type": "number",
                "description": "设置Slider滑动步长。若设置的step值小于0或大于max值时，则按默认值显示。",
                "default": 1,
                "required": False
            },
            "style": {
                "type": "SliderStyle",
                "description": "设置Slider的滑块与滑轨显示样式。",
                "default": "SliderStyle.OutSet",
                "required": False
            },
            "direction": {
                "type": "Axis",
                "description": "设置滑动条滑动方向为水平或竖直方向。",
                "default": "Axis.Horizontal",
                "required": False
            },
            "reverse": {
                "type": "boolean",
                "description": "设置滑动条取值范围是否反向，横向Slider默认为从左往右滑动，竖向Slider默认为从上往下滑动。",
                "default": False,
                "required": False
            }
        }
    },
    "SliderStyle": {
        "type": "enum",
        "enum": ["OutSet", "InSet", "NONE"],
        "description": "滑块在滑轨上、滑轨内或无滑块",
        "enumDescriptions": {
            "OutSet": "滑块在滑轨上",
            "InSet": "滑块在滑轨内",
            "NONE": "无滑块"
        }
    },
    "SliderBlockStyle": {
        "type": "object",
        "description": "Slider组件滑块形状参数。",
        "properties": {
            "type": {
                "type": "SliderBlockType",
                "description": "设置滑块形状。",
                "default": "SliderBlockType.DEFAULT",
                "required": True
            },
            "image": {
                "type": "ResourceStr",
                "description": "设置滑块图片资源。图片显示区域大小由blockSize属性控制，请勿输入尺寸过大的图片。",
                "required": False
            },
            "shape": {
                "type": ["Circle", "Ellipse", "Path", "Rect"],
                "description": "设置滑块使用的自定义形状。",
                "required": False
            }
        }
    },
    "SliderBlockType": {
        "type": "enum",
        "enum": ["DEFAULT", "IMAGE", "SHAPE"],
        "description": "Slider组件滑块形状枚举。",
        "enumDescriptions": {
            "DEFAULT": "使用默认滑块（圆形）。",
            "IMAGE": "使用图片资源作为滑块。",
            "SHAPE": "使用自定义形状作为滑块。"
        }
    },
    "SliderInteraction": {
        "type": "enum",
        "enum": ["SLIDE_AND_CLICK", "SLIDE_ONLY", "SLIDE_AND_CLICK_UP"],
        "description": "用户与滑动条组件交互方式",
        "enumDescriptions": {
            "SLIDE_AND_CLICK": "用户可拖拽滑块或者点击滑轨使滑块移动，鼠标或手指按下即发生移动。",
            "SLIDE_ONLY": "不允许用户通过点击滑轨使滑块移动。",
            "SLIDE_AND_CLICK_UP": "用户可拖拽滑块或者点击滑轨使滑块移动，鼠标或手指抬起时，若与屏幕按压位置一致，则触发移动。"
        }
    },
    "SlideRange": {
        "type": "object",
        "description": "定义SlideRange中使用的回调类型。",
        "properties": {
            "from": {
                "type": "number",
                "description": "设置有效滑动区间的开始。",
                "required": True
            },
            "to": {
                "type": "number",
                "description": "设置有效滑动区间的结束。",
                "required": True
            }
        }
    },
    "SliderChangeMode": {
        "type": "enum",
        "enum": ["Begin", "Moving", "End", "Click"],
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "Begin": "手势/鼠标接触或者按下滑块。",
            "Moving": "正在拖动滑块过程中。",
            "End": "手势/鼠标离开滑块。",
            "Click": "点击滑动条使滑块位置移动。"
        }
    },
    "SliderConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。元服务API： 从API version 12开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "value": {
                "type": "number",
                "description": "当前进度值。",
                "required": True
            },
            "min": {
                "type": "number",
                "description": "最小值。",
                "required": True
            },
            "max": {
                "type": "number",
                "description": "最大值。",
                "required": True
            },
            "step": {
                "type": "number",
                "description": "Slider滑动步长。",
                "required": True
            },
            "triggerChange": {
                "type": "SliderTriggerChangeCallback",
                "description": "触发Slider变化。",
                "required": True
            }
        }
    },
    "SliderTriggerChangeCallback": {
        "type": "object",
        "description": "定义SliderConfiguration中使用的回调类型。",
        "properties": {
            "value": {
                "type": "number",
                "description": "设置当前的进度值。",
                "required": True
            },
            "mode": {
                "type": "SliderChangeMode",
                "description": "设置事件触发的相关状态值。",
                "required": True
            }
        }
    },
    "TextBackgroundStyle": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "color": {
                "type": "ResourceColor",
                "description": "文本背景色。",
                "required": False
            },
            "radius": {
                "type": ["Dimension", "BorderRadiuses"],
                "description": "文本背景圆角。",
                "required": False
            }
        }
    },
    "ItemState": {
        "type": "enum",
        "enum": ["Normal", "Disabled", "Waiting", "Skip"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "Normal": "正常状态，右侧文本按钮正常显示，可点击进入下一个StepperItem。",
            "Disabled": "不可用状态，右侧文本按钮灰度显示，不可点击进入下一个StepperItem。",
            "Waiting": "等待状态，右侧文本按钮不显示，显示等待进度条，不可点击进入下一个StepperItem。",
            "Skip": "跳过状态，右侧文本按钮默认显示“跳过”"
        }
    },
    "SymbolEffect": {
        "type": "object",
        "description": "定义SymbolEffect类。",
        "properties": {
            "type": {
                "type": "ButtonType",
                "description": "type属性的描述。",
                "default": "ButtonType.Capsule"
            },
            "stateEffect": {
                "type": "boolean",
                "description": "stateEffect属性的描述",
                "default": True
            },
            "buttonStyle": {
                "type": "number",
                "description": "buttonStyle属性的描述",
                "default": "ButtonStyleMode.EMPHASIZED"
            },
            "controlSize": {
                "type": ["number", "Resource"],
                "description": "controlSize属性的描述。",
                "default": 1
            }
        }
    },
    "ScaleSymbolEffect": {
        "type": "object",
        "description": "ScaleSymbolEffect继承自父类SymbolEffect。从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "scope": {
                "type": "EffectScope",
                "description": "动效范围。",
                "default": "EffectScope.LAYER",
                "required": False
            },
            "direction": {
                "type": "EffectDirection",
                "description": "动效方向。",
                "default": "EffectDirection.DOWN",
                "required": False
            }
        }
    },
    "HierarchicalSymbolEffect": {
        "type": "object",
        "description": "HierarchicalSymbolEffect继承自父类SymbolEffect。从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "fillStyle": {
                "type": "EffectFillStyle",
                "description": "动效模式。",
                "default": "EffectFillStyle.CUMULATIVE",
                "required": False
            }
        }
    },
    "AppearSymbolEffect": {
        "type": "object",
        "description": "AppearSymbolEffect继承自父类SymbolEffect。从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "scope": {
                "type": "EffectScope",
                "description": "动效范围。",
                "default": "EffectScope.LAYER",
                "required": False
            }
        }
    },
    "DisappearSymbolEffect": {
        "type": "object",
        "description": "DisappearSymbolEffect继承自父类SymbolEffect。从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "scope": {
                "type": "EffectScope",
                "description": "动效范围。",
                "default": "EffectScope.LAYER",
                "required": False
            }
        }
    },
    "BounceSymbolEffect": {
        "type": "object",
        "description": "BounceSymbolEffect继承自父类SymbolEffect。从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "scope": {
                "type": "EffectScope",
                "description": "动效范围。",
                "default": "EffectScope.LAYER",
                "required": False
            },
            "direction": {
                "type": "EffectDirection",
                "description": "动效方向。",
                "default": "EffectDirection.DOWN",
                "required": False
            }
        }
    },
    "ReplaceSymbolEffect": {
        "type": "object",
        "description": "ReplaceSymbolEffect继承自父类SymbolEffect。从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "scope": {
                "type": "EffectScope",
                "description": "动效范围。",
                "default": "EffectScope.LAYER",
                "required": False
            }
        }
    },
    "PulseSymbolEffect": {
        "type": "object",
        "description": "PulseSymbolEffect的构造函数，脉冲动效。",
        "properties": {}
    },
    "EffectDirection": {
        "type": "enum",
        "enum": ["DOWN", "UP"],
        "description": "该枚举类用于描述图标的动画效果，从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "DOWN": "图标缩小再复原。",
            "UP": "图标放大再复原。"
        }
    },
    "EffectScope": {
        "type": "enum",
        "enum": ["LAYER", "WHOLE"],
        "description": "从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "LAYER": "分层模式。",
            "WHOLE": "整体模式。"
        }
    },
    "EffectFillStyle": {
        "type": "enum",
        "enum": ["CUMULATIVE", "ITERATIVE"],
        "description": "从API version 12开始，该接口支持在ArkTS卡片和元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "CUMULATIVE": "累加模式。",
            "ITERATIVE": "迭代模式。"
        }
    },
    "SymbolEffectStrategy": {
        "type": "enum",
        "enum": ["NONE", "SCALE", "HIERARCHICAL"],
        "description": "动效类型的枚举值。设置动效后启动即生效，无需触发。",
        "enumDescriptions": {
            "NONE": "无动效（默认值）。",
            "SCALE": "整体缩放动效。",
            "HIERARCHICAL": "层级动效。"
        }
    },
    "SymbolRenderingStrategy": {
        "type": "enum",
        "enum": ["SINGLE", "MULTIPLE_COLOR", "MULTIPLE_OPACITY"],
        "description": "渲染模式的枚举值。",
        "enumDescriptions": {
            "SINGLE": "单色模式（默认值）。默认为黑色，可以设置一个颜色。当用户设置多个颜色时，仅生效第一个颜色。",
            "MULTIPLE_COLOR": "多色模式。最多可以设置三个颜色。当用户只设置一个颜色时，修改第一层颜色，其他颜色保持默认颜色。颜色设置顺序与图标分层顺序匹配，当颜色数量大于图标分层时，多余的颜色不生效。仅支持设置颜色，不透明度设置不生效。",
            "MULTIPLE_OPACITY": "分层模式。默认为黑色，可以设置一个颜色。当用户设置多个颜色时，仅生效第一个颜色。不透明度与图层相关，第一层100%、第二层50%、第三层20%。"
        }
    },
    "TextSpanType": {
        "type": "enum",
        "enum": ["TEXT", "IMAGE", "MIXED"],
        "description": "Span类型信息。",
        "enumDescriptions": {
            "TEXT": "Span为文字类型。",
            "IMAGE": "Span为图像类型。",
            "MIXED": "Span为图文混合类型。"
        }
    },
    "TextResponseType": {
        "type": "enum",
        "enum": ["RIGHT_CLICK", "LONG_PRESS", "SELECT"],
        "description": "该枚举类用于描述触发菜单弹出的不同方式",
        "enumDescriptions": {
            "RIGHT_CLICK": "通过鼠标右键触发菜单弹出",
            "LONG_PRESS": "通过长按触发菜单弹出",
            "SELECT": "通过鼠标选中触发菜单弹出"
        }
    },
    "TextOptions": {
        "type": "object",
        "description": "Text初始化参数。",
        "properties": {
            "controller": {
                "type": "TextController",
                "description": "文本控制器。",
                "required": True
            }
        }
    },
    "TextController": {
        "type": "object",
        "description": "Text组件的控制器。",
        "properties": {
            "controller": {
                "type": "TextController",
                "description": "导入对象",
                "required": True
            }
        }
    },
    "TextAreaOptions": {
        "type": "object",
        "description": "TextAreaOptions对象说明",
        "properties": {
            "placeholder": {
                "type": "ResourceStr",
                "description": "设置无输入时的提示文本。输入内容后，提示文本不显示。仅设置placeholder属性时，手柄依然跟随拖动，手柄松开后光标停留在文字开头位置。",
                "required": False
            },
            "text": {
                "type": "ResourceStr",
                "description": "设置输入框当前的文本内容。建议通过onChange事件将状态变量与文本实时绑定，避免组件刷新时TextArea中的文本内容异常。从API version 10开始，该参数支持$$双向绑定变量。",
                "required": False
            },
            "controller": {
                "type": "TextAreaController",
                "description": "设置TextArea控制器。",
                "required": False
            }
        }
    },
    "TextAreaController": {
        "type": "object",
        "description": "TextArea组件的控制器继承自TextContentControllerBase。",
        "properties": {
            "controller": {
                "type": "TextAreaController",
                "description": "导入对象",
                "required": True
            }
        }
    },
    "TextAreaType": {
        "type": "enum",
        "enum": ["NORMAL", "NUMBER", "PHONE_NUMBER", "EMAIL", "NUMBER_DECIMAL", "URL"],
        "description": "该枚举类定义了不同类型的输入模式",
        "enumDescriptions": {
            "NORMAL": "基本输入模式。支持输入数字、字母、下划线、空格、特殊字符。",
            "NUMBER": "纯数字输入模式。",
            "PHONE_NUMBER": "电话号码输入模式。支持输入数字、空格、+ 、-、*、#、(、)，长度不限。",
            "EMAIL": "邮箱地址输入模式。支持数字，字母，下划线、小数点、!、#、$、%、&、'、*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。",
            "NUMBER_DECIMAL": "带小数点的数字输入模式。支持数字，小数点（只能存在一个小数点）。",
            "URL": "带URL的输入模式。"
        }
    },
    "ContentType": {
        "type": "enum",
        "enum": [
            "USER_NAME",
            "PASSWORD",
            "NEW_PASSWORD",
            "FULL_STREET_ADDRESS",
            "HOUSE_NUMBER",
            "DISTRICT_ADDRESS",
            "CITY_ADDRESS",
            "PROVINCE_ADDRESS",
            "COUNTRY_ADDRESS",
            "PERSON_FULL_NAME",
            "PERSON_LAST_NAME",
            "PERSON_FIRST_NAME",
            "PHONE_NUMBER",
            "PHONE_COUNTRY_CODE",
            "FULL_PHONE_NUMBER",
            "EMAIL_ADDRESS",
            "BANK_CARD_NUMBER",
            "ID_CARD_NUMBER",
            "NICKNAME",
            "DETAIL_INFO_WITHOUT_STREET",
            "FORMAT_ADDRESS"
        ],
        "description": "自动填充类型。",
        "enumDescriptions": {
            "USER_NAME": "【用户名】在已启用密码保险箱的情况下，支持用户名的自动保存和自动填充。",
            "PASSWORD": "【密码】在已启用密码保险箱的情况下，支持密码的自动保存和自动填充。",
            "NEW_PASSWORD": "【新密码】在已启用密码保险箱的情况下，支持自动生成新密码。",
            "FULL_STREET_ADDRESS": "【详细地址】在已启用情景化自动填充的情况下，支持详细地址的自动保存和自动填充。",
            "HOUSE_NUMBER": "【门牌号】在已启用情景化自动填充的情况下，支持门牌号的自动保存和自动填充。",
            "DISTRICT_ADDRESS": "【区/县】在已启用情景化自动填充的情况下，支持区/县的自动保存和自动填充。",
            "CITY_ADDRESS": "【市】在已启用情景化自动填充的情况下，支持市的自动保存和自动填充。",
            "PROVINCE_ADDRESS": "【省】在已启用情景化自动填充的情况下，支持省的自动保存和自动填充。",
            "COUNTRY_ADDRESS": "【国家】在已启用情景化自动填充的情况下，支持国家的自动保存和自动填充。",
            "PERSON_FULL_NAME": "【姓名】在已启用情景化自动填充的情况下，支持姓名的自动保存和自动填充。",
            "PERSON_LAST_NAME": "【姓氏】在已启用情景化自动填充的情况下，支持姓氏的自动保存和自动填充。",
            "PERSON_FIRST_NAME": "【名字】在已启用情景化自动填充的情况下，支持名字的自动保存和自动填充。",
            "PHONE_NUMBER": "【手机号码】在已启用情景化自动填充的情况下，支持手机号码的自动保存和自动填充。",
            "PHONE_COUNTRY_CODE": "【国家代码】在已启用情景化自动填充的情况下，支持国家代码的自动保存和自动填充。",
            "FULL_PHONE_NUMBER": "【包含国家代码的手机号码】在已启用情景化自动填充的情况下，支持包含国家代码的手机号码的自动保存和自动填充。",
            "EMAIL_ADDRESS": "【邮箱地址】在已启用情景化自动填充的情况下，支持邮箱地址的自动保存和自动填充。",
            "BANK_CARD_NUMBER": "【银行卡号】在已启用情景化自动填充的情况下，支持银行卡号的自动保存和自动填充。",
            "ID_CARD_NUMBER": "【身份证号】在已启用情景化自动填充的情况下，支持身份证号的自动保存和自动填充。",
            "NICKNAME": "【昵称】在已启用情景化自动填充的情况下，支持昵称的自动保存和自动填充。",
            "DETAIL_INFO_WITHOUT_STREET": "【无街道地址】在已启用情景化自动填充的情况下，支持无街道地址的自动保存和自动填充。",
            "FORMAT_ADDRESS": "【标准地址】在已启用情景化自动填充的情况下，支持标准地址的自动保存和自动填充。"
        }
    },
    "TextClockController": {
        "type": "object",
        "description": "TextClock容器组件的控制器，可以将该控制器绑定到TextClock组件，通过它控制文本时钟的启动与停止。一个TextClock组件仅支持绑定一个控制器。",
        "properties": {
            "controller": {
                "type": "TextClockController",
                "description": "TextClockController的实例，用于控制文本时钟的启动与停止。",
                "required": True
            }
        }
    },
    "TextClockConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。元服务API： 从API version 12开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "timeZoneOffset": {
                "type": "number",
                "description": "当前文本时钟时区偏移量。",
                "required": True
            },
            "started": {
                "type": "boolean",
                "description": "指示文本时钟是否启动。",
                "default": True,
                "required": False
            },
            "timeValue": {
                "type": "number",
                "description": "当前文本时钟时区的UTC秒数。",
                "required": True
            }
        }
    },
    "InputType": {
        "type": "enum",
        "enum": ["Normal", "Password", "Email", "Number", "PhoneNumber", "USER_NAME", "NEW_PASSWORD", "NUMBER_PASSWORD",
                 "NUMBER_DECIMAL", "URL"],
        "description": "系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "Normal": "基本输入模式，无特殊限制。",
            "Password": "密码输入模式。支持输入数字、字母、下划线、空格、特殊字符。密码显示小眼睛图标，默认输入文字短暂显示后变成圆点，从API version 12开始，特定设备上输入文字直接显示为圆点。密码输入模式不支持下划线样式。在已启用密码保险箱的情况下，支持用户名、密码的自动保存和自动填充。",
            "Email": "邮箱地址输入模式。支持数字、字母、下划线、小数点、!、#、$、%、&、'、*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。",
            "Number": "纯数字输入模式。",
            "PhoneNumber": "电话号码输入模式。支持输入数字、空格、+ 、-、*、#、(、)，长度不限。",
            "USER_NAME": "用户名输入模式。在已启用密码保险箱的情况下，支持用户名、密码的自动保存和自动填充。",
            "NEW_PASSWORD": "新密码输入模式。密码显示小眼睛图标，默认输入文字短暂显示后变成圆点，从API version 12开始，特定设备上输入文字直接显示为圆点。在已启用密码保险箱的情况下，支持自动生成新密码。",
            "NUMBER_PASSWORD": "纯数字密码输入模式。密码显示小眼睛图标，默认输入文字短暂显示后变成圆点，从API version 12开始，特定设备上输入文字直接显示为圆点。密码输入模式不支持下划线样式。",
            "NUMBER_DECIMAL": "带小数点的数字输入模式。支持数字，小数点（只能存在一个小数点）。",
            "URL": "带URL的输入模式。"
        }
    },
    "ContentType12": {
        "type": "enum",
        "enum": [
            "USER_NAME",
            "PASSWORD",
            "NEW_PASSWORD",
            "FULL_STREET_ADDRESS",
            "HOUSE_NUMBER",
            "DISTRICT_ADDRESS",
            "CITY_ADDRESS",
            "PROVINCE_ADDRESS",
            "COUNTRY_ADDRESS",
            "PERSON_FULL_NAME",
            "PERSON_LAST_NAME",
            "PERSON_FIRST_NAME",
            "PHONE_NUMBER",
            "PHONE_COUNTRY_CODE",
            "FULL_PHONE_NUMBER",
            "EMAIL_ADDRESS",
            "BANK_CARD_NUMBER",
            "ID_CARD_NUMBER",
            "NICKNAME",
            "DETAIL_INFO_WITHOUT_STREET",
            "FORMAT_ADDRESS"
        ],
        "description": "自动填充类型。",
        "enumDescriptions": {
            "USER_NAME": "【用户名】在已启用密码保险箱的情况下，支持用户名的自动保存和自动填充。",
            "PASSWORD": "【密码】在已启用密码保险箱的情况下，支持密码的自动保存和自动填充。",
            "NEW_PASSWORD": "【新密码】在已启用密码保险箱的情况下，支持自动生成新密码。",
            "FULL_STREET_ADDRESS": "【详细地址】在已启用情景化自动填充的情况下，支持详细地址的自动保存和自动填充。",
            "HOUSE_NUMBER": "【门牌号】在已启用情景化自动填充的情况下，支持门牌号的自动保存和自动填充。",
            "DISTRICT_ADDRESS": "【区/县】在已启用情景化自动填充的情况下，支持区/县的自动保存和自动填充。",
            "CITY_ADDRESS": "【市】在已启用情景化自动填充的情况下，支持市的自动保存和自动填充。",
            "PROVINCE_ADDRESS": "【省】在已启用情景化自动填充的情况下，支持省的自动保存和自动填充。",
            "COUNTRY_ADDRESS": "【国家】在已启用情景化自动填充的情况下，支持国家的自动保存和自动填充。",
            "PERSON_FULL_NAME": "【姓名】在已启用情景化自动填充的情况下，支持姓名的自动保存和自动填充。",
            "PERSON_LAST_NAME": "【姓氏】在已启用情景化自动填充的情况下，支持姓氏的自动保存和自动填充。",
            "PERSON_FIRST_NAME": "【名字】在已启用情景化自动填充的情况下，支持名字的自动保存和自动填充。",
            "PHONE_NUMBER": "【手机号码】在已启用情景化自动填充的情况下，支持手机号码的自动保存和自动填充。",
            "PHONE_COUNTRY_CODE": "【国家代码】在已启用情景化自动填充的情况下，支持国家代码的自动保存和自动填充。",
            "FULL_PHONE_NUMBER": "【包含国家代码的手机号码】在已启用情景化自动填充的情况下，支持包含国家代码的手机号码的自动保存和自动填充。",
            "EMAIL_ADDRESS": "【邮箱地址】在已启用情景化自动填充的情况下，支持邮箱地址的自动保存和自动填充。",
            "BANK_CARD_NUMBER": "【银行卡号】在已启用情景化自动填充的情况下，支持银行卡号的自动保存和自动填充。",
            "ID_CARD_NUMBER": "【身份证号】在已启用情景化自动填充的情况下，支持身份证号的自动保存和自动填充。",
            "NICKNAME": "【昵称】在已启用情景化自动填充的情况下，支持昵称的自动保存和自动填充。",
            "DETAIL_INFO_WITHOUT_STREET": "【无街道地址】在已启用情景化自动填充的情况下，支持无街道地址的自动保存和自动填充。",
            "FORMAT_ADDRESS": "【标准地址】在已启用情景化自动填充的情况下，支持标准地址的自动保存和自动填充。"
        }
    },
    "TextInputStyle": {
        "type": "enum",
        "enum": ["Default", "Inline"],
        "description": "元服务API： 从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "Default": "默认风格，光标宽1.5vp，光标高度与文本选中底板高度和字体大小相关。",
            "Inline": "内联输入风格。文本选中底板高度与输入框高度相同。内联输入是在有明显的编辑态/非编辑态的区分场景下使用，例如：文件列表视图中的重命名。不支持showError属性。"
        }
    },
    "PasswordIcon": {
        "type": "object",
        "description": "密码输入模式时，能够切换密码隐藏的显示状态的图标和密码显示的隐藏状态的图标。",
        "properties": {
            "onIconSrc": {
                "type": ["string", "Resource"],
                "description": "密码输入模式时，能够切换密码隐藏的显示状态的图标。",
                "required": False
            },
            "offIconSrc": {
                "type": ["string", "Resource"],
                "description": "密码输入模式时，能够切换密码显示的隐藏状态的图标。",
                "required": False
            }
        }
    },
    "TextInputController": {
        "type": "object",
        "description": "TextInput组件的控制器继承自TextContentControllerBase。",
        "properties": {
            "controller": {
                "type": "TextInputController",
                "description": "导入对象",
                "required": True
            }
        }
    },
    "UnderlineColor": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "typing": {
                "type": ["ResourceColor", "undefined"],
                "description": "键入时下划线颜色。",
                "default": "恢复默认",
                "required": False
            },
            "normal": {
                "type": ["ResourceColor", "undefined"],
                "description": "非特殊状态时下划线颜色。",
                "default": "恢复默认",
                "required": False
            },
            "error": {
                "type": ["ResourceColor", "undefined"],
                "description": "错误时下划线颜色。此选项会修改showCounter属性中达到最大字符数时的颜色。",
                "default": "恢复默认",
                "required": False
            },
            "disable": {
                "type": ["ResourceColor", "undefined"],
                "description": "禁用时下划线颜色。",
                "default": "恢复默认",
                "required": False
            }
        }
    },
    "SubmitEvent": {
        "type": "object",
        "description": "定义用户提交事件。",
        "properties": {
            "keepEditableState": {
                "type": "function",
                "description": "用户自定义输入框编辑状态。调用时保持编辑态。",
                "required": True
            },
            "text": {
                "type": "string",
                "description": "输入框文本内容。",
                "required": True
            }
        }
    },
    "TextPickerOptions": {
        "type": "object",
        "description": "TextPickerOptions对象说明",
        "properties": {
            "range": {
                "type": ["string[]", "string[][]", "Resource", "TextPickerRangeContent[]",
                         "TextCascadePickerRangeContent[]"],
                "description": "选择器的数据选择列表。不可设置为空数组，若设置为空数组，则不显示；若动态变化为空数组，则保持当前正常值显示。说明：单列数据选择器使用string[]，Resource，TextPickerRangeContent[]类型。多列数据选择器使用string[][]类型。多列联动数据选择器使用TextCascadePickerRangeContent[]类型。Resource类型只支持strarray.json。range的类型及列数不可以动态修改。",
                "required": True
            },
            "selected": {
                "type": ["number", "number[]"],
                "description": "设置默认选中项在数组中的索引值。说明：单列数据选择器使用number类型。多列、多列联动数据选择器使用number[]类型。从API version 10开始，该参数支持$$双向绑定变量。",
                "default": 0,
                "required": False
            },
            "value": {
                "type": ["string", "string[]"],
                "description": "设置默认选中项的值，优先级低于selected。说明：只有显示文本列表时该值有效。显示图片或图片加文本的列表时，该值无效。单列数据选择器使用string类型。多列、多列联动数据选择器使用string[]类型。从API version 10开始，该参数支持$$双向绑定变量。",
                "required": False
            }
        }
    },
    "TextPickerRangeContent": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "icon": {
                "type": ["string", "Resource"],
                "description": "图片资源。",
                "required": True
            },
            "text": {
                "type": ["string", "Resource"],
                "description": "文本信息。",
                "required": False
            }
        }
    },
    "TextCascadePickerRangeContent": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "text": {
                "type": ["string", "Resource"],
                "description": "文本信息。",
                "required": True
            },
            "children": {
                "type": "TextCascadePickerRangeContent[]",
                "description": "联动数据。",
                "required": False
            }
        }
    },
    "DividerOptions": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "strokeWidth": {
                "type": ["Dimension"],
                "description": "分割线的线宽（默认单位vp），也可指定单位为px，不支持\"百分比\"类型。",
                "required": False
            },
            "startMargin": {
                "type": ["Dimension"],
                "description": "分割线与TextPicker侧边起始端的距离（默认单位vp），也可指定单位为px，不支持“百分比”类型。",
                "required": False
            },
            "endMargin": {
                "type": ["Dimension"],
                "description": "分割线与TextPicker侧边结束端的距离（默认单位vp），也可指定单位为px，不支持“百分比”类型。",
                "required": False
            },
            "color": {
                "type": ["ResourceColor"],
                "description": "分割线的颜色。",
                "required": False
            }
        }
    },
    "TextTimerOptions": {
        "type": "object",
        "description": "TextTimerOptions对象说明",
        "properties": {
            "isCountDown": {
                "type": "boolean",
                "description": "是否倒计时。",
                "default": False,
                "required": False
            },
            "count": {
                "type": "number",
                "description": "倒计时时间（isCountDown为True时生效），单位为毫秒。最长不超过86400000毫秒（24小时）。 0<count<86400000时，count值为倒计时初始值。否则，使用默认值为倒计时初始值。",
                "default": 60000,
                "required": False
            },
            "controller": {
                "type": "TextTimerController",
                "description": "TextTimer控制器。",
                "required": False
            }
        }
    },
    "TextTimerController": {
        "type": "object",
        "description": "TextTimer组件的控制器，用于控制文本计时器。一个TextTimer组件仅支持绑定一个控制器，组件创建完成后相关指令才能被调用。",
        "properties": {
            "textTimerController": {
                "type": "TextTimerController",
                "description": "TextTimerController的实例，用于控制TextTimer组件。",
                "required": True
            }
        }
    },
    "TextTimerConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。元服务API： 从API version 12开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "count": {
                "type": "number",
                "description": "倒计时时间（isCountDown为True时生效），单位为毫秒。最长不超过86400000毫秒（24小时）。 0<count<86400000时，count值为倒计时初始值。否则，使用默认值为倒计时初始值。",
                "default": 60000,
                "required": False
            },
            "isCountDown": {
                "type": "boolean",
                "description": "是否倒计时。",
                "default": False,
                "required": False
            },
            "started": {
                "type": "boolean",
                "description": "是否已经开始了倒计时。",
                "required": False
            },
            "elapsedTime": {
                "type": "number",
                "description": "计时器经过的时间，单位为设置格式的最小单位。",
                "required": False
            }
        }
    },
    "TimePickerOptions": {
        "type": "object",
        "description": "TimePickerOptions对象说明",
        "properties": {
            "selected": {
                "type": "Date",
                "description": "设置选中项的时间。",
                "default": "当前系统时间",
                "required": False
            },
            "format": {
                "type": "TimePickerFormat",
                "description": "指定需要显示的TimePicker的格式。",
                "default": "TimePickerFormat.HOUR_MINUTE",
                "required": False
            }
        }
    },
    "TimePickerFormat": {
        "type": "enum",
        "enum": ["HOUR_MINUTE", "HOUR_MINUTE_SECOND"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "HOUR_MINUTE": "按照小时和分显示。",
            "HOUR_MINUTE_SECOND": "按照小时、分钟和秒显示。"
        }
    },
    "TimePickerResult": {
        "type": "object",
        "description": "返回值为24小时制时间。",
        "properties": {
            "hour": {
                "type": "number",
                "description": "选中时间的时。",
                "required": True
            },
            "minute": {
                "type": "number",
                "description": "选中时间的分。",
                "required": True
            },
            "second": {
                "type": "number",
                "description": "选中时间的秒。",
                "required": True
            }
        }
    },
    "ToggleType": {
        "type": "enum",
        "enum": ["Checkbox", "Button", "Switch"],
        "description": "该枚举类定义了不同类型的切换控件样式。",
        "enumDescriptions": {
            "Checkbox": "提供单选框样式。从API version 11开始，Checkbox默认样式由圆角方形变为圆形。通用属性margin的默认值为：{top: '14px', right: '14px', bottom: '14px', left: '14px'}。默认尺寸为:{width:'20vp', height:'20vp'}。",
            "Button": "提供状态按钮样式，如果子组件有文本设置，则相应的文本内容会显示在按钮内部。默认尺寸为:高为28vp，宽无默认值。",
            "Switch": "提供开关样式。通用属性margin默认值为：{top: '6px', right: '14px', bottom: '6px', left: '14px'}。默认尺寸为:{width:'36vp', height:'20vp'}。"
        }
    },
    "SwitchStyle": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "pointRadius": {
                "type": ["number", "Resource"],
                "description": "设置Switch类型的圆形滑块半径。不支持百分比，设定值小于0时按照默认算法设置，设定值大于等于0时按照设定值设置。未设定此属性时，圆形滑块半径根据默认算法设置。默认算法：（组件高度（单位：vp） / 2） - （2vp * 组件高度（单位：vp） / 20vp）。",
                "required": False
            },
            "unselectedColor": {
                "type": "ResourceColor",
                "description": "设置Switch类型关闭状态的背景颜色。",
                "default": "0x337F7F7F",
                "required": False
            },
            "pointColor": {
                "type": "ResourceColor",
                "description": "设置Switch类型的圆形滑块颜色。",
                "default": "#FFFFFFFF",
                "required": False
            },
            "trackBorderRadius": {
                "type": ["number", "Resource"],
                "description": "设置Switch类型的滑轨的圆角。不支持百分比，设定值小于0时按照默认算法设置，设定值大于组件高度一半时按照组件高度一半设置，其他场合按照设定值设置。未设定此属性时，滑轨圆角根据默认算法设置。默认算法：组件高度（单位：vp） / 2。",
                "required": False
            }
        }
    },
    "ToggleConfiguration": {
        "type": "object",
        "description": "开发者需要自定义class实现ContentModifier接口。从API version 12开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "isOn": {
                "type": "boolean",
                "description": "开关是否打开。",
                "default": False,
                "required": True
            },
            "enabled": {
                "type": "boolean",
                "description": "是否可以切换状态。",
                "default": False,
                "required": True
            },
            "triggerChange": {
                "type": "Callback<boolean>",
                "description": "触发switch选中状态变化。",
                "required": True
            }
        }
    },
    "XComponentOptions": {
        "type": "object",
        "description": "定义XComponent的具体配置参数。",
        "properties": {
            "type": {
                "type": "XComponentType",
                "description": "用于指定XComponent组件类型。",
                "required": True
            },
            "controller": {
                "type": "XComponentcontroller",
                "description": "给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。",
                "required": True
            },
            "imageAIOptions": {
                "type": "ImageAIOptions",
                "description": "给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。",
                "required": False
            }
        }
    },
    "XComponentType": {
        "type": "enum",
        "enum": ["SURFACE", "COMPONENT", "TEXTURE", "NODE"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "SURFACE": "用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容单独展示到屏幕上。元服务API： 从API version 11开始，该接口支持在元服务中使用。",
            "COMPONENT": "XComponent将变成一个容器组件，并可在其中执行非UI逻辑以动态加载显示内容。说明：从API version 12 开始，该接口废弃，建议使用其他容器组件替代。元服务API： 从API version 11开始，该接口支持在元服务中使用。",
            "TEXTURE": "用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容会和XComponent组件的内容合成后展示到屏幕上。元服务API： 从API version 11开始，该接口支持在元服务中使用。",
            "NODE": "用于Native UI节点的占位容器，开发者通过Native API 开发的页面组件可展示在此容器区域内。说明：该类型不再演进，推荐使用ContentSlot占位组件管理Native API创建的组件。元服务API： 从API version 12开始，该接口支持在元服务中使用。"
        }
    },
    "XComponentController": {
        "type": "object",
        "description": "XComponent组件的控制器，可以将此对象绑定至XComponent组件，然后通过控制器来调用组件方法。",
        "properties": {}
    },
    "SurfaceRect": {
        "type": "object",
        "description": "用于描述XComponent持有Surface的显示区域。",
        "properties": {
            "offsetX": {
                "type": "number",
                "description": "Surface显示区域相对于XComponent组件左上角的x轴坐标，单位：px。",
                "default": 0,
                "required": False
            },
            "offsetY": {
                "type": "number",
                "description": "Surface显示区域相对于XComponent组件左上角的y轴坐标，单位：px。",
                "default": 0,
                "required": False
            },
            "surfaceWidth": {
                "type": "number",
                "description": "Surface显示区域的宽度，单位：px。",
                "required": True
            },
            "surfaceHeight": {
                "type": "number",
                "description": "Surface显示区域的高度，单位：px。",
                "required": True
            }
        }
    },
    "SurfaceRotationOptions": {
        "type": "object",
        "description": "用于描述XComponent持有Surface在屏幕旋转时是否锁定方向的设置。",
        "properties": {
            "lock": {
                "type": "boolean",
                "description": "Surface在屏幕旋转时是否锁定方向",
                "default": False,
                "required": False
            }
        }
    },
    # "NavPathStack": {
    #   "type": "object",
    #   "description": "Navigation路由栈，允许被继承。开发者可以在派生类中新增属性方法，也可以重写基类NavPathStack的方法。派生类对象可以替代基类NavPathStack对象使用。使用示例参见示例10。",
    #   "properties": {
    #     "pushPath": {
    #       "description": "将info指定的NavDestination页面信息入栈。",
    #       "properties": {
    #         "info": {
    #           "type": "NavPathInfo",
    #           "description": "NavDestination页面的信息。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         },
    #         "options": {
    #           "type": "NavigationOptions",
    #           "description": "页面栈操作选项。",
    #           "required": False
    #         }
    #       }
    #     },
    #     "pushPathByName": {
    #       "description": "将name指定的NavDestination页面信息入栈，传递的数据为param。",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "NavDestination页面名称。",
    #           "required": True
    #         },
    #         "param": {
    #           "type": "unknown",
    #           "description": "NavDestination页面详细参数。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         },
    #         "onPop": {
    #           "type": "Callback<PopInfo>",
    #           "description": "Callback回调，用于页面出栈时触发该回调处理返回结果。",
    #           "required": True
    #         }
    #       }
    #     },
    #     "pushDestination": {
    #       "description": "将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果。",
    #       "properties": {
    #         "info": {
    #           "type": "NavPathInfo",
    #           "description": "NavDestination页面的信息。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         },
    #         "options": {
    #           "type": "NavigationOptions",
    #           "description": "页面栈操作选项。",
    #           "required": False
    #         }
    #       },
    #       "returns": {
    #         "description": "异常返回结果。",
    #         "type": "Promise<void>"
    #       }
    #     },
    #     "pushDestinationByName": {
    #       "description": "将name指定的NavDestination页面信息入栈，传递的数据为param，使用Promise异步回调返回接口调用结果。",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "NavDestination页面名称。",
    #           "required": True
    #         },
    #         "param": {
    #           "type": "Object",
    #           "description": "NavDestination页面详细参数。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         },
    #         "onPop": {
    #           "type": "Callback<PopInfo>",
    #           "description": "Callback回调，用于页面出栈时处理返回结果。",
    #           "required": True
    #         }
    #       },
    #       "returns": {
    #         "description": "异常返回结果。",
    #         "type": "Promise<void>"
    #       }
    #     },
    #     "replacePath": {
    #       "description": "将当前页面栈栈顶退出，将info指定的NavDestination页面信息入栈。",
    #       "properties": {
    #         "info": {
    #           "type": "NavPathInfo",
    #           "description": "新栈顶页面参数信息。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         },
    #         "options": {
    #           "type": "NavigationOptions",
    #           "description": "页面栈操作选项。",
    #           "required": False
    #         }
    #       }
    #     },
    #     "replacePathByName": {
    #       "description": "将当前页面栈栈顶退出，将name指定的页面入栈。",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "NavDestination页面名称。",
    #           "required": True
    #         },
    #         "param": {
    #           "type": "Object",
    #           "description": "NavDestination页面详细参数。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         }
    #       }
    #     },
    #     "removeByIndexes": {
    #       "description": "将页面栈内索引值在indexes中的NavDestination页面删除。",
    #       "properties": {
    #         "indexes": {
    #           "type": "Array<number>",
    #           "description": "待删除NavDestination页面的索引值数组。",
    #           "required": True
    #         }
    #       },
    #       "returns": {
    #         "description": "返回删除的NavDestination页面数量。",
    #         "type": "number"
    #       }
    #     },
    #     "removeByName": {
    #       "description": "将页面栈内指定name的NavDestination页面删除。",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "删除的NavDestination页面的名字。",
    #           "required": True
    #         }
    #       },
    #       "returns": {
    #         "description": "返回删除的NavDestination页面数量。",
    #         "type": "number"
    #       }
    #     },
    #     "pop": {
    #       "description": "弹出路由栈栈顶元素。",
    #       "properties": {
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         },
    #         "result": {
    #           "type": "Object",
    #           "description": "页面自定义处理结果。不支持boolean类型。",
    #           "required": True
    #         }
    #       },
    #       "returns": {
    #         "description": "返回栈顶NavDestination页面的信息。当路由栈为空时返回undefined。",
    #         "type": ["NavPathInfo", "undefined"]
    #       }
    #     },
    #     "popToName": {
    #       "description": "回退路由栈到由栈底开始第一个名为name的NavDestination页面。",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "NavDestination页面名称。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         },
    #         "result": {
    #           "type": "Object",
    #           "description": "页面自定义处理结果。不支持boolean类型。",
    #           "required": True
    #         }
    #       },
    #       "returns": {
    #         "description": "如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。",
    #         "type": "number"
    #       }
    #     },
    #     "popToIndex": {
    #       "description": "回退路由栈到index指定的NavDestination页面。",
    #       "properties": {
    #         "index": {
    #           "type": "number",
    #           "description": "NavDestination页面的位置索引。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         },
    #         "result": {
    #           "type": "Object",
    #           "description": "页面自定义处理结果。不支持boolean类型。",
    #           "required": True
    #         }
    #       }
    #     },
    #     "moveToTop": {
    #       "description": "将由栈底开始第一个名为name的NavDestination页面移到栈顶。",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "NavDestination页面名称。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         }
    #       },
    #       "returns": {
    #         "description": "如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的当前索引，否则返回-1。",
    #         "type": "number"
    #       }
    #     },
    #     "moveIndexToTop": {
    #       "description": "将index指定的NavDestination页面移到栈顶。",
    #       "properties": {
    #         "index": {
    #           "type": "number",
    #           "description": "NavDestination页面的位置索引。",
    #           "required": True
    #         },
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         }
    #       }
    #     },
    #     "clear": {
    #       "description": "清除栈中所有页面。",
    #       "properties": {
    #         "animated": {
    #           "type": "boolean",
    #           "description": "是否支持转场动画。",
    #           "required": False,
    #           "default": True
    #         }
    #       }
    #     },
    #     "getAllPathName": {
    #       "description": "获取栈中所有NavDestination页面的名称。",
    #       "returns": {
    #         "description": "返回栈中所有NavDestination页面的名称。",
    #         "type": "Array<string>"
    #       }
    #     },
    #     "getParamByIndex": {
    #       "description": "获取index指定的NavDestination页面的参数信息。",
    #       "properties": {
    #         "index": {
    #           "type": "number",
    #           "description": "NavDestination页面的位置索引。",
    #           "required": True
    #         }
    #       },
    #       "returns": {
    #         "description": "返回对应NavDestination页面的参数信息。传入index无效时返回undefined。",
    #         "type": ["unknown", "undefined"]
    #       }
    #     },
    #     "getParamByName": {
    #       "description": "获取全部名为name的NavDestination页面的参数信息。",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "NavDestination页面名称。",
    #           "required": True
    #         }
    #       },
    #       "returns": {
    #         "description": "返回全部名为name的NavDestination页面的参数信息。",
    #         "type": "Array<unknown>"
    #       }
    #     },
    #     "getIndexByName": {
    #       "description": "获取全部名为name的NavDestination页面的位置索引。",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "NavDestination页面名称。",
    #           "required": True
    #         }
    #       },
    #       "returns": {
    #         "description": "返回全部名为name的NavDestination页面的位置索引。",
    #         "type": "Array<number>"
    #       }
    #     },
    #     "size": {
    #       "description": "获取栈大小。",
    #       "returns": {
    #         "description": "返回栈大小。",
    #         "type": "number"
    #       }
    #     },
    #     "disableAnimation": {
    #       "description": "关闭（True）或打开（False）当前Navigation中所有转场动画。",
    #       "properties": {
    #         "value": {
    #           "type": "boolean",
    #           "description": "是否关闭转场动画。",
    #           "required": False,
    #           "default": False
    #         }
    #       }
    #     },
    #     "getParent": {
    #       "description": "获取父NavPathStack。",
    #       "returns": {
    #         "description": "如果当前NavPathStack所属Navigation的外层有另外的一层Navigation，则能够获取到外层Navigation的NavPathStack。否则获取不到NavPathStack，返回null。",
    #         "type": ["NavPathStack", "null"]
    #       }
    #     },
    #     "setInterception": {
    #       "description": "设置Navigation页面跳转拦截回调。",
    #       "properties": {
    #         "interception": {
    #           "type": "NavigationInterception",
    #           "description": "设置Navigation跳转拦截对象。",
    #           "required": True
    #         }
    #       }
    #     }
    #   }
    # },
    # "NavPathInfo": {
    #   "type": "object",
    #   "description": "路由页面信息。",
    #   "properties": {
    #     "constructor": {
    #       "description": "构造函数",
    #       "properties": {
    #         "name": {
    #           "type": "string",
    #           "description": "NavDestination页面名称。",
    #           "required": True
    #         },
    #         "param": {
    #           "type": "unknown",
    #           "description": "NavDestination页面详细参数。",
    #           "required": False
    #         },
    #         "onPop": {
    #           "type": "Callback<PopInfo>",
    #           "description": "NavDestination页面触发pop时返回的回调。",
    #           "required": False
    #         }
    #       }
    #     }
    #   }
    # },
    # "PatternLockController": {
    #   "type": "object",
    #   "description": "PatternLock组件的控制器，可以通过它进行组件状态重置。",
    #   "properties": {
    #     "reset": {
    #       "description": "重置组件状态。",
    #       "properties": {},
    #     },
    #     "setChallengeResult": {
    #       "description": "用于设置图案密码正确或错误状态。",
    #       "properties": {
    #         "result": {
    #           "type": "PatternLockChallengeResult",
    #           "description": "图案密码状态。",
    #           "required": True
    #         }
    #       }
    #     }
    #   }
    # },
    # "RichEditorController": {
    #     "type": "object",
    #     "description": "RichEditor组件的控制器，继承自RichEditorBaseController。",
    #     "properties": {
    #       "getCaretOffset": {
    #         "description": "返回当前光标所在位置。",
    #         "returns": {
    #           "description": "当前光标所在位置。",
    #           "type": "number"
    #         }
    #       },
    #       "setCaretOffset": {
    #         "description": "设置光标位置。",
    #         "properties": {
    #           "offset": {
    #             "type": "number",
    #             "description": "光标偏移位置。超出文本范围时，设置失败。",
    #             "required": True
    #           }
    #         },
    #         "returns": {
    #           "description": "光标是否设置成功。",
    #           "type": "boolean"
    #         }
    #       },
    #       "addTextSpan": {
    #         "description": "添加文本内容，如果组件光标闪烁，插入后光标位置更新为新插入文本的后面。",
    #         "properties": {
    #           "value": {
    #             "type": "string",
    #             "description": "文本内容。",
    #             "required": True
    #           },
    #           "options": {
    #             "type": "RichEditorTextSpanOptions",
    #             "description": "文本选项。",
    #             "required": False
    #           }
    #         },
    #         "returns": {
    #           "description": "添加完成的TextSpan所在的位置。",
    #           "type": "number"
    #         }
    #       },
    #       "addImageSpan": {
    #         "description": "添加图片内容，如果组件光标闪烁，插入后光标位置更新为新插入图片的后面。",
    #         "properties": {
    #           "value": {
    #             "type": "PixelMap|ResourceStr",
    #             "description": "图片内容。",
    #             "required": True
    #           },
    #           "options": {
    #             "type": "RichEditorImageSpanOptions",
    #             "description": "图片选项。",
    #             "required": False
    #           }
    #         },
    #         "returns": {
    #           "description": "添加完成的ImageSpan所在的位置。",
    #           "type": "number"
    #         }
    #       },
    #       "addBuilderSpan": {
    #         "description": "RichEditor组件添加占位Span，占位Span调用系统的measure方法计算真实的长宽和位置。可通过RichEditorBuilderSpanOptions设置此builder在RichEditor中的index（一个文字为一个单位）。此占位Span不可获焦，支持拖拽，支持部分通用属性，占位、删除等能力等同于ImageSpan，长度视为一个文字。不支持通过bindSelectionMenu设置自定义菜单。不支持通过getSpans，getSelection，onSelect，aboutToDelete获取builderSpan信息。不支持通过updateSpanStyle，updateParagraphStyle等方式更新builder。对此builder节点进行复制或粘贴不生效。builder的布局约束由RichEditor传入，如果builder里最外层组件不设置大小，则会用RichEditor的大小作为maxSize。builder的手势相关事件机制与通用手势事件相同，如果builder中未设置透传，则仅有builder中的子组件响应。如果组件光标闪烁，插入后光标位置更新为新插入builder的后面。通用属性仅支持size、padding、margin、aspectRatio、borderStyle、borderWidth、borderColor、borderRadius、backgroundColor、backgroundBlurStyle、opacity、blur、backdropBlur、shadow、grayscale、brightness、saturate、contrast、invert、sepia、hueRotate、colorBlend、linearGradientBlur、clip、mask、foregroundBlurStyle、accessibilityGroup、accessibilityText、accessibilityDescription、accessibilityLevel、sphericalEffect、lightUpEffect、pixelStretchEffect。",
    #         "properties": {
    #           "value": {
    #             "type": "CustomBuilder",
    #             "description": "自定义组件。",
    #             "required": True
    #           },
    #           "options": {
    #             "type": "RichEditorBuilderSpanOptions",
    #             "description": "builder选项。",
    #             "required": False
    #           }
    #         },
    #         "returns": {
    #           "description": "添加完成的builderSpan所在的位置。",
    #           "type": "number"
    #         }
    #       },
    #       "addSymbolSpan": {
    #         "description": "在Richeditor中添加SymbolSpan，如果组件光标闪烁，插入后光标位置更新为新插入Symbol的后面。暂不支持手势、复制、拖拽处理。",
    #         "properties": {
    #           "value": {
    #             "type": "Resource",
    #             "description": "组件内容。",
    #             "required": True
    #           },
    #           "options": {
    #             "type": "RichEditorSymbolSpanOptions",
    #             "description": "组件选项。",
    #             "required": False
    #           }
    #         },
    #         "returns": {
    #           "description": "添加完成的SymbolSpan所在的位置。",
    #           "type": "number"
    #         }
    #       },
    #       "getTypingStyle": {
    #         "description": "获得用户预设的样式。",
    #         "returns": {
    #           "description": "用户预设样式。",
    #           "type": "RichEditorTextStyle"
    #         }
    #       },
    #       "setTypingStyle": {
    #         "description": "设置用户预设的样式。",
    #         "properties": {
    #           "value": {
    #             "type": "RichEditorTextStyle",
    #             "description": "预设样式。",
    #             "required": True
    #           }
    #         }
    #       },
    #       "updateSpanStyle": {
    #         "description": "更新文本、图片或SymbolSpan样式。若只更新了一个Span的部分内容，则会根据更新部分、未更新部分将该Span拆分为多个Span。使用该接口更新文本、图片或SymbolSpan样式时默认不会关闭自定义文本选择菜单。",
    #         "properties": {
    #           "value": {
    #             "type": ["RichEditorUpdateTextSpanStyleOptions" , "RichEditorUpdateImageSpanStyleOptions","RichEditorUpdateSymbolSpanStyleOptions"],
    #             "description": "文本、图片或SymbolSpan的样式选项信息。",
    #             "required": True
    #           }
    #         }
    #       },
    #       "updateParagraphStyle": {
    #         "description": "更新段落的样式。",
    #         "properties": {
    #           "value": {
    #             "type": "RichEditorParagraphStyleOptions",
    #             "description": "段落的样式选项信息。",
    #             "required": True
    #           }
    #         }
    #       },
    #       "getSpans": {
    #         "description": "获取span信息。",
    #         "properties": {
    #           "value": {
    #             "type": "RichEditorRange",
    #             "description": "需要获取span范围。",
    #             "required": False
    #           }
    #         },
    #         "returns": {
    #           "description": "文本和图片Span信息。",
    #           "type": "Array<RichEditorTextSpanResult | RichEditorImageSpanResult>"
    #         }
    #       },
    #       "deleteSpans": {
    #         "description": "删除指定范围内的文本和图片。",
    #         "properties": {
    #           "value": {
    #             "type": "RichEditorRange",
    #             "description": "删除范围。省略时，删除所有文本和图片。",
    #             "required": False
    #           }
    #         }
    #       },
    #       "getParagraphs": {
    #         "description": "获得指定返回的段落。",
    #         "properties": {
    #           "value": {
    #             "type": "RichEditorRange",
    #             "description": "需要获取段落的范围。",
    #             "required": False
    #           }
    #         },
    #         "returns": {
    #           "description": "选中段落的信息。",
    #           "type": "Array<RichEditorParagraphResult>"
    #         }
    #       },
    #       "closeSelectionMenu": {
    #         "description": "关闭自定义选择菜单或系统默认选择菜单。"
    #       },
    #       "setSelection": {
    #         "description": "支持设置文本选中，选中部分背板高亮。selectionStart和selectionEnd均为-1时表示全选。未获焦时调用该接口不产生选中效果。从API version 12开始，在2in1设备中，无论options取何值，调用setSelection接口都不会弹出菜单，此外，如果组件中已经存在菜单，调用setSelection接口会关闭菜单。在非2in1设备中，options取值为MenuPolicy.DEFAULT时，遵循以下规则：组件内有手柄菜单时，接口调用后不关闭菜单，并且调整菜单位置。组件内有不带手柄的菜单时，接口调用后不关闭菜单，并且菜单位置不变。组件内无菜单时，接口调用后也无菜单显示。使用示例。",
    #         "properties": {
    #           "selectionStart": {
    #             "type": "number",
    #             "description": "选中开始位置。",
    #             "required": True
    #           },
    #           "selectionEnd": {
    #             "type": "number",
    #             "description": "选中结束位置。",
    #             "required": True
    #           },
    #           "options": {
    #             "type": "SelectionOptions",
    #             "description": "选择项配置。",
    #             "required": False
    #           }
    #         }
    #       },
    #       "getSelection": {
    #         "description": "获取选中内容。如果未选中内容，返回光标所在span信息。",
    #         "returns": {
    #           "description": "选中内容信息。",
    #           "type": "RichEditorSelection"
    #         }
    #       },
    #       "fromStyledString": {
    #         "description": "将属性字符串转换成span信息。",
    #         "properties": {
    #           "value": {
    #             "type": "StyledString",
    #             "description": "转换前的属性字符串。",
    #             "required": True
    #           }
    #         },
    #         "returns": {
    #           "description": "文本和图片Span信息。",
    #           "type": "Array<RichEditorSpan>"
    #         }
    #       },
    #       "toStyledString": {
    #         "description": "将给定范围的组件内容转换成属性字符串。",
    #         "properties": {
    #           "styledString": {
    #             "type": "RichEditorRange",
    #             "description": "需要获取的范围。",
    #             "required": True
    #           }
    #         },
    #         "returns": {
    #           "description": "转换后的属性字符串",
    #           "type": "StyledString"
    #         }
    #       }
    #     }
    #   },
    # "RichEditorBaseController": {
    #     "type": "object",
    #     "description": "RichEditor组件控制器基类。",
    #     "properties": {
    #       "getCaretOffset": {
    #         "description": "返回当前光标所在位置。",
    #         "returns": {
    #           "description": "当前光标所在位置。",
    #           "type": "number"
    #         }
    #       },
    #       "setCaretOffset": {
    #         "description": "设置光标位置。",
    #         "properties": {
    #           "offset": {
    #             "type": "number",
    #             "description": "光标偏移位置。超出所有内容范围时，设置失败。",
    #             "required": True
    #           }
    #         },
    #         "returns": {
    #           "description": "光标是否设置成功。",
    #           "type": "boolean"
    #         }
    #       },
    #       "closeSelectionMenu": {
    #         "description": "关闭自定义选择菜单或系统默认选择菜单。"
    #       },
    #       "getTypingStyle": {
    #         "description": "获得用户预设的样式。",
    #         "returns": {
    #           "description": "用户预设样式。",
    #           "type": "RichEditorTextStyle"
    #         }
    #       },
    #       "setTypingStyle": {
    #         "description": "设置用户预设的样式。",
    #         "properties": {
    #           "value": {
    #             "type": "RichEditorTextStyle",
    #             "description": "预设样式。",
    #             "required": True
    #           }
    #         }
    #       },
    #       "setSelection": {
    #         "description": "支持设置组件内的内容选中，选中部分背板高亮。selectionStart和selectionEnd均为-1时表示全选。未获焦时调用该接口不产生选中效果。",
    #         "properties": {
    #           "selectionStart": {
    #             "type": "number",
    #             "description": "选中开始位置。",
    #             "required": True
    #           },
    #           "selectionEnd": {
    #             "type": "number",
    #             "description": "选中结束位置。",
    #             "required": True
    #           },
    #           "options": {
    #             "type": "SelectionOptions",
    #             "description": "选择项配置。",
    #             "required": False
    #           }
    #         }
    #       },
    #       "isEditing": {
    #         "description": "获取当前富文本的编辑状态。",
    #         "returns": {
    #           "description": "True为编辑态，false为非编辑态。",
    #           "type": "boolean"
    #         }
    #       },
    #       "stopEditing": {
    #         "description": "退出编辑态。"
    #       },
    #       "getLayoutManager": {
    #         "description": "获取布局管理器对象。",
    #         "returns": {
    #           "description": "布局管理器对象。",
    #           "type": "LayoutManager"
    #         }
    #       },
    #       "getPreviewText": {
    #         "description": "获取预上屏信息。",
    #         "returns": {
    #           "description": "预上屏信息。",
    #           "type": "PreviewText"
    #         }
    #       }
    #     }
    #   },
    #   "RichEditorStyledStringController": {
    #     "type": "object",
    #     "description": "使用属性字符串构建的RichEditor组件的控制器，继承自RichEditorBaseController。",
    #     "properties": {
    #       "getSelection": {
    #         "description": "获取当前富文本当前的选中区域范围。",
    #         "returns": {
    #           "type": "RichEditorRange",
    #           "description": "选中区域范围。"
    #         }
    #       },
    #       "setStyledString": {
    #         "description": "设置富文本组件显示的属性字符串。",
    #         "properties": {
    #           "styledString": {
    #             "type": ["StyledString", "MutableStyledString"],
    #             "description": "属性字符串。",
    #             "required": True
    #           }
    #         }
    #       },
    #       "getStyledString": {
    #         "description": "获取富文本组件显示的属性字符串。",
    #         "returns": {
    #           "type": "MutableStyledString",
    #           "description": "富文本组件显示的属性字符串"
    #         }
    #       },
    #       "onContentChanged": {
    #         "description": "注册文本内容变化回调，该回调会在后端程序导致文本内容变更时触发",
    #         "properties": {
    #           "listener": {
    #             "type": "StyledStringChangedListener",
    #             "description": "文本内容变化回调监听器。",
    #             "required": True
    #           }
    #         }
    #       }
    #     }
    #   },
    #   "SearchController": {
    #     "type": "object",
    #     "description": "Search组件的控制器继承自TextContentControllerBase。",
    #     "properties": {
    #       "constructor": {
    #         "description": "SearchController的构造函数。",
    #         "properties": {}
    #       },
    #       "caretPosition": {
    #         "description": "设置输入光标的位置。",
    #         "properties": {
    #           "value": {
    #             "type": "number",
    #             "description": "从字符串开始到光标所在位置的长度。",
    #             "required": True
    #           }
    #         }
    #       },
    #       "stopEditing": {
    #         "description": "退出编辑态。",
    #         "properties": {}
    #       },
    #       "setTextSelection": {
    #         "description": "组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。",
    #         "properties": {
    #           "selectionStart": {
    #             "type": "number",
    #             "description": "文本选择区域起始位置，文本框中文字的起始位置为0。当selectionStart小于0时、按照0处理；当selectionStart大于文字最大长度时、按照文字最大长度处理。",
    #             "required": True
    #           },
    #           "selectionEnd": {
    #             "type": "number",
    #             "description": "文本选择区域结束位置。当selectionEnd小于0时、按照0处理；当selectionEnd大于文字最大长度时、按照文字最大长度处理。",
    #             "required": True
    #           },
    #           "options": {
    #             "type": "SelectionOptions",
    #             "description": "选中文字时的配置。默认值：MenuPolicy.DEFAULT。如果selectionStart或selectionEnd被赋值为undefined时，当作0处理。如果selectionMenuHidden被赋值为True或设备为2in1时，即使options被赋值为MenuPolicy.SHOW，调用setTextSelection也不弹出菜单。如果选中的文本含有emoji表情时，表情的起始位置包含在设置的文本选中区域内就会被选中。",
    #             "required": False,
    #             "default":"MenuPolicy.DEFAULT"
    #           }
    #         }
    #       }
    #     }
    #   },
    #   "BaseSpan": {
    #     "type": "object",
    #     "description": "定义BaseSpan基础类，包含Span的通用属性。",
    #     "properties": {
    #       "textBackgroundStyle": {
    #         "description": "设置背景样式。作为ContainerSpan的子组件时可以继承它的此属性值，优先使用其自身的此属性。",
    #         "properties": {
    #           "style": {
    #             "type": "TextBackgroundStyle",
    #             "description": "背景样式。",
    #             "required": True,
    #             "default": {
    #               "color": "Color.Transparent",
    #               "radius": 0
    #             }
    #           }
    #         },
    #         "returns": {
    #           "description": "返回当前Span的属性。",
    #           "type": "T"
    #         }
    #       },
    #       "baselineOffset": {
    #         "description": "设置Span基线的偏移量。此属性与父组件的baselineOffset是共存的。",
    #         "properties": {
    #           "value": {
    #             "type": "LengthMetrics",
    #             "description": "设置Span基线的偏移量，设置该值为百分比时，按默认值显示。正数内容向上偏移，负数向下偏移。在ImageSpan中，设置为非0时会导致设置verticalAlign失效。",
    #             "required": True,
    #             "default": 0
    #           }
    #         },
    #         "returns": {
    #           "description": "返回当前Span的属性。",
    #           "type": "T"
    #         }
    #       }
    #     }
    #   },
    "BadgePosition": {
        "type": "enum",
        "enum": ["RightTop", "Right", "Left"],
        "description": "卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。元服务API： 从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "RightTop": "圆点显示在右上角。",
            "Right": "圆点显示在右侧纵向居中。",
            "Left": "圆点显示在左侧纵向居中。"
        }
    },
    "ScrollState": {
        "type": "enum",
        "enum": ["Idle", "Scroll", "Fling"],
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "Idle": "空闲状态。滚动状态回归空闲时触发，控制器提供的无动画方法控制滚动时触发。",
            "Scroll": "滚动状态。手指拖动List，拖动滚动条和滚动鼠标滚轮时触发。",
            "Fling": "惯性滚动状态。动画控制的滚动都会触发。包括快速划动松手后的惯性滚动，划动到边缘回弹的滚动，快速拖动内置滚动条松手后的惯性滚动，使用滚动控制器提供的带动画的方法控制的滚动。"
        }
    },
    "ListItemGroupArea": {
        "type": "enum",
        "enum": ["NONE", "IN_LIST_ITEM_AREA", "IN_HEADER_AREA", "IN_FOOTER_AREA"],
        "description": "该枚举类用于描述当前页面可视边的位置",
        "enumDescriptions": {
            "NONE": "当前页面可视边处于none位置。例如，ListItemGroup中既没有header、footer，也没有ListItem。",
            "IN_LIST_ITEM_AREA": "当前页面可视边处于ListItem位置。",
            "IN_HEADER_AREA": "当前页面可视边处于header位置。",
            "IN_FOOTER_AREA": "当前页面可视边处于footer位置。"
        }
    },
    "Sticky": {
        "type": "enum",
        "enum": ["None", "Normal", "Opacity"],
        "description": "从API version9开始废弃不再使用，推荐使用List组件stickyStyle枚举。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "None": "无吸顶效果。",
            "Normal": "当前item吸顶。",
            "Opacity": "当前item吸顶显示透明度变化效果。"
        }
    },
    "EditMode": {
        "type": "enum",
        "enum": ["None", "Deletable", "Movable"],
        "description": "从API version9开始废弃不再使用，无替代接口。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "None": "编辑操作不限制。",
            "Deletable": "可删除。",
            "Movable": "可移动。"
        }
    },
    "ListItemStyle": {
        "type": "enum",
        "enum": ["NONE", "CARD"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "NONE": "无样式。",
            "CARD": "显示默认卡片样式。"
        }
    },
    "SwipeActionState": {
        "type": "enum",
        "enum": ["COLLAPSED", "EXPANDED", "ACTIONING"],
        "description": "该枚举类用于描述ListItem在滑动操作时的状态",
        "enumDescriptions": {
            "COLLAPSED": "收起状态，当ListItem向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列方向为“水平”时）时操作项处于隐藏状态。",
            "EXPANDED": "展开状态，当ListItem向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列方向为“水平”时）时操作项处于显示状态。",
            "ACTIONING": "长距离状态，当ListItem进入长距删除区后删除ListItem的状态。滑动后松手的位置超过或等于设置的距离阈值，并且设置的距离阈值有效时才能进入该状态。"
        }
    },
    "ListItemGroupStyle": {
        "type": "enum",
        "enum": ["NONE", "CARD"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "NONE": "无样式。",
            "CARD": "显示默认卡片样式。"
        }
    },
    "NavigationType": {
        "type": "enum",
        "enum": ["Push", "Replace", "Back"],
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "Push": "跳转到应用内的指定页面。",
            "Replace": "用应用内的某个页面替换当前页面，并销毁被替换的页面。",
            "Back": "返回到指定的页面。指定的页面不存在栈中时不响应。未传入指定的页面时返回上一页。"
        }
    },
    "RefreshStatus": {
        "type": "enum",
        "enum": ["Inactive", "Drag", "OverDrag", "Refresh", "Done"],
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "Inactive": "默认未下拉状态。",
            "Drag": "下拉中，下拉距离小于刷新距离。",
            "OverDrag": "下拉中，下拉距离超过刷新距离。",
            "Refresh": "下拉结束，回弹至刷新距离，进入刷新中状态。",
            "Done": "刷新结束，返回初始状态（顶部）。"
        }
    },
    "GridItemStyle": {
        "type": "enum",
        "enum": ["NONE", "PLAIN"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "NONE": "无样式。",
            "PLAIN": "显示Hover、Press态样式。"
        }
    },
    "ListItemAlign": {
        "type": "enum",
        "enum": ["Start", "Center", "End"],
        "description": "ListItem在List中，交叉轴方向的对齐方式",
        "enumDescriptions": {
            "Start": "ListItem在List中，交叉轴方向首部对齐",
            "Center": "ListItem在List中，交叉轴方向居中对齐",
            "End": "ListItem在List中，交叉轴方向尾部对齐"
        }
    },
    "StickyStyle": {
        "type": "enum",
        "enum": ["None", "Header", "Footer"],
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "None": "ListItemGroup的header不吸顶，footer不吸底。",
            "Header": "ListItemGroup的header吸顶，footer不吸底。",
            "Footer": "ListItemGroup的footer吸底，header不吸顶。"
        }
    },
    "ScrollSnapAlign": {
        "type": "enum",
        "enum": ["NONE", "START", "CENTER", "END"],
        "description": "设置列表项滚动结束对齐效果。只支持item等高场景限位，不等高场景可能存在不准确的情况。",
        "enumDescriptions": {
            "NONE": "默认无项目滚动对齐效果。",
            "START": "视图中的第一项将在列表的开头对齐。当列表位移至末端，需要将末端的item完整显示，可能出现开头不对齐的情况。",
            "CENTER": "视图中的中间项将在列表中心对齐。顶端和末尾的item都可以在列表中心对齐，列表显示可能露出空白，第一个或最后一个item会对齐到中间位置。",
            "END": "视图中的最后一项将在列表末尾对齐。当列表位移至顶端，需要将顶端的item完整显示，可能出现末尾不对齐的情况。"
        }
    },
    "BreakpointsReference": {
        "type": "enum",
        "enum": ["WindowSize", "ComponentSize"],
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "WindowSize": "以窗口为参照。",
            "ComponentSize": "以容器为参照。"
        }
    },
    "GridRowDirection": {
        "type": "enum",
        "enum": ["Row", "RowReverse"],
        "description": "从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "Row": "栅格元素按照行方向排列。",
            "RowReverse": "栅格元素按照逆序行方向排列。"
        }
    },
    "GridDirection": {
        "type": "enum",
        "enum": ["Row", "Column", "RowReverse", "ColumnReverse"],
        "description": "元服务API： 从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "Row": "主轴布局方向沿水平方向布局，即自左往右先填满一行，再去填下一行。",
            "Column": "主轴布局方向沿垂直方向布局，即自上往下先填满一列，再去填下一列。",
            "RowReverse": "主轴布局方向沿水平方向反向布局，即自右往左先填满一行，再去填下一行。",
            "ColumnReverse": "主轴布局方向沿垂直方向反向布局，即自下往上先填满一列，再去填下一列。"
        }
    },
    "ScrollAlign": {
        "type": "enum",
        "enum": ["START", "CENTER", "END", "AUTO"],
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "START": "首部对齐。指定item首部与List首部对齐。",
            "CENTER": "居中对齐。指定item主轴方向居中对齐于List。",
            "END": "尾部对齐。指定item尾部与List尾部对齐。",
            "AUTO": "自动对齐。若指定item完全处于显示区，不做调整。否则依照滑动距离最短的原则，将指定item首部对齐或尾部对齐于List,使指定item完全处于显示区。"
        }
    },
    "ScrollDirection": {
        "type": "enum",
        "enum": ["Horizontal", "Vertical", "None", "Free"],
        "description": "ScrollDirection枚举说明",
        "enumDescriptions": {
            "Horizontal": "仅支持水平方向滚动。",
            "Vertical": "仅支持竖直方向滚动。",
            "None": "不可滚动。",
            "Free": "支持竖直或水平方向滚动"
        }
    },
    "BadgeParam": {
        "type": "object",
        "description": "包含创建Badge组件的基础参数。卡片能力：从API version 9开始，该接口支持在ArkTS卡片中使用。元服务API：从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "position": {
                "type": ["BadgePosition", "Position10+"],
                "description": "设置提示点显示位置。说明：Position作为入参，不支持设置百分比；设置为非法值时，默认（0,0）处理。",
                "default": "BadgePosition.RightTop",
                "required": False
            },
            "style": {
                "type": "BadgeStyle",
                "description": "Badge组件可设置样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。",
                "required": True
            }
        }
    },
    "BadgeParamWithNumber": {
        "type": "object",
        "description": "BadgeParamWithNumber继承自BadgeParam，具有BadgeParam的全部属性。从API version 9开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "count": {
                "type": "number",
                "description": "设置提醒消息数。小于等于0时不显示信息标记。取值范围：[-2147483648,2147483647]，超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。",
                "required": True
            },
            "maxCount": {
                "type": "number",
                "description": "最大消息数，超过最大消息时仅显示maxCount+。取值范围：[-2147483648,2147483647]，超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。",
                "default": 99,
                "required": False
            }
        }
    },
    "BadgeParamWithString": {
        "type": "object",
        "description": "BadgeParamWithString继承自BadgeParam，具有BadgeParam的全部属性。卡片能力：从API version 9开始，该接口支持在ArkTS卡片中使用。元服务API：从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "value": {
                "type": "string",
                "description": "提示内容的文本字符串。",
                "required": True
            }
        }
    },
    "BadgeStyle": {
        "type": "object",
        "description": "BadgeStyle对象说明。卡片能力：从API version 9开始，该接口支持在ArkTS卡片中使用。元服务API：从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "color": {
                "type": "ResourceColor",
                "description": "文本颜色。",
                "default": "Color.White",
                "required": False
            },
            "fontSize": {
                "type": ["number", "string"],
                "description": "文本大小。不支持设置百分比。",
                "default": 10,
                "required": False
            },
            "badgeSize": {
                "type": ["number", "string"],
                "description": "Badge的大小。不支持设置百分比。当设置为非法值时，按照默认值处理。",
                "default": 16,
                "required": False
            },
            "badgeColor": {
                "type": "ResourceColor",
                "description": "Badge的颜色。",
                "default": "Color.Red",
                "required": False
            },
            "fontWeight": {
                "type": ["number", "FontWeight", "string"],
                "description": "设置文本的字体粗细。不支持设置百分比。",
                "default": "FontWeight.Normal",
                "required": False
            },
            "borderColor": {
                "type": "ResourceColor",
                "description": "底板描边颜色。",
                "default": "Color.Red",
                "required": False
            },
            "borderWidth": {
                "type": "Length",
                "description": "底板描边粗细。不支持设置百分比。",
                "default": 1,
                "required": False
            }
        }
    },
    "ColumnSplitDividerStyle": {
        "type": "object",
        "description": "与RowSplit相同，ColumnSplit的分割线可以改变上下两边子组件的高度，子组件可改变高度的范围取决于子组件的最大最小高度。支持clip、margin等通用属性，clip不设置的时候默认值为True。",
        "properties": {
            "startMargin": {
                "type": "Dimension",
                "description": "分割线与其上方子组件的距离。",
                "default": 0,
                "required": False
            },
            "endMargin": {
                "type": "Dimension",
                "description": "分割线与其下方子组件的距离。",
                "default": 0,
                "required": False
            }
        }
    },
    "FlexOptions": {
        "type": "object",
        "description": "FlexOptions对象说明",
        "properties": {
            "direction": {
                "type": "FlexDirection",
                "description": "子组件在Flex容器上排列的方向，即主轴的方向。",
                "default": "FlexDirection.Row",
                "required": False
            },
            "wrap": {
                "type": "FlexWrap",
                "description": "Flex容器是单行/列还是多行/列排列。在多行布局时，通过交叉轴方向，确认新行堆叠方向。",
                "default": "FlexWrap.NoWrap",
                "required": False
            },
            "justifyContent": {
                "type": "FlexAlign",
                "description": "所有子组件在Flex容器主轴上的对齐格式。",
                "default": "FlexAlign.Start",
                "required": False
            },
            "alignItems": {
                "type": "ItemAlign",
                "description": "所有子组件在Flex容器交叉轴上的对齐格式。",
                "default": "ItemAlign.Start",
                "required": False
            },
            "alignContent": {
                "type": "FlexAlign",
                "description": "交叉轴中有额外的空间时，多行内容的对齐方式。仅在wrap为Wrap或WrapReverse下生效。",
                "default": "FlexAlign.Start",
                "required": False
            },
            "space": {
                "type": "FlexSpaceOptions",
                "description": "所有子组件在Flex容器主轴或交叉轴的space。可选值为大于等于0的数字，或者可以转换为数字的字符串。space为负数、百分比或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。",
                "default": "{main:LengthMetrics.px(0), cross:LengthMetrics.px(0)}",
                "required": False
            }
        }
    },
    "HoverEventParam": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "foldStatus": {
                "type": "FoldStatus",
                "description": "当前设备的折叠状态。",
                "required": True
            },
            "isHoverMode": {
                "type": "boolean",
                "description": "当前是否悬停模式。",
                "required": True
            },
            "appRotation": {
                "type": "AppRotation",
                "description": "当前应用方向。",
                "required": True
            },
            "windowStatusType": {
                "type": "WindowStatusType",
                "description": "窗口模式枚举。",
                "required": True
            }
        }
    },
    "GridColOptions": {
        "type": "object",
        "description": "栅格子组件的配置选项，包括占用列数、偏移列数和序号。",
        "properties": {
            "span": {
                "type": ["number", "GridColColumnOption"],
                "description": "栅格子组件占用栅格容器组件的列数。span为0表示该元素不参与布局计算，即不会被渲染。",
                "default": 1,
                "required": False
            },
            "offset": {
                "type": ["number", "GridColColumnOption"],
                "description": "栅格子组件相对于原本位置偏移的列数。",
                "default": 0,
                "required": False
            },
            "order": {
                "type": ["number", "GridColColumnOption"],
                "description": "元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。",
                "default": 0,
                "required": False
            }
        }
    },
    "GridColColumnOption": {
        "type": "object",
        "description": "用于自定义指定在不同宽度设备类型上，栅格子组件占据的栅格数量单位。",
        "properties": {
            "xs": {
                "type": "number",
                "description": "在栅格大小为xs的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "sm": {
                "type": "number",
                "description": "在栅格大小为sm的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "md": {
                "type": "number",
                "description": "在栅格大小为md的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "lg": {
                "type": "number",
                "description": "在栅格大小为lg的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "xl": {
                "type": "number",
                "description": "在栅格大小为xl的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "xxl": {
                "type": "number",
                "description": "在栅格大小为xxl的设备上，栅格容器组件的栅格列数。",
                "required": False
            }
        }
    },
    "GridRowOptions": {
        "type": "object",
        "description": "GridRowOptions对象说明",
        "properties": {
            "columns": {
                "type": ["number", "GridRowColumnOption"],
                "description": "设置布局列数。",
                "default": 12,
                "required": False
            },
            "gutter": {
                "type": ["Length", "GutterOption"],
                "description": "栅格布局间距。",
                "default": 0,
                "required": False
            },
            "breakpoints": {
                "type": "BreakPoints",
                "description": "设置断点值的断点数列以及基于窗口或容器尺寸的相应参照。",
                "default": {
                    "value": ["320vp", "600vp", "840vp"],
                    "reference": "BreakpointsReference.WindowSize"
                },
                "required": False
            },
            "direction": {
                "type": "GridRowDirection",
                "description": "栅格布局排列方向。",
                "default": "GridRowDirection.Row",
                "required": False
            }
        }
    },
    "GutterOption": {
        "type": "object",
        "description": "栅格布局间距类型，用于描述栅格子组件不同方向的间距。",
        "properties": {
            "x": {
                "type": ["Length", "GridRowSizeOption"],
                "description": "栅格子组件水平方向间距。",
                "required": False
            },
            "y": {
                "type": ["Length", "GridRowSizeOption"],
                "description": "栅格子组件竖直方向间距。",
                "required": False
            }
        }
    },
    "GridRowColumnOption": {
        "type": "object",
        "description": "栅格在不同宽度设备类型下，栅格列数。",
        "properties": {
            "xs": {
                "type": "number",
                "description": "在栅格大小为xs的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "sm": {
                "type": "number",
                "description": "在栅格大小为sm的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "md": {
                "type": "number",
                "description": "在栅格大小为md的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "lg": {
                "type": "number",
                "description": "在栅格大小为lg的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "xl": {
                "type": "number",
                "description": "在栅格大小为xl的设备上，栅格容器组件的栅格列数。",
                "required": False
            },
            "xxl": {
                "type": "number",
                "description": "在栅格大小为xxl的设备上，栅格容器组件的栅格列数。",
                "required": False
            }
        }
    },
    "GridRowSizeOption": {
        "type": "object",
        "description": "栅格在不同宽度设备类型下，gutter的大小。",
        "properties": {
            "xs": {
                "type": "Length",
                "description": "在最小宽度类型设备上，栅格子组件的间距。",
                "required": False
            },
            "sm": {
                "type": "Length",
                "description": "在小宽度类型设备上，栅格子组件的间距。",
                "required": False
            },
            "md": {
                "type": "Length",
                "description": "在中等宽度类型设备上，栅格子组件的间距。",
                "required": False
            },
            "lg": {
                "type": "Length",
                "description": "在大宽度类型设备上，栅格子组件的间距。",
                "required": False
            },
            "xl": {
                "type": "Length",
                "description": "在特大宽度类型设备上，栅格子组件的间距。",
                "required": False
            },
            "xxl": {
                "type": "Length",
                "description": "在超大宽度类型设备上，栅格子组件的间距。",
                "required": False
            }
        }
    },
    "BreakPoints": {
        "type": "object",
        "description": "设置栅格容器组件的断点。",
        "properties": {
            "value": {
                "type": "Array<string>",
                "description": "设置断点位置的单调递增数组。",
                "default": ["320vp", "600vp", "840vp"],
                "required": False
            },
            "reference": {
                "type": "BreakpointsReference",
                "description": "断点切换参照物。",
                "default": "BreakpointsReference.WindowSize",
                "required": False
            }
        }
    },
    "GridLayoutOptions": {
        "type": "object",
        "description": "布局选项。其中,irregularIndexes和onGetIrregularSizeByIndex可对仅设置rowsTemplate或columnsTemplate的Grid使用，可以指定一个index数组，并为其中的index对应的GridItem设置其占据的行数与列数，使用方法参见示例3；onGetRectByIndex可对同时设置rowsTemplate和columnsTemplate的Grid使用，为指定的index对应的GridItem设置位置和大小，使用方法参见示例1。",
        "properties": {
            "regularSize": {
                "type": "array",
                "description": "大小规则的GridItem在Grid中占的行数和列数，只支持占1行1列即[1, 1]。",
                "required": True
            },
            "irregularIndexes": {
                "type": "array",
                "description": "指定的GridItem索引在Grid中的大小是不规则的。当不设置onGetIrregularSizeByIndex时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。",
                "required": False
            },
            "onGetIrregularSizeByIndex": {
                "type": "function",
                "description": "配合irregularIndexes使用，设置不规则GridItem占用的行数和列数。开发者可为irregularIndexes中指明的index对应的GridItem设置占用的行数和列数。在API version 12之前，垂直滚动Grid不支持GridItem占多行，水平滚动Grid不支持GridItem占多列。",
                "required": False
            },
            "onGetRectByIndex": {
                "type": "function",
                "description": "设置指定索引index对应的GridItem的位置及大小[rowStart,columnStart,rowSpan,columnSpan]。其中rowStart为行起始位置，columnStart为列起始位置，无单位。rowSpan为GridItem占用的行数，columnSpan为GridItem占用的列数，无单位。rowStart和columnStart取大于等于0的自然数，若取负数时，rowStart和columnStart默认为0。rowSpan和columnSpan取大于等于1的自然数，若取小数则向下取整，若小于1则按1计算。说明：第一种情况：某个GridItem发现给它指定的起始位置被占据了，则从起始位置[0,0]开始按顺序从左到右，从上到下寻找起始的放置位置。第二种情况：如果起始位置没有被占据，但其他位置被占据了，无法显示全部的GridItem大小，则只会布局一部分。",
                "required": False
            }
        }
    },
    "ComputedBarAttribute": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "totalOffset": {
                "type": "number",
                "description": "Grid内容相对显示区域的总偏移，单位px。",
                "required": True
            },
            "totalLength": {
                "type": "number",
                "description": "Grid内容总长度，单位px。",
                "required": True
            }
        }
    },
    "GridItemOptions": {
        "type": "object",
        "description": "GridItemOptions11+对象说明",
        "properties": {
            "style": {
                "type": "GridItemStyle",
                "description": "设置GridItem样式。",
                "default": "GridItemStyle.NONE",
                "required": False
            }
        }
    },
    "CloseSwipeActionOptions": {
        "type": "object",
        "description": "收起EXPANDED状态ListItem回调事件集合，用于设置收起动画完成后回调事件。",
        "properties": {
            "onFinish": {
                "type": "()=>void",
                "description": "在收起动画完成后触发。",
                "required": False
            }
        }
    },
    "ListScroller": {
        "type": "object",
        "description": "List组件的滚动控制器，通过它控制List组件的滚动，仅支持一对一绑定到List组件。ListScroller继承自Scroller，具有Scroller的全部方法。",
        "properties": {}
    },
    "OnScrollVisibleContentChangeCallback": {
        "type": "object",
        "description": "有子组件划入或划出List显示区域时触发。",
        "properties": {
            "start": {
                "type": "VisibleListContentInfo",
                "description": "当前显示界面第一个ListItem或ListItemGroup的详细信息。",
                "required": True
            },
            "end": {
                "type": "VisibleListContentInfo",
                "description": "当前显示界面最后一个ListItem或ListItemGroup的详细信息。",
                "required": True
            }
        }
    },
    "VisibleListContentInfo": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "index": {
                "type": "number",
                "description": "List显示区域内ListItem或ListItemGroup的索引值。",
                "required": True
            },
            "itemGroupArea": {
                "type": "ListItemGroupArea",
                "description": "如果当前可视页面的上边或下边在某个ListItemGroup之中，将会显示它所处的位置。",
                "required": False
            },
            "itemIndexInGroup": {
                "type": "number",
                "description": "如果当前可视页面的上边或下边在某个Group之中，将会显示Start或End的ListItem在Group中的索引。",
                "required": False
            }
        }
    },
    "SwipeActionItem": {
        "type": "object",
        "description": "List垂直布局，ListItem向右滑动，item左边的长距离滑动删除选项或向左滑动时，item右边的长距离滑动删除选项。List水平布局，ListItem向上滑动，item下边的长距离滑动删除选项或向下滑动时，item上边的长距离滑动删除选项。",
        "properties": {
            "actionAreaDistance": {
                "type": "Length",
                "description": "设置组件长距离滑动删除距离阈值。不支持设置百分比。删除距离阈值大于item宽度减去划出组件宽度，或删除距离阈值小于等于0就不会设置删除区域。",
                "default": "56vp",
                "required": False
            },
            "onAction": {
                "type": "() => void",
                "description": "组件进入长距删除区后删除ListItem时调用，进入长距删除区后抬手时触发。滑动后松手的位置超过或等于设置的距离阈值，并且设置的距离阈值有效时才会触发。",
                "required": False
            },
            "onEnterActionArea": {
                "type": "() => void",
                "description": "在滑动条目进入删除区域时调用，只触发一次，当再次进入时仍触发。",
                "required": False
            },
            "onExitActionArea": {
                "type": "() => void",
                "description": "当滑动条目退出删除区域时调用，只触发一次，当再次退出时仍触发。",
                "required": False
            },
            "builder": {
                "type": "CustomBuilder",
                "description": "当列表项向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列方向为“水平”时）时显示的操作项。",
                "required": False
            },
            "onStateChange": {
                "type": "(swipeActionState) => void",
                "description": "当列表项滑动状态变化时候触发。",
                "required": False
            }
        }
    },
    "ListItemOptions": {
        "type": "object",
        "description": "ListItemOptions10+对象说明。元服务API：从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "style": {
                "type": "ListItemStyle",
                "description": "设置List组件卡片样式。设置为ListItemStyle.NONE时无样式。设置为ListItemStyle.CARD时，建议配合ListItemGroup的ListItemGroupStyle.CARD同时使用，显示默认卡片样式。卡片样式下，ListItem默认规格：高度48vp，宽度100%，左右内边距8vp。如果需要实现ListItem高度自适应，可以把height设置为undefined。卡片样式下, 为卡片内的列表选项提供了默认的focus、hover、press、selected和disable样式。当前卡片模式下，使用默认Axis.Vertical排列方向，如果listDirection属性设置为Axis.Horizontal，会导致显示混乱；List属性alignListItem默认为ListItemAlign.Center，居中对齐显示。",
                "default": "ListItemStyle.NONE",
                "required": False
            }
        }
    },
    "ListItemGroupOptions": {
        "type": "object",
        "description": "ListItemGroupOptions对象说明",
        "properties": {
            "header": {
                "type": "CustomBuilder",
                "description": "设置ListItemGroup头部组件。可以放单个子组件或不放子组件。",
                "required": False
            },
            "footer": {
                "type": "CustomBuilder",
                "description": "设置ListItemGroup尾部组件。可以放单个子组件或不放子组件。",
                "required": False
            },
            "space": {
                "type": ["number", "string"],
                "description": "列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。",
                "default": 0,
                "required": False
            },
            "style": {
                "type": "ListItemGroupStyle",
                "description": "设置List组件卡片样式。设置为ListItemGroupStyle.NONE时无样式。设置为ListItemGroupStyle.CARD时，建议配合ListItem的ListItemStyle.CARD同时使用，显示默认卡片样式。卡片样式下，ListItemGroup默认规格：左右外边距12vp，上下左右内边距4vp。卡片样式下, 为卡片内的列表选项提供了默认的focus、hover、press、selected和disable样式。当前卡片模式下，使用默认Axis.Vertical排列方向，如果listDirection属性设置为Axis.Horizontal，会导致显示混乱;List属性alignListItem默认为ListItemAlign.Center，居中对齐显示。",
                "default": "ListItemGroupStyle.NONE",
                "required": False
            }
        }
    },
    "RefreshOptions": {
        "type": "object",
        "description": "RefreshOptions对象说明",
        "properties": {
            "refreshing": {
                "type": "boolean",
                "description": "组件当前是否处于刷新中状态。True表示处于刷新中状态，False表示未处于刷新中状态。",
                "default": False,
                "required": True
            },
            "offset": {
                "type": ["string", "number"],
                "description": "下拉起点距离组件顶部的距离。取值范围[0vp,64vp]。大于64vp按照64vp处理。不支持百分比，不支持负数。",
                "default": 16,
                "required": False
            },
            "friction": {
                "type": ["number", "string"],
                "description": "下拉摩擦系数，取值范围为0到100。0表示下拉刷新容器不跟随手势下拉而下拉。100表示下拉刷新容器紧紧跟随手势下拉而下拉。数值越大，下拉刷新容器跟随手势下拉的反应越灵敏。",
                "default": 62,
                "required": False
            },
            "builder": {
                "type": "CustomBuilder",
                "description": "自定义刷新区域显示内容。API version 10及之前版本，自定义组件的高度限制在64vp之内。API version 11及以后版本没有此限制。自定义组件设置了固定高度时，自定义组件会以固定高度显示在刷新区域下方；自定义组件未设置高度时，自定义组件高度会自适应刷新区域高度，会发生自定义组件高度跟随刷新区域变化至0的现象。建议对自定义组件设置最小高度约束来避免自定义组件高度小于预期的情况发生，具体可参照示例2。",
                "required": False
            },
            "promptText": {
                "type": "ResourceStr",
                "description": "设置刷新区域底部显示的自定义文本。输入文本的限制参考Text组件，使用builder自定义刷新区域显示内容时，promptText不显示。promptText设置有效时，refreshOffset属性默认值为96vp。",
                "required": False
            }
        }
    },
    "GuideLineStyle": {
        "type": "object",
        "description": "guideLine参数，用于定义一条guideline的id、方向和位置。",
        "properties": {
            "id": {
                "type": "string",
                "description": "guideline的id，必须是唯一的并且不可与容器内组件重名。",
                "required": True
            },
            "direction": {
                "type": "Axis",
                "description": "指定guideline的方向。",
                "default": "Axis.Vertical",
                "required": True
            },
            "position": {
                "type": "GuideLinePosition",
                "description": "指定guideline的位置。",
                "default": {
                    "start": 0
                },
                "required": True
            }
        }
    },
    "GuideLinePosition": {
        "type": "object",
        "description": "guideLine位置参数，用于定义guideline的位置。",
        "properties": {
            "start": {
                "type": "Dimension",
                "description": "guideline距离容器左侧或者顶部的距离。",
                "required": False
            },
            "end": {
                "type": "Dimension",
                "description": "guideline距离容器右侧或者底部的距离。",
                "required": False
            }
        }
    },
    "LocalizedBarrierStyle": {
        "type": "object",
        "description": "barrier参数，用于定义一条barrier的id、方向和生成时所依赖的组件。",
        "properties": {
            "id": {
                "type": "string",
                "description": "barrier的id，必须是唯一的并且不可与容器内组件重名。",
                "required": True
            },
            "localizedDirection": {
                "type": "LocalizedBarrierDirection",
                "description": "指定barrier的方向。",
                "required": True
            },
            "referencedId": {
                "type": "Array<string>",
                "description": "指定生成barrier所依赖的组件。",
                "required": True
            }
        }
    },
    "LocalizedBarrierDirection": {
        "type": "object",
        "description": "定义屏障线的方向。",
        "properties": {
            "START": {
                "type": "number",
                "description": "屏障在其所有referencedId的最左/右侧，LTR模式时为最左侧，RTL模式时为最右侧。",
                "default": 0
            },
            "END": {
                "type": "number",
                "description": "屏障在其所有referencedId的最左/右侧, LTR模式时为最右侧，RTL模式时为最左侧。",
                "default": 1
            },
            "TOP": {
                "type": "number",
                "description": "屏障在其所有referencedId的最上方。",
                "default": 2
            },
            "BOTTOM": {
                "type": "number",
                "description": "屏障在其所有referencedId的最下方。",
                "default": 3
            }
        }
    },
    "BarrierStyle": {
        "type": "object",
        "description": "barrier参数，用于定义一条barrier的id、方向和生成时所依赖的组件。",
        "properties": {
            "id": {
                "type": "string",
                "description": "barrier的id，必须是唯一的并且不可与容器内组件重名。",
                "required": True
            },
            "direction": {
                "type": "BarrierDirection",
                "description": "指定barrier的方向。",
                "default": "BarrierDirection.LEFT",
                "required": True
            },
            "referencedId": {
                "type": "Array<string>",
                "description": "指定生成barrier所依赖的组件。",
                "required": True
            }
        }
    },
    "ScrollSnapOptions": {
        "type": "object",
        "description": "设置Scroll组件限位滚动时的对齐方式和限位点等属性。",
        "properties": {
            "snapAlign": {
                "type": "ScrollSnapAlign",
                "description": "设置Scroll组件限位滚动时的对齐方式。",
                "default": "ScrollSnapAlign.NONE",
                "required": True
            },
            "snapPagination": {
                "type": ["Dimension", "Array<Dimension>"],
                "description": "设置Scroll组件限位滚动时的限位点，限位点即为Scroll组件能滑动停靠的偏移量。当属性为Dimension时，表示每页的大小，系统会按照该大小来自动计算每个限位点的位置。当属性为Array<Dimension>时，每个Dimension代表限位点的位置。每个Dimension的范围为[0,可滑动距离]，0和可滑动距离的底部自动成为限位点。当该属性不填或者Dimension为小于等于0的输入时，按异常值，无限位滚动处理。当该属性值为Array<Dimension>数组时，数组中的数值必须为单调递增。当输入为百分比时，实际的大小为Scroll组件的视口与百分比数值之积。",
                "required": False
            },
            "enableSnapToStart": {
                "type": "boolean",
                "description": "在Scroll组件限位滚动模式下，该属性设置为False后，允许Scroll在开头和第一个限位点间自由滑动。该属性仅当snapPagination属性为Array<Dimension>时生效，不支持Dimension。",
                "default": True,
                "required": False
            },
            "enableSnapToEnd": {
                "type": "boolean",
                "description": "在Scroll组件限位滚动模式下，该属性设置为False后，允许Scroll在最后一个限位点和末尾间自由滑动。该属性仅当snapPagination属性为Array<Dimension>时生效，不支持Dimension。",
                "default": True,
                "required": False
            }
        }
    },
    "ScrollOnScrollCallback": {
        "type": "object",
        "description": "Scroll滚动时触发的回调。",
        "properties": {
            "xOffset": {
                "type": "number",
                "description": "每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。",
                "required": True
            },
            "yOffset": {
                "type": "number",
                "description": "每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。",
                "required": True
            },
            "scrollState": {
                "type": "ScrollState",
                "description": "当前滚动状态。",
                "required": True
            }
        }
    },
    "ScrollOnWillScrollCallback": {
        "type": "object",
        "description": "Scroll滚动前触发的回调。",
        "properties": {
            "xOffset": {
                "type": "number",
                "description": "每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。",
                "required": True
            },
            "yOffset": {
                "type": "number",
                "description": "每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。",
                "required": True
            },
            "scrollState": {
                "type": "ScrollState",
                "description": "当前滚动状态。",
                "required": True
            },
            "scrollSource": {
                "type": "ScrollSource",
                "description": "当前滚动操作的来源。",
                "required": True
            }
        }
    },
    "OffsetResult": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。返回值单位为vp。",
        "properties": {
            "xOffset": {
                "type": "number",
                "description": "水平滑动偏移。",
                "required": True
            },
            "yOffset": {
                "type": "number",
                "description": "竖直滑动偏移。",
                "required": True
            }
        }
    },
    "ScrollAnimationOptions": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "duration": {
                "type": "number",
                "description": "设置滚动时长。设置为小于0的值时，按默认值显示。",
                "default": 1000,
                "required": False
            },
            "curve": {
                "type": ["Curve", "ICurve"],
                "description": "设置滚动曲线。",
                "default": "Curve.Ease",
                "required": False
            },
            "canOverScroll": {
                "type": "boolean",
                "description": "设置滚动是否可越界。仅在设置为True，且组件的edgeEffect设置为EdgeEffect.Spring时，滚动能够越界，并在越界时启动回弹动画。",
                "default": False,
                "required": False
            }
        }
    },
    "OffsetOptions": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "xOffset": {
                "type": "Dimension",
                "description": "水平滑动偏移",
                "default": "0",
                "required": False
            },
            "yOffset": {
                "type": "Dimension",
                "description": "垂直滑动偏移",
                "default": "0",
                "required": False
            }
        }
    },
    "ScrollEdgeOptions": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "velocity": {
                "type": "number",
                "description": "设置滚动到容器边缘的固定速度。如果设置小于等于0的值，参数不生效。",
                "default": 0,
                "required": False
            }
        }
    },
    "SwiperDisplayMode": {
        "type": "enum",
        "enum": ["Stretch", "AutoLinear", "STRETCH", "AUTO_LINEAR"],
        "description": "Swiper在主轴上的尺寸大小模式枚举。",
        "enumDescriptions": {
            "Stretch": "Swiper滑动一页的宽度为Swiper组件自身的宽度。从API version 10开始不再维护，建议使用STRETCH代替。",
            "AutoLinear": "Swiper滑动一页的宽度为子组件宽度中的最大值。从API version 10开始不再维护，建议使用Scroller.scrollTo代替。",
            "STRETCH": "Swiper滑动一页的宽度为Swiper组件自身的宽度。",
            "AUTO_LINEAR": "Swiper滑动一页的宽度为视窗内最左侧子组件的宽度。从API version 10开始支持，从API version 12开始不再维护，建议使用Scroller.scrollTo代替。"
        }
    },
    "SwiperNestedScrollMode": {
        "type": "enum",
        "enum": ["SELF_ONLY", "SELF_FIRST"],
        "description": "Swiper组件和父组件的嵌套滚动模式枚举。",
        "enumDescriptions": {
            "SELF_ONLY": "Swiper只自身滚动，不与父组件联动。",
            "SELF_FIRST": "Swiper自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Swiper触发边缘效果。"
        }
    },
    "Indicator": {
        "type": "object",
        "description": "设置导航点距离Swiper组件距离。",
        "properties": {
            "left": {
                "type": "Length",
                "required": True,
                "description": "设置导航点距离Swiper组件左边的距离。",
                "default": 0,
            },
            "top": {
                "type": "Length",
                "required": True,
                "description": "设置导航点距离Swiper组件顶部的距离。",
                "default": 0,
            },
            "right": {
                "type": "Length",
                "required": True,
                "description": "设置导航点距离Swiper组件右边的距离。",
                "default": 0,
            },
            "bottom": {
                "type": "Length",
                "required": True,
                "description": "设置导航点距离Swiper组件底部的距离。",
                "default": 0,
            },
            "start": {
                "type": "LengthMetrics",
                "required": True,
                "description": "在RTL模式下为导航点距离Swiper组件右边的距离，在LTR模式下为导航点距离Swiper组件左边的距离",
                "default": 0,
            },
            "end": {
                "type": "LengthMetrics",
                "required": True,
                "description": "在RTL模式下为导航点距离Swiper组件左边的距离，在LTR模式下为导航点距离Swiper组件右边的距离。",
                "default": 0,
            }
        }
    }
    ,

    "DotIndicator": {
        "type": "object",
        "description": "圆点指示器属性及功能继承自Indicator。",
        "properties": {
            "itemWidth": {
                "type": "Length",
                "description": "设置Swiper组件圆点导航指示器的宽，不支持设置百分比。",
                "default": 6,
                "required": True
            },
            "itemHeight": {
                "type": "Length",
                "description": "设置Swiper组件圆点导航指示器的高，不支持设置百分比。",
                "default": 6,
                "required": True
            },
            "selectedItemWidth": {
                "type": "Length",
                "description": "设置选中Swiper组件圆点导航指示器的宽，不支持设置百分比。",
                "default": 12,
                "required": True
            },
            "selectedItemHeight": {
                "type": "Length",
                "description": "设置选中Swiper组件圆点导航指示器的高，不支持设置百分比。",
                "default": 6,
                "required": True
            },
            "mask": {
                "type": "boolean",
                "description": "设置是否显示Swiper组件圆点导航指示器的蒙版样式。",
                "default": False,
                "required": True
            },
            "color": {
                "type": "ResourceColor",
                "description": "设置Swiper组件圆点导航指示器的颜色。",
                "default": "'#182431'",
                "required": True
            },
            "selectedColor": {
                "type": "ResourceColor",
                "description": "设置选中Swiper组件圆点导航指示器的颜色。",
                "default": "'#007DFF'",
                "required": True
            },
            "maxDisplayCount": {
                "type": "number",
                "description": "设置圆点导航点指示器样式下，导航点显示个数最大值，当实际导航点个数大于最大导航点个数时，会生效超长效果样式。",
                "required": True
            }
        }
    },
    "DigitIndicator": {
        "type": "object",
        "description": "数字指示器属性及功能继承自Indicator。从API version 10开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "fontColor": {
                "type": "ResourceColor",
                "description": "设置Swiper组件数字导航点的字体颜色。",
                "default": "#ff182431",
                "required": True
            },
            "selectedFontColor": {
                "type": "ResourceColor",
                "description": "设置选中Swiper组件数字导航点的字体颜色。",
                "default": "#ff182431",
                "required": True
            },
            "digitFont": {
                "type": "object",
                "description": "设置Swiper组件数字导航点的字体样式：- size：数字导航点指示器的字体大小，不支持设置百分比。- weight：数字导航点指示器的字重。",
                "properties": {
                    "size": {
                        "type": "Length",
                        "description": "数字导航点指示器的字体大小，不支持设置百分比。",
                        "default": "14vp"
                    },
                    "weight": {
                        "type": ["number", "FontWeight", "string"],
                        "description": "数字导航点指示器的字重。",
                        "default": "FontWeight.Normal"
                    }
                },
                "required": True
            },
            "selectedDigitFont": {
                "type": "object",
                "description": "设置选中Swiper组件数字导航点的字体样式：- size：数字导航点选中指示器的字体大小，不支持设置百分比。- weight：数字导航点选中指示器的字重。",
                "properties": {
                    "size": {
                        "type": "Length",
                        "description": "数字导航点选中指示器的字体大小，不支持设置百分比。",
                        "default": "14vp"
                    },
                    "weight": {
                        "type": ["number", "FontWeight", "string"],
                        "description": "数字导航点选中指示器的字重。",
                        "default": "FontWeight.Normal"
                    }
                },
                "required": True
            }
        }
    }
    ,

    "ArrowStyle": {
        "type": "object",
        "description": "左右箭头属性。",
        "properties": {
            "showBackground": {
                "type": "boolean",
                "description": "设置箭头底板是否显示。",
                "default": False,
                "required": False
            },
            "isSidebarMiddle": {
                "type": "boolean",
                "description": "设置箭头显示位置。默认显示在导航点指示器两侧。",
                "default": False,
                "required": False
            },
            "backgroundSize": {
                "type": "Length",
                "description": "设置底板大小。不支持设置百分比。",
                "default": "24vp",
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "设置底板颜色。",
                "default": "#00000000",
                "required": False
            },
            "arrowSize": {
                "type": "Length",
                "description": "设置箭头大小。不支持设置百分比。",
                "default": "18vp",
                "required": False
            },
            "arrowColor": {
                "type": "ResourceColor",
                "description": "设置箭头颜色。",
                "default": "#182431",
                "required": False
            }
        }
    }
    ,

    "SwiperAutoFill": {
        "type": "object",
        "description": "自适应属性。从API version 10开始，该接口支持在ArkTS卡片中使用。从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "minSize": {
                "type": "VP",
                "description": "设置元素显示最小宽度。",
                "default": 0,
                "required": True
            }
        }
    }
    ,

    "SwiperAnimationEvent": {
        "type": "object",
        "description": "Swiper组件动画相关信息集合。",
        "properties": {
            "currentOffset": {
                "type": "number",
                "description": "Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移。单位VP。",
                "default": 0,
                "required": True
            },
            "targetOffset": {
                "type": "number",
                "description": "Swiper动画目标元素在主轴方向上，相对于Swiper起始位置的位移。单位VP。",
                "default": 0,
                "required": True
            },
            "velocity": {
                "type": "number",
                "description": "Swiper离手动画开始时的离手速度。单位VP/S。",
                "default": 0,
                "required": True
            }
        }
    }
    ,

    "SwiperContentAnimatedTransition": {
        "type": "object",
        "description": "Swiper自定义切换动画相关信息。",
        "properties": {
            "timeout": {
                "type": "number",
                "description": "Swiper自定义切换动画超时时间。从页面执行默认动画（页面滑动）至移出视窗外的第一帧开始计时，如果到达该时间后，开发者仍未调用SwiperContentTransitionProxy的finishTransition接口通知Swiper组件此页面的自定义动画已结束，那么组件就会认为此页面的自定义动画已结束，立即将该页面节点下渲染树。",
                "default": 0,
                "required": False
            },
            "transition": {
                "type": "Callback<SwiperContentTransitionProxy>",
                "description": "自定义切换动画具体内容。",
                "required": True
            }
        }
    }
    ,

    "SwiperContentTransitionProxy": {
        "type": "object",
        "description": "Swiper自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画视窗内的页面信息，同时，也可以通过调用该对象的finishTransition接口通知Swiper组件页面自定义动画已结束。",
        "properties": {
            "selectedIndex": {
                "type": "number",
                "description": "当前选中页面的索引。",
                "required": True
            },
            "index": {
                "type": "number",
                "description": "视窗内页面的索引。",
                "required": True
            },
            "position": {
                "type": "number",
                "description": "index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。",
                "required": True
            },
            "mainAxisLength": {
                "type": "number",
                "description": "index对应页面在主轴方向上的长度。",
                "required": True
            }
        }
    }
    ,

    "ContentDidScrollCallback": {
        "type": "object",
        "description": "Swiper滑动时触发的回调，参数可参考SwiperContentTransitionProxy中的说明。",
        "properties": {
            "selectedIndex": {
                "type": "number",
                "description": "当前选中页面的索引。",
                "required": True
            },
            "index": {
                "type": "number",
                "description": "视窗内页面的索引。",
                "required": True
            },
            "position": {
                "type": "number",
                "description": "index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。",
                "required": True
            },
            "mainAxisLength": {
                "type": "number",
                "description": "index对应页面在主轴方向上的长度。",
                "required": True
            }
        }
    }
    ,

    "TabContentAnimatedTransition": {
        "type": "object",
        "description": "Tabs自定义切换动画相关信息。",
        "properties": {
            "timeout": {
                "type": "number",
                "description": "Tabs自定义切换动画超时时间。从自定义动画开始切换计时，如果到达该时间后，开发者仍未调用TabContentTransitionProxy的finishTransition接口通知Tabs组件自定义动画结束，那么组件就会认为此次自定义动画已结束，直接执行后续操作。",
                "default": 1000,
                "required": False
            },
            "transition": {
                "type": "function",
                "description": "自定义切换动画具体内容。",
                "required": True
            }
        }
    }
    ,

    "TabContentTransitionProxy": {
        "type": "object",
        "description": "Tabs自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画的起始和目标页面信息，同时，也可以通过调用该对象的finishTransition接口通知Tabs组件自定义动画已结束。",
        "properties": {
            "from": {
                "type": "number",
                "description": "自定义动画起始页面对应的index值。",
                "required": True
            },
            "to": {
                "type": "number",
                "description": "自定义动画目标页面对应的index值。",
                "required": True
            },
            "finishTransition": {
                "type": "function",
                "description": "通知Tabs组件，此页面的自定义动画已结束。",
                "required": True
            }
        }
    }
    ,

    "TabsController": {
        "type": "object",
        "description": "Tabs组件的控制器，用于控制Tabs组件进行页签切换。不支持一个TabsController控制多个Tabs组件。",
        "properties": {
            "constructor": {
                "type": "function",
                "description": "TabsController的构造函数。"
            },
            "changeIndex": {
                "type": "function",
                "description": "控制Tabs切换到指定页签。",
                "properties": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "页签在Tabs里的索引值，索引值从0开始。设置小于0或大于最大数量的值时，取默认值0。"
                    }
                }
            },
            "preloadItems": {
                "type": "function",
                "description": "控制Tabs预加载指定子节点。调用该接口后会一次性加载所有指定的子节点，因此为了性能考虑，建议分批加载子节点。",
                "properties": {
                    "indices": {
                        "type": "Optional<Array<number>>",
                        "required": True,
                        "description": "需预加载的子节点的下标数组。默认值：空数组。"
                    }
                },
                "returns": {
                    "type": "Promise<void>",
                    "description": "预加载完成后触发的回调。"
                },
                "errors": {
                    "401": "Parameter invalid. Possible causes: 1. The parameter type is not Array<number>; 2. The parameter is an empty array; 3. The parameter contains an invalid index."
                }
            }
        }
    }
    ,

    "SideBarContainerType": {
        "type": "enum",
        "enum": ["Embed", "Overlay", "AUTO"],
        "description": "该枚举类用于定义侧边栏的显示模式",
        "enumDescriptions": {
            "Embed": "侧边栏嵌入到组件内，和内容区并列显示。组件尺寸小于minContentWidth + minSideBarWidth,并且未设置showSideBar时，侧边栏自动隐藏。未设置minSideBarWidth或者minContentWidth采用未设置接口的默认值进行计算。组件在自动隐藏后，如果通过点击控制按钮唤出侧边栏，则侧边栏悬浮在内容区上显示。",
            "Overlay": "侧边栏浮在内容区上面。",
            "AUTO": "组件尺寸大于等于minSideBarWidth+minContentWidth时，采用Embed模式显示。组件尺寸小于minSideBarWidth+minContentWidth时，采用Overlay模式显示。未设置minSideBarWidth或minContentWidth时，会使用未设置接口的默认值进行计算，若计算的值小于600vp，则使用600vp做为模式切换的断点值。"
        }
    }
    ,

    "SideBarPosition": {
        "type": "object",
        "enum": ["Start", "End"],
        "description": "侧边栏显示位置。",
        "enumDescriptions": {
            "Start": "侧边栏位于容器左侧。",
            "End": "侧边栏位于容器右侧。"
        }
    }
    ,

    "ButtonStyle": {
        "type": "object",
        "description": "ButtonStyle对象说明",
        "properties": {
            "left": {
                "type": "number",
                "description": "设置侧边栏控制按钮距离容器左界限的间距。",
                "default": 16,
                "required": False
            },
            "top": {
                "type": "number",
                "description": "设置侧边栏控制按钮距离容器上界限的间距。",
                "default": 48,
                "required": False
            },
            "width": {
                "type": "number",
                "description": "设置侧边栏控制按钮的宽度。",
                "default": {
                    "从API version 10开始": 24
                },
                "required": False
            },
            "height": {
                "type": "number",
                "description": "设置侧边栏控制按钮的高度。",
                "default": {
                    "从API version 10开始": 24
                },
                "required": False
            },
            "icons": {
                "type": "object",
                "description": "设置侧边栏控制按钮的图标：\n- shown: 设置侧边栏显示时控制按钮的图标。\n说明：\n资源获取错误时，使用默认图标。\n- hidden: 设置侧边栏隐藏时控制按钮的图标。\n- switching:设置侧边栏显示和隐藏状态切换时控制按钮的图标。",
                "properties": {
                    "shown": {
                        "type": ["string", "PixelMap", "Resource"],
                        "description": "设置侧边栏显示时控制按钮的图标。",
                        "required": False
                    },
                    "hidden": {
                        "type": ["string", "PixelMap", "Resource"],
                        "description": "设置侧边栏隐藏时控制按钮的图标。",
                        "required": False
                    },
                    "switching": {
                        "type": ["string", "PixelMap", "Resource"],
                        "description": "设置侧边栏显示和隐藏状态切换时控制按钮的图标。",
                        "required": False
                    }
                },
                "required": False
            }
        }
    }
    ,

    "DividerStyle": {
        "type": "object",
        "description": "分割线的样式设置",
        "properties": {
            "strokeWidth": {
                "type": "Length",
                "description": "分割线的线宽。",
                "default": "1vp",
                "required": True
            },
            "color": {
                "type": "ResourceColor",
                "description": "分割线的颜色。",
                "default": "#000000，3%"
            },
            "startMargin": {
                "type": "Length",
                "description": "分割线与侧边栏顶端的距离。",
                "default": 0
            },
            "endMargin": {
                "type": "Length",
                "description": "分割线与侧边栏底端的距离。",
                "default": 0
            }
        }
    }
    ,

    "SubTabBarStyle": {
        "type": "object",
        "description": "子页签样式。打开后在切换页签时会播放跳转动画。",
        "properties": {
            "constructor": {
                "type": "function",
                "description": "SubTabBarStyle的构造函数。支持ComponentContent设置自定义内容。",
                "properties": [
                    {
                        "name": "content",
                        "type": ["ResourceStr", "ComponentContent"],
                        "required": True,
                        "description": "页签内的内容。"
                    }
                ]
            },
            "of": {
                "type": "function",
                "description": "SubTabBarStyle的静态构造函数。",
                "properties": [
                    {
                        "name": "content",
                        "type": ["ResourceStr", "ComponentContent"],
                        "required": True,
                        "description": "页签内的内容。支持ComponentContent设置自定义内容。"
                    }
                ],
                "returns": {
                    "type": "SubTabBarStyle",
                    "description": "返回创建的SubTabBarStyle对象。"
                }
            },
            "indicator": {
                "type": "IndicatorStyle",
                "required": True,
                "description": "设置选中子页签的下划线风格。子页签的下划线风格仅在水平模式下有效。"
            },
            "selectedMode": {
                "type": "SelectedMode",
                "required": True,
                "description": "设置选中子页签的显示方式。子页签的显示方式仅在水平模式下有效。",
                "default": "SelectedMode.INDICATOR"
            },
            "board": {
                "type": "BoardStyle",
                "required": True,
                "description": "设置选中子页签的背板风格。子页签的背板风格仅在水平模式下有效。"
            },
            "labelStyle": {
                "type": "LabelStyle",
                "required": True,
                "description": "设置子页签的label文本和字体的样式。"
            },
            "padding": {
                "type": "LocalizedPadding",
                "required": True,
                "description": "设置子页签的内边距属性，支持镜像能力（不支持百分比设置）。",
                "default": "{start:LengthMetrics.vp(8),end:LengthMetrics.vp(8),top:LengthMetrics.vp(17),"
                           "bottom:LengthMetrics.vp(18)}"
            },
            "id": {
                "type": "string",
                "required": True,
                "description": "设置子页签的id。"
            }
        }
    },

    "LabelStyle": {
        "type": "object",
        "description": "Label文本和字体的样式。",
        "properties": {
            "overflow": {
                "type": "TextOverflow",
                "required": False,
                "description": "设置Label文本超长时的显示方式。",
                "default": "TextOverflow.ELLIPSIS"
            },
            "maxLines": {
                "type": "number",
                "required": False,
                "description": "设置Label文本的最大行数。",
                "default": 1
            },
            "minFontSize": {
                "type": ["number", "ResourceStr"],
                "required": False,
                "description": "设置Label文本最小显示字号（不支持百分比设置）。",
                "default": "0.0fp"
            },
            "maxFontSize": {
                "type": ["number", "ResourceStr"],
                "required": False,
                "description": "设置Label文本最大显示字号（不支持百分比设置）。",
                "default": "0.0fp"
            },
            "heightAdaptivePolicy": {
                "type": "TextHeightAdaptivePolicy",
                "required": False,
                "description": "设置Label文本自适应高度的方式。",
                "default": "TextHeightAdaptivePolicy.MAX_LINES_FIRST"
            },
            "font": {
                "type": "Font",
                "required": False,
                "description": "设置Label文本字体样式。",
                "default": "字体大小16.0fp、字体类型'HarmonyOS Sans'，字体风格正常，字重正常。"
            },
            "unselectedColor": {
                "type": "ResourceColor",
                "required": False,
                "description": "设置Label文本字体未选中时的颜色。",
                "default": "#99182431"
            },
            "selectedColor": {
                "type": "ResourceColor",
                "required": False,
                "description": "设置Label文本字体选中时的颜色。",
                "default": "#FF007DFF"
            }
        }
    },
    "BottomTabBarStyle": {
        "type": "object",
        "description": "底部页签和侧边页签样式。",
        "properties": {
            "constructor": {
                "type": "function",
                "description": "BottomTabBarStyle的构造函数。",
                "properties": {
                    "icon": {
                        "type": ["ResourceStr", "TabBarSymbol12+"],
                        "required": True,
                        "description": "页签内的图片内容。"
                    },
                    "text": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "页签内的文字内容。"
                    },

                }
            },
            "of": {
                "type": "function",
                "description": "BottomTabBarStyle的静态构造函数。",
                "properties": {
                    "icon": {
                        "type": ["ResourceStr", "TabBarSymbol"],
                        "required": True,
                        "description": "页签内的图片内容。"
                    },
                    "text": {
                        "type": "ResourceStr",
                        "required": True,
                        "description": "页签内的文字内容。"
                    }
                },
                "returns": {
                    "type": "BottomTabBarStyle",
                    "description": "返回创建的BottomTabBarStyle对象。"
                }
            },
            "padding": {
                "type": ["Padding", "Dimension", "LocalizedPadding12+"],
                "required": True,
                "description": "设置底部页签的内边距属性（不支持百分比设置）。使用Dimension时，四个方向内边距同时生效。使用LocalizedPadding时，支持镜像能力。",
                "default": "{left:4.0vp,right:4.0vp,top:0.0vp,bottom:0.0vp}"
            },
            "verticalAlign": {
                "type": "VerticalAlign",
                "required": True,
                "description": "设置底部页签的图片、文字在垂直方向上的对齐格式。",
                "default": "VerticalAlign.Center"
            },
            "layoutMode": {
                "type": "LayoutMode",
                "required": True,
                "description": "设置底部页签的图片、文字排布的方式，具体参照LayoutMode枚举。",
                "default": "LayoutMode.VERTICAL"
            },
            "symmetricExtensible": {
                "type": "boolean",
                "required": True,
                "description": "设置底部页签的图片、文字是否可以对称借左右底部页签的空余位置中的最小值，仅fixed水平模式下在底部页签之间有效。",
                "default": False
            },
            "labelStyle": {
                "type": "LabelStyle",
                "required": True,
                "description": "设置底部页签的label文本和字体的样式。"
            },
            "id": {
                "type": "string",
                "required": True,
                "description": "设置底部页签的id。"
            },
            "iconStyle": {
                "type": "TabBarIconStyle",
                "required": True,
                "description": "设置底部页签的label图标的样式。"
            },

        }
    }
    ,

    "BoardStyle": {
        "type": "object",
        "description": "背板的圆角半径（不支持百分比设置）。",
        "properties": {
            "borderRadius": {
                "type": "Length",
                "description": "背板的圆角半径（不支持百分比设置）。",
                "default": 8.0,
                "required": False
            }
        }
    },

    "TabBarSymbol": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "normal": {
                "type": "SymbolGlyphModifier",
                "description": "页签内symbol图标普通态样式。",
                "default": {
                    "fontColor": "#66182431",
                    "renderingStrategy": "SymbolRenderingStrategy.MULTIPLE_OPACITY",
                    "fontSize": "24vp"
                },
                "required": True
            },
            "selected": {
                "type": "SymbolGlyphModifier",
                "description": "页签内symbol图标选中态样式。",
                "default": {
                    "fontColor": "#ff007dff",
                    "renderingStrategy": "SymbolRenderingStrategy.MULTIPLE_OPACITY",
                    "fontSize": "24vp"
                },
                "required": False
            }
        }
    }
    ,

    "LayoutMode": {
        "type": "enum",
        "enum": ["AUTO", "VERTICAL", "HORIZONTAL"],
        "description": "元服务API： 从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "AUTO": "若页签宽度大于104vp，页签内容为左右排布，否则页签内容为上下排布。仅TabBar为垂直模式或Fixed水平模式时有效。",
            "VERTICAL": "页签内容上下排布。",
            "HORIZONTAL": "页签内容左右排布。"
        }
    }
    ,

    "TabBarIconStyle": {
        "type": "object",
        "description": "从API version 12开始，该接口支持在元服务中使用。",
        "properties": {
            "unselectedColor": {
                "type": "ResourceColor",
                "description": "设置Label图标未选中时的颜色。仅对svg图源生效，设置后会替换svg图片的填充颜色。",
                "default": "#33182431",
                "required": False
            },
            "selectedColor": {
                "type": "ResourceColor",
                "description": "设置Label图标选中时的颜色。仅对svg图源生效，设置后会替换svg图片的填充颜色。",
                "default": "#FF007DFF",
                "required": False
            }
        }
    }
    ,

    "WaterFlowOptions": {
        "type": "object",
        "description": "WaterFlowOptions对象说明",
        "properties": {
            "footer": {
                "type": "CustomBuilder",
                "description": "设置WaterFlow尾部组件。",
                "required": False
            },
            "scroller": {
                "type": "Scroller",
                "description": "可滚动组件的控制器，与可滚动组件绑定。不允许和其他滚动类组件，如：List、Grid、Scroll等绑定同一个滚动控制对象。",
                "required": False
            },
            "sections": {
                "type": "WaterFlowSections",
                "description": "设置FlowItem分组，实现同一个瀑布流组件内部各分组使用不同列数混合布局。使用分组混合布局时会忽略columnsTemplate和rowsTemplate属性。使用分组混合布局时不支持单独设置footer，可以使用最后一个分组作为尾部组件。",
                "required": False
            },
            "layoutMode": {
                "type": "WaterFlowLayoutMode",
                "description": "设置WaterFlow的布局模式，根据使用场景选择更切合的模式。默认值：ALWAYS_TOP_DOWN。",
                "default": "ALWAYS_TOP_DOWN",
                "required": False
            }
        }
    }
    ,

    "WaterFlowSections": {
        "type": "object",
        "description": "瀑布流分组信息。",
        "properties": {
            "splice": {
                "type": "function",
                "description": "移除或者替换已存在的分组和/或添加新分组。",
                "properties": {
                    "start": {
                        "type": "number",
                        "required": True,
                        "description": "从0开始计算的索引，会转换为整数，表示要开始改变分组的位置。如果索引是负数，则从末尾开始计算，使用start + WaterFlowSections.length()。如果 start < -WaterFlowSections.length()，则使用0。如果 start >= WaterFlowSections.length()，则在最后添加新分组。"
                    },
                    "deleteCount": {
                        "type": "number",
                        "required": False,
                        "description": "表示要从start开始删除的分组数量。如果省略了deleteCount，或者其值大于或等于由start指定的位置到WaterFlowSections末尾的分组数量，那么从start到WaterFlowSections末尾的所有分组将被删除。如果deleteCount是0或者负数，则不会删除任何分组。"
                    },
                    "sections": {
                        "type": "Array<SectionOptions>",
                        "required": False,
                        "description": "表示要从start开始加入的分组。如果不指定，splice()将只从瀑布流中删除分组。"
                    },
                    "layoutMode": {
                        "type": "WaterFlowLayoutMode",
                        "description": "设置WaterFlow的布局模式，根据使用场景选择更切合的模式。默认值：ALWAYS_TOP_DOWN。",
                        "default": "ALWAYS_TOP_DOWN",
                        "required": False
                    }
                },
                "returnType": {
                    "type": "boolean",
                    "description": "分组是否修改成功，要加入的分组中有任意分组的itemsCount不是正整数时返回false。"
                }
            },
            "push": {
                "type": "function",
                "description": "将指定分组添加到瀑布流末尾。",
                "properties": {
                    "section": {
                        "type": "SectionOptions",
                        "required": True,
                        "description": "添加到瀑布流末尾的分组。"
                    }
                },
                "returnType": {
                    "type": "boolean",
                    "description": "分组是否添加成功，新分组的itemsCount不是正整数时返回false。"
                }
            },
            "update": {
                "type": "function",
                "description": "修改指定索引分组的配置信息。",
                "properties": {
                    "sectionIndex": {
                        "type": "number",
                        "required": True,
                        "description": "从0开始计算的索引，会转换为整数，表示要修改的分组的位置。如果索引是负数，则从末尾开始计算，使用sectionIndex + WaterFlowSections.length()。如果sectionIndex < -WaterFlowSections.length()，则使用0。如果sectionIndex >= WaterFlowSections.length()，则在最后添加新分组。"
                    },
                    "section": {
                        "type": "SectionOptions",
                        "required": True,
                        "description": "新的分组信息。"
                    }
                },
                "returnType": {
                    "type": "boolean",
                    "description": "分组是否更新成功，新分组的itemsCount不是正整数时返回false。"
                }
            },
            "values": {
                "type": "function",
                "description": "获取瀑布流中所有分组配置信息。",
                "returnType": {
                    "type": "Array<SectionOptions>",
                    "description": "瀑布流中所有分组配置信息。"
                }
            },
            "length": {
                "type": "function",
                "description": "获取瀑布流中分组数量。",
                "returnType": {
                    "type": "number",
                    "description": "瀑布流中分组数量。"
                }
            }
        }
    }
    ,

    "GetItemMainSizeByIndex": {
        "type": "object",
        "description": "根据index获取指定Item的主轴大小。纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。",
        "properties": {
            "index": {
                "type": "number",
                "description": "FlowItem在WaterFlow中的索引。",
                "required": True
            }
        }
    }
    ,

    "WaterFlowLayoutMode": {
        "type": "enum",
        "enum": ["ALWAYS_TOP_DOWN", "SLIDING_WINDOW"],
        "description": "从API version 12开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "ALWAYS_TOP_DOWN": "默认的从上到下的布局模式。视窗内的FlowItem依赖视窗上方所有FlowItem的布局信息。因此跳转或切换列数时，需要计算出上方所有的FlowItem的布局信息。",
            "SLIDING_WINDOW": "移动窗口式的布局模式。只考虑视窗内的布局信息，对视窗上方的FlowItem没有依赖关系，因此向后跳转或切换列数时只需要布局视窗内的FlowItem。有频繁切换列数的场景的应用建议使用该模式。说明：1. 无动画跳转到较远的位置时，会以目标位置为基准，向前或向后布局FlowItem。这之后如果滑回跳转前的位置，内容的布局效果可能和之前不一致。 这个效果会导致跳转后回滑到顶部时，顶部节点可能不对齐。所以该布局模式下会在滑动到顶部后自动调整布局，保证顶部对齐。在有多个分组的情况下，会在滑动结束时调整视窗顶部的分组。2. 该模式不支持使用滚动条，就算设置了滚动条也无法显示。3. 不支持scroller的scrollTo接口。4. 如果在同一帧内调用跳转（如无动画的scrollToIndex、scrollEdge）和输入偏移量（如滑动手势或滚动动画），两者都会生效。"
        }
    }
    ,

    "WithThemeOptions": {
        "type": "object",
        "description": "设置WithTheme作用域内组件缺省样式及深浅色模式。",
        "properties": {
            "theme": {
                "type": "CustomTheme",
                "description": "用于自定义WithTheme作用域内组件缺省配色。",
                "default": "undefined",
                "required": False
            },
            "colorMode": {
                "type": "ThemeColorMode",
                "description": "用于指定WithTheme作用域内组件深浅色模式。",
                "default": "ThemeColorMode.System",
                "required": False
            }
        }
    }
    ,

    "VideoOptions": {
        "type": "object",
        "description": "视频选项对象，用于配置视频的数据源、播放倍速、预览图片路径、控制器和图像AI分析选项。",
        "properties": {
            "src": {
                "type": ["string", "Resource"],
                "description": "视频的数据源，支持本地视频和网络视频。Resource格式可以跨包/跨模块访问资源文件，常用于访问本地视频。string格式可用于加载网络视频和本地视频，常用于加载网络视频。",
                "required": False
            },
            "currentProgressRate": {
                "type": ["number", "string", "PlaybackSpeed"],
                "description": "视频播放倍速。number取值仅支持：0.75，1.0，1.25，1.75，2.0。",
                "default": "PlaybackSpeed.Speed_Forward_1_00_X",
                "required": False
            },
            "previewUri": {
                "type": ["string", "PixelMap", "Resource"],
                "description": "视频未播放时的预览图片路径，默认不显示图片。",
                "required": False
            },
            "controller": {
                "type": "VideoController",
                "description": "设置视频控制器，可以控制视频的播放状态。",
                "required": False
            },
            "imageAIOptions": {
                "type": "ImageAIOptions",
                "description": "设置图像AI分析选项，可配置分析类型或绑定一个分析控制器。",
                "required": False
            }
        }
    }
    ,

    "PlaybackSpeed": {
        "type": "enum",
        "enum": [
            "Speed_Forward_0_75_X",
            "Speed_Forward_1_00_X",
            "Speed_Forward_1_25_X",
            "Speed_Forward_1_75_X",
            "Speed_Forward_2_00_X"
        ],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "Speed_Forward_0_75_X": "0.75倍速播放。",
            "Speed_Forward_1_00_X": "1倍速播放。",
            "Speed_Forward_1_25_X": "1.25倍速播放。",
            "Speed_Forward_1_75_X": "1.75倍速播放。",
            "Speed_Forward_2_00_X": "2倍速播放。"
        }
    }
    ,

    "SeekMode": {
        "type": "enum",
        "enum": ["PreviousKeyframe", "NextKeyframe", "ClosestKeyframe", "Accurate"],
        "description": "元服务API： 从API version 11开始，该接口支持在元服务中使用。",
        "enumDescriptions": {
            "PreviousKeyframe": "跳转到前一个最近的关键帧。",
            "NextKeyframe": "跳转到后一个最近的关键帧。",
            "ClosestKeyframe": "跳转到最近的关键帧。",
            "Accurate": "精准跳转，不论是否为关键帧。"
        }
    }
    ,

    "AlertDialogParam": {
        "type": "object",
        "description": "弹窗参数对象，用于配置弹窗的各种属性。",
        "properties": {
            "title": {
                "type": "ResourceStr",
                "description": "弹窗标题。",
                "required": False
            },
            "subtitle": {
                "type": "ResourceStr",
                "description": "弹窗副标题。",
                "required": False
            },
            "message": {
                "type": "ResourceStr",
                "description": "弹窗内容。",
                "required": True
            },
            "autoCancel": {
                "type": "boolean",
                "description": "点击遮障层时，是否关闭弹窗，true表示关闭弹窗。false表示不关闭弹窗。",
                "default": True,
                "required": False
            },
            "cancel": {
                "type": "() => void",
                "description": "点击遮障层关闭dialog时的回调。",
                "required": False
            },
            "alignment": {
                "type": "DialogAlignment",
                "description": "弹窗在竖直方向上的对齐方式。",
                "default": "DialogAlignment.Default",
                "required": False
            },
            "offset": {
                "type": "Offset",
                "description": "弹窗相对alignment所在位置的偏移量。",
                "default": {"dx": 0, "dy": 0},
                "required": False
            },
            "gridCount": {
                "type": "number",
                "description": "弹窗容器宽度所占用栅格数。",
                "default": 4,
                "required": False
            },
            "maskRect": {
                "type": "Rectangle",
                "description": "弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。",
                "default": {"x": 0, "y": 0, "width": "100%", "height": "100%"},
                "required": False
            },
            "showInSubWindow": {
                "type": "boolean",
                "description": "某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。",
                "default": False,
                "required": False
            },
            "isModal": {
                "type": "boolean",
                "description": "弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。",
                "default": True,
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "弹窗背板颜色。",
                "default": "Color.Transparent",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "弹窗背板模糊材质。",
                "default": "BlurStyle.COMPONENT_ULTRA_THICK",
                "required": False
            },
            "onWillDismiss": {
                "type": "Callback<DismissDialogAction>",
                "description": "交互式关闭回调函数。",
                "required": False
            },
            "cornerRadius": {
                "type": ["BorderRadiuses", "Dimension", "LocalizedBorderRadiuses"],
                "description": "设置背板的圆角半径。可分别设置4个圆角的半径。",
                "default": {"topLeft": "32vp", "topRight": "32vp", "bottomLeft": "32vp", "bottomRight": "32vp"},
                "required": False
            },
            "transition": {
                "type": "TransitionEffect",
                "description": "设置弹窗显示和退出的过渡效果。",
                "required": False
            },
            "width": {
                "type": "Dimension",
                "description": "设置弹窗背板的宽度。",
                "required": False
            },
            "height": {
                "type": "Dimension",
                "description": "设置弹窗背板的高度。",
                "required": False
            },
            "borderWidth": {
                "type": ["Dimension", "EdgeWidths", "LocalizedEdgeWidths"],
                "description": "可分别设置4个边框宽度。",
                "default": 0,
                "required": False
            },
            "borderColor": {
                "type": ["ResourceColor", "EdgeColors", "LocalizedEdgeColors"],
                "description": "设置弹窗背板的边框颜色。",
                "default": "Color.Black",
                "required": False
            },
            "borderStyle": {
                "type": ["BorderStyle", "EdgeStyles"],
                "description": "设置弹窗背板的边框样式。",
                "default": "BorderStyle.Solid",
                "required": False
            },
            "shadow": {
                "type": ["ShadowOptions", "ShadowStyle"],
                "description": "设置弹窗背板的阴影。",
                "required": False
            },
            "textStyle": {
                "type": "TextStyle",
                "description": "设置弹窗message内容的文本样式。",
                "required": False
            }
        }
    }
    ,

    "AlertDialogParamWithConfirm": {
        "type": "object",
        "description": "继承自AlertDialogParam。元服务API：从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "confirm": {
                "type": "object",
                "required": False,
                "description": "确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。默认响应Enter键能力在defaultFocus为true时不生效。",
                "properties": {
                    "enabled": {
                        "type": "boolean",
                        "description": "点击Button是否响应，true表示Button可以响应，false表示Button不可以响应。",
                        "default": True
                    },
                    "defaultFocus": {
                        "type": "boolean",
                        "description": "设置Button是否是默认焦点，true表示Button是默认焦点，false表示Button不是默认焦点。",
                        "default": False
                    },
                    "style": {
                        "type": "DialogButtonStyle",
                        "description": "设置Button的风格样式。",
                        "default": "DialogButtonStyle.DEFAULT"
                    },
                    "value": {
                        "type": "ResourceStr",
                        "description": "Button文本内容。"
                    },
                    "fontColor": {
                        "type": "ResourceColor",
                        "description": "Button文本颜色。"
                    },
                    "backgroundColor": {
                        "type": "ResourceColor",
                        "description": "Button背景颜色。"
                    },
                    "action": {
                        "type": "function",
                        "description": "Button选中时的回调。"
                    }
                }
            }
        }
    }
    ,

    "AlertDialogParamWithButtons": {
        "type": "object",
        "description": "继承自AlertDialogParam。元服务API：从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "primaryButton": {
                "type": "object",
                "required": False,
                "description": "确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。默认响应Enter键能力在defaultFocus为true时不生效。",
                "properties": {
                    "enabled": {
                        "type": "boolean",
                        "description": "点击Button是否响应。",
                        "default": True
                    },
                    "defaultFocus": {
                        "type": "boolean",
                        "description": "设置Button是否是默认焦点。",
                        "default": False
                    },
                    "style": {
                        "type": "DialogButtonStyle",
                        "description": "设置Button的风格样式。",
                        "default": "DialogButtonStyle.DEFAULT"
                    },
                    "value": {
                        "type": "ResourceStr",
                        "description": "Button文本内容。"
                    },
                    "fontColor": {
                        "type": "ResourceColor",
                        "description": "Button文本颜色。"
                    },
                    "backgroundColor": {
                        "type": "ResourceColor",
                        "description": "Button背景颜色。"
                    },
                    "action": {
                        "type": "function",
                        "description": "Button选中时的回调。"
                    }
                }
            },
            "secondaryButton": {
                "type": "object",
                "required": False,
                "description": "确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。",
                "properties": {
                    "enabled": {
                        "type": "boolean",
                        "description": "点击Button是否响应。",
                        "default": True
                    },
                    "defaultFocus": {
                        "type": "boolean",
                        "description": "设置Button是否是默认焦点。",
                        "default": False
                    },
                    "style": {
                        "type": "DialogButtonStyle",
                        "description": "设置Button的风格样式。",
                        "default": "DialogButtonStyle.DEFAULT"
                    },
                    "value": {
                        "type": "ResourceStr",
                        "description": "Button文本内容。"
                    },
                    "fontColor": {
                        "type": "ResourceColor",
                        "description": "Button文本颜色。"
                    },
                    "backgroundColor": {
                        "type": "ResourceColor",
                        "description": "Button背景颜色。"
                    },
                    "action": {
                        "type": "function",
                        "description": "Button选中时的回调。"
                    }
                }
            }
        }
    }
    ,

    "AlertDialogParamWithOptions": {
        "type": "object",
        "description": "继承自AlertDialogParam。元服务API：从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "buttons": {
                "type": "Array<AlertDialogButtonOptions>",
                "description": "弹窗容器中的多个按钮。",
                "required": True
            },
            "buttonDirection": {
                "type": "DialogButtonDirection",
                "description": "按钮排布方向。建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮），非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。",
                "default": "DialogButtonDirection.AUTO",
                "required": False
            }
        }
    }
    ,

    "AlertDialogButtonOptions": {
        "type": "object",
        "description": "AlertDialogButtonOptions10+对象说明",
        "properties": {
            "enabled": {
                "type": "boolean",
                "description": "点击Button是否响应",
                "default": True,
                "required": False
            },
            "defaultFocus": {
                "type": "boolean",
                "description": "设置Button是否是默认焦点",
                "default": False,
                "required": False
            },
            "style": {
                "type": "DialogButtonStyle",
                "description": "设置Button的风格样式",
                "default": "DialogButtonStyle.DEFAULT",
                "required": False
            },
            "value": {
                "type": "ResourceStr",
                "description": "Button的文本内容，若值为null，则该按钮不显示",
                "required": True
            },
            "fontColor": {
                "type": "ResourceColor",
                "description": "Button的文本颜色",
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "Button背景颜色",
                "required": False
            },
            "action": {
                "type": "() => void",
                "description": "Button选中时的回调",
                "required": True
            },
            "primary": {
                "type": "boolean",
                "description": "在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效",
                "required": False
            }
        }
    }
    ,

    "DialogButtonDirection": {
        "type": "enum",
        "enum": ["AUTO", "HORIZONTAL", "VERTICAL"],
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "AUTO": "两个及以下按钮水平排布，两个以上为竖直排布。",
            "HORIZONTAL": "按钮水平布局。",
            "VERTICAL": "按钮竖直布局。"
        }
    }
    ,

    "DialogAlignment": {
        "type": "enum",
        "enum": [
            "Top",
            "Center",
            "Bottom",
            "Default",
            "TopStart",
            "TopEnd",
            "CenterStart",
            "CenterEnd",
            "BottomStart",
            "BottomEnd"
        ],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "Top": "垂直顶部对齐。",
            "Center": "垂直居中对齐。",
            "Bottom": "垂直底部对齐。",
            "Default": "默认对齐。",
            "TopStart": "左上对齐。",
            "TopEnd": "右上对齐。",
            "CenterStart": "左中对齐。",
            "CenterEnd": "右中对齐。",
            "BottomStart": "左下对齐。",
            "BottomEnd": "右下对齐。"
        }
    }
    ,

    "ActionSheetOptions": {
        "type": "object",
        "description": "ActionSheetOptions对象说明",
        "properties": {
            "title": {
                "type": ["Resource", "string"],
                "description": "弹窗标题。",
                "required": True
            },
            "subtitle": {
                "type": "ResourceStr",
                "description": "弹窗副标题。",
                "required": False
            },
            "message": {
                "type": ["Resource", "string"],
                "description": "弹窗内容。",
                "required": True
            },
            "autoCancel": {
                "type": "boolean",
                "description": "点击遮障层时，是否关闭弹窗。",
                "default": True,
                "required": False
            },
            "confirm": {
                "type": "object",
                "description": "确认Button的使能状态、默认焦点、按钮风格、文本内容和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。默认响应Enter键能力在defaultFocus为true时不生效。",
                "properties": {
                    "enabled": {
                        "type": "boolean",
                        "description": "点击Button是否响应，true表示Button可以响应，false表示Button不可以响应。",
                        "default": True
                    },
                    "defaultFocus": {
                        "type": "boolean",
                        "description": "设置Button是否是默认焦点，true表示Button是默认焦点，false表示Button不是默认焦点。",
                        "default": False
                    },
                    "style": {
                        "type": "DialogButtonStyle",
                        "description": "设置Button的风格样式。",
                        "default": "DialogButtonStyle.DEFAULT"
                    },
                    "value": {
                        "type": ["Resource", "string"],
                        "description": "Button文本内容。"
                    },
                    "action": {
                        "type": "function",
                        "description": "Button选中时的回调。"
                    }
                },
                "required": False
            },
            "cancel": {
                "type": "function",
                "description": "点击遮障层关闭dialog时的回调。",
                "required": False
            },
            "alignment": {
                "type": "DialogAlignment",
                "description": "弹窗在竖直方向上的对齐方式。",
                "default": "DialogAlignment.Bottom",
                "required": False
            },
            "offset": {
                "type": "object",
                "description": "弹窗相对alignment所在位置的偏移量。",
                "properties": {
                    "dx": {
                        "type": ["number", "string", "Resource"],
                        "description": "弹窗相对alignment所在位置的水平偏移量。"
                    },
                    "dy": {
                        "type": ["number", "string", "Resource"],
                        "description": "弹窗相对alignment所在位置的垂直偏移量。"
                    }
                },
                "default": {
                    "dx": 0,
                    "dy": "40vp"
                },
                "required": False
            },
            "sheets": {
                "type": "Array<SheetInfo>",
                "description": "设置选项内容，每个选择项支持设置图片、文本和选中的回调。",
                "required": True
            },
            "maskRect": {
                "type": "Rectangle",
                "description": "弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。",
                "default": {
                    "x": 0,
                    "y": 0,
                    "width": "100%",
                    "height": "100%"
                },
                "required": False
            },
            "showInSubWindow": {
                "type": "boolean",
                "description": "某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。",
                "default": False,
                "required": False
            },
            "isModal": {
                "type": "boolean",
                "description": "弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。",
                "default": True,
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "弹窗背板颜色。",
                "default": "Color.Transparent",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "弹窗背板模糊材质。",
                "default": "BlurStyle.COMPONENT_ULTRA_THICK",
                "required": False
            },
            "onWillDismiss": {
                "type": "Callback<DismissDialogAction>",
                "description": "交互式关闭回调函数。",
                "required": False
            },
            "cornerRadius": {
                "type": ["BorderRadiuses", "Dimension", "LocalizedBorderRadiuses"],
                "description": "设置背板的圆角半径。",
                "default": {
                    "topLeft": "32vp",
                    "topRight": "32vp",
                    "bottomLeft": "32vp",
                    "bottomRight": "32vp"
                },
                "required": False
            },
            "borderWidth": {
                "type": ["Dimension", "EdgeWidths", "LocalizedEdgeWidths"],
                "description": "设置弹窗背板的边框宽度。",
                "default": 0,
                "required": False
            },
            "borderColor": {
                "type": ["ResourceColor", "EdgeColors", "LocalizedEdgeColors"],
                "description": "设置弹窗背板的边框颜色。",
                "default": "Color.Black",
                "required": False
            },
            "borderStyle": {
                "type": ["BorderStyle", "EdgeStyles"],
                "description": "设置弹窗背板的边框样式。",
                "default": "BorderStyle.Solid",
                "required": False
            },
            "width": {
                "type": "Dimension",
                "description": "设置弹窗背板的宽度。",
                "required": False
            },
            "height": {
                "type": "Dimension",
                "description": "设置弹窗背板的高度。",
                "required": False
            },
            "shadow": {
                "type": ["ShadowOptions", "ShadowStyle"],
                "description": "设置弹窗背板的阴影。",
                "required": False
            },
            "transition": {
                "type": "TransitionEffect",
                "description": "设置弹窗显示和退出的过渡效果。",
                "required": False
            }
        }
    }
    ,

    "SheetInfo": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。",
        "properties": {
            "title": {
                "type": ["string", "Resource"],
                "description": "选项的文本内容。",
                "required": True
            },
            "icon": {
                "type": ["string", "Resource"],
                "description": "选项的图标，默认无图标显示。",
                "default": "无图标显示",
                "required": False
            },
            "action": {
                "type": "()=>void",
                "description": "选项选中的回调。",
                "required": True
            }
        }
    }
    ,

    "CustomDialogControllerOptions": {
        "type": "object",
        "description": "CustomDialogControllerOptions对象说明",
        "properties": {
            "builder": {
                "type": "CustomDialog",
                "description": "自定义弹窗内容构造器。若builder构造器使用回调函数作为入参，请注意使用this绑定问题，如build: custombuilder({ callback: ()=> {...}})。若在builder构造器中监听数据变化请使用@Link，其他方式如@Prop、@ObjectLink不适用此场景。",
                "required": True
            },
            "cancel": {
                "type": "() => void",
                "description": "返回、ESC键和点击遮障层弹窗退出时的回调。",
                "required": False
            },
            "autoCancel": {
                "type": "boolean",
                "description": "是否允许点击遮障层退出，true表示关闭弹窗。false表示不关闭弹窗。",
                "default": True,
                "required": False
            },
            "alignment": {
                "type": "DialogAlignment",
                "description": "弹窗在竖直方向上的对齐方式。",
                "default": "DialogAlignment.Default",
                "required": False
            },
            "offset": {
                "type": "Offset",
                "description": "弹窗相对alignment所在位置的偏移量。",
                "default": {"dx": 0, "dy": 0},
                "required": False
            },
            "customStyle": {
                "type": "boolean",
                "description": "弹窗容器样式是否自定义。设置false时（默认值）：1、圆角为32vp。2、未设置弹窗宽度高度：弹窗容器的宽度根据栅格系统自适应。高度自适应自定义的内容节点。3、设置弹窗宽度高度：弹窗容器的宽度不超过默认样式下的最大宽度（自定义节点设置100%的宽度），弹窗容器的高度不超过默认样式下的最大高度（自定义节点设置100%的高度）。设置为true：1、圆角为0，弹窗背景色为透明色。2、不支持设置弹窗宽度、高度、边框宽度、边框样式、边框颜色以及阴影宽度。",
                "default": False,
                "required": False
            },
            "gridCount": {
                "type": "number",
                "description": "弹窗宽度占栅格宽度的个数。默认为按照窗口大小自适应，异常值按默认值处理，最大栅格数为系统最大栅格数。",
                "required": False
            },
            "maskColor": {
                "type": "ResourceColor",
                "description": "自定义蒙层颜色。",
                "default": "0x33000000",
                "required": False
            },
            "maskRect": {
                "type": "Rectangle",
                "description": "弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。",
                "default": {"x": 0, "y": 0, "width": "100%", "height": "100%"},
                "required": False
            },
            "openAnimation": {
                "type": "AnimateParam",
                "description": "自定义设置弹窗弹出的动画效果相关参数。tempo默认值为1，当设置小于等于0的值时按默认值处理。iterations默认值为1，默认播放一次，设置为其他数值时按默认值处理。playMode控制动画播放模式，默认值为PlayMode.Normal，设置为其他数值时按照默认值处理。",
                "required": False
            },
            "closeAnimation": {
                "type": "AnimateParam",
                "description": "自定义设置弹窗关闭的动画效果相关参数。tempo默认值为1，当设置小于等于0的值时按默认值处理。iterations默认值为1，默认播放一次，设置为其他数值时按默认值处理。playMode控制动画播放模式，默认值为PlayMode.Normal，设置为其他数值时按照默认值处理。页面转场切换时，建议使用默认关闭动效。",
                "required": False
            },
            "showInSubWindow": {
                "type": "boolean",
                "description": "某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。",
                "default": False,
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "设置弹窗背板填充。如果同时设置了内容构造器的背景色，则backgroundColor会被内容构造器的背景色覆盖。",
                "default": "Color.Transparent",
                "required": False
            },
            "cornerRadius": {
                "type": ["BorderRadiuses", "Dimension"],
                "description": "设置背板的圆角半径。可分别设置4个圆角的半径。自定义弹窗默认的背板圆角半径为32vp，如果需要使用cornerRadius属性，请和borderRadius属性一起使用。",
                "default": {"topLeft": "32vp", "topRight": "32vp", "bottomLeft": "32vp", "bottomRight": "32vp"},
                "required": False
            },
            "isModal": {
                "type": "boolean",
                "description": "弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。",
                "default": True,
                "required": False
            },
            "onWillDismiss": {
                "type": "Callback<DismissDialogAction>",
                "description": "交互式关闭回调函数。当用户执行点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。在onWillDismiss回调中，不能再做onWillDismiss拦截。",
                "required": False
            },
            "borderWidth": {
                "type": ["Dimension", "EdgeWidths"],
                "description": "设置弹窗背板的边框宽度。可分别设置4个边框宽度。默认值：0。百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。",
                "default": 0,
                "required": False
            },
            "borderColor": {
                "type": ["ResourceColor", "EdgeColors"],
                "description": "设置弹窗背板的边框颜色。默认值：Color.Black。如果使用borderColor属性，需要和borderWidth属性一起使用。",
                "default": "Color.Black",
                "required": False
            },
            "borderStyle": {
                "type": ["BorderStyle", "EdgeStyles"],
                "description": "设置弹窗背板的边框样式。默认值：BorderStyle.Solid。如果使用borderStyle属性，需要和borderWidth属性一起使用。",
                "default": "BorderStyle.Solid",
                "required": False
            },
            "width": {
                "type": "Dimension",
                "description": "设置弹窗背板的宽度。弹窗宽度默认最大值：400vp。百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。",
                "required": False
            },
            "height": {
                "type": "Dimension",
                "description": "设置弹窗背板的高度。弹窗高度默认最大值：0.9 *（窗口高度 - 安全区域）。百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。",
                "required": False
            },
            "shadow": {
                "type": ["ShadowOptions", "ShadowStyle"],
                "description": "设置弹窗背板的阴影。当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "弹窗背板模糊材质。",
                "default": "BlurStyle.COMPONENT_ULTRA_THICK",
                "required": False
            }
        }
    }
    ,

    "CustomDialogController": {
        "type": "object",
        "description": "CustomDialogController仅在作为@CustomDialog和@Component struct的成员变量，且在@Component struct内部定义时赋值才有效，具体用法可看下方示例。",
        "properties": {
            "dialogController": {
                "type": ["CustomDialogController", "null"],
                "description": "CustomDialogController仅在作为@CustomDialog和@Component struct的成员变量，且在@Component struct内部定义时赋值才有效，具体用法可看下方示例。",
                "default": "new CustomDialogController(CustomDialogControllerOptions)",
                "required": True
            },
            "open": {
                "type": "function",
                "description": "显示自定义弹窗内容，允许多次使用，但如果弹框为SubWindow模式，则该弹框不允许再弹出SubWindow弹框。",
                "required": False
            },
            "close": {
                "type": "function",
                "description": "关闭显示的自定义弹窗，若已关闭，则不生效。",
                "required": False
            }
        }
    }
    ,

    "CalendarDialogOptions": {
        "type": "object",
        "description": "继承自CalendarOptions。",
        "properties": {
            "onAccept": {
                "type": "function",
                "description": "点击弹窗中的“确定”按钮时触发该回调。value：选中的日期值。",
                "required": False
            },
            "onCancel": {
                "type": "function",
                "description": "点击弹窗中的“取消”按钮时触发该回调。",
                "required": False
            },
            "onChange": {
                "type": "function",
                "description": "选择弹窗中日期使当前选中项改变时触发该回调。value：选中的日期值。",
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "弹窗背板颜色。",
                "default": "Color.Transparent",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "弹窗背板模糊材质。",
                "default": "BlurStyle.COMPONENT_ULTRA_THICK",
                "required": False
            },
            "acceptButtonStyle": {
                "type": "PickerDialogButtonStyle",
                "description": "设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。说明：acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。",
                "required": False
            },
            "cancelButtonStyle": {
                "type": "PickerDialogButtonStyle",
                "description": "设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。说明：acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。",
                "required": False
            },
            "onDidAppear": {
                "type": "function",
                "description": "弹窗弹出时的事件回调。说明：1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。",
                "required": False
            },
            "onDidDisappear": {
                "type": "function",
                "description": "弹窗消失时的事件回调。说明：1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。",
                "required": False
            },
            "onWillAppear": {
                "type": "function",
                "description": "弹窗显示动效前的事件回调。说明：1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。",
                "required": False
            },
            "onWillDisappear": {
                "type": "function",
                "description": "弹窗退出动效前的事件回调。说明：1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。",
                "required": False
            },
            "shadow": {
                "type": ["ShadowOptions", "ShadowStyle"],
                "description": "设置弹窗背板的阴影。当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM",
                "required": False
            }
        }
    }
    ,

    "CalendarPickerDialog": {
        "type": "object",
        "description": "定义日历选择器弹窗并弹出。",
        "properties": {
            "options": {
                "type": "CalendarDialogOptions",
                "description": "配置日历选择器弹窗的参数。",
                "required": False
            }
        }
    }
    ,

    "DatePickerDialog": {
        "type": "object",
        "description": "定义日期滑动选择器弹窗并弹出。",
        "properties": {
            "options": {
                "type": "DatePickerDialogOptions",
                "description": "配置日期选择器弹窗的参数。",
                "required": False
            }
        }
    }
    ,

    "DatePickerDialogOptions": {
        "type": "object",
        "description": "继承自DatePickerOptions。",
        "properties": {
            "lunar": {
                "type": "boolean",
                "description": "日期是否显示为农历，true表示显示农历，false表示不显示农历。",
                "default": False,
                "required": False
            },
            "showTime": {
                "type": "boolean",
                "description": "是否展示时间项，true表示显示时间，false表示不显示时间。",
                "default": False,
                "required": False
            },
            "useMilitaryTime": {
                "type": "boolean",
                "description": "展示时间是否为24小时制，true表示显示24小时制，false表示显示12小时制。当展示时间为12小时制时，上下午与小时无联动关系。",
                "default": False,
                "required": False
            },
            "lunarSwitch": {
                "type": "boolean",
                "description": "是否展示切换农历的开关，true表示展示开关，false表示不展示开关。",
                "default": False,
                "required": False
            },
            "disappearTextStyle": {
                "type": "PickerTextStyle",
                "description": "设置所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff182431",
                    "font": {
                        "size": "14fp",
                        "weight": "FontWeight.Regular"
                    }
                },
                "required": False
            },
            "textStyle": {
                "type": "PickerTextStyle",
                "description": "设置所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff182431",
                    "font": {
                        "size": "16fp",
                        "weight": "FontWeight.Regular"
                    }
                },
                "required": False
            },
            "selectedTextStyle": {
                "type": "PickerTextStyle",
                "description": "设置选中项的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff007dff",
                    "font": {
                        "size": "20vp",
                        "weight": "FontWeight.Medium"
                    }
                },
                "required": False
            },
            "acceptButtonStyle": {
                "type": "PickerDialogButtonStyle",
                "description": "设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。",
                "required": False
            },
            "cancelButtonStyle": {
                "type": "PickerDialogButtonStyle",
                "description": "设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。",
                "required": False
            },
            "alignment": {
                "type": "DialogAlignment",
                "description": "弹窗在竖直方向上的对齐方式。",
                "default": "DialogAlignment.Default",
                "required": False
            },
            "offset": {
                "type": "Offset",
                "description": "弹窗相对alignment所在位置的偏移量。",
                "default": {
                    "dx": 0,
                    "dy": 0
                },
                "required": False
            },
            "maskRect": {
                "type": "Rectangle",
                "description": "弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。",
                "default": {
                    "x": 0,
                    "y": 0,
                    "width": "100%",
                    "height": "100%"
                },
                "required": False
            },
            "onAccept": {
                "type": "function",
                "description": "点击弹窗中的“确定”按钮时触发该回调。从API version 8 开始支持，从 API version 10 开始废弃，建议使用onDateAccept。",
                "required": False
            },
            "onCancel": {
                "type": "function",
                "description": "点击弹窗中的“取消”按钮时触发该回调。",
                "required": False
            },
            "onChange": {
                "type": "function",
                "description": "滑动弹窗中的滑动选择器使当前选中项改变时触发该回调。从API version 8 开始支持，从 API version 10 开始废弃，建议使用onDateChange。",
                "required": False
            },
            "onDateAccept": {
                "type": "function",
                "description": "点击弹窗中的“确定”按钮时触发该回调。当showTime设置为true时，回调接口返回值value中时和分为选择器选择的时和分。否则，返回值value中时和分为系统时间的时和分。",
                "required": False
            },
            "onDateChange": {
                "type": "function",
                "description": "滑动弹窗中的滑动选择器使当前选中项改变时触发该回调。当showTime设置为true时，回调接口返回值value中时和分为选择器选择的时和分。否则，返回值value中时和分为系统时间的时和分。",
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "弹窗背板颜色。",
                "default": "Color.Transparent",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "弹窗背板模糊材质。",
                "default": "BlurStyle.COMPONENT_ULTRA_THICK",
                "required": False
            },
            "onDidAppear": {
                "type": "function",
                "description": "弹窗弹出时的事件回调。正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。当弹窗入场动效未完成时关闭弹窗，该回调不会触发。",
                "required": False
            },
            "onDidDisappear": {
                "type": "function",
                "description": "弹窗消失时的事件回调。正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。",
                "required": False
            },
            "onWillAppear": {
                "type": "function",
                "description": "弹窗显示动效前的事件回调。正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。",
                "required": False
            },
            "onWillDisappear": {
                "type": "function",
                "description": "弹窗退出动效前的事件回调。正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。",
                "required": False
            },
            "shadow": {
                "type": ["ShadowOptions", "ShadowStyle"],
                "description": "设置弹窗背板的阴影。当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM",
                "required": False
            },
            "dateTimeOptions": {
                "type": "DateTimeOptions",
                "description": "设置时分是否显示前置0，目前只支持设置hour和minute参数。hour: 24小时制默认为\"2-digit\"，即有前置0；12小时制默认为\"numeric\"，即没有前置0。minute: 默认为\"2-digit\"，即有前置0。",
                "default": {
                    "hour": "24小时制默认为\"2-digit\"，即有前置0；12小时制默认为\"numeric\"，即没有前置0。",
                    "minute": "默认为\"2-digit\"，即有前置0。"
                },
                "required": False
            }
        }
    }
    ,

    "TimePickerDialog": {
        "type": "object",
        "description": "定义时间滑动选择器弹窗并弹出。",
        "properties": {
            "options": {
                "type": "TimePickerDialogOptions",
                "description": "配置时间选择器弹窗的参数。",
                "required": False
            }
        }
    }
    ,

    "TimePickerDialogOptions": {
        "type": "object",
        "description": "继承自TimePickerOptions。",
        "properties": {
            "useMilitaryTime": {
                "type": "boolean",
                "description": "展示时间是否为24小时制，默认为12小时制。当展示时间为12小时制时，上下午与小时无联动关系。",
                "default": False,
                "required": False
            },
            "disappearTextStyle": {
                "type": "PickerTextStyle",
                "description": "设置所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff182431",
                    "font": {
                        "size": "14fp",
                        "weight": "FontWeight.Regular"
                    }
                },
                "required": False
            },
            "textStyle": {
                "type": "PickerTextStyle",
                "description": "设置所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff182431",
                    "font": {
                        "size": "16fp",
                        "weight": "FontWeight.Regular"
                    }
                },
                "required": False
            },
            "selectedTextStyle": {
                "type": "PickerTextStyle",
                "description": "设置选中项的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff007dff",
                    "font": {
                        "size": "20vp",
                        "weight": "FontWeight.Medium"
                    }
                },
                "required": False
            },
            "acceptButtonStyle": {
                "type": "PickerDialogButtonStyle",
                "description": "设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。",
                "required": False
            },
            "cancelButtonStyle": {
                "type": "PickerDialogButtonStyle",
                "description": "设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。",
                "required": False
            },
            "alignment": {
                "type": "DialogAlignment",
                "description": "弹窗在竖直方向上的对齐方式。",
                "default": "DialogAlignment.Default",
                "required": False
            },
            "offset": {
                "type": "Offset",
                "description": "弹窗相对alignment所在位置的偏移量。",
                "default": {
                    "dx": 0,
                    "dy": 0
                },
                "required": False
            },
            "maskRect": {
                "type": "Rectangle",
                "description": "弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。",
                "default": {
                    "x": 0,
                    "y": 0,
                    "width": "100%",
                    "height": "100%"
                },
                "required": False
            },
            "onAccept": {
                "type": "function",
                "description": "点击弹窗中的“确定”按钮时触发该回调。",
                "required": False
            },
            "onCancel": {
                "type": "function",
                "description": "点击弹窗中的“取消”按钮时触发该回调。",
                "required": False
            },
            "onChange": {
                "type": "function",
                "description": "滑动弹窗中的选择器使当前选中时间改变时触发该回调。",
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "弹窗背板颜色。",
                "default": "Color.Transparent",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "弹窗背板模糊材质。",
                "default": "BlurStyle.COMPONENT_ULTRA_THICK",
                "required": False
            },
            "onDidAppear": {
                "type": "function",
                "description": "弹窗弹出时的事件回调。正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。当弹窗入场动效未完成时关闭弹窗，该回调不会触发。",
                "required": False
            },
            "onDidDisappear": {
                "type": "function",
                "description": "弹窗消失时的事件回调。正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。",
                "required": False
            },
            "onWillAppear": {
                "type": "function",
                "description": "弹窗显示动效前的事件回调。正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。",
                "required": False
            },
            "onWillDisappear": {
                "type": "function",
                "description": "弹窗退出动效前的事件回调。正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。",
                "required": False
            },
            "shadow": {
                "type": ["ShadowOptions", "ShadowStyle"],
                "description": "设置弹窗背板的阴影。当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM",
                "required": False
            },
            "dateTimeOptions": {
                "type": "DateTimeOptions",
                "description": "设置时分是否显示前置0，目前只支持设置hour和minute参数。hour: 24小时制默认为\"2-digit\"，即有前置0；12小时制默认为\"numeric\"，即没有前置0。minute: 默认为\"2-digit\"，即有前置0。",
                "default": {
                    "hour": "2-digit",
                    "minute": "2-digit"
                },
                "required": False
            }
        }
    },

    "TextPickerDialog.show": {
        "type": "object",
        "description": "定义文本滑动选择器弹窗并弹出。",
        "properties": {
            "options": {
                "type": "TextPickerDialogOptions",
                "description": "配置文本选择器弹窗的参数。",
                "required": False
            }
        }
    }
    ,

    "TextPickerDialogOptions": {
        "type": "object",
        "description": "文本选择器弹窗的参数继承自TextPickerOptions。",
        "properties": {
            "defaultPickerItemHeight": {
                "type": ["number", "string"],
                "description": "设置选择器中选项的高度。",
                "default": "选中项56vp，非选中项36vp。设置该参数后，选中项与非选中项的高度均为所设置的值。",
                "required": False
            },
            "disappearTextStyle": {
                "type": "PickerTextStyle",
                "description": "设置所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff182431",
                    "font": {
                        "size": "14fp",
                        "weight": "FontWeight.Regular"
                    }
                },
                "required": False
            },
            "textStyle": {
                "type": "PickerTextStyle",
                "description": "设置所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff182431",
                    "font": {
                        "size": "16fp",
                        "weight": "FontWeight.Regular"
                    }
                },
                "required": False
            },
            "selectedTextStyle": {
                "type": "PickerTextStyle",
                "description": "设置选中项的文本颜色、字号、字体粗细。",
                "default": {
                    "color": "#ff007dff",
                    "font": {
                        "size": "20vp",
                        "weight": "FontWeight.Medium"
                    }
                },
                "required": False
            },
            "acceptButtonStyle": {
                "type": "PickerDialogButtonStyle",
                "description": "设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。",
                "required": False
            },
            "cancelButtonStyle": {
                "type": "PickerDialogButtonStyle",
                "description": "设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。",
                "required": False
            },
            "canLoop": {
                "type": "boolean",
                "description": "设置是否可循环滚动，true：可循环，false：不可循环。",
                "default": True,
                "required": False
            },
            "alignment": {
                "type": "DialogAlignment",
                "description": "弹窗在竖直方向上的对齐方式。",
                "default": "DialogAlignment.Default",
                "required": False
            },
            "offset": {
                "type": "Offset",
                "description": "弹窗相对alignment所在位置的偏移量。",
                "default": {
                    "dx": 0,
                    "dy": 0
                },
                "required": False
            },
            "maskRect": {
                "type": "Rectangle",
                "description": "弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。",
                "default": {
                    "x": 0,
                    "y": 0,
                    "width": "100%",
                    "height": "100%"
                },
                "required": False
            },
            "onAccept": {
                "type": "function",
                "description": "点击弹窗中的“确定”按钮时触发该回调。",
                "required": False
            },
            "onCancel": {
                "type": "function",
                "description": "点击弹窗中的“取消”按钮时触发该回调。",
                "required": False
            },
            "onChange": {
                "type": "function",
                "description": "滑动弹窗中的选择器使当前选中项改变时触发该回调。",
                "required": False
            },
            "backgroundColor": {
                "type": "ResourceColor",
                "description": "弹窗背板颜色。",
                "default": "Color.Transparent",
                "required": False
            },
            "backgroundBlurStyle": {
                "type": "BlurStyle",
                "description": "弹窗背板模糊材质。",
                "default": "BlurStyle.COMPONENT_ULTRA_THICK",
                "required": False
            },
            "onDidAppear": {
                "type": "function",
                "description": "弹窗弹出时的事件回调。",
                "required": False
            },
            "onDidDisappear": {
                "type": "function",
                "description": "弹窗消失时的事件回调。",
                "required": False
            },
            "onWillAppear": {
                "type": "function",
                "description": "弹窗显示动效前的事件回调。",
                "required": False
            },
            "onWillDisappear": {
                "type": "function",
                "description": "弹窗退出动效前的事件回调。",
                "required": False
            },
            "shadow": {
                "type": ["ShadowOptions", "ShadowStyle"],
                "description": "设置弹窗背板的阴影。",
                "required": False
            }
        }
    }
    ,

    "TextPickerResult": {
        "type": "object",
        "description": "TextPickerResult对象说明",
        "properties": {
            "value": {
                "type": ["string", "string[]"],
                "description": "选中项的文本内容。当显示文本或图片加文本列表时，value值为选中项中的文本值。（文本选择器显示多列时，value为数组类型。）当显示图片列表时，value值为空。value值不支持包含转义字符'\\'。",
                "required": True
            },
            "index": {
                "type": ["number", "number[]"],
                "description": "选中项在选择范围数组中的索引值。（文本选择器显示多列时，index为数组类型。）",
                "required": True
            }
        }
    }
    ,

    "LocationIconStyle": {
        "type": "enum",
        "enum": ["FULL_FILLED", "LINES"],
        "description": "位置按钮展示不同样式的图标。",
        "enumDescriptions": {
            "FULL_FILLED": "位置按钮展示填充样式图标。",
            "LINES": "位置按钮展示线条样式图标。"
        }
    }
    ,

    "LocationDescription": {
        "type": "enum",
        "enum": [
            "CURRENT_LOCATION",
            "ADD_LOCATION",
            "SELECT_LOCATION",
            "SHARE_LOCATION",
            "SEND_LOCATION",
            "LOCATING",
            "LOCATION",
            "SEND_CURRENT_LOCATION",
            "RELOCATION",
            "PUNCH_IN",
            "CURRENT_POSITION"
        ],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "CURRENT_LOCATION": "位置按钮的文字描述为“当前位置”。",
            "ADD_LOCATION": "位置按钮的文字描述为“添加位置”。",
            "SELECT_LOCATION": "位置按钮的文字描述为“选择位置”。",
            "SHARE_LOCATION": "位置按钮的文字描述为“共享位置”。",
            "SEND_LOCATION": "位置按钮的文字描述为“发送位置”。",
            "LOCATING": "位置按钮的文字描述为“定位”。",
            "LOCATION": "位置按钮的文字描述为“位置”。",
            "SEND_CURRENT_LOCATION": "位置按钮的文字描述为“发送实时位置”。",
            "RELOCATION": "位置按钮的文字描述为“重定位”。",
            "PUNCH_IN": "位置按钮的文字描述为“打卡定位”。",
            "CURRENT_POSITION": "位置按钮的文字描述为“所在位置”。"
        }
    }
    ,

    "LocationButtonOnClickResult": {
        "type": "enum",
        "enum": ["SUCCESS", "TEMPORARY_AUTHORIZATION_FAILED"],
        "description": "位置按钮点击结果的枚举类",
        "enumDescriptions": {
            "SUCCESS": "位置按钮点击成功",
            "TEMPORARY_AUTHORIZATION_FAILED": "位置按钮点击后位置权限授权失败"
        }
    }
    ,

    "PasteIconStyle": {
        "type": "enum",
        "enum": ["LINES"],
        "description": "粘贴按钮展示线条样式图标。",
        "enumDescriptions": {
            "LINES": "粘贴按钮展示线条样式图标。"
        }
    }
    ,

    "PasteDescription": {
        "type": "enum",
        "enum": ["PASTE"],
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力： SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "PASTE": "粘贴按钮的文字描述为“粘贴”。"
        }
    }
    ,

    "PasteButtonOnClickResult": {
        "type": "enum",
        "enum": ["SUCCESS", "TEMPORARY_AUTHORIZATION_FAILED"],
        "description": "该枚举类用于表示粘贴按钮点击后的结果",
        "enumDescriptions": {
            "SUCCESS": "粘贴按钮点击成功",
            "TEMPORARY_AUTHORIZATION_FAILED": "粘贴按钮点击后权限授权失败"
        }
    }
    ,

    "SaveIconStyle": {
        "type": "enum",
        "enum": ["FULL_FILLED", "LINES"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "FULL_FILLED": "保存按钮展示填充样式图标。",
            "LINES": "保存按钮展示线条样式图标。"
        }
    }
    ,

    "SaveDescription": {
        "type": "enum",
        "enum": ["DOWNLOAD", "DOWNLOAD_FILE", "SAVE", "SAVE_IMAGE", "SAVE_FILE", "DOWNLOAD_AND_SHARE", "RECEIVE",
                 "CONTINUE_TO_RECEIVE", "SAVE_TO_GALLERY"],
        "description": "该枚举类的描述信息",
        "enumDescriptions": {
            "DOWNLOAD": "保存按钮的文字描述为“下载”。",
            "DOWNLOAD_FILE": "保存按钮的文字描述为“下载文件”。",
            "SAVE": "保存按钮的文字描述为“保存”。",
            "SAVE_IMAGE": "保存按钮的文字描述为“保存图片”。",
            "SAVE_FILE": "保存按钮的文字描述为“保存文件”。",
            "DOWNLOAD_AND_SHARE": "保存按钮的文字描述为“下载分享”。",
            "RECEIVE": "保存按钮的文字描述为“接收”。",
            "CONTINUE_TO_RECEIVE": "保存按钮的文字描述为“继续接收”。",
            "SAVE_TO_GALLERY": "保存按钮的文字描述为“保存至图库”。"
        }
    },
    "SaveButtonOnClickResult": {
        "type": "enum",
        "enum": ["SUCCESS", "TEMPORARY_AUTHORIZATION_FAILED"],
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "enumDescriptions": {
            "SUCCESS": "保存按钮点击成功。",
            "TEMPORARY_AUTHORIZATION_FAILED": "保存按钮点击后权限授权失败。"
        }
    },
    "IndicatorStyle": {
        "type": "object",
        "description": "从API version 11开始，该接口支持在元服务中使用。系统能力：SystemCapability.ArkUI.ArkUI.Full",
        "properties": {
            "color": {
                "type": "ResourceColor",
                "description": "下划线的颜色和背板颜色。",
                "default": "#FF007DFF",
                "required": False
            },
            "height": {
                "type": "Length",
                "description": "下划线的高度（不支持百分比设置）。",
                "default": "2.0",
                "required": False
            },
            "width": {
                "type": "Length",
                "description": "下划线的宽度（不支持百分比设置）。宽度设置为0时，按页签文本宽度显示。",
                "default": "0.0",
                "required": False
            },
            "borderRadius": {
                "type": "Length",
                "description": "下划线的圆角半径（不支持百分比设置）。",
                "default": "0.0",
                "required": False
            },
            "marginTop": {
                "type": "Length",
                "description": "下划线与文字的间距（不支持百分比设置）。",
                "default": "8.0",
                "required": False
            }
        }
    },
    "SelectedMode": {
        "type": "enum",
        "description": "选中子页签的显示方式。",
        "enum": ["INDICATOR", "BOARD"],
        "enumDescriptions": {
            "INDICATOR": "使用下划线模式。",
            "BOARD": "使用背板模式。"
        }
    }
}
