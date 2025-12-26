import requests

BASE_URL = "https://health-insurance-premium-model-api-bvgrg3bmcyhbbpb4.centralindia-01.azurewebsites.net"

def test_root_endpoint():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    print("Root endpoint OK:", data)


def test_predict_endpoint():
    payload = {
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

    response = requests.post(f"{BASE_URL}/predict", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "predicted_premium" in data
    assert isinstance(data["predicted_premium"], (int, float))
    assert data["predicted_premium"] > 0

    print("Prediction successful. Premium:", data["predicted_premium"])
