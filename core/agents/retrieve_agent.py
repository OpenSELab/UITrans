from typing import Dict, Any

from langchain_core.vectorstores import VectorStore

from core.agents.llm_agent import LLMAgent
from core.prompt import PromptLoader


class RetrieveAgent(LLMAgent):
    agent_role: str = "retriever"
    agent_description: str = "一名高效的信息检索助手，熟练从文档中精准提取与用户查询相关的内容，具备深度理解相关文本的能力，并确保信息的准确性和性。您根据用户的查询指令，严谨执行信息提取任务，优先提供简洁、符合的回答。"

    def __init__(self, db_client: VectorStore, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.db_client = db_client

    def recommend_docs(self, query: str):
        ...

    def retrieve_docs(self, query: str, k: int = 10, filter: Dict[str, Any] = None,
                      where_document: Dict[str, Any] = None, max_rounds: int = 5):
        remaining_results_num = k
        current_round = 1
        # 用于约束回答的提示
        strict_prompt = ""

        total_documents = self.db_client.similarity_search_with_relevance_scores(
            query,
            k=remaining_results_num * max_rounds,
            filter=filter,
            where_document=where_document
        )
        while current_round <= max_rounds:
            documents = [
                document.page_content
                for document, score in total_documents[:remaining_results_num]
            ]
            retrieve_docs_prompt = PromptLoader.get_prompt(
                f"{self.agent_role}/retrieve_docs.prompt",
                query=query,
                documents=documents
            )
            retrieve_docs_prompt += strict_prompt
            response = self.generate_reply(retrieve_docs_prompt, remember=False)
            response_content = response[-1]["content"]
            if "UPDATE CONTEXT" in response_content:
                # 已经查询了全部文档
                if len(documents) < remaining_results_num:
                    return "UNKNOWN"
                # 继续添加文档
                current_round += 1
                remaining_results_num = k * current_round
            elif "TERMINATE" in response_content:
                return response_content
            else:
                strict_prompt = """如果你无法根据当前文档回答问题，你应该准确回复“UPDATE CONTEXT”。
当你成功回答用户问题后，如果不需要进一步的操作，请在回答的末尾添加“TERMINATE”。"""
        return "UNKNOWN"


if __name__ == '__main__':
    ...
