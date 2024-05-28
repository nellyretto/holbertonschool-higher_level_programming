#!/usr/bin/python3


"""
This module contains a function to read and print the contents of a file.
"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
