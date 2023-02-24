#!/usr/bin/python
"""The Class Amenity"""
import models
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Representation of Amenity """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializing an Amenity Object.
        Variable Arguments
        """
        super().__init__(self, *args, **kwargs)
