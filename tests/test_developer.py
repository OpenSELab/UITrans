import json
import os
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.component.components import get_harmony_component
from core.pilot.harmony.resource import load_harmony_resource
from core.pilot.harmony.utils import get_component_related_types
from core.pilot.schema import BreakdownLayoutTranslation, ChooseComponent, BreakdownLayout
from core.prompt.prompt_loader import PromptLoader
from template.harmony_empty_ability import HarmonyEmptyAbilityV5ProjectTemplate
from core.llms.oai_client import OpenAIClient

os.chdir("../")

ConfigLoader.from_file("./config.yaml")
harmony_template = HarmonyEmptyAbilityV5ProjectTemplate()
openai_default_config = ConfigLoader.get_config().llm_config.get("deepseek").model_dump()
resource = load_harmony_resource(r"D:\Codes\Python\harmony-pilot\demos\haromny_demos\hmdemo\entry\src\main\resources")

"""# FirstFragment
## 导航栏功能
这个功能点涉及将一个导航栏（默认显示在屏幕顶部），用于提供标准的导航和操作功能。导航栏的样式为宽度匹配父布局，高度为默认的56vp，导航栏的功能包括显示标题，没有回退按钮。
## 滚动布局功能
这个功能点涉及一个滚动布局组件，用于在页面上实现内容滚动显示。滚动布局包含下列按钮组件和文本显示组件。滚动视图的宽度和高度都设置为与父容器匹配。
## 按钮导航功能
这个功能点涉及将一个按钮组件放置在屏幕顶部中央，按钮的文本内容为“Next”（引用自资源文件@string/next）。当用户点击该按钮时，应用会从当前的FirstFragment导航到SecondFragment。
## 文本显示功能
这个功能点涉及将一个文本视图组件放置在按钮组件下方，文本视图的文本内容为“Lorem Ipsum”（引用自资源文件@string/lorem_ipsum）。文本视图位于屏幕中央，并且与按钮组件之间有16vp的垂直间距。文本左对齐。
## 浮动操作按钮功能
这个功能点涉及将一个浮动操作按钮（默认显示在屏幕底部右侧。浮动操作按钮的样式为宽度自适应内容，高度自适应内容，位于底部和右侧，右侧外边距为`@dimen/fab_margin`，底部外边距为16vp，图标为`ic_dialog_email`（邮件图标）。浮动操作按钮的功能包括在点击时显示一个默认显示在屏幕底部的快捷消息提示，提示内容为"Replace with your own action"。
"""


