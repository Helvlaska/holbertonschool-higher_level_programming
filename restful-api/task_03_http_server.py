#!/usr/bin/env python3
"""
Ce module implémente un serveur HTTP simple avec Python.

Il gère les requêtes GET sur différentes routes et renvoie des réponses
au format texte ou JSON selon l’URL demandée.
"""
# J'importe la methode de la bibliothèque http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
# J'import json pour la convertion de données
import json

# On crée une classe héritée de BaseHTTPRequestHandler
# pour gérer les requêtes


class Api_test(BaseHTTPRequestHandler):
    """
    Classe héritée de BaseHTTPRequestHandler
    pour gérer des routes HTTP simples.

    Elle définit la méthode do_GET() pour répondre aux requêtes GET
    sur différentes URLs comme /, /data, /status et /info.
    """
    # Création methode pour gérer les requêtes GET
    def do_GET(self):
        """
        Gère les requêtes GET entrantes selon l’URL demandée.

        - "/"       : Renvoie un message d’accueil (texte brut)
        - "/data"   : Renvoie un objet JSON avec nom, âge et ville
        - "/status" : Renvoie "OK" (texte brut)
        - "/info"   : Renvoie des métadonnées de l’API (JSON)
        - autres    : Renvoie une erreur 404 (JSON)
        """
        # Je vérifie si l'url est /data
        # /hello, /trucMuche ont s'en fiche c'est pour test
        # par ce que en réalité ça ressemble à ça :
        # http://localhost:8000/hello
        if self.path == "/":
            # Si c'est bien /
            # Je renvoie le code status que tout s'est bien passé
            self.send_response(200)
            # J'ouvre un header
            # Je dis sous quel format je renvoie la réponse
            self.send_header("Content-type", "text/plain")
            # Je ferme le header
            self.end_headers()
            # Je crée le contenue de ma réponse
            # Je convertis ma réponse sous le bon format (json)
            self.wfile.write(b"Hello, this is a simple API!")
        # Je vérifie si l'url est "/"
        elif self.path == "/data":
            # Si c'est bien /hello
            # Je renvoie le code status que tout s'est bien passé
            self.send_response(200)
            # J'ouvre un header
            # Je dis sous quel format je renvoie la réponse
            self.send_header("Content-type", "application/json")
            # Je ferme le header
            self.end_headers()
            # Je crée le contenue de ma réponse
            # sous forme de dictionnaire python
            reponse = {"name": "John", "age": 30, "city": "New York"}
            # Je convertis ma réponse sous le bon format (json)
            self.wfile.write(json.dumps(reponse).encode("utf-8"))
        # Je vérifie si l'url est "/status"
        elif self.path == "/status":
            # Si c'est bien /status
            # Je renvoie le code status que tout s'est bien passé
            self.send_response(200)
            # J'ouvre un header
            # Je dis sous quel format je renvoie la réponse
            self.send_header("Content-type", "text/plain")
            # Je ferme le header
            self.end_headers()
            # Je crée le contenu de ma réponse
            # Je convertis ma réponse sous le bon format (json)
            self.wfile.write(b"OK")
        # Je vérifie si l'url est "/info"
        elif self.path == "/info":
            # Si c'est bien /info
            # Je renvoie le code status que tout s'est bien passé
            self.send_response(200)
            # J'ouvre un header
            # Je dis sous quel format je renvoie la réponse
            self.send_header("Content-type", "application/json")
            # Je ferme le header
            self.end_headers()
            # Je crée le contenue de ma réponse
            # sous forme de dictionnaire python
            reponse = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            # Je convertis ma réponse sous le bon format (json)
            self.wfile.write(json.dumps(reponse).encode("utf-8"))
        # Si ça ne marche pas et que je n'atteinds pas l'url
        else:
            # Je renvoie un code d'erreur
            self.send_response(404)
            # J'ouvre un header
            # Je dis sous quel format je renvoie la réponse
            self.send_header("Content-type", "text/plain")
            # Je ferme le header
            self.end_headers()
            # Je crée le contenu de ma réponse
            # Je convertis ma réponse sous le bon format (json)
            self.wfile.write("Endpoint not found".encode("utf-8"))


if __name__ == "__main__":
    # je crée une écoute sur toutes les adresses (/, /data, /status)
    server_address = ("", 8000)
    # Je fais run le serveur pour qu'il écoute et renvoie ma sous classe
    httpd = HTTPServer(server_address, Api_test)
    # Message de check si le serveur est actif
    print(f"\u26a1 Serveur d'API actif sur http://localhost:8000")
    # Je lance la boucle infinie de traitement des requêtes
    httpd.serve_forever()
