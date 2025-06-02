#!/usr/bin/python3
"""
Fonctionnement du script :

- Tente de charger une liste existante depuis le fichier 'add_item.json'.
- Si le fichier n'existe pas, initialise une liste vide.
- Ajoute les arguments passés en ligne de commande à cette liste.
- Sauvegarde la nouvelle version de la liste dans le fichier JSON.

Modules utilisés :
- save_to_json_file : pour enregistrer l'objet dans un fichier JSON.
- load_from_json_file : pour charger un objet à partir d'un fichier JSON.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []  # initialiser une liste vide si le fichier n'existe pas

# ajouter les nouveaux arguments à la liste
my_list.extend(sys.argv[1:])

# sauvegarder la liste mise à jour
save_to_json_file(my_list, filename)
