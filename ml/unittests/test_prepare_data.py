import pandas as pd

from prepare_data.config import Config

def test_data_preparation():
    config = Config()
    train_data = pd.read_parquet(f"{config.data_path}/{config.train_data_file}")
    test_data = pd.read_parquet(f"{config.data_path}/{config.test_data_file}")
    
    assert(set(train_data["labels"].unique()) == set([0, 1]))
    assert(set(test_data["labels"].unique()) == set([0, 1]))
