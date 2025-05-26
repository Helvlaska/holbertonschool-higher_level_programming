#!/usr/bin/python3
""" Création d'une classe avec une méthode qui
renvoie un message d'erreur
"""


class BaseGeometry():
    """ Création d'une classe vide
    qui renvoie une exception avec un message d'erreur
    """
    def area(self):
        raise Exception("area() is not implemented")
