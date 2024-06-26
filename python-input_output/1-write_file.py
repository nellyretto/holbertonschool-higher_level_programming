#!/usr/bin/python3


"""
This module contains a function to write text to a file.

Functions:
    write_file(filename, text): Writes the given text to the specified file.

"""


def write_file(filename="", text=""):
    """
    Writes the given text to the specified file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
