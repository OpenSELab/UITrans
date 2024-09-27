import os
import re
import json
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.component.components import get_harmony_component
from core.pilot.harmony.resource import load_harmony_resource
from core.pilot.harmony.utils import get_component_related_types
from core.pilot.schema import BreakdownLayout, BreakdownLayoutTranslation, ChooseComponent, Files, \
    BreakdownComponentTranslation
from core.prompt.prompt_loader import PromptLoader
from template.harmony_empty_ability import HarmonyEmptyAbilityV5ProjectTemplate
from core.llms.oai_client import OpenAIClient
from core.logger.runtime import get_logger

os.chdir("D:/Codes/Python/harmony-pilot")

logger = get_logger(name="harmony-pilot test")


def extract_code_blocks(markdown_text):
    """从 Markdown 文本中提取代码块"""
    code_block_pattern = re.compile(r'```.*?\n(.*?)\n```', re.DOTALL)
    code_block_match = code_block_pattern.search(markdown_text)
    if code_block_match:
        return code_block_match.group(1)
    return markdown_text

# ======================== 从文件中加载配置 ========================
ConfigLoader.from_file(r"D:\Codes\Python\harmony-pilot\config.yaml")
harmony_template = HarmonyEmptyAbilityV5ProjectTemplate()
openai_default_config = ConfigLoader.get_config().llm_config.get("deepseek").model_dump()
resource = load_harmony_resource(r"D:\Codes\ArkTS\dashbook\entry\src\main\resources")
client = OpenAIClient(openai_default_config)