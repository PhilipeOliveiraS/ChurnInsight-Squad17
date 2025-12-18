#  Daily Scrum Report - 16/12/2025
**Duração:** ~2h 45min
**Facilitador:** Philipe Oliveira (Tech Lead)

###  Check-in de Equipe & Papéis (Definidos na Daily)
* **Philipe:** Tech Lead / Platform Engineering / Data Science.
* **Raiuri:** Lead de Backend (Delegado pelo Tech Lead).
* **Romulo:** Lead de Frontend / UX (Apresentou protótipo visual).
* **Vlademir:** Data Science (Foco em Modelagem ML).
* **Stephanie:** Data Science / Dados (Onboarding iniciado).
* **Lucas:** Backend Developer (Foco em DTOs/Contratos).
* **Felipe:** Backend Developer (Foco em Mock/Lógica).

###  Status Report & Entregas
1.  **Backend (Raiuri/Lucas/Felipe):**
    * **Impedimento Crítico:** O monorepo atual gerou conflitos de IDE e \.gitignore\ para o time de Java.
    * **Decisão Arquitetural:** Raiuri propôs e o time acatou a separação do Backend Java em um repositório dedicado dentro da Organização para destravar o desenvolvimento.
    * **Progresso:** Lucas já estruturou localmente os \Controllers\ e \DTOs\. Felipe já possui a lógica dos dados mockados, aguardando apenas o endpoint.

2.  **Data Science (Vlademir/Stephanie/Philipe):**
    * **Vlademir:** Concluiu o baseline (Regressão Logística). Iniciará a implementação do *Random Forest* para comparar a acurácia.
    * **Stephanie:** Iniciou o onboarding. Tarefa imediata é consumir a documentação (Sprint Log/Readme) e o Notebook do Colab para se integrar.

3.  **Frontend/UX (Romulo):**
    * **Demo Apresentada:** Romulo compartilhou tela mostrando uma interface funcional com simulação de entrada de dados, cálculo de risco de churn e *Dark/Light Mode* implementado.
    * **Ação:** Instruído pelo Tech Lead a subir o código imediatamente, mesmo que incompleto, para registrar atividade.

###  Plano de Ação - Próximas 24 Horas (Tarefas Distribuídas)

####  Tech Lead (Philipe)
- [ ] **Infra:** Criar a GitHub Organization \NextHorizon-Squad17\.
- [ ] **Multi-Repo:** Criar os repositórios \ChurnInsight-Backend\ e \ChurnInsight-Frontend\ na Org.
- [ ] **Access:** Adicionar todos os membros (via e-mail) na Organização e configurar permissões.
- [ ] **Docs:** Atualizar README principal linkando os novos repositórios.

#### ☕ Squad Backend (Liderança: Raiuri)
- **Raiuri:**
    - [ ] Subir a estrutura base ("esqueleto") do Spring Boot no novo repositório de Backend.
    - [ ] Configurar o *Project Board* com as tarefas de backend distribuídas para Felipe e Lucas.
    - [ ] Enviar e-mail para convite da Org.
- **Lucas:**
    - [ ] Migrar o código local (DTOs/Controllers) para o novo repositório assim que o Raiuri subir a base.
    - [ ] Finalizar a definição dos contratos (\CustomerDTO\, \ChurnResponseDTO\) até o fim da semana.
- **Felipe:**
    - [ ] Integrar a lógica de *Mock Data* (JSON) no endpoint que o Lucas vai criar.
    - [ ] Realizar Pull Request da feature de Mock no novo repositório.

####  Squad Frontend (Liderança: Romulo)
- **Romulo:**
    - [ ] Enviar e-mail pendente para convite da Org.
    - [ ] Inicializar o repositório \ChurnInsight-Frontend\ com a estrutura React/Vite.
    - [ ] Realizar **Push** do código apresentado na Daily (Tela de Simulação + Dark Mode) para garantir contribuição no gráfico do GitHub.

####  Squad Data Science (Liderança: Philipe/Vlademir)
- **Vlademir:**
    - [ ] Treinar modelo *Random Forest* no Colab.
    - [ ] Gerar relatório comparativo de acurácia (Baseline vs Random Forest).
- **Stephanie:**
    - [ ] Enviar e-mail pendente para convite da Org.
    - [ ] Leitura completa do \SPRINT_LOG.md\ e histórico do chat para nivelamento.
    - [ ] Acessar o Google Colab do projeto e rodar as células para validar o ambiente.
    - [ ] Definir com Philipe qual tarefa específica de dados irá assumir após o estudo inicial.
