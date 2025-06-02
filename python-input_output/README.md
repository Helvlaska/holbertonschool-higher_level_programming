# 📁 Python - Input/Output & JSON

## 📚 Description

Ce projet aborde les fondamentaux de la gestion des fichiers et de la sérialisation en Python.  
Il couvre l'ouverture, l'écriture, l'ajout, la lecture de fichiers texte, ainsi que la conversion d'objets Python en chaînes JSON (et inversement).  
Les fonctions utilisent systématiquement le mot-clé `with` pour garantir une bonne gestion des ressources.

## 🛠️ Fonctions implémentées

| Fichier                | Fonction                        | Description |
|------------------------|----------------------------------|-------------|
| `0-read_file.py`       | `read_file(filename=\"\")`       | Lit un fichier texte UTF-8 et affiche son contenu |
| `1-write_file.py`      | `write_file(filename, text)`     | Écrit une chaîne dans un fichier, retourne le nombre de caractères écrits |
| `2-append_write.py`    | `append_write(filename, text)`   | Ajoute une chaîne à la fin d’un fichier |
| `3-to_json_string.py`  | `to_json_string(my_obj)`         | Convertit un objet Python en chaîne JSON |
| `4-from_json_string.py`| `from_json_string(my_str)`       | Convertit une chaîne JSON en objet Python |
| `5-save_to_json_file.py`| `save_to_json_file(my_obj, filename)` | Sérialise un objet Python dans un fichier JSON |
| `6-load_from_json_file.py`| `load_from_json_file(filename)` | Désérialise un fichier JSON en objet Python |
| `7-add_item.py`        | Script : ajoute tous les arguments à une liste JSON sauvegardée |
| `8-class_to_json.py`   | `class_to_json(obj)`             | Retourne le dictionnaire simple pour la sérialisation d'un objet |
| `9-student.py`         | Classe `Student` avec méthode `to_json()` |
| `10-student.py`        | `to_json(attrs)` : filtrage des attributs à sérialiser |
| `11-student.py`        | `reload_from_json(json)` : recharge les attributs depuis un dictionnaire |
| `12-pascal_triangle.py`| `pascal_triangle(n)`             | Génère un triangle de Pascal sous forme de liste de listes |

## ✅ Contraintes

- Aucun module externe n’est autorisé sauf `json` lorsque précisé
- Utilisation obligatoire de `with` pour la gestion des fichiers
- Pas de gestion d’erreurs demandée sauf indication contraire
- Aucune importation de modules système comme `os` ou `sys` sauf mention explicite

## 🚀 Exécution

```bash
python3 0-main.py
python3 3-main.py


🧠 Concepts abordés
Input / Output (lecture et écriture de fichiers)

Utilisation du mot-clé with pour la gestion des ressources

Sérialisation / désérialisation en JSON

Passage d'arguments via la ligne de commande

Conception de classes et export JSON
