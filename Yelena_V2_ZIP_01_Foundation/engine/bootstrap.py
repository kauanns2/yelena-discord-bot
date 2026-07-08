"""
Engine Bootstrap

Inicializa toda a arquitetura da Yelena.
"""

from engine.loader import ModuleLoader
from engine.registry import ModuleRegistry


class Bootstrap:

    def __init__(self, kernel):

        self.kernel = kernel

        self.registry = ModuleRegistry()

        self.loader = ModuleLoader(self.registry)

    def initialize(self):

        print("[Engine] Inicializando...")

        self.loader.scan_modules()

        self.loader.load_modules()

        self.kernel.attach_registry(self.registry)

        print("[Engine] Inicialização concluída.")
