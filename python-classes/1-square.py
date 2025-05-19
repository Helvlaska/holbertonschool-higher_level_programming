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

    def __init__(self, size):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du carré.
        """
        self.__size = size
