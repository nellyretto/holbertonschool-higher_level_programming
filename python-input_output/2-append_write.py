#!/usr/bin/python3


"""
This module contains a function to append text to a file.

The function `append_write` takes in a filename and text as parameters
and appends the text to the file.
It returns the number of characters written to the file.

Example usage:
    append_write("file.txt", "Hello, World!")

This will append the text "Hello, World!" to the file "file.txt"
and return the number of characters written.

Note: If the file does not exist, it will be created.
"""


def append_write(filename="", text=""):
    """
    Append text to a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
