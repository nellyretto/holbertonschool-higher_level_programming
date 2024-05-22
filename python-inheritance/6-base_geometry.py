#!/usr/bin/python3


"""
This area has class BaseGeometry
"""


class BaseGeometry:

    """
    This is the base class for geometry objects.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        This method raises an exception since it is not
        implemented in the base class.
        Subclasses should override this method to provide
        their own implementation.
        """
        raise Exception("area() is not implemented")
