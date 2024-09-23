import json
import os
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.component.components import get_harmony_component
from core.pilot.harmony.resource import load_harmony_resource
from core.pilot.harmony.utils import get_component_related_types
from core.pilot.schema import BreakdownLayoutTranslation, ChooseComponent, Files, BreakdownComponentTranslation
from core.prompt.prompt_loader import PromptLoader
from template import HarmonyEmptyAbilityV5ProjectTemplate
from core.llms.oai_client import OpenAIClient

os.chdir("../")

ConfigLoader.from_file("./config.yaml")
harmony_template = HarmonyEmptyAbilityV5ProjectTemplate()
openai_default_config = ConfigLoader.get_config().llm_config.get("deepseek").model_dump()
resource = load_harmony_resource(r"D:\Codes\ArkTS\dashbook\entry\src\main\resources")

import re


def extract_code_blocks(markdown_text):
    """从 Markdown 文本中提取代码块"""
    code_block_pattern = re.compile(r'```.*?\n(.*?)\n```', re.DOTALL)
    code_block_match = code_block_pattern.search(markdown_text)
    if code_block_match:
        return code_block_match.group(1)
    return markdown_text


def translate_layout_test():
    client = OpenAIClient(openai_default_config)

    layout_translation = BreakdownComponentTranslation.model_validate(json.loads(r"""
{
    "tasks": [
        {
            "description": "在ets/pages/HelpTutorialPage.ets文件中添加ScrollView组件，并设置其布局和样式与安卓布局文件中的ViewPager一致。",
            "done": false,
            "component": "<androidx.viewpager.widget.ViewPager\nandroid:id=\"@+id/activity_help_view_pager\"\nandroid:clipToPadding=\"false\"\nandroid:clipChildren=\"false\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nandroid:layout_above=\"@+id/linear_layout_indicator\">\n</androidx.viewpager.widget.ViewPager>"
        },
        {
            "description": "在ets/pages/HelpTutorialPage.ets文件中添加Divider组件，并设置其布局和样式与安卓布局文件中的View一致。",
            "done": false,
            "component": "<View android:layout_width=\"match_parent\"\nandroid:layout_above=\"@+id/linear_layout_indicator\"\nandroid:layout_height=\"1dp\"\nandroid:background=\"#E0E0E0\" />"
        },
        {
            "description": "在ets/pages/HelpTutorialPage.ets文件中添加Row组件，并设置其布局和样式与安卓布局文件中的LinearLayout一致。",
            "done": false,
            "component": "<LinearLayout\nandroid:id=\"@+id/linear_layout_indicator\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"56dp\"\nandroid:weightSum=\"1\"\nandroid:layout_alignParentBottom=\"true\"\nandroid:orientation=\"horizontal\">"
        },
        {
            "description": "在ets/pages/HelpTutorialPage.ets文件中的Row组件内添加Button组件，并设置其布局和样式与安卓布局文件中的Button一致。",
            "done": false,
            "component": "<Button\nandroid:id=\"@+id/activity_help_skip_textview\"\nandroid:layout_width=\"0dp\"\nandroid:layout_height=\"match_parent\"\nandroid:layout_alignParentBottom=\"true\"\nandroid:layout_centerInParent=\"true\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:fontFamily=\"sans-serif\"\nandroid:gravity=\"center\"\nandroid:text=\"@string/tutorial_skip\"\nandroid:textColor=\"@color/tutorial_buttonTextColor\"\nandroid:textSize=\"18sp\"\nandroid:layout_weight=\"0.25\" />"
        },
        {
            "description": "在ets/pages/HelpTutorialPage.ets文件中的Row组件内添加Blank组件，并设置其布局和样式与安卓布局文件中的CirclePageIndicator一致。",
            "done": false,
            "component": "<za.co.riggaroo.materialhelptutorial.view.CirclePageIndicator\nandroid:id=\"@+id/activity_help_view_page_indicator\"\nandroid:layout_width=\"0dp\"\nandroid:layout_height=\"wrap_content\"\nandroid:layout_above=\"@+id/activity_help_skip_textview\"\napp:fillColor=\"#41FFFFFF\"\napp:pageColor=\"#14FFFFFF\"\napp:radius=\"6dp\"\nandroid:layout_weight=\"0.5\"\napp:strokeColor=\"#E0E0E0\"\napp:strokeWidth=\"0dp\"\nandroid:layout_gravity=\"center_vertical\"\nandroid:minHeight=\"24dp\" />"
        },
        {
            "description": "在ets/pages/HelpTutorialPage.ets文件中的Row组件内添加Column组件，并设置其布局和样式与安卓布局文件中的LinearLayout一致。",
            "done": false,
            "component": "<LinearLayout\nandroid:layout_width=\"0dp\"\nandroid:layout_weight=\"0.25\"\nandroid:orientation=\"vertical\"\nandroid:layout_height=\"match_parent\">"
        },
        {
            "description": "在ets/pages/HelpTutorialPage.ets文件中的Column组件内添加Image组件，并设置其布局和样式与安卓布局文件中的ImageButton一致。",
            "done": false,
            "component": "<ImageButton\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nandroid:src=\"@drawable/ic_navigate_next\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:id=\"@+id/activity_next_button\"\nandroid:layout_margin=\"8dp\"\nandroid:visibility=\"visible\"\nandroid:padding=\"16dp\" />"
        },
        {
            "description": "在ets/pages/HelpTutorialPage.ets文件中的Column组件内添加Button组件，并设置其布局和样式与安卓布局文件中的Button一致。",
            "done": false,
            "component": "<Button\nandroid:id=\"@+id/activity_tutorial_done\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:fontFamily=\"sans-serif\"\nandroid:gravity=\"center\"\nandroid:text=\"@string/tutorial_done\"\nandroid:textColor=\"@color/tutorial_buttonTextColor\"\nandroid:textSize=\"18sp\"\nandroid:visibility=\"gone\" />"
        }
    ]
}
            """))
    choose_component = ChooseComponent.common_parse_raw("""
    {
      "components": [
        "Scroll",
        "Divider",
        "Row",
        "Column",
        "Button",
        "Image",
        "Blank"
      ]
    }
        """)
    related_component = {}
    for component in choose_component.components:
        related_component.update(get_harmony_component(component))
    harmony_types = get_component_related_types(list(related_component.keys()))
    current_task_index = 0
    android_layout = {
        "name": "materialhelptutorial/res/layout/activity_help_tutorial.xml",
        "content": "<RelativeLayout xmlns:android=\"http://schemas.android.com/apk/res/android\"\nxmlns:app=\"http://schemas.android.com/apk/res-auto\"\nandroid:layout_width=\"match_parent\"\nandroid:id=\"@+id/activity_help_root\"\nandroid:layout_height=\"match_parent\"\nandroid:orientation=\"vertical\">\n\n<androidx.viewpager.widget.ViewPager\nandroid:id=\"@+id/activity_help_view_pager\"\nandroid:clipToPadding=\"false\"\nandroid:clipChildren=\"false\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nandroid:layout_above=\"@+id/linear_layout_indicator\">\n\n</androidx.viewpager.widget.ViewPager>\n\n<View android:layout_width=\"match_parent\"\n\nandroid:layout_above=\"@+id/linear_layout_indicator\"\nandroid:layout_height=\"1dp\"\nandroid:background=\"#E0E0E0\"\n/>\n<LinearLayout\nandroid:id=\"@+id/linear_layout_indicator\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"56dp\"\nandroid:weightSum=\"1\"\nandroid:layout_alignParentBottom=\"true\"\nandroid:orientation=\"horizontal\">\n\n<Button\nandroid:id=\"@+id/activity_help_skip_textview\"\nandroid:layout_width=\"0dp\"\nandroid:layout_height=\"match_parent\"\nandroid:layout_alignParentBottom=\"true\"\nandroid:layout_centerInParent=\"true\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:fontFamily=\"sans-serif\"\nandroid:gravity=\"center\"\nandroid:text=\"@string/tutorial_skip\"\nandroid:textColor=\"@color/tutorial_buttonTextColor\"\nandroid:textSize=\"18sp\"\nandroid:layout_weight=\"0.25\" />\n\n<za.co.riggaroo.materialhelptutorial.view.CirclePageIndicator\nandroid:id=\"@+id/activity_help_view_page_indicator\"\nandroid:layout_width=\"0dp\"\nandroid:layout_height=\"wrap_content\"\nandroid:layout_above=\"@id/activity_help_skip_textview\"\napp:fillColor=\"#41FFFFFF\"\napp:pageColor=\"#14FFFFFF\"\napp:radius=\"6dp\"\nandroid:layout_weight=\"0.5\"\napp:strokeColor=\"#E0E0E0\"\napp:strokeWidth=\"0dp\"\nandroid:layout_gravity=\"center_vertical\"\nandroid:minHeight=\"24dp\" />\n\n<LinearLayout\nandroid:layout_width=\"0dp\"\nandroid:layout_weight=\"0.25\"\nandroid:orientation=\"vertical\"\nandroid:layout_height=\"match_parent\">\n<ImageButton\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nandroid:src=\"@drawable/ic_navigate_next\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:id=\"@+id/activity_next_button\"\nandroid:layout_margin=\"8dp\"\nandroid:visibility=\"visible\"\nandroid:padding=\"16dp\" />\n<Button\nandroid:id=\"@+id/activity_tutorial_done\"\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nstyle=\"@android:style/Widget.Holo.Button.Borderless\"\nandroid:fontFamily=\"sans-serif\"\nandroid:gravity=\"center\"\nandroid:text=\"@string/tutorial_done\"\nandroid:textColor=\"@color/tutorial_buttonTextColor\"\nandroid:textSize=\"18sp\"\nandroid:visibility=\"gone\" />\n</LinearLayout>\n\n</LinearLayout>\n\n\n</RelativeLayout>",
    }
    # print(related_component)
    system_prompt = PromptLoader.get_prompt("code_monkey/system.prompt")
    translate_layout_prompt = PromptLoader.get_prompt(
        "code_monkey/translate_layout.prompt",
        tasks=layout_translation.tasks,
        current_task=layout_translation.tasks[current_task_index],
        android_layout=android_layout,
        harmony_components=related_component,
        is_component_content=True,
        harmony_types=harmony_types,
        is_type_content=True,
        project_resources=resource
    )
    print(translate_layout_prompt)
    messages = [
        {"content": system_prompt, "role": "system"},
        {"content": translate_layout_prompt, "role": "user"}
    ]
    # while current_task_index < len(layout_translation.tasks):
    #     response = client.create(messages=messages, temperature=0.0)
    #     current_task_index += 1
    response = client.create(messages=messages, temperature=0.0)
    print(response.choices[0].message.content)
    harmony_code = extract_code_blocks(response.choices[0].message.content)
    current_task_index += 1
    messages.append({"content": response.choices[0].message.content, "role": "assistant"})
    translate_layout_prompt1 = PromptLoader.get_prompt(
        "code_monkey/translate_layout.prompt",
        tasks=layout_translation.tasks,
        current_task=layout_translation.tasks[current_task_index],
        android_layout=android_layout,
        arkts_layout={
            "name": "ets/pages/Index.ets",
            "content": harmony_code
        },
        harmony_components=related_component,
        is_component_content=True,
        harmony_types=harmony_types,
        is_type_content=True,
        project_resources=resource
    )
    messages.append({"content": translate_layout_prompt1, "role": "user"})
    print(translate_layout_prompt1)
    response = client.create(messages=messages, temperature=0.0)
    print(response.choices[0].message.content)
    print(response.usage)


