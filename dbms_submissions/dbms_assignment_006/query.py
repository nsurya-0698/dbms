Q1 = '''SELECT fname, lname FROM actor INNER JOIN cast ON id =  pid where mid = 12148'''
Q2 = '''SELECT count(mid) FROM cast LEFT OUTER JOIN actor 
           ON id = pid WHERE fname = "Harrison (I)" AND lname = "Ford"'''
Q3 = '''SELECT DISTINCT pid FROM cast INNER JOIN movie ON id = mid WHERE name LIKE "Young Latin Girls%"'''
Q4 = '''SELECT count(DISTINCT pid) FROM movie INNER JOIN cast ON mid = id WHERE year BETWEEN 1990 AND 2000'''