"""
===========================================================
YELENA V2
Kernel
===========================================================

O Kernel coordena a arquitetura.

Ele NÃO conhece a estrutura dos módulos.

Cada módulo informa suas conexões.

O Kernel apenas navega pela teia.
===========================================================
"""

from pathlib import Path


class Kernel:

    def __init__(self, root: Path):

        self.root = root

        self.registry = None

        self.running = False

    def boot(self):

        print("[Kernel] Inicializando...")

        self.running = True

    def shutdown(self):

        print("[Kernel] Encerrando...")

        self.running = False

    def attach_registry(self, registry):

        self.registry = registry

    def modules(self):

        if self.registry is None:

            return []

        return self.registry.all()

    def get_module(self, module_id):

        if self.registry is None:

            return None

        return self.registry.get(module_id)

    def resolve_connections(self, module_id):

        module = self.get_module(module_id)

        if module is None:

            return []

        return sorted(

            module.get("connections", []),

            key=lambda item: item["weight"],

            reverse=True

        )

    def is_running(self):

        return self.running
