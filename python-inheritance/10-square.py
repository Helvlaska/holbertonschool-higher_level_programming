#!/usr/bin/python3
""" Création d'une classe qui hérite de la classe Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe représentant un carré, héritée de Rectangle.

    Un carré est un rectangle avec des côtés égaux.
    """
    def __init__(self, size):
        """
        Initialise un carré avec une taille donnée.

        Valide que la taille est un entier strictement positif,
        puis initialise le rectangle avec largeur = hauteur = size.

        Args:
            size (int): La taille des côtés du carré.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur ou égal à 0.
        """
        self.integer_validator("size", size)

        super().__init__(size, size)
