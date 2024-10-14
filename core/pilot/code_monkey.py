import asyncio
import re
from typing import List, Dict, Any, Coroutine, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

import shortuuid
import torch
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from sqlalchemy import select

from core.agents.schema import AgentTask
from core.config.config_loader import ConfigLoader
from core.db.model.harmony import HarmonyComponentExample
from core.db.model.translation import TranslationTable
from core.db.session import SessionManager
from core.llms.base import LLMClient
from core.logger.runtime import get_logger
from core.agents.llm_agent import LLMAgent
from core.pilot.retrieve_agent import RetrieveAgent
from core.pilot.schema import BreakdownAndroidLayout, TranslateAndroidComponent, ChooseComponent, Translation, \
    GenerateComponentQuery, GenerateComponentDescription
from core.prompt import PromptLoader
from core.pilot.harmony.utils import get_harmony_component, get_component_related_types, generate_type_document, \
    generate_component_interface_document
from core.state.schema import State
from core.state.global_state import global_state

logger = get_logger(name="Code Monkey Agent")


def correct_wrap_content(harmony_component_code: str) -> str:
    wrap_content_pattern = r"\.(width|height)\('wrap_content'\)"
    return re.sub(wrap_content_pattern, lambda mat: f".{mat.group(1)}('auto')", harmony_component_code)


def correct_match_parent(harmony_component_code: str) -> str:
    match_parent_pattern = r"\.(width|height)\('match_parent'\)"
    return re.sub(match_parent_pattern, lambda mat: f".{mat.group(1)}('100%')", harmony_component_code)


def correct_text_selectable(harmony_component_code: str) -> str:
    text_selectable_pattern = r"\.textSelectable\(([\s\S]*?)\)"
    text_selectable_match = re.search(text_selectable_pattern, harmony_component_code)
    if text_selectable_match:
        text_selectable_match_text = text_selectable_match.group(1)
        if text_selectable_match_text == "true":
            return re.sub(text_selectable_pattern,
                          lambda mat: f".textSelectable(TextSelectableMode.SELECTABLE_FOCUSABLE)",
                          harmony_component_code)
        elif text_selectable_match_text == "false":
            return re.sub(text_selectable_pattern, lambda mat: f".textSelectable(TextSelectableMode.UNSELECTABLE)",
                          harmony_component_code)
        else:
            return harmony_component_code
    return harmony_component_code


def correct_margin_and_padding(harmony_component_code: str) -> str:
    margin_padding_pattern = r"\.(margin|padding)\(\{([\s\S]*?)\}\)"
    margin_padding_match = re.search(margin_padding_pattern, harmony_component_code, re.MULTILINE)
    if margin_padding_match:
        attr_name = margin_padding_match.group(1)
        margin_padding_match_text = margin_padding_match.group(2)
        margin_padding_match_text = margin_padding_match_text.replace("start:", "left:").replace("end:", "right:")
        return re.sub(margin_padding_pattern, f".{attr_name}({{{margin_padding_match_text}}})", harmony_component_code)
    return harmony_component_code

def correct_line_spacing(harmony_component_code: str) -> str:
    line_spacing_pattern = r"\.lineSpacing\(([\s\S]*?)\)"
    line_spacing_match = re.search(line_spacing_pattern, harmony_component_code)
    if line_spacing_match:
        line_spacing_value = line_spacing_match.group(1).strip("'").rstrip('vp').rstrip('fp').rstrip('dp').rstrip('sp')
        line_spacing_value = f"LengthMetrics.vp({line_spacing_value})"
        return re.sub(line_spacing_pattern, f".lineSpacing({line_spacing_value})", harmony_component_code)
    return harmony_component_code

def correct_some_more(harmony_component_code: str) -> str:
    fit_system_windows_pattern = r"\.fitsSystemWindows\(true\)"
    harmony_component_code = re.sub(fit_system_windows_pattern, "", harmony_component_code)
    return harmony_component_code


