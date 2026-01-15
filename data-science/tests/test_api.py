import os
import sys
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

# 1. Configuração de Caminho (Para o Python achar a pasta 'api')
# Adiciona o diretório pai ao path para importar o main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.main import app

# 2. Inicializa o Cliente de Teste
client = TestClient(app)

# --- TESTES DE SAÚDE (HEALTH CHECK) ---
def test_health_check():
    """Verifica se a API está de pé e o modelo carregado."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "model_loaded": True}

# --- TESTES DE PREDIÇÃO (HAPPY PATH) ---
# Usamos @patch para 'enganar' a função que chama o Google Gemini.
# Não queremos gastar créditos de API rodando testes.
@patch("api.main.generate_retention_plan")
def test_predict_churn_high_risk(mock_genai):
    """Teste de um cliente com perfil de ALTO RISCO (Simulado)."""
    
    # Configuramos o Mock para retornar um texto fixo sem chamar o Google
    mock_genai.return_value = "PLANO SIMULADO: Oferecer desconto."

    payload = {
        "Gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "TenureMonths": 1,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic", # Fator de risco alto
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",     # Fator de risco alto
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check", # Fator de risco alto
        "MonthlyCharges": 100.00,
        "TotalCharges": 100.00
    }

    response = client.post("/predict", json=payload)

    # Asserções (O que esperamos receber)
    assert response.status_code == 200
    data = response.json()
    
    assert "prediction" in data
    assert "probability" in data
    assert "risk_level" in data
    assert "retention_strategy" in data
    
    # Como os dados são de alto risco, esperamos probabilidade alta
    # (Baseado no modelo treinado, Fiber+Month-to-month costuma ser churn)
    # Nota: Se o modelo mudar, isso pode falhar, mas é um bom smoke test.
    assert data["risk_level"] in ["ALTO", "MÉDIO"] 
    assert data["retention_strategy"] == "PLANO SIMULADO: Oferecer desconto."

# --- TESTES DE VALIDAÇÃO (SAD PATH) ---
def test_predict_validation_error():
    """Verifica se a API rejeita dados inválidos (Proteção Literal)."""
    payload = {
        "Gender": "Alien", # Valor inválido (Só aceita Male/Female)
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "TenureMonths": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 70.0,
        "TotalCharges": 800.0
    }

    response = client.post("/predict", json=payload)
    
    # Deve retornar 422 Unprocessable Entity
    assert response.status_code == 422
    assert "Alien" in response.text # O erro deve mencionar o valor errado