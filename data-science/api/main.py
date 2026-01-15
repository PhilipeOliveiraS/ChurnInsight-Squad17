import os
import sys
import pickle
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
import google.genai as genai
from google.genai.types import GenerateContentConfig
from dotenv import load_dotenv

# 1. Configuração Inicial e Carregamento de Variáveis
load_dotenv()
app = FastAPI(title="ChurnInsight Intelligence API", version="2.2 - Enterprise Pathing")

# 2. Configuração de Caminhos (Path Resolution)
# Isso garante que funcione tanto rodando de '/app' (Docker) quanto de '/data-science' (Local)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "churn_model_final.pkl")

# 3. Carregar API Key
GEMINI_KEY = os.getenv("GOOGLE_API_KEY")
if not GEMINI_KEY:
    print("⚠️ AVISO DE SEGURANÇA: GOOGLE_API_KEY não encontrada no ambiente.")

# 4. Carregar Modelo ML
pipeline = None
try:
    with open(MODEL_PATH, "rb") as f:
        pipeline = pickle.load(f)
    print(f"✅ Modelo carregado com sucesso de: {MODEL_PATH}")
except FileNotFoundError:
    print(f"❌ ERRO CRÍTICO: Modelo não encontrado em {MODEL_PATH}")
    # Não paramos a API para permitir health checks, mas predict falhará
except Exception as e:
    print(f"❌ Erro ao carregar pickle: {str(e)}")

# 5. Contrato de Dados (DTO) - Validado com Literal
class CustomerData(BaseModel):
    # Dados Demográficos
    Gender: Literal["Male", "Female"]
    SeniorCitizen: int 
    Partner: Literal["Yes", "No"]
    Dependents: Literal["Yes", "No"]
    
    # Dados de Serviço
    TenureMonths: int
    PhoneService: Literal["Yes", "No"]
    MultipleLines: Literal["Yes", "No", "No phone service"]
    InternetService: Literal["DSL", "Fiber optic", "No"]
    OnlineSecurity: Literal["Yes", "No", "No internet service"]
    OnlineBackup: Literal["Yes", "No", "No internet service"]
    DeviceProtection: Literal["Yes", "No", "No internet service"]
    TechSupport: Literal["Yes", "No", "No internet service"]
    StreamingTV: Literal["Yes", "No", "No internet service"]
    StreamingMovies: Literal["Yes", "No", "No internet service"]
    
    # Dados Financeiros e Contratuais
    Contract: Literal["Month-to-month", "One year", "Two year"]
    PaperlessBilling: Literal["Yes", "No"]
    PaymentMethod: Literal["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    MonthlyCharges: float
    TotalCharges: float

# 6. Motor de Inteligência Generativa (GenAI)
def generate_retention_plan(churn_prob, customer_profile):
    if not GEMINI_KEY:
        return "Plano de retenção indisponível (Chave de API não configurada)."
    
    try:
        client = genai.Client(api_key=GEMINI_KEY)
        
        prompt = f"""
        CONTEXTO: Cliente Telecom com probabilidade de Churn de {churn_prob:.1%}.
        PERFIL TÉCNICO: {customer_profile}
        
        TAREFA: Aja como um Especialista Sênior em Sucesso do Cliente.
        Crie um plano tático de 3 ações imediatas para evitar o cancelamento.
        REGRAS:
        1. Seja direto e comercial.
        2. Foque em resolver dores ligadas ao tipo de contrato e serviço (ex: Fibra, Preço).
        3. Responda em Português do Brasil.
        """
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=prompt,
            config=GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=500
            )
        )
        return response.text
    except Exception as e:
        return f"Erro no processamento GenAI: {str(e)}"

# 7. Endpoint Principal: Predição + Prescrição
@app.post("/predict")
def predict_churn(data: CustomerData):
    if pipeline is None:
        raise HTTPException(status_code=500, detail="Modelo ML não está carregado no servidor.")

    try:
        # A. Preparação dos Dados (Mapeamento JSON -> DataFrame)
        input_dict = {
            'Gender': [data.Gender],
            'Senior Citizen': [data.SeniorCitizen],
            'Partner': [data.Partner],
            'Dependents': [data.Dependents],
            'Tenure Months': [data.TenureMonths],
            'Phone Service': [data.PhoneService],
            'Multiple Lines': [data.MultipleLines],
            'Internet Service': [data.InternetService],
            'Online Security': [data.OnlineSecurity],
            'Online Backup': [data.OnlineBackup],
            'Device Protection': [data.DeviceProtection],
            'Tech Support': [data.TechSupport],
            'Streaming TV': [data.StreamingTV],
            'Streaming Movies': [data.StreamingMovies],
            'Contract': [data.Contract],
            'PaperlessBilling': [data.PaperlessBilling], # Ajuste de nome se necessário pelo modelo
            'Paperless Billing': [data.PaperlessBilling], # Garantindo compatibilidade com ambas grafias
            'Payment Method': [data.PaymentMethod],
            'Monthly Charges': [data.MonthlyCharges],
            'TotalCharges': [data.TotalCharges]
        }
        
        # Correção rápida para garantir que o modelo ache a coluna certa (com ou sem espaço)
        # O modelo foi treinado com 'Paperless Billing' (com espaço), mas o JSON pode vir sem.
        # O dict acima garante que a chave exista.
        
        df_input = pd.DataFrame(input_dict)
        
        # Remove colunas duplicadas ou desnecessárias se houver
        df_input = df_input.loc[:, ~df_input.columns.duplicated()]

        # B. Predição (Core ML)
        # O pipeline já contem o StandardScaler e OneHotEncoder
        prediction = pipeline.predict(df_input)[0]
        probability = pipeline.predict_proba(df_input)[0][1]

        # C. Lógica de Negócio e GenAI
        churn_risk = "BAIXO"
        retention_plan = "Cliente saudável. Monitoramento padrão."

        if probability > 0.50: 
            churn_risk = "ALTO" if probability > 0.75 else "MÉDIO"
            
            # Criação do Contexto para a IA
            profile_summary = (f"Gênero: {data.Gender}, Idade/Senior: {data.SeniorCitizen}, "
                               f"Contrato: {data.Contract}, Internet: {data.InternetService}, "
                               f"Pagamento: {data.PaymentMethod}, Gasto Mensal: R${data.MonthlyCharges}")
            
            retention_plan = generate_retention_plan(probability, profile_summary)

        # D. Resposta Final
        return {
            "prediction": int(prediction),
            "probability": float(round(probability, 4)),
            "risk_level": churn_risk,
            "retention_strategy": retention_plan
        }

    except Exception as e:
        print(f"❌ Erro na predição: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro interno de processamento: {str(e)}")

# 8. Health Check
@app.get("/health")
def health_check():
    return {
        "status": "ok", 
        "service": "ChurnInsight Intelligence", 
        "model_loaded": pipeline is not None
    }