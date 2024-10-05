import os.path
from typing import Dict, Any

import yaml
from core.config.schema import Config, LLMConfig, PromptTemplateConfig, RAGConfig, LoggerConfig, DBConfig
from core.prompt.prompt_loader import PromptLoader


class ConfigLoader:
    """Pilot Config 加载器

    llm_config: 默认的LLM配置
        provider: 服务提供商
            base_url: LLM API BASE URL
            api_key: LLM API KEY
            temperature: 温度
            ... 其他参数
    prompt_template_dirs: Prompt 模板
        type: 模板类型，目前支持：jinja、py_str
        path: 模板路径
    """
    config: Config = None

    default_config_filepath = "config.yaml"

    @classmethod
    def get_config(cls):
        if cls.config is None:
            if os.path.exists(cls.default_config_filepath):
                return cls.from_file(cls.default_config_filepath)
            raise ValueError("config 未被初始化。")
        return cls.config

    @classmethod
    def _init_llms_config(cls, config: Dict[str, Any]) -> Dict[str, LLMConfig]:
        """初始化 LLM 配置"""
        _llms = config.get("llms", [])
        if not _llms:
            raise ValueError("配置 llms 不能为空。")
        _llms_config = {}
        for _llm in _llms:
            _llms_config[_llm["provider"]] = LLMConfig(**_llm)
        return _llms_config

    @classmethod
    def _init_prompt_template_config(cls, config: Dict[str, Any]) -> PromptTemplateConfig:
        """初始化 Prompt 模板配置"""
        _prompt = config.get("prompt", {})
        if not _prompt:
            raise ValueError("配置 prompt 不能为空。")
        _prompt_template_config = PromptTemplateConfig(**_prompt)
        return _prompt_template_config

    @classmethod
    def _init_rag_config(cls, config: Dict[str, Any]) -> RAGConfig:
        """初始化 RAG 配置"""
        _rag = config.get("rag", {})
        if not _rag:
            raise ValueError("配置 rag 不能为空。")
        _rag_config = RAGConfig(**_rag)
        return _rag_config

    @classmethod
    def _init_db_config(cls, config: Dict[str, Any]) -> DBConfig:
        """初始化 DB 配置"""
        _db = config.get("db", {})
        if not _db:
            raise ValueError("配置 db 不能为空。")
        _db_config = DBConfig(**_db)
        return _db_config

    @classmethod
    def from_file(cls, filepath: str) -> Config:
        """从 yaml 文件中加载环境信息
        :param filepath: yaml 文件路径
        :return: ConfigLoader
        """
        with open(filepath, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        _llms_config = cls._init_llms_config(config)
        _prompt_template_config = cls._init_prompt_template_config(config)
        _rag_config = cls._init_rag_config(config)
        _db_config = cls._init_db_config(config)

        cls.config = Config(
            llm_config=_llms_config,
            prompt_template_config=_prompt_template_config,
            rag_config=_rag_config,
            db_config=_db_config
        )
        # 初始化 Prompt 加载器
        PromptLoader.from_paths(_prompt_template_config.paths)

        return cls.config


__all__ = ["ConfigLoader"]
