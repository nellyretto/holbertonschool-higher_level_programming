
"""
This modules has the ABC class that serves for this code
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that returns the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Class representing a dog, inheriting from Animal.
    """

    def sound(self):
        """
        Returns the sound of a dog, which is "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    Class representing a cat, inheriting from Animal.
    """

    def sound(self):
        """
        Returns the sound of a cat, which is "Meow".
        """
        return "Meow"
