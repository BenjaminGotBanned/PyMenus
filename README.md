# PyMenus

### Basic terminal menus made in Python
---

#### Setup

Make sure you have the latest version of PyMenus: `pip install PyMenus`

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

