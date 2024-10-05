import os
import unittest

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from core.agents.retrieve_agent import RetrieveAgent
from core.config.config_loader import ConfigLoader
from core.llms import LLMFactory
from core.pilot.harmony.component import get_harmony_component
from core.pilot.harmony.utils import get_component_related_types

os.chdir("../")

config = ConfigLoader.from_file("./config.yaml")
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["openai"].dict())
db_client = Chroma(
    collection_name="temp-collection",
    persist_directory=config.rag_config.persist_directory,
    embedding_function=HuggingFaceEmbeddings(
        model_name=config.rag_config.embedding.text.model,
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True},
    )
)


class TestRetrieveAgent(unittest.TestCase):

    def test_init_rag_db(self):
        from langchain_core.documents import Document

        harmony_components = get_harmony_component()

        documents = []
        for component_name, component_schema in harmony_components.items():
            documents.append(Document(
                page_content=f"""组件名：{component_name}
组件描述：{component_schema.description}
""",
                metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "component"},
            ))
            for interface in component_schema.interfaces:
                documents.append(Document(
                    page_content=f"""接口名：{interface.description}
接口参数：{interface.params}
        """,
                    metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "interface"},
                ))
            for attribute_name, attribute_schema in component_schema.attributes.items():
                documents.append(Document(
                    page_content=f"""{attribute_schema.description}
属性名称：{attribute_name}
属性参数：{attribute_schema.params}
""",
                    metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "attribute",
                              "name": attribute_name},
                ))
            for event_name, event_schema in component_schema.events.items():
                documents.append(Document(
                    page_content=f"""{event_schema.description}
事件名称：{event_name}
事件参数：{event_schema.params}
事件返回值：{event_schema.returns}
""",
                    metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "event",
                              "name": event_name},
                ))
            related_types = get_component_related_types(component_name)
            for type_name, type_schema in related_types.items():
                if type_schema.type == "object":
                    document = Document(
                        page_content=f"""类型名：{type_name}
类型描述：{type_schema.description}
参数：{type_schema.properties}
                        """,
                        metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "type",
                                  "name": type_name},
                    )
                elif type_schema.type == "enum":
                    # 枚举值介绍
                    all_enum_description = ""
                    for enum_value, enum_description in type_schema.enumDescriptions.items():
                        all_enum_description += f"* {enum_value}: {enum_description}\n"
                    document = Document(
                        page_content=f"""枚举类型名：{type_name}
枚举类型描述：{type_schema.description}
枚举值：{type_schema.enum}
枚举值描述：
{all_enum_description}
                        """,
                        metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "enum",
                                  "name": type_name},
                    )
                else:
                    # 普通类型
                    document = Document(
                        page_content=f"""类型名：{type_name}
类型描述：{type_schema.description}
类型：{type_schema.type}
                        """,
                        metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "type",
                                  "name": type_name},
                    )
                documents.append(document)
                if type_schema.examples:
                    for example in type_schema.examples:
                        documents.append(Document(
                            page_content=f"""类型{type_name}示例：
{example}
""",
                            metadata={"source": "harmony-component-doc", "component_name": component_name,
                                      "type": "example", "name": type_name},
                        ))

        db_client.add_documents(documents)

    def test_retrieve_agent(self):
        retrieve_agent = RetrieveAgent(db_client=db_client, llm_client=llm_client)
        result_document = retrieve_agent.retrieve_docs(
            query="用于替代安卓的ConstraintLayout，作为页面的根布局，支持子组件的垂直排列。",

        )
        print(result_document)
