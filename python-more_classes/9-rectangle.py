#!/usr/bin/python3
"""
Module contenant la classe Rectangle
pour représenter un Rectangle géométrique.
"""


class Rectangle:
    """Classe représentant un rectangle avec
    largeur et hauteur, incluant validations.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Creation d'une class Rectangle vide

        Args:
            width: la largeur du rectangle
            height: la hauteur du rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        # crée une liste contenant une ligne de `sym` par ligne du rectangle
        lines = []
        for _ in range(self.height):
            lines.append(str(self.print_symbol) * self.width)

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
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Retourne le plus grand rectangle (ou rect_1 s'ils sont égaux)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Crée une nouvelle instance de Rectangle
        où la largeur et la hauteur sont égales à size.

        Args:
            size (int): La taille des côtés du carré (par défaut 0).

        Returns:
            Rectangle: Une nouvelle instance de Rectangle avec:
            largeur == hauteur == size.
        """
        # cls = class
        # cls(width, height)
        # width = height = size
        # donc ont renvoie que la nouvelle instance prends size en paramètre
        return cls(size, size)
