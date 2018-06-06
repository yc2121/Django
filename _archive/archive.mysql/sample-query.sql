USE world
;
/* QUERY 1 */ 
SELECT c.name, l.Language, l.Percentage
FROM country AS c, countrylanguage AS l 
WHERE c.code = l.CountryCode and l.Language='Slovene'
;
SELECT c.name, l.Language, l.Percentage
FROM country AS c
JOIN countrylanguage AS l
ON c.code=l.CountryCode and l.Language='Slovene'
;
/* QUERY 2 */
SELECT country.Name, COUNT(c.Name)
FROM city AS c, country
WHERE c.CountryCode = country.Code
GROUP BY country.Name
ORDER BY COUNT(c.Name) DESC
;
/* QUERY 3 */
SELECT c.Name, c.Population
FROM city AS c, country AS d
WHERE c.CountryCode = d.code and d.Name='Mexico' and c.Population > 500000
ORDER BY c.Population DESC
;
/* QUERY 4 */
SELECT l.Percentage, l.Language, c.Name
FROM country AS c, countrylanguage AS l
WHERE l.CountryCode = c.code
ORDER BY l.Percentage DESC
;
/* QUERY 5 */
SELECT c.Name /*, c.SurfaceArea, c.Population */
FROM country AS c
WHERE c.SurfaceArea < 501 and c.Population > 100000
;
/* QUERY 6 */
