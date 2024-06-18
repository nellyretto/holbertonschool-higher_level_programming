-- listing all cities on the databse in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;