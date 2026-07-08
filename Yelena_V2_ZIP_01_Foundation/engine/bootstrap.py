"""
===========================================================
YELENA V2
Engine Bootstrap
===========================================================

Responsável por inicializar toda a arquitetura da Yelena.

Fluxo:

Bot
 ↓
Kernel
 ↓
Bootstrap
 ↓
Loader
 ↓
Registry
 ↓
Arquitetura
"""

from engine.loader import ModuleLoader
from engine.registry import ModuleRegistry


class Bootstrap:
    """
    Inicializador principal da arquitetura.
    """

    def __init__(self, kernel):

        self.kernel = kernel

        self.registry = ModuleRegistry()

        self.loader = ModuleLoader(self.registry)

    def initialize(self):

        print("===================================")
        print(" Engine Bootstrap")
        print("===================================")

        # Inicializa o Kernel
        self.kernel.boot()

        # Procura todos os módulos
        self.loader.scan_modules()

        # Carrega os módulos encontrados
        self.loader.load_modules()

        # Entrega o registro ao Kernel
        self.kernel.attach_registry(self.registry)

        print(
            f"[Engine] {self.registry.count()} módulos registrados."
        )

        print("[Engine] Inicialização concluída.")
