-- Import in hbtn_0c_0 database this table dump
-- Displays avg temp in July and August
SELECT city, AVG(value) AS avg_tnp FROM temperatures WHERE month=7 or month=8 GROUP BY city ORDER BY avg_tmp DESC LIMIT 3;
