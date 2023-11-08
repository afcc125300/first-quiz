import pets_db as pets_db
from question5 import sql_create_favorite_foods, sql_alter_tables_with_favorite_food, sql_select_all_vegetarian_pets

CREATE TABLE favorite_foods (
  food_id integer,
  name text,
  vegetarian integer
);


ALTER TABLE animals
ADD COLUMN favorite_food_id integer;

ALTER TABLE people
ADD COLUMN favorite_food_id integer;


SELECT a.name AS pet_name, f.name AS food_name
FROM animals AS a
JOIN favorite_foods AS f ON a.favorite_food_id = f.food_id
WHERE f.vegetarian = 1;
