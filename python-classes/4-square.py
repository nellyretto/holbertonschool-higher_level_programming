#!/usr/bin/python3


"""
This module defines a class Square.

This module demonstrates encapsulation, data validation,
 and the use of properties in Python.
"""


class Square:
    """
    A class to represent a square.

    ...

    Attributes
    ----------
    __size : int
        private instance attribute to store the size of the square

    Methods
    -------
    __init__(self, size=0):
        The constructor for Square class. Initializes the size of the square.
    area(self):
        Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        The constructor for Square class.

        Parameters:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        The size getter.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        The size setter.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
