# 📝 Ata de Reunião: Daily Scrum - 17/12/2025

**Foco:** Reta final para Sprint Demo & Alinhamento de Infraestrutura.

---

## 👥 Participantes
* ✅ **Presentes:** PHILIPE (Tech Lead), RAIURI (Back Lead), Rômulo (Front Lead), Lucas (Back), Felipe (Back).
*  **Ausentes:** Vlademir (Justificado/Trabalho), Stephanie (Não justificado).

---

##  Decisões & Deliberações

### 1. Infraestrutura & GitHub
* **Segurança:** Branches \main\ e \develop\ protegidas. Merge direto proibido (exige PR + Review).
* **Correção de Rota (Backend):** Identificada duplicidade de branch (\development\ criada por engano vs \develop\ oficial).
    * **Ação:** RAIURI fará o merge para unificar na \develop\.
* **Documentação:** Guia de Git para Data Science criado e disponível em Recursos.

### 2. Status Técnico
* **Backend:** Código base submetido. Lucas e Felipe desbloqueados (problema de JDK resolvido). Foco total em DTOs de autenticação.
* **Frontend:** Repositório criado. Rômulo aguarda estrutura do JSON (nomes dos campos) para criar telas mockadas.

### 3. Estratégia para Sprint Demo (Amanhã - 19h)
* **Liderança:** Devido a compromisso acadêmico de PHILIPE, **RAIURI assumirá a condução da Demo**.
* **O que será apresentado:** Vídeo funcional da aplicação (Frontend com dados mockados + Backend estrutural).
* **Plano B:** Se a API não integrar a tempo, o Front apresenta com dados fictícios ("Mocks") para garantir o visual.

---

##  Plano de Ação (Próximas 24h)

| Responsável | Ação | Prazo |
| :--- | :--- | :--- |
| **RAIURI** | Corrigir branch \development\ -> \develop\ e criar Cards no Kanban. | Imediato |
| **LUCAS/FELIPE** | Clonar repo correto e finalizar DTOs de Autenticação. | Hoje a noite |
| **RÔMULO** | Criar telas mockadas (Login/Dashboard) para o vídeo. | Amanhã (16h) |
| **PHILIPE** | Gerar entregáveis burocráticos (PDFs, Links) e editar o vídeo final. | Amanhã (Tarde) |
| **DATA SCIENCE** | Subir notebooks para o repositório (Força-tarefa PHILIPE). | Amanhã |

---

> **🔗 Links Úteis:**
> * [Repositório Backend](https://github.com/NextHorizon-Squad17/ChurnInsight-Backend)
> * [Repositório Frontend](https://github.com/NextHorizon-Squad17/ChurnInsight-Frontend)
> * [Guia Git para Data Science](https://github.com/NextHorizon-Squad17/ChurnInsight-Squad17/blob/main/docs/GUIA_COLAB_GIT.md)
