-- Ecrire un script qui repertorie tous les privilèges des users MySQL
-- Liste les utilisateurs MySQL
SELECT user, host FROM mysql.user;
-- Affiche les privilèges de user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- Affiche les privilèges de user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
