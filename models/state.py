#!/usr/bin/python
"""The Class State"""


import models
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of State """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializing a State Object.
        Variable Arguments
        """
        super().__init__(self, *args, **kwargs)
