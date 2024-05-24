from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class representing a shape."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize a Circle object with a given radius."""
        self.radius = abs(radius)

    def area(self):
        """Calculate the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return pi * self.radius * 2


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle object with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return (self.width + self.height) * 2


def shape_info(shape):
    """Print the area and perimeter of a given shape."""
    print('Area:', shape.area())
    print('Perimeter:', shape.perimeter())
