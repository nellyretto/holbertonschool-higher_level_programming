#!/usr/bin/python3


"""
This module contains the Student class.
"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attributes
            to include in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: self.__dict__[attr] for attr
                    in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        """
        Updates the attributes of the Student
        instance based on a JSON dictionary.

        Args:
            json (dict): A dictionary containing
            the attribute-value pairs to update.
        """
        for key, value in json.items():
            setattr(self, key, value)
