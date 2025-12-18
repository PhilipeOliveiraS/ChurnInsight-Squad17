#  Guia de Missão: Data Analyst & Analytics Engineer (Squad 17)

**Para:** Stephanie
**De:** Philipe Oliveira (Tech Lead)
**Contexto:** Hackathon ONE 2025 - Projeto *ChurnInsight*

---

##  Sua Importância na Equipe
Stephanie, quero que você grave isso: **Machine Learning é 80% Dados e 20% Modelo.**
Eu (na IA Avançada) e o Vlademir (nos Modelos Clássicos) somos totalmente dependentes de você. Se você entregar dados "sujos", com nulos mal tratados ou sem padronização, nossos modelos vão falhar, não importa o quão complexos sejam (*Garbage In, Garbage Out*).

Você é a **Guardiã da Qualidade**. Sua missão é transformar uma planilha crua em "combustível premium" para nossas IAs. Você tem a certificação, agora é hora de mostrar a prática.

---

##  O Mapa da Jornada (O Que Faremos e Por Quê)

Vamos dividir sua atuação em 3 Missões de Investigação e Engenharia. Não tenha medo de errar, tenha curiosidade de descobrir.

###  Missão 1: A Detetive de Dados (EDA - Análise Exploratória)
**O Conceito:** Antes de tentar prever o futuro, precisamos entender o passado. Como os dados se comportam?
**Sua Tarefa:** "Interrogar" o dataset.

1.  **Raio-X Inicial:** Use \df.info()\, \df.describe()\ e \df.head()\.
    * *Pergunta chave:* Temos colunas misturadas (texto e número)? Temos valores faltando (NaN)?
2.  **Caça aos Padrões Visuais:**
    * **Histogramas:** Plote a distribuição da idade (\Age\). A maioria dos clientes é jovem ou idosa?
    * **Boxplots:** Olhe para o Salário (\EstimatedSalary\) e Saldo (\Balance\). Existem pontos muito fora da curva (*outliers*)?
    * **Correlação:** Gere um *Heatmap* (mapa de calor). Será que quem tem mais \CreditScore\ tem mais \Balance\?
3.  **Ferramenta Sugerida:** Bibliotecas \pandas\, \matplotlib\ e \seaborn\. Se quiser impressionar, teste o \sweetviz\ (ele gera um relatório automático incrível).

> 💡 **O Pulo do Gato:** Não gere apenas gráficos. Escreva uma frase abaixo de cada um. Ex: *"O gráfico mostra que clientes da Alemanha têm saldo maior que os da França"*. Isso é Ouro.

---

### 🧹 Missão 2: A Limpeza (Pré-processamento)
**O Conceito:** Modelos matemáticos (como o meu e do Vlademir) não entendem texto ("Mulher", "França") e odeiam buracos (Nulos). Eles só entendem números.
**Sua Tarefa:** Traduzir o mundo real para a linguagem da máquina.

1.  **Tratando Nulos (Missing Values):**
    * Se faltar a idade de alguém, o que fazemos? Jogamos a linha fora? Preenchemos com a média das idades? Pesquise sobre *"Imputation strategies"*.
2.  **Encoding (Texto vira Número):**
    * A coluna \Gender\ tem "Male"/"Female". O modelo precisa de 0 ou 1.
    * **Label Encoding:** Transforma em 0, 1, 2. (Bom para coisas com ordem, ex: Ruim, Médio, Bom).
    * **One-Hot Encoding:** Cria novas colunas (\Is_Male\, \Is_Female\). (Melhor para \Geography\, pois a Espanha não é "maior" que a França).
3.  **Scaling (Padronização):**
    * O \Salary\ vai de 0 a 100.000. A \Age\ vai de 18 a 90. Essa diferença de escala confunde a Rede Neural.
    * Use o \StandardScaler\ ou \MinMaxScaler\ para deixar tudo na mesma régua (ex: entre 0 e 1).

---

###  Missão 3: O Insight de Ouro (Feature Engineering Básico)
**O Conceito:** Às vezes, a informação mais importante não está na coluna, mas na combinação delas.
**Sua Tarefa:** Criar uma nova variável inteligente.

* **Ideia:** Um cliente pode ter um salário alto, mas gastar tudo. Que tal criar uma coluna \Balance_Per_Salary\ (Saldo dividido pelo Salário)? Isso pode indicar se a pessoa é poupadora ou gastadora. Tente criar essa coluna nova no Pandas.

---

##  Manual de Uso da IA (Sua Mentora Particular)

Use a IA para te ensinar a sintaxe e a lógica, nunca para fazer o trabalho sem você entender.

### ✅ O Jeito CERTO de usar (Aprendizado Acelerado)
* *"Explique a diferença entre One-Hot Encoding e Label Encoding como se eu tivesse 10 anos. Qual devo usar para países?"*
* *"Como eu faço um gráfico de barras no Seaborn mudando a cor baseado no gênero? Me dê o exemplo de código."*
* *"O que é um 'Outlier' e por que ele atrapalha a média?"*

### ❌ O Jeito ERRADO (Atalho Perigoso)
* *"Faça uma análise exploratória desse arquivo csv para mim."* (Você perde a chance de treinar seu olhar analítico).

---

## � Como Pesquisar Informação
1.  **Pandas Cheat Sheet:** Digite isso no Google Imagens. Tenha uma "cola" dos comandos principais (\groupby\, \loc\, \illna\).
2.  **Documentação do Seaborn:** É cheia de exemplos visuais lindos. Escolha um gráfico que você achou bonito e tente adaptar para os nossos dados.
3.  **Kaggle:** Procure por "Titanic EDA" ou "House Prices EDA". Veja como os melhores analistas contam uma história com os dados.

---

##  Checklist de Entrega (Seu Objetivo Imediato)

Para validar seu ambiente e sua primeira entrega, preciso que você suba/compartilhe um Notebook contendo:

- [ ] Carregamento dos dados sem erros.
- [ ] Um resumo textual do que você viu no \df.describe()\ (ex: "A média de idade é X anos").
- [ ] Pelo menos 3 gráficos diferentes (ex: um de distribuição, um de contagem de Churn, um de correlação).
- [ ] Identificação de Nulos (tem ou não tem?).
- [ ] Seu primeiro Insight: Uma observação curiosa sobre os dados.

Você tem total capacidade para isso. Lembre-se: **Você está preparando o terreno onde vamos construir a vitória.** Qualquer dúvida, grite no chat! 

---
**Philipe Oliveira (PH)**
*Tech Lead & Squad 17 AI Researcher*
