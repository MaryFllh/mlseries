from unittest.mock import MagicMock, patch

import pandas as pd
from prepare_data.__main__ import split_train_test_data


@patch("prepare_data.__main__.pd.read_csv")
@patch("prepare_data.__main__.train_test_split")
@patch("prepare_data.__main__.pd.DataFrame.to_parquet")
def test_split_train_test_data(mock_to_parquet, mock_train_test_split, mock_read_csv):
    config = MagicMock()
    config.data_path = "/data"
    config.data_file = "data_file.csv"
    config.train_data_file = "train.csv"
    config.test_data_file = "test.csv"

    mock_read_csv.return_value = pd.DataFrame(
        {
            "Sentiment": [0, 1, 4, 2, 4, 3, 0, 4, 2, 0, 1],
            "Phrase": [
                "foo",
                "char",
                "kar",
                "bar",
                "lar",
                "baz",
                "qux",
                "quux",
                "corge",
                "vid",
                "chill",
            ],
        }
    )

    expected_data = pd.DataFrame(
        {
            "Sentiment": [0, 4, 4, 0, 4, 0],
            "Phrase": ["foo", "kar", "lar", "qux", "quux", "vid"],
            "labels": [0, 1, 1, 0, 1, 0],
        }
    )

    mock_train_test_split.return_value = (
        pd.DataFrame(
            {
                "Sentiment": [0, 0, 4, 4, 0],
                "Phrase": ["foo", "kar", "lar", "qux", "vid"],
                "labels": [0, 0, 1, 1, 0],
            }
        ),
        pd.DataFrame({"Sentiment": [4], "Phrase": ["quux"], "labels": [1]}),
    )

    split_train_test_data(config)
    pd.testing.assert_frame_equal(
        mock_train_test_split.call_args[0][0].reset_index(drop=True),
        expected_data.reset_index(drop=True),
    )
    mock_read_csv.assert_called_once_with(
        f"{config.data_path}/{config.data_file}", sep="\t"
    )
    assert mock_to_parquet.call_count == 2
