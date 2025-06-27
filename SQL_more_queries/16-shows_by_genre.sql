-- Etape 4 - Sélectionne ce qu'on veut afficher
SELECT tv_shows.title, tv_genres.name
-- Etape 1 - Définir la table principale
FROM tv_shows
-- Etape 2 - Associer la table principale à la table de liaison
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Etape 3 - Associer la table de liaison à la table secondaire
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Etape 5 - Trier les résultats
ORDER BY tv_shows.title, tv_genres.name
