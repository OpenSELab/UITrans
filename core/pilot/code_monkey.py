import asyncio
from typing import List, Dict, Any, Coroutine

import shortuuid

from sqlalchemy import select

from core.config.config_loader import ConfigLoader
from core.db.model.translation import TranslationTable
from core.db.session import SessionManager
from core.llms.base import LLMClient
from core.logger.runtime import get_logger
from core.agents.llm_agent import LLMAgent
from core.pilot.schema import BreakdownAndroidLayout, TranslateAndroidComponent, ChooseComponent, Translation
from core.prompt import PromptLoader
from core.pilot.harmony.utils import get_harmony_component, get_component_related_types


logger = get_logger(name="Code Monkey Agent")

from core.pilot.harmony.resource import load_harmony_resource
resource = load_harmony_resource(r"D:\Code\Harmony\NormalAbility\entry\src\main\resources")
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

    async def _query_translations_from_db(self, component: Dict[str, Any]) -> List[TranslationTable]:
        """查询数据库获得安卓组件对应的鸿蒙组件的转译表

        Args:
            component (Dict[str]): 安卓组件
                - name (str): 组件名称
                - content (str): 组件内容
                - description (str): 组件描述

        Returns:
            str: 组件文档
        """
        component_name = component["name"]
        async with SessionManager(ConfigLoader.get_config().db_config) as session:
            result = await session.execute(
                select(TranslationTable)
                .where(TranslationTable.source_component == component_name and TranslationTable.source_language == "android")
            )
            translations = list(result.scalars().all())
        self.logger.debug(f"Querying Harmony Component From DB: {component_name}, Size: {len(translations)}")
        if len(translations) != 0:
            return self._filter_translations(component, translations)
        return translations  # []

    def _filter_translations(self, component: Dict[str, Any], translations: List[TranslationTable]) -> List[TranslationTable]:
        """利用向量相似度及关键词匹配过滤转译表

        Args:
            component (Dict[str]): 安卓组件
                - name (str): 组件名称
                - content (str): 组件内容
                - description (str): 组件描述
            translations (List[TranslationTable]): 转译表
        """
        if len(translations) == 0:
            return []
        return translations

    def _filter_component_documents(self, component: Dict[str, Any], harmony_components: Dict[str, Any]) -> Dict[str, Any]:
        """利用向量相似度及关键词匹配过滤组件文档

        Args:
            component (Dict[str]): 安卓组件
                - name (str): 组件名称
                - content (str): 组件内容
                - description (str): 组件描述
            harmony_components (Dict[str, Any]): 鸿蒙组件文档
                - xxx
                - examples (List[str]): 组件示例
        """
        return harmony_components

    async def _translate_component(self, task: Dict[str, Any], translations: List[TranslationTable]) -> Translation:
        """根据转译表转译组件

        Args:
            - task (Dict[str]): 任务
                - done (bool): 任务是否完成
                - description (str): 任务描述
                - component (Dict[str]): 安卓组件
                    - name (str): 组件名称
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
        related_harmony_components = set()
        for translation in translations:
            related_harmony_components.update(translation.target_component)
        harmony_components = self._filter_component_documents(task["component"], get_harmony_component(list(related_harmony_components)))
        harmony_types = get_component_related_types(list(harmony_components.keys()))

        translate_android_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/translate_android_component.prompt",
            current_task=task,
            translations=translations,
            harmony_types=harmony_types,
            is_type_content=True,
            harmony_components=harmony_components,
            is_component_content=True,
            project_resources=resource,
            android_component=task["component"]
        )
        print()
        print(translate_android_component_prompt)
        print(task["description"])
        messages = self.generate_reply(translate_android_component_prompt, remember=False, model_schema=TranslateAndroidComponent)
        print(messages[-1]["content"])
        translate_android_component = TranslateAndroidComponent.common_parse_raw(messages[-1]["content"])
        print(translate_android_component.harmony_component)
        print(translate_android_component.harmony_component_description)
        translation = Translation(
            description=task["description"],
            source_language="android",
            source_component=task["component"]["name"],
            source_component_code=task["component"]["content"],
            source_component_description=task["component"]["description"],
            target_language="harmony",
            target_component=list(related_harmony_components),
            target_component_code=translate_android_component.harmony_component,
            target_component_description=translate_android_component.harmony_component_description,
            explanation=translate_android_component.explanation
        )
        return translation

    async def _generate_component(self, task: Dict[str, Any]) -> Translation:
        """根据安卓组件及鸿蒙文档生成对应组件

        Args:
            task (Dict[str]): 任务
                - done (bool): 任务是否完成
                - description (str): 任务描述
                - component (Dict[str]): 安卓组件
                    - name (str): 组件名称
                    - content (str): 组件内容
                    - description (str): 组件描述
        """
        # 1. 根据需求选择可能需要的鸿蒙组件
        custom_harmony_components = {}
        predefined_harmony_components = get_harmony_component()
        predefined_harmony_components.update(custom_harmony_components)
        choose_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/choose_component.prompt",
            current_task=task,
            # 全部组件文档，但没有使用说明，只有简介
            harmony_components=get_harmony_component(),
            is_component_content=False,
        )
        choose_component_messages = self.generate_reply(choose_component_prompt, remember=False, model_schema=ChooseComponent)
        choose_component = ChooseComponent.common_parse_raw(choose_component_messages[-1]["content"])
        # 2. 查询组件文档以及类型文档
        harmony_components = self._filter_component_documents(task["component"], get_harmony_component(list(choose_component.components)))
        harmony_types = get_component_related_types(list(choose_component.components))
        # 3. 根据组件文档生成鸿蒙代码
        generate_harmony_component_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/translate_android_component.prompt",
            current_task=task,
            harmony_types=harmony_types,
            is_type_content=True,
            harmony_components=harmony_components,
            is_component_content=True,
            project_resources=resource,
            android_component=task["component"]
        )
        generate_harmony_component_messages = self.generate_reply(generate_harmony_component_prompt, remember=False, model_schema=TranslateAndroidComponent)
        translate_android_component = TranslateAndroidComponent.common_parse_raw(generate_harmony_component_messages[-1]["content"])
        translation = Translation(
            description=task["description"],
            source_language="android",
            source_component=task["component"]["name"],
            source_component_code=task["component"]["content"],
            source_component_description=task["component"]["description"],
            target_language="harmony",
            target_component=list(choose_component.components),
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
        # TODO: 修改为并发查询
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

        # 修改为并发转译
        # 异步转译所有组件
        async def async_translate_components():
            translate_component_tasks: List[Coroutine[Any, Any, Translation]] = []
            for index, (task, translation) in enumerate(zip(breakdown_android_layout.tasks, translations)):
                if len(translation) == 0:
                    # TODO: 提高生成的效果，目前跳过生成
                    continue
                    translate_component_tasks.append(self._generate_component(task.model_dump()))
                else:
                    translate_component_tasks.append(self._translate_component(task.model_dump(), translation))
            return await asyncio.gather(*translate_component_tasks)

        translate_android_components = asyncio.run(async_translate_components())

        return list(translate_android_components)

