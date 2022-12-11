#!/usr/bin/python
"""The Class Place"""
import models
from models.base_model import BaseModel

class Place(BaseModel):
    """Representation of Place """

    def __init__(self, *args, **kwargs):
        """Initializing a Place Object.
        Variable Arguments
        """
        super().__init__(self, *args, **kwargs)