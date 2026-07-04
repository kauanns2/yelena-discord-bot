# YELENA KERNEL

## Objetivo

O Kernel é o núcleo central da arquitetura da Yelena.

Ele organiza todos os sistemas da IA antes que a Engine seja iniciada.

Sua função é fornecer informações estruturais para que a Engine saiba como carregar módulos, resolver dependências e construir o contexto da conversa.

O Kernel nunca responde usuários.

O Kernel nunca gera prompts.

O Kernel nunca altera a personalidade.

Ele apenas coordena toda a arquitetura.

--------------------------------------------

## Responsabilidades

✓ Registrar grupos

✓ Registrar prioridades

✓ Registrar dependências

✓ Definir estados internos

✓ Definir ordem de carregamento

✓ Validar a arquitetura

--------------------------------------------

## Não é responsabilidade do Kernel

✗ Personalidade

✗ Emoções

✗ Memórias

✗ Conhecimento

✗ Conversação

✗ Respostas

--------------------------------------------

## Arquivos

kernel.yaml
Identidade do Kernel.

groups.yaml
Registro dos grupos cognitivos.

dependencies.yaml
Mapa de dependências entre grupos.

loading.yaml
Estratégias de carregamento.

priorities.yaml
Sistema de prioridades.

states.yaml
Estados internos do Kernel.

--------------------------------------------

## Fluxo

Bot

↓

Kernel

↓

Engine

↓

Activation

↓

Loader

↓

Planner

↓

Prompt

↓

Gemini

↓

Response

↓

Discord
