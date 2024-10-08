import operator
from typing import Dict, Any, List

from langchain_core.vectorstores import VectorStore
from langchain_core.documents import Document
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

from core.agents.llm_agent import LLMAgent
from core.config.config_loader import ConfigLoader
from core.pilot.harmony.utils import get_component_related_types, generate_type_document
from core.prompt import PromptLoader


class RetrieveAgent(LLMAgent):
    agent_role: str = "retriever"
    agent_description: str = "一名高效的信息检索助手，熟练从文档中精准提取与用户查询相关的内容，具备深度理解相关文本的能力，并确保信息的准确性和性。您根据用户的查询指令，严谨执行信息提取任务，优先提供简洁、符合的回答。"

    def __init__(self, db_client: VectorStore, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.db_client = db_client
        self.rank_model = HuggingFaceCrossEncoder(
            model_name=ConfigLoader.get_config().rag_config.embedding.rerank.model)

    def recommend_docs(self, query: str):
        ...

    def rerank_docs(self, query: str, documents: List[Document], k: int = 20):
        scores = self.rank_model.score([(query, doc.page_content) for doc in documents])
        docs_with_scores = list(zip(documents, scores))
        result = sorted(docs_with_scores, key=operator.itemgetter(1), reverse=True)
        return result[: k]

    def retrieve_docs(self, query: str, k: int = 20, where: Dict[str, Any] = None,
                      where_document: Dict[str, Any] = None, max_rounds: int = 5, rerank: bool = False):
        last_results_num = 0
        remaining_results_num = k
        current_round = 1
        # 用于约束回答的提示
        strict_prompt = ""

        where = where or {}

        total_documents = self.db_client.similarity_search_with_relevance_scores(
            query,
            k=remaining_results_num * max_rounds * 2,
            filter=where,
            where_document=where_document
        )
        if rerank:
            total_documents = self.rerank_docs(query, [
                document
                for document, score in total_documents
            ], remaining_results_num * max_rounds)
        documents = []
        document_index = 0
        while current_round <= max_rounds:
            for document, score in total_documents[last_results_num:remaining_results_num]:
                document_content = f"## 文档#{document_index}:\n" + document.page_content + "\n"
                documents.append(document_content)
                document_index += 1

            retrieve_docs_prompt = PromptLoader.get_prompt(
                f"{self.agent_role}/retrieve_docs.prompt",
                query=query,
                documents=documents
            )
            retrieve_docs_prompt += strict_prompt

            response = self.generate_reply(retrieve_docs_prompt, remember=False)
            response_content = response[-1]["content"]
            if "UPDATE CONTEXT" in response_content:
                # 继续添加文档
                current_round += 1
                last_results_num = remaining_results_num
                remaining_results_num = k * current_round
            elif "TERMINATE" in response_content:
                # 去掉回答中的"TERMINATE"标记，根据回答中的文档索引[x, xx, xxx]返回文档
                response_content = response_content.replace("TERMINATE", "")
                return response_content
            else:
                strict_prompt = """如果你无法根据当前文档回答问题，你应该准确回复“UPDATE CONTEXT”。
        当你成功回答用户问题后，如果不需要进一步的操作，请在回答的末尾添加“TERMINATE”。"""
        return "UNKNOWN"

    def retrieve_component_docs(self, query: str, k: int = 20, where: Dict[str, Any] = None,
                                where_document: Dict[str, Any] = None, max_rounds: int = 5):
        last_results_num = 0
        remaining_results_num = k
        current_round = 1
        # 用于约束回答的提示
        strict_prompt = ""

        where = where or {}
        if len(where) == 0:
            where["source"] = {
                "$eq": "harmony-component-doc"
            }
        else:
            where = {
                "$and": [
                    where,
                    {
                        "source": {
                            "$eq": "harmony-component-doc"
                        }
                    }
                ]
            }

        total_documents = self.db_client.similarity_search_with_relevance_scores(
            query,
            k=remaining_results_num * max_rounds,
            filter=where,
            where_document=where_document
        )
        # ranked_documents = self.rerank_docs(query, [
        #     document
        #     for document, score in total_documents
        # ], remaining_results_num * max_rounds)
        documents = []
        related_types = {}
        document_index = 0
        while current_round <= max_rounds:
            for document, score in total_documents[last_results_num:remaining_results_num]:
                document_content = ""
                component_name = document.metadata.get("component_name", "")
                type_or_event_name = document.metadata.get("name", "")
                # if component_name and type_or_event_name:
                #     # 根据文档查找相关的类型
                #     temp_related_types = get_component_related_types(
                #         component_name,
                #         attributes_and_events=[type_or_event_name]
                #     )
                #     for type_name, type_schema in temp_related_types.items():
                #         if type_name not in related_types:
                #             related_types[type_name] = type_schema
                #             documents.append(f"## 文档#{document_index}:\n" + generate_type_document(type_name, type_schema) + "\n")
                #             document_index += 1

                document_content += f"## 文档#{document_index}:\n" + document.page_content + "\n"
                documents.append(document_content)
                document_index += 1

            retrieve_docs_prompt = PromptLoader.get_prompt(
                f"{self.agent_role}/retrieve_docs.prompt",
                query=query,
                documents=documents
            )
            retrieve_docs_prompt += strict_prompt
            print(retrieve_docs_prompt)

            response = self.generate_reply(retrieve_docs_prompt, remember=False)
            response_content = response[-1]["content"]
            if "UPDATE CONTEXT" in response_content:
                # 继续添加文档
                current_round += 1
                last_results_num = remaining_results_num
                remaining_results_num = k * current_round
            elif "TERMINATE" in response_content:
                # 去掉回答中的"TERMINATE"标记，根据回答中的文档索引[x, xx, xxx]返回文档
                response_content = response_content.replace("TERMINATE", "")
                document_indices = list(map(lambda x: int(x.strip()), response_content.strip().strip("[]").split(",")))
                final_documents = "\n".join([documents[i] for i in document_indices])
                return final_documents
            else:
                strict_prompt = """如果你无法根据当前文档回答问题，你应该准确回复“UPDATE CONTEXT”。
当你成功回答用户问题后，如果不需要进一步的操作，请在回答的末尾添加“TERMINATE”。"""
        return "UNKNOWN"


if __name__ == '__main__':
    ...
