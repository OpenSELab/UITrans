import os
import time
import zipfile
import re

import gradio
import shortuuid
from tqdm import tqdm
import gradio as gr
from android.main import analyse_page_dict
from android.base import AndroidProjConfig
from core.config.config_loader import ConfigLoader
from core.llms import LLMFactory
from core.pilot.code_monkey import CodeMonkeyAgent
from core.pilot.developer import DeveloperAgent
from core.pilot.schema import BreakdownAndroidLayout, BreakdownLayoutTranslation

config = ConfigLoader.from_file("config.yaml")
component_name_pattern = re.compile(r"<\s*([\w\.]+)")

all_examples = {
    "component": [

    ]
}


def get_llm_client():
    llm_client = LLMFactory.create_llm_from_config(
        llm_client_type="openai",
        llm_config=config.llm_config["deepseek"].model_dump(),
        generate_config={
            "temperature": 0.01
        }
    )
    return llm_client


# Define a function to convert Android XML components to HarmonyOS code.
def convert_android_component_to_harmony(android_xml):
    # 初始化llm
    llm_client = get_llm_client()
    code_monkey_agent = CodeMonkeyAgent(llm_client=llm_client)
    breakdown_android_layout = BreakdownAndroidLayout(
        tasks=[{
            "done": False,
            "description": "将安卓组件代码转译为鸿蒙ArkUI组件代码，以便在鸿蒙系统中使用。",
            "component": {
                "name": component_name_pattern.findall(android_xml),
                "content": android_xml
            }
        }]
    )
    translations, agent_state = code_monkey_agent.translate_component_v1(breakdown_android_layout)
    harmonyos_code = translations[0].target_component_code
    return harmonyos_code


def convert_android_page_to_harmony(android_xml):
    # 初始化llm
    tqdm_progress = tqdm(total=100, desc="转译进度")
    llm_client = get_llm_client()
    code_monkey_agent = CodeMonkeyAgent(llm_client=llm_client)
    developer_agent = DeveloperAgent(llm_client=llm_client)
    android_layout_xml_name = "example.xml"
    android_layouts = {
        android_layout_xml_name: {
            "name": android_layout_xml_name,
            "content": android_xml
        }
    }
    layout_translation = BreakdownLayoutTranslation(
        tasks=[{
            "description": f"将{android_layout_xml_name}转译为对应的Harmony页面",
            "done": False,
            "android": android_layout_xml_name,
            "harmony": "ets/pages/Index.ets"
        }]
    )
    tqdm_progress.update(10)
    breakdown_android_layout = developer_agent.breakdown_android_layout(layout_translation, android_layouts)
    tqdm_progress.update(30)
    translations, agent_state = code_monkey_agent.translate_component_v1(breakdown_android_layout)
    tqdm_progress.update(80)
    code_block_pattern = r"```(?:\w+)?\n([\s\S]*?)```"
    assemble_result = developer_agent.assemble_harmony_layout(breakdown_android_layout,
                                                              android_layouts[android_layout_xml_name], translations)
    tqdm_progress.update(100)
    code_block_match = re.search(code_block_pattern, assemble_result)
    if code_block_match:
        harmonyos_code = code_block_match.group(1)
    else:
        harmonyos_code = assemble_result
    tqdm_progress.close()
    return harmonyos_code


def parse_android_project(android_zip):
    if not zipfile.is_zipfile(android_zip):
        gr.Warning("错误: 无效的 zip 文件!")
        return False, None
    unzip_dir = f"android_projects/{shortuuid.uuid()}"
    print(unzip_dir)
    os.makedirs(unzip_dir, exist_ok=True)

    with zipfile.ZipFile(android_zip, 'r') as zip_ref:
        print(zip_ref.namelist())
        file_list = zip_ref.namelist()
        root_folders = set(file.split('/')[0] for file in file_list if '/' in file)
        if len(root_folders) == 1:
            root_folder = root_folders.pop()
            print("根目录文件：", root_folder)
        else:
            gr.Warning("错误: .zip文件中没有唯一的根目录文件夹!")
            return False, None
        zip_ref.extractall(unzip_dir)
        print(f"Android项目已解压到: {unzip_dir}")
        proj_root = os.path.join(unzip_dir, root_folder)
        print(f"Android项目根目录为：{proj_root}")
        android_config = AndroidProjConfig()
        android_config.PROJ_NAME = os.path.basename(proj_root)
        android_config.PROJECT_ROOT = proj_root
        output_dir = analyse_page_dict(unzip_dir, android_config)

    return True, output_dir


def convert_android_project_to_harmony(project_id):
    # Simple conversion logic (this is a placeholder, actual conversion logic should be implemented)
    for i in tqdm(range(100), desc="转译进度"):
        if i == 99:
            yield "完成"
        else:
            yield f"进度: {i}"
            time.sleep(0.1)


