# 📚 Python - Object-relational mapping

> Projet Holberton – Bases de la programmation orientée objet avec SQL et Python

## 🧠 Contexte

Ce projet lie deux mondes fondamentaux : les **bases de données relationnelles** (MySQL) et le **langage Python**.
Il est divisé en deux grandes parties :

1. Connexion directe à une base MySQL via `MySQLdb` (requêtes SQL classiques)
2. Utilisation de l'ORM `SQLAlchemy` pour manipuler la base uniquement via des objets Python

L’objectif : comprendre comment structurer des données de manière persistante **sans écrire de SQL** à terme, tout en s’initiant aux bonnes pratiques de sécurité (SQL injection, `.env`).

---

## 📌 Objectifs pédagogiques

- Se connecter à une base MySQL avec Python
- Lire, insérer, mettre à jour, supprimer des données via script
- Comprendre les principes d’un ORM et la couche d’abstraction
- Mapper une classe Python avec une table MySQL
- Utiliser SQLAlchemy pour exécuter des requêtes complexes

---

## 🧩 Structure du projet

| N°  | Fichier(s)                          | Description                                                                 |
|-----|-------------------------------------|-----------------------------------------------------------------------------|
| 0   | `0-select_states.py`               | Liste tous les états depuis la table `states` avec `MySQLdb`.              |
| 1   | `1-filter_states.py`               | Liste les états commençant par "N".                                        |
| 2   | `2-my_filter_states.py`            | Filtre un état par nom donné en argument (vulnérable à l'injection SQL).   |
| 3   | `3-my_safe_filter_states.py`       | Filtrage sécurisé d’un état (protégé contre l’injection SQL).              |
| 4   | `4-cities_by_state.py`             | Affiche toutes les villes avec leur état (jointure entre `cities` et `states`). |
| 5   | `5-filter_cities.py`               | Affiche toutes les villes d’un état donné (sécurisé).                      |
| 6   | `model_state.py`                   | Définition de la classe `State` via SQLAlchemy.                            |
|     | `6-model_state.py`                 | Création de la table `states` dans la BDD via ORM.                         |
| 7   | `7-model_state_fetch_all.py`       | Affiche tous les objets `State` (triés par `id`).                          |
| 8   | `8-model_state_fetch_first.py`     | Affiche le premier `State` (par `id`) ou "Nothing" si vide.                |
| 9   | `9-model_state_filter_a.py`        | Affiche tous les `State` contenant la lettre "a".                          |
| 10  | `10-model_state_my_get.py`         | Recherche un `State` par nom, affiche son `id` ou "Not found".            |
| 11  | `11-model_state_insert.py`         | Ajoute l’état "Louisiana" et affiche son `id`.                             |
| 12  | `12-model_state_update_id_2.py`    | Met à jour le nom du `State` avec `id = 2` en "New Mexico".               |
| 13  | `13-model_state_delete_a.py`       | Supprime tous les `State` contenant la lettre "a".                         |
| 14  | `model_city.py`                    | Définition de la classe `City`, liée à `State` (clé étrangère).           |
|     | `14-model_city_fetch_by_state.py`  | Affiche toutes les villes, groupées par état.                              |

---

## 🔧 Technologies

- Python 3.8.5
- MySQL 8.0
- MySQLdb 2.0.x (`mysqlclient`)
- SQLAlchemy 1.4.x
- Ubuntu 20.04 LTS

---

## 🛡️ Sécurité

Pour éviter de stocker les identifiants en dur dans les scripts Python, le projet utilise un fichier `.env` contenant :
    MYSQL_USER=mon_utilisateur
    MYSQL_PWD=mon_mot_de_passe
