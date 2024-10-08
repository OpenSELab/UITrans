from typing import Dict, Any
from core.llms.basic_client import BasicLLMClient
from core.llms.oai_client import OpenAIClient


class LLMFactory:

    @staticmethod
    def create_llm_from_config(llm_client_type: str, llm_config: Dict[str, Any], **kwargs):
        """根据配置创建大语言模型

        Args:
            llm_client_type (str): 大语言模型类型
            llm_config (Dict[str, Any]): 大语言模型配置
        """

        if llm_client_type == "openai":
            return OpenAIClient(llm_config, **kwargs)
        elif llm_client_type == "basic":
            return BasicLLMClient(llm_config, **kwargs)
        else:
            raise ValueError(f"不支持的大语言模型类型：{llm_client_type}")
