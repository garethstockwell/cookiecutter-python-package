"""
{{cookiecutter.package_name}}.cli module
"""

import argparse

from {{cookiecutter.package_name}}.my_module import do_something


def main():
    """
    "{{cookiecutter.project_name}}" entry point
    """

    parser = argparse.ArgumentParser("{{cookiecutter.project_name}}")

    parser.add_argument("input", type=int, help="input value")

    args = parser.parse_args()

    print(do_something(args.input))
