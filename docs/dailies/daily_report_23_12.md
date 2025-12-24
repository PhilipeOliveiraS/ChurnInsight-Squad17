# � Relatório Executivo da Daily Scrum: Projeto ChurnInsight (23/12/2025)

**Facilitador:** Philipe Oliveira (Tech Lead)
**Status do Projeto:** 🟡 AMARELO (Atenção - Prazo de Integração)
**Foco Tático:** Força-Tarefa de Integração End-to-End

---

## 1.0 Resumo Executivo
Este relatório consolida o status do Squad 17 no "Dia D" para a integração entre Backend e IA. O objetivo é garantir o "Happy Path" funcional antes do feriado de Natal.

**Status: Amarelo (Atenção)**
Atribuído devido ao prazo crítico de 24h para conectar os serviços. Observa-se uma mudança cultural positiva: o time migrou do "Desenvolvimento Isolado" para uma **"Força-Tarefa de Integração"**, demonstrando maturidade ao focar coletivamente no desbloqueio da dependência principal.

---

## 2.0 Status Report por Frente (Squad Pulse)

###  Backend (Raiuri, Lucas)
* **Prontidão:** Ambiente Docker e Banco de Dados configurados pelo Raiuri, estabelecendo a base para CI/CD na OCI. Autenticação avançada pelo Lucas.
* **Bloqueio Crítico:** A equipe está travada aguardando o **Contrato de Interface (JSON Schema)** da IA para conectar a autenticação ao serviço de predição.

###  Data Science (Vlademir, Stephanie)
* **Progresso:** Stephanie avançou na normalização de dados com apoio do Tech Lead. O time prepara a serialização do modelo (Pickle) e do Scaler.
* **Meta:** Transformar o modelo em um artefato pronto para ser "servido" via API.

###  Frontend (Romulo)
* **Status:** Pendente de atualização (Ausência justificada). Foco na substituição de mocks por chamadas reais.

### 👨‍💻 Tech Lead (Philipe) - O "Enabler"
* **Ação:** Assumiu o compromisso de entregar a arquitetura da API Python (FastAPI) e a documentação da interface (Swagger) hoje.
* **Impacto:** Desbloquear o Backend através da estratégia *Contract-First*.

---

## 3.0 Decisões Arquiteturais & Técnicas
Escolhas de engenharia para acelerar a entrega e garantir governança:

1.  **Contract-First Development:** O Tech Lead define o JSON Schema (entrada/saída) primeiro. Isso desacopla os times, permitindo desenvolvimento paralelo sem dependência bloqueante.
2.  **FastAPI para Microserviço de IA:** Escolhido pela alta performance assíncrona e geração automática de documentação (Swagger), facilitando o consumo pelo Java.
3.  **Persistência com Pickle:** Padrão adotado para serializar o modelo de ML, garantindo portabilidade e carregamento rápido em memória.

---

## 4.0 Gestão de Riscos & Impedimentos
Matriz de riscos atualizada para o cenário pré-feriado.

| Risco | Mitigação |
| :--- | :--- |
| **Falha na Integração (Backend-IA) antes do Natal** | **Ação Imediata:** Tech Lead codará a API e o Contrato hoje (23/12). |
| **Dependência do Backend** | **Contract-First:** O contrato libera o Backend para codar o cliente HTTP mesmo sem a IA pronta. |
| **Disponibilidade da Equipe** | **Foco Total:** Alinhamento para fechar o "Happy Path" até 24/12, liberando o feriado. |

---
*Este documento serve como registro oficial de governança e alinhamento estratégico do Squad 17.*
