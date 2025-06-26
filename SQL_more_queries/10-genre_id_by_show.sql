-- Se placer dans la BDD hbtn_0d_tvshows
USE hbtn_0d_tvshows;
-- Sélectionnes les colonnes nécessaires
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows
-- montre tous les genres, avec ou sans correspondance dans la table d’association
-- JOIN <table secondaire> ON <quoi faire avec la table actuelle>
JOIN tv_shows_genres ON tv_shows.id =  tv_shows_genres.show_id
-- Liste ordonnée par tv_shows.id
ORDER BY tv_shows.id
