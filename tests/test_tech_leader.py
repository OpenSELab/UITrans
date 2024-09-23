import json
import os
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.resource import load_harmony_resource
from core.pilot.schema import BreakdownLayoutTranslation
from core.prompt.prompt_loader import PromptLoader
from template import HarmonyEmptyAbilityV5ProjectTemplate
from core.llms.oai_client import OpenAIClient

os.chdir("../")

ConfigLoader.from_file("./config.yaml")
harmony_template = HarmonyEmptyAbilityV5ProjectTemplate()
openai_default_config = ConfigLoader.get_config().llm_config.get("deepseek").model_dump()
resource = load_harmony_resource(r"D:\Codes\Python\harmony-pilot\demos\haromny_demos\hmdemo\entry\src\main\resources")


def test_complexity_analysis():
    openai_default_config["model"] = "deepseek-chat"
    client = OpenAIClient(openai_default_config)
    user_story = """请你创建一个页面，FirstFragment，该页面需要实现以下功能
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

    system_prompt = PromptLoader.get_prompt("tech_leader/system.prompt")
    complexity_analysis_prompt = PromptLoader.get_prompt(
        "tech_leader/complexity_analysis.prompt",
        story=user_story
    )
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": complexity_analysis_prompt, "role": "user"}
    ])
    print(response.choices[0].message.content)


def test_breakdown_story():
    from core.pilot.schema import BreakdownStory
    openai_default_config["model"] = "deepseek-chat"
    client = OpenAIClient(openai_default_config)

    system_prompt = PromptLoader.get_prompt("tech_leader/system.prompt")
    project_name = "Harmony 示例代码"
    project_description = "这是一个HarmonyOS应用示例代码项目，该应用采用Stage模型且API版本为12。"
    project_files = harmony_template.files
    user_story = """请你创建一个页面，FirstFragment，该页面需要实现以下功能
## 导航栏功能
这个功能点涉及将一个导航栏（默认显示在屏幕顶部），用于提供标准的导航和操作功能。导航栏的样式为宽度匹配父布局，高度为默认的56vp，导航栏的功能包括显示标题，没有回退按钮。
## 滚动布局功能
这个功能点涉及一个滚动布局组件，用于在页面上实现内容滚动显示。滚动布局包含下列按钮组件和文本显示组件。滚动视图的宽度和高度都设置为与父容器匹配。
## 按钮导航功能
这个功能点涉及将一个按钮组件放置在屏幕顶部中央，按钮的文本内容引用自资源@string/next。当用户点击该按钮时，应用会从当前的FirstFragment导航到SecondFragment。
## 文本显示功能
这个功能点涉及将一个文本视图组件放置在按钮组件下方，文本视图的文本内容引用自资源@string/lorem_ipsum。文本视图位于屏幕中央，并且与按钮组件之间有16vp的垂直间距。文本左对齐。
## 浮动操作按钮功能
这个功能点涉及将一个浮动操作按钮（默认显示在屏幕底部右侧。浮动操作按钮的样式为宽度自适应内容，高度自适应内容，位于底部和右侧，右侧外边距为`@dimen/fab_margin`，底部外边距为16vp，图标为`ic_dialog_email`（邮件图标）。浮动操作按钮的功能包括在点击时显示一个默认显示在屏幕底部的快捷消息提示，提示内容为"Replace with your own action"。

该页面的结构为：
<androidx.core.widget.NestedScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:padding="16dp">

        <Button
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
    """
    breakdown_story_prompt = PromptLoader.get_prompt(
        "tech_leader/breakdown_story.prompt",
        project_name=project_name,
        project_description=project_description,
        project_files=project_files,
        project_resources=resource,
        story={
            "description": user_story,
            "complexity": "简单"
        },
        is_file_content=False,
        is_resource_content=False
    )
    # print(breakdown_story_prompt)
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": breakdown_story_prompt, "role": "user"}
    ], model_schema=BreakdownStory, temperature=0.7)
    print(response.choices[0].message.content)


def test_breakdown_layout_translation():
    layout_files = [
        {
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
        """
        },
        {
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
        """
        },
        {
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
        """
        }
    ]
    client = OpenAIClient(openai_default_config)

    system_prompt = PromptLoader.get_prompt("tech_leader/system.prompt")
    breakdown_layout_translation_prompt = PromptLoader.get_prompt(
        "tech_leader/breakdown_layout_translation.prompt",
        layout_files=layout_files
    )
    print(breakdown_layout_translation_prompt)
    # response = client.create(messages=[
    #     {"content": system_prompt, "role": "system"},
    #     {"content": breakdown_layout_translation_prompt, "role": "user"}
    # ], model_schema=BreakdownLayoutTranslation, temperature=1.25)
    # print(response.choices[0].message.content)