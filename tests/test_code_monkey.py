import json
import os
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.component.components import get_harmony_component
from core.pilot.harmony.resource import load_harmony_resource
from core.pilot.harmony.utils import get_component_related_types
from core.pilot.schema import BreakdownLayoutTranslation, ChooseComponent, Files
from core.prompt.prompt_loader import PromptLoader
from template.harmony_empty_ability import HarmonyEmptyAbilityV5ProjectTemplate
from core.llms.oai_client import OpenAIClient

os.chdir("../")

ConfigLoader.from_file("./config.yaml")
harmony_template = HarmonyEmptyAbilityV5ProjectTemplate()
openai_default_config = ConfigLoader.get_config().llm_config.get("deepseek").model_dump()
resource = load_harmony_resource(r"D:\Codes\Python\harmony-pilot\demos\haromny_demos\hmdemo\entry\src\main\resources")

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
        """
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
        """
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
        """
    }
}


def test_translate_layout():
    openai_default_config["model"] = "deepseek-chat"
    client = OpenAIClient(openai_default_config)

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

#     choose_component = ChooseComponent.common_parse_raw("""
# {
#   "components": [
#     "Scroll",
#     "Column",
#     "Button",
#     "Text"
#   ]
# }
#     """)
    choose_component = ChooseComponent.common_parse_raw("""
    {
      "components": [
        "Button"
      ]
    }
        """)
    related_component = {}
    for component in choose_component.components:
        related_component.update(get_harmony_component(component))
    harmony_types = get_component_related_types(list(related_component.keys()))
    current_task_index = 0
    # print(related_component)
    system_prompt = PromptLoader.get_prompt("code_monkey/system.prompt")
    translate_layout_plan_prompt = PromptLoader.get_prompt(
        "code_monkey/translate_layout.prompt",
        tasks=layout_translation.tasks,
        current_task=layout_translation.tasks[current_task_index],
        android_layout={
            "name": "Button",
            "content": """<Button
            android:id="@+id/button_first"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/next"
            app:layout_constraintBottom_toTopOf="@id/textview_first"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />
        """
        },
        harmony_components=related_component,
        is_component_content=True,
        harmony_types=harmony_types,
        is_type_content=True,
        project_resources=resource
    )
    print(translate_layout_plan_prompt)
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": translate_layout_plan_prompt, "role": "user"}
    ], temperature=0.0)
    print(response.choices[0].message.content)
    print(response.usage)


def test_translate_component():
    components_name = ["Text", "Column"]
    android_component_name = "com.google.android.material.card.MaterialCardView"
    android_component = """<com.google.android.material.card.MaterialCardView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="16dp"
        app:cardBackgroundColor="#FF018786"
        app:cardCornerRadius="16dp"
        app:cardElevation="8dp"
        app:cardMaxElevation="12dp"
        app:cardPreventCornerOverlap="true"
        app:cardUseCompatPadding="true"
        app:contentPadding="16dp"
        app:strokeColor="#FF03DAC5"
        app:strokeWidth="2dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="16dp">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Card Title"
                android:textColor="#FFBB86FC"
                android:textSize="24sp"
                android:textStyle="bold" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="This is a sample description text for the card."
                android:textColor="#FF6200EE"
                android:textSize="16sp"
                android:paddingTop="8dp" />
        </LinearLayout>
    </com.google.android.material.card.MaterialCardView>"""
    android_component_prompt = f"""你是一个专业的安卓开发者，你的任务是为示例代码编写详细的功能与效果描述：
{android_component}
在编写时你需要遵守以下规则：
* 1. 详细描述该组件的主要功能和预期效果。
* 2. 不要给出任何代码示例。
    """
    related_harmony_components = {}
    for component_name in components_name:
        related_harmony_components.update(get_harmony_component(component_name))
    # print(related_harmony_components)
    related_harmony_types = get_component_related_types(list(related_harmony_components.keys()))
    android_layout = {
        "name": f"{android_component_name} Component",
        "content": android_component,
        "description": ""
    }
    current_task = {
        "done": False,
        "description": f"实现安卓组件{android_component_name}的代码转译，生成鸿蒙ArkUI的代码，你可以使用多个组件来实现该功能。",
    }
    system_prompt = PromptLoader.get_prompt("code_monkey/system.prompt")
    client = OpenAIClient(openai_default_config)
    # response = client.create(messages=[
    #     {"content": system_prompt, "role": "system"},
    #     {"content": android_component_prompt, "role": "user"}
    # ], temperature=1.0)
    # android_layout["description"] = response.choices[0].message.content
    # print(response.choices[0].message.content)
    translate_layout_prompt = PromptLoader.get_prompt(
        "code_monkey/translate_layout.prompt",
        tasks=[current_task],
        current_task=current_task,
        android_layout=android_layout,
        harmony_components=related_harmony_components,
        is_component_content=True,
        harmony_types=related_harmony_types,
        is_type_content=True,
        project_resources=resource
    )
    print(translate_layout_prompt)
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": translate_layout_prompt, "role": "user"}
    ], temperature=0.0)
    print(response.choices[0].message.content)
    print(response.usage)