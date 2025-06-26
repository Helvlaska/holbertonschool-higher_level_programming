-- Sélectionnes les colonnes nécessaires (l'id et le nom de la ville, et le nom du pays de la ville)
SELECT cities.id, cities.name, states.name
-- Dans la table cities
FROM cities
-- Lie chaque ville à l'état correspondant
JOIN states ON cities.state_id = states.id
-- Trie les id des villes dans l'ordre croissant
ORDER BY cities.ID;