def translate_component_test():
    components_name = ["Toggle"]
    android_component_name = "androidx.appcompat.widget.AppCompatToggleButton"
    android_component = """<androidx.appcompat.widget.AppCompatToggleButton
        android:id="@+id/toggle_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textOn="开"
        android:textOff="关"
        android:checked="false"/> <!-- 默认状态为关闭 -->"""
    android_component_prompt = f"""你是一个专业的安卓开发者，你的任务是为示例代码编写详细的功能与效果描述，同时指出组件的默认属性及默认效果：
{android_component}
在编写时你需要遵守以下规则：
* 1. 详细描述该组件的主要功能和预期效果。
* 2. 指出该组件的默认属性和默认效果。
* 3. 不要给出任何代码示例。
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
        # project_resources=resource
    )
    print(translate_layout_prompt)
    response = client.create(messages=[
        {"content": system_prompt, "role": "system"},
        {"content": translate_layout_prompt, "role": "user"}
    ], temperature=0.2)
    print(response.choices[0].message.content)
    print(response.usage)
    # response = client.create(messages=[
    #     {"content": system_prompt, "role": "system"},
    #     {"content": translate_layout_prompt, "role": "user"},
    #     {"content": response.choices[0].message.content, "role": "assistant"},
    #     {"content": "明明不存在indeterminate属性", "role": "user"}
    # ], temperature=0.2)
    # print(response.choices[0].message.content)
    # print(response.usage)


if __name__ == '__main__':
    translate_layout_test()
