from typing import Annotated, Dict, Any

import torch.cuda
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from core.pilot.retrieve_agent import RetrieveAgent
from core.config.config_loader import ConfigLoader
from core.llms import LLMFactory

config = ConfigLoader.get_config()
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["deepseek"].dict())

db_client = Chroma(
    collection_name="harmony-component-doc",
    persist_directory=config.rag_config.persist_directory,
    embedding_function=HuggingFaceEmbeddings(
        model_name=config.rag_config.embedding.text.model,
        model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
)

retrieve_agent = RetrieveAgent(db_client=db_client, llm_client=llm_client)


def search_component_document(
        query: Annotated[str, "查询语句"],
        where: Annotated[Dict[str, Dict[str, Any]], "过滤元数据"] = None,
):
    """查询组件文档

    Args:
        query (Annotated[str, "查询语句"]): 查询语句
        where (Annotated[Dict[str, Dict[str, Any], "过滤元数据"], optional): 过滤元数据.
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
    return retrieve_agent.retrieve_component_docs(query, where=where)
