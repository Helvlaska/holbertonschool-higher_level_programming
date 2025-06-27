-- Etape 4 - sélectionner ce qu'ont veux afficher
SELECT tv_genres.name
-- Etape 1 - ma table principale
FROM tv_genres
-- Etape 3 - filtrer ce que l'ont veut
WHERE tv_shows.title = 'Dexter'
-- Etape 2.1 - associer la table principale à la secondaire
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Etape 2.2 - associer la table secondaire à la table tertiaire
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
-- Etape 5 - Dans quel ordre ?
ORDER BY tv_genres.name;
