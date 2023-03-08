import pandas as pd
from model_params import TrainTestSplit
from sklearn.model_selection import train_test_split

from .config import Config


def split_train_test_data():
    config = Config()

    data = pd.read_csv(f"{config.data_path}/{config.data_file}", sep="\t")
    data = data[(data["Sentiment"] == 0) | (data["Sentiment"] == 4)]
    data["labels"] = data.apply(lambda x: 0 if x["Sentiment"] == 0 else 1, axis=1)

    data_train, data_test = train_test_split(data, test_size=TrainTestSplit.TEST_SIZE)

    data_train.to_parquet(f"{config.data_path}/{config.train_data_file}")
    data_test.to_parquet(f"{config.data_path}/{config.test_data_file}")


if __name__ == "__main__":
    split_train_test_data()
