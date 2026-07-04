# ARCHITECTURE

---

# Visão Geral

A arquitetura da Yelena é baseada em sistemas independentes.

Cada sistema possui uma única responsabilidade.

A comunicação acontece sempre de cima para baixo.

Nenhum módulo pode ignorar o Kernel.

---

# Arquitetura Geral

```
Discord
    │
    ▼
 bot.py
    │
    ▼
━━━━━━━━━━━━━━━━━━━━━━━━━━
        KERNEL
━━━━━━━━━━━━━━━━━━━━━━━━━━
│
├── groups
├── dependencies
├── loading
├── priorities
└── states
    │
    ▼
━━━━━━━━━━━━━━━━━━━━━━━━━━
        ENGINE
━━━━━━━━━━━━━━━━━━━━━━━━━━
│
├── Activation
├── Loader
├── Context
├── Memory
├── Planner
├── Prompt
├── Validator
└── Response
    │
    ▼
Gemini
    │
    ▼
Discord
```

---

# Fluxo Completo

1. O usuário envia uma mensagem.

↓

2. bot.py recebe.

↓

3. Kernel inicializa.

↓

4. Engine consulta o Kernel.

↓

5. Activation identifica os grupos necessários.

↓

6. Loader carrega somente os módulos necessários.

↓

7. Context organiza todas as informações.

↓

8. Planner monta o plano de resposta.

↓

9. Prompt gera o prompt final.

↓

10. Validator verifica consistência.

↓

11. Gemini responde.

↓

12. Response adapta a resposta ao estilo da Yelena.

↓

13. Discord recebe a resposta.

---

# Hierarquia

Kernel

↓

Engine

↓

Sistemas

↓

Grupos

↓

Módulos

↓

Arquivos YAML

---

# Responsabilidade do Kernel

• Registrar grupos

• Registrar prioridades

• Registrar dependências

• Registrar estados

• Validar arquitetura

• Controlar carregamento

---

# Responsabilidade da Engine

• Interpretar mensagens

• Ativar grupos

• Carregar módulos

• Construir contexto

• Planejar resposta

• Gerar prompt

• Validar saída

• Entregar resposta

---

# Comunicação

Kernel

↓

Engine

↓

Activation

↓

Loader

↓

Context

↓

Planner

↓

Prompt

↓

Validator

↓

Gemini

↓

Response

---

# Modularidade

Todos os grupos funcionam de maneira independente.

Cada grupo possui seus próprios módulos.

Cada módulo possui seus próprios arquivos.

Nenhum grupo pode modificar outro grupo diretamente.

Toda interação acontece através da Engine.

---

# Objetivo

Esta arquitetura foi criada para permitir expansão contínua sem necessidade de alterar a estrutura principal do sistema.

Novos grupos podem ser adicionados.

Novos módulos podem ser registrados.

A Engine continuará funcionando utilizando as regras definidas pelo Kernel.
