import contextlib
import json
import os
import re
import subprocess
from typing import Literal, Tuple, List

import shortuuid
from core.utils.harmony_utils.page import create_harmony_page


@contextlib.contextmanager
def chdir(root):
    if root == ".":
        yield
        return
    cwd = os.getcwd()
    os.chdir(root)
    try:
        yield
    except BaseException as e:
        raise e
    finally:
        os.chdir(cwd)


def build_by_hvigorw(
        hvigorw_bin: str,
        harmony_project_dir: str,
        log_level: Literal["debug", "info", "warn", "error"] = "warn",
        timeout: int = 30
) -> Tuple[bool, str]:
    """利用 hvigorw 构建项目，进而实现 ArkTS 编译检查
    hvigorw assembleHap

    Args:
        hvigorw_bin: hvigorw 可执行文件路径
        harmony_project_dir: Harmony 项目目录
        log_level: 日志级别
        timeout: 超时时间

    Returns:
        Tuple[bool, str]: 构建结果，构建日志
    """
    build_mode: Literal["debug", "release"] = "debug"
    is_daemon: bool = False  # 守护进程
    is_parallel: bool = True  # 并行编译
    is_incremental: bool = True  # 增量编译

    command = [hvigorw_bin, "assembleHap"]

    # 构建模式
    command.append(f"-p --buildMode={build_mode}")
    # 日志等级
    command.append(f"--{log_level}")
    # 守护进程
    if is_daemon:
        command.append("--daemon")
    else:
        command.append("--no-daemon")
    # 并行编译
    if is_parallel:
        command.append("--parallel")
    else:
        command.append("--no-parallel")
    # 增量编译
    if is_incremental:
        command.append("--incremental")
    else:
        command.append("--no-incremental")

    with chdir(harmony_project_dir):
        try:
            build_progress = subprocess.run(command, capture_output=True, timeout=timeout)
            status_code = build_progress.returncode
            if status_code != 0:
                # 构建失败
                if build_progress.stderr:
                    try:
                        return False, build_progress.stderr.decode("utf-8")
                    except UnicodeDecodeError:
                        return False, str(build_progress.stderr)
                else:
                    try:
                        return False, build_progress.stdout.decode("utf-8")
                    except UnicodeDecodeError:
                        return False, str(build_progress.stdout)
            else:
                return True, ""
        except subprocess.TimeoutExpired as e:
            # 构建超时
            return False, "timeout"


def compile_harmony_project(
        hvigorw_bin: str,
        harmony_project_dir: str,
        log_level: Literal["debug", "info", "warn", "error"] = "error",
        timeout: int = 30
) -> Tuple[bool, List[str]]:
    """获取编译器输出

    Args:
        hvigorw_bin: hvigorw 可执行文件路径
        harmony_project_dir: Harmony 项目目录
        log_level: 日志级别
        timeout: 超时时间

    Returns:
        Tuple[bool, str]: 构建结果，构建错误信息
    """
    build_flag, build_log = build_by_hvigorw(
        hvigorw_bin,
        harmony_project_dir,
        log_level,
        timeout
    )
    if build_flag:
        return True, []
    else:
        # 构建失败，提取编译器输出
        compiler_output = ""
        for hvigor_log in build_log.split("> hvigor "):
            if "ArkTS Compiler Error" in hvigor_log:
                compiler_output = hvigor_log
                break
        # 去掉错误中的文件路径及其行列信息
        print(compiler_output)
        compiler_errors = re.findall(r"\d+[\s\S]*?:\d+:\d+\s(.*?)(?=\d+[\s\S]*?:\d+:\d+|\nCOMPILE RESULT)", compiler_output, re.DOTALL)
        # 去除颜色以及前后的换行等内容
        compiler_errors = [error.strip('\x1b[').strip() for error in compiler_errors]
        return False, compiler_errors


