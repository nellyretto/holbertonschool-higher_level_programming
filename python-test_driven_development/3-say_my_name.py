#!/usr/bin/python3

"""

Test cases for adding task

"""


def say_my_name(first_name, last_name=""):

    """
    Prints a string with the format "My name is {first_name} {last_name}".

    Parameters:
    first_name (str): The first name to be printed. Must be a string.
    last_name (str, optional): The last name to be printed. Must be a string.
    Defaults to an empty string.

    Raises:
    TypeError: If either first_name or last_name is not a string.

    Returns:
    None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
