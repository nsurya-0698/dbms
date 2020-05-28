Q1 = '''select `actor`.id, `actor`.fname, `actor`.lname, `actor`.gender from (actor inner join cast on `actor`.id = `cast`.pid ) inner join movie on `cast`.mid = `movie`.id where `movie`.name like "Annie%";'''
Q2 = '''select m.id, m.name, m.rank, m.year 
        from (director  as d inner join moviedirector as md on d.id = md.did) inner join movie as m on md.mid = m.id 
        where d.fname like "Biff%" and d.lname like "Malibu%"  and m.year in (1999, 1994, 2003) order by rank DESC, year ASC'''
Q3 = '''select m.year, count(id) as no_of_movies 
        from movie as m 
        group by year 
        having avg(rank) > (select avg(rank) from movie) 
        order by year ASC;'''
Q4 = '''select m.id, m.name, m.year, m.rank 

        from movie as m where m.year = 2001 and m.rank < (select avg(rank) from movie where year =2001) 

         order by m.rank DESC limit 10; '''
Q5 = ''''''
Q6 = '''select distinct `actor`.id from actor inner join cast on `actor`.id = `cast`.pid inner join movie on `movie`.id = `cast`.mid group by `actor`.id, `movie`.id having count(distinct role)> 1  order by `actor`.id ASC limit 100;'''

Q7 = '''select fname, count(fname) from director group by fname having count(fname) > 1;'''

Q8 = '''SELECT `director`.id,fname,lname FROM director WHERE 
        EXISTS(SELECT * FROM moviedirector JOIN cast ON `moviedirector`.mid = `cast`.mid WHERE `moviedirector`.did = `director`.id GROUP BY did,`moviedirector`.mid HAVING COUNT(DISTINCT pid)>=100)  
        AND NOT EXISTS (SELECT * FROM moviedirector JOIN cast ON `moviedirector`.mid = `cast`.mid WHERE `moviedirector`.did = `director`.id GROUP BY did,`moviedirector`.mid HAVING COUNT(DISTINCT pid)<100)'''