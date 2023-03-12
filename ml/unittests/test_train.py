from unittest.mock import MagicMock, patch

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from train.__main__ import train


@patch("train.__main__.pd.read_parquet")
@patch("train.__main__.joblib.dump")
def test_train(mock_dump, mock_read_parquet):
    # Create a mock Config object and set data paths
    config = MagicMock()
    config.data_path = "/path/to/data"
    config.train_data_file = "train_data.parquet"
    config.model_path = "/path/to/model"
    config.model_file = "model.joblib"

    # Create mock data
    data = pd.DataFrame(
        {
            "Phrase": ["this is a test", "this is another test"],
            "labels": [0, 1],
        }
    )
    mock_read_parquet.return_value = data

    # Call the train function
    train(config)

    # Check that pd.read_parquet was called with the correct file path
    pd.read_parquet.assert_called_once_with(
        f"{config.data_path}/{config.train_data_file}"
    )

    # Check that joblib.dump was called with a Pipeline object
    _, args, _ = joblib.dump.mock_calls[0]
    assert isinstance(args[0], Pipeline)