class CodeMonkeyAgent(LLMAgent):
    """技术领导智能体

    Args:
        llm_client (LLMClient): 大语言模型客户端
        name (str): 智能体的名称
        description (str): 智能体的描述
    """

    agent_role: str = "code_monkey"
    agent_description: str = "一名专业的全栈开发者，擅长编写模块化、清晰且易维护的代码，并高效完成技术主管分配的任务，确保代码符合生产标准。"

    def __init__(
            self,
            llm_client: LLMClient,
            name: str = f"{agent_role}-{shortuuid.uuid()}",
            description: str = agent_description
    ):
        super(CodeMonkeyAgent, self).__init__(llm_client, name, description, logger=logger)
        self.component_db_client = Chroma(
            collection_name="harmony-component-doc",
            persist_directory=ConfigLoader.get_config().rag_config.persist_directory,
            embedding_function=HuggingFaceEmbeddings(
                model_name=ConfigLoader.get_config().rag_config.embedding.text.model,
                model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"},
                encode_kwargs={"normalize_embeddings": True},
            ),
            collection_metadata={
                "hnsw:M": 64,  # 增大图结构中节点的最大连接数，避免图结构过于稀疏，无法生成高质量的邻居搜索结果。默认值为：16
                "hnsw:construction_ef": 200,  # 控制图结构的质量，值越大，图结构质量越高，但搜索速度越慢。默认值为：100
                "hnsw:space": "cosine"  # 距离度量方式使用余弦相似度，可选值为：cosine、l2、ip。默认值为：l2
            }
        )
        self.retrieve_agent = RetrieveAgent(db_client=self.component_db_client, llm_client=llm_client)
        # Agent 执行的所有任务，task_id: 任务细节
        self.agent_state = State()
        self.tasks: List[AgentTask] = []

    def _query_component_document(self, android_component: Dict[str, Any], parent_agent_task: AgentTask) -> Dict[
        str, Any]:
        """查询组件文档

        Args:
            android_component (Dict[str]): 安卓组件
                - name (List[str]): 组件名称
                - content (str): 组件内容
                - layout_description (str): 组件描述
                - function_description (str): 功能描述
            parent_agent_task (AgentTask): 父任务

        Returns:
            Dict[str, Any]: 组件文档及查询
                - document: 组件文档
                - queries: 所有查询
                - components: 所有组件

        Jinja2 Variables:
            current_task (Task): 当前任务
            harmony_components (Dict[str, Any]): 鸿蒙组件文档
            android_component (Dict[str, Any]): 待转译的Android组件
            project_resources (Dict[str, Any]): 项目资源
            is_resource_content (bool): 是否显示资源内容，默认为空
        """
        agent_task = AgentTask(
            description="查询组件文档",
            details={"android_component": android_component},
            subtasks=[]
        )
        parent_agent_task.subtasks.append(agent_task)
        # 1. 生成查询描述
        generate_component_query_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/generate_component_query.prompt",
            harmony_components=get_harmony_component(),
            android_component=android_component
        )
        generate_component_query_messages = self.generate_reply(generate_component_query_prompt,
                                                                remember=False,
                                                                model_schema=GenerateComponentQuery)
        component_query = GenerateComponentQuery.common_parse_raw(
            generate_component_query_messages[-1]["content"])
        generate_component_query_agent_task = AgentTask(
            description="生成组件查询",
            details={
                "prompt": generate_component_query_prompt,
                "component_query": component_query.model_dump(),
            }
        )
        agent_task.subtasks.append(generate_component_query_agent_task)
        # 2. 修正查询描述
        # 2.1 修正组件名称，去掉不存在的组件
        temp_components = []
        all_harmony_components = get_harmony_component()
        for component in component_query.components:
            if component in all_harmony_components:
                temp_components.append(component)
        component_query.components = temp_components
        # 2.2 修正查询中的组件名称，去掉不存在的组件
        temp_queries = []
        for query in component_query.queries:
            if query.component in all_harmony_components:
                temp_queries.append(query)
        component_query.queries = temp_queries
        correct_component_query_agent_task = AgentTask(
            description="修正组件查询",
            details={
                "component_query": component_query.model_dump(),
                "corrected_component_query": component_query.model_dump()
            }
        )
        agent_task.subtasks.append(correct_component_query_agent_task)
        # 3. 查询知识库
        # 3.1 查询示例文档
        example_threshold = 0.6
        example_results = self.component_db_client.similarity_search_with_relevance_scores(
            query=android_component["function_description"],
            k=3,
            filter={
                "$and": [
                    {
                        "source": {
                            "$eq": "harmony-component-example-doc"
                        }
                    },
                    {
                        "component_name": {
                            "$in": component_query.components
                        }
                    }
                ]
            } if len(component_query.components) > 0 else {
                "source": {
                    "$eq": "harmony-component-example-doc"
                }
            },
            score_threshold=example_threshold
        )

        async def async_query_harmony_component_db(id):
            async with SessionManager(ConfigLoader.get_config().db_config) as session:
                results = await session.execute(
                    select(HarmonyComponentExample).where(HarmonyComponentExample.id == id)
                )
                return list(results.scalars().all())[0]

        component_examples = {}
        for example_doc, example_score in example_results:
            if "table_id" not in example_doc.metadata:
                continue
            table_id = example_doc.metadata["table_id"]
            example_entity = asyncio.run(async_query_harmony_component_db(table_id))
            example_description = example_entity.description
            example_code = example_entity.code
            if example_doc.metadata["component_name"] not in component_examples:
                component_examples[example_doc.metadata["component_name"]] = []

            component_examples[example_doc.metadata["component_name"]].append({
                "description": example_description,
                "code": example_code
            })
        query_examples_agent_task = AgentTask(
            description="查询示例文档",
            details={
                "query": android_component["function_description"],
                "k": 3,
                "component_name": component_query.components,
                "score_threshold": example_threshold,
                "example_knowledge_results": example_results,
                "component_examples": component_examples
            }
        )
        agent_task.subtasks.append(query_examples_agent_task)
        # 3.2 查询组件文档
        # 组件：查询文档
        # chroma 原生支持多个查询，langchain 不支持
        query_component_document_agent_task = AgentTask(
            description="查询组件文档",
            subtasks=[]
        )
        agent_task.subtasks.append(query_component_document_agent_task)
        query_component_document_iter_agent_task = AgentTask(
            description="依次从知识库中查询每个组件的相关属性、事件文档",
            subtasks=[]
        )
        query_component_document_agent_task.subtasks.append(query_component_document_iter_agent_task)
        total_query_results = {}
        for query in component_query.queries:
            query_results = self.component_db_client._collection.query(
                query_embeddings=self.component_db_client.embedding_function.embed_documents(query.queries),
                n_results=10,
                where={
                    "$and": [
                        {
                            "component_name": {
                                "$eq": query.component
                            }
                        },
                        {
                            "source": {
                                "$eq": "harmony-component-doc"
                            }
                        }
                    ]
                }
            )
            query_component_document_iter_item_agent_task = AgentTask(
                description=f"查询组件{query.component}的相关属性、事件文档",
                details={
                    "query": query.queries,
                    "n_results": 10,
                    "query_results": query_results
                }
            )
            query_component_document_iter_agent_task.subtasks.append(query_component_document_iter_item_agent_task)
            # 3.2.1 解析查询结果
            # 舍弃低于阈值的结果，当前阈值为0.67
            query_component_document_filter_agent_task = AgentTask(
                description="过滤低于阈值的查询结果",
                subtasks=[]
            )
            query_component_document_agent_task.subtasks.append(query_component_document_filter_agent_task)
            threshold = 0.6
            temp_existed_ids = []
            for query_text, result_ids, result_documents, result_metadatas, result_distances in zip(
                    query.queries, query_results["ids"], query_results["documents"], query_results["metadatas"],
                    query_results["distances"]
            ):
                query_text_results = []
                for result_id, result_document, result_metadata, result_distance in zip(result_ids, result_documents,
                                                                                        result_metadatas,
                                                                                        result_distances):
                    # 这里使用的是余弦相似度，更新result_distance的值，使其变为[0, 1]的值
                    result_distance = 1 - result_distance
                    if result_distance < threshold:
                        continue
                    if query.component not in total_query_results:
                        total_query_results[query.component] = []
                    if result_id in temp_existed_ids:
                        continue
                    total_query_results[query.component].append((result_document, result_metadata, result_distance))
                    temp_existed_ids.append(result_id)
                    query_text_results.append((result_document, result_metadata, result_distance))
                query_component_document_filter_item_agent_task = AgentTask(
                    description=f"过滤低于阈值的查询结果: {query_text}",
                    details={
                        "query": query_text,
                        "result_ids": result_ids,
                        "result_documents": result_documents,
                        "result_metadatas": result_metadatas,
                        "result_distances": result_distances,
                        "threshold": threshold,
                        "query_text_results": query_text_results
                    }
                )
                query_component_document_filter_agent_task.subtasks.append(
                    query_component_document_filter_item_agent_task)

        # 3.3 生成组件文档
        component_documents = []
        related_types = {}
        for component_name, query_results in total_query_results.items():
            temp_existed_attributes_and_events = []
            # 3.3.1 生成组件文档
            temp_document = f"# {component_name}\n"
            temp_document += generate_component_interface_document(component_name)
            for result_document, result_metadata, result_distance in query_results:
                if "name" in result_metadata:
                    attribute_or_event_name = result_metadata["name"]
                    temp_existed_attributes_and_events.append(attribute_or_event_name)
                temp_document += result_document
            # 3.3.2 生成组件示例文档
            if component_name in component_examples:
                for example in component_examples[component_name]:
                    temp_document += "示例：" + example["description"] + "\n"
                    temp_document += example["code"] + "\n\n"
            component_documents.append(temp_document)
            temp_related_types = get_component_related_types(component_name,
                                                             attributes_and_events=temp_existed_attributes_and_events)
            related_types.update(temp_related_types)
        generate_component_document_agent_task = AgentTask(
            description="生成组件文档",
            details={
                "component_documents": component_documents,
                "related_types": related_types
            }
        )
        agent_task.subtasks.append(generate_component_document_agent_task)
        # 3.4 生成类型文档
        type_documents = []
        for type_name, type_schema in related_types.items():
            type_documents.append(
                generate_type_document(type_name, type_schema)
            )
        generate_type_document_agent_task = AgentTask(
            description="生成类型文档",
            details={
                "type_documents": type_documents
            }
        )
        agent_task.subtasks.append(generate_type_document_agent_task)
        # 3.5 组合成最终组件文档
        final_component_document = "\n".join(type_documents + component_documents)
        return {
            "document": final_component_document,
            "component_document": get_harmony_component(component_query.components),
            "queries": total_query_results,
            "components": component_query.components,
            "idea": component_query.idea
        }

    async def _query_translations_from_db(self, component: Dict[str, Any]) -> List[TranslationTable]:
        """查询数据库获得安卓组件对应的鸿蒙组件的转译表

        Args:
            component (Dict[str]): 安卓组件
                - name (List[str]): 组件名称
                - content (str): 组件内容
                - description (str): 组件描述

        Returns:
            str: 组件文档
        """
        component_name = component["name"]
        async with SessionManager(ConfigLoader.get_config().db_config) as session:
            result = await session.execute(
                select(TranslationTable)
                .where(TranslationTable.source_component.in_(component_name) & (
                        TranslationTable.source_language == "android") & (TranslationTable.disabled == False))
            )
            translations = list(result.scalars().all())
        self.logger.debug(f"Querying Harmony Component From DB: {component_name}, Size: {len(translations)}")
        if len(translations) != 0:
            return self._filter_translations(component, translations)
        return translations  # []

    def _filter_translations(self, component: Dict[str, Any], translations: List[TranslationTable]) -> List[
        TranslationTable]:
        """利用向量相似度及关键词匹配过滤转译表

        Args:
            component (Dict[str]): 安卓组件
                - name (List[str]): 组件名称
                - content (str): 组件内容
                - description (str): 组件描述
            translations (List[TranslationTable]): 转译表
        """
        if len(translations) == 0:
            return []
        return translations

    def _generate_component_description(self, component: Dict[str, Any], parent_agent_task: AgentTask) -> GenerateComponentDescription:
        """生成组件描述

        Args:
            component (Dict[str]): 安卓组件
                - name (List[str]): 组件名称
                - content (str): 组件内容
                - description (str): 组件描述
            parent_agent_task (AgentTask): 父任务
        """
        generate_component_description_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/generate_component_description.prompt",
            android_component=component
        )
        generate_component_description_messages = self.generate_reply(generate_component_description_prompt,
                                                                      remember=False, model_schema=GenerateComponentDescription)
        generate_component_description_response = generate_component_description_messages[-1]["content"].replace(
            "TERMINATE", "")
        generate_component_description = GenerateComponentDescription.common_parse_raw(
            generate_component_description_response)
        agent_task = AgentTask(
            description="生成组件描述",
            details={
                "prompt": generate_component_description_prompt,
                "component_description": generate_component_description
            }
        )
        parent_agent_task.subtasks.append(agent_task)
        return generate_component_description

    def _translate_component(self, translation_task: Dict[str, Any], translations: List[TranslationTable],
                             parent_agent_task: AgentTask = None) -> Translation:
        """根据转译表转译组件

        Args:
            - translation_task (Dict[str]): 任务
                - done (bool): 任务是否完成
                - description (str): 任务描述
                - component (Dict[str]): 安卓组件
                    - name (List[str]): 组件名称
                    - content (str): 组件内容
                    - description (str): 组件描述
            - translations (List[TranslationTable]): 转译表
0
        Jinja2 Template Args:
            current_task (Task): 当前任务
            harmony_types (dict): 鸿蒙类型文档
                - type_name (str): 类型名称
                - type_schema (json str): 类型定义
            harmony_components (dict): 鸿蒙组件文档
            project_resources (dict): 项目资源
            android_component (str): 待转译的Android组件
        """
        agent_task = AgentTask(
            description="根据转译表转译组件",
            subtasks=[]
        )
        parent_agent_task.subtasks.append(agent_task)
        # 1. 查询组件文档
        query_component_document = self._query_component_document(translation_task, agent_task)
        component_document = query_component_document["document"]
        related_harmony_components = query_component_document["components"]
        # 2. 转译组件
        # 2.1 生成详细描述
        translation_task["component"]["description"] = self._generate_component_description(
            translation_task["component"], agent_task)
        translate_android_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/translate_android_component.prompt",
            current_task=translation_task,
            translations=translations,
            component_document=component_document,
            harmony_components=query_component_document["component_document"],
            project_resources=global_state.harmony.get("resources"),
            android_component=translation_task["component"]
        )
        # print(translate_android_component_prompt)
        translate_component_messages = self.generate_reply(translate_android_component_prompt, remember=False,
                                                           model_schema=TranslateAndroidComponent)
        # print(translate_component_messages[-1]["content"])
        # translate_android_component = TranslateAndroidComponent.common_parse_raw(translate_component_messages[-1]["content"])
        # print(translate_android_component.harmony_component)
        # print(translate_android_component.harmony_component_description)
        # print(translate_android_component.explanation)
        # 3. 检查转译结果
        # check_component_prompt = PromptLoader.get_prompt(
        #     f"{self.agent_role}/check_translate_component.prompt",
        # )
        # check_messages = translate_component_messages + [{
        #     "role": "user",
        #     "content": check_component_prompt
        # }]
        # checked_translate_component_messages = self.generate_reply(check_messages, remember=False, model_schema=TranslateAndroidComponent)
        # print(checked_translate_component_messages[-1]["content"])
        # TODO: 完善Check
        checked_translate_component_messages = translate_component_messages
        translate_android_component = TranslateAndroidComponent.common_parse_raw(
            checked_translate_component_messages[-1]["content"])
        translate_component_agent_task = AgentTask(
            description="转译组件",
            details={
                "prompt": translate_android_component_prompt,
                "translated_component": translate_android_component.model_dump()
            }
        )
        agent_task.subtasks.append(translate_component_agent_task)
        translate_android_component.harmony_component = self.postprocess_harmony_component_code(
            translate_android_component.harmony_component, agent_task)
        # print(translate_android_component.harmony_component)
        # print(translate_android_component.harmony_component_description)
        # print(translate_android_component.explanation)
        translation = Translation(
            description=translation_task["description"],
            source_language="android",
            source_component=translation_task["component"]["name"][0],
            source_component_code=translation_task["component"]["content"],
            source_component_description=translation_task["component"]["description"],
            target_language="harmony",
            target_component=list(related_harmony_components),
            target_component_code=translate_android_component.harmony_component,
            target_component_description=translation_task["component"]["description"],
            explanation=translate_android_component.explanation
        )
        return translation

    def _generate_component(self, translation_task: Dict[str, Any], parent_agent_task: AgentTask) -> Translation:
        """根据安卓组件及鸿蒙文档生成对应组件

        Args:
            task (Dict[str]): 任务
                - done (bool): 任务是否完成
                - description (str): 任务描述
                - component (Dict[str]): 安卓组件
                    - name (List[str]): 组件名称
                    - content (str): 组件内容
                    - description (str): 组件描述
        """
        agent_task = AgentTask(
            description="根据转译表转译组件",
            subtasks=[]
        )
        parent_agent_task.subtasks.append(agent_task)
        # 1. 查询组件文档
        query_component_document = self._query_component_document(translation_task, agent_task)
        component_document = query_component_document["document"]
        related_components = query_component_document["components"]
        # 2. 根据组件文档生成鸿蒙代码
        translation_task["component"]["description"] = self._generate_component_description(
            translation_task["component"], agent_task)
        generate_harmony_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/translate_android_component.prompt",
            current_task=translation_task,
            component_document=component_document,
            harmony_components=query_component_document["component_document"],
            project_resources=global_state.harmony.get("resources"),
            android_component=translation_task["component"],
            related_harmony_component=related_components
        )
        # print(generate_harmony_component_prompt)
        generate_harmony_component_messages = self.generate_reply(generate_harmony_component_prompt, remember=False,
                                                                  model_schema=TranslateAndroidComponent)
        # print(generate_harmony_component_messages[-1]["content"])
        # 3. 检查生成结果
        # check_messages = generate_harmony_component_messages + [{
        #     "role": "user",
        #     "content": "请检查所选用的组件、类型、属性和方法完全符合鸿蒙ArkUI官方文档的定义与规范, 以及使用的资源文件都已被定义"
        # }]
        # checked_generate_harmony_component_messages = self.generate_reply(check_messages, remember=False, model_schema=TranslateAndroidComponent)
        # TODO: 完善Check
        checked_generate_harmony_component_messages = generate_harmony_component_messages
        translate_android_component = TranslateAndroidComponent.common_parse_raw(
            checked_generate_harmony_component_messages[-1]["content"])
        generate_harmony_component_agent_task = AgentTask(
            description="生成鸿蒙组件",
            details={
                "prompt": generate_harmony_component_prompt,
                "generated_component": translate_android_component.model_dump()
            }
        )
        agent_task.subtasks.append(generate_harmony_component_agent_task)
        translate_android_component.harmony_component = self.postprocess_harmony_component_code(
            translate_android_component.harmony_component, agent_task)
        # print(translate_android_component.harmony_component)
        translation = Translation(
            description=translation_task["description"],
            source_language="android",
            source_component=translation_task["component"]["name"][0],
            source_component_code=translation_task["component"]["content"],
            source_component_description=translation_task["component"]["description"],
            target_language="harmony",
            target_component=related_components,
            target_component_code=translate_android_component.harmony_component,
            target_component_description=translation_task["component"]["description"],
            explanation=translate_android_component.explanation
        )
        return translation

    def postprocess_harmony_component_code(self, harmony_component_code: str, parent_agent_task: AgentTask) -> str:
        # 高度、宽度随父组件及自适应
        harmony_component_code = correct_match_parent(harmony_component_code)
        harmony_component_code = correct_wrap_content(harmony_component_code)
        # 文本可选
        harmony_component_code = correct_text_selectable(harmony_component_code)
        # 间距
        harmony_component_code = correct_margin_and_padding(harmony_component_code)
        # 行间距
        harmony_component_code = correct_line_spacing(harmony_component_code)
        # 多余的内容
        harmony_component_code = correct_some_more(harmony_component_code)
        agent_task = AgentTask(
            description="后处理鸿蒙组件代码",
            details={
                "harmony_component_code": harmony_component_code
            }
        )
        parent_agent_task.subtasks.append(agent_task)
        return harmony_component_code

    def translate_component(self, breakdown_android_layout: BreakdownAndroidLayout) -> Tuple[
        List[Translation], AgentTask]:
        """根据转译表转译安卓布局组件

        Args:
            - breakdown_android_layout (BreakdownAndroidLayout): 任务列表
        """

        agent_task = AgentTask(
            description="转译安卓布局组件",
            details={
                "breakdown_android_layout": breakdown_android_layout.model_dump()
            }
        )
        self.tasks.append(agent_task)

        # 异步查询所有组件的转译表
        async def async_query_translations():
            # 从数据库中查询转译表
            query_translations_tasks = []
            for task in breakdown_android_layout.tasks:
                query_translations_tasks.append(self._query_translations_from_db(task.component.model_dump()))
            # 等待所有查询任务完成
            return await asyncio.gather(*query_translations_tasks)

        # 转译表: [[...], [...], ...]
        translations = asyncio.run(async_query_translations())

        # TODO: 修改为并发转译
        # with ThreadPoolExecutor(max_workers=len(breakdown_android_layout.tasks)) as executor:
        #     # 生成所有组件的转译任务
        #     translate_component_tasks = {}
        #     for index, (task, translation) in enumerate(zip(breakdown_android_layout.tasks, translations)):
        #         if len(translation) == 0:
        #             future = executor.submit(self._generate_component(task.model_dump(), agent_task))
        #         else:
        #             future = executor.submit(self._translate_component(task.model_dump(), translation, agent_task))
        #         translate_component_tasks[future] = index
        #
        #     # 等待所有转译任务完成
        #     translate_component_results = []
        #     for future in as_completed(translate_component_tasks):
        #         try:
        #             translation, sub_agent_task = future.result()
        #             agent_task.subtasks.append(sub_agent_task)
        #             translate_component_results.append((translate_component_tasks[future], translation))
        #         except Exception as e:
        #             logger.error(f"Failed to translate component: {e}")
        #             continue
        # translate_android_components = []
        # for result in sorted(translate_component_results, key=lambda x: x[0]):
        #     translate_android_components.append(result[1])
        # agent_task.details["translated_android_components"] = translate_android_components
        # return translate_android_components, agent_task

        # 异步转译所有组件
        # async def async_translate_components():
        #     translate_component_tasks: List[Coroutine[Any, Any, Translation]] = []
        #     for index, (task, translation) in enumerate(zip(breakdown_android_layout.tasks, translations)):
        #         if len(translation) == 0:
        #             translate_component_tasks.append(self._generate_component(task.model_dump()))
        #         else:
        #             translate_component_tasks.append(self._translate_component(task.model_dump(), translation))
        #     return await asyncio.gather(*translate_component_tasks)
        #
        # translate_android_components = asyncio.run(async_translate_components())
        # return list(translate_android_components)

        translate_android_components = []
        for index, (task, translation) in enumerate(zip(breakdown_android_layout.tasks, translations)):
            if len(translation) == 0:
                translate_android_components.append(self._generate_component(task.model_dump(), agent_task))
            else:
                translate_android_components.append(
                    self._translate_component(task.model_dump(), translation, agent_task))
        agent_task.details["translated_android_components"] = translate_android_components
        return translate_android_components, agent_task

    def _translate_component_v1(self, all_translation_tasks, translation_task: Dict[str, Any], translations: List[TranslationTable], parent_agent_task: AgentTask = None) -> Translation:
        """根据转译表转译组件

        Args:
            translation_task (Dict[str]): 任务
                - done (bool): 任务是否完成
                - description (str): 任务描述
                - component (Dict[str]): 安卓组件
                    - name (List[str]): 组件名称
                    - content (str): 组件内容
                    - description (str): 组件描述
            translations (List[TranslationTable]): 转译表
        """
        agent_task = AgentTask(
            description="根据转译表转译组件v1",
            subtasks=[]
        )
        parent_agent_task.subtasks.append(agent_task)
        # 1. 生成组件描述, 包括组件样式布局描述和功能描述
        generate_component_description = self._generate_component_description(translation_task["component"], agent_task)
        translation_task["component"]["layout_description"] = generate_component_description.layout_description
        translation_task["component"]["function_description"] = generate_component_description.function_description
        # 2. 查询组件文档
        query_component_document = self._query_component_document(translation_task["component"], agent_task)
        translate_android_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/translate_android_component.prompt",
            tasks=all_translation_tasks,
            current_task=translation_task,
            translations=translations,
            component_document=query_component_document["document"],
            harmony_components=query_component_document["component_document"],
            project_resources=global_state.harmony.get("resources"),
            android_component=translation_task["component"],
            idea=query_component_document["idea"]
        )
        # print(translate_android_component_prompt)
        translate_component_messages = self.generate_reply(translate_android_component_prompt, remember=False,
                                                           model_schema=TranslateAndroidComponent)
        translate_android_component = TranslateAndroidComponent.common_parse_raw(translate_component_messages[-1]["content"])
        translate_android_component_agent_task = AgentTask(
            description="转译组件v1",
            details={
                "prompt": translate_android_component_prompt,
                "translated_component": translate_android_component.model_dump()
            }
        )
        agent_task.subtasks.append(translate_android_component_agent_task)
        translate_android_component.harmony_component = self.postprocess_harmony_component_code(
            translate_android_component.harmony_component, agent_task)
        translation = Translation(
            description=translation_task["description"],
            source_language="android",
            source_component=translation_task["component"]["name"][0],
            source_component_code=translation_task["component"]["content"],
            source_component_description=translation_task["component"]["layout_description"],
            target_language="harmony",
            target_component=list(query_component_document["components"]),
            target_component_code=translate_android_component.harmony_component,
            target_component_description=translation_task["component"]["function_description"] + "\n\n" + translation_task["component"]["layout_description"],
            explanation=translate_android_component.explanation
        )
        return translation

    def _generate_component_v1(self, all_translation_tasks, translation_task: Dict[str, Any], parent_agent_task: AgentTask) -> Translation:
        """根据安卓组件及鸿蒙文档生成对应组件

        Args:
            task (Dict[str]): 任务
                - done (bool): 任务是否完成
                - description (str): 任务描述
                - component (Dict[str]): 安卓组件
                    - name (List[str]): 组件名称
                    - content (str): 组件内容
                    - description (str): 组件描述
        """
        agent_task = AgentTask(
            description="根据转译表转译组件v1",
            subtasks=[]
        )
        parent_agent_task.subtasks.append(agent_task)
        # 1. 生成组件描述, 包括组件样式布局描述和功能描述
        generate_component_description = self._generate_component_description(translation_task["component"], agent_task)
        translation_task["component"]["layout_description"] = generate_component_description.layout_description
        translation_task["component"]["function_description"] = generate_component_description.function_description
        # 2. 查询组件文档
        query_component_document = self._query_component_document(translation_task["component"], agent_task)
        generate_harmony_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/translate_android_component.prompt",
            tasks=all_translation_tasks,
            current_task=translation_task,
            component_document=query_component_document["document"],
            harmony_components=query_component_document["component_document"],
            project_resources=global_state.harmony.get("resources"),
            android_component=translation_task["component"],
            idea=query_component_document["idea"]
        )
        # print(generate_harmony_component_prompt)
        generate_harmony_component_messages = self.generate_reply(generate_harmony_component_prompt, remember=False,
                                                                  model_schema=TranslateAndroidComponent)
        # print(generate_harmony_component_messages[-1]["content"])
        translate_android_component = TranslateAndroidComponent.common_parse_raw(
            generate_harmony_component_messages[-1]["content"])
        translate_android_component.harmony_component = self.postprocess_harmony_component_code(
            translate_android_component.harmony_component, agent_task)
        translation = Translation(
            description=translation_task["description"],
            source_language="android",
            source_component=translation_task["component"]["name"][0],
            source_component_code=translation_task["component"]["content"],
            source_component_description=translation_task["component"]["layout_description"],
            target_language="harmony",
            target_component=query_component_document["components"],
            target_component_code=translate_android_component.harmony_component,
            target_component_description=translation_task["component"]["function_description"] + "\n\n" + translation_task["component"]["layout_description"],
            explanation=translate_android_component.explanation
        )
        return translation


    def translate_component_v1(self, breakdown_android_layout: BreakdownAndroidLayout) -> Tuple[
        List[Translation], AgentTask]:
        """根据转译表转译安卓布局组件

        Args:
            - breakdown_android_layout (BreakdownAndroidLayout): 任务列表
        """

        agent_task = AgentTask(
            description="转译安卓布局组件",
            details={
                "breakdown_android_layout": breakdown_android_layout.model_dump()
            }
        )
        self.tasks.append(agent_task)

        # 异步查询所有组件的转译表
        async def async_query_translations():
            # 从数据库中查询转译表
            query_translations_tasks = []
            for task in breakdown_android_layout.tasks:
                query_translations_tasks.append(self._query_translations_from_db(task.component.model_dump()))
            # 等待所有查询任务完成
            return await asyncio.gather(*query_translations_tasks)

        # 转译表: [[...], [...], ...]
        translations = asyncio.run(async_query_translations())

        translate_component_results = []
        # TODO: 修改为并发转译
        with ThreadPoolExecutor(max_workers=len(breakdown_android_layout.tasks)) as executor:
            # 生成所有组件的转译任务
            translate_component_tasks = {}
            for index, (task, translation) in enumerate(zip(breakdown_android_layout.tasks, translations)):
                if len(translation) == 0:
                    future = executor.submit(
                        self._generate_component_v1,
                        all_translation_tasks=breakdown_android_layout.tasks,
                        translation_task=task.model_dump(),
                        parent_agent_task=agent_task
                    )
                else:
                    future = executor.submit(
                        self._translate_component_v1,
                        all_translation_tasks=breakdown_android_layout.tasks,
                        translation_task=task.model_dump(),
                        translations=translation,
                        parent_agent_task=agent_task
                    )
                translate_component_tasks[future] = index

            # 等待所有转译任务完成
            for future in as_completed(list(translate_component_tasks.keys())):
                try:
                    translation = future.result()
                    translate_component_results.append((translate_component_tasks[future], translation))
                except Exception as e:
                    logger.error(f"Failed to translate component: {e}")
                    continue
        translate_android_components = []
        for result in sorted(translate_component_results, key=lambda x: x[0]):
            translate_android_components.append(result[1])
        agent_task.details["translated_android_components"] = translate_android_components
        return translate_android_components, agent_task

        # translate_android_components = []
        # for index, (task, translation) in enumerate(zip(breakdown_android_layout.tasks, translations)):
        #     if len(translation) == 0:
        #         translate_android_components.append(self._generate_component_v1(breakdown_android_layout.tasks, task.model_dump(), agent_task))
        #     else:
        #         translate_android_components.append(self._translate_component_v1(breakdown_android_layout.tasks, task.model_dump(), translation, agent_task))
        # agent_task.details["translated_android_components"] = translate_android_components
        #
        # return translate_android_components, agent_task