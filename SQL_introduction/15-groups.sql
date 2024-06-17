-- listing number of records with the same score in the second table
SELECT score, COUNT(*)
as number FROM second_table
GROUP BY score
ORDER BY number DESC;