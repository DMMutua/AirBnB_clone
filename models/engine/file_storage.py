#!/usr/bin/python3
"""
The Implementation of a FileStorage Class.
In AirBNB_Clone; The FileStorage Class:
    serializes BaseClass Instances to a JSON File using the `self.__dict__` feature.
    Deserializes a JSON File's Objects to BaseClass Instances using the `self.__dict__` feature.
"""

import json


class FileStorage:
    """Implements Serializing Instances to JSON Files and Deserialization Back to Instances"""

    # string - path to the JSON file being Serialized to and Deserialized from
    __file_path = "file.json"
    # dictionary - empty at declaration: will store all Objects by <class name>.id
    __objects = {}

    def all(self):
        """returning the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in dictionary __objects the object with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serialization of __objects to the JSON file (filepath: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file_context:
            json.dump(json_objects, file_context)

    def reload(self):
        """Deserialization of the JSON file (filepath: __file_path) to __objects dictionary"""
        try:
            with open(self.__file_path, 'r') as file_context:
                objdict = json.load(file_context)
            for o in objdict.values():
                cls_name = o["__class__"]
                del o["__class__"]
                self.new(eval(cls_name)(**o))
        except():
            pass
