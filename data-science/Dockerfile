FROM python:3.10-slim

WORKDIR /app

# Dependências de sistema
RUN apt-get update && apt-get install -y libgomp1

# 1. Instalação de Pacotes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copia Código Fonte
COPY api/main.py api/main.py
# Cria um arquivo __init__.py para tratar a raiz como pacote (truque para imports funcionarem)
RUN touch __init__.py 

# 3. Copia o Modelo
COPY model/churn_model_final.pkl model/churn_model_final.pkl

# 4. --- NOVO: Copia a pasta de testes ---
COPY tests/ tests/

# 5. Variáveis
# (O .env será injetado no run, não copiado)

EXPOSE 8000

# Comando padrão continua sendo subir a API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]