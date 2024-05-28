#!/usr/bin/python3

"""
This module provides a function to load data from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return the deserialized object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The deserialized object.

    Raises:
        FileNotFoundError: If the file does not exist.
        JSONDecodeError: If the file is not valid JSON.

    """
    with open(filename, 'r') as file:
        return json.load(file)
