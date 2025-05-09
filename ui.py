import json
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
from core.translator import init_harmony_from_android

config = ConfigLoader.from_file("config.yaml")
component_name_pattern = re.compile(r"<\s*([\w\.]+)")


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
    if not android_xml:
        gr.Warning("错误: 请先输入 Android XML 组件代码!")
        return ""
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
    if not android_xml:
        gr.Warning("错误: 请先输入 Android XML 页面代码!")
        return ""
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


def convert_android_project_to_harmony(android_project_path_id):
    if not android_project_path_id:
        gr.Warning("错误: 请上传 Android 项目 Zip 压缩包并等待解析完成!")
        return "请先上传 Android 项目 Zip 压缩包!", None
    project_progress_bar = tqdm(total=100, desc="转译进度")
    parsed_android_project_path = android_project_path_id
    parsed_page_filepath = os.path.join(parsed_android_project_path, "page_data.json")
    base_harmony_project_path = parsed_android_project_path.replace("android_projects", "harmony_projects")
    harmony_project_path = base_harmony_project_path + "-harmony"
    harmony_project_log_path = base_harmony_project_path + "_log.json"
    os.makedirs(harmony_project_path, exist_ok=True)
    project_progress_bar.update(5)
    # 初始化项目
    init_harmony_from_android(
        parsed_android_project_path,
        harmony_project_path
    )
    project_progress_bar.update(10)
    # 将页面拉伸
    with open(parsed_page_filepath, "r", encoding="utf-8") as f:
        page_tasks = json.loads(f.read())
    page_num = len(page_tasks)
    llm_client = get_llm_client()
    code_monkey_agent = CodeMonkeyAgent(llm_client=llm_client)
    developer_agent = DeveloperAgent(llm_client=llm_client)
    project_progress_bar.update(15)
    start_time = time.time()
    for i, (android_layout_xml_name, android_layout_xml_dict) in enumerate(page_tasks.items()):
        android_page_name = android_layout_xml_name.replace("\\", "/").split("/")[-1].strip(".xml")
        words = reversed(android_page_name.split("_"))
        harmony_page_name = "".join([word.capitalize() for word in words])
        android_layouts = {
            android_layout_xml_name: android_layout_xml_dict
        }
        layout_translation = BreakdownLayoutTranslation(
            tasks=[{
                "description": f"将{android_layout_xml_name}转译为对应的Harmony页面",
                "done": False,
                "android": android_layout_xml_name,
                "harmony": f"ets/pages/{harmony_page_name}.ets"
            }]
        )
        breakdown_android_layout = developer_agent.breakdown_android_layout(layout_translation, android_layouts)
        translations, agent_state = code_monkey_agent.translate_component_v1(breakdown_android_layout)
        code_block_pattern = r"```(?:\w+)?\n([\s\S]*?)```"
        assemble_result = developer_agent.assemble_harmony_layout(breakdown_android_layout,
                                                                  android_layouts[android_layout_xml_name],
                                                                  translations)
        end_time = time.time()
        with open(harmony_project_log_path, "w", encoding="utf-8") as f:
            f.write(json.dumps({
                "android_layout": android_layouts[android_layout_xml_name],
                "breakdown_android_layout": breakdown_android_layout.model_dump(),
                "translations": [translation.model_dump() for translation in translations],
                "translation_agent_task": agent_state.model_dump(),
                "assemble_harmony_layout": assemble_result,
                "time": end_time - start_time
            }, ensure_ascii=False))
        code_block_match = re.search(code_block_pattern, assemble_result)
        if code_block_match:
            harmonyos_code = code_block_match.group(1)
        else:
            harmonyos_code = assemble_result
        with open(
                os.path.join(harmony_project_path, "entry", "src", "main", "ets", "pages", f"{harmony_page_name}.ets"),
                "w", encoding="utf-8") as f:
            f.write(harmonyos_code)
        project_progress_bar.update((i + 1) / page_num)
    project_progress_bar.update(100)
    zipped_harmony_project_path = handle_download_harmony_project(harmony_project_path)
    return "转译完成，点击 Zip 压缩包即可下载", zipped_harmony_project_path


def handle_download_harmony_project(harmony_project_path: str):
    if not harmony_project_path:
        gr.Warning("错误: 请先转译 Android 项目!")
        return ""
    zip_file_path = f"{harmony_project_path}.zip"
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for root, dirs, files in os.walk(harmony_project_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, harmony_project_path)
                zip_ref.write(file_path, arcname)
    return zip_file_path


