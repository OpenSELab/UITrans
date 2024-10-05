import os
import unittest

from core.config.config_loader import ConfigLoader
from core.agents.llm_agent import LLMAgent
from core.llms import LLMFactory
from core.tools.file_tools import create_file, read_file, list_files

os.chdir("../")
config = ConfigLoader.from_file("./config.yaml")
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["openai"].dict())


class TestLLMAgent(unittest.TestCase):

    def test_llm_agent(self):
        print(os.getcwd())
        llm_agent = LLMAgent(llm_client=llm_client)
        llm_agent.register_tool(create_file)
        llm_agent.register_tool(read_file)
        llm_agent.generate_reply("say this is test.")

    def test_llm_agent_tool_calls(self):
        llm_agent = LLMAgent(llm_client)
        llm_agent.register_tool(list_files)
        llm_agent.register_tool(read_file)
        llm_agent.register_tool(create_file)
        llm_agent.solve(
            "请递归列出目录core/pilot下的所有文件，包括其子目录中的文件。并任意读取一个文件的内容。你应该先查看有哪些文件，然后再挑选一个文件查看内容。",
            sender="test")
        llm_agent.print_chat_messages("test")
