# 📡 RESTful API - Projet Holberton

Ce projet a pour objectif d'explorer les bases des API RESTful à travers différentes étapes progressives, en utilisant à la fois des outils en ligne de commande, des scripts Python, le module `http.server` intégré, ainsi que le framework Flask.

---

## 📚 Contenu du projet

### 0. Basics of HTTP/HTTPS
- Comprendre la différence entre HTTP et HTTPS.
- Observer la structure des requêtes HTTP avec l’inspecteur réseau.
- Identifier les principales méthodes (GET, POST...) et les codes de statut HTTP (200, 404, 500...).

### 1. Utilisation de `curl` pour interagir avec une API
- Installation et test de `curl`.
- Requêtes GET, POST et visualisation des en-têtes avec `-I`.
- Interaction avec l’API publique [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

### 2. Consommation d'une API avec Python et `requests`
- Script Python utilisant `requests.get()` pour afficher et sauvegarder les posts.
- Conversion du JSON en CSV à l’aide du module `csv`.

### 3. Création d’une API simple avec `http.server`
- Serveur HTTP local répondant aux endpoints :
  - `/` → message d’accueil.
  - `/data` → données JSON (nom, âge, ville).
  - `/status` → "OK"
  - `/info` → version + description de l'API.
  - Autres → 404 avec message JSON personnalisé.

### 4. Création d’une API RESTful avec Flask
- Initialisation d’un serveur Flask.
- Routes dynamiques et POST avec gestion de données utilisateurs en mémoire.
- Réponses JSON, statuts HTTP, validation.

### 5. Sécurisation de l’API avec Auth & JWT
- Authentification basique avec `Flask-HTTPAuth`.
- Authentification avancée avec `Flask-JWT-Extended`.
- Gestion de rôles (user/admin).
- Protection des routes avec des décorateurs.
- Gestion des erreurs 401/403 de manière personnalisée.

---

## 🛠️ Technologies utilisées
- Python 3
- curl
- Flask
- http.server
- requests
- JSON, CSV
- JWT (JSON Web Token)
- Git & GitHub

---

## 💡 Organisation du dépôt
restful-api/
├── task_02_requests.py
├── main_02_requests.py
├── task_03_http_server.py
├── task_04_flask.py
├── task_05_basic_security.py
├── posts.csv
└── README.md
