import numpy as np
from entities.review import Review
from joblib import load
from utils.config import Config
from utils.logger import logger


class PredictService:
    """
    A class serving a trained model for prediction requests

    Methods:
        infer(review: Review) runs inference on a review and sends
                    back the sentiment and a prediciton score from 1-100
    """

    def __init__(self):
        """
        Loads the env vars and the trained model
        """
        self.config = Config()
        self.model = load(f"{self.config.model_path}/{self.config.model_file}")

    def predict(self, review: Review):
        """
        Runs inference on a review and sends back the sentiment and a prediciton
        score from 1-100

        Args:
            review(Review): a Review entity which contains text for prediction

        Returns:
            response(dict): a dictionary with the predicted positive or negative
                            sentiment and an associated prediciton score
        """
        response = dict()
        review = review.text.lower()
        response["prediction"] = (
            "positive" if self.model.predict([review])[0] else "negative"
        )
        positive_prediction_score = np.round(
            self.model.predict_proba([review])[0][1] * 100, 3
        )
        response["prediction_score"] = (
            positive_prediction_score
            if response["prediction"] == "positive"
            else 100 - positive_prediction_score
        )

        logger.info("Completed prediction on review: %s", response)
        return response
