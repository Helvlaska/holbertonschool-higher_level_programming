#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Je dis que crée une application avec Flask
app = Flask(__name__)
# Je configure mon application avec token JWT (bibliothèque)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# J'initialise les systèmes d'authentification
# Pour l'authentification basique
auth = HTTPBasicAuth()
# Pour les tokens
jwt = JWTManager(app)

# Dictionnaire des utilisateurs avec mot de passe hashé
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Je crée une authentification basique
@auth.verify_password
def verify_username_password(username, password):
    # Je vérifie que le user existe
    if username in users:
        # Je récupère le mdp
        mot_de_passe = users[username]["password"]
        # Je le vérifie avec une methode de check
        verification = check_password_hash(mot_de_passe, password)
        # Je retourne un booleen selon le check
        return verification
    # Si le user n'existe pas return False
    return False

# Je récupère un login et un mdp passé par le user
@app.route("/basic-protected")
# Selon la réponse de l'authentification basique, j'acède à la fonction
@auth.login_required
def basic_protected():
    # Je retourne un message si l'authentification est réussie
    return "Basic Auth: Access Granted"

# Je crée une route pour que le user puisse accéder à son compte
@app.route("/login", methods=["POST"])
def login():
    # Je récupère les données JSON envoyées par le client
    data = request.get_json()
    # Je vérifie que le JSON contient bien username et password
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Donnez un username et un password"}), 400
    # Je récupère le username et le password
    username = data["username"]
    password = data["password"]

    # Je vérifie que l'utilisateur existe
    if username not in users:
        return jsonify({"error": "Identifiants invalides"}), 401

    # Je vérifie que le mot de passe est correct
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Mot de passe incorrect"}), 401

    # Je crée un token JWT avec l'identité du user
    # Le token contient l'identité de l'utilisateur (username)
    access_token = create_access_token(identity=username)
    # Je retourne le token au user
    return jsonify({"access_token": access_token}), 200

# Je crée une route protégée par le token
@app.route("/jwt-protected", methods=["GET"])
# Si pas de token, pas d'accès
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

# Je crée une route pour les utilisateurs avec le rôle admin
@app.route("/admin-only", methods=["GET"])
# Si pas de token, pas d'accès
@jwt_required()
def admin_only():
    # Je récupère le nom d'utilisateur depuis le token
    username = get_jwt_identity()
    # Je vérifie si l'utilisateur a bien un rôle admin
    if users[username]["role"] == "admin":
        return "Admin Access: Granted", 200
    else:
        return jsonify({"error": "Admin access required"}), 403

if __name__ == "__main__":
    app.run(debug=True)
