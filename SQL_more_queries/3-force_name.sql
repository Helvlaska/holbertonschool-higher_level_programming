-- Crée la table force_name sur le serveur
-- Création de la table force_name si elles n'existe pas déjà
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
