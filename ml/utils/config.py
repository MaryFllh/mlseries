from os import getenv
from sys import exit


class Config:
    def __init__(self):
        if getenv("MODEL_PATH") is None:
            self.exit_program("MODEL_PATH")
        else:
            self.model_path = getenv("MODEL_PATH")

        if getenv("MODEL_FILE") is None:
            self.exit_program("MODEL_FILE")
        else:
            self.model_file = getenv("MODEL_FILE")

        if getenv("AWS_SECRET_ACCESS_KEY") is None:
            self.exit_program("AWS_SECRET_ACCESS_KEY")
        else:
            self.aws_access_key = getenv("AWS_SECRET_ACCESS_KEY")

        if getenv("AWS_SECRET_ACCESS_KEY_ID") is None:
            self.exit_program("AWS_SECRET_ACCESS_KEY_ID")
        else:
            self.aws_secret_key = getenv("AWS_SECRET_ACCESS_KEY_ID")

    def exit_program(self, env_var):
        error_message = (
            f"utils: {env_var} is missing from the set environment variables."
        )
        exit(f"{error_message}")
