#!/usr/bin/python3
"""
The Implementation of a FileStorage Class.
In AirBNB_Clone; The FileStorage Class:
    serializes BaseClass Instances to a JSON File using the `self.__dict__` feature.
    Deserializes a JSON File's Objects to BaseClass Instances using the `self.__dict__` feature.
"""

import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path

classes = {
"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User
}
class FileStorage:
    """Implements Serializing Instances to JSON Files and Deserialization Back to Instances"""

    # string - path to the JSON file being Serialized to and Deserialized from
    __file_path = "file.json"
    # dictionary - empty at declaration: will store all Objects by <class name>.id
    __objects = {}

    def all(self):
        """returning the dictionary `__objects`.
        This Dictionary Stores all class Objects by `<class name>.id`
        """

        return self.__objects

    def new(self, obj):
        """sets in dictionary __objects the object with key <obj class name>.id
        Args:
            obj (inst): The Object being added in the `__objects` class attribute
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serialization of __objects to the JSON file (filepath: __file_path)
        Conversion of contents of `__objects` into JSON Strings and
        Loading to JSON File on `__file_path`
        """
        json_dictionary = {}
        for key, value in self.__objects.items():
            json_dictionary[key] = value.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as file_context:
            file_context.write(json.dumps(json_dictionary))

    def reload(self):
        """Deserialization of the JSON file (filepath: __file_path) to __objects dictionary
        If the file on `__file_path` class attribute exists, each object
        on the file will be deserialized and appended to the `__objects`
        class attribute like an instance with the object data.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file_context:
                json_dictionary = json.loads(file_context.read())

                for key, value in json_dictionary.items():
                    self.__objects[key] = eval(v['__class__'])(**value)

    def delete(self, obj=None):
        """Deleting obj from __objects if it exists there"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Calling the reload() method for deserialization of JSON file to Objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returning the object based on the class name and its ID,
        or NONE if it is not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        Counting the Number of Objects in Storage
        """
        all_classes = classes.values()

        if not cls:
            count = 0
            for a_clas in all_classes:
                count += len(models.storage.all(a_clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
