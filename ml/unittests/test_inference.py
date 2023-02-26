import pytest

from services.predict import PredictService


predict_service = PredictService()

def test_predict_service():
    review1 = "It was great"
    review2 = "terrible. impossible to bear!"

    assert(predict_service.predict(review1)["prediction"] == "positive")
    assert(predict_service.predict(review2)["prediction"] == "negative")
