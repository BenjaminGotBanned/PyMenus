import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "PyMenus",
    version = "1.0.5",
    author = "Benjamin O'Brien",
    author_email = "bobrien9274@gmail.com",
    description = "Simple, terminal-based menus for Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ii-Python/PyMenus",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "colorama",
        "termcolor",
        "readchar"
    ],
    python_requires = ">=3.6"
)
