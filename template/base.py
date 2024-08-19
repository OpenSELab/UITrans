import os
from typing import Dict, Any

from core.logger.runtime import get_logger
from core.llms.base import LLMClient

logger = get_logger(name="Project Template Manager")


class BaseProjectTemplate:
    """
    Base project template, providing a common interface for all project templates.

    Attributes:
        - name: The name of the project template
        - path: The path to the project template
        - description: A description of the project template
        - file_descriptions: A dictionary of file descriptions
    """
    name: str
    path: str
    description: str
    file_descriptions: Dict[str, Any]

    def __init__(self):
        self.__files = []
        self._load_files()

    @property
    def files(self):
        return self.__files

    def _load_files(self):
        """Load files from the project template descriptions."""
        self.__files = []
        for file_path, file_desc in self.file_descriptions.items():
            temp_file_path = os.path.join(self.path, file_path).replace("\\", "/")
            temp_file_ext = os.path.splitext(temp_file_path)[1]
            if not os.path.exists(temp_file_path):
                logger.error(f"File '{temp_file_path}' does not exist")
                continue
            if os.path.isdir(temp_file_path):
                logger.error(f"File '{temp_file_path}' is a directory")
                continue
            try:
                if temp_file_ext not in [".json", ".json5", ".ets", ".ts", ".gitignore", ".txt"]:
                    self.__files.append({
                        "path": file_path,
                        "content": None,  # TODO: 处理媒体文件，
                        "description": file_desc
                    })
                    logger.debug(f"Skipping file '{temp_file_path}', unsupported file type: {temp_file_path}")
                else:
                    with open(os.path.join(self.path, file_path), "r", encoding="utf-8") as f:
                        self.__files.append({
                            "path": file_path,
                            "content": f.read(),
                            "description": file_desc
                        })
                    logger.debug(f"Loading file '{temp_file_path}'")
            except Exception as e:
                logger.error(f"Failed to load file '{temp_file_path}': {e}")

    def add_file(self, path: str, client: LLMClient = None):
        raise NotImplementedError


