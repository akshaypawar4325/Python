import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="banks")
cur=db.cursor()

option=0
while(option!=3):
    print("1.For Registration")
    print("2.For Login")
    print("3.For Exit")
    option=int(input("Choose option"))
    if(option==1):
        a1=input("Enter your name: ")
        a2=int(input("Enter acc no: "))
        a3=int(input("Enter acc pin:"))
        a4=int(input("Enter acc balance: "))
        v1="insert into bank1 values(%s,%s,%s,%s,%s)"
        v2=[0,a1,a2,a3,a4];
        cur.execute(v1,v2)
        
        
        type1="credit"
        u1="insert into passbook values(%s,%s,%s,%s,%s)"
        u2=[0,a2,a2,a4,type1]
        cur.execute(u1,u2)
        db.commit()

    elif(option==2):
        regAcc=int(input("Enter Acc: "))
        regPin=int(input("Enter password: "))
        
        var1="select * from bank1 where accno=%s and password=%s"
        va1=[regAcc,regPin]
        cur.execute(var1,va1)
        data=cur.fetchall()
            
        if(len(data)>0):
            print("Your welcome! Login Successfull!!")
            option=0
            while(option!=3):
                print("1.for add money")
                print("2.for transfer money")
                print("3.Print passbook")
                option=int(input("Choose option: "))
                if(option==1):
                    m=int(input("Enter add money amount: "))
                    bal1="select balance from bank1 where accno=%s"
                    d=[regAcc]
                    cur.execute(bal1,d)
                    old=cur.fetchone()
                    c=int(old[0])+m
                    print(c)
                    q="update bank1 set balance=%s where accno=%s"
                    v=[c,regAcc]
                    cur.execute(q,v)
                   
                    
                    type1="credit"
                    q1="insert into passbook values(%s,%s,%s,%s,%s)"
                    q2=[0,regAcc,regAcc,m,type1]
                    cur.execute(q1,q2)
                    db.commit()
                    
                elif(option==2):
                    m=int(input("Enter transfer money amount: "))
                    bal1="select balance from bank1 where accno=%s"
                    d=[regAcc]
                    cur.execute(bal1,d)
                    old=cur.fetchone()
                    c=int(old[0])-m
                    print(c)
                    q="update bank1 set balance=%s where accno=%s"
                    v=[c,regAcc]
                    cur.execute(q,v)
                    db.commit()

                    p1=int(input("Enter transfer account no:"))
                    p2=int(input("Enter transfer account pin:"))
                    x="select * from bank1 where accno=%s and password=%s"
                    y=[p1,p2]
                    cur.execute(x,y)
                    data=cur.fetchall()
                    print(data)

                    
                    bal1="select balance from bank1 where accno=%s"
                    d=[p1]
                    cur.execute(bal1,d)
                    old=cur.fetchone()
                    c=int(old[0])+m
                    print(c)
                    q="update bank1 set balance=%s where accno=%s"
                    v=[c,p1]
                    cur.execute(q,v)
                    
                    
                    type1="credit"
                    type2="debit"

                    o1="select amount from passbook where fromacc=%s"
                    o2=[regAcc]
                    cur.execute(o1,o2)
                    old3=cur.fetchone()
                    c3=int(old3[0])-m                  
                    n1="insert into passbook values(%s,%s,%s,%s,%s)"
                    n2=[0,regAcc,p1,c3,type2]
                    cur.execute(n1,n2)
                    

                    o3="select amount from passbook where toacc=%s"
                    o4=[p1]
                    cur.execute(o3,o4)
                    old4=cur.fetchone()
                    c4=int(old[0])+m
                    n3="insert into passbook values(%s,%s,%s,%s,%s)"
                    n4=[0,regAcc,p1,c4,type1]
                    cur.execute(n3,n4)
                    db.commit()
                    
                                        
                elif(option==3):
                    
                    g1="select * from passbook where fromacc=%s"
                    g2=[regAcc]
                    cur.execute(g1,g2)
                    bank=cur.fetchall()
                    print(bank)
                    
                        
    elif(option==3):
        print("Exit")