def compile_harmony_component(
        component_code: str,
        hvigorw_bin: str,
        temp_harmony_project_dir: str,
        *,
        component_code_description: str = "",
        log_level: Literal["debug", "info", "warn", "error"] = "error",
        timeout: int = 30
) -> Tuple[bool, str]:
    """获取编译器输出

    Args:
        hvigorw_bin: hvigorw 可执行文件路径
        temp_harmony_project_dir: Harmony 项目目录
        component_code: 组件名称
        log_level: 日志级别
        timeout: 超时时间

    Returns:
        Tuple[bool, str]: 构建结果，构建错误信息
    """
    # 1. 格式化组件代码
    component_code_match = re.search(r"(.*?)(@Entry|@Component)[\s\S]*?struct[\s\S]*?([a-zA-Z0-9_]+)[\s\S]*?\{(.+)}\s*?(.*?)$", component_code, re.DOTALL)
    component_name = f"TestComponent{shortuuid.uuid()}"
    if component_code_match:
        # 含有struct的
        before_component_code = component_code_match.group(1).strip()
        component_code = component_code_match.group(4)
        after_component_code = component_code_match.group(5).strip()
        component_code = """/*
[COMPONENT_CODE_DESCRIPTION]
*/

[BEFORE_COMPONENT_CODE]

@Entry
@Component
struct [COMPONENT_NAME] {
  [COMPONENT_CODE]
}

[AFTER_COMPONENT_CODE]
        """.replace("[COMPONENT_CODE_DESCRIPTION]", component_code_description) \
            .replace("[BEFORE_COMPONENT_CODE]", before_component_code) \
            .replace("[COMPONENT_NAME]", component_name) \
            .replace("[COMPONENT_CODE]", component_code) \
            .replace("[AFTER_COMPONENT_CODE]", after_component_code)
    else:
        # 仅含有组件
        component_code = """/*
[COMPONENT_CODE_DESCRIPTION]

@Entry
@Component
struct [COMPONENT_NAME] {
  build() {
    [COMPONENT_CODE]
  }
}
*/
      
        """.replace("[COMPONENT_CODE_DESCRIPTION]", component_code_description) \
            .replace("[COMPONENT_NAME]", component_name)
    # 1. 在 entry/src/main/pages/ets/pages 下创建一个新的页面，并在 entry/src/main/resources/base/profile/main_pages.json 中注册该页面
    create_harmony_page(
        component_code,
        component_name,
        temp_harmony_project_dir,
        "entry",
        "pages"
    )
    # 2. 获得错误日志
    compiler_flag, compiler_log = compile_harmony_project(
        hvigorw_bin,
        temp_harmony_project_dir,
        log_level,
        timeout
    )
    # 3. 从 main_pages.json 中删除注册的页面
    main_pages_filepath = os.path.join(temp_harmony_project_dir, "entry", "src", "main", "resources", "base", "profile", "main_pages.json")
    with open(main_pages_filepath, "r", encoding="utf-8") as f:
        main_pages = json.load(f)
    if "src" in main_pages:
        if f"pages/{component_name}" in main_pages["src"]:
            main_pages["src"].remove(f"pages/{component_name}")
            with open(main_pages_filepath, "w", encoding="utf-8") as f:
                json.dump(main_pages, f, indent=2, ensure_ascii=False)
    return compiler_flag, compiler_log




if __name__ == '__main__':
    component_code = """
@Component
struct xxx {
  build() {
    Stack() {
        Column() {
          Text('Elegant Card Title 1')
            .width('auto') // android:layout_width="wrap_content"
            .height('auto') // android:layout_height="wrap_content"
            .fontSize(20) // android:textSize="20sp"
            .fontWeight(FontWeight.Bold) // android:textStyle="bold"
            .fontColor($r('app.color.design_default_color_on_primary')) // android:textColor="@color/design_default_color_on_primary"

          Text('This is an enhanced description for Card 1. It has more padding and better styling.')
            .width('auto') // android:layout_width="wrap_content"
            .height('auto') // android:layout_height="wrap_content"
            .fontSize(16) // android:textSize="16sp"
            .lineSpacing(LengthMetrics.vp(4)) // android:lineSpacingExtra="4dp"
            .fontColor($r('app.color.design_default_color_on_primary')) // android:textColor="@color/design_default_color_on_primary"
            .margin({ top: 8 }) // android:layout_marginTop="8dp"
        }
        .width('100%') // android:layout_width="match_parent"
        .height('auto') // android:layout_height="wrap_content"
        .padding(20) // android:padding="20dp"
        .alignItems(HorizontalAlign.Start)
      }
      .width('100%') // android:layout_width="match_parent"
      .height('auto') // android:layout_height="wrap_content"
      .margin({ bottom: 16 }) // android:layout_marginBottom="16dp"
      .backgroundColor($r('app.color.cardview_light_background')) // android:backgroundTint="@color/cardview_light_background"
      .borderRadius(12) // app:cardCornerRadius="12dp"
      .shadow(8) // app:cardElevation="8dp"
      .borderWidth(1) // app:strokeWidth="1dp"
      .borderColor($r('app.color.cardview_shadow_start_color')) // app:strokeColor="@color/cardview_shadow_start_color"

  }
}
    
    """
    compiler_flag, compiler_log = compile_harmony_component(
        component_code,
        "D:/Devkits/Harmony/command-line-tools/bin/hvigorw.bat",
        "D:/Code/Harmony/bookdash",
        component_code_description="测试代码"
    )
    print(compiler_flag)
    print(compiler_log)

