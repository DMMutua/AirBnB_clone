#!/usr/bin/python
"""The Class Amenity"""


import models
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of Amenity """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializing a City Object.
        Variable Arguments
        """
        super().__init__(self, *args, **kwargs)
