class InvalidField(Exception):
    pass

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        self.student_id = None
    
    @staticmethod
    def filter(**kwargs):
        li=[]
        for i in kwargs.items():
            s=i[0].split("__")
            if s[0] not in ["student_id", "name", "age", "score"]:
                raise InvalidField
            
            if len(s)==1:
                formate=f'{i[0]}=="{i[1]}"'
            elif s[1] == "lt":
                formate=f'{s[0]}<{i[1]}'
            elif s[1] == "lte":
                formate=f'{s[0]}<={i[1]}'
            elif s[1] == "gt":
                formate=f'{s[0]}>{i[1]}'
            elif s[1] == "gte":
                formate=f'{s[0]}>={i[1]}'
            elif s[1] =="neq":
                formate=f'{s[0]}!="{i[1]}"'
            elif s[1] =="in":
                formate=f'{s[0]} in {tuple(i[1])}'
            elif s[1] =="contains": 
                formate=f'{s[0]} like "%{i[1]}%"'
            
            li.append(formate)
        m=" and ".join(li)
        return m
        
    @classmethod
    def avg(cls, field, **kwargs):
        if field not in ["student_id", "name", "age", "score"]:
            raise InvalidField
        if len(kwargs.items())==0:
            query=f'select avg({field}) from Student'
        else:
            a=Student.filter(**kwargs)
            query=f'select avg({field}) from Student where {a}'
        ans=read_data(query)
        return ans[0][0]
    
    @classmethod
    def min(cls, field, **kwargs):
        if field not in ["student_id", "name", "age", "score"]:
            raise InvalidField
        if len(kwargs.items())==0:
            query=f'select min({field}) from Student'
        else:
            a=Student.filter(**kwargs)
            query=f'select min({field}) from Student where {a}'
        ans=read_data(query)
        return ans[0][0]
        
    @classmethod
    def max(cls, field, **kwargs):
        if field not in ["student_id", "name", "age", "score"]:
            raise InvalidField
        if len(kwargs.items())==0:
            query=f'select max({field}) from Student'
        else:
            a=Student.filter(**kwargs)
            query=f'select max({field}) from Student where {a}'
        ans=read_data(query)
        return ans[0][0]
        
    @classmethod
    def sum(cls, field, **kwargs):
        if field not in ["student_id", "name", "age", "score"]:
            raise InvalidField
        if len(kwargs.items())==0:
            query=f'select sum({field}) from Student'
        else:
            a=Student.filter(**kwargs)
            query=f'select sum({field}) from Student where {a}'
        ans=read_data(query)
        return ans[0][0]
    
    @classmethod
    def count(cls, field=None, **kwargs):
        if field == None:
            query=f'select count(*) from Student'
        elif field not in ["student_id", "name", "age", "score"]:
            raise InvalidField
        elif len(kwargs.items())==0:
            query=f'select count({field}) from Student'
        else:
            a=Student.filter(**kwargs)
            query=f'select count({field}) from Student where {a}'
        ans=read_data(query)
        return ans[0][0]
    
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
