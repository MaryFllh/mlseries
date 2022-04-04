from os import getenv
from sys import exit


class Config:
    def __init__(self):
        if getenv("ML_BASE_URI") is None:
            self.exit_program("ML_BASE_URI")
        else:
            self.ml_base_uri = getenv("ML_BASE_URI")

    def exit_program(self, env_var):
        error_message = (
            f"server: {env_var} is missing from the set environment variables."
        )
        exit(f"{error_message}")
