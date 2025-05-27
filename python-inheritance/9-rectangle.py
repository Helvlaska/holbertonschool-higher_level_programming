#!/usr/bin/python3
""" Création d'une classe qui hérite de la classe BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Représente un rectangle, sous-classe de BaseGeometry.

    Attributs privés :
        - __width (int) : largeur du rectangle (doit être un entier > 0)
        - __height (int) : hauteur du rectangle (doit être un entier > 0)

    Méthodes :
        - __init__(self, width, height) : construit un rectangle validé
    """
    def __init__(self, width, height):
        """
        Initialise un nouveau rectangle avec une largeur et une hauteur,
        toutes deux validées par integer_validator (hérité de BaseGeometry).

        Args:
            width (int) : largeur du rectangle
            height (int) : hauteur du rectangle

        Raises:
            TypeError : si width ou height ne sont pas des entiers
            ValueError : si width ou height <= 0
        """
        super().__init__()

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            int: Le produit de la largeur et de la hauteur.
        """
        return (self.__width * self.__height)
    
    def __str__(self):
        """
        Retourne une représentation textuelle du rectangle.

        Format retourné :
            [Rectangle] <largeur>/<hauteur>

        Returns:
            str: Représentation formatée du rectangle.
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
    