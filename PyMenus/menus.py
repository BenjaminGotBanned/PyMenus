# Modules
from colorama import init
from os import system, name

from readchar import readkey
from termcolor import colored # We need termcolor because colorama doesn't seem to work

from .errors import AlreadyExists, NoOptions, NotSupported

# Platform independent clear screen
def clear():

    if name == "nt":

        system("cls")

    elif name == "posix":

        system("clear")

    else:

        raise NotSupported("The current platform is not supported.")


# Initialize colorama
init()

# Menu class
class Menu():

    """

    Class to create a PyMenu menu.

    """

    def __init__(self):

        self.index = 0

        self.options = {}

    def add_option(self, name, function):

        """

        Adds an option to an existing menu.

        """

        if name in self.options:

            raise AlreadyExists("An option with that name already exists.")
        
        self.options[name] = function

    def show(self):

        """

        Begins displaying the menu and all of it's options.

        """

        if len(self.options) == 0:

            raise NoOptions("No options are in the menu!")

        _options = []

        for option in self.options:

            _options.append(option)

        task = None

        while True:

            clear()

            for option in self.options:

                try:

                    if option == _options[self.index]:

                        print(colored(_options[self.index], "grey", "on_white"))

                    else:

                        print(colored(option, "white", "on_grey"))

                except:

                    self.index = 0

                    print(colored(_options[self.index], "grey", "on_white"))

            char = readkey()

            if char == "\x1b\x5b\x41":

                self.index -= 1

            elif char == "\x1b\x5b\x42":

                self.index += 1

            elif char == "\x0d":

                task = self.options[_options[self.index]]

                break

        clear()

        task()