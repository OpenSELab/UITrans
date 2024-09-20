MEDIA_COMPONENT = {
    "Video": {
        "description": "用于播放视频文件并控制其播放状态的组件。",
        "interfaces": [
            {
                "description": "Video(value: VideoOptions)",
                "params": {
                    "value": {
                        "type": "VideoOptions",
                        "required": True,
                        "description": "视频选项对象。"
                    }
                }
            }
        ],
        "attributes": {
            "muted": {
                "description": "设置是否静音。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否静音。",
                        "default": False
                    }
                }
            },
            "autoPlay": {
                "description": "设置是否自动播放。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否自动播放。",
                        "default": False
                    }
                }
            },
            "controls": {
                "description": "设置控制视频播放的控制栏是否显示。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "控制栏是否显示。",
                        "default": True
                    }
                }
            },
            "objectFit": {
                "description": "设置视频显示模式。",
                "params": {
                    "value": {
                        "type": "ImageFit",
                        "required": True,
                        "description": "视频显示模式。",
                        "default": "Cover"
                    }
                }
            },
            "loop": {
                "description": "设置是否单个视频循环播放。",
                "params": {
                    "value": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否循环播放。",
                        "default": False
                    }
                }
            },
            "enableAnalyzer": {
                "description": "设置组件支持AI分析。使能后，视频播放暂停时自动进入分析状态，开始分析当前画面帧，视频继续播放后自动退出分析状态。",
                "params": {
                    "enable": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否启用AI分析功能。"
                    }
                }
            },
            "analyzerConfig": {
                "description": "设置AI分析识别类型，包括主体识别和文字识别功能，默认全部开启。",
                "params": {
                    "config": {
                        "type": "ImageAnalyzerConfig",
                        "required": True,
                        "description": "AI分析识别类型配置。"
                    }
                }
            }
        },
        "events": {
            "onStart": {
                "description": "播放时触发该事件。",
                "params":{}
            },
            "onPause": {
                "description": "暂停时触发该事件。",
                "params":{}
            },
            "onFinish": {
                "description": "播放结束时触发该事件。",
                "params":{}
            },
            "onError": {
                "description": "播放失败时触发该事件。",
                "params":{}
            },
            "onStop": {
                "description": "播放停止时触发该事件。",
                "params":{}
            },
            "onPrepared": {
                "description": "视频准备完成时触发该事件。",
                "params": {
                    "duration": {
                        "type": "number",
                        "required": True,
                        "description": "当前视频的时长，单位为秒。"
                    }
                }
            },
            "onSeeking": {
                "description": "操作进度条过程时上报时间信息。",
                "params": {
                    "time": {
                        "type": "number",
                        "required": True,
                        "description": "当前视频播放的进度，单位为秒。"
                    }
                }
            },
            "onSeeked": {
                "description": "操作进度条完成后，上报播放时间信息。",
                "params": {
                    "time": {
                        "type": "number",
                        "required": True,
                        "description": "当前视频播放的进度，单位为秒。"
                    }
                }
            },
            "onUpdate": {
                "description": "播放进度变化时触发该事件。",
                "params": {
                    "time": {
                        "type": "number",
                        "required": True,
                        "description": "当前视频播放的进度，单位为秒。"
                    }
                }
            },
            "onFullscreenChange": {
                "description": "在全屏播放与非全屏播放状态之间切换时触发该事件。",
                "params": {
                    "fullscreen": {
                        "type": "boolean",
                        "required": True,
                        "description": "是否全屏播放。"
                    }
                }
            }
        },
        "examples": [
            """/*\n实现思路：\n本示例展示了如何在鸿蒙ArkUI中使用Video组件来播放视频，并提供了多种控制视频播放的功能，如切换视频源、预览图、控制条显示、播放速度调整等。同时，还展示了如何使用图像分析功能来分析视频内容。\n\n总体功能与效果描述：\n用户可以通过界面上的按钮来控制视频的播放、暂停、停止、重置、设置播放时间、切换视频源和预览图、显示或隐藏控制条、调整播放速度等。此外，还可以通过图像分析功能来分析视频中的主体和文本。\n*/\n\n// VideoCreateComponent.ets\n@Entry\n@Component\nstruct VideoCreateComponent {\n  @State videoSrc: Resource = $rawfile('video1.mp4') // 视频源文件\n  @State previewUri: Resource = $r('app.media.poster1') // 视频预览图\n  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X // 当前播放速度\n  @State isAutoPlay: boolean = False // 是否自动播放\n  @State showControls: boolean = True // 是否显示控制条\n  controller: VideoController = new VideoController() // 视频控制器\n\n  build() {\n    Column() {\n      Video({\n        src: this.videoSrc, // 视频源\n        previewUri: this.previewUri, // 预览图\n        currentProgressRate: this.curRate, // 播放速度\n        controller: this.controller // 视频控制器\n      })\n        .width('100%')\n        .height(600)\n        .autoPlay(this.isAutoPlay) // 自动播放\n        .controls(this.showControls) // 控制条显示\n        .onStart(() => {\n          console.info('onStart') // 视频开始播放事件\n        })\n        .onPause(() => {\n          console.info('onPause') // 视频暂停事件\n        })\n        .onFinish(() => {\n          console.info('onFinish') // 视频播放完成事件\n        })\n        .onError(() => {\n          console.info('onError') // 视频播放错误事件\n        })\n        .onStop(() => {\n          console.info('onStop') // 视频停止事件\n        })\n        .onPrepared((e?: DurationObject) => {\n          if (e != undefined) {\n            console.info('onPrepared is ' + e.duration) // 视频准备完成事件，输出视频时长\n          }\n        })\n        .onSeeking((e?: TimeObject) => {\n          if (e != undefined) {\n            console.info('onSeeking is ' + e.time) // 视频跳转中事件，输出跳转时间\n          }\n        })\n        .onSeeked((e?: TimeObject) => {\n          if (e != undefined) {\n            console.info('onSeeked is ' + e.time) // 视频跳转完成事件，输出跳转时间\n          }\n        })\n        .onUpdate((e?: TimeObject) => {\n          if (e != undefined) {\n            console.info('onUpdate is ' + e.time) // 视频更新事件，输出当前播放时间\n          }\n        })\n\n      Row() {\n        Button('src').onClick(() => {\n          this.videoSrc = $rawfile('video2.mp4') // 切换视频源\n        }).margin(5)\n        Button('previewUri').onClick(() => {\n          this.previewUri = $r('app.media.poster2') // 切换预览图\n        }).margin(5)\n        Button('controls').onClick(() => {\n          this.showControls = !this.showControls // 切换控制条显示\n        }).margin(5)\n      }\n\n      Row() {\n        Button('start').onClick(() => {\n          this.controller.start() // 开始播放\n        }).margin(2)\n        Button('pause').onClick(() => {\n          this.controller.pause() // 暂停播放\n        }).margin(2)\n        Button('stop').onClick(() => {\n          this.controller.stop() // 停止播放\n        }).margin(2)\n        Button('reset').onClick(() => {\n          this.controller.reset() // 重置播放\n        }).margin(2)\n        Button('setTime').onClick(() => {\n          this.controller.setCurrentTime(10, SeekMode.Accurate) // 设置播放时间\n        }).margin(2)\n      }\n\n      Row() {\n        Button('rate 0.75').onClick(() => {\n          this.curRate = PlaybackSpeed.Speed_Forward_0_75_X // 设置播放速度为0.75倍\n        }).margin(5)\n        Button('rate 1').onClick(() => {\n          this.curRate = PlaybackSpeed.Speed_Forward_1_00_X // 设置播放速度为1倍\n        }).margin(5)\n        Button('rate 2').onClick(() => {\n          this.curRate = PlaybackSpeed.Speed_Forward_2_00_X // 设置播放速度为2倍\n        }).margin(5)\n      }\n    }\n  }\n}\n\ninterface DurationObject {\n  duration: number; // 视频时长\n}\n\ninterface TimeObject {\n  time: number; // 时间点\n}"""
        ]
    }
}
