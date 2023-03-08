from pydantic import BaseModel


class Review(BaseModel):
    text: str

    class Config:
        """
        Controls the behaviour of the Review class
        """

        min_anystr_length = 4
        error_msg_templates = {
            "value_error.any_str.min_length": "min_length:{limit_value}",
        }
