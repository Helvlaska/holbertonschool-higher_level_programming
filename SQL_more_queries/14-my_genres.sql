-- Étape 1 - Sélectionner ce qu'on veut afficher (le nom du genre)
SELECT tv_genres.name
-- Étape 2 - Définir la table principale
FROM tv_genres
-- Étape 3 - Associer la table principale à la table de liaison (tv_show_genres)
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Étape 4 - Associer la table de liaison à la table des shows
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Étape 5 - Filtrer uniquement sur les shows avec le titre 'Dexter'
WHERE tv_shows.title = 'Dexter'
-- Étape 6 - Trier les résultats par ordre alphabétique
ORDER BY tv_genres.name;
