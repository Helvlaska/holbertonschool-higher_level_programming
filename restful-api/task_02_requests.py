#!/usr/bin/env python3

import requests  # J'importe la bibliothèque requests
import csv   # J'importe la bibliothèque csv

# Je créer une fonction pour récupérer
# tout les messages de JSONplaceholder
# et les afficher dans la console


def fetch_and_print_posts():
    # Je déclare l'URL de l'API
    url = "https://jsonplaceholder.typicode.com/posts"
    # J'essaye de...
    try:
        # Je fais une requête GET à l'API
        # et je stocke la réponse dans une variable
        reponse = requests.get(url)
        # Je print le code statut de ma requête
        print(f"Status Code: {reponse.status_code}")
        # Je vérifie que la requête a réussi
        if reponse.status_code == 200:
            # Je convertis la réponse en JSON
            reponse_json = reponse.json()
            # Je parcours les posts et je les affiche
            for objet in reponse_json:
                print(f"Title: {objet['title']}")
        else:
            # Si la requête a échoué, j'affiche un message d'erreur
            print(f"Code statut: {reponse.status_code}")
    # Si l'essai ne marche pas, j'attrape l'exception
    # et j'affiche un message d'erreur
    except requests.exceptions.RequestException as e:
        # Si une exception est levée, j'affiche un message d'erreur
        print(f"Une erreur s'est produite : {e}")

# Je créer une fonction pour récupérer
# tout les messages de JSONplaceholder
# et les sauvegarder dans un fichier csv


def fetch_and_save_posts():
    # Je déclare l'URL de l'API
    url = "https://jsonplaceholder.typicode.com/posts"
    # J'essaye de...
    try:
        # Je fais une requête GET à l'API
        # et je stocke la réponse dans une variable
        reponse = requests.get(url)
        # Je vérifie que la requête a réussi
        if reponse.status_code == 200:
            # Je convertis la réponse en JSON
            reponse_json = reponse.json()
            # Je crée un fichier CSV pour sauvegarder les posts
            with open(
                "posts.csv", mode="w", newline="", encoding="utf-8"
            ) as fichier_csv:
                # Je crée un writer pour écrire dans le fichier CSV
                writer = csv.writer(fichier_csv)
                # J'écris l'en-tête du fichier CSV
                writer.writerow(["id", "title", "body"])
                # Je boucle sur les réponses JSON
                for obj in reponse_json:
                    # et j'écris chaque post dans le fichier CSV
                    writer.writerow([obj["id"], obj["title"], obj["body"]])
        else:  # si la requête a échoué, j'affiche un message d'erreur
            print(f"Code statut: {reponse.status_code}")
    # Si une exception est levée, j'affiche un message d'erreur
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite : {e}")
        return
