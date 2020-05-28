Q1 = '''SELECT D.ID, D.FNAME 
        FROM DIRECTOR AS D 
        WHERE NOT EXISTS (SELEcT DID FROM MOVIEDIRECTOR MD JOIN MOVIE ON `MOVIE`.ID = MD.MID WHERE MD.DID = D.ID AND MOVIE.YEAR < 2000)
        AND EXISTS (SELEcT DID FROM MOVIEDIRECTOR MD JOIN MOVIE ON `MOVIE`.ID = MD.MID WHERE MD.DID = D.ID AND MOVIE.YEAR > 2000)
        ORDER BY D.ID;'''
Q3 = '''select * 
        from actor as a 
        where NOT EXISTS(select c.pid from cast as c INNER JOIN movie as m on c.mid = m.id WHERE c.pid = a.id and m.year BETWEEN 1990 and 2000) 
        ORDER BY a.id DESC LIMIT 100;'''
Q2='''select fname,(select name from movie inner join moviedirector on `movie`.id=`moviedirector`.mid inner join director on `moviedirector`.did=`director`.id where `director`.id=`d`.id order by rank desc,name asc limit 1) as name from director as d limit 100;'''