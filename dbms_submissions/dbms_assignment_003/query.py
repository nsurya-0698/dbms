Q1 = '''select count(*) from movie where year==1991'''
Q2 = '''select min(rank) from movie'''
Q3 = '''select max(rank) from movie where year==2000'''
Q4 = '''select avg(rank) from movie where year == 2000'''
Q5 = '''select count(DISTINCT year) from movie'''
Q6 = '''select min(year), max(year) from movie'''