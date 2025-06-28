#!/usr/bin/env python3
"""Script qui se connecte à une base de données MySQL et affiche
toutes les entrées de la table `states`."""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Point d'entrée principal du script.
    Utilise les arguments passés en ligne de commande :
    - argv[1] : nom d'utilisateur MySQL
    - argv[2] : mot de passe MySQL
    - argv[3] : nom de la base de données
    """
    # Connexion à la BDD
    connexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création d'un curseur pour lire et écrire dans la BDD
    curseur = connexion.cursor()

    # Requête pour récupérer tout les states de la BDD
    curseur.execute("SELECT * FROM states ORDER BY id")

    # Récupération de la requête
    lignes = curseur.fetchall()
    for ligne in lignes:
        print(ligne)

    # Fermeture propre du curseur et de la connexion
    curseur.close()
    connexion.close()
