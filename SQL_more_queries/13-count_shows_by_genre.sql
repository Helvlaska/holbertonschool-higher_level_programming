-- Je sélectionnes les colonnes à afficher -ETAPE 4
-- Je crée un alias (AS) pour les noms des genres
-- Je dis que le résultat de COUNT aura un alias aussi (AS)
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
-- Je déclare ma table principale - ETAPE 1
-- Je veux afficher les genres -> j'utilise la table tv_genres
FROM tv_genres
--  Pour chaque genre, trouve toutes les lignes dans tv_show_genres où le genre_id correspond à cet id de genre - ETAPE 2
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Regroupe les selon les noms de genre -ETAPE 3
GROUP BY tv_genres.name
-- Trie les de façon à se qu'il s'affichent l'ordre décroissant - ETAPE 5
ORDER BY number_of_shows DESC;
