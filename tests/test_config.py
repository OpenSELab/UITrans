import os
from core.config.config_loader import ConfigLoader
from core.prompt.prompt_loader import PromptLoader

os.chdir("../")

ConfigLoader.from_file("./config.yaml")


def test_prompt_loader():
    tech_leader_system_message = PromptLoader.get_prompt("tech_leader/system.prompt")
    print(tech_leader_system_message)
