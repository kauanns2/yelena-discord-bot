"""
===========================================================
YELENA V2
Bootstrap
===========================================================

Este arquivo é apenas o ponto de entrada da arquitetura.

Ele NÃO contém lógica da IA.

Todas as responsabilidades são delegadas aos módulos.

Fluxo:

Bot
 ↓
Kernel
 ↓
Engine
 ↓
Arquitetura
 ↓
Discord

===========================================================
"""

from pathlib import Path

from engine.bootstrap import Bootstrap
from kernel.kernel import Kernel


PROJECT_ROOT = Path(__file__).resolve().parent


def main():

    print("===================================")
    print(" Inicializando Yelena V2")
    print("===================================")

    kernel = Kernel(PROJECT_ROOT)

    bootstrap = Bootstrap(kernel)

    bootstrap.initialize()

    print("Sistema iniciado com sucesso.")


if __name__ == "__main__":
    main()
