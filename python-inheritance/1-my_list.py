#!/usr/bin/python3


"""
This module defines a custom list class called MyList that
inherits from the built-in list class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))
