-- Sélectionnes les colonnes nécessaires
SELECT tv_shows.title, tv_show_genres.genre_id
-- De la table tv_shows
FROM tv_shows
-- Chercher les corélations entre les deux tables
-- JOIN <table secondaire> ON <quoi faire avec la table actuelle>
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Liste ordonnées par tv_shows.title et tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
