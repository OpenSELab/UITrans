import os
import unittest

from core.llms import LLMFactory
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.component import get_harmony_component
from core.prompt import PromptLoader

os.chdir("../")

config = ConfigLoader.from_file("./config.yaml")
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["deepseek"].dict())


class TestRAG(unittest.TestCase):

    def test_rag(self):
        from langchain_core.documents import Document
        from langchain_chroma import Chroma
        from langchain_huggingface import HuggingFaceEmbeddings

        harmony_components = get_harmony_component("Button")

        documents = []
        for component_name, component_schema in harmony_components.items():
            for attribute_name, attribute_schema in component_schema.attributes.items():
                documents.append(Document(
                    page_content=f"""{attribute_schema.description}
属性名称：{attribute_name}
属性参数：{attribute_schema.params}
""",
                    metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "attribute", "name": attribute_name},
                ))
            for event_name, event_schema in component_schema.events.items():
                documents.append(Document(
                    page_content=f"""{event_schema.description}
事件名称：{event_name}
事件参数：{event_schema.params}
事件返回值：{event_schema.returns}
""",
                    metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "event", "name": event_name},
                ))


        embedding_model = HuggingFaceEmbeddings(
            model_name="models/embedding/gte-large-zh",
            model_kwargs={"device": "cuda"},
            encode_kwargs={"normalize_embeddings": True},
        )
        vectorstore = Chroma.from_documents(
            documents,
            embedding=embedding_model,
            collection_name="temp-collection",
            collection_metadata={
                "hnsw:space": "cosine"
            }
        )
        for document in documents:
            print(document.page_content)
        results = vectorstore.similarity_search_with_relevance_scores("设置组件自身的高度和宽度", k=10)
        for result in results:
            print(result)
