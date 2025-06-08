#!/usr/bin/env python3
"""
Module task_02_csv

Ce module contient une fonction permettant de lire un
fichier CSV et de convertir son contenu en un fichier JSON.
Il illustre la sérialisation de données tabulaires vers un format texte
structuré, lisible et interopérable.

Fonctionnalités :
- Lecture de fichiers CSV à l’aide de csv.DictReader
- Conversion du contenu en liste de dictionnaires
- Écriture dans un fichier JSON avec indentation
- Gestion des erreurs de lecture/écriture

Fichier de sortie : data.json
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convertit un fichier CSV en fichier JSON (data.json).

    Args:
        filename (str): Nom du fichier CSV à convertir.

    Returns:
        bool: True si la conversion a réussi, False sinon.

    Exceptions gérées :
        - FileNotFoundError : Fichier CSV introuvable.
        - IOError : Problèmes de lecture/écriture.
        - csv.Error : Fichier mal formé ou encodage incorrect.
    """
    # Ont essaye de...
    try:
        list_dict = []  # Initialiser une liste vide
        # D'ouvrir le fichier csv en mode lecture
        with open(filename, mode="r", newline="") as file:
            # De récupérer les données lus dans le fichier
            content = csv.DictReader(file)
            # De boucler dans content ligne par ligne
            for ligne in content:
                # De stocker les lignes dans la liste de dictionnaires
                list_dict.append(ligne)

        # D'ouvrir mon fichier json en mode écriture
        with open("data.json", "w") as json_file:
            # D'ajouter ma liste de dictionnaires au fichier.json
            json.dump(list_dict, json_file, indent=4)

        return True  # Si tout se passe bien je return True
    # Sinon ça lève une exception et return False
    except (FileNotFoundError, IOError, csv.Error) as e:
        print(f"Erreur lors de la conversion : {e}")
        return False
