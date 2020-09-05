# PyMenus

### Basic terminal menus made in Python

[![PyPI version](https://badge.fury.io/py/PyMenus.svg)](https://badge.fury.io/py/PyMenus)
[![Lol get rekt](https://img.shields.io/badge/Your%20mom-is%20gay-green.svg)](https://shields.io/)
---

#### Setup

Make sure you have the latest version of PyMenus: `pip install pymenus`

To create a menu, use the `Menu` class; an example:

```
from PyMenus import Menu

m = Menu()
```

You can then add options to it:

```
def func():

    print("Hello, world.")

m.add_option("Option 1", func)
```

To display the menu, use the `show()` function.

Overall code:

```
from PyMenus import Menu

m = Menu()

def func():

  print("Hello, world.")

m.add_option("Option 1", func)

m.show()
```

