import os
import time
import zipfile

import shortuuid
from tqdm import tqdm
import gradio as gr
from android.base import android_config
from android.main import analyse_page_dict


# Define a function to convert Android XML components to HarmonyOS code.
def convert_android_component_to_harmony(android_xml):
    # Simple conversion logic (this is a placeholder, actual conversion logic should be implemented)
    harmonyos_code = android_xml.replace("android:", "harmony:")
    return harmonyos_code


def convert_android_page_to_harmony(android_xml):
    # Simple conversion logic (this is a placeholder, actual conversion logic should be implemented)
    harmonyos_code = android_xml.replace("android:", "harmony:")
    return harmonyos_code


def parse_android_project(android_zip):
    if not zipfile.is_zipfile(android_zip):
        gr.Warning("错误: 无效的 zip 文件!")
        return False, None
    unzip_dir = f"./android_projects/{shortuuid.uuid()}/"
    print(unzip_dir)
    os.makedirs(unzip_dir, exist_ok=True)

    with zipfile.ZipFile(android_zip, 'r') as zip_ref:
        root_dirs = list(file for file in zip_ref.namelist() if file.endswith('/') and file.count('/') == 1)
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
        android_config.PROJ_NAME = os.path.basename(proj_root)
        android_config.PROJECT_ROOT = proj_root
        analyse_page_dict(unzip_dir)

    return True, unzip_dir


def convert_android_project_to_harmony(project_id):
    # Simple conversion logic (this is a placeholder, actual conversion logic should be implemented)
    for i in tqdm(range(100), desc="转译进度"):
        if i == 99:
            yield "完成"
        else:
            yield f"进度: {i}"
            time.sleep(0.1)


# Create a Gradio Blocks app with a single tab for component conversion.
with gr.Blocks() as app:
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

        # Define the event listener for the button click.
        convert_button.click(convert_android_component_to_harmony, inputs=android_xml_input, outputs=harmonyos_output)
    with gr.Tab("页面转译"):
        gr.Markdown("## 页面转译")
        gr.Markdown("请在下列输入框中粘贴 Android XML 页面代码，然后点击“确定”按钮以将其转译为 HarmonyOS 代码。")
        android_xml_input = gr.TextArea(label="输入 Android XML 页面", lines=20, max_lines=100)
        convert_button = gr.Button("确定")
        harmonyos_output = gr.TextArea(label="输出 HarmonyOS 代码", lines=10, max_lines=100)

        # Define the event listener for the button click.
        convert_button.click(convert_android_page_to_harmony, inputs=android_xml_input, outputs=harmonyos_output)
    with gr.Tab("项目转译"):
        gr.Markdown("## 项目转译")
        gr.Markdown("请在下列文件上传框中上传 Android 项目的 Zip 压缩包，然后点击“确定”按钮以将其转译为 HarmonyOS 代码。")
        android_xml_zip_input = gr.File(label="上传 Android 项目压缩包")
        convert_button = gr.Button("确定", interactive=True)
        message_output = gr.Text(label="转译进度", interactive=False, lines=1, max_lines=1, autoscroll=True)
        download_button = gr.Button("下载", interactive=True)

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
    app.launch(show_error=True, share=True, show_api=False)
