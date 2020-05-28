class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        self.student_id = None
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
    
    @staticmethod
    def get(**kwargs):
        for k,v in kwargs.items():
             if k not in ["student_id", "name", "age", "score"]:
                raise InvalidField
             if k=="name":
                query1=(f'select * from student where {k} == "{v}"')
             else:
                query1=(f'select * from student where {k}=={v}')
           
             ans=read_data(query1)
             if len(ans)==0:
                raise DoesNotExist
                
             elif len(ans)>1:
                raise MultipleObjectsReturned
             else:
                b= Student(ans[0][1],ans[0][2],ans[0][3])
                b.student_id=ans[0][0]
                return b
    
    @classmethod
    def filter(cls, **kwargs):

        for k,v in kwargs.items():
            key = k
            value = v
            s=key.split("__")
            if s[0] not in ("student_id", "name", "age", "score"):
                raise InvalidField
            
            if key in ("student_id", "name", "age", "score"):
                query1=read_data(f'select * from Student where {key} = "{value}"')
                
            elif s[1] == "lt":
                query1=read_data(f'select * from Student where {s[0]}<"{value}"')
            elif s[1] == "lte":
                query1 = read_data(f'select * from Student where {s[0]}<="{value}"')
            elif s[1] == "gt":
                query1=read_data(f'select * from Student where {s[0]} > "{value}"')
            elif s[1] == "gte":
                query1=read_data(f'select * from Student where {s[0]} >= "{value}"')
            elif s[1] =="neq":
                query1=read_data(f'select * from Student where {s[0]} != "{value}"')
            elif s[1] =="in":
                value = tuple(value)
                query1=read_data(f'select * from Student where {s[0]} in {value}')
            elif s[1] =="contains": 
                query1=read_data(f'select * from Student where {s[0]} like "%{value}%"')
                    
            if len(query1) == 0:
                return []
            else:
                li=[]
                for i in query1:
                    qc = Student(i[1], i[2], i[3])
                    qc.student_id=i[0]
                    li.append(qc)
        return li
        
                
    def save(self):
        import sqlite3
        connection=sqlite3.connect("selected_students.sqlite3")
        crsr= connection.cursor()
        crsr.execute("PRAGMA foreign_keys=on;")
        if(self.student_id==None):
            sql_query='INSERT INTO Student(student_id,name,age,score) VALUES(Null,"{}",{},{})'.format(self.name,self.age,self.score)
            crsr.execute(sql_query)
            self.student_id=crsr.lastrowid
        else:
            sql_query=f'INSERT or replace INTO Student(student_id, name, age, score) values({self.student_id}, "{self.name}", {self.age}, {self.score})'
            crsr.execute(sql_query)
            
        connection.commit()
        connection.close()
        
    def delete(self):
        query=f'DELETE from Student where student_id={self.student_id}'
        write_data(query)
        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
