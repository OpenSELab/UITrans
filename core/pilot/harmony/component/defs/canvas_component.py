CANVAS_COMPONENT = {
    "Canvas": {
        "description": "提供画布组件，用于自定义绘制图形。",
        "interfaces": [
            {
                "description": "Canvas(context?: CanvasRenderingContext2D | DrawingRenderingContext)",
                "params": {
                    "context": {
                        "type": ["CanvasRenderingContext2D", "DrawingRenderingContext"],
                        "description": "CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象，具体描述见CanvasRenderingContext2D对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象，具体描述见DrawingRenderingContext对象。"
                    }
                }
            },
            {
                "description": "Canvas(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions)",
                "params": {
                    "context": {
                        "type": ["CanvasRenderingContext2D", "DrawingRenderingContext"],
                        "description": "CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象，具体描述见CanvasRenderingContext2D对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象，具体描述见DrawingRenderingContext对象。"
                    },
                    "imageAIOptions": {
                        "type": "ImageAIOptions",
                        "description": "给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。"
                    }
                }
            }
        ],
        "attributes": {
            "enableAnalyzer12+": {
                "description": "设置组件支持AI分析，需要搭配context中的StartImageAnalyzer和StopImageAnalyzer一起使用。不能和overlay属性同时使用，两者同时设置时overlay中CustomBuilder属性将失效。该特性依赖设备能力。",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "description": "组件支持AI分析，设置为true时，组件可进行AI分析。",
                        "default": False
                    }
                }
            }
        },
        "events": {
            "onReady": {
                "description": "Canvas组件初始化完成时或者Canvas组件发生大小变化时的事件回调，当该事件被触发时画布被清空，该事件之后Canvas组件宽高确定且可获取，可使用Canvas相关API进行绘制。当Canvas组件仅发生位置变化时，只触发onAreaChange事件、不触发onReady事件。onAreaChange事件在onReady事件后触发。",
                "params": {}
            }
        }
    },
    "CanvasGradient": {
        "description": "渐变对象。",
        "interfaces": [
            {
                "description": "addColorStop(offset: number, color: string): void",
                "params": {
                    "offset": {
                        "type": "number",
                        "required": True,
                        "description": "设置渐变点距离起点的位置占总体长度的比例，范围为0到1。"
                    },
                    "color": {
                        "type": "string",
                        "required": True,
                        "description": "设置渐变的颜色。颜色格式参考ResourceColor中string类型说明"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {}
    },
    "CanvasPattern": {
        "description": "一个Object对象，使用createPattern方法创建，通过指定图像和重复方式创建图片填充的模板。",
        "interfaces": [
            {
                "description": "setTransform(transform?: Matrix2D): void",
                "params": {
                    "transform": {
                        "type": "Matrix2D",
                        "required": False,
                        "description": "转换矩阵。"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {}
    },
    "CanvasRenderingContext2D": {
        "description": "使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。"},
    "DrawingRenderingContext": {
        "description": "使用DrawingRenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。",
        "interfaces": [
            {
                "description": "DrawingRenderingContext(unit?: LengthMetricsUnit)",
                "params": {
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "description": "用来配置DrawingRenderingContext对象的单位模式，配置后无法更改，配置方法同CanvasRenderingContext2D。",
                        "default": "DEFAULT"
                    }
                }
            }
        ],
        "attributes": {
            "size": {
                "description": "Context大小的宽和高。默认单位为vp。",
                "params": {
                    "width": {
                        "type": "number",
                        "description": "宽度"
                    },
                    "height": {
                        "type": "number",
                        "description": "高度"
                    }
                }
            },
            "canvas": {
                "description": "绘制模块的Canvas对象，具体描述见绘制模块中的Canvas对象。",
                "params": {
                    "canvas": {
                        "type": "Canvas",
                        "description": "Canvas对象"
                    }
                }
            }
        },
        "events": {
            "invalidate": {
                "description": "invalidate(): void\n使组件无效，触发组件的重新渲染。",
                "params": {}
            }
        }
    },
    "ImageBitmap": {
        "description": "ImageBitmap对象可以存储canvas渲染的像素数据。",
        "interfaces": [
            {
                "description": "ImageBitmap(data: PixelMap, unit?: LengthMetricsUnit)",
                "params": {
                    "data": {
                        "type": "PixelMap",
                        "required": True,
                        "description": "通过PixelMap创建ImageBitmap对象。"
                    },
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "required": False,
                        "description": "用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同CanvasRenderingContext2D。",
                        "default": "DEFAULT"
                    }
                }
            },
            {
                "description": "ImageBitmap(src: string, unit?: LengthMetricsUnit)",
                "params": {
                    "src": {
                        "type": "string",
                        "required": True,
                        "description": "图片的数据源支持本地图片。支持本地图片类型：bmp、jpg、png、svg和webp类型。ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。"
                    },
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "required": False,
                        "description": "用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同CanvasRenderingContext2D。",
                        "default": "DEFAULT"
                    }
                }
            }
        ],
        "attributes": {
            "width": {
                "description": "ImageBitmap的像素宽度。默认单位为vp。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "ImageBitmap的像素宽度。"
                    }
                }
            },
            "height": {
                "description": "ImageBitmap的像素高度。默认单位为vp。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "ImageBitmap的像素高度。"
                    }
                }
            }
        },
        "events": {
            "close": {
                "description": "close(): void\n释放ImageBitmap对象相关联的所有图形资源，并将ImageBitmap对象的宽高置为0。",
                "params": {}
            }
        }
    },
    "ImageData": {
        "description": "ImageData对象可以存储canvas渲染的像素数据。",
        "interfaces": [
            {
                "description": "constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)",
                "params": {
                    "width": {
                        "type": "number",
                        "required": True,
                        "description": "矩形区域实际像素宽度，默认单位为vp。"
                    },
                    "height": {
                        "type": "number",
                        "required": True,
                        "description": "矩形区域实际像素高度，默认单位为vp。"
                    },
                    "data": {
                        "type": "Uint8ClampedArray",
                        "required": False,
                        "description": "一维数组，保存了相应的颜色数据，数据值范围为0到255。"
                    },
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "required": False,
                        "description": "用来配置ImageData对象的单位模式，配置后无法动态更改，配置方法同CanvasRenderingContext2D。",
                        "default": "DEFAULT"
                    }
                }
            }
        ],
        "attributes": {
            "width": {
                "description": "矩形区域实际像素宽度。单位为px。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "矩形区域实际像素宽度。"
                    }
                }
            },
            "height": {
                "description": "矩形区域实际像素高度。单位为px。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "矩形区域实际像素高度。"
                    }
                }
            },
            "data": {
                "description": "一维数组，保存了相应的颜色数据，数据值范围为0到255。",
                "params": {
                    "value": {
                        "type": "Uint8ClampedArray",
                        "required": True,
                        "description": "一维数组，保存了相应的颜色数据。"
                    }
                }
            }
        },
        "events": {}
    },
    "Matrix2D": {
        "description": "矩阵对象，可以对矩阵进行缩放、旋转、平移等变换。",
        "interfaces": [
            {
                "description": "Matrix2D(unit?: LengthMetricsUnit)",
                "params": {
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "description": "长度度量单位。"
                    }
                }
            }
        ],
        "attributes": {
            "scaleX": {
                "description": "水平缩放比例系数。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "水平缩放比例系数。"
                    }
                }
            },
            "scaleY": {
                "description": "垂直缩放比例系数。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "垂直缩放比例系数。"
                    }
                }
            },
            "rotateX": {
                "description": "水平旋转角度。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "水平旋转角度。"
                    }
                }
            },
            "rotateY": {
                "description": "垂直旋转角度。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "垂直旋转角度。"
                    }
                }
            },
            "translateX": {
                "description": "水平平移距离。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "水平平移距离。"
                    }
                }
            },
            "translateY": {
                "description": "垂直平移距离。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "垂直平移距离。"
                    }
                }
            }
        },
        "events": {},
        "methods": [
            {
                "description": "identity(): Matrix2D",
                "params": {},
                "returns": {
                    "type": "Matrix2D",
                    "description": "创建一个单位矩阵。"
                }
            },
            {
                "description": "invert(): Matrix2D",
                "params": {},
                "returns": {
                    "type": "Matrix2D",
                    "description": "得到当前矩阵的逆矩阵。"
                }
            },
            {
                "description": "multiply(other?: Matrix2D): Matrix2D",
                "params": {
                    "other": {
                        "type": "Matrix2D",
                        "description": "目标矩阵。"
                    }
                },
                "returns": {
                    "type": "Matrix2D",
                    "description": "当前矩阵与目标矩阵相乘。"
                }
            },
            {
                "description": "rotate(degree: number, rx?: number, ry?: number): Matrix2D",
                "params": {
                    "degree": {
                        "type": "number",
                        "description": "旋转角度，单位为弧度。"
                    },
                    "rx": {
                        "type": "number",
                        "description": "旋转点的水平方向坐标。"
                    },
                    "ry": {
                        "type": "number",
                        "description": "旋转点的垂直方向坐标。"
                    }
                },
                "returns": {
                    "type": "Matrix2D",
                    "description": "对当前矩阵进行旋转运算。"
                }
            },
            {
                "description": "translate(tx?: number, ty?: number): Matrix2D",
                "params": {
                    "tx": {
                        "type": "number",
                        "description": "水平方向平移距离。"
                    },
                    "ty": {
                        "type": "number",
                        "description": "垂直方向平移距离。"
                    }
                },
                "returns": {
                    "type": "Matrix2D",
                    "description": "对当前矩阵进行左乘平移运算。"
                }
            },
            {
                "description": "scale(sx?: number, sy?: number): Matrix2D",
                "params": {
                    "sx": {
                        "type": "number",
                        "description": "水平缩放比例系数。"
                    },
                    "sy": {
                        "type": "number",
                        "description": "垂直缩放比例系数。"
                    }
                },
                "returns": {
                    "type": "Matrix2D",
                    "description": "对当前矩阵进行右乘缩放运算。"
                }
            }
        ]
    },
    "OffscreenCanvas": {
        "description": "OffscreenCanvas组件用于自定义绘制图形，可以在屏幕外渲染的画布，避免影响应用程序主线程性能。",
        "interfaces": [
            {
                "description": "OffscreenCanvas(width: number, height: number, unit?: LengthMetricsUnit)",
                "params": {
                    "width": {
                        "type": "number",
                        "required": True,
                        "description": "OffscreenCanvas组件的宽度。"
                    },
                    "height": {
                        "type": "number",
                        "required": True,
                        "description": "OffscreenCanvas组件的高度。"
                    },
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "required": False,
                        "description": "用来配置OffscreenCanvas对象的单位模式，配置后无法动态更改。",
                        "default": "DEFAULT"
                    }
                }
            }
        ],
        "attributes": {
            "width": {
                "description": "OffscreenCanvas组件的宽度。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "OffscreenCanvas组件的宽度。"
                    }
                }
            },
            "height": {
                "description": "OffscreenCanvas组件的高度。",
                "params": {
                    "value": {
                        "type": "number",
                        "required": True,
                        "description": "OffscreenCanvas组件的高度。"
                    }
                }
            }
        },
        "events": {
            "transferToImageBitmap": {
                "description": "transferToImageBitmap(): ImageBitmap",
                "params": {},
                "returns": {
                    "type": "ImageBitmap",
                    "description": "从OffscreenCanvas组件中最近渲染的图像创建一个ImageBitmap对象。"
                }
            },
            "getContext": {
                "description": "getContext(contextType: \"2d\", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D",
                "params": {
                    "contextType": {
                        "type": "string",
                        "required": True,
                        "description": "绘图上下文的类型。"
                    },
                    "options": {
                        "type": "RenderingContextSettings",
                        "required": False,
                        "description": "绘图上下文的设置。"
                    }
                },
                "returns": {
                    "type": "OffscreenCanvasRenderingContext2D",
                    "description": "返回OffscreenCanvas组件的绘图上下文。"
                }
            }
        }
    },
    "OffscreenCanvasRenderingContext2D": {
        "description": "使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是矩形、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到canvas上，加快了绘制速度。",
        "interfaces": [
            {
                "description": "OffscreenCanvasRenderingContext2D(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)",
                "params": {
                    "width": {
                        "type": "number",
                        "required": True,
                        "description": "离屏画布的宽度。"
                    },
                    "height": {
                        "type": "number",
                        "required": True,
                        "description": "离屏画布的高度。"
                    },
                    "settings": {
                        "type": "RenderingContextSettings",
                        "description": "渲染上下文设置。"
                    },
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "description": "长度度量单位。"
                    }
                }
            }
        ],
        "attributes": {
            "fillStyle": {
                "description": "指定绘制的填充色。",
                "params": {
                    "value": {
                        "type": ["string", "number", "CanvasGradient", "CanvasPattern"],
                        "description": "填充色。类型为string时，表示设置填充区域的颜色；类型为number时，表示设置填充区域的颜色；类型为CanvasGradient时，表示渐变对象，使用createLinearGradient方法创建；类型为CanvasPattern时，使用createPattern方法创建。"
                    }
                }
            },
            "lineWidth": {
                "description": "设置绘制线条的宽度。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "线条的宽度。默认单位：vp。"
                    }
                }
            },
            "strokeStyle": {
                "description": "设置线条的颜色。",
                "params": {
                    "value": {
                        "type": ["string", "number", "CanvasGradient", "CanvasPattern"],
                        "description": "线条的颜色。类型为string时，表示设置线条使用的颜色；类型为number时，表示设置线条使用的颜色；类型为CanvasGradient时，表示渐变对象，使用createLinearGradient方法创建；类型为CanvasPattern时，使用createPattern方法创建。"
                    }
                }
            },
            "lineCap": {
                "description": "指定线端点的样式。",
                "params": {
                    "value": {
                        "type": "CanvasLineCap",
                        "description": "线端点的样式。可选值为：'butt'、'round'、'square'。默认值：'butt'。"
                    }
                }
            },
            "lineJoin": {
                "description": "指定线段间相交的交点样式。",
                "params": {
                    "value": {
                        "type": "CanvasLineJoin",
                        "description": "线段间相交的交点样式。可选值为：'round'、'bevel'、'miter'。默认值：'miter'。"
                    }
                }
            },
            "miterLimit": {
                "description": "设置斜接面限制值，该值指定了线条相交处内角和外角的距离。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "斜接面限制值。默认值：10。单位：px。"
                    }
                }
            },
            "font": {
                "description": "设置文本绘制中的字体样式。",
                "params": {
                    "value": {
                        "type": "string",
                        "description": "字体样式。语法：ctx.font='font-size font-family'。"
                    }
                }
            },
            "textAlign": {
                "description": "设置文本绘制中的文本对齐方式。",
                "params": {
                    "value": {
                        "type": "CanvasTextAlign",
                        "description": "文本对齐方式。可选值为：'left'、'right'、'center'、'start'、'end'。默认值：'left'。"
                    }
                }
            },
            "textBaseline": {
                "description": "设置文本绘制中的水平对齐方式。",
                "params": {
                    "value": {
                        "type": "CanvasTextBaseline",
                        "description": "水平对齐方式。可选值为：'alphabetic'、'top'、'hanging'、'middle'、'ideographic'、'bottom'。默认值：'alphabetic'。"
                    }
                }
            },
            "globalAlpha": {
                "description": "设置透明度，0.0为完全透明，1.0为完全不透明。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "透明度。默认值：1.0。"
                    }
                }
            },
            "lineDashOffset": {
                "description": "设置画布的虚线偏移量，精度为float。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "虚线偏移量。默认值：0.0。单位：px。"
                    }
                }
            },
            "globalCompositeOperation": {
                "description": "设置合成操作的方式。",
                "params": {
                    "value": {
                        "type": "string",
                        "description": "合成操作的方式。可选值有：'source-over'、'source-atop'、'source-in'、'source-out'、'destination-over'、'destination-atop'、'destination-in'、'destination-out'、'lighter'、'copy'、'xor'。默认值：'source-over'。"
                    }
                }
            },
            "shadowBlur": {
                "description": "设置绘制阴影时的模糊级别，值越大越模糊，精度为float。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "模糊级别。默认值：0.0。"
                    }
                }
            },
            "shadowColor": {
                "description": "设置绘制阴影时的阴影颜色。",
                "params": {
                    "value": {
                        "type": "string",
                        "description": "阴影颜色。默认值：透明黑色。"
                    }
                }
            },
            "shadowOffsetX": {
                "description": "设置绘制阴影时和原有对象的水平偏移值。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "水平偏移值。默认值：0。默认单位：vp。"
                    }
                }
            },
            "shadowOffsetY": {
                "description": "设置绘制阴影时和原有对象的垂直偏移值。",
                "params": {
                    "value": {
                        "type": "number",
                        "description": "垂直偏移值。默认值：0。默认单位：vp。"
                    }
                }
            },
            "imageSmoothingEnabled": {
                "description": "用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "description": "是否启用图像平滑度调整。默认值：true。"
                    }
                }
            },
            "imageSmoothingQuality": {
                "description": "imageSmoothingEnabled为true时，用于设置图像平滑度。",
                "params": {
                    "value": {
                        "type": "ImageSmoothingQuality",
                        "description": "图像平滑度。可选值为：'low'、'medium'、'high'。默认值：'low'。"
                    }
                }
            },
            "direction": {
                "description": "用于设置绘制文字时使用的文字方向。",
                "params": {
                    "value": {
                        "type": "CanvasDirection",
                        "description": "文字方向。可选值为：'inherit'、'ltr'、'rtl'。默认值：'inherit'。"
                    }
                }
            },
            "filter": {
                "description": "用于设置图像的滤镜。",
                "params": {
                    "value": {
                        "type": "string",
                        "description": "滤镜效果。支持的滤镜效果如下：'none'、'blur'、'brightness'、'contrast'、'grayscale'、'hue-rotate'、'invert'、'opacity'、'saturate'、'sepia'。默认值：'none'。"
                    }
                }
            }
        },
        "events": {
            "onReady": {
                "description": "当Canvas组件完成绘制时触发的事件。",
                "params": {}
            }
        }
    },
    "Path2D": {
        "description": "路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的stroke接口或者fill接口进行绘制。",
        "interfaces": [
            {
                "description": "Path2D(unit?: LengthMetricsUnit)",
                "params": {
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "description": "路径的单位。"
                    }
                }
            },
            {
                "description": "Path2D(description: string, unit?: LengthMetricsUnit)",
                "params": {
                    "description": {
                        "type": "string",
                        "required": True,
                        "description": "符合SVG路径描述规范的路径字符串。"
                    },
                    "unit": {
                        "type": "LengthMetricsUnit",
                        "description": "路径的单位。"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {},
        "rules": None,
        "examples": None,
        "is_common_attrs": False
    }
}
