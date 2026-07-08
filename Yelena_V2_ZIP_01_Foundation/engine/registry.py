"""
Module Registry

Mantém o registro central de todos os módulos carregados.
"""

from pathlib import Path


class ModuleRegistry:

    def __init__(self):

        self.modules = []

    def register(self, path: Path):

        self.modules.append(path)

    def get(self, name: str):

        for module in self.modules:

            if module.name == name:

                return module

        return None

    def exists(self, name: str):

        return self.get(name) is not None

    def count(self):

        return len(self.modules)

    def clear(self):

        self.modules.clear()
