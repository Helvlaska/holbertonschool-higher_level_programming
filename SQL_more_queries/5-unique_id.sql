-- Créer une table unique_id sur le serveur
CREATE TABLE IF NOT EXISTS unique_id (
    -- l'id est un integer qui vaut par defaut 1 et il est unique
    id INT DEFAULT 1 UNIQUE,
    -- name est une string qui est composée au max de 256 caractères
    name VARCHAR(256)
);
