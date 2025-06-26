-- Créer la BDD hbtn_0d_usa, vérifie si elle existe déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Utiliser la database
USE hbtn_0d_usa;
-- Créer une table states, vérifie si elle existe déjà
CREATE TABLE IF NOT EXISTS states (
    -- l'id est un integer, auto généré, ne peu pas être null, et est une clé primaire
    id INT PRIMARY KEY AUTO_INCREMENT,
    -- name ne peu pas être null, est une string, de max 256 caractères
    name VARCHAR(256) NOT NULL
);
