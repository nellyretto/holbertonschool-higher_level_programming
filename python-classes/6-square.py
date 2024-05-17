#!/usr/bin/python3


class Square:
    """
    A class to represent a square with a specific size and position.

    ...

    Attributes
    ----------
    __size : int
        private instance attribute to store the size of the square
    __position : tuple
        private instance attribute to store the position of the square

    Methods
    -------
    __init__(self, size=0, position=(0, 0)):
        The constructor for Square class. Initializes the size and
        position of the square.
    my_print(self):
        Prints the square using the "#" character.
    area(self):
        Returns the area of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for Square class.

        Parameters:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif not all(
            isinstance(coord, int) and coord >= 0 for coord in position
        ):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """
        Prints the square using the "#" character.

        If the size is 0, prints an empty line.
        """

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        The position getter.

        Returns:
            tuple: The position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        The position setter.

        Parameters:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """

        if not isinstance(value, tuple):
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

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
