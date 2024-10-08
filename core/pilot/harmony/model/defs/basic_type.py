BASIC_TYPE = {
    "Resource": {
        "type": "Resource",
        "description": "资源引用类型，用于设置组件属性的值。可以通过$r或者$rawfile创建Resource类型对象，不可以修改Resource中的各属性的值。",
        "examples": [
            "```ets\n// belonging：系统资源或者应用资源，相应的取值为'sys'和'app'；\n// type：资源类型，支持'boolean'、'color'、'float'、'intarray'、'integer'、'pattern'、'plural'、'strarray'、'string'、'media'；\n// name：资源名称，在资源定义时确定。\n$r('belonging.type.name')\n```",
            "```ets\n// filename：工程中resources/rawfile目录下的文件名称。\n$rawfile('filename')\n```"
        ]
    },
    "Length": {
        "type": ["string", "number", "Resource"],
        "description": "长度类型，用于描述尺寸单位。\n* string：需要显式指定像素单位，如'10px'，或百分比字符串，如'100%'。\n* number：默认单位为vp。\n* Resource：资源引用类型，引入系统或应用资源中的尺寸。"
    },
    "Padding": {
        "type": "object",
        "description": "内边距类型，描述组件不同方向的内边距。",
        "properties": {
            "top": {"type": "Length", "description": "上内边距，组件内元素距组件顶部的尺寸。"},
            "right": {"type": "Length", "description": "左内边距，组件内元素距组件左侧的尺寸。"},
            "bottom": {"type": "Length", "description": "右内边距，组件内元素距组件右侧的尺寸。"},
            "left": {"type": "Length", "description": "下内边距，组件内元素距组件底部的尺寸。"}
        }
    },
    "LengthMetrics": {
        "type": "object",
        "description": "用于设置长度属性，当长度单位为PERCENT时，值为1表示100%。",
        "properties": {
            "value": {
                "type": "number",
                "description": "长度属性的值。"
            },
            "unit": {
                "type": "LengthUnit",
                "description": "长度属性的单位，默认为vp。"
            }
        }
    },
    "LengthUnit": {
        "type": "enum",
        "enum": ["PX", "VP", "FP", "PERCENT", "LPX"],
        "description": "长度属性单位枚举。",
        "enumDescriptions": {
            "PX": "长度类型，用于描述以px像素单位为单位的长度。",
            "VP": "长度类型，用于描述以vp逻辑像素为单位的长度。",
            "FP": "长度类型，用于描述以fp字体像素为单位的长度。",
            "PERCENT": "长度类型，用于描述百分比长度。",
            "LPX": "长度类型，用于描述以lpx逻辑像素为单位的长度。"
        }
    },
    "ResourceStr": {
        "type": ["string", "Resource"],
        "description": "字符串类型，用于描述字符串入参可以使用的类型。\n* string：字符串类型。\n* Resource：资源引用类型，引入系统资源或者应用资源中的字符串。"
    },
    "LocalizedPadding": {
        "type": "object",
        "description": "内边距类型，用于描述组件不同方向的内边距。",
        "properties": {
            "top": {
                "type": "LengthMetrics",
                "description": "上内边距，组件内元素距组件顶部的尺寸。"
            },
            "bottom": {
                "type": "LengthMetrics",
                "description": "下内边距，组件内元素距组件底部的尺寸。"
            },
            "start": {
                "type": "LengthMetrics",
                "description": "左内边距，组件内元素距组件左边界的尺寸，从右至左显示语言模式下为右内边距，组件内元素距组件右边界的尺寸。"
            },
            "end": {
                "type": "LengthMetrics",
                "description": "右内边距，组件内元素距组件右边界的尺寸，从右至左显示语言模式下为左内边距，组件内元素距组件左边界的尺寸。"
            }
        }
    },
    "Margin": {
        "type": "object",
        "description": "外边距类型，用于描述组件不同方向的外边距。",
        "properties": {
            "top": {
                "type": "Length",
                "description": "上外边距，组件距其父组件顶部的尺寸。"
            },
            "left": {
                "type": "Length",
                "description": "左外边距，组件距其父组件左侧的尺寸。"
            },
            "right": {
                "type": "Length",
                "description": "右外边距，组件距其父组件右侧的尺寸。"
            },
            "bottom": {
                "type": "Length",
                "description": "下外边距，组件距其父组件底部的尺寸。"
            }
        }
    },
    "LocalizedMargin": {
        "type": "object",
        "description": "外边距类型，用于描述组件不同方向的外边距。",
        "properties": {
            "top": {
                "type": "LengthMetrics",
                "description": "上外边距，组件距其父组件顶部的尺寸。"
            },
            "bottom": {
                "type": "LengthMetrics",
                "description": "下外边距，组件距其父组件底部的尺寸。"
            },
            "start": {
                "type": "LengthMetrics",
                "description": "左外边距，组件距其父组件左边界的尺寸，从右至左显示语言模式下为右外边距，组件距其父组件右边界的尺寸。"
            },
            "end": {
                "type": "LengthMetrics",
                "description": "右外边距，组件距其父组件右边界的尺寸，从右至左显示语言模式下为左外边距，组件距其父组件左边界的尺寸。"
            }
        }
    },
    "EdgeWidths": {
        "type": "object",
        "description": "边框宽度类型，用于描述组件边框不同方向的宽度。",
        "properties": {
            "top": {
                "type": "Length",
                "description": "组件上边框宽度。"
            },
            "left": {
                "type": "Length",
                "description": "组件左边框宽度。"
            },
            "right": {
                "type": "Length",
                "description": "组件右边框宽度。"
            },
            "bottom": {
                "type": "Length",
                "description": "组件下边框宽度。"
            }
        }
    },
    "LocalizedEdgeWidths": {
        "type": "object",
        "description": "边框宽度类型，用于描述组件边框不同方向的宽度。",
        "properties": {
            "top": {
                "type": "LengthMetrics",
                "description": "组件上边框宽度。"
            },
            "bottom": {
                "type": "LengthMetrics",
                "description": "组件下边框宽度。"
            },
            "start": {
                "type": "LengthMetrics",
                "description": "组件左边框宽度，从右至左显示语言模式下为组件右边框宽度。"
            },
            "end": {
                "type": "LengthMetrics",
                "description": "组件右边框宽度，从右至左显示语言模式下为组件左边框宽度。"
            }
        }
    },
    "BorderRadiuses": {
        "type": "object",
        "description": "圆角类型，用于描述组件边框圆角半径。",
        "properties": {
            "topLeft": {
                "type": "Length",
                "description": "组件左上角圆角半径。"
            },
            "topRight": {
                "type": "Length",
                "description": "组件右上角圆角半径。"
            },
            "bottomLeft": {
                "type": "Length",
                "description": "组件左下角圆角半径。"
            },
            "bottomRight": {
                "type": "Length",
                "description": "组件右下角圆角半径。"
            }
        }
    },
    "LocalizedBorderRadiuses": {
        "type": "object",
        "description": "圆角类型，用于描述组件边框圆角半径。",
        "properties": {
            "topStart": {
                "type": "LengthMetrics",
                "description": "组件左上角圆角半径。从右至左显示语言模式下为组件右上角圆角半径。"
            },
            "topEnd": {
                "type": "LengthMetrics",
                "description": "组件右上角圆角半径。从右至左显示语言模式下为组件左上角圆角半径。"
            },
            "bottomStart": {
                "type": "LengthMetrics",
                "description": "组件左下角圆角半径。从右至左显示语言模式下为组件右下角圆角半径。"
            },
            "bottomEnd": {
                "type": "LengthMetrics",
                "description": "组件右下角圆角半径。从右至左显示语言模式下为组件左下角圆角半径。"
            }
        }
    },
    "EdgeColors": {
        "type": "object",
        "description": "边框颜色，用于描述组件边框四条边的颜色。",
        "properties": {
            "top": {
                "type": "ResourceColor",
                "description": "组件上边框颜色。"
            },
            "left": {
                "type": "ResourceColor",
                "description": "组件左边框颜色。"
            },
            "right": {
                "type": "ResourceColor",
                "description": "组件右边框颜色。"
            },
            "bottom": {
                "type": "ResourceColor",
                "description": "组件下边框颜色。"
            }
        }
    },
    "LocalizedEdgeColors": {
        "type": "object",
        "description": "边框颜色，用于描述组件边框四条边的颜色。",
        "properties": {
            "top": {
                "type": "ResourceColor",
                "description": "组件上边框颜色。"
            },
            "bottom": {
                "type": "ResourceColor",
                "description": "组件下边框颜色。"
            },
            "start": {
                "type": "ResourceColor",
                "description": "组件左边框颜色，从右至左显示语言模式下为组件右边框颜色。"
            },
            "end": {
                "type": "ResourceColor",
                "description": "组件右边框颜色，从右至左显示语言模式下为组件左边框颜色。"
            }
        }
    },
    "EdgeStyles": {
        "type": "object",
        "description": "边框样式，用于描述组件边框四条边的样式。",
        "properties": {
            "top": {
                "type": "BorderStyle",
                "description": "组件上边框样式。"
            },
            "left": {
                "type": "BorderStyle",
                "description": "组件左边框样式。"
            },
            "right": {
                "type": "BorderStyle",
                "description": "组件右边框样式。"
            },
            "bottom": {
                "type": "BorderStyle",
                "description": "组件下边框样式。"
            }
        }
    },
    "Offset": {
        "type": "object",
        "description": "相对布局完成位置坐标偏移量。",
        "properties": {
            "dx": {
                "type": "Length",
                "required": True,
                "description": "水平方向偏移量。"
            },
            "dy": {
                "type": "Length",
                "required": True,
                "description": "竖直方向偏移量。"
            }
        }
    },
    "RectResult": {
        "type": "object",
        "description": "位置和尺寸类型，用于描述组件的位置和宽高。",
        "properties": {
            "x": {
                "type": "number",
                "description": "水平方向横坐标。"
            },
            "y": {
                "type": "number",
                "description": "竖直方向纵坐标。"
            },
            "width": {
                "type": "number",
                "description": "内容宽度大小。"
            },
            "height": {
                "type": "number",
                "description": "内容高度大小。"
            }
        }
    },
    "ResourceColor": {
        "type": ["string", "Resource", "Color", "number"],
        "description": "颜色类型，用于描述资源颜色类型。\n* string：rgb或者argb格式颜色。示例：'#ffffff', '#ff000000', 'rgb(255, 100, 255)', 'rgba(255, 100, 255, 0.5)'。\n* Resource：资源引用类型，引入系统资源或者应用资源中的颜色。\n* Color: 颜色枚举值。\n* number: HEX格式颜色，支持rgb或者argb。示例：0xffffff，0xffff0000。number无法识别传入位数，格式选择依据值的大小，例如0x00ffffff作rgb格式解析"
    },
    "ColoringStrategy": {
        "type": "enum",
        "enum": ["INVERT", "AVERAGE", "PRIMARY"],
        "description": "智能取色枚举类型，用于设置前景色。",
        "enumDescriptions": {
            "INVERT": "设置前景色为控件背景色的反色。",
            "AVERAGE": "设置控件背景阴影色为控件背景阴影区域的平均色。",
            "PRIMARY": "设置控件背景阴影色为控件背景阴影区域的主色。"
        }
    },
    "LengthConstrain": {
        "type": "object",
        "description": "长度约束类型，用于描述组件的最小和最大尺寸。",
        "properties": {
            "minLength": {
                "type": "Length",
                "required": True,
                "description": "组件最小长度。"
            },
            "maxLength": {
                "type": "Length",
                "required": True,
                "description": "组件最大长度。"
            }
        }
    },
    "Font": {
        "type": "object",
        "description": "设置文本样式。",
        "properties": {
            "size": {
                "type": "Length",
                "description": "设置文本尺寸，Length为number类型时，使用fp单位。不支持设置百分比字符串。",
                "default": 16.0
            },
            "weight": {
                "type": ["FontWeight", "number", "string"],
                "description": "设置文本的字体粗细，number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。",
                "default": "400 | FontWeight.Normal"
            },
            "family": {
                "type": ["string", "Resource"],
                "description": "设置文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。"
            },
            "style": {
                "type": "FontStyle",
                "description": "设置文本的字体样式。",
                "default": "FontStyle.Normal"
            }
        }
    },
    "Area": {
        "type": "object",
        "description": "区域类型，用于描述组件的位置和尺寸。",
        "properties": {
            "position": {
                "type": "Position",
                "description": "目标元素左上角相对父元素左上角的位置。"
            },
            "globalPosition": {
                "type": "Position",
                "description": "目标元素左上角相对页面左上角的位置。"
            },
            "width": {
                "type": "Length",
                "description": "目标元素的宽度，作为返回值时，类型为number，单位vp。"
            },
            "height": {
                "type": "Length",
                "description": "目标元素的高度，作为返回值时，类型为number，单位vp。"
            }
        }
    },
    "Position": {
        "type": "object",
        "description": "位置类型，用于表示一个坐标点。",
        "properties": {
            "x": {
                "type": "Length",
                "description": "x轴坐标，作为返回值时，类型为number，单位vp。"
            },
            "y": {
                "type": "Length",
                "description": "y轴坐标，作为返回值时，类型为number，单位vp。"
            }
        }
    },
    "LocalizedPosition": {
        "type": "object",
        "description": "位置类型，用于表示一个坐标点。",
        "properties": {
            "start": {
                "type": "LengthMetrics",
                "description": "LTR模式时x轴相对左边坐标，RTL模式x轴相对右边坐标。"
            },
            "top": {
                "type": "LengthMetrics",
                "description": "y轴坐标。"
            }
        }
    },
    "Edges": {
        "type": "object",
        "description": "位置类型，表示相对四边的偏移量。同时设置top和bottom，仅top生效；同时设置left和right，仅left生效。",
        "properties": {
            "top": {
                "type": "Dimension",
                "description": "相对顶边的偏移量"
            },
            "left": {
                "type": "Dimension",
                "description": "相对左边的偏移量"
            },
            "right": {
                "type": "Dimension",
                "description": "相对右边的偏移量"
            },
            "bottom": {
                "type": "Dimension",
                "description": "相对底边的偏移量"
            }
        }
    },
    "LocalizedEdges": {
        "type": "object",
        "description": "位置类型，表示相对四边的偏移量。同时设置top和bottom，仅top生效；同时设置start和end，仅start生效。",
        "properties": {
            "top": {
                "type": "LengthMetrics",
                "description": "相对顶边的偏移量。"
            },
            "bottom": {
                "type": "LengthMetrics",
                "description": "相对底边的偏移量。"
            },
            "start": {
                "type": "LengthMetrics",
                "description": "LTR模式时相对左边的偏移量，RTL模式时相对右边的偏移量。"
            },
            "end": {
                "type": "LengthMetrics",
                "description": "LTR模式时相对右边的偏移量，RTL模式时相对左边的偏移量。"
            }
        }
    },
    "ConstraintSizeOptions": {
        "type": "object",
        "description": "设置约束尺寸，组件布局时，进行尺寸范围限制。",
        "properties": {
            "minWidth": {
                "type": "Length",
                "description": "组件最小宽度。"
            },
            "maxWidth": {
                "type": "Length",
                "description": "组件最大宽度。"
            },
            "minHeight": {
                "type": "Length",
                "description": "组件最小高度。"
            },
            "maxHeight": {
                "type": "Length",
                "description": "组件最大高度。"
            }
        }
    },
    "SizeOptions": {
        "type": "object",
        "description": "设置宽高尺寸。",
        "properties": {
            "width": {
                "type": "Length",
                "description": "元素宽度。"
            },
            "height": {
                "type": "Length",
                "description": "元素高度。"
            }
        }
    },
    "BorderOptions": {
        "type": "object",
        "description": "边框属性集合，用于描述边框相关信息。",
        "properties": {
            "width": {
                "type": ["Length", "EdgeWidths", "LocalizedEdgeWidths"],
                "description": "边框宽度。"
            },
            "color": {
                "type": ["ResourceColor", "EdgeColors"],
                "description": "边框颜色。"
            },
            "style": {
                "type": ["BorderStyle", "EdgeStyles"],
                "description": "边框样式。"
            },
            "radius": {
                "type": ["Length", "BorderRadiuses"],
                "description": "边框圆角半径。"
            }
        }
    },
    "ColorFilter": {
        "type": "object",
        "description": "创建具有4*5矩阵的颜色过滤器。",
        "properties": {
            "constructor": {
                "type": "number[]",
                "required": True,
                "description": "创建具有4*5矩阵的颜色过滤器, 入参为[m*n]位于m行和n列中矩阵值, 矩阵是行优先的。"
            }
        }
    },
    "CustomBuilder": {
        "type": "object",
        "description": "组件属性方法参数可使用CustomBuilder类型来自定义UI描述。",
        "properties": {
            "CustomBuilder": {
                "type": "() => any | void",
                "description": "生成用户自定义组件，在使用时结合@Builder使用。"
            }
        }
    },
    "PixelStretchEffectOptions": {
        "type": "object",
        "description": "像素扩展属性集合,用于描述像素扩展的信息。",
        "properties": {
            "left": {
                "type": "Length",
                "description": "组件图像左边沿像素扩展距离。"
            },
            "right": {
                "type": "Length",
                "description": "组件图像右边沿像素扩展距离。"
            },
            "top": {
                "type": "Length",
                "description": "组件图像上边沿像素扩展距离。"
            },
            "bottom": {
                "type": "Length",
                "description": "组件图像下边沿像素扩展距离。"
            }
        }
    },
    "ModalTransition": {
        "type": "enum",
        "enum": ["NONE", "DEFAULT", "ALPHA"],
        "description": "全屏模态转场方式枚举类型，用于设置全屏模态转场类型。",
        "enumDescriptions": {
            "NONE": "无转场效果",
            "DEFAULT": "默认转场效果",
            "ALPHA": "透明度转场效果"
        }
    },
    "Dimension": {
        "type": "enum",
        "enum": ["PX", "VP", "FP", "LPX", "PERCENT", "Resource"],
        "description": "长度类型，用于描述尺寸单位。",
        "enumDescriptions": {
            "PX": "需要指定以px像素单位，如'10px'。",
            "VP": "需要指定数字或vp像素单位，如10或'10vp'。",
            "FP": "需要指定以fp像素单位，如'10fp'。",
            "LPX": "需要指定以lpx像素单位，如'10lpx'。",
            "PERCENT": "需要指定以%像素单位，如'10%'。",
            "Resource": "资源引用类型，引入系统资源或者应用资源中的尺寸。"
        }
    },
    "PX": {
        "type": "string",
        "description": "{number}px, 需要指定以px像素单位，如'10px'。"
    },
    "VP": {
        "type": ["string", "number"],
        "description": "{number}vp|number, 需要指定数字或vp像素单位，如10或'10vp'。"
    },
    "FP": {
        "type": "string",
        "description": "{number}fp, 需要指定以fp像素单位，如'10fp'。"
    },
    "LPX": {
        "type": "string",
        "description": "{number}lpx, 需要指定以lpx像素单位，如'10lpx'。"
    },
    "Percentage": {
        "type": "string",
        "description": "{number}%, 需要指定以%像素单位，如'10%'。"
    },
    "Degree": {
        "type": "number",
        "description": "{number}deg，需要指定以deg像素单位，如'10deg'。"
    },
    "MultiShadowOptions": {
        "type": "object",
        "description": "投影样式。",
        "properties": {
            "radius": {
                "type": ["number", "Resource"],
                "description": "投影模糊半径，单位为vp。",
                "default": 20
            },
            "offsetX": {
                "type": ["number", "Resource"],
                "description": "X轴的偏移量，单位为vp。",
                "default": 5
            },
            "offsetY": {
                "type": ["number", "Resource"],
                "description": "Y轴的偏移量，单位为vp。",
                "default": 5
            }
        }
    },
    "SwiperAnimationEvent": {
        "type": "object",
        "description": "Swiper组件动画相关信息集合。",
        "properties": {
            "currentOffset": {
                "type": "number",
                "required": True,
                "description": "Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移，单位vp。",
                "default": 0
            },
            "targetOffset": {
                "type": "number",
                "required": True,
                "description": "Swiper动画目标元素在主轴方向上，相对于Swiper起始位置的位移，单位vp。",
                "default": 0
            },
            "velocity": {
                "type": "number",
                "required": True,
                "description": "Swiper离手动画开始时的离手速度。单位vp/s",
                "default": 0
            }
        }
    },
    "TabsAnimationEvent": {
        "type": "object",
        "description": "Tabs组件动画相关信息集合。",
        "properties": {
            "currentOffset": {
                "type": "number",
                "required": True,
                "description": "Tabs当前显示元素在主轴方向上，相对于Tabs起始位置的位移，单位vp。",
                "default": 0
            },
            "targetOffset": {
                "type": "number",
                "required": True,
                "description": "Tabs动画目标元素在主轴方向上，相对于Tabs起始位置的位移，单位vp。",
                "default": 0
            },
            "velocity": {
                "type": "number",
                "required": True,
                "description": "Tabs离手动画开始时的离手速度。单位vp/s",
                "default": 0
            }
        }
    },
    "SafeAreaType": {
        "type": "enum",
        "enum": ["SYSTEM", "CUTOUT", "KEYBOARD"],
        "description": "扩展安全区域的枚举类型。",
        "enumDescriptions": {
            "SYSTEM": "系统默认安全区域，包括状态栏、导航栏。",
            "CUTOUT": "设备的非安全区域，例如刘海屏或挖孔屏区域。",
            "KEYBOARD": "软键盘区域。"
        }
    },
    "SafeAreaEdge": {
        "type": "enum",
        "enum": ["TOP", "BOTTOM", "START", "END"],
        "description": "扩展安全区域的方向。",
        "enumDescriptions": {
            "TOP": "上方区域。",
            "BOTTOM": "下方区域。",
            "START": "前部区域。",
            "END": "尾部区域。"
        }
    },
    "KeyboardAvoidMode": {
        "type": "enum",
        "enum": ["OFFSET", "RESIZE"],
        "description": "配置键盘避让时页面的避让模式。",
        "enumDescriptions": {
            "OFFSET": "上抬模式。",
            "RESIZE": "压缩模式。"
        }
    },
    "LayoutSafeAreaType": {
        "type": "enum",
        "enum": ["SYSTEM"],
        "description": "扩展布局安全区域的枚举类型。",
        "enumDescriptions": {
            "SYSTEM": "系统默认安全区域，包括状态栏、导航栏。",
        }
    },
    "LayoutSafeAreaEdge": {
        "type": "enum",
        "enum": ["TOP", "BOTTOM"],
        "description": "扩展安全区域的方向。",
        "enumDescriptions": {
            "TOP": "上方区域。",
            "BOTTOM": "下方区域。",
        }
    },
    "TouchPoint": {
        "type": "object",
        "description": "配置跟手点坐标，不配置时，默认居中。",
        "properties": {
            "X": {
                "type": "Dimension",
                "description": "跟手点X轴坐标。"
            },
            "Y": {
                "type": "Dimension",
                "description": "跟手点Y轴坐标。"
            }
        }
    },
    "TabContentAnimatedTransition": {
        "type": "object",
        "description": "Tabs自定义切换动画相关信息。",
        "properties": {
            "timeout": {
                "type": "number",
                "description": "Tabs自定义切换动画超时时间。从自定义动画开始切换计时，如果到达该时间后，开发者仍未调用TabContentTransitionProxy的finishTransition接口通知Tabs组件自定义动画结束，那么组件就会认为此次自定义动画已结束，直接执行后续操作，单位ms。",
                "default": 1000
            },
            "transition": {
                "type": "(proxy: TabContentTransitionProxy) => void",
                "required": True,
                "description": "自定义切换动画具体内容。",
            }
        }
    },
    "TabContentTransitionProxy": {
        "type": "object",
        "description": "Tabs自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画的起始和目标页面信息，同时，也可以通过调用该对象的finishTransition接口通知Tabs组件自定义动画已结束。",
        "properties": {
            "from": {
                "type": "number",
                "required": True,
                "description": "自定义动画起始页面对应的index值。"
            },
            "to": {
                "type": "number",
                "required": True,
                "description": "自定义动画目标页面对应的index值。"
            },
            "finishTransition()": {
                "type": "void",
                "required": True,
                "description": "通知Tabs组件，此次自定义动画已结束。"
            }
        }
    },
    "PixelRoundPolicy": {
        "type": "object",
        "description": "组件像素级取整对齐策略。",
        "properties": {
            "start": {
                "type": "PixelRoundCalcPolicy",
                "description": "组件前部边界取整对齐。"
            },
            "end": {
                "type": "PixelRoundCalcPolicy",
                "description": "组件尾部边界取整对齐。"
            },
            "top": {
                "type": "PixelRoundCalcPolicy",
                "description": "组件上边界取整对齐。"
            },
            "bottom": {
                "type": "PixelRoundCalcPolicy",
                "description": "组件下边界取整对齐。"
            }
        }
    },
    "VoidCallback": {
        "type": "() => void",
        "description": "无参数回调函数。"
    },
    "Callback": {
        "type": "(data: T) => V",
        "description": "带参数的函数回调。"
    },
    "HoverCallback": {
        "type": "(isHover: boolean, event: HoverEvent) => void",
        "description": "hover事件的回调类型。"
    },
    "VisibleAreaEventOptions": {
        "type": "object",
        "description": "关于区域变化相关的参数。",
        "properties": {
            "ratios": {
                "type": "Array<number>",
                "required": True,
                "description": "阈值数组。其中，每个阈值代表组件可见面积（即组件在屏幕显示区的面积，只计算父组件内的面积，超出父组件部分不会计算）与组件自身面积的比值。每个阈值的取值范围为[0.0, 1.0]，如果开发者设置的阈值超出该范围，则会实际取值0.0或1.0。"
            },
            "expectedUpdateInterval": {
                "type": "number",
                "description": "预期更新间隔，单位为ms。定义了开发者期望的更新间隔。",
                "default": 1000
            }
        }
    },
    "VisibleAreaChangeCallback": {
        "type": "(isVisible: boolean, currentRatio: number) => void",
        "description": "组件可见区域变化事件的回调。\n- isVisible：表示组件的可见面积与自身面积的比值与上一次变化相比的情况，比值变大为true，比值变小为false。\n- currentRatio：触发回调时，组件可见面积与自身面积的比值。"
    },
    "StyledStringValue": {
        "type": "enum",
        "enum": ["TextStyle", "DecorationStyle", "BaselineOffsetStyle", "LetterSpacingStyle", "LineHeightStyle",
                 "TextShadowStyle", "GestureStyle", "ParagraphStyle", "ImageAttachment", "CustomSpan"],
        "description": "样式对象类型，用于设置属性字符串的样式。",
        "enumDescriptions": {
            "TextStyle": "文本字体样式。",
            "DecorationStyle": "文本装饰线样式。",
            "BaselineOffsetStyle": "文本基线偏移量样式。",
            "LetterSpacingStyle": "文本字符间距样式。",
            "LineHeightStyle": "文本行高样式。",
            "TextShadowStyle": "文本阴影样式。",
            "GestureStyle": "事件手势样式。",
            "ParagraphStyle": "文本段落样式。",
            "ImageAttachment": "图片样式。",
            "CustomSpan": "自定义绘制Span样式。"
        }
    },
    "SubmitEvent": {
        "type": "object",
        "description": "定义用户提交事件。",
        "properties": {
            "keepEditableState": {
                "type": "() => void",
                "required": True,
                "description": "用户自定义输入框编辑状态，调用时保持编辑态。"
            },
            "text": {
                "type": "string",
                "required": True,
                "description": "输入框文本内容。"
            }
        }
    },
    "EnterKeyType": {
        "type": "enum",
        "enum": ["Go", "Search", "Send", "Next", "Done", "PREVIOUS", "NEW_LINE"],
        "description": "定义输入框回车键类型。",
        "enumDescriptions": {
            "Go": "显示为开始样式。",
            "Search": "显示为搜索样式。",
            "Send": "显示为发送样式。",
            "Next": "显示为下一步样式。",
            "Done": "显示为完成样式。",
            "PREVIOUS": "显示为上一步样式。",
            "NEW_LINE": "显示为换行样式。"
        }
    },
    "DividerStyleOptions": {
        "type": "object",
        "description": "分割线样式属性集合, 用于描述分割线相关信息。",
        "properties": {
            "strokeWidth": {
                "type": "LengthMetrics",
                "description": "分割线的线宽。"
            },
            "color": {
                "type": "ResourceColor",
                "description": "分割线的颜色。"
            },
            "startMargin": {
                "type": "LengthMetrics",
                "description": "分割线与菜单侧边起始端的距离。"
            },
            "endMargin": {
                "type": "LengthMetrics",
                "description": "分割线与菜单侧边结束端的距离。"
            }
        }
    },
    "ButtonOptions": {
        "type": "object",
        "description": "按钮样式属性集合, 用于描述按钮相关信息。",
        "properties": {
            "type": {
                "type": "ButtonType",
                "description": "描述按钮显示样式。",
                "default": "ButtonType.Capsule"
            },
            "stateEffect": {
                "type": "boolean",
                "description": "按钮按下时是否开启按压态显示效果，当设置为false时，按压效果关闭。",
                "default": "true"
            },
            "buttonStyle": {
                "type": "ButtonStyleMode",
                "description": "描述按钮的样式和重要程度。按钮重要程度：强调按钮>普通按钮>文字按钮。",
                "default": "ButtonStyleMode.EMPHASIZED"
            },
            "controlSize": {
                "type": "ControlSize",
                "description": "描述按钮的尺寸。",
                "default": "ControlSize.NORMAL"
            },
            "role": {
                "type": "ButtonRole",
                "description": "描述按钮的角色。",
                "default": "ButtonRole.NORMAL"
            }
        }
    },
    # ---------------------------------------------------------------------------------------------------------------
    "IndexerAlign": {
        "type": "enum",
        "enum": ["Left", "Right", "START", "END"],
        "description": "索引器对齐方式。",
        "enumDescriptions": {
            "Left": "弹框显示在索引条右侧。",
            "Right": "弹框显示在索引条左侧。",
            "START": "在LTR场景下，弹框显示在索引条右侧的位置。在RTL场景下，弹框显示在索引条左侧的位置。",
            "END": "在LTR场景下，弹框显示在索引条左侧的位置。在RTL场景下，弹框显示在索引条右侧的位置。"
        }
    },
    "ImageFit": {
        "type": "enum",
        "enum": ["Contain", "Cover", "Auto", "Fill", "ScaleDown", "None", "TOP_START", "TOP", "TOP_END", "START", "CENTER", "END", "BOTTOM_START", "BOTTOM", "BOTTOM_END"],
        "description": "图片填充方式。",
        "enumDescriptions": {
            "Contain": "保持图片宽高比缩放图片，使图片的长边能完全显示出来。",
            "Cover": "保持图片宽高比缩放图片，使图片的短边能完全显示出来。",
            "Auto": "保持图片原始尺寸。",
            "Fill": "拉伸图片，使图片填满容器。",
            "ScaleDown": "保持图片宽高比缩放图片，使图片的长边和短边都不超过容器的边界。",
            "None": "不缩放图片。",
            "TOP_START": "图片在容器的左上角显示。",
            "TOP": "图片在容器的上方居中显示。",
            "TOP_END": "图片在容器的右上角显示。",
            "START": "图片在容器的左边居中显示。",
            "CENTER": "图片在容器的中间显示。",
            "END": "图片在容器的右边居中显示。",
            "BOTTOM_START": "图片在容器的左下角显示。",
            "BOTTOM": "图片在容器的下方居中显示。",
            "BOTTOM_END": "图片在容器的右下角显示。"
        }
    },
    "Direction": {
        "type": "enum",
        "enum": ["Ltr", "Rtl", "Auto"],
        "description": "布局方向。",
        "enumDescriptions": {
            "Ltr": "元素从左到右布局。",
            "Rtl": "元素从右到左布局。",
            "Auto": "使用系统默认布局方向。"
        }
    },
}
