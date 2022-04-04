from os import getenv
from sys import exit

from utils.logger import logger


class Config:
    def __init__(self):
        if getenv("DATA_PATH") is None:
            self.exit_program("DATA_PATH")
        else:
            self.data_path = getenv("DATA_PATH")

        if getenv("DATA_FILE") is None:
            self.exit_program("DATA_FILE")
        else:
            self.data_file = getenv("DATA_FILE")

        if getenv("TRAIN_DATA_FILE") is None:
            self.exit_program("TRAIN_DATA_FILE")
        else:
            self.train_data_file = getenv("TRAIN_DATA_FILE")

        if getenv("TEST_DATA_FILE") is None:
            self.exit_program("TEST_DATA_FILE")
        else:
            self.test_data_file = getenv("TEST_DATA_FILE")

    def exit_program(self, env_var):
        error_message = (
            f"prepare_data: {env_var} is missing from the set environment variables."
        )
        logger.error(error_message)
        exit(error_message)
