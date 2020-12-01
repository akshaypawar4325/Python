import pymysql as con
db=con.connect(host="localhost",user="root",password="root",database="bank")
cur=db.cursor()

option=0
while(option!=3):
    print("1.For Registration")
    print("2.For Login")
    print("3.For Exit")
    option=int(input("Choose option"))
    if(option==1):
        accName=input("Enter your name: ")
        accNo=int(input("Enter acc no: "))
        accPin=int(input("Enter acc pin:"))
        accBal=int(input("Enter acc balance: "))
        v1="insert into bank1 values(%s,%s,%s,%s,%s)"
        v2=[0,accName,accNo,accPin,accBal]
        cur.execute(v1,v2)
        db.commit()

    elif(option==2):
        regAcc=int(input("Enter Acc: "))
        regPin=int(input("Enter password: "))
        
        var1="select * from bank1 where accNumber=%s and accPin=%s "
        va1=[regAcc,regPin]
        cur.execute(var1,va1)
        data=cur.fetchall()
            
        if(len(data)>0):
            print("Your welcome! Login Successfull!!")
            option=0
            while(option!=3):
                print("1.for add money")
                print("2.for transfer money")
                print("3.for exit")
                option=int(input("Choose option: "))
                if(option==1):
                    m=int(input("Enter add money amount: "))
                    bal1="select bal from bank1 where accNumber=%s"
                    d=[regAcc]
                    cur.execute(bal1,d)
                    old=cur.fetchone()
                    c=int(old[0])+m
                    print(c)
                    q="update bank1 set bal=%s where accNumber=%s"
                    v=[c,regAcc]
                    cur.execute(q,v)
                    db.commit()
                    
                elif(option==2):
                    m=int(input("Enter transfer money amount: "))
                    bal1="select bal from bank1 where accNumber=%s"
                    d=[regAcc]
                    cur.execute(bal1,d)
                    old=cur.fetchone()
                    c=int(old[0])-m
                    print(c)
                    q="update bank1 set bal=%s where accNumber=%s"
                    v=[c,regAcc]
                    cur.execute(q,v)
                    db.commit()

                    p1=int(input("Enter transfer account no:"))
                    p2=int(input("Enter transfer account pin:"))
                    x="select * from bank1 where accNumber=%s and accPin=%s"
                    y=[p1,p2]
                    cur.execute(x,y)
                    data=cur.fetchall()
                    print(data)

                    bal1="select bal from bank1 where accNumber=%s"
                    d=[p1]
                    cur.execute(bal1,d)
                    old=cur.fetchone()
                    c=int(old[0])+m
                    print(c)
                    q="update bank1 set bal=%s where accNumber=%s"
                    v=[c,p1]
                    cur.execute(q,v)
                    db.commit()

                                        
                elif(option==3):
                    print("exit")

            
    elif(option==3):
        print("Exit")
