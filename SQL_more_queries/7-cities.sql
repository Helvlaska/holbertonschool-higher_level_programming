-- Créer la BDD hbtn_0d_usa si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Utiliser cette BDD
USE hbtn_0d_usa;
-- Créer la table cities dans la BDD hbtn_0d_usa
CREATE TABLE IF NOT EXISTS cities (
    -- l'id est un integer auto généré, ne peu pas être null, et est une clé primaire
    id INT PRIMARY KEY AUTO_INCREMENT,
    -- state_id ne peu pas être null
    state_id INT NOT NULL,
    -- name est une string de max 256 caractères et ne peu pas être null
    name VARCHAR(256) NOT NULL,
    -- Déclaration clé étrangère:
    -- Import de la clé id de la table state
    FOREIGN KEY (state_id) REFERENCES states(id)
);

