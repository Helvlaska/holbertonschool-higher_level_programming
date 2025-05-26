#!/usr/bin/python3
""" Création d'une fonction qui renvoie True
si l'objet est une instance de la classe spécifiée
sinon false 
"""


def is_same_class(obj, a_class):
    """ Retourne un booléen si l'objet est une instance
    de la classe spécifiée.

    Args:
        obj (any): L'objet à inspecter.
        a_class : La classe de référence

    Returns:
        True : L'objet est une instance de la classe spécifiée
        False : L'objet n'est pas une instance de la classe spécifiée
    """
    return isinstance(obj, a_class)
