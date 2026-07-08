# Kernel

## Objetivo

O Kernel é o núcleo operacional da arquitetura Yelena V2.

Ele é responsável por controlar todo o ciclo de vida do sistema, registrar os módulos disponíveis e navegar pela arquitetura em forma de teia, carregando apenas as informações realmente necessárias para cada tarefa.

O Kernel não possui personalidade, memória, emoções ou conhecimento. Sua responsabilidade é fornecer uma base estável para que todos os módulos especializados possam funcionar de maneira integrada.

---

# Filosofia

A arquitetura da Yelena NÃO carrega todos os módulos ao mesmo tempo.

O Kernel trabalha como um navegador da teia da arquitetura.

Cada módulo representa um nó especializado.

Quando uma solicitação chega ao sistema, o Kernel identifica quais nós são necessários e percorre apenas os caminhos relevantes.

Isso reduz consumo de memória, melhora desempenho e evita o envio de informações desnecessárias ao modelo de IA.

---

# Responsabilidades

O Kernel é responsável por:

- inicializar a arquitetura;
- localizar módulos registrados;
- registrar novos módulos;
- controlar o ciclo de vida dos módulos;
- navegar pela teia de conhecimento;
- disponibilizar serviços internos ao Engine;
- validar módulos antes do carregamento;
- gerenciar estados internos do sistema.

---

# O que o Kernel NÃO faz

O Kernel nunca deve:

- responder usuários;
- construir prompts;
- decidir respostas;
- interpretar emoções;
- armazenar conhecimento;
- gerar personalidade.

Essas funções pertencem aos módulos especializados.

---

# Fluxo de funcionamento

Sistema iniciado

↓

Kernel inicializa

↓

Localiza módulos

↓

Registra módulos

↓

Recebe solicitação

↓

Navega pela teia

↓

Entrega apenas os módulos necessários ao Engine

↓

Aguarda nova solicitação

---

# Estrutura

kernel/

- definition/
- README.md

A pasta **definition** contém todas as definições estruturais utilizadas pelo Kernel.

---

# Estado

Status: Ativo

Prioridade: Máxima

Camada: Infraestrutura

---

# Observações

O Kernel representa o ponto central de navegação da arquitetura.

Toda a comunicação entre módulos deve passar por ele ou por serviços disponibilizados por ele.

Mudanças neste módulo podem impactar toda a arquitetura.
