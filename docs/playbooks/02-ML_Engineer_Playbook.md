#  Guia de Missão: Machine Learning Engineer (Squad 17)

**Para:** Vlademir  
**De:** Philipe Oliveira (Tech Lead)  
**Contexto:** Hackathon ONE 2025 - Projeto ChurnInsight

---

##  Sua Importância na Equipe
Vlademir, até agora você construiu o nosso chão (o baseline com Regressão Logística). Isso foi vital para sabermos de onde partimos.

Agora, a sua missão muda. Você será o responsável por construir o motor robusto que vai desafiar a minha IA Experimental.

Eu preciso que você crie modelos sólidos, matematicamente validados, que funcionem no mundo real. Se a minha Rede Neural (que é instável e complexa) falhar, é o seu modelo que vai para produção salvar a entrega do Squad. Você é a nossa garantia de qualidade e performance.

---

##  O Mapa da Jornada (O Que Faremos e Por Quê)
Não quero apenas que você digite código. Quero que você entenda a "alma" do problema de Churn. Vamos dividir sua atuação em 3 Missões de Aprendizado.

###  Missão 1: O Combate ao Desbalanceamento (A Armadilha da Acurácia)
* **O Conceito:** Em Churn, a maioria dos clientes fica (Classe 0) e poucos saem (Classe 1). Se 90% dos clientes ficam e seu modelo chutar "Fica" para todo mundo, ele terá 90% de acurácia, mas será inútil (zero inteligência). Isso é o "Paradoxo da Acurácia".
* **Sua Tarefa:** Ensinar o modelo a ver a minoria.

**Estude & Aplique:** Técnicas de Oversampling.
1.  **SMOTE (Synthetic Minority Over-sampling Technique):** Ele cria "clientes sintéticos" parecidos com os que saíram, para equilibrar o jogo.
2.  **ADASYN:** Uma variação que foca nos casos mais difíceis de aprender.
3.  **Biblioteca Sugerida:** \imbalanced-learn\ (é padrão de mercado).

>  **Dica de Pesquisa:** Procure por "How SMOTE works visualization" no Google Imagens. Entender visualmente como ele cria os pontos novos no gráfico vai explodir sua mente.

###  Missão 2: O Poder das Árvores (Random Forest & Boosting)
* **O Conceito:** A Regressão Logística traça uma reta. Mas o comportamento humano é complexo e não linear. Árvores de Decisão criam regras ("Se salário < X e Idade > Y...").
* **Sua Tarefa:** Implementar modelos que capturam essa complexidade.

1.  **Random Forest:** Crie uma "floresta" de decisores. É um modelo robusto que dificilmente dá errado (overfitting).
2.  **Gradient Boosting (XGBoost ou LightGBM):** Aqui está o estado da arte para dados tabulares. Esses modelos aprendem com os erros das árvores anteriores.
3.  **Desafio:** Eles têm muitos hiperparâmetros (\learning_rate\, \max_depth\). Seu objetivo não é achar o número mágico na sorte, mas entender o que cada um faz.

> 💡 **Dica de Ouro:** Não use apenas o \model.fit()\. Gere o gráfico de **Feature Importance** ao final. Quero que você me diga: "Philipe, o modelo XGBoost diz que a Idade é mais importante que o Salário". Isso é Ouro para o Negócio.

### 🛡️ Missão 3: A Prova de Fogo (Validação Cruzada)
* **O Conceito:** Testar o modelo dividindo em "Treino/Teste" uma única vez é perigoso (pode ser sorte).
* **Sua Tarefa:** Implementar K-Fold Cross-Validation.

Imagine dividir o baralho em 5 partes. Treine com 4, teste com 1. Repita 5 vezes trocando as partes. A média dessas 5 notas é a verdadeira performance do seu modelo.

---

## 🤖 Manual de Uso da IA (Seu Copiloto, não sua Muleta)
Neste Hackathon, queremos ser produtivos, mas você precisa sair daqui sabendo mais do que entrou. Use o ChatGPT/Claude/Gemini da seguinte forma:

**✅ O Jeito CERTO de usar (Aprendizado Acelerado)**
* Para explicar conceitos: *"Aja como um professor sênior de Data Science. Me explique a diferença matemática entre Random Forest e XGBoost usando uma analogia simples."*
* Para debugar erros: Cole o erro e pergunte: *"Por que esse erro de 'dimension mismatch' está acontecendo no meu código de Cross-Validation?"*
* Para documentar: *"Gere docstrings no padrão Google para essa função que escrevi, explicando os parâmetros."*

**❌ O Jeito ERRADO (Muleta)**
* *"Escreva o código completo de um modelo de churn para mim."* (Você não aprende nada, e se der erro, não saberá consertar).
* Copiar e colar código sem ler linha por linha.

---

## 📚 Como Pesquisar como um Sênior
Não fique preso em tutoriais genéricos do Medium. Vá na fonte:

1.  **Scikit-Learn User Guide:** É a bíblia. Procure por "Supervised learning" e "Ensemble methods". A documentação deles explica a teoria antes do código.
2.  **Kaggle Notebooks:** Procure competições de "Bank Churn Prediction". Veja os notebooks mais votados ("Most Voted"). Não copie, leia a lógica que eles usaram para tratar os dados.

---

## ✅ Checklist de Entrega (Para a próxima revisão)
Seu objetivo é subir no Git um Notebook (ou script Python) limpo contendo:

- [ ] Aplicação de SMOTE ou técnica de balanceamento.
- [ ] Treinamento de um Random Forest.
- [ ] Treinamento de um XGBoost (ou LightGBM).
- [ ] Relatório de Métricas comparando os dois (foque em Recall e F1-Score da classe 1).
- [ ] Gráfico de Feature Importance (Quais variáveis mandam no jogo?).

Estou aqui para fazer Code Review e te destravar. Se errar, erre rápido e me chame. Confio no seu potencial para entregar nosso modelo campeão! 

**Philipe Oliveira (PH)** *Tech Lead & Squad 17 AI Researcher*
