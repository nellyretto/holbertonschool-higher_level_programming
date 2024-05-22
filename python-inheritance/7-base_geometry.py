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
