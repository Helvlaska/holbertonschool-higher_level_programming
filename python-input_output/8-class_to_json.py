#!/usr/bin/python3
"""
Module 8-class_to_json
Retourne un dictionnaire représentant les attributs simples
d'une instance pour la sérialisation JSON.
"""


def class_to_json(obj):
    """
    Retourne un dictionnaire décrivant les attributs simples d'une instance.

    Cette fonction extrait tous les attributs publics
    (sans underscore au début) de l'objet passé en argument,
    et les retourne sous forme de paires clé/valeur prêtes à être
    sérialisées en JSON.

    Args:
        obj: Une instance d'une classe.

    Returns:
        new_dictionnaire: Un dictionnaire contenant les attributs de l'objet
        (listes, chaînes, booléens, entiers, dictionnaires),
        prêt à être sérialisé.
    """
    my_list_attributs = dir(obj)
    new_dictionnaire = {}

    for i in my_list_attributs:
        if not i.startswith('__'):
            value = getattr(obj, i)
            new_dictionnaire[i] = value
    return new_dictionnaire
