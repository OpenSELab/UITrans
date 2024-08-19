from typing import Optional, TypeAlias, List, Dict, Literal

from pydantic import BaseModel, Field

LLM_PROVIDER: TypeAlias = str


class LoggerConfig(BaseModel):
    level: str = Field(description="日志级别", default="INFO")
    type: Literal["console", "file"] = Field(description="日志输出类型", default="console")
    file: Optional[str] = Field(description="日志文件路径", default=None)
    format: str = Field(description="日志格式", default="%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s")


class LLMConfig(BaseModel):
    provider: LLM_PROVIDER = Field(description="大模型服务提供商")
    base_url: str = Field(description="LLM API 接口基本 URL")
    api_key: str = Field(description="LLM API 接口密钥")
    temperature: Optional[float] = Field(description="LLM 模型调用默认温度", default=None)
    model: Optional[str] = Field(description="LLM 模型名称", default=None)


class PromptTemplateConfig(BaseModel):
    paths: List[str]


class EmbeddingModelConfig(BaseModel):
    model: str = Field(description="模型名称/模型路径")
    base_url: Optional[str] = Field(description="API URL", default=None)
    api_key: Optional[str] = Field(description="API 密钥", default=None)
    instruction: str = Field(description="指令", default="")
    provider: str = Field(description="提供商", default="Harmony Pilot")


class EmbeddingConfig(BaseModel):
    code: EmbeddingModelConfig = Field(description="代码编码模型配置")
    text: EmbeddingModelConfig = Field(description="文本编码模型配置")


class RAGConfig(BaseModel):
    embedding: EmbeddingConfig = Field(description="RAG 编码模型配置")


class Config(BaseModel):
    logger_config: LoggerConfig = Field(description="日志配置")
    llm_config: Dict[LLM_PROVIDER, LLMConfig]
    prompt_template_config: PromptTemplateConfig
    rag_config: RAGConfig
