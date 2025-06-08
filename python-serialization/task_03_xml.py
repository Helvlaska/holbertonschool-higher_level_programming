#!/usr/bin/env python3
"""
Module task_03_xml

Ce module fournit deux fonctions permettant de :
- Sérialiser un dictionnaire Python dans un fichier XML.
- Désérialiser un fichier XML pour en reconstituer un dictionnaire Python.

Le format utilisé est basé sur le module `xml.etree.ElementTree` de la
bibliothèque standard.
Toutes les valeurs sont converties en chaînes de caractères dans le
fichier XML.

Fichier XML attendu :
<data>
    <cle1>valeur1</cle1>
    <cle2>valeur2</cle2>
</data>
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python dans un fichier XML.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier XML de sortie.

    Comportement :
        Crée un élément racine <data> et y ajoute une balise
        par paire clé/valeur.
        Toutes les valeurs sont converties en chaînes de caractères.
    """
    # Création élément "racine"(data)
    # Tout les éléments enfant key/value du dico
    root = ET.Element("data")
    # Boucle sur les paires key/value
    for key, value in dictionary.items():
        # Pour chaque paire ont crée un enfant
        child = ET.SubElement(root, key)
        # La value est convertie en string
        child.text = str(value)
    # Création d'un obj basé sur la "racine"
    tree = ET.ElementTree(root)
    # Ecriture dans le fichier
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        dict: Un dictionnaire dont les clés sont les balises
        XML et les valeurs leur contenu texte.

    Remarque :
        Toutes les valeurs sont des chaînes de caractères
        (pas de reconversion automatique).
    """
    # Lecture et parsing du fichier
    tree = ET.parse(filename)
    # Récupération de la racine
    root = tree.getroot()
    # Initialisation d'un dico vide pour stocker les données
    result = {}
    # Boucle sur chaque enfant de la racine
    for child in root:
        # Ajout dans le dico sous format key/value
        result[child.tag] = child.text
    return result  # return le dico reconstitué
