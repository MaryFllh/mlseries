import re

import requests
from config import Config
from entities.review import Review
from fastapi import FastAPI, HTTPException, status

app = FastAPI()
config = Config()


@app.post("/review_sentiment/", status_code=status.HTTP_200_OK)
def add_review(review: Review):
    """
    This endpoint receives reviews, creates an appropriate
    payload and makes a post request to ml's endpoint for a
    prediction on the input

    Args:
        review(Review): the input should conform to the Review model

    Returns:
        response(dict): response from ml's endpoint which includes
                        prediction details

    Raises:
        HTTPException: if the input is a sequence of numbers
    """
    endpoint = f"{config.ml_base_uri}/prediction_job/"
    if re.findall(r"^\-?[1-9][0-9]*$", review.text):
        raise HTTPException(status_code=422, detail="Review cannot be a number")

    payload = {
        "text": review.text,
    }
    resp = requests.post(endpoint, json=payload)
    return resp.json()
