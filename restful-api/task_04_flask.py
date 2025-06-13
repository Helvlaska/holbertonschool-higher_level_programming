#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

# Je veux juste renvoyer un message
@app.route("/") 
def home(): 
    return "Welcome to the Flask API!"

# Je crée une nouvelle route /status
@app.route("/status")
def ok_status():
    return "OK"

# Je crée une nouvelle route /data
# elle doit renvoyer une liste de tous les noms d'users
@app.route("/data", methods=["GET"])
def get_users():
    # Je vérifie si la liste est vide
    if len(users) == 0:
        # Je retourne une liste vide 
        # et un code status pour dire que ça c'est bien passé
        return jsonify([]), 200
    # Si la liste contient des items
    else:
        # Je retourne la liste de user avec les keys (username)
        return jsonify(list(users.keys())), 200

@app.route("/users/<username>", methods=["GET"])
def search_user(username):
    # Je vérifie si le username est dans mon dictionnaire de users
    if username in users:
        # Si oui je retourne le dictionnaire de l'username
        return jsonify(users[username]), 200
    # sinon
    else:
        return jsonify({"error": "User not found"}), 404
    
# Je crée une nouvelle route /add_user
# elle doit ajouter un nouveau user au dictionnaire users
@app.route("/add_user", methods=["POST"])
def add_users():
    # Je récupère mes données entrées par l'utilisateur (curl,...)
    data = request.get_json()
    # Je vérifie que les données entrée ne sont pas vide ou sans erronées
    if not data or 'username' not in data:
        # Je retourne un message d'erreur et un code status
        return jsonify({"error": "Username is required"}), 400
    # Sinon je stock le username des données dans une variable
    username = data['username']
    # J'ajoute mes données récupérées dans le dictionnaire users
    # qui à pour clef le username
    users[username] = data
    # Je retourne en format json un message
    # et les données récupérées
    return jsonify({"message": "User added", "user": data}), 201
    
if __name__ == "__main__": 
    app.run(debug=True)