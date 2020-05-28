Q1 = '''SELECT count(id) FROM movie WHERE year < 2000'''
Q2 = '''SELECT avg(rank) FROM movie WHERE year = 1991'''
Q3 = '''SELECT min(rank) FROM movie WHERE year = 1991'''
Q4 = '''SELECT fname, lname FROM actor INNER JOIN cast ON id =  pid where mid = 27'''
Q5 = '''SELECT count(mid) FROM cast LEFT OUTER JOIN actor 
           ON id = pid WHERE fname = "Jon" AND lname = "Dough"'''
Q6 = '''SELECT name FROM movie WHERE year BETWEEN 2003 and 2006 AND name LIKE "Young Latin Girls%"'''
Q7 = '''SELECT fname,lname FROM ((movie inner join moviedirector on `movie`.id = `moviedirector`.mid) inner join director on `moviedirector`.did = `director`.id) where name LIKE "Star Trek%"'''
'''Q8'''
Q9 ='''SELECT fname , lname FROM director inner join moviedirector ON `director`.id=did inner join movie on `movie`.id = mid where year=2001 GROUP BY did HAVING COUNT(mid)>=4 order by fname ASC, lname DESC'''
Q10 = '''SELECT  DISTINCT gender , COUNT(id) FROM actor GROUP BY gender ORDER BY gender ASC'''
Q11 = ''' SELECT DISTINCT m.name, n.name, m.rank, m.year FROM movie m inner join movie n on m.name != n.name and `m`.rank = `n`.rank and `m`.year = `n`.year order by m.name ASC limit 100'''
Q12 = '''SELECT fname ,year ,avg(rank) FROM ((actor inner join cast on `actor`.id =`cast`.pid) inner join movie on mid = `movie`.id) group by year, `actor`.id  order by fname ASC, year DESC limit 100''' 
Q13 = '''SELECT `actor`.fname,`director`.id, AVG(rank) as score, FROM ((((actor inner join cast on `actor`.id = `cast`.pid) inner join movie on `movie`.id = `cast`.mid) inner join moviedirector ON `moviedirector`.mid = `cast`.mid) inner join director on `moviedirector`.did = `director`.id) GROUP BY `actor`.id, `director`.id haveing count(`movie`.id) >= 5 ORDER BY score DESC, `director`.id ASC, `actor`.id DESC
LIMIT 100'''