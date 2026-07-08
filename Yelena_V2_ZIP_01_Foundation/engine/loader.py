"""
Module Loader

Responsável por localizar todos os módulos da Yelena.
"""

from pathlib import Path


class ModuleLoader:

    def __init__(self, registry):

        self.registry = registry

        self.root = Path(__file__).resolve().parents[2]

    def scan_modules(self):

        print("[Loader] Procurando módulos...")

        for folder in sorted(self.root.iterdir()):

            if (
                folder.is_dir()
                and folder.name.startswith("Yelena_V2_ZIP_")
            ):

                self.registry.register(folder)

                print(f"[Loader] Encontrado: {folder.name}")

    def load_modules(self):

        print("[Loader] Carregando módulos...")

        for module in self.registry.modules:

            print(f"[Loader] Carregado: {module.name}")
