#!/usr/bin/python
"""The Class Review"""


import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of Review """

    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        """Initializing an Review Object.
        Variable Arguments
        """
        super().__init__(self, *args, **kwargs)
