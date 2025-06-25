# 📁 Projet SQL - Introduction

Ce projet fait partie du programme **[Foundations v2.1 - Part 2]** proposé par Holberton School.

## 🎯 Objectifs pédagogiques

À l’issue de ce projet, je suis capable de :
- Expliquer ce qu’est une base de données relationnelle
- Définir et manipuler une base MySQL
- Utiliser le langage SQL (Structured Query Language)
- Différencier DDL (Data Definition Language) et DML (Data Manipulation Language)
- Créer, modifier et supprimer des bases et des tables
- Insérer, sélectionner, mettre à jour et supprimer des données
- Utiliser des sous-requêtes et des fonctions SQL
- Comprendre la différence entre backticks (`) et apostrophes (')

---

## 🛠️ Environnement de travail

- 💻 **OS** : Ubuntu 20.04 LTS (ou Ubuntu 22.04 via conteneur CoD)
- 🧩 **MySQL** : version 8.0
- 🛠️ **Éditeurs autorisés** : `vi`, `vim`, `emacs`
- 📌 **Convention** :
  - Chaque fichier SQL commence par un commentaire décrivant la tâche
  - Chaque requête est précédée d’un commentaire expliquant son but
  - Les mots-clés SQL sont en majuscules (`SELECT`, `WHERE`, etc.)
  - Tous les fichiers se terminent par une ligne vide
  - Les longueurs sont contrôlées avec `wc`

---

## 🗃️ Contenu du projet

Chaque fichier SQL répond à une tâche précise :

| Fichier                         | Description                                                             |
|---------------------------------|-------------------------------------------------------------------------|
| `0-list_databases.sql`          | Liste toutes les bases de données                                      |
| `1-create_database_if_missing.sql` | Crée une base `hbtn_0c_0` si elle n'existe pas                         |
| `2-remove_database.sql`         | Supprime la base `hbtn_0c_0` si elle existe                            |
| `3-list_tables.sql`             | Liste toutes les tables d'une base donnée                              |
| `4-first_table.sql`             | Crée une table `first_table` avec `id` et `name`                       |
| `5-full_table.sql`              | Affiche la structure SQL complète de `first_table`                     |
| `6-list_values.sql`             | Liste toutes les lignes de `first_table`                               |
| `7-insert_value.sql`            | Insère une ligne : `(89, "Best School")` dans `first_table`            |
| `8-count_89.sql`                | Compte les lignes où `id = 89` dans `first_table`                      |
| `9-full_creation.sql`           | Crée une table `second_table` et y insère plusieurs lignes             |
| `10-top_score.sql`              | Liste les lignes de `second_table` triées par score décroissant        |
| `11-best_score.sql`             | Liste les lignes avec `score >= 10`, triées par score                  |
| `12-no_cheating.sql`           | Met à jour le score de "Bob" sans utiliser son `id`                    |
| `13-change_class.sql`          | Supprime les lignes avec `score <= 5`                                  |
| `14-average.sql`               | Calcule la moyenne des scores de `second_table`                        |
| `15-groups.sql`                | Compte combien de fois chaque score apparaît                           |
| `16-no_link.sql`               | Affiche uniquement les lignes où `name` n’est pas vide                 |

---

## 🚀 Instructions d'exécution

Démarrer MySQL :
```bash
sudo service mysql start
```

---

## Exécuter un script :
```bash
cat fichier.sql | mysql -uroot -p [nom_base]
```

---

## 📌 Remarques
- Ce projet est 100% en SQL brut, sans interface graphique.
- Chaque fichier est indépendant et peut être testé dans un conteneur Ubuntu/Mysql.
- Le projet a été testé avec mysql -u root -p en ligne de commande.
