#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import MySQLdb

# Charger les variables du fichier .env pour mes identifiants
load_dotenv()

# Connexion à la BDD
connexion = MySQLdb.connect(
    host = "localhost",
    port = 3306,
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWORD"),
    db = "hbtn_0e_0_usa"
)

# Création d'un curseur pour lire et écrire dans la BDD
curseur = connexion.cursor()

# Requête pour récupérer tout les states de la BDD
curseur.execute("SELECT * FROM states")

# Récupération de la requête
lignes = curseur.fetchall()
for ligne in lignes:
    print(ligne)

# Fermeture propre du curseur et de la connexion
curseur.close()
connexion.close()
