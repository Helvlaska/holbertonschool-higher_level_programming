#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)
from werkzeug.security import generate_password_hash, check_password_hash

# Je dis que crée une application avec Flask
app = Flask(__name__)
# J'initialise l'authentification basique
auth = HTTPBasicAuth()

# Je configure mon application avec token JWT (bibliothèque)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
# J'initialise l'authentification pour les tokens
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
    # Je récupère le username dans le dictionnaire users
    user = users.get(username)
    # Je vérifie si l'utilisateur existe et si le mot de passe est correct
    if user and check_password_hash(user['password'], password):
        # Si oui, je retourne l'utilisateur
        return user
    # Si l'utilisateur n'existe pas ou le mot de passe est incorrect
    return None


# Je récupère un login et un mdp passé par le user
@app.route("/basic-protected", methods=['GET'])
# Selon la réponse de l'authentification basique, j'acède à la fonction
@auth.login_required
def basic_protected():
    # Je retourne un message si l'authentification est réussie
    return "Basic Auth: Access Granted"


# Je crée une route pour que le user puisse accéder à son compte
@app.route("/login", methods=["POST"])
def login():
    # Je récupère les données entrées par l'utilisateur
    data = request.get_json()
    # Je stock le username et le mot de passe dans des variables
    username = data.get("username")
    password = data.get("password")
    # Je récupère l'utilisateur correspondant au username
    user = users.get(username)
    # Je vérifie si l'utilisateur existe et si le mot de passe est correct
    if user and check_password_hash(user['password'], password):
        # Si oui, je crée un token JWT avec le username
        # et le rôle de l'utilisateur
        access_token = create_access_token(
            identity={
                'username': username,
                'role': user["role"]
                }
        )
        # Je retourne le token en format json
        return jsonify(access_token=access_token)
    # Si l'utilisateur n'existe pas ou le mot de passe est incorrect
    # je retourne un message d'erreur
    return jsonify({"error": "Invalid credentials"}), 401


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
    user_name = get_jwt_identity()
    # Je vérifie si l'utilisateur a bien un rôle admin
    if user_name["role"] == "admin":
        return "Admin Access: Granted", 200
    else:
        return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
