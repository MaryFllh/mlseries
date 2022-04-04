import json
from fastapi import FastAPI
import uuid
import requests

from fastapi import status

from config import Config
from utils.logger import logger


app = FastAPI()
config = Config()


@app.get("/")
def read_root():
    return {
        "message": "Sentiment Analysis of Reviews",
    }


@app.get("/review_sentiment/", status_code=status.HTTP_200_OK)
def add_review(review):
    endpoint = f"{config.ml_base_uri}/prediction_job/"

    payload = {
        "text": review,
    }
    resp = requests.post(endpoint, json=payload)
    return resp.json()
