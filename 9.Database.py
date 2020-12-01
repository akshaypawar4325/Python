#Example of Setting the database
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
v="insert into t1 values(%s,%s,%s,%s)"
val=[0,"akshay","appawar4435@gmail.com","appawar"]
cur.execute(v,val)
db.commit()

#===============================
'''
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
name=input("Enter name: ")
email=input("Enter email: ")
password=input("Enter password")
v="insert into t1 values(%s,%s,%s,%s)"
val=[0,name,email,password]
cur.execute(v,val)
db.commit()
'''
#===============================

'''
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
n=int(input("How many:"))
for i in range(n):
    name=input("Enter name: ")
    email=input("Enter email: ")
    password=input("Enter password")
    v="insert into t1 values(%s,%s,%s,%s)"
    val=[0,name,email,password]
    cur.execute(v,val)
db.commit()
'''
#===============================

'''
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
n=int(input("How many:"))
for i in range(n):
    name=input("Enter name: ")
    email=input("Enter email: ")
    password=input("Enter password")
    v="insert into t1 values(%s,%s,%s,%s)"
    val=[0,name,email,password]
    cur.execute(v,val)
db.commit()
'''

#===============================
'''
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
#v="select * from t1 where idt1=1";
v="select name from t1 where idt1=1";
cur.execute(v)
#data=cur.fetchall()
data=cur.fetchone()
print(data)
'''
#===============================

'''
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
#v="select * from t1 where idt1=1";
v="select name from t1 where idt1=%s";
val=[1]
cur.execute(v,val)
data=cur.fetchone()
print(data)
'''
#===============================

'''
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
v="update t1 set name=%s where idt1=%s";
val=["tejas",1]
cur.execute(v,val)
db.commit()
'''
#===============================

'''
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
v="update t1 set name=%s where idt1=%s";
val=["pawan",1]
val1=["rahul",2]
cur.execute(v,val)
cur.execute(v,val1)
db.commit()
'''
#===============================

'''
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
v="update t1 set name=%s,email=%s where idt1=%s";
val=["ram","ram@gmail.com",1]
val1=["lamkshman","lakshman@gmail.com",2]
cur.execute(v,val)
cur.execute(v,val1)
db.commit()
'''

