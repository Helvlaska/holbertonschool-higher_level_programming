-- Ecrire un script qui énumère le nombre d'enregistrements ayant le même
-- score dans la table second_table de la BDD
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
