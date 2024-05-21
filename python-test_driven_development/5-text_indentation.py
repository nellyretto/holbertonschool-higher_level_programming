#!/usr/bin/python3


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

    print(text.replace(". ", ".\n\n").replace("? ", "?\n\n"
                                              ).replace(": ", ":\n\n"))
