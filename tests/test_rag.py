import os

from core.config.config_loader import ConfigLoader
from core.prompt.prompt_loader import PromptLoader

from core.pilot.harmony.component import get_harmony_component

os.chdir("../")

ConfigLoader.from_file("./config.yaml")


def test_component_example_document():
    components = get_harmony_component()
    examples = []
    for component_name, component_schema in components.items():
        component_examples = component_schema.examples
        if component_examples and len(component_examples) > 0:
            examples.extend(component_examples)
    print(examples)


def test_component_document():
    total_harmony_components = PromptLoader.get_prompt(
        "harmony/components.prompt",
        harmony_components=get_harmony_component(),
        is_component_content=True
    )
    print(total_harmony_components)
