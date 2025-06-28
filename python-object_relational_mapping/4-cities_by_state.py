#!/usr/bin/ python3
"""Script qui affiche toutes les villes de la base de données, ainsi que
le nom de leur état respectif, triées par identifiant de ville."""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Point d’entrée du script.
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

    # Requête pour récupérer toutes les villes de la BDD
    curseur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id
    """)

    # Récupération de la requête
    lignes = curseur.fetchall()
    for ligne in lignes:
        print(ligne)

    # Fermeture propre du curseur et de la connexion
    curseur.close()
    connexion.close()
