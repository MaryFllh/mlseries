import re

import pytest
from config import Config
from entities.review import Review
from fastapi.testclient import TestClient
from pydantic import ValidationError
from requests_mock import ANY
from server_main import add_review, app


@pytest.fixture
def config():
    return Config()


@pytest.fixture(scope="module")
def module_client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def client(module_client, requests_mock):
    # ref: https://github.com/encode/starlette/issues/818
    test_app_base_url_prefix_regex = re.compile(
        rf"{re.escape(module_client.base_url)}(/.*)?"
    )
    requests_mock.register_uri(ANY, test_app_base_url_prefix_regex, real_http=True)
    return module_client


def test_add_review(config, requests_mock, client):
    review1 = "hi"
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
    response = client.post("/review_sentiment/", json=Review(text=review2).dict())
    assert response.status_code == 422
    assert response.json()["detail"] == "Review cannot be a number"

    adapter = requests_mock.post(
        f"{config.ml_base_uri}/prediction_job/",
        json={"prediction": "positive", "prediction_score": 80},
    )
    review3 = "very pleasant. highly recommend"
    client.post("/review_sentiment/", json=Review(text=review3).dict())
    assert adapter.last_request.json() == {"text": review3}
    assert adapter.call_count == 1
