import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="h1")
cur=db.cursor()
option=0
while(option!=5):
    print("1.add table")
    print("2.show table")
    print("3.update table")
    print("4.delete table")
    print("5.exit")
    option=int(input("Choose option: "))
    if(option==1):
        name=input("Enter name: ")
        email=input("Enter email: ")
        password=input("Enter password: ")
        v="insert into t1 values(%s,%s,%s,%s)"
        val=[0,name,email,password]
        cur.execute(v,val)
        db.commit()
    elif(option==2):
        #id1=int(input("Enter id:"))
        v="select * from t1"
        #val=[id1]
        cur.execute(v)
        data=cur.fetchall()
        print(data)
    elif(option==3):
        id1=int(input("Enter id:"))
        name=input("column name:")
        v="update t1 set name=%s where idt1=%s"
        val=[name,id1]
        cur.execute(v,val)
        db.commit()
    elif(option==4):
        id1=int(input("Enter id:"))
        v="delete from t1 where idt1=%s"
        val=[id1]
        cur.execute(v,val)
        db.commit()
    elif(option==5):
        print("exit")