# Create a Gradio Blocks app with a single tab for component conversion.
global_css = """
.tab-container button {
  font-size: 20px;
}
.demo-video {
    display: flex;
    align-items: center;
    justify-content: center;
}
.demo-video iframe {
    width: 960px;
    height: 642px;
}
"""

all_examples = {
    "components": [
        [
            "CheckBox",
            "<CheckBox\n        android:id=\"@+id/chbOne\"\n        android:layout_width=\"wrap_content\"\n        android:layout_height=\"wrap_content\"\n        android:checked=\"true\"\n        android:text=\"吃饭\" />",
            "examples/images/checkbox.png"
        ],
        [
            "RatingBar",
            "<RatingBar\n        android:id=\"@+id/rating1\"\n        android:layout_width=\"wrap_content\"\n        android:layout_height=\"wrap_content\"\n        android:numStars=\"5\"\n        android:stepSize=\"0.5\"\n        android:rating=\"3\"\n        android:isIndicator=\"false\" />",
            "examples/images/ratingbar.png"
        ],
        [
            "EditText",
            "<EditText\nandroid:id=ght=\"50dp\"\nandroid:layout_marginBottom=\"15dp\"\nandroid:autofillHints=\"\"\nandroid:hint=\"请输入文字\"\nandroid:inputType=\"text\"\nandroid:paddingLeft=\"15dp\"\nandroid:paddingRight=\"15dp\"\nandroid:textColor=\"@color/black\"\nandroid:textSize=\"16sp\" />",
            "examples/images/edittext.png"
        ]
    ],
    "pages": [
        [
            "页面1",
            "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<androidx.core.widget.NestedScrollView xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    xmlns:tools=\"http://schemas.android.com/tools\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    tools:context=\".FirstFragment\">\n\n    <androidx.constraintlayout.widget.ConstraintLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:padding=\"16dp\">\n\n        <Button\n            android:id=\"@+id/button_first\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:text=\"@string/next\"\n            app:layout_constraintBottom_toTopOf=\"@id/textview_first\"\n            app:layout_constraintEnd_toEndOf=\"parent\"\n            app:layout_constraintStart_toStartOf=\"parent\"\n            app:layout_constraintTop_toTopOf=\"parent\" />\n\n        <TextView\n            android:id=\"@+id/textview_first\"\n            android:layout_width=\"wrap_content\"\n            android:layout_height=\"wrap_content\"\n            android:layout_marginTop=\"16dp\"\n            android:text=\"@string/lorem_ipsum\"\n            app:layout_constraintBottom_toBottomOf=\"parent\"\n            app:layout_constraintEnd_toEndOf=\"parent\"\n            app:layout_constraintStart_toStartOf=\"parent\"\n            app:layout_constraintTop_toBottomOf=\"@id/button_first\" />\n    </androidx.constraintlayout.widget.ConstraintLayout>\n</androidx.core.widget.NestedScrollView>",
            "examples/images/page1.png"
        ],
        [
            "页面2",
            "<androidx.coordinatorlayout.widget.CoordinatorLayout\n    xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n    android:layout_width=\"match_parent\"\n    android:layout_height=\"match_parent\"\n    android:fitsSystemWindows=\"true\">\n\n    <ImageView\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:scaleType=\"centerCrop\"\n        android:src=\"@drawable/appbackground\"/>\n\n    <com.google.android.material.appbar.AppBarLayout\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"?attr/actionBarSize\"\n        android:fitsSystemWindows=\"true\">\n\n        <androidx.appcompat.widget.Toolbar\n            android:id=\"@+id/toolbar\"\n            android:layout_width=\"match_parent\"\n            android:layout_height=\"wrap_content\"\n            android:background=\"?attr/colorPrimary\"\n            android:fitsSystemWindows=\"true\"\n            android:minHeight=\"?attr/actionBarSize\"\n            android:title=\"@string/action_about\"\n            app:layout_scrollFlags=\"scroll|enterAlways\"\n            app:popupTheme=\"@style/ThemeOverlay.AppCompat.Light\"\n            app:theme=\"@style/ThemeOverlay.AppCompat.Dark.ActionBar\"\n            />\n\n\n    </com.google.android.material.appbar.AppBarLayout>\n\n    <ScrollView\n        android:id=\"@+id/nestedScrollView\"\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"match_parent\"\n        android:layout_marginTop=\"?attr/actionBarSize\"\n        android:fitsSystemWindows=\"true\"\n        >\n\n        <LinearLayout\n            android:layout_width=\"match_parent\"\n            android:layout_height=\"wrap_content\"\n            android:orientation=\"vertical\"\n            android:paddingBottom=\"@dimen/activity_vertical_margin\"\n            android:paddingTop=\"@dimen/activity_vertical_margin\">\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\">\n\n                    <TextView\n                            android:id=\"@+id/text_view_about\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"24dp\"\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:layout_marginTop=\"16dp\"\n                            android:breakStrategy=\"high_quality\"\n                            android:hyphenationFrequency=\"full\"\n                            android:text=\"@string/heading_about\"\n                            android:textAppearance=\"?android:attr/textAppearanceMedium\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"16sp\">\n\n                        <requestFocus/>\n                    </TextView>\n                </LinearLayout>\n            </androidx.cardview.widget.CardView>\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\"\n                        android:padding=\"8dp\">\n\n                    <ImageView\n                            android:id=\"@+id/imageViewLogo\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"200dp\"\n                            android:layout_gravity=\"center\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"8dp\"\n                            android:layout_marginRight=\"8dp\"\n                            android:layout_marginTop=\"8dp\"\n                            app:srcCompat=\"@drawable/bookdash_logo\"/>\n\n\n                </LinearLayout>\n\n            </androidx.cardview.widget.CardView>\n\n            <androidx.cardview.widget.CardView\n                    android:layout_width=\"match_parent\"\n                    android:layout_height=\"wrap_content\"\n                    android:layout_marginBottom=\"4dp\"\n                    android:layout_marginLeft=\"@dimen/activity_horizontal_margin\"\n                    android:layout_marginRight=\"@dimen/activity_horizontal_margin\"\n\n                    android:layout_marginTop=\"4dp\"\n                    android:padding=\"16dp\"\n                    app:cardCornerRadius=\"8dp\">\n\n                <LinearLayout\n                        android:layout_width=\"match_parent\"\n                        android:layout_height=\"wrap_content\"\n                        android:orientation=\"vertical\">\n\n                    <TextView\n                            android:id=\"@+id/textViewHeading\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:layout_marginTop=\"16dp\"\n                            android:text=\"@string/why_bookdash_heading\"\n                            android:textAppearance=\"?android:attr/textAppearanceLarge\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"24sp\"/>\n\n                    <TextView\n                            android:id=\"@+id/text_why_bookdash\"\n                            style=\"@style/TextAppearance.AppCompat.Medium\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"16dp\"\n\n                            android:layout_marginLeft=\"16dp\"\n                            android:layout_marginRight=\"16dp\"\n                            android:breakStrategy=\"high_quality\"\n                            android:fontFamily=\"sans-serif\"\n                            android:hyphenationFrequency=\"normal\"\n                            android:text=\"@string/why_bookdash\"\n                            android:textIsSelectable=\"true\"\n                            android:textSize=\"16sp\"/>\n\n                    <Button\n                            android:id=\"@+id/button_learn_more\"\n                            style=\"@style/Widget.AppCompat.Button.Borderless\"\n                            android:layout_width=\"wrap_content\"\n                            android:layout_height=\"wrap_content\"\n                            android:layout_marginBottom=\"8dp\"\n                            android:layout_marginLeft=\"8dp\"\n                            android:layout_marginRight=\"8dp\"\n                            android:fontFamily=\"sans-serif\"\n                            android:text=\"@string/learn_more\"\n                            android:textColor=\"@color/colorAccent\"/>\n                </LinearLayout>\n\n            </androidx.cardview.widget.CardView>\n\n\n        </LinearLayout>\n\n\n    </ScrollView>\n\n</androidx.coordinatorlayout.widget.CoordinatorLayout>\n\n\n",
            "examples/images/page2.png"
        ]
    ],
    "projects": [
        ["javademo", "examples/javademo.zip"]
    ]
}

