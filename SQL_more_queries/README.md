# 📚 SQL - More Queries

> Holberton School / Foundations v2.1 – Part 2
> Projet noté | Poids : 1 | Correction manuelle

## 🧠 Objectifs pédagogiques

À la fin de ce projet, vous serez capable d’expliquer (sans Google !) :

- Comment créer un nouvel utilisateur MySQL
- Comment gérer les privilèges d’un utilisateur sur une base ou une table
- Ce qu’est une **clé primaire** (`PRIMARY KEY`)
- Ce qu’est une **clé étrangère** (`FOREIGN KEY`)
- Comment utiliser les contraintes `NOT NULL` et `UNIQUE`
- Comment récupérer des données issues de **plusieurs tables**
- Ce que sont les **subqueries**
- La différence entre **JOIN** et **UNION**

---

## ⚙️ Environnement & Contraintes

- OS : Ubuntu 20.04 LTS
- MySQL : version 8.0.25
- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous les fichiers doivent :
  - Commencer par un commentaire décrivant la tâche
  - Utiliser les mots-clés SQL en **majuscules**
  - Se terminer par une **nouvelle ligne**
  - Inclure un **commentaire SQL avant chaque requête**
- Le fichier `README.md` est obligatoire
- Vérification de la longueur des fichiers via `wc`

---

## 📁 Fichiers attendus

| Fichier                         | Description |
|--------------------------------|-------------|
| `0-privileges.sql`             | Affiche les privilèges des utilisateurs `user_0d_1` et `user_0d_2` |
| `1-create_user.sql`            | Crée l'utilisateur `user_0d_1` avec tous les privilèges |
| `2-create_read_user.sql`       | Crée la base `hbtn_0d_2` et un utilisateur lecture seule `user_0d_2` |
| `3-force_name.sql`             | Crée une table avec une colonne `name` non-nulle |
| `4-never_empty.sql`            | Crée une table avec un `id` par défaut |
| `5-unique_id.sql`              | Crée une table avec un `id` unique par défaut |
| `6-states.sql`                 | Crée une base `hbtn_0d_usa` et une table `states` avec clé primaire |
| `7-cities.sql`                 | Crée la table `cities` avec une clé étrangère vers `states` |
| `8-cities_of_california_subquery.sql` | Liste les villes de Californie sans utiliser `JOIN` |
| `9-cities_by_state_join.sql`   | Liste toutes les villes avec leur état, avec `JOIN` |
| `10-genre_id_by_show.sql`      | Liste tous les shows ayant au moins un genre |
| `11-genre_id_all_shows.sql`    | Liste tous les shows avec leurs genres (NULL si aucun) |
| `12-no_genre.sql`              | Liste les shows **sans aucun genre** |
| `13-count_shows_by_genre.sql`  | Compte le nombre de shows par genre (ordre décroissant) |
| `14-my_genres.sql`             | Affiche tous les genres du show *Dexter* |
| `15-comedy_only.sql`           | Liste tous les shows de genre *Comedy* |
| `16-shows_by_genre.sql`        | Liste tous les shows avec leurs genres associés (NULL si aucun) |

---

## 🗃️ Base de données utilisée

Certaines tâches nécessitent d’importer un dump SQL :

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

---

## 📌 Recommandations

- Testez chaque fichier individuellement :

```bash
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```

- Respectez strictement les formats de sortie.
- Les mots-clés SQL (SELECT, INSERT, JOIN, etc.) doivent être en MAJUSCULES.
- Utilisez les commentaires SQL pour expliquer chaque requête.
