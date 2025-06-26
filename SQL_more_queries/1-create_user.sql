-- Créer l'utilisateur user_0d_1 avec tous les privilèges
-- Crée l'utilisateur s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Accorde tous les privilèges à l'utilisateur sur toutes les bases et toutes les tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
