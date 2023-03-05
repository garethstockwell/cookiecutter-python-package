"""
{{cookiecutter.package_name}}.my_python_package module
"""

import os


def do_something(value):
    """
    Do something

    Args:
        value(int): input value

    Returns: str
    """

    path_lib = os.path.dirname(os.path.abspath(__file__))
    path_content = os.path.join(path_lib, "data", "content.txt")
    with open(path_content, "rt", encoding="utf-8") as stream:
        data = stream.read()
        return data.replace("VALUE", str(value))
