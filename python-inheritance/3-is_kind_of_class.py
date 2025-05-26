#!/usr/bin/python3
""" Création d'une fonction qui renvoie True
si l'objet est une instance ou si l'objet est une instance
d'une classe qui à hérité d'une classe spécifiée sinon false
"""


def is_kind_of_class(obj, a_class):
    """ Retourne un booléen si l'objet est une instance
    de la classe spécifiée ou l'objet d'une sous classe qui à hérité
    d'une classe.

    Args:
        obj (any): L'objet à inspecter.
        a_class : La classe de référence

    Returns:
        True : L'objet est une instance de la classe spécifiée ou
        d'une sous classe qui à hérité d'une classe
        False : L'objet n'est pas une instance de la classe spécifiée ou
        d'une sous classe qui à hérité d'une classe
    """
    return isinstance(obj, a_class)
