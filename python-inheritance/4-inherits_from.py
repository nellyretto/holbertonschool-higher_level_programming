#!/usr/bin/python3


"""
this contains the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Checks if an object inherits from a given class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object inherits from the class, False otherwise.
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