with gr.Blocks(css=global_css) as app:
    html_content = f"""
        <div style="display: flex; align-items: center; justify-content: center; height: 28vh; padding: 10px; margin: 0 auto;">
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
    # gr.Video("examples/video/demo.mp4", label="演示视频", width=960)
    video_url = "https://outin-3bb925968a2f11ef940e00163e0edab2.oss-cn-shanghai.aliyuncs.com/sv/1d60ba83-1928e88ad92/1d60ba83-1928e88ad92.mp4?Expires=1728972131&OSSAccessKeyId=LTAIVVfYx6D0HeL2&Signature=KO1BpcEfclEjBqKGYAtriaiLN%2Fo%3D"
    gr.HTML(f"""
        <div class="demo-video">
            <iframe src="{video_url}" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
        </div>
    """)
    with gr.Tab("组件转译"):
        gr.Markdown("## 组件转译")
        gr.Markdown("请在下列输入框中粘贴 Android XML 组件代码，然后点击“确定”按钮以将其转译为 HarmonyOS 代码。")
        android_xml_input = gr.TextArea(label="输入 Android XML 组件", lines=10, max_lines=100)
        component_example_image = gr.Image(visible=True, label="示意图")
        convert_button = gr.Button("确定")
        harmonyos_output = gr.TextArea(label="输出 HarmonyOS 代码", lines=10, max_lines=100)
        component_progress = gr.Progress(track_tqdm=True)
        # Define the event listener for the button click.
        convert_button.click(convert_android_component_to_harmony, inputs=android_xml_input, outputs=harmonyos_output)
        component_examples = gr.Examples(
            examples=all_examples["components"],
            inputs=[gr.Text(visible=False, label="组件名"), android_xml_input, component_example_image],
        )
    with gr.Tab("页面转译"):
        gr.Markdown("## 页面转译")
        gr.Markdown("请在下列输入框中粘贴 Android XML 页面代码，然后点击“确定”按钮以将其转译为 HarmonyOS 代码。")
        android_xml_input = gr.TextArea(label="输入 Android XML 页面", lines=20, max_lines=100)
        page_example_image = gr.Image(visible=True, height=300, label="示意图")
        convert_button = gr.Button("确定")
        harmonyos_output = gr.TextArea(label="输出 HarmonyOS 代码", lines=10, max_lines=100)
        page_progress = gr.Progress(track_tqdm=True)
        # Define the event listener for the button click.
        convert_button.click(convert_android_page_to_harmony, inputs=android_xml_input, outputs=harmonyos_output)

        page_examples = gr.Examples(
            examples=all_examples["pages"],
            inputs=[gr.Text(visible=False, label="页面名"), android_xml_input, page_example_image],
        )
    with gr.Tab("项目转译"):
        gr.Markdown("## 项目转译")
        gr.Markdown("请在下列文件上传框中上传 Android 项目的 Zip 压缩包，然后点击“确定”按钮以将其转译为 HarmonyOS 代码。")
        android_xml_zip_input = gr.File(label="上传 Android 项目压缩包")
        message_output = gr.Text(label="转译进度", interactive=False, lines=1, max_lines=1, autoscroll=True)
        convert_button = gr.Button("开始转译", interactive=True)
        project_progress_bar = gr.Progress(track_tqdm=True)
        android_project_path_id_text = gr.Text("", visible=False, label="Android 项目路径")
        harmony_output = gr.File(label="下载 HarmonyOS 项目 Zip 压缩包")


        def handle_parse_android_project(_android_xml_zip):
            android_xml_parsed_flag, project_path_id = parse_android_project(_android_xml_zip)
            if android_xml_parsed_flag:
                print(f"解析返回文件夹路径为：{project_path_id}")
                return "解析成功，点击确定按钮开始转译", project_path_id
            else:
                return "解析失败，请上传正确的 Android 项目 Zip 压缩包", ""


        def handle_parse_android_project1(_, _android_xml_zip):
            android_xml_parsed_flag, project_path_id = parse_android_project(_android_xml_zip)
            if android_xml_parsed_flag:
                print(f"解析返回文件夹路径为：{project_path_id}")
                return "解析成功，点击确定按钮开始转译", project_path_id
            else:
                return "解析失败，请上传正确的 Android 项目 Zip 压缩包", ""


        project_examples = gr.Examples(
            examples=all_examples["projects"],
            inputs=[gr.Text(visible=False, label="项目名"), android_xml_zip_input],
            run_on_click=True,
            fn=handle_parse_android_project1,
            outputs=[message_output, android_project_path_id_text]
        )

        android_xml_zip_input.upload(handle_parse_android_project, inputs=android_xml_zip_input,
                                     outputs=[message_output, android_project_path_id_text])
        convert_button.click(convert_android_project_to_harmony, inputs=[android_project_path_id_text],
                             outputs=[message_output, harmony_output])

# Launch the Gradio app.
if __name__ == "__main__":
    # 设置队列最大为20，最大并发数为3
    app.queue(max_size=20, default_concurrency_limit=3).launch(show_error=True, share=False, show_api=False)
