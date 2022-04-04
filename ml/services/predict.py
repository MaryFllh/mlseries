from joblib import load
import numpy as np


from utils.config import Config
from utils.logger import logger


class PredictService:
    def __init__(self):
        self.config = Config()
        self.model = load(f"{self.config.model_path}/{self.config.model_file}")

    def add_prediction_job(self, review):
        response = dict()
        X = review
        response["prediction"] = str(self.model.predict(np.array([X]))[0])
        response["prediction_score"] = str(
            self.model.predict_proba(np.array([X]))[0][1]
        )

        logger.info("Completed prediction on review: %s", response)
        return response
