from typing import Any, List
from pydantic import BaseModel, Field

from core.logger.runtime import get_logger
from core.agents.llm_agent import LLMAgent

logger = get_logger(name="Tech Leader Agent")


class TechLeaderAgent(LLMAgent):
    """技术领导智能体

    """

    name: str = "Tech Leader Agent"
    description: str = "技术主管，负责制定开发计划。"

    def __init__(self, name: str, description: str, config: dict[str, Any], **kwargs):
        super().__init__(name, description, config, **kwargs)
