import json
import os.path
import time

from core.config.config_loader import ConfigLoader
from core.llms import LLMFactory
from core.pilot.code_monkey import CodeMonkeyAgent
from core.pilot.developer import DeveloperAgent
from core.pilot.harmony.resource import load_harmony_resource
from core.pilot.schema import BreakdownLayoutTranslation
from core.state.global_state import global_state

config = ConfigLoader.from_file("./config.yaml")
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["deepseek"].model_dump())


with open("pages/page_tasks.json", "r", encoding="utf-8") as f:
    page_tasks = json.loads(f.read())

for page_task in page_tasks:
    android_layout_xml_name = page_task["name"]

    android_layouts = {
        android_layout_xml_name: page_task
    }
    tests_page = None
    android_layout_xml_name_path = android_layout_xml_name.replace('\\', '/').replace('/', '_')
    target_filepath = f"pages/results/{android_layouts[android_layout_xml_name]['source']}_temp_agent_task_{android_layout_xml_name_path}.json"
    if os.path.exists(target_filepath):
        flag = True
        if tests_page:
            for test_page in tests_page:
                if test_page in target_filepath:
                    print(f"Processing {android_layout_xml_name} from {android_layouts[android_layout_xml_name]['source']}...")
                    flag = False
                    break
        if flag:
            print(f"Skipping {android_layout_xml_name} from {android_layouts[android_layout_xml_name]['source']}...")
            continue
    else:
        print(f"Processing {android_layout_xml_name} from {android_layouts[android_layout_xml_name]['source']}...")
    try:
        layout_translation = BreakdownLayoutTranslation(
            tasks=[{
                "description": f"将{android_layout_xml_name}转译为对应的Harmony页面",
                "done": False,
                "android": android_layout_xml_name,
                "harmony": "ets/pages/Index.ets"
            }]
        )
        resources = load_harmony_resource(global_state.harmony.get("project_dir") + "/entry/src/main/resources")
        developer_agent = DeveloperAgent(llm_client=llm_client)
        code_monkey_agent = CodeMonkeyAgent(llm_client=llm_client)

        start_time = time.time()
        breakdown_android_layout = developer_agent.breakdown_android_layout(layout_translation, android_layouts)
        global_state.harmony.set("resources", resources)
        all_translations, translation_agent_task = code_monkey_agent.translate_component_v1(breakdown_android_layout)
        developer_agent = DeveloperAgent(llm_client=llm_client)
        assemble_harmony_layout_result = developer_agent.assemble_harmony_layout(breakdown_android_layout,
                                                                                 android_layouts[
                                                                                     android_layout_xml_name],
                                                                                 all_translations)
        end_time = time.time()
        print(f"Time: {end_time - start_time}")
        with open(target_filepath, "w", encoding="utf-8") as f:
            f.write(json.dumps({
                "android_layout": android_layouts[android_layout_xml_name],
                "breakdown_android_layout": breakdown_android_layout.model_dump(),
                "translations": [translation.model_dump() for translation in all_translations],
                "translation_agent_task": translation_agent_task.model_dump(),
                "assemble_harmony_layout": assemble_harmony_layout_result,
                "time": end_time - start_time
            }, ensure_ascii=False))
    except Exception as e:
        with open("pages/failures.txt", "a", encoding="utf-8") as f:
            f.write(f"Failed to process {android_layout_xml_name}: {str(e)}\n")
        print(f"Failed to process {android_layout_xml_name}: {str(e)}")
