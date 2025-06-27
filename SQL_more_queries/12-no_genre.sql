-- Sélectionner les colonnes nécessaires
SELECT tv_shows.title, tv_show_genres.genre_id
-- Sélectionner la table
FROM tv_shows
-- Chercher toutes les corélations entre les tables même celles qui valent NULL avec LEFT JOIN
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Trie cette recherche en gardant que celles qui valent NULL
WHERE tv_show_genres.show_id IS NULL
-- Retourne une liste croissante et ordonnée par tv_shows.title et tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
