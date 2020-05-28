Q1 = '''select pid as actor_id, count(mid) as no_of_movie from cast group by pid'''
Q2 = '''SELECT year, count(id) AS count FROM movie 
        GROUP BY year ORDER BY year ASC'''
Q3 = '''SELECT year, AVG(rank) AS avg_rank FROM movie
       GROUP BY year HAVING count(id) > 10 ORDER BY year DESC'''
Q4 = '''SELECT year, MAX(rank) AS avg_rank FROM movie
        GROUP BY year ORDER BY year ASC'''
Q5 = '''SELECT rank, count(id) as no_of_movie FROM movie
        where name like "a%" GROUP BY rank'''