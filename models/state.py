#!/usr/bin/python
"""The Class State"""
import models
from models.base_model import BaseModel

class Place(BaseModel):
    """Representation of State """

    def __init__(self, *args, **kwargs):
        """Initializing a State Object.
        Variable Arguments
        """
        super().__init__(self, *args, **kwargs)