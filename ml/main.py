from fastapi import FastAPI, Request, status
from services.predict import PredictService
from utils.logger import logger
from pydantic import BaseModel


class Review(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "review about the movie",
            }
        }


app = FastAPI()

predict_service = PredictService()


@app.get("/")
def read_root():
    return {"ML inference root!"}


@app.post("/prediction_job/", status_code=status.HTTP_201_CREATED)
def add_prediction_job(request: Request, review: Review):
    try:
        resp = predict_service.add_prediction_job(review.text)
        return resp
    except Exception as e:
        logger.info(
            "There was an exception when making a predition for review %s: %s",
            review.text,
            e,
        )
