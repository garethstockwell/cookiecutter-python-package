"""
tests.test_my_module
"""

from unittest import TestCase

from ddt import ddt, data

from {{cookiecutter.package_name}}.my_module import do_something


@ddt
class TestMyModule(TestCase):
    """
    Unit tests for {{cookiecutter.package_name}}.my_module module
    """

    @data(
        *[
            (0, "BEFORE\n0\nAFTER\n"),
            (1, "BEFORE\n1\nAFTER\n"),
            (42, "BEFORE\n42\nAFTER\n"),
        ]
    )
    def test_do_something(self, test_data):
        """
        Test correct output of {{cookiecutter.package_name}}.my_module.do_something
        """
        (arg, expected) = test_data
        result = do_something(arg)
        self.assertEqual(result, expected)
