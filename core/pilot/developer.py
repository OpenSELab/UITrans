from typing import List

import shortuuid
from core.llms.base import LLMClient
from core.logger.runtime import get_logger
from core.agents.llm_agent import LLMAgent
from core.pilot.schema import BreakdownLayoutTranslation, BreakdownAndroidLayout, Translation
from core.prompt import PromptLoader

logger = get_logger(name="Developer Agent")


class DeveloperAgent(LLMAgent):
    """技术领导智能体

    Args:
        llm_client (LLMClient): 大语言模型客户端
        name (str): 智能体的名称
        description (str): 智能体的描述
    """

    agent_role: str = "developer"
    agent_description: str = "一名高效的全栈软件开发者，擅长编写模块化、清晰且符合生产级标准的代码，并确保代码库易于维护，具备完善的错误处理和日志记录机制。你根据技术主管的指示，严谨执行开发任务。"

    def __init__(
            self,
            llm_client: LLMClient,
            name: str = f"{agent_role}-{shortuuid.uuid()}",
            description: str = agent_description
    ):
        super(DeveloperAgent, self).__init__(llm_client, name, description, logger=logger)

    def breakdown_android_layout(self, layout_translation: BreakdownLayoutTranslation, android_layouts: dict) -> BreakdownAndroidLayout:
        """拆解Android布局

        Args:
            - layout_translation (BreakdownLayoutTranslation): 布局转译任务
            - android_layouts (dict): Android布局内容

        Jinja2 Template Args:
            - tasks (List[Task]): 任务列表
            - current_task (Task): 当前任务
            - android_layout (dict): Android布局
                - name: 布局文件名
                - content: 布局文件内容
        """
        current_task_index = 0
        breakdown_android_layout_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/breakdown_android_layout.prompt",
            tasks=layout_translation.tasks,
            current_task=layout_translation.tasks[current_task_index],
            android_layout=android_layouts[layout_translation.tasks[current_task_index].android]
        )
        messages = self.generate_reply(breakdown_android_layout_prompt, model_schema=BreakdownAndroidLayout, remember=False)
        response = BreakdownAndroidLayout.common_parse_raw(messages[-1]["content"])
        self.logger.info(f"Breakdown Android Layout: {response}")
        return response

    def assemble_harmony_layout(self, breakdown_android_layout: BreakdownAndroidLayout, android_layout: dict, translations: List[Translation]):
        """组装鸿蒙布局

        Args:
            - breakdown_android_layout (BreakdownAndroidLayout): 拆解的Android布局
            - android_layout (dict): Android布局
            - translations (Translation): 翻译结果

        Jinja2 Template Args:
            - breakdown_android_layout (BreakdownAndroidLayout): 拆解的Android布局
            - translations (Translation): 翻译结果
            - android_layout (dict): Android布局
        """
        assemble_harmony_layout_prompt = PromptLoader.get_prompt(
            f"{self.agent_role}/assemble_harmony_layout.prompt",
            tasks=breakdown_android_layout.tasks,
            translations=translations,
            android_layout=android_layout
        )
        messages = self.generate_reply(assemble_harmony_layout_prompt, remember=False)
        self.logger.info(f"Assemble Harmony Layout: {messages[-1]['content']}")
        return messages[-1]["content"]

