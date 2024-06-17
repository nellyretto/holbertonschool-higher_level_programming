-- listing all records from the secodn table in descsending order avoiding 0 name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;