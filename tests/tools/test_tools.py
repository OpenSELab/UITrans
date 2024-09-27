import os

from core.config.config_loader import ConfigLoader
from core.agents.llm_agent import LLMAgent
from core.llms import LLMFactory
from core.tools.file_tools import create_file, read_file, list_files

os.chdir("../")
config = ConfigLoader.from_file("./config.yaml")
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["deepseek"].dict())
llm_agent = LLMAgent(llm_client)


def test_agent_list_files():
    llm_agent.register_tool(list_files)
    response_message = llm_agent.receive("请列出目录core/prompt/prompts下的所有文件。")
    print(response_message)
