from typing import Optional, TypeAlias, List, Dict, Literal

from pydantic import BaseModel, Field, field_validator

LLM_PROVIDER: TypeAlias = str


class LoggerConfig(BaseModel):
    level: str = Field(description="日志级别", default="INFO")
    type: Literal["console", "file"] = Field(description="日志输出类型", default="console")
    fmt: str = Field(description="日志格式",
                     default="%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logfile: Optional[str] = Field(description="日志文件路径", default=None)


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
    rerank: EmbeddingModelConfig = Field(description="重排序编码模型配置")


class RAGConfig(BaseModel):
    persist_directory: str = Field(description="持久化目录")
    embedding: EmbeddingConfig = Field(description="RAG 编码模型配置")


class DBConfig(BaseModel):
    """
    Configuration for database connections.

    Supported URL schemes:

    * sqlite+aiosqlite: SQLite database using the aiosqlite driver
    """

    url: str = Field(
        "sqlite+aiosqlite:///sqlite.db",
        description="Database connection URL",
    )
    debug_sql: bool = Field(False, description="Log all SQL queries to the console")

    @classmethod
    @field_validator("url")
    def validate_url_scheme(cls, v: str) -> str:
        if v.startswith("sqlite+aiosqlite://"):
            return v
        raise ValueError(f"Unsupported database URL scheme in: {v}")


class Config(BaseModel):
    llm_config: Dict[LLM_PROVIDER, LLMConfig]
    prompt_template_config: PromptTemplateConfig
    rag_config: Optional[RAGConfig] = None
    db_config: Optional[DBConfig] = None
