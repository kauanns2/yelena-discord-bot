"""
===========================================================
YELENA V2
Module Registry
===========================================================

Registro central de todos os módulos da arquitetura.
"""

from pathlib import Path


class ModuleRegistry:

    def __init__(self):

        self.modules = {}

    def register(self, module_path: Path):

        module_name = module_path.name

        self.modules[module_name] = {
            "name": module_name,
            "path": module_path,
            "loaded": False,
            "metadata": {},
        }

    def load(self, module_name):

        if module_name in self.modules:

            self.modules[module_name]["loaded"] = True

    def get(self, module_name):

        return self.modules.get(module_name)

    def exists(self, module_name):

        return module_name in self.modules

    def count(self):

        return len(self.modules)

    def all(self):

        return list(self.modules.values())

    def clear(self):

        self.modules.clear()
