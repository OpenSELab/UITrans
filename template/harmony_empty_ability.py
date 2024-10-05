import os

from .base import BaseProjectTemplate


class HarmonyEmptyAbilityV5ProjectTemplate(BaseProjectTemplate):
    """
    Harmony Empty Ability V5 project template.
    """

    name = "harmony_empty_ability_v5"
    path = "template/harmony_empty_ability_v5"
    description = "Harmony Empty Ability V5 project template."
    file_descriptions = {
        "AppScope/app.json5": "用于定义应用程序元数据和设置的配置文件。它包括应用程序的捆绑包名称、供应商、版本信息、图标、标签和各种 API 版本要求等详细信息。该文件对于应用程序在不同设备和环境中的识别、部署和兼容性至关重要。",
        "AppScope/resources/base/element/string.json": "用于定义`应用程序`字符串资源的配置文件。它包括键为`string`的键值对集合，在集合中定义了字符串资源的名和值。",
        "AppScope/resources/base/media/app_icon.png": "应用程序在手机设置中显示的图标。",
        "entry/oh-package.json5": "用于管理OpenHarmony项目依赖和配置的文件，分为工程级和模块级。工程级文件位于项目根目录，主要配置全局选项如依赖覆盖、参数化配置等。模块级文件位于各模块根目录，定义包名、版本、依赖项等基本信息。该文件支持多种依赖类型（生产依赖、开发依赖、动态依赖），并提供版本控制、依赖替换、参数化配置等功能，确保项目依赖的一致性和可维护性。",
        "entry/obfuscation-rules.txt": "用于定义应用程序代码混淆规则，保护知识产权和增强代码安全性，防止逆向工程。",
        "entry/hvigorfile.ts": "用于定义和自动化应用程序的构建流程，包括编译、打包、测试和部署等任务，提高开发效率和项目质量。",
        "entry/build-profile.json5": "用于定义应用程序或模块的构建配置信息，包括工程级和模块级的配置。该文件详细描述了编译选项、签名方案、目标平台、版本信息、构建模式、资源管理等关键参数。",
        "entry/.gitignore": "用于指定Git版本控制系统中需要忽略的文件和目录",
        "entry/src/main/module.json5": "用于在应用程序中定义特定于模块的元数据和设置的配置文件。它包括模块的名称、类型、入口点、支持的设备类型以及各种配置选项等详细信息，包括扩展功能、权限等。该文件对于模块在不同设备和环境中的识别、部署和功能至关重要。",
        "entry/src/main/ets/entryability/EntryAbility.ets": "用于定义应用程序主入口组件的行为和生命周期，包括初始化用户界面、管理状态转换、响应用户交互以及处理窗口创建和销毁等关键事件。",
        "entry/src/main/ets/entrybackupability/EntryBackupAbility.ets": "用于定义应用程序备份扩展组件的行为，实现数据备份和恢复功能。",
        "entry/src/main/ets/pages/Index.ets": "定义了一个名为Index的空白页面，该页面作为EntryAbility.ets中的默认启动页面。",
        "entry/src/main/resources/base/element/color.json": "用于定义默认`entry模块`颜色资源的配置文件。它包括键为`color`的键值对集合，在集合中定义了颜色资源的名和值。",
        "entry/src/main/resources/base/element/string.json": "用于定义默认`entry模块`字符串资源的配置文件。它包括键为`string`的键值对集合，在集合中定义了字符串资源的名和值。",
        "entry/src/main/resources/base/media/background.png": "用于应用程序图标背景的图像。",
        "entry/src/main/resources/base/media/foreground.png": "用于应用程序图标前景的图像。",
        "entry/src/main/resources/base/media/startIcon.png": "应用程序在桌面及启动页的图标。",
        "entry/src/main/resources/base/media/layered_image.json": "用于定义应用图标前景图和背景图的配置文件。",
        "entry/src/main/resources/base/profile/backup_config.json": "应用程序备份与恢复的配置文件。",
        "entry/src/main/resources/base/profile/main_pages.json": "用于定义应用程序页面的配置文件，该文件定义了应用程序中主要页面的路由信息和显示窗口相关的配置，只有在此文件中定义的页面才支持路由跳转。",
        "entry/src/main/resources/en_US/element/string.json": "用于定义英语（美国）(en_US)区域设置下`entry模块`颜色资源的配置文件。它包括键为`color`的键值对集合，在集合中定义了颜色资源的名和值。",
        "entry/src/main/resources/zh_CN/element/string.json": "用于定义中文（中国）(zh_CN)区域设置下`entry模块`字符串资源的配置文件。它包括键为`string`的键值对集合，在集合中定义了字符串资源的名和值。",
        # TODO: 添加额外 mock、ohosTest、test 等目录及其文件的介绍
    }
