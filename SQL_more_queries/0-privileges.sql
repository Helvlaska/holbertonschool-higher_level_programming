-- Ecrire un script qui repertorie tous les privilèges des users MySQL
SELECT user, host FROM mysql.user;
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
