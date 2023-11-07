import pets_db
from question4 import sql_pets_owned_by_nobody, sql_only_owned_by_bessie, sql_pets_older_than_owner

# Part 4.A: Select the pets that are owned by nobody.
sql_pets_owned_by_nobody = """
SELECT a.name, a.species, a.age
FROM animals a
LEFT JOIN people_animals pa ON a.animal_id = pa.pet_id
WHERE pa.owner_id IS NULL;
"""

# Part 4.B: Select how many pets are older than their owners.
sql_pets_older_than_owner = """
SELECT COUNT(*) as count
FROM animals a
JOIN people_animals pa ON a.animal_id = pa.pet_id
JOIN people p ON pa.owner_id = p.person_id
WHERE a.age > p.age;
"""

# Part 4.C: Select the pets that are owned by Bessie and nobody else.
sql_only_owned_by_bessie = """
SELECT p.name, a.name, a.species
FROM animals a
JOIN people_animals pa ON a.animal_id = pa.pet_id
JOIN people p ON pa.owner_id = p.person_id
WHERE p.name = 'bessie'
AND NOT EXISTS (
    SELECT 1
    FROM people_animals pa2
    WHERE pa2.pet_id = a.animal_id AND pa2.owner_id <> p.person_id
);
"""
