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
        if getenv("MODEL_PATH") is None:
            self.exit_program("MODEL_PATH")
        else:
            self.model_path = getenv("MODEL_PATH")

        if getenv("MODEL_FILE") is None:
            self.exit_program("MODEL_FILE")
        else:
            self.model_file = getenv("MODEL_FILE")

    def exit_program(self, env_var):
        """
        if an environment variable is missing, it exists with an error message

        Args:
            env_var (str): the name of the missing environment variable
        """
        error_message = (
            f"ML: {env_var} is missing from the set of environment variables."
        )
        exit(f"{error_message}")
