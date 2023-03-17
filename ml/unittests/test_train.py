from unittest import TestCase
from unittest.mock import Mock, patch

import pandas as pd
from sklearn.pipeline import Pipeline
from train.__main__ import train


class TestTrain(TestCase):
    def setUp(self):
        # Create a mock self.config object and set data paths
        self.config = Mock()
        self.config = Mock()
        self.config.data_path = "/path/to/data"
        self.config.train_data_file = "train_data.parquet"
        self.config.model_path = "/path/to/model"
        self.config.model_file = "model.joblib"

    @patch("train.__main__.Config", autospec=True)
    @patch("train.__main__.pd.read_parquet")
    @patch("train.__main__.joblib.dump")
    def test_train(self, mock_dump, mock_read_parquet, mock_config):
        mock_config.return_value = self.config

        # Create mock data
        data = pd.DataFrame(
            {
                "Phrase": ["this is a test", "this is another test"],
                "labels": [0, 1],
            }
        )
        mock_read_parquet.return_value = data

        # Call the train function
        train()

        # Check that pd.read_parquet was called with the correct file path
        pd.read_parquet.assert_called_once_with(
            f"{self.config.data_path}/{self.config.train_data_file}"
        )

        # Check that joblib.dump was called with a Pipeline object
        _, args, _ = mock_dump.mock_calls[0]
        assert isinstance(args[0], Pipeline)
