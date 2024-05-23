#!/usr/bin/python3

"""
Importing for efficient code compacting
"""

Rectangle = __import__('8-rectangle').Rectangle

"""
class that inherits from rectangle class
"""


class Square(Rectangle):

    """
    Represents a square shape.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