# Create a Gradio Blocks app with a single tab for component conversion.
css = """
.tab-container button {
  font-size: 20px;
}
"""
with gr.Blocks(css=css) as app:
    html_content = """
    <div style="display: flex; align-items: center; justify-content: center; height: 30vh; padding: 10px; margin: 0 auto;">
        <div style="margin-right: 10px;">
            <img src="https://hyj-first-1306572465.cos.ap-nanjing.myqcloud.com/a2h_logo.svg" alt="Logo Image" style="width: 200px; height: 200px;">
        </div>
        <div>
            <h1 style="font-size: 64px; color: black;">A2H Converter</h1>
            <p style="font-size: 16px; color: gray;">一款支持安卓UI到鸿蒙ArkUI的智能转译工具</p>
        </div>
    </div>
    """
    gr.HTML(html_content)
    with gr.Tab("组件转译"):
        gr.Markdown("## 组件转译")
        gr.Markdown("请在下列输入框中粘贴 Android XML 组件代码，然后点击“确定”按钮以将其转译为 HarmonyOS 代码。")
        android_xml_input = gr.TextArea(label="输入 Android XML 组件", lines=20, max_lines=100)
        convert_button = gr.Button("确定")
        harmonyos_output = gr.TextArea(label="输出 HarmonyOS 代码", lines=10, max_lines=100)
        component_progress = gr.Progress(track_tqdm=True)
        # Define the event listener for the button click.
        convert_button.click(convert_android_component_to_harmony, inputs=android_xml_input, outputs=harmonyos_output)

        component_examples = gr.Examples(
            examples=[
                "<CheckBox\n        android:id=\"@+id/chbOne\"\n        android:layout_width=\"wrap_content\"\n        android:layout_height=\"wrap_content\"\n        android:checked=\"true\"\n        android:text=\"吃饭\" />",
                "<RatingBar\n        android:id=\"@+id/rating1\"\n        android:layout_width=\"wrap_content\"\n        android:layout_height=\"wrap_content\"\n        android:numStars=\"5\"\n        android:stepSize=\"0.5\"\n        android:rating=\"3\"\n        android:isIndicator=\"false\" />",
                "<EditText\nandroid:id=ght=\"50dp\"\nandroid:layout_marginBottom=\"15dp\"\nandroid:autofillHints=\"\"\nandroid:hint=\"请输入文字\"\nandroid:inputType=\"text\"\nandroid:paddingLeft=\"15dp\"\nandroid:paddingRight=\"15dp\"\nandroid:textColor=\"@color/black\"\nandroid:textSize=\"16sp\" />"
            ],
            inputs=[android_xml_input],
        )
    with gr.Tab("页面转译"):
        gr.Markdown("## 页面转译")
        gr.Markdown("请在下列输入框中粘贴 Android XML 页面代码，然后点击“确定”按钮以将其转译为 HarmonyOS 代码。")
        android_xml_input = gr.TextArea(label="输入 Android XML 页面", lines=20, max_lines=100)
        convert_button = gr.Button("确定")
        harmonyos_output = gr.TextArea(label="输出 HarmonyOS 代码", lines=10, max_lines=100)
        page_progress = gr.Progress(track_tqdm=True)
        # Define the event listener for the button click.
        convert_button.click(convert_android_page_to_harmony, inputs=android_xml_input, outputs=harmonyos_output)

        page_examples = gr.Examples(
            examples=[
                "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<androidx.core.widget.NestedScrollView xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    xmlns:tools=\"http://schemas.android.com/tools\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    tools:context=\".FirstFragment\">\n\n    <androidx.constraintlayout.widget.ConstraintLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:padding=\"16dp\">\n\n        <Button\n            android:id=\"@+id/button_first\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:text=\"@string/next\"\n            app:layout_constraintBottom_toTopOf=\"@id/textview_first\"\n            app:layout_constraintEnd_toEndOf=\"parent\"\n            app:layout_constraintStart_toStartOf=\"parent\"\n            app:layout_constraintTop_toTopOf=\"parent\" />\n\n        <TextView\n            android:id=\"@+id/textview_first\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginTop=\"16dp\"\n            android:text=\"@string/lorem_ipsum\"\n            app:layout_constraintBottom_toBottomOf=\"parent\"\n            app:layout_constraintEnd_toEndOf=\"parent\"\n            app:layout_constraintStart_toStartOf=\"parent\"\n            app:layout_constraintTop_toBottomOf=\"@id/button_first\" />\n    </androidx.constraintlayout.widget.ConstraintLayout>\n</androidx.core.widget.NestedScrollView>",
                "<androidx.coordinatorlayout.widget.CoordinatorLayout\n    xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:fitsSystemWindows=\"true\">\n\n    <ImageView\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:scaleType=\"centerCrop\"\n        android:src=\"@drawable/appbackground\"/>\n\n    <com.google.android.material.appbar.AppBarLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"?attr/actionBarSize\"\n        android:fitsSystemWindows=\"true\">\n\n        <androidx.appcompat.widget.Toolbar\n            android:id=\"@+id/toolbar\"\n            android:layout_width=\"match_parent\"\n            android:layout_height=\"wrap_content\"\n            android:background=\"?attr/colorPrimary\"\n            android:fitsSystemWindows=\"true\"\n            android:minHeight=\"?attr/actionBarSize\"\n            android:title=\"@string/action_about\"\n            app:layout_scrollFlags=\"scroll|enterAlways\"\n            app:popupTheme=\"@style/ThemeOverlay.AppCompat.Light\"\n            app:theme=\"@style/ThemeOverlay.AppCompat.Dark.ActionBar\"\n            />\n\n\n    </com.google.android.material.appbar.AppBarLayout>\n\n    <ScrollView\n        android:id=\"@+id/nestedScrollView\"\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:layout_marginTop=\"?attr/actionBarSize\"\n        android:fitsSystemWindows=\"true\"\n        >\n\n        <LinearLayout\n            android:layout_width=\"match_parent\"\n            android:layout_height=\"wrap_content\"\n            android:orientation=\"vertical\"\n            android:paddingBottom=\"@dimen/activity_vertical_margin\"\n            android:paddingTop=\"@dimen/activity_vertical_margin\">\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\">\n\n                    <TextView\n                            android:id=\"@+id/text_view_about\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"24dp\"\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:layout_marginTop=\"16dp\"\n                            android:breakStrategy=\"high_quality\"\n                            android:hyphenationFrequency=\"full\"\n                            android:text=\"@string/heading_about\"\n                            android:textAppearance=\"?android:attr/textAppearanceMedium\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"16sp\">\n\n                        <requestFocus/>\n                    </TextView>\n                </LinearLayout>\n            </androidx.cardview.widget.CardView>\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\"\n                        android:padding=\"8dp\">\n\n                    <ImageView\n                            android:id=\"@+id/imageViewLogo\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"200dp\"\n                            android:layout_gravity=\"center\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"8dp\"\n                            android:layout_marginRight=\"8dp\"\n                            android:layout_marginTop=\"8dp\"\n                            app:srcCompat=\"@drawable/bookdash_logo\"/>\n\n\n                </LinearLayout>\n\n            </androidx.cardview.widget.CardView>\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\">\n\n                    <TextView\n                            android:id=\"@+id/textViewHeading\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:layout_marginTop=\"16dp\"\n                            android:text=\"@string/why_bookdash_heading\"\n                            android:textAppearance=\"?android:attr/textAppearanceLarge\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"24sp\"/>\n\n                    <TextView\n                            android:id=\"@+id/text_why_bookdash\"\n                            style=\"@style/TextAppearance.AppCompat.Medium\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"16dp\"\n\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:breakStrategy=\"high_quality\"\n                            android:fontFamily=\"sans-serif\"\n                            android:hyphenationFrequency=\"normal\"\n                            android:text=\"@string/why_bookdash\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"16sp\"/>\n\n                    <Button\n                            android:id=\"@+id/button_learn_more\"\n                            style=\"@style/Widget.AppCompat.Button.Borderless\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"8dp\"\n                            android:layout_marginRight=\"8dp\"\n                            android:fontFamily=\"sans-serif\"\n                            android:text=\"@string/learn_more\"\n                            android:textColor=\"@color/colorAccent\"/>\n                </LinearLayout>\n\n            </androidx.cardview.widget.CardView>\n\n\n        </LinearLayout>\n\n\n    </ScrollView>\n\n</androidx.coordinatorlayout.widget.CoordinatorLayout>\n\n\n"
            ],
            inputs=[android_xml_input],
        )
    with gr.Tab("项目转译"):
        gr.Markdown("## 项目转译")
        gr.Markdown("请在下列文件上传框中上传 Android 项目的 Zip 压缩包，然后点击“确定”按钮以将其转译为 HarmonyOS 代码。")
        android_xml_zip_input = gr.File(label="上传 Android 项目压缩包")
        convert_button = gr.Button("确定", interactive=True)
        message_output = gr.Text(label="转译进度", interactive=False, lines=1, max_lines=1, autoscroll=True)
        download_button = gr.Button("下载", interactive=True)
        project_progress_bar = gr.Progress(track_tqdm=True)

        # 存储解析后的内容
        android_xml_parsed_content = ""


        def handle_parse_android_project(_android_xml_zip):
            android_xml_parsed_flag, android_xml_parsed_content = parse_android_project(_android_xml_zip)
            if android_xml_parsed_flag:
                print(f"解析返回文件夹路径为：{android_xml_parsed_content}")
                return "解析成功，点击确定按钮开始转译"
            else:
                return "解析失败，请上传正确的 Android 项目 Zip 压缩包"


        def handle_convert_android_project_to_harmony():
            for message in convert_android_project_to_harmony(android_xml_parsed_content):
                yield message


        def handle_download_harmony_project():
            return "文件路径"


        # Define the event listener for the file upload.
        android_xml_zip_input.upload(handle_parse_android_project, inputs=android_xml_zip_input,
                                     outputs=[message_output])
        convert_button.click(handle_convert_android_project_to_harmony, inputs=[], outputs=[message_output])
        # Define the event listener for the button click.
        download_button.click(handle_download_harmony_project, inputs=[], outputs=gr.File())

# Launch the Gradio app.
if __name__ == "__main__":
    # 设置队列最大为20，最大并发数为3
    app.queue(max_size=20, default_concurrency_limit=3).launch(show_error=True, share=True, show_api=False)
