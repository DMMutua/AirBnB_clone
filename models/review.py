#!/usr/bin/python
"""The Class Review"""
import models
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Representation of Review """

    def __init__(self, *args, **kwargs):
        """Initializing an Review Object.
        Variable Arguments
        """
        super().__init__(self, *args, **kwargs)