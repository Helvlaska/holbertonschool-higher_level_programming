-- Ecrire un script qui repertorie tout les enregistrements de la table
-- second_table de la BDD
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
