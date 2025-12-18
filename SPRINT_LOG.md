

# 📜 SPRINT LOG & ARCHITECTURAL JOURNEY | SQUAD 17

> **Documento Vivo:** Este log registra a evolução estratégica, técnica e cultural do projeto **ChurnInsight**. Aqui documentamos não apenas o código, mas as decisões de arquitetura e governança tomadas pela liderança e pelo time.

---

## 🗓️ SPRINT 01: Planning & Arquitetura Híbrida
**Data:** 15 de Dezembro de 2025 | **Fase:** Definição Arquitetural & Início do Code

### 🚀 Resumo Executivo
Nesta Planning, elevamos o nível de maturidade do projeto. Para mitigar riscos de integração e garantir o 1º lugar, definimos uma **Estratégia Híbrida de Dados** e uma arquitetura de desenvolvimento desacoplada (**Mock-First**). O objetivo é garantir que Backend e Data Science caminhem em paralelo sem bloqueios.

### 🏛️ Decisões Estratégicas (C-Level)

#### 1. A Estratégia "Híbrida" (O Diferencial Competitivo)
Decidimos não depender apenas do dataset padrão (IBM Telco). O ChurnInsight atuará em duas camadas:
* **Motor Preditivo (Compliance):** Modelo treinado no dataset oficial da IBM para prever o *Churn Score* (Quem sai?).
* **Motor Consultivo (Inovação):** Mineração proprietária de dados (Scraping) de reviews reais do mercado brasileiro para explicar a *Causa Raiz* (Por que sai?) e sugerir ações de retenção.

#### 2. Arquitetura "Mock-First"
* **Decisão:** O Backend Java não aguardará o modelo de IA estar pronto.
* **Implementação:** Criaremos interfaces de serviço que retornam dados "Mocados" (Fictícios). Isso permite que o Frontend seja construído imediatamente. Quando a IA estiver pronta, apenas trocaremos a implementação da interface (via Spring Profiles).

#### 3. Profissionalização do Workflow
* Migração do projeto pessoal para uma **GitHub Organization**.
* Adoção do **GitHub Projects (Kanban)** para gestão de tasks, saindo do informal para o rastreável.

### 🛠️ Distribuição Tática (Sprint Backlog)

| Frente | Responsável | Missão Crítica da Semana |
| :--- | :--- | :--- |
| **Data Science** | **Vlademir** | Entregar o **Baseline Model** (Regressão Logística) usando dataset IBM Telco. *Status: MVP Entregue (Acurácia Validada).* |
| **Backend** | **Raiuri / Lucas** | Estruturar DTOs, Endpoints e Contratos de API. Subir o esqueleto Spring Boot na Organization. |
| **Mock Service** | **Felipe** | Implementar o serviço de previsão simulada para desbloquear o Frontend. |
| **Intelligence** | **Philipe** | Mineração de dados não-estruturados (NLP) e orquestração da arquitetura híbrida. |

---

## 🗓️ SPRINT 00: Fundação, Arquitetura e Cultura (Demo Report)
**Data:** 11 de Dezembro de 2025 | **Fase:** Setup & Team Building

### 🚀 Resumo Executivo
A Squad 17 (NEXT HORIZON) encerra sua primeira semana (Semana 0) com sentimento de dever cumprido! Realizamos nossa Sprint Demo consolidando nossa base técnica e alinhando nossa cultura de trabalho para o Hackathon ONE.

### 🏆 Highlights da Semana

#### 1. 🏗️ Fundação Técnica & Governança
Sob a facilitação de Philipe Oliveira, estruturamos nossa "fábrica de software" adotando padrões de mercado desde o dia 1:
* **Documentação Viva:** Aprovamos o `ONBOARDING.md` e elevamos o `README.md` ao nível de Whitepaper Técnico.
* **Governança:** Regras de proteção de branch (`main`), Code Review obrigatório e Git Flow.
* **Multidisciplinaridade:** Philipe (Tech Lead) atuando de ponta a ponta (Dados, Front e DevOps) para cobrir lacunas e garantir velocidade.

#### 2. 🧠 Cultura de Inovação & AI-Driven
Realizamos um brainstorming estratégico focado em **Agentic AI**. Decidimos que o ChurnInsight não será apenas um dashboard passivo, mas uma plataforma que gera planos de retenção autônomos.

#### 3. 👥 Reconhecimento do Time
* **Felipe & Lucas (Backend):** Pela iniciativa rápida no Spring Boot e disponibilidade para pair programming.
* **Raiuri (Backend Lead):** Pela visão de arquitetura e liderança técnica no Java.
* **Rômulo (Fullstack):** Pela visão híbrida apoiando a integração.
* **Vlademir (Data Science):** Pela paixão na análise exploratória (EDA).

---

> *"Nossa meta não é apenas entregar software, é construir uma equipe de alta performance guiada por excelência e propósito."*
>
> **Assinado:** Philipe Oliveira - Tech Lead | Squad 17