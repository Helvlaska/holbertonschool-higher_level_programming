-- Etape 5 - sélectionne ce qu'on veut afficher
SELECT tv_shows.title
-- Etape 1 - Définir la table principale
FROM tv_shows
-- Etape 2 - Associer la table principale à la table de liaison
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Etape 3 - Associer la table de liaison à la troisième table
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Etape 4 - Filtrer uniquement sur le genre 'Comedy'
WHERE tv_genres.name = 'Comedy'
-- Etape 6 - trier les résultats par ordre alphabétique
ORDER BY tv_shows.title
