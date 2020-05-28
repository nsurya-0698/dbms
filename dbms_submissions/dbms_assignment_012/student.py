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
    
    @staticmethod
    def get(**kwargs):
        for k,v in kwargs.items():
            if k=="student_id" and v!=None:
                query=f'SELECT * FROM Student where student_id={v}'
            
            elif k=="name" and v!="":
                query=f'SELECT * FROM Student where name="{v}"'
                
            elif k=="age" and v!=-1:
                query=f'SELECT * FROM Student where age={v}'
            
            elif k=="score" and v!=-1:
                query=f'SELECT * FROM Student where score={v}'  
                
            elif k not in ["student_id","name","age","score"]:
                raise InvalidField
            
            ans=read_data(query)
            if len(ans)==0:
                raise DoesNotExist
                
            elif len(ans)>1:
                raise MultipleObjectsReturned
            else:
                b= Student(ans[0][1],ans[0][2],ans[0][3])
                b.student_id=ans[0][0]
                return b
                
    def save(self):
        import sqlite3
        connection=sqlite3.connect("students.sqlite3")
        crsr= connection.cursor()
        crsr.execute("PRAGMA foreign_keys=on;")
        if(self.student_id==None):
            sql_query='INSERT INTO Student(student_id,name,age,score) VALUES(Null,"{}",{},{})'.format(self.name,self.age,self.score)
            crsr.execute(sql_query)
            self.student_id=crsr.lastrowid
        else:
            sql_query='UPDATE Student SET name="{}",age={},score={} WHERE student_id={}'.format(self.name,self.age,self.score,self.student_id)
            crsr.execute(sql_query)
        connection.commit()
        connection.close()
        
    def delete(self):
        query=f'DELETE from Student where student_id={self.student_id}'
        write_data(query)
        
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
