import pytest
from config import Config
from entities.review import Review
from fastapi import HTTPException
from fastapi.testclient import TestClient
from main import add_review, app
from pydantic import ValidationError
from requests_mock import Adapter

client = TestClient(app)
config = Config()


def test_add_review(requests_mock: Adapter):

    review1 = 123
    with pytest.raises(ValidationError) as exc_info:
        add_review(Review(text=review1))
    assert exc_info.value.errors() == [
        {
            "loc": ("text",),
            "msg": "min_length:4",
            "type": "value_error.any_str.min_length",
            "ctx": {"limit_value": 4},
        }
    ]

    review2 = 123458303
    with pytest.raises(HTTPException) as exc_info:
        add_review(Review(text=review2))
    assert exc_info.value.status_code == 422
    assert exc_info.value.detail == "Review cannot be a number"

    adapter = requests_mock.post(
        f"{config.ml_base_uri}/prediction_job/",
        json={"prediction": "positive", "prediction_score": 80},
    )
    review3 = "very pleasant. highly recommend"
    add_review(Review(text=review3))
    assert adapter.last_request.json() == {"text": review3}
    assert adapter.call_count == 1
