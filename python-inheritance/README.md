# 🐍 Projet Python : L'Héritage (Inheritance)

Ce projet explore le concept **d'héritage** en Python à travers une série d'exercices structurés. Il couvre des notions clés comme l'héritage de classes, la redéfinition de méthodes, la validation de types, les méthodes abstraites, et plus encore.

---

## 🗂️ Table des matières

1. [📁 Structure du projet](#structure-du-projet)
2. [⚙️ Prérequis](#prérequis)
3. [📌 Présentation des exercices](#présentation-des-exercices)
4. [🧪 Comment lancer les tests](#comment-lancer-les-tests)
5. [🧠 Notions abordées](#notions-abordées)

---

## 📁 Structure du projet

```
python-inheritance/
├── 0-lookup.py
├── 1-my_list.py
├── 2-is_same_class.py
├── 3-is_kind_of_class.py
├── 4-inherits_from.py
├── 5-base_geometry.py
├── 6-base_geometry.py
├── 7-base_geometry.py
├── 8-rectangle.py
├── 9-rectangle.py
├── 10-square.py
├── 11-square.py
└── tests/
    ├── 1-my_list.txt
    └── 7-base_geometry.txt
```

---

## ⚙️ Prérequis

* Aucun module ne doit être importé (sauf indication contraire)
* Tous les modules, classes et fonctions doivent être documentés avec une **docstring** claire
* Tous les fichiers de test :

  * Doivent avoir l'extension `.txt`
  * Doivent être placés dans le dossier `tests/`

---

## 📌 Présentation des exercices

### 0. Lookup 🔍

Retourne la liste des attributs et méthodes disponibles d'un objet via `dir()`.

### 1. MyList 📃

Crée une classe `MyList` qui hérite de `list`, avec une méthode `print_sorted()` pour afficher la liste triée.

### 2. Exact same object ✅

Vérifie si un objet est exactement une instance d'une classe spécifiée.

### 3. Same class or inherit from 👨‍👩‍👧‍👦

Retourne `True` si un objet est une instance d'une classe ou d'une de ses sous-classes.

### 4. Only sub class of 🧬

Retourne `True` uniquement si l'objet est une sous-classe (pas la même classe) d'une autre.

### 5. Geometry module 📐

Définit une classe vide `BaseGeometry`.

### 6. Improve Geometry 🚧

Ajoute la méthode `area()` à `BaseGeometry`, qui lève une exception `area() is not implemented`.

### 7. Integer validator 🔢

Ajoute la méthode `integer_validator()` à `BaseGeometry`, qui valide le type et la valeur d'un entier.

### 8. Rectangle 🧱

Crée une classe `Rectangle` qui hérite de `BaseGeometry`, avec validation des attributs `width` et `height`.

### 9. Full rectangle 🧾

Implémente `__str__()` et `area()` dans la classe `Rectangle` pour afficher ses dimensions.

### 10. Square #1 ◼️

Crée une classe `Square` qui hérite de `Rectangle`, avec largeur = hauteur.

### 11. Square #2 🧊

Améliore `Square` avec une représentation personnalisée : `[Square] largeur/hauteur`.

---

## 🧪 Comment lancer les tests

Tous les doctests sont exécutés avec la commande suivante :

```bash
python3 -m doctest ./tests/*
```

---

## 🧠 Notions abordées

* Héritage de classes en Python
* Utilisation de `super()` pour étendre les constructeurs
* Redéfinition de méthodes
* Vérification de types avec `isinstance()` et `type()`
* Attributs privés (encapsulation)
* Méthodes abstraites (via levée d'exceptions)
* Bon usage de `__str__` et `__repr__`
* Tests avec doctest

---

> 🧠 Ce projet pose les bases de la programmation orientée objet (POO) en Python et prépare à des sujets plus avancés comme les classes abstraites et les interfaces.
