#!/usr/bin/python3


"""
This area contains the functions is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or
    is derived from, a specified class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to check against.

    Returns:
        object: The object itself if it is an instance of, or
        is derived from, the specified class.
        False: If the object is not an instance of, or is not
        derived from, the specified class.
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return obj
