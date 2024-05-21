#!/usr/bin/python3

""""
Test cases for adding task

"""


def print_square(size):

    """
    Prints a square of a given size.

    Parameters:
    size (int): The size of the square to be printed. Must be an integer.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.

    Returns:
    None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for item in range(size):
        print("#" * size)
