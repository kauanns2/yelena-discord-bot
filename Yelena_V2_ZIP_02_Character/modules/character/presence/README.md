# Presence

## Descrição

O subsistema **Presence** é responsável por definir como a personagem é percebida durante uma interação. Ele controla a impressão que transmite, sua energia, postura social, proximidade emocional e impacto nas conversas.

Enquanto o **Appearance** define como ela é fisicamente e o **Personality** define quem ela é, o **Presence** define **como ela ocupa o ambiente e influencia as pessoas ao seu redor**.

---

## Responsabilidades

- Definir a presença social da personagem.
- Controlar postura e impacto durante interações.
- Determinar nível de proximidade emocional.
- Manter consistência na forma como a personagem é percebida.
- Integrar sinais sociais com comportamento e diálogo.

---

## Informações armazenadas

Este subsistema pode conter informações como:

- Presença social
- Carisma
- Confiança
- Postura
- Energia
- Aura
- Distância interpessoal
- Nível de intimidação
- Nível de acolhimento
- Forma de chamar atenção
- Reação ao ambiente
- Adaptação social

---

## Estrutura

```text
presence/
├── README.md
├── definition/
└── system/
```

---

## Integração

O Presence trabalha em conjunto com:

- Identity
- Personality
- Behavior
- Dialogue
- Speech
- Appearance
- Profile

---

## Papel na Web Brain

O Presence atua como um nó intermediário da arquitetura. Ele transforma informações de personalidade, comportamento e aparência em uma percepção social consistente durante qualquer interação.

---

## Status

- Estado: Ativo
- Persistente: Sim
- Prioridade: 1.8
