import joblib
import pandas as pd
from model_params import LogisticRegressionConfig
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from .config import Config


def train():
    """
    Loads the training data, creates, fits a pipeline on
    the data and saves the model
    """
    config = Config()

    lr_params = {
        "n_jobs": LogisticRegressionConfig.n_jobs,
        "C": LogisticRegressionConfig.C,
        "max_iter": LogisticRegressionConfig.max_iter,
    }
    train_dataframe = pd.read_parquet(f"{config.data_path}/{config.train_data_file}")

    X = train_dataframe["Phrase"]
    y = train_dataframe["labels"]

    clf = Pipeline(
        [
            ("vect", CountVectorizer()),
            ("tfidf", TfidfTransformer()),
            ("clf", LogisticRegression(**lr_params)),
        ]
    )
    clf.fit(X, y)
    joblib.dump(clf, f"{config.model_path}/{config.model_file}")


if __name__ == "__main__":
    train()
