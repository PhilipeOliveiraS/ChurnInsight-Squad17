# 📉 ChurnInsight (Squad 17)

> **Oracle ONE Next Education | Hackathon No Country**
> *Plataforma de Inteligência Preditiva para Retenção de Clientes (Churn Prediction).*

![Status](https://img.shields.io/badge/Status-MVP_Em_Desenvolvimento-yellow) ![Java](https://img.shields.io/badge/Backend-Java_Spring_Boot-orange) ![Python](https://img.shields.io/badge/AI-Scikit_Learn-blue) ![Front](https://img.shields.io/badge/Frontend-React_Dashboard-cyan) ![Cloud](https://img.shields.io/badge/Deploy-Oracle_OCI-red)

## 🎯 O Problema de Negócio
Empresas de telecomunicações perdem milhões anualmente com a evasão de clientes (Churn). O desafio não é apenas prever *quem* vai sair, mas entender *por que* e *como* agir preventivamente.

## 💡 Nossa Solução (Value Proposition)
O **ChurnInsight** não é apenas um modelo de previsão. É um **Ecossistema de Decisão** que entrega:
1.  **Visão de Negócio:** Dashboard executivo com mapas de calor (Geolocalização) e análise de causa raiz.
2.  **Visão Técnica:** Monitoramento de latência da API, logs de requisição e acurácia do modelo em tempo real.
3.  **Arquitetura Enterprise:** Microsserviços desacoplados rodando em contêineres na Oracle Cloud.

## 🏗️ Arquitetura Técnica (Microserviços)

O sistema opera em uma arquitetura distribuída para garantir escalabilidade e manutenção:

* **🧠 Cérebro (Data Science):** Modelo de Classificação (Random Forest/XGBoost) treinado em Python, exposto via API leve (FastAPI).
* **⚙️ Motor (Backend):** API REST em **Java 17 (Spring Boot)** que orquestra as requisições, valida regras de negócio e persiste dados.
* **🎨 Vitrine (Frontend):** Dashboard interativo (React/Streamlit) com modos *Dark/Light* e *Multi-language (PT/ES/EN)*.
* **☁️ Infraestrutura:** Docker Containers orquestrados na Oracle Cloud Infrastructure (OCI).

## 🗂️ Sobre os Dados (Dataset Enriched)
Utilizamos uma versão enriquecida do dataset padrão da indústria (**IBM Telco Churn V2**), contendo **7.043 registros** e **33 colunas**.

### Diferenciais do Dataset:
* ✅ **Geolocalização:** Latitude/Longitude e Cidade para mapas de calor de risco.
* ✅ **Causa Raiz:** Coluna `Churn Reason` para análise qualitativa (removida no treino para evitar *Data Leakage*).
* ✅ **Valor:** `CLTV` (Customer Lifetime Value) para priorização de retenção financeira.

## 🚀 Como Executar
1. Clone o repositório.
2. Verifique os READMEs individuais nas pastas `/backend` e `/frontend` (em breve).

---
**Squad 17 - Oracle ONE G8**
*Construindo o futuro da retenção de clientes.*