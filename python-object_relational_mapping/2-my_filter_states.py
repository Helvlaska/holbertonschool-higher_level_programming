#!/usr/bin/python3
"""Script qui se connecte à une base de données MySQL et affiche
toutes les entrées de la table `states`dont le nom correspond à l'argument."""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Point d'entrée principal du script.
    Utilise les arguments passés en ligne de commande :
    - argv[1] : nom d'utilisateur MySQL
    - argv[2] : mot de passe MySQL
    - argv[3] : nom de la base de données
    - argv[4] : nom du pays recherché dans la BDD
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

    # Stocker l'argument du pays recherché dans une variable
    pays = sys.argv[4]

    # Requête pour récupérer tout les states de la BDD
    # correspondant à l'argument
    curseur.execute("""
        SELECT * FROM states
        WHERE BINARY name = '{}'
        ORDER BY id
    """.format(pays))

    # Récupération de la requête
    lignes = curseur.fetchall()
    for ligne in lignes:
        print(ligne)

    # Fermeture propre du curseur et de la connexion
    curseur.close()
    connexion.close()
