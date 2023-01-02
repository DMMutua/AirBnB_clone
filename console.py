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
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
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
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.list_of_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            instance_key = command + '.' + arg
            instance_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

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

#Ensuring the program implemented in this file is executable except when Imported.
if __name__ == '__main__':
    HBNBCommand().cmdloop()

