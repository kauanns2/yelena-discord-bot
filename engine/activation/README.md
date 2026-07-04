# Activation Engine

## Objetivo

O Activation Engine é responsável por decidir quais módulos da Yelena serão carregados para responder uma mensagem.

Ele reduz o consumo de contexto do Gemini carregando apenas o necessário.

---

## Pipeline

1. Recebe a mensagem do usuário.
2. Analisa intenção.
3. Detecta assunto.
4. Detecta emoção.
5. Detecta necessidade de memória.
6. Detecta necessidade de personalidade.
7. Detecta necessidade de planejamento.
8. Seleciona módulos.
9. Envia os módulos para o Loader.

---

## Responsabilidades

- Ativar módulos.
- Desativar módulos desnecessários.
- Definir prioridade.
- Economizar tokens.
- Melhorar velocidade.
- Evitar contexto inútil.

---

## Nunca faz

- Não responde usuários.
- Não cria respostas.
- Não interpreta personalidade.
- Não conversa.

Ele apenas decide o que será carregado.
