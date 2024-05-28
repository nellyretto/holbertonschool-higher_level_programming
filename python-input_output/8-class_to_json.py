#!/usr/bin/python3

"""
This module provides a function to convert a Python class
object to a JSON serializable dictionary.
"""

import json


def class_to_json(obj):
    """
    Converts a Python class object to a JSON serializable dictionary.

    Args:
        obj: The object to be converted.

    Returns:
        A dictionary representing the object's attributes.

    """
    return obj.__dict__
