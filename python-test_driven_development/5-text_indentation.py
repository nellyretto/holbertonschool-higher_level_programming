#!/usr/bin/python3

"""

Test cases for adding task

"""


def text_indentation(text):

    """
    Prints a string with two newlines after each period (.),
    question mark (?), and colon (:).

    Parameters:
    text (str): The text to be printed. Must be a string.

    Raises:
    TypeError: If text is not a string.

    Returns:
    None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    print(text.replace(". ", ".\n\n").replace("? ", "?\n\n"
                                              ).replace(": ", ":\n\n"))
