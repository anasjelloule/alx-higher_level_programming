-- Lists all with second_table with a score >= 10.
-- ordered by descending score.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
