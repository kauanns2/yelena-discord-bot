# Speech

## Descrição

O subsistema **Speech** define como a personagem fala durante qualquer interação. Ele controla aspectos linguísticos, estruturais e comunicativos da fala, garantindo consistência independentemente do contexto.

Enquanto o **Dialogue** decide **o que dizer**, o **Speech** determina **como dizer**.

---

## Responsabilidades

- Definir o estilo de escrita.
- Controlar vocabulário.
- Definir tamanho médio das respostas.
- Controlar uso de gírias.
- Definir formalidade.
- Controlar pontuação.
- Definir ritmo da conversa.
- Manter consistência linguística.
- Adaptar a fala ao contexto sem perder identidade.

---

## Informações armazenadas

Este subsistema pode conter informações como:

- Formalidade
- Vocabulário
- Gírias
- Expressões favoritas
- Comprimento das mensagens
- Ritmo de conversa
- Uso de emojis
- Uso de pontuação
- Uso de maiúsculas
- Ênfase
- Intensidade emocional
- Adaptação contextual
- Maneira de responder perguntas
- Maneira de iniciar conversas
- Maneira de finalizar conversas

---

## Estrutura

```text
speech/
├── README.md
├── definition/
└── system/
```

---

## Integração

O Speech trabalha em conjunto com:

- Identity
- Personality
- Behavior
- Dialogue
- Presence
- Voice Style
- Profile

---

## Papel na Web Brain

O Speech transforma intenções produzidas pelos demais módulos em mensagens naturais e consistentes, preservando a identidade comunicativa da personagem durante qualquer conversa.

---

## Status

- Estado: Ativo
- Persistente: Sim
- Prioridade: 1.8
