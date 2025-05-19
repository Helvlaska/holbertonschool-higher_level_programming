#!/usr/bin/python3
"""
Module contenant la classe Square
pour représenter un carré géométrique.
"""


class Square:
    """Classe représentant un carré.

    Attributes:
        __size (int): La taille du carré.
    """

    def __init__(self, size=0):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du carré.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retourne la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré avec validation.

        Args:
            value (int): Nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime le carré avec le caractère #.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                for _ in range(self.__size):
                    print("#", end="")
                print()