#!/usr/bin/python3

"""
This module contains the definition of the BaseGeometry class.
"""


class BaseGeometry:
    """
    This is the base class for geometry objects.
    """

    def integer_validator(self, name, value):
        """
        Validates if a given value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """
        Calculate the area of the geometry.

        This method raises an exception since it is not
        implemented in the base class.
        Subclasses should override this method to provide
        their own implementation.
        """
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Represents a square shape.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        super().__init__(size, size)
