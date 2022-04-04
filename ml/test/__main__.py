import pandas as pd

from json import dump
from joblib import load
from sklearn.metrics import confusion_matrix, accuracy_score

from .config import Config


def test_model():
    config = Config()

    model = load(f"{config.model_path}/{config.model_file}")

    data_test = pd.read_parquet(f"{config.data_path}/{config.test_data_file}")
    X = data_test["Phrase"]
    y = data_test["labels"]
    y_pred = model.predict(X)

    accuracy = accuracy_score(y, y_pred)
    true_negative, false_positive, false_negative, true_positive = confusion_matrix(
        y, y_pred, normalize="true"
    ).ravel()

    with open(f"{config.metric_path}/{config.metric_file}", "w") as metrics:
        dump(
            {
                "results": {
                    "accuracy": accuracy,
                    "true_negative": true_negative,
                    "false_positive": false_positive,
                    "false_negative": false_negative,
                    "true_positive": true_positive,
                }
            },
            metrics,
        )


if __name__ == "__main__":
    test_model()
