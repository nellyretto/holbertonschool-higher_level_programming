#!/usr/bin/python3

"""

Test cases for adding task

"""


def add_integer(a, b=98):

    """
    Adds two integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
