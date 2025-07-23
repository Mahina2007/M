"""
-- BASIC SELECT
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name;
SELECT column1 AS alias1, column2 AS alias2 FROM table_name
WHERE ;

-- FILTERING
SELECT * FROM table_name WHERE column1 = value;
SELECT * FROM table_name WHERE column1 > value;
SELECT * FROM table_name WHERE column1 < value;
SELECT * FROM table_name WHERE column1 >= value;
SELECT * FROM table_name WHERE column1 <= value;
SELECT * FROM table_name WHERE column1 <> value;
SELECT * FROM table_name WHERE condition1 AND condition2;
SELECT * FROM table_name WHERE condition1 OR condition2;
SELECT * FROM table_name WHERE NOT condition;
SELECT * FROM table_name WHERE column1 BETWEEN value1 AND value2;
SELECT * FROM table_name WHERE column1 IN (value1, value2, value3);
SELECT * FROM table_name WHERE column1 LIKE 'pattern%';
SELECT * FROM table_name WHERE column1 LIKE '%pattern';
SELECT * FROM table_name WHERE column1 LIKE '%pattern%';
SELECT * FROM table_name WHERE column1 LIKE '_pattern';
SELECT * FROM table_name WHERE column1 IS NULL;
SELECT * FROM table_name WHERE column1 IS NOT NULL;

-- SORTING AND LIMITING
SELECT * FROM table_name ORDER BY column1;
SELECT * FROM table_name ORDER BY column1 ASC;
SELECT * FROM table_name ORDER BY column1 DESC;
SELECT * FROM table_name ORDER BY column1, column2 DESC;
SELECT * FROM table_name LIMIT 10;
SELECT * FROM table_name LIMIT 10 OFFSET 20;

-- AGGREGATION
SELECT COUNT(*) FROM table_name;
SELECT AVG(column1) FROM table_name;
SELECT SUM(column1) FROM table_name;
SELECT MAX(column1) FROM table_name;
SELECT MIN(column1) FROM table_name;
SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
SELECT column1, AVG(column2) FROM table_name GROUP BY column1;
SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > 5;

-- DISTINCT
SELECT column1 FROM table_name;
SELECT COUNT(DISTINCT column1) FROM table_name;

-- SUBQUERIES
SELECT * FROM table1 WHERE column1 > (SELECT AVG(column1) FROM table1);
SELECT sub.avg_value FROM (SELECT AVG(column1) AS avg_value FROM table1) sub;
SELECT column1, (SELECT COUNT(*) FROM table2 WHERE table2.id = table1.id) AS count FROM table1;
SELECT * FROM table1 WHERE EXISTS (SELECT 1 FROM table2 WHERE table2.id = table1.id);


where
select name, age from users where age is not null;

and
or
is null / is not null
limit
offset
as
between
in
like

COUNT()
SUM()
AVG()
MIN()
MAX()

group by
having
order by desc

"""
