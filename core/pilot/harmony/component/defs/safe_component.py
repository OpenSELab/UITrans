SAFE_COMPONENT = {
    "LocationButton": {
        "description": "安全控件的位置控件，用户通过点击该位置按钮，可以临时获取精准定位权限，而不需要权限弹框授权确认。",
        "interfaces": [
            {
                "description": "LocationButton() 默认创建带有图标、文本、背景的位置按钮。",
                "params": {}
            },
            {
                "description": "LocationButton(option: LocationButtonOptions)",
                "params": {
                    "option": {
                        "type": "LocationButtonOptions",
                        "required": False,
                        "description": "创建包含指定元素的位置按钮。"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {
            "onClick": {
                "description": "点击动作触发该回调。",
                "params": {
                    "event": {
                        "type": "ClickEvent",
                        "required": True,
                        "description": "见ClickEvent对象说明。"
                    },
                    "result": {
                        "type": "LocationButtonOnClickResult",
                        "required": True,
                        "description": "位置权限的授权结果。"
                    }
                }
            }
        },

        "is_common_attrs": False,
        "examples": [
            """/*\n实现思路：\n本示例展示了如何使用LocationButton组件，通过不同的参数配置来展示不同样式的按钮。每个按钮可以包含图标、文字和背景，并且可以通过点击事件获取位置信息。\n总体功能与效果描述：\n通过不同的参数配置，展示不同样式的LocationButton组件，包括默认样式、仅图标和背景样式、以及图标、文字和背景都存在的样式。点击按钮时，可以获取位置信息并在控制台输出。\n*/\n\n// Index.ets\n@Entry\n@Component\nstruct Index {\n  build() {\n    Row() {\n      Column({space:10}) {\n        // 默认参数下，图标、文字、背景都存在\n        LocationButton().onClick((event: ClickEvent, result: LocationButtonOnClickResult)=>{\n          console.info("result " + result) // 点击按钮时，在控制台输出位置信息\n        })\n        \n        // 传入参数即表示元素存在，不传入的参数表示元素不存在，如果不传入buttonType，会默认添加ButtonType.Capsule配置，显示图标+背景。\n        LocationButton({icon:LocationIconStyle.LINES})\n        \n        // 只显示图标+背景，如果设置背景色高八位的α值低于0x1A，则会被系统强制调整为0xFF\n        LocationButton({icon:LocationIconStyle.LINES, buttonType:ButtonType.Capsule})\n          .backgroundColor(0x10007dff) // 设置背景色，系统会强制调整透明度\n        \n        // 图标、文字、背景都存在，如果设置背景色高八位的α值低于0x1A，则会被系统强制调整为0xFF\n        LocationButton({icon:LocationIconStyle.LINES, text:LocationDescription.CURRENT_LOCATION, buttonType:ButtonType.Capsule})\n      }.width('100%')\n    }.height('100%')\n  }\n}"""
        ]
    },
    "PasteButton": {
        "description": "安全控件的粘贴按钮，用户通过点击该粘贴按钮，可以临时获取读取剪贴板权限。",
        "interfaces": [
            {
                "description": "PasteButton()默认创建带有图标、文本、背景的粘贴按钮。",
                "params": {}
            },
            {
                "description": "PasteButton(option: PasteButtonOptions) 创建包含指定元素的粘贴按钮。",
                "params": {
                    "option": {
                        "type": "PasteButtonOptions",
                        "description": "创建包含指定元素的粘贴按钮。",
                        "required": False,
                        "default": {
                            "icon": "PasteIconStyle.LINES",
                            "text": "PasteDescription.PASTE",
                            "buttonType": "ButtonType.Capsule"
                        }
                    }
                }
            }
        ],
        "attributes": {},
        "events": {
            "onClick": {
                "description": "点击动作触发该回调",
                "params": {
                    "event": {
                        "type": "ClickEvent",
                        "required": True,
                        "description": "见ClickEvent对象说明"
                    },
                    "result": {
                        "type": "PasteButtonOnClickResult",
                        "required": True,
                        "description": "剪贴板权限的授权结果，授权后可以读取当前剪贴板内容。"
                    }
                }
            }
        },
        "examples": [
            """/*\n实现思路：\n本示例展示了如何使用PasteButton组件，通过不同的参数配置来显示不同的按钮样式。每个PasteButton实例都可以通过设置不同的属性来调整其外观和行为。\n总体功能与效果描述：\n通过不同的PasteButton实例，展示了如何在按钮中显示图标、文字和背景，并且如何通过点击事件获取粘贴板内容。\n*/\n\n// xxx.ets\n@Entry\n@Component\nstruct Index {\n  build() {\n    Row() {\n      Column({space:10}) {\n        // 默认参数下，图标、文字、背景都存在\n        PasteButton().onClick((event: ClickEvent, result: PasteButtonOnClickResult)=>{\n          console.info("result " + result) // 点击按钮时，输出粘贴板内容到控制台\n        })\n        \n        // 传入参数即表示元素存在，不传入的参数表示元素不存在，如果不传入buttonType，会默认添加ButtonType.Capsule配置，显示图标+背景。\n        PasteButton({icon:PasteIconStyle.LINES})\n        \n        // 只显示图标+背景，如果设置背景色高八位的α值低于0x1A，则会被系统强制调整为0xFF\n        PasteButton({icon:PasteIconStyle.LINES, buttonType:ButtonType.Capsule})\n          .backgroundColor(0x10007dff) // 设置背景色，但α值低于0x1A会被强制调整为0xFF\n        \n        // 图标、文字、背景都存在，如果设置背景色高八位的α值低于0x1A，则会被系统强制调整为0xFF\n        PasteButton({icon:PasteIconStyle.LINES, text:PasteDescription.PASTE, buttonType:ButtonType.Capsule})\n      }.width('100%')\n    }.height('100%')\n  }\n}"""
        ]
    },
    "SaveButton": {
        "description": "安全控件的保存控件，用户通过点击该保存按钮，可以临时获取存储权限，而不需要权限弹框授权确认。",
        "details": "该组件从API Version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。",
        "interfaces": [
            {
                "description": "SaveButton() 默认创建带有图标、文本、背景的保存按钮。",
                "params": {}
            },
            {
                "description": "SaveButton(option: SaveButtonOptions) 创建包含指定元素的保存按钮。",
                "params": {
                    "option": {
                        "type": "SaveButtonOptions",
                        "required": False,
                        "description": "创建包含指定元素的保存按钮。"
                    }
                }
            }
        ],
        "attributes": {},
        "events": {
            "onClick": {
                "description": "点击动作触发该回调",
                "params": {
                    "event": {
                        "type": "ClickEvent",
                        "required": True,
                        "description": "见ClickEvent对象说明"
                    },
                    "result": {
                        "type": "SaveButtonOnClickResult",
                        "required": True,
                        "description": "存储权限的授权结果，授权时长为10秒，即触发点击后，可以在10秒之内不限制次数的调用特定媒体库接口，超出10秒的调用会鉴权失败。"
                    }
                }
            }
        },
        "is_common_attrs": False,
        "examples": [
            """/*\n实现思路：\n本示例展示了如何使用SaveButton组件来保存图片到设备中。通过点击按钮，触发保存图片的操作，包括创建图片文件、写入内容和关闭文件。\n总体功能与效果描述：\n用户点击SaveButton后，程序会尝试创建一个图片文件，并向其中写入内容，最后关闭文件。如果操作成功，图片将被保存到设备中。\n*/\n\n// Index.ets\nimport { photoAccessHelper } from '@kit.MediaLibraryKit';\nimport { fileIo } from '@kit.CoreFileKit';\n\n@Entry\n@Component\nstruct Index {\n  build() {\n    Row() {\n      Column({space:10}) {\n        // 默认参数下，图标、文字、背景都存在\n        SaveButton().onClick(async (event:ClickEvent, result:SaveButtonOnClickResult) => {\n          if (result == SaveButtonOnClickResult.SUCCESS) {\n            try {\n              const context = getContext(this);\n              let helper = photoAccessHelper.getPhotoAccessHelper(context);\n              // onClick触发后10秒内通过createAsset接口创建图片文件，10秒后createAsset权限收回。\n              let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');\n              // 使用uri打开文件，可以持续写入内容，写入过程不受时间限制\n              let file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);\n              // 写入文件\n              await fileIo.write(file.fd, "context");\n              // 关闭文件\n              await fileIo.close(file.fd);\n            } catch (error) {\n              console.error("error is " + JSON.stringify(error));\n            }\n          }\n        })\n        // 传入参数即表示元素存在，不传入的参数表示元素不存在，如果不传入buttonType，会默认添加ButtonType.Capsule配置，显示图标+背景。\n        SaveButton({icon:SaveIconStyle.FULL_FILLED})\n        // 只显示图标+背景，如果设置背景色高八位的α值低于0x1A，则会被系统强制调整为0xFF\n        SaveButton({icon:SaveIconStyle.FULL_FILLED, buttonType:ButtonType.Capsule})\n          .backgroundColor(0x10007dff)\n        // 图标、文字、背景都存在，如果设置背景色高八位的α值低于0x1A，则会被系统强制调整为0xFF\n        SaveButton({icon:SaveIconStyle.FULL_FILLED, text:SaveDescription.DOWNLOAD, buttonType:ButtonType.Capsule})\n      }.width('100%')\n    }.height('100%')\n  }\n}"""
        ]
    }
}
