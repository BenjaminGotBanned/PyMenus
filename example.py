from time import sleep
from PyMenus import Menu

m = Menu()

def option1():

    print("You pressed option 1.")

    sleep(999)

def option2():

    print("You pressed option 2.")

    sleep(999)
    
def option3():

    print("You pressed option 3.")

    sleep(999)

m.add_option("Option 1", option1)

m.add_option("Option 2", option2)

m.add_option("Option 3", option3)

m.show()
