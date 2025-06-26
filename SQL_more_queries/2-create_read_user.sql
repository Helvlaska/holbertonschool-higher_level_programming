-- Créer une la BDD hbtn_0d_2 et le user_0d_2
-- Crée a BDD si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Crée l'utilisateur s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Accorde le privilège SELECT à l'utilisateur sur la BDD hbtn_0d_2
GRANT SELECT PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
