import shortuuid
from core.llms.base import LLMClient
from core.logger.runtime import get_logger
from core.agents.llm_agent import LLMAgent

logger = get_logger(name="Tech Leader Agent")


class TechLeaderAgent(LLMAgent):
    """技术领导智能体

    Args:
        llm_client (LLMClient): 大语言模型客户端
        name (str): 智能体的名称
        description (str): 智能体的描述
    """

    agent_role: str = "Tech Leader Agent"
    agent_description: str = "技术主管，负责制定开发计划。"

    def __init__(
            self,
            llm_client: LLMClient,
            name: str = f"{agent_role}-{shortuuid.uuid()}",
            description: str = agent_description
    ):
        super(TechLeaderAgent, self).__init__(llm_client, name, description)

