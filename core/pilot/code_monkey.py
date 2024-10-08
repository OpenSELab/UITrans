import asyncio
from typing import List, Dict, Any, Coroutine
from concurrent.futures import ThreadPoolExecutor, as_completed

import shortuuid
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from sqlalchemy import select

from core.agents.schema import AgentTasks
from core.config.config_loader import ConfigLoader
from core.db.model.harmony import HarmonyComponentExample
from core.db.model.translation import TranslationTable
from core.db.session import SessionManager
from core.llms.base import LLMClient
from core.logger.runtime import get_logger
from core.agents.llm_agent import LLMAgent
from core.pilot.retrieve_agent import RetrieveAgent
from core.pilot.schema import BreakdownAndroidLayout, TranslateAndroidComponent, ChooseComponent, Translation, \
    GenerateComponentQuery
from core.prompt import PromptLoader
from core.pilot.harmony.utils import get_harmony_component, get_component_related_types, generate_type_document, \
    generate_component_interface_document
from core.tools.search_tools import search_component_document

logger = get_logger(name="Code Monkey Agent")

from core.pilot.harmony.resource import load_harmony_resource

resource = load_harmony_resource(r"D:\Code\Harmony\bookdash\entry\src\main\resources")


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
                model_kwargs={"device": "cuda"},
                encode_kwargs={"normalize_embeddings": True},
            ),
            collection_metadata={
                "hnsw:M": 64,  # 增大图结构中节点的最大连接数，避免图结构过于稀疏，无法生成高质量的邻居搜索结果。默认值为：16
                "hnsw:construction_ef": 200,  # 控制图结构的质量，值越大，图结构质量越高，但搜索速度越慢。默认值为：100
                "hnsw:space": "cosine"  # 距离度量方式使用余弦相似度，可选值为：cosine、l2、ip。默认值为：l2
            }
        )
        self.retrieve_agent = RetrieveAgent(db_client=self.component_db_client, llm_client=llm_client)

    def make_plan(self, requirement: str, interactive: bool = False, **kwargs) -> AgentTasks:
        """制定计划

        Args:
            requirement (str): 需求
            interactive (bool): 是否支持交互式

        Jinja2 Variables:
            requirement (dict): 需求
            tools (list): 工具列表
            project_files (list): 项目文件列表
            is_file_content (bool): 是否显示文件内容，默认为空
            project_resources (dict): 项目资源列表
            is_resource_content (bool): 是否显示资源内容，默认为空
        """
        ...

    def query_component_document(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """查询组件文档

        Args:
            task (Dict[str]): 任务
                - done (bool): 任务是否完成
                - description (str): 任务描述
                - component (Dict[str]): 安卓组件
                    - name (List[str]): 组件名称
                    - content (str): 组件内容
                    - description (str): 组件描述

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
        # 1. 生成查询描述
        generate_component_description_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/generate_component_query.prompt",
            current_task=task,
            harmony_components=get_harmony_component(),
            android_component=task["component"],
            project_resources=resource
        )
        generate_component_query_messages = self.generate_reply(generate_component_description_prompt,
                                                                      remember=False,
                                                                      model_schema=GenerateComponentQuery)
        component_query = GenerateComponentQuery.common_parse_raw(
            generate_component_query_messages[-1]["content"])
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
        # 3. 查询知识库
        # 3.1 查询示例文档
        example_threshold = 0.6
        example_results = self.component_db_client.similarity_search_with_relevance_scores(
            query=task["component"]["description"],
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
        # 3.2 查询组件文档
        # 组件：查询文档
        # chroma 原生支持多个查询，langchain 不支持
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
            # 3.2.1 解析查询结果
            # 舍弃低于阈值的结果，当前阈值为0.67
            threshold = 0.6
            temp_existed_ids = []
            for query_text, result_ids, result_documents, result_metadatas, result_distances in zip(
                    query.queries, query_results["ids"], query_results["documents"], query_results["metadatas"],
                    query_results["distances"]
            ):
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
        # 3.4 生成类型文档
        type_documents = []
        for type_name, type_schema in related_types.items():
            type_documents.append(
                generate_type_document(type_name, type_schema)
            )
        # 3.5 组合成最终组件文档
        final_component_document = "\n".join(type_documents + component_documents)
        return {
            "document": final_component_document,
            "queries": total_query_results,
            "components": component_query.components
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

    def _translate_component(self, task: Dict[str, Any], translations: List[TranslationTable]) -> Translation:
        """根据转译表转译组件

        Args:
            - task (Dict[str]): 任务
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
        # 1. 查询组件文档
        query_component_document = self.query_component_document(task)
        component_document = query_component_document["document"]
        related_harmony_components = query_component_document["components"]
        # 2. 转译组件
        task["component"]["description"] = """
        该组件通过卡片布局实现了一个展示Logo的界面。卡片的宽度占据整个父布局，高度根据内容自适应，内边距为 16 单位，边角圆度为 8 单位。卡片内部包含一个线性布局，该布局的宽度占据整个卡片，高度根据内容自适应，内边距为 8 单位，方向为垂直排列。

在卡片内部的线性布局中，包含一个图像视图用于展示Logo。图像视图的宽度根据内容自适应，高度固定为 200 单位，横向和纵向均居中对齐。图像视图的上下左右边距均为 8 单位。图像视图展示的图片资源为 bookdash_logo。

整个布局通过卡片布局和线性布局的嵌套关系，确保Logo在卡片中居中展示，卡片与父布局之间有一定的边距，使得界面整洁美观。
        """
        translate_android_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/translate_android_component.prompt",
            current_task=task,
            translations=translations,
            component_document=component_document,
            project_resources=resource,
            android_component=task["component"]
        )
        print(translate_android_component_prompt)
        translate_component_messages = self.generate_reply(translate_android_component_prompt, remember=False,
                                       model_schema=TranslateAndroidComponent)
        print(translate_component_messages[-1]["content"])
        # translate_android_component = TranslateAndroidComponent.common_parse_raw(translate_component_messages[-1]["content"])
        # print(translate_android_component.harmony_component)
        # print(translate_android_component.harmony_component_description)
        # print(translate_android_component.explanation)
        # 3. 检查转译结果
        check_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/check_translate_component.prompt",
        )
        # check_messages = translate_component_messages + [{
        #     "role": "user",
        #     "content": check_component_prompt
        # }]
        # checked_translate_component_messages = self.generate_reply(check_messages, remember=False, model_schema=TranslateAndroidComponent)
        # print(checked_translate_component_messages[-1]["content"])
        # TODO: 完善Check
        checked_translate_component_messages = translate_component_messages
        translate_android_component = TranslateAndroidComponent.common_parse_raw(checked_translate_component_messages[-1]["content"])
        print(translate_android_component.harmony_component)
        # print(translate_android_component.harmony_component_description)
        print(translate_android_component.explanation)
        translation = Translation(
            description=task["description"],
            source_language="android",
            source_component=task["component"]["name"][0],
            source_component_code=task["component"]["content"],
            source_component_description=task["component"]["description"],
            target_language="harmony",
            target_component=list(related_harmony_components),
            target_component_code=translate_android_component.harmony_component,
            target_component_description=translate_android_component.harmony_component_description,
            explanation=translate_android_component.explanation
        )
        return translation

    def _generate_component(self, task: Dict[str, Any]) -> Translation:
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
        # 1. 查询组件文档
        query_component_document = self.query_component_document(task)
        component_document = query_component_document["document"]
        related_components = query_component_document["components"]
        # 2. 根据组件文档生成鸿蒙代码
        generate_harmony_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/translate_android_component.prompt",
            current_task=task,
            component_document=component_document,
            project_resources=resource,
            android_component=task["component"]
        )
        print(generate_harmony_component_prompt)
        generate_harmony_component_messages = self.generate_reply(generate_harmony_component_prompt, remember=False,
                                                                  model_schema=TranslateAndroidComponent)
        print(generate_harmony_component_messages[-1]["content"])
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
        print(translate_android_component.harmony_component)
        translation = Translation(
            description=task["description"],
            source_language="android",
            source_component=task["component"]["name"][0],
            source_component_code=task["component"]["content"],
            source_component_description=task["component"]["description"],
            target_language="harmony",
            target_component=related_components,
            target_component_code=translate_android_component.harmony_component,
            target_component_description=translate_android_component.harmony_component_description,
            explanation=translate_android_component.explanation
        )
        return translation

    def translate_component(self, breakdown_android_layout: BreakdownAndroidLayout) -> List[Translation]:
        """根据转译表转译安卓布局组件

        Args:
            - breakdown_android_layout (BreakdownAndroidLayout): 任务列表
        """

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
        #             future = executor.submit(self._generate_component, task.model_dump())
        #         else:
        #             future = executor.submit(self._translate_component, task.model_dump(), translation)
        #         translate_component_tasks[future] = index
        #
        #     # 等待所有转译任务完成
        #     translate_component_results = []
        #     for future in as_completed(translate_component_tasks):
        #         translate_component_results.append((translate_component_tasks[future], future.result()))
        # return [result[1] for result in sorted(translate_component_results, key=lambda x: x[0])]

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
                translate_android_components.append(self._generate_component(task.model_dump()))
            else:
                translate_android_components.append(self._translate_component(task.model_dump(), translation))
        return translate_android_components


"""
{
    "description": "在应用中创建一个卡片视图，作为登录输入区域的容器。卡片视图的宽度占据整个父布局，高度固定为 249dp，四周留有 20dp 的边距，底部额外留有 8dp 的边距。卡片背景颜色为自定义的半透明黑色。卡片内部包含一个垂直排列的线性布局，背景颜色为浅灰色。线性布局中包含两个文本输入框，分别用于输入 Email 和 Password，每个输入框的左右边距为 40dp，Email 输入框顶部边距为 28dp，Password 输入框顶部边距为 0dp。每个输入框左侧有一个图标，提示文本分别为“Email”和“Password”，文本颜色为蓝色灰色。线性布局底部包含一个 Sign In 按钮，按钮宽度自适应，高度固定，右对齐，上下左右边距为 25sp，背景颜色为自定义的按钮背景色，文本为“Sign In”，文本颜色为浅黑色，字体加粗。",
    "components": ["Column", "TextInput", "Button", "RelativeContainer"]
}
"""
