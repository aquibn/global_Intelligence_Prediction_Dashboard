import pytest
from api.ml_api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    test_data = {
        "environment": "Linux Kernel",
        "attack_vector": "NETWORK",
        "cvss_score": 7.5
    }
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert 'predicted_impact' in response.json
