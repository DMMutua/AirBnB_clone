#!/usr/bin/python3
"""
This File Hosts the Source Code for the entry Point of the Command Line Interpretor.
This Module Can Create, modify, and delete instances.
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    The Command Processor Class to be Implemented for the CLI Console
    Intended for the AirBnB clone web application.
    """
    prompt = "(hbnb) "

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


#Ensuring the program implemented in this file is executable except when Imported.
if __name__ == '__main__':
    HBNBCommand().cmdloop()
