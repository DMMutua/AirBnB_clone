#!/usr/bin/python
"""The Class User"""
import models
from models.base_model import BaseModel

class User(BaseModel):
    """Representation of User """

    def __init__(self, *args, **kwargs):
        """Initializing a User Object.
        Variable Arguments
        """
        super().__init__(self, *args, **kwargs)