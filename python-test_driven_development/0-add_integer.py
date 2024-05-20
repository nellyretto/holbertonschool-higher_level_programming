#!/usr/bin/python3

"""
Test cases for adding task
"""


def add_integer(a, b=98):

    """
    Adds two integers or floats.

    This function adds two numbers, which should be integers or floats.
    If either of a or b is a float,
    it will be cast to an integer before addition.

    Parameters:
    a (int, float): The first number to add. Must be an integer or float.
    b (int, float, optional): The second number to add.
    Must be an integer or float. Defaults to 98.

    Returns:
    int: The sum of a and b, after casting them to integers.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    return a + b
