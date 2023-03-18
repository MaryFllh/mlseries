from unittest import TestCase

from entities.review import Review
from services.predict import PredictService


class TestPredictService(TestCase):
    def setUp(self):
        self.predict_service = PredictService()

    def test_predict_service(self):
        review = Review(text="terrible. impossible to bear!")

        response = self.predict_service.predict(review)

        self.assertIsInstance(response, dict)
        self.assertIn("prediction", response)
        self.assertIn("prediction_score", response)
        self.assertEqual(response["prediction"], "negative")
        self.assertGreaterEqual(response["prediction_score"], 0)
        self.assertLessEqual(response["prediction_score"], 100)
