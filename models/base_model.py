#!/usr/bin/python3
"Definations and implementation of the BaseModel class"

from uuid import uuid4
from datetime import datetime

timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    The BaseModel Class Representation for the AIRBNB_Clone Project.
        Methods:
            `__init__`, `save`, `__str__`, `to_dict`
    """

    def __init__(self, *args, **kwargs):
        """Initialization method of objects of the BaseModel Class.
            args:
                *args: any attributes of the BaseModel Class, 
                            allowing dynamic attribute setting
                **kwargs: key/value pairs for attribute setting on instantiation
                            of class objects
        """

        if kwargs:

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], timeformat)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], timeformat)
            else:
                self.created_at = datetime.utcnow()
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at


    def save(self):
        """Updates the attribute `updated_at` of an object to the current date-time"""

        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returning the attribute dictionary of key/values  of a particular
        instance of the BaseClass.
            the Attributes `created_at` and `updated_at` are returned as type `str`
            and in ISO format.
        """

        obj_dict = self.__dict__.copy()
        if "created_at" in obj_dict:
            obj_dict["created_at"] = obj_dict["created_at"].strftime(timeformat)
        
        if "updated_at" in obj_dict:
            obj_dict["updated_at"] = obj_dict["updated_at"].strftime(timeformat)

        obj.dict["__class__"] = self.__class__.__name__

        return obj_dict

    def __str__(self):
        """Returning the string representation of the objects of BaseClass.
            Returns in the format `[<class name>] (<self.id>) <self.__dict__>`.
        """

        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