layout_files = {
    "res/layout/activity_main.xml": {
        "name": "res/layout/activity_main.xml",
        "content": """<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fitsSystemWindows="true"
    tools:context=".MainActivity">

    <com.google.android.material.appbar.AppBarLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:fitsSystemWindows="true">

        <com.google.android.material.appbar.MaterialToolbar
            android:id="@+id/toolbar"
            android:layout_width="match_parent"
            android:layout_height="?attr/actionBarSize" />

    </com.google.android.material.appbar.AppBarLayout>

    <include layout="@layout/content_main" />

    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/fab"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom|end"
        android:layout_marginEnd="@dimen/fab_margin"
        android:layout_marginBottom="16dp"
        app:srcCompat="@android:drawable/ic_dialog_email" />

</androidx.coordinatorlayout.widget.CoordinatorLayout>
        """,
        "contains": ["res/layout/content_main.xml"],
        "java": ""  # java code
    },
    "res/layout/content_main.xml": {
        "name": "res/layout/content_main.xml",
        "content": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:layout_behavior="@string/appbar_scrolling_view_behavior">

    <fragment
        android:id="@+id/nav_host_fragment_content_main"
        android:name="androidx.navigation.fragment.NavHostFragment"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:defaultNavHost="true"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:navGraph="@navigation/nav_graph" />
</androidx.constraintlayout.widget.ConstraintLayout>
        """,
        "contains": ["res/layout/fragment_first.xml"],
        "java": ""  # java code
    },
    "res/layout/fragment_first.xml": {
        "name": "res/layout/fragment_first.xml",
        "content": """<?xml version="1.0" encoding="utf-8"?>
<androidx.core.widget.NestedScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".FirstFragment">

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:padding="16dp">

        <Button
            android:id="@+id/button_first"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/next"
            app:layout_constraintBottom_toTopOf="@id/textview_first"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <TextView
            android:id="@+id/textview_first"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="16dp"
            android:text="@string/lorem_ipsum"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@id/button_first" />
    </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.core.widget.NestedScrollView>    
        """,
        "contains": [],
        "java": ""  # java code
    }
}


def test_choose_component():
    layout_translation = BreakdownLayoutTranslation.model_validate(json.loads("""
{
  "tasks": [
    {
      "description": "创建ets/pages/FragmentFirst.ets页面，实现安卓布局文件res/layout/fragment_first.xml的转译。",
      "done": false,
      "harmony": "ets/pages/FragmentFirst.ets",
      "android": "res/layout/fragment_first.xml"
    },
    {
      "description": "创建ets/pages/ContentMain.ets页面，实现安卓布局文件res/layout/content_main.xml的转译。",
      "done": false,
      "harmony": "ets/pages/ContentMain.ets",
      "android": "res/layout/content_main.xml"
    },
    {
      "description": "创建ets/pages/Index.ets页面，实现安卓布局文件res/layout/activity_main.xml的转译。",
      "done": false,
      "harmony": "ets/pages/Index.ets",
      "android": "res/layout/activity_main.xml"
    }
  ]
}
        """))
    client = OpenAIClient(openai_default_config)
    current_task_index = 0
    current_task = layout_translation.tasks[current_task_index]
    android_layout = layout_files[current_task.android]
    current_task_description = f"""{current_task.description}
# {android_layout['name']}
{android_layout['content']}
"""
    system_prompt = PromptLoader.get_prompt("developer/system.prompt")
    choose_component_prompt = PromptLoader.get_prompt(
        "developer/choose_component.prompt",
        tasks=layout_translation.tasks,
        current_task_description=current_task_description,
        harmony_components=get_harmony_component()
    )
    print(choose_component_prompt)
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": choose_component_prompt, "role": "user"}
    ], model_schema=ChooseComponent)
    print(response.choices[0].message.content)
    choose_component = ChooseComponent.common_parse_raw(response.choices[0].message.content)
    related_component = {}
    for component in choose_component.components:
        related_component.update(get_harmony_component(component))
    print(related_component)


def test_breakdown_layout():
    client = OpenAIClient(openai_default_config)

    layout_files = {
        "app/res/xml/app_preferences.xml": {
            "name": "app/res/xml/app_preferences.xml",
            "content": "<androidx.preference.PreferenceScreen\nxmlns:android=\"http://schemas.android.com/apk/res/android\">\n\n<androidx.preference.Preference\nandroid:key=\"tutorial_display_key\"\nandroid:summary=\"@string/show_tutorial_settings_summary\"\nandroid:title=\"@string/show_tutorial_settings_title\" />\n\n<androidx.preference.SwitchPreferenceCompat\nandroid:defaultValue=\"true\"\nandroid:key=\"pref_new_book_notification\"\nandroid:summary=\"@string/settings_new_book_notifications_summary\"\nandroid:title=\"@string/settings_new_book_notifications\"\n/>\n</androidx.preference.PreferenceScreen>",
            "java": "",
            "contains": [],
            "resources": {
                "@string/show_tutorial_settings_summary": "resources/values/strings.xml",
                "@string/show_tutorial_settings_title": "resources/values/strings.xml",
                "@string/settings_new_book_notifications_summary": "resources/values/strings.xml",
                "@string/settings_new_book_notifications": "resources/values/strings.xml"

            }
        }
    }

    layout_translation = BreakdownLayoutTranslation.model_validate(json.loads("""
    {
      "tasks": [
        {
          "description": "创建ets/pages/AppPreferences.ets页面，实现安卓布局文件app/res/xml/app_preferences.xml的转译。",
          "done": false,
          "harmony": "ets/pages/AppPreferences.ets",
          "android": "app/res/xml/app_preferences.xml"
        }
      ]
    }
            """))
    current_task_index = 0
    system_prompt = PromptLoader.get_prompt("developer/system.prompt")
    translate_layout_plan_prompt = PromptLoader.get_prompt(
        "developer/breakdown_layout.prompt",
        tasks=layout_translation.tasks,
        current_task=layout_translation.tasks[current_task_index],
        android_layout=layout_files[layout_translation.tasks[current_task_index].android],
        harmony_components=get_harmony_component(),
        is_component_content=False,
        is_type_content=True,
        project_resources=resource
    )
    print(translate_layout_plan_prompt)
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": translate_layout_plan_prompt, "role": "user"}
    ], model_schema=BreakdownLayout, temperature=0.2)
    print(response.choices[0].message.content)
    print(response.usage)
