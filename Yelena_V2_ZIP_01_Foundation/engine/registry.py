"""
===========================================================
YELENA V2
Module Registry
===========================================================

Registro central de todos os módulos carregados.
O Registry é responsável apenas por armazenar módulos.
Toda a lógica de decisão pertence ao Kernel.
===========================================================
"""


class ModuleRegistry:

    def __init__(self):

        self.modules = {}

    def register(self, module):

        manifest = module.get("manifest", {})

        module_id = manifest.get("id")

        if module_id is None:
            raise ValueError(
                "Manifest sem campo 'id'."
            )

        module["loaded"] = False

        module["initialized"] = False

        module["connections"] = []

        module["weight"] = {}

        module["cache"] = {}

        module["errors"] = []

        self.modules[module_id] = module

    def exists(self, module_id):

        return module_id in self.modules

    def get(self, module_id):

        return self.modules.get(module_id)

    def all(self):

        return list(self.modules.values())

    def count(self):

        return len(self.modules)

    def clear(self):

        self.modules.clear()

    def loaded_modules(self):

        return [
            module
            for module in self.modules.values()
            if module["loaded"]
        ]

    def initialized_modules(self):

        return [
            module
            for module in self.modules.values()
            if module["initialized"]
        ]
