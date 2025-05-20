#!/usr/bin/python3
"""
Module contenant la classe Rectangle
pour représenter un Rectangle géométrique.
"""


class Rectangle:
    """
    Creation d'une class Rectangle vide
    """

    def __init__(self, width=0, height=0):
        """
        Creation d'une class Rectangle vide

        Args:
            width: la largeur du rectangle
            height: la hauteur du rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retourne la largeur du rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Retourne la hauteur du rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle avec validation.

        Args:
            value (int): Nouvelle largeur du rectangle.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle avec validation.

        Args:
            value (int): Nouvelle hauteur du rectangle.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value
