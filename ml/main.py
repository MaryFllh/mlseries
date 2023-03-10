from entities.review import Review
from fastapi import FastAPI, status
from services.predict import PredictService

app = FastAPI()

predict_service = PredictService()


@app.post("/prediction_job/", status_code=status.HTTP_201_CREATED)
def add_prediction_job(review: Review):
    """
    This endpoint receives reviews, sends it to the
    prediction service for prediction and returns the response

    Args:
        review(Review): the input should conform to the Review model

    Returns:
        response(dict): response from predict_service which includes
                        prediction details
    """
    response = predict_service.predict(review.text)
    return response
