# Personality

## Descrição

O subsistema **Personality** é responsável por definir quem a personagem é em nível psicológico. Ele reúne traços de personalidade, valores, crenças, preferências e padrões de tomada de decisão, garantindo que a Yelena mantenha uma personalidade consistente em qualquer situação.

Este módulo complementa o **Identity**, influencia diretamente o **Behavior**, orienta o **Dialogue** e serve como uma das principais fontes de contexto para toda a Web Brain.

---

## Responsabilidades

- Definir traços de personalidade.
- Registrar valores e crenças.
- Determinar preferências comportamentais.
- Influenciar decisões e reações.
- Garantir consistência psicológica.

---

## Informações armazenadas

Este subsistema pode conter informações como:

- Traços de personalidade
- Virtudes
- Defeitos
- Valores
- Crenças
- Objetivos pessoais
- Medos
- Motivações
- Preferências
- Limites
- Temperamento
- Forma de pensar

---

## Estrutura

```text
personality/
├── README.md
├── definition/
└── system/
```

---

## Integração

O Personality trabalha em conjunto com:

- Identity
- Behavior
- Dialogue
- Speech
- Presence
- Profile

---

## Papel na Web Brain

O Personality é um dos nós centrais da arquitetura. Ele fornece a base psicológica utilizada pelos demais subsistemas para produzir respostas, decisões e comportamentos coerentes.

---

## Status

- Estado: Ativo
- Persistente: Sim
- Prioridade: 1.9
