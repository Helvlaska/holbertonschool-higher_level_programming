#!/usr/bin/env python3
"""
Module task_00_basic_serialization

Ce module fournit deux fonctions pour :
- Sérialiser un dictionnaire Python dans un fichier JSON.
- Désérialiser un fichier JSON pour reconstituer le dictionnaire original.

Utilise le module json de la bibliothèque standard.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et l’enregistre dans un fichier JSON.

    Args:
        data (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier de sortie.
        Écrase le fichier s’il existe déjà.

    Raises:
        TypeError: Si l'objet n'est pas sérialisable en JSON.
        IOError: En cas de problème d'écriture dans le fichier.
    """
    # Sérialisation dans un fichier JSON
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charge un fichier JSON et le désérialise en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        dict: Le contenu du fichier sous forme de dictionnaire Python.

    Raises:
        json.JSONDecodeError: Si le fichier n’est pas un JSON valide.
        FileNotFoundError: Si le fichier est introuvable.
        IOError: En cas d’erreur de lecture.
    """
    # Lire et désérialiser le fichier JSON
    with open(filename, "r") as file:
        return json.load(file)
