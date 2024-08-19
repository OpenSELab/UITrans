from typing import Dict, Any
from .basic_client import BasicLLMClient
from .oai_client import OpenAIClient


class LLMFactory:

    @staticmethod
    def create_llm_from_config(llm_config: Dict[str, Any]):
        """根据配置创建大语言模型
        """
        llm_client_type = llm_config.get("type", "default")

        if llm_client_type == "openai":
            return OpenAIClient(llm_config)
        elif llm_client_type == "basic":
            return BasicLLMClient(llm_config)
        else:
            raise ValueError(f"不支持的大语言模型类型：{llm_client_type}")
