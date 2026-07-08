"""
===========================================================
YELENA V2
Module Loader
===========================================================

Responsável por localizar todos os módulos da arquitetura
e registrar suas definições.
"""

from pathlib import Path
import yaml


class ModuleLoader:

    def __init__(self, registry):

        self.registry = registry

        self.root = Path(__file__).resolve().parents[2]

    def scan_modules(self):

        print("[Loader] Procurando módulos...")

        for folder in sorted(self.root.iterdir()):

            if not folder.is_dir():
                continue

            if not folder.name.startswith("Yelena_V2_ZIP_"):
                continue

            definition = folder / "definition"

            manifest = definition / "manifest.yaml"

            metadata = definition / "metadata.yaml"

            schema = definition / "schema.yaml"

            dependencies = definition / "dependencies.yaml"

            version = definition / "version.yaml"

            if not manifest.exists():
                continue

            module = {

                "path": folder,

                "manifest": self.read_yaml(manifest),

                "metadata": self.read_yaml(metadata),

                "schema": self.read_yaml(schema),

                "dependencies": self.read_yaml(dependencies),

                "version": self.read_yaml(version),

            }

            self.registry.register(module)

            print(
                f"[Loader] {module['manifest']['name']} registrado."
            )

    def load_modules(self):

        for module in self.registry.all():

            module["loaded"] = True

    @staticmethod
    def read_yaml(path):

        if not path.exists():

            return {}

        with open(path, "r", encoding="utf-8") as file:

            return yaml.safe_load(file) or {}
