#!/usr/bin/python3

"""
This module provides a function to save an object to a JSON file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves the given object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename: The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
