"""
Kernel da Yelena V2

Responsável por controlar o ciclo de vida do sistema.
"""

from pathlib import Path


class Kernel:

    def __init__(self, root: Path):

        self.root = root

        self.registry = None

        self.started = False

    def attach_registry(self, registry):

        self.registry = registry

        print("[Kernel] Registry conectado.")

    def boot(self):

        print("[Kernel] Inicializando Kernel...")

        self.started = True

    def shutdown(self):

        print("[Kernel] Encerrando Kernel...")

        self.started = False

    def is_running(self):

        return self.started

    def get_root(self):

        return self.root

    def get_registry(self):

        return self.registry
