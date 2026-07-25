# Identity

## Descrição

O subsistema **Identity** é responsável por definir e manter a identidade permanente da personagem. Ele reúne as informações fundamentais que determinam quem a personagem é e fornece esses dados como referência para todos os demais subsistemas do módulo **Character**.

A identidade representa características que normalmente não mudam durante a execução do sistema, servindo como base para personalidade, comportamento, aparência, diálogo, fala e presença.

---

## Responsabilidades

- Definir a identidade principal da personagem.
- Disponibilizar informações de identidade para outros módulos.
- Garantir consistência entre os dados compartilhados.
- Atuar como um dos nós centrais da Web Brain.

---

## Estrutura

```text
identity/
├── README.md
├── definition/
│   ├── manifest.yaml
│   ├── metadata.yaml
│   ├── schema.yaml
│   ├── dependencies.yaml
│   └── version.yaml
└── system/
    ├── registry.yaml
    ├── state.yaml
    └── links.yaml
