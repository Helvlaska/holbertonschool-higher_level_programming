# 📦 Python - Server-Side Rendering (SSR)

Ce projet me guidera dans l’implémentation du SSR en Python à l’aide de **Flask** et du moteur de templates **Jinja2**. j'apprendrais à afficher dynamiquement des données issues de plusieurs sources (fichiers, bases de données) à travers des pages HTML générées côté serveur.

---

## 🚀 Objectifs pédagogiques

- Comprendre la différence entre SSR et client-side rendering.
- Identifier les avantages du SSR (performance, SEO, simplicité).
- Apprendre à utiliser **Flask** comme serveur web léger.
- Utiliser **Jinja2** pour créer des pages HTML dynamiques.
- Lire et afficher des données à partir de fichiers **JSON**, **CSV** et **SQLite**.
- Gérer des entrées dynamiques et afficher les erreurs côté serveur.

---

## 🧩 Contenu du projet

### ✅ Tâche 0 — Générateur de fichiers personnalisés *(task_00_intro.py)*

Créer une fonction `generate_invitations(template, attendees)` :

- 📄 Lit un template de fichier avec des placeholders : `{name}`, `{event_title}`, etc.
- 🔄 Remplace dynamiquement les valeurs pour chaque invité.
- 📝 Génére un fichier `output_X.txt` par invité.
- ✅ Gestion des erreurs : mauvais types, template vide, données manquantes (remplacées par "N/A").

### ✅ Tâche 1 — Application Flask de base *(task_01_jinja.py)*

Créer une première application Flask :

- 🎨 Page HTML de base : `index.html` avec balises `<h1>`, `<p>`, `<ul>`.
- 🔁 Réutilisation de templates `header.html` et `footer.html` via `{% include %}`.
- 📂 Création de plusieurs routes (`/`, `/about`, `/contact`) avec des pages spécifiques.

### ✅ Tâche 2 — Template dynamique avec Jinja *(task_02_logic.py)*

- 📁 Lecture d’un fichier `items.json` contenant une liste d’objets.
- 🔃 Affichage dynamique via une boucle `{% for %}`.
- ⚠️ Affichage conditionnel (`{% if items %}`) si la liste est vide.
- 📍 Route : `/items`.

### ✅ Tâche 3 — Affichage de données JSON ou CSV *(task_03_files.py)*

- 📁 Lecture de `products.json` ou `products.csv` selon le paramètre `source`.
- 🧮 Utilisation d’un paramètre facultatif `id` pour filtrer un produit spécifique.
- 🧾 Affichage des produits sous forme de tableau dans `product_display.html`.
- ❗ Gestion des erreurs :
  - source invalide → "Wrong source"
  - id introuvable → "Product not found"

### ✅ Tâche 4 — Lecture de données SQLite *(task_04_db.py)*

- 🗃️ Connexion à la base `products.db` (table `Products`).
- 🔄 Extension du paramètre `source=sql`.
- 🔎 Filtrage par `id` optionnel.
- ♻️ Réutilisation du même template HTML.
- 🛑 Gestion d’erreurs SQL et sources invalides.

---

## 📁 Arborescence du projet

python-server_side_rendering/
├── data/
│ ├── template.txt
│ ├── attendees.json
│ ├── items.json
│ ├── products.json
│ ├── products.csv
│ └── products.db
├── templates/
│ ├── index.html
│ ├── about.html
│ ├── contact.html
│ ├── header.html
│ ├── footer.html
│ └── product_display.html
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
└── README.md

---

## 🧪 Exécution du projet

### 📌 Lancer le serveur Flask

```bash
# Pour chaque tâche Flask :
python3 task_00_intro.py
python3 task_01_jinja.py
python3 task_02_logic.py
...
```

---

## 🌐 Accès dans le navigateur

- Accueil : http://localhost:5000/
- Liste des objets : http://localhost:5000/items
- Produits JSON : http://localhost:5000/products?source=json
- Produits CSV : http://localhost:5000/products?source=csv
- Produits SQL : http://localhost:5000/products?source=sql

---

## 🎯 Ce que je saurais faire à la fin

✔ Comprendre les différences entre SSR et CSR.
✔ Créer des routes Flask et des templates dynamiques avec Jinja.
✔ Lire des fichiers JSON/CSV et des bases SQLite.
✔ Gérer des erreurs et des entrées utilisateur proprement.
✔ Concevoir des pages web dynamiques et performantes côté serveur.
