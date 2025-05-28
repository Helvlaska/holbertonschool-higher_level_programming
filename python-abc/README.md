# 🐍 Projet POO Avancée – Python : Classes Abstraites, Héritage Multiple et Mixins

## 🎯 Objectif du projet

Ce projet a pour but d’approfondir la **programmation orientée objet (POO) en Python**, en explorant plusieurs notions clés :
- Les **classes abstraites** et l’utilisation du module `abc`
- Le **duck typing**
- L’**héritage multiple** et la résolution des méthodes (MRO)
- La **surcharge de classes natives**
- L’utilisation de **mixins** pour ajouter des fonctionnalités de manière modulaire

---

## 🧠 Concepts abordés

- ✅ Classes abstraites et méthodes obligatoires (`@abstractmethod`)
- ✅ Polymorphisme par le duck typing
- ✅ Héritage de classes natives (`list`, `iterator`)
- ✅ Méthodes magiques (`__next__`, etc.)
- ✅ Résolution de l’ordre des méthodes (MRO)
- ✅ Mixins pour la composition de comportements

---

## 🗂 Structure des fichiers

python-abc/
├── task_00_abc.py
├── task_01_duck_typing.py
├── task_02_verboselist.py
├── task_03_countediterator.py
├── task_04_flyingfish.py
├── task_05_dragon.py
├── main_00_abc.py
├── main_01_duck_typing.py
├── main_02_verboselist.py
├── main_03_countediterator.py
├── main_04_flyingfish.py
└── main_05_dragon.py


---

## 🔍 Détail des tâches

| Tâche | Description | Notions clés |
|------:|-------------|--------------|
| 0 | Classe abstraite `Animal` avec méthodes redéfinies dans `Dog` et `Cat` | `abc`, `@abstractmethod` |
| 1 | Classe `Shape` abstraite, duck typing avec `shape_info()` | Polymorphisme, duck typing |
| 2 | Surcharge des méthodes `append`, `extend`, `remove`, `pop` dans `VerboseList` | Héritage de `list` |
| 3 | Itérateur personnalisé `CountedIterator` avec suivi du nombre d’éléments parcourus | `__next__`, `iter`, encapsulation |
| 4 | Classe `FlyingFish` héritant de `Fish` et `Bird`, avec exploration du MRO | Héritage multiple, MRO |
| 5 | Mixins `SwimMixin` et `FlyMixin`, classe `Dragon` combinant plusieurs comportements | Mixins, composition |

---

## ⚙️ Utilisation

Pour tester chaque tâche :
```bash
$ python3 main_XX_<nom>.py
