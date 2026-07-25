# Profile

## Descrição

O subsistema **Profile** reúne as informações públicas e persistentes da personagem. Ele funciona como a identidade consultável da Yelena, organizando dados gerais que podem ser utilizados por outros módulos sem acessar diretamente componentes mais específicos.

O objetivo é fornecer uma visão unificada da personagem, servindo como ponto central para informações descritivas e de referência.

---

## Responsabilidades

- Centralizar informações gerais da personagem.
- Disponibilizar dados públicos para outros módulos.
- Organizar informações persistentes.
- Facilitar consultas da Engine e do Kernel.
- Reduzir duplicação de informações entre subsistemas.

---

## Informações armazenadas

Este subsistema pode conter informações como:

- Nome
- Apelidos
- Idade
- Nacionalidade
- Idiomas
- Profissão
- Ocupação
- Estado atual
- Resumo da personalidade
- Resumo da aparência
- Resumo da história
- Preferências gerais
- Informações públicas

---

## Estrutura

```text
profile/
├── README.md
├── definition/
└── system/
```

---

## Integração

O Profile recebe informações de diversos subsistemas, incluindo:

- Identity
- Appearance
- Personality
- Behavior
- Presence
- Dialogue
- Speech
- Voice Style

Também fornece informações para praticamente todos os módulos que necessitam consultar dados gerais da personagem.

---

## Papel na Web Brain

O Profile atua como um agregador de informações. Em vez de armazenar toda a lógica da personagem, ele reúne resumos e referências para facilitar consultas rápidas durante o processamento de contexto.

---

## Status

- Estado: Ativo
- Persistente: Sim
- Prioridade: 1.7
