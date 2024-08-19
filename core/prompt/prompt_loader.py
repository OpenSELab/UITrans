from typing import List, Tuple, Dict

from jinja2 import FileSystemLoader, Environment, StrictUndefined, TemplateNotFound


class PromptTemplate:
    """Prompt 模板
    """

    def get(self, prompt_name: str, **kwargs) -> str:
        raise NotImplementedError

    def list_templates(self) -> List[str]:
        raise NotImplementedError


class JinjaPromptTemplate(PromptTemplate):
    """Jinja Prompt 模板
    """

    def __init__(self, paths: List[str]):
        self._template_env = Environment(
            loader=FileSystemLoader(paths),
            autoescape=False,
            lstrip_blocks=True,
            trim_blocks=True,
            keep_trailing_newline=True,
            # undefined=StrictUndefined  # TODO：最终使用 StrictUndefined
        )

    def get(self, prompt_name: str, **kwargs) -> str:
        try:
            tpl = self._template_env.get_template(prompt_name)
        except TemplateNotFound as err:
            raise ValueError(f"模板不存在: {prompt_name}") from err
        return tpl.render(**kwargs)

    def list_templates(self) -> List[str]:
        return self._template_env.list_templates()


class PromptLoader:
    """Prompt 加载器

    目前仅支持 Jinja 模板
    """

    _prompt_templates: List[PromptTemplate] = None
    _prompts: Dict[Tuple[str, ...], PromptTemplate] = None

    @classmethod
    def from_paths(cls, paths: List[str]):
        """加载 Jinja Prompt 模板"""
        cls._prompt_templates = [JinjaPromptTemplate(paths)]

    @classmethod
    def get_prompt(cls, prompt_name: str, **kwargs) -> str:
        """获取 Prompt 模板"""
        for temp_tpl in cls._prompt_templates:
            if prompt_name in temp_tpl.list_templates():
                return temp_tpl.get(prompt_name, **kwargs)
        raise ValueError(f"模板不存在: {prompt_name}")


__all__ = ["PromptLoader"]
