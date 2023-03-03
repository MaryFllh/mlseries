import os

from fastapi import HTTPException
from fastapi.testclient import TestClient

from main import app



client = TestClient(app)

def test_add_review():
    review1 = 123
    response = client.post("/review_sentiment/", json={"review": review1})
    assert response.status_code == 422
    
    # review2 = "very pleasant. highly recommend"
    # response = client.post("/review_sentiment/", json={"review": str(review2)})
    # assert response.status_code == 201