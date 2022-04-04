from os import getenv
from sys import exit

from utils.logger import logger


class Config:
    def __init__(self):
        if getenv("DATA_PATH") is None:
            self.exit_program("DATA_PATH")
        else:
            self.data_path = getenv("DATA_PATH")

        if getenv("TRAIN_DATA_FILE") is None:
            self.exit_program("TRAIN_DATA_FILE")
        else:
            self.train_data_file = getenv("TRAIN_DATA_FILE")

        if getenv("MODEL_PATH") is None:
            self.exit_program("MODEL_PATH")
        else:
            self.model_path = getenv("MODEL_PATH")

        if getenv("MODEL_FILE") is None:
            self.exit_program("MODEL_FILE")
        else:
            self.model_file = getenv("MODEL_FILE")

    def exit_program(self, env_var):
        error_message = (
            f"train: {env_var} is missing from the set environment variables."
        )
        logger.error(error_message)
        exit(error_message)
