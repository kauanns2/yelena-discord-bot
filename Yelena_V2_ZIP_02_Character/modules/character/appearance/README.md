# Appearance

## Descrição

O subsistema **Appearance** é responsável por definir toda a aparência física da personagem. Ele centraliza informações visuais permanentes e semipermanentes para que todos os outros módulos descrevam a Yelena de forma consistente.

Este módulo não controla comportamento nem personalidade; seu único objetivo é representar **como a personagem é vista**.

---

## Responsabilidades

- Definir características físicas.
- Registrar traços permanentes da aparência.
- Disponibilizar descrições visuais para outros módulos.
- Garantir consistência entre todas as descrições da personagem.

---

## Informações armazenadas

Este subsistema pode conter informações como:

- Espécie
- Sexo
- Idade aparente
- Altura
- Peso
- Corpo
- Rosto
- Pele
- Olhos
- Cabelo
- Voz (aspecto físico)
- Cicatrizes
- Marcas
- Tatuagens
- Roupas padrão
- Acessórios
- Expressões naturais

---

## Estrutura

```text
appearance/
├── README.md
├── definition/
└── system/
```

---

## Integração

O Appearance fornece informações para:

- Personality
- Dialogue
- Speech
- Presence
- Profile

---

## Papel na Web Brain

O Appearance é um nó de suporte da arquitetura. Ele fornece contexto visual sempre que outro módulo precisa descrever ou interpretar a personagem.

---

## Status

- Estado: Ativo
- Persistente: Sim
- Prioridade: 1.9
