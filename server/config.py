from os import getenv
from sys import exit


class Config:
    """
    Checks for all necessary configurations and exits the app
    if they are not set correctly.

    Methods:
        exit_program(env_var): if an environment variable is
                missing, it exists with an error message
    """

    def __init__(self):
        if getenv("ML_BASE_URI") is None:
            self.exit_program("ML_BASE_URI")
        else:
            self.ml_base_uri = getenv("ML_BASE_URI")

    def exit_program(self, env_var):
        error_message = (
            f"SERVER: {env_var} is missing from the set of environment variables."
        )
        exit(f"{error_message}")
