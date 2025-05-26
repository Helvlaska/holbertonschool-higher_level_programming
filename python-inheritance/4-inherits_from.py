#!/usr/bin/python3
""" Création d'une fonction qui renvoie True
si l'objet est une instance d'une classe qui à hérité
de la classe spécifiée sinon false
"""


def inherits_from(obj, a_class):
    """ Retourne un booléen si l'objet est une instance
    de la classe qui à hérité de la classe spécifiée.

    Args:
        obj (any): L'objet à inspecter.
        a_class : La classe qui à hérité de la classe spécifiée.

    Returns:
        True : L'objet est une instance de la classe qui
        à hérité de la classe spécifiée.
        False : L'objet n'est pas une instance de la classe qui
        à hérité de la classe spécifiée.
    """
    return issubclass(type(obj), a_class)
