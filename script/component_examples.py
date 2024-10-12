# 组件名：组件示例
examples = {
    "Scroll": [
        {
            "description": "实现了一个可滚动的页面布局，页面内容在垂直方向上排列，并且页面顶部和底部有固定的内边距，以适应系统窗口和操作栏的高度。",
            "code": "Scroll() {\n        Column() {\n\n        }\n        .width('100%')\n        .height('auto')\n        .padding({\n          bottom: $r('app.float.activity_vertical_margin'),\n          top: $r('app.float.activity_vertical_margin')\n        })\n      }\n      .width('auto')\n      .height('auto')\n      .margin({ top: '56vp' })"
        }
    ],
    "Stack": [
        {
            "description": "页面呈现一个带有圆角和内边距的卡片视图，卡片内部包含一个文本视图，文本视图显示一段可选择的文本，文本内容为“关于”标题。",
            "code": "Stack() {\n        Column() {\n          Text($r('app.string.heading_about'))\n            .id('text_view_about')\n            .width('auto')\n            .height('auto')\n            .margin({\n              bottom: '24vp',\n              left: '16vp',\n              right: '16vp',\n              top: '16vp'\n            })\n            .lineBreakStrategy(LineBreakStrategy.HIGH_QUALITY)\n            .textSelectable(TextSelectableMode.SELECTABLE_FOCUSABLE)\n            .fontSize('16fp')\n        }\n        .width('100%')\n        .height('auto')\n      }\n      .width('100%')\n      .height('auto')\n      .margin({\n        bottom: '4vp',\n        left: $r('app.float.activity_horizontal_margin'),\n        right: $r('app.float.activity_horizontal_margin'),\n        top : '4vp'\n      })\n      .padding('16vp')\n      .borderRadius('8vp')"
        },
        {
            "description": "实现了一个居中显示的图像视图，图像的宽度和高度分别为自适应和200vp，图像资源为 app.media.bookdash_logo ，图像在容器中水平和垂直居中显示，并且图像缩放类型为适应中心。",
            "code": "      Stack() {\n        Column() {\n          Image($r('app.media.bookdash_logo'))\n            .id('imageViewLogo')\n            .width('auto')\n            .height('200vp')\n            .margin({\n              left: '8vp',\n              right: '8vp',\n              top: '8vp',\n              bottom: '8vp'\n            })\n            .objectFit(ImageFit.Auto)\n        }\n        .width('100%')\n        .height('auto')\n        .padding('8vp')\n      }\n      .width('100%')\n      .height('auto')\n      .margin({\n        bottom: '4vp',\n        left: $r('app.float.activity_horizontal_margin'),\n        right: $r('app.float.activity_horizontal_margin'),\n        top : '4vp'\n      })\n      .padding('16vp')\n      .borderRadius('8vp')"
        },
        {
            "description": "该页面呈现了一个带有圆角边框的卡片视图，卡片内部包含两段文本和一个按钮。第一段文本较大，作为标题显示，第二段文本为常规大小，提供详细信息。按钮用于触发进一步的操作，如了解更多信息。整体布局简洁，信息层次分明，便于用户阅读和交互。",
            "code": "Stack() {\n        Column() {\n          Text($r('app.string.why_bookdash_heading'))\n            .id('textViewHeading')\n            .width('auto')\n            .height('auto')\n            .margin({\n              bottom: '8vp',\n              left: '16vp',\n              right: '16vp',\n              top: '16vp'\n            })\n            .textSelectable(TextSelectableMode.SELECTABLE_FOCUSABLE)\n            .fontSize('24fp')\n\n          Text($r('app.string.why_bookdash'))\n            .id('text_why_bookdash')\n            .width('auto')\n            .height('auto')\n            .margin({\n              bottom: '16fp',\n              left: '16fp',\n              right: '16fp'\n            })\n            .lineBreakStrategy(LineBreakStrategy.HIGH_QUALITY)\n            .textSelectable(TextSelectableMode.SELECTABLE_FOCUSABLE)\n            .fontSize('16fp')\n        }\n        .width('100%')\n        .height('auto')\n      }\n      .width('100%')\n      .height('auto')\n      .margin({\n        bottom: '4vp',\n        left: $r('app.float.activity_horizontal_margin'),\n        right: $r('app.float.activity_horizontal_margin'),\n        top : '4vp'\n      })\n      .padding('16vp')\n      .borderRadius('8vp')"
        }
    ]
}