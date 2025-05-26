#!/usr/bin/python3
""" Fonction qui renvoie la liste des attributs
    et méthodes disponibles d'un objet.
"""


def lookup(obj):
    """ Retourne une liste contenant les noms des attributs et méthodes
    accessibles de l'objet passé en paramètre.

    Args:
        obj (any): L'objet à inspecter.

    Returns:
        list: Liste des attributs et méthodes accessibles de l'objet.
    """
    return dir(obj)
