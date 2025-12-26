# Health Insurance Premium Model API

A production-grade machine learning inference service for predicting health insurance premiums.
The model is exposed as a REST API using FastAPI and is designed to be consumed by any client
(web applications, backend services, mobile apps, or external systems).

This repository contains only the model inference layer.
No UI or frontend logic is included.

---

## Use Case

This service predicts health insurance premiums based on:
- Demographics
- Income
- Lifestyle factors
- Medical history
- Insurance plan selection

---

## Architecture Overview
````
Client (Web / Mobile / Backend)
        |
        |  HTTP (JSON)
        v
FastAPI Model Inference Service
        |
        v
Trained ML Models + Scalers

---
````
## Project Structure
````
health-insurance-premium-model-api/
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── inference.py
│   └── schemas.py
├── artifacts/
├── tests/
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

---
````
## Running the API Locally
````
pip install -r requirements.txt
uvicorn api.main:app --reload

---
````
## API Usage
````
POST /predict

Request:
{
  "age": 30,
  "dependants": 2,
  "income": 12,
  "genetical_risk": 1,
  "insurance_plan": "Gold",
  "gender": "Male",
  "marital_status": "Married",
  "employment_status": "Salaried",
  "bmi": "Overweight",
  "smoking": "No Smoking",
  "region": "Southwest",
  "medical_history": "Diabetes"
}

Response:
{
  "predicted_premium": 5994
}

---
````
## Example: Python Client
````
import requests

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={
        "age": 35,
        "dependants": 2,
        "income": 15,
        "genetical_risk": 1,
        "insurance_plan": "Gold",
        "gender": "Male",
        "marital_status": "Married",
        "employment_status": "Salaried",
        "bmi": "Overweight",
        "smoking": "Occasional",
        "region": "Southwest",
        "medical_history": "Diabetes"
    }
)

print(response.json())

---

## License

MIT License
