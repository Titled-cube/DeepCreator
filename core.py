import os
import time
from pathlib import Path

class DeepCreator:
    def __init__(self, base_dir: str = ".", debug: bool = False):
        self.base_dir = Path(base_dir)
        self.debug = debug
        self.ai_enabled = False
        self.ai_generator = None


    def log(self, message: str):
        """Логирование действий"""
        if self.debug:
            print(f"[DEEP_CREATOR] {message}")

    def create_directory(self, dir_name: str):
        """Создание директории"""
        dir_path = self.base_dir / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        self.log(f"Создана директория: {dir_path}")


    def enable_ai(self, api_key: str, service: str = "openrouter"):
        """Активация ИИ-функционала"""
        self.ai_generator = AIGenerator(api_key, service)
        self.ai_enabled = True
        self.log("ИИ-модуль активирован")

    def create_file(self, file_name: str, content: str = ""):
        """Расширенный метод с ИИ-поддержкой"""
        if self.ai_enabled and file_name.lower() == "readme.md":
            ai_content = self.ai_generator.generate_documentation(
                self.base_dir.name, 
                "Создай README.md с секциями: Установка, Использование, Лицензия"
            )
            content = ai_content or content
        
        super().create_file(file_name, content)

    def build_structure(self, structure: dict):
        """Построение структуры проекта"""
        for name, content in structure.items():
            if isinstance(content, dict):
                self.create_directory(name)
                with self._enter_subdir(name):
                    self.build_structure(content)
            else:
                self.create_file(name, content)

    def _enter_subdir(self, dir_name: str):
        """Контекстный менеджер для поддиректорий"""
        class SubdirContext:
            def __init__(self, creator, dir_name):
                self.creator = creator
                self.original_dir = creator.base_dir
                self.dir_name = dir_name

            def __enter__(self):
                self.creator.base_dir /= self.dir_name
                self.creator.log(f"Вход в директорию: {self.creator.base_dir}")

            def __exit__(self, *args):
                self.creator.base_dir = self.original_dir
                self.creator.log(f"Возврат в директорию: {self.creator.base_dir}")

        return SubdirContext(self, dir_name)