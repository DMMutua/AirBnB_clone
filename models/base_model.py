#!/usr/bin/python3
"Definations and implementation of the basemodel class"

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The BaseModel Class Representation for the AIRBNB_Clone Project.
    """
timeformat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialization method of objects of the BaseModel Class.
            args:
                *args: any attributes of the BaseModel Class, 
                            allowing dynamic attribute setting
                **kwargs: key/value pairs for attribute setting on instantiation
                            of class objects
        """

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        while len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeformat)
                else:
                    self.__dict__[key] = value


    def save(self):
        """Updates the attribute `updated_at` of an object to the current time"""

        self.updated_at = datetime.today()

    def to_dict(self):
        """Returning the dictionary of the BaseModel Instance.
        the key/value pair of __class__ is included and reps
        the class of the object in question"""

        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict
