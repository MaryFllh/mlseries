import pytest
from entities.review import Review
from fastapi.testclient import TestClient
from ml_main import app


@pytest.fixture(scope="session")
def module_client():
    with TestClient(app) as c:
        yield c


def test_predict_service(module_client):
    review = "This is a must see."
    response = module_client.post("/prediction_job/", json=Review(text=review).dict())
    assert response.status_code == 201
    assert "prediction" in response.json()
    assert "prediction_score" in response.json()
