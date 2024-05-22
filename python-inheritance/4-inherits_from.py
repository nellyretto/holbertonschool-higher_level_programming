#!/usr/bin/pyhton3


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
    return type(obj) != a_class and issubclass(type(obj), a_class)
