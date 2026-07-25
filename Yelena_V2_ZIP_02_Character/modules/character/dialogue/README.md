# Dialogue

## Descrição

O subsistema **Dialogue** é responsável por definir como a personagem organiza e constrói suas mensagens durante uma conversa. Ele estabelece o estilo de resposta, o fluxo do diálogo, a forma de manter contexto e a coerência das interações.

Este módulo não define a personalidade da personagem nem sua voz; ele determina **como as conversas são estruturadas**.

---

## Responsabilidades

- Definir o fluxo das conversas.
- Organizar respostas de forma natural.
- Manter contexto entre mensagens.
- Controlar continuidade dos diálogos.
- Garantir coerência durante interações longas.

---

## Informações armazenadas

Este subsistema pode conter informações como:

- Estrutura de respostas
- Continuidade de contexto
- Formas de iniciar conversas
- Formas de encerrar conversas
- Ritmo das mensagens
- Organização de tópicos
- Estratégias para perguntas e respostas
- Continuidade de assuntos

---

## Estrutura

```text
dialogue/
├── README.md
├── definition/
└── system/
```

---

## Integração

O Dialogue trabalha em conjunto com:

- Identity
- Personality
- Behavior
- Speech
- Presence
- Profile

---

## Papel na Web Brain

O Dialogue atua como um nó de comunicação da arquitetura. Ele utiliza informações fornecidas pelos demais subsistemas para construir respostas consistentes, naturais e contextualizadas.

---

## Status

- Estado: Ativo
- Persistente: Sim
- Prioridade: 1.7
