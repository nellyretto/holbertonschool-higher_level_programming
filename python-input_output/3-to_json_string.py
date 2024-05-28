#!/usr/bin/python3

"""
This module provides a function to convert a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        A JSON string representation of the input object.
    """
    return json.dumps(my_obj)
