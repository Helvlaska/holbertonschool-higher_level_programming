#!/usr/bin/python3
"""
Module contenant la classe Rectangle
pour représenter un Rectangle géométrique.
"""


class Rectangle:
    """Classe représentant un rectangle avec
    largeur et hauteur, incluant validations.

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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Retourne l'air du rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        Retourne le périmètre du rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):
        """Imprime le rectangle avec le caractère #
        """
        if self.width == 0 or self.height == 0:
            return ""
        # crée une liste contenant une ligne de `#` par ligne du rectangle
        lines = []
        for _ in range(self.height):
            lines.append("#" * self.width)

        # rejoint les lignes avec un saut de ligne
        # ["###", "###"] → "###\n###"
        return "\n".join(lines)

    def __repr__(self):
        """Imprime les paramètres de rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Imprime un message quand un rectangle est supprimé
        """
        print("Bye rectangle...")
