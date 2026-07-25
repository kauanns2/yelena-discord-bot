# Behavior

## Descrição

O subsistema **Behavior** é responsável por definir como a personagem age em diferentes situações. Ele estabelece padrões de comportamento, reações, hábitos, linguagem corporal e tomada de decisões, garantindo que a Yelena mantenha uma personalidade consistente em qualquer contexto.

Este módulo não define **quem** a personagem é (Identity) nem **como ela aparenta ser** (Appearance), mas sim **como ela se comporta**.

---

## Responsabilidades

- Definir padrões de comportamento.
- Controlar reações naturais da personagem.
- Registrar hábitos e costumes.
- Fornecer contexto comportamental para os demais módulos.
- Garantir consistência nas ações e respostas.

---

## Informações armazenadas

Este subsistema pode conter informações como:

- Hábitos
- Rotina
- Linguagem corporal
- Gestos
- Postura
- Maneirismos
- Reações emocionais
- Reações sociais
- Impulsividade
- Autocontrole
- Nível de iniciativa
- Forma de resolver conflitos
- Adaptação a diferentes ambientes

---

## Estrutura

```text
behavior/
├── README.md
├── definition/
└── system/
```

---

## Integração

O Behavior trabalha em conjunto com:

- Identity
- Personality
- Dialogue
- Speech
- Presence
- Profile

---

## Papel na Web Brain

O Behavior é um nó de suporte da arquitetura. Ele utiliza a identidade e a personalidade da personagem para produzir comportamentos coerentes, permitindo que o Kernel selecione ações consistentes conforme o contexto.

---

## Status

- Estado: Ativo
- Persistente: Sim
- Prioridade: 1.8
