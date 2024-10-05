from typing import Annotated, Dict, Any

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from core.agents.retrieve_agent import RetrieveAgent
from core.config.config_loader import ConfigLoader
from core.llms import LLMFactory
from core.pilot.harmony.utils import get_harmony_component, get_component_related_types
from core.prompt import PromptLoader

config = ConfigLoader.get_config()
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["deepseek"].dict())

db_client = Chroma(
    collection_name="temp-collection",
    persist_directory=config.rag_config.persist_directory,
    embedding_function=HuggingFaceEmbeddings(
        model_name=config.rag_config.embedding.text.model,
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True},
    )
)

retrieve_agent = RetrieveAgent(db_client=db_client, llm_client=llm_client)


def search_component_document(
        query: Annotated[str, "查询语句"],
        filter: Annotated[Dict[str, Dict[str, Any]], "过滤元数据"] = None,
):
    """查询组件文档

    Args:
        query (Annotated[str, "查询语句"]): 查询语句
        filter (Annotated[Dict[str, Dict[str, Any], "过滤元数据"], optional): 过滤元数据.
            filter必须遵循如下结构:
            ```
            {
                "metadata_field": {
                     <Operator>: <Value>
                }
            }
            ```
            其中 metadata_field 是元数据字段名，Operator 是过滤操作符，Value 是过滤值。
            metadata_field的可选值为 "component_name"，表示组件名。
            Operator的可选值如下：
                - "$eq": 等于
                - "$ne": 不等于
                - "$gt": 大于
                - "$gte": 大于等于
                - "$lt": 小于
                - "$lte": 小于等于
                - "$in": 在列表中
                - "$nin": 不在列表中

    """
    components = []
    component_filter = filter.get("component_name", None)
    if component_filter:
        for filter_operator, filter_value in component_filter.items():
            if filter_operator in ["$in", "$eq"]:
                if isinstance(filter_value, str):
                    components.append(filter_value)
                elif isinstance(filter_value, list):
                    components.extend(filter_value)

    return retrieve_agent.retrieve_docs(query, filter=filter)
