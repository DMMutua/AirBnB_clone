#!/usr/bin/python3
"""
This File Hosts the Source Code for the entry Point of the Command Line Interpretor.
This Module Can Create, modify, and delete instances.
"""


import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """
    The Command Processor Class to be Implemented for the CLI Console
    Intended for the AirBnB clone web application.
    """
    prompt = "(hbnb) "

    list_of_classes = ['BaseModel', 'User', 'State', 'City',
            'Amenity', 'Place', 'Review']

    def do_quit(self, argv):
        """
Quit Command to exit the program
        """
        return True

    def do_EOF(self, argv):
        """
        EOF Signal to Exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        Ensures that the CLI instances of class `HBNBCommand`
        return nothing when an empty line character is given
        as response to prompt.
        Overrides default `emptyline` behavior of repeating last
        nonempty command entered.
        """
        pass

    def do_create(self, line):
        """
        Command to Create New Instance of `BaseModel`.
        Saves it (to JSON FilePath: __file_path) and 
        Prints the id of the instance of BaseModel
        Args:
            Line < **argv >: A line with the Arguments of an Allowed Class Name
        """
        command = self.parseline(line)[0]
        if command is None:
            print('** class name missing **')
        elif command not in self.list_of_classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(command)()
            new_object.save()
            print(new_object.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance of `BaseModel`
        Class based on the class name and ID.
        Args:
            Line < **argv >: A line with the Arguments of an Allowed Class and
                Valid ID.
        """
        arg_vector = shlex.split(line)
        command = arg_vector[0]
        arg = arg_vector[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.list_of_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            instance_data = models.storage.all().get(command + '.' + arg)
            if instance_data is None:
                print('** no instance found **')
            else:
                print(instance_data)

    def do_destroy(self, line):
        """
        Deletes an instance of `BaseModel` Class
        Based on the class Name and Id.
        Args:
            Line < **argv >: A line with the Arguments of an Allowed Class and
                Valid ID.
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.list_of_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        Args:
            line < **argv >: A line with 1 Argument that should 
                            Ideally be a Valid Class Name. 
        """
        command = self.parseline(line)[0]
        objects = models.storage.all()
        if command is None:
            for each_object in objects:
                print(str(each_object))
        elif command in self.list_of_classes:
            keys = objects.keys()
            for any_key in keys:
                if any_key.startswith(command):
                    print(str(objects[any_key]))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updating an Instance Based on the class Name and `id`
        by Adding or Updating an Attribute.
        Args:
            line < **argv >: <class name> <id> <attribute name> "<attribute value>"
        """
        classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

        args = shlex.split(line)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


#Ensuring the program implemented in this file is executable except when Imported.
if __name__ == '__main__':
    HBNBCommand().cmdloop()

