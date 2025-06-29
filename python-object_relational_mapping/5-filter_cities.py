#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
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

    # Stock l'argument du pays dans une variable
    pays = sys.argv[4]

    # Requête pour récupérer toutes les villes du pays
    curseur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id
    """, (pays,))

    # Récupération et mise en forme de la requête
    lignes = curseur.fetchall()
    # Création d'une liste vide
    cities_list = []
    # Boucle pour récupérer le resultat de la requête ligne par ligne
    for ligne in lignes:
        # Chaque ligne est un tuple ('San Jose',)
        # Je recupère le 1er élément de chaque ligne
        cities_name = ligne[0]
        # Je l'ajoute à ma liste
        cities_list.append(cities_name)
    # Je formate ma liste de villes et je la print
    result = ", ".join(cities_list)
    print(result)

    # Fermeture propre du curseur et de la connexion
    curseur.close()
    connexion.close()
