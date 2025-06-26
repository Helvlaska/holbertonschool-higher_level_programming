-- Récupère l'id et le nom des villes
SELECT id, name FROM cities
-- Seulement celles qui sont liées à l'id de la californie
WHERE state_id = (
    -- Récupère l'id de la californie
    SELECT id FROM states WHERE name = 'California'
)
-- Dans l'ordre croissant de l'id des villes
ORDER BY id;
