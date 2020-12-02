from tkinter import *
from tkinter import messagebox
import pymysql as con
db=con.connect(host="localhost",user="root",password="root",db="bank2")
cur=db.cursor()
#Login form========================================================================================================
def dbAddMoney():
    e1input=e1.get()
    e11input=e11.get()
    bal1="select balance from bank where accno=%s"
    bal2=[e1input]
    cur.execute(bal1,bal2)
    old=cur.fetchone()
    
    c=int(old[0])+int(e11input)

    q="update bank set balance=%s where accno=%s"
    v=[c,e1input]
    cur.execute(q,v)
    db.commit()

    #passbook addmoney entry
    
    type1="Credit"
    c1="insert into passbook values(%s,%s,%s,%s,%s)"
    c2=[0,e1input,e1input,c,type1]
    cur.execute(c1,c2)
    db.commit()
    
def dbTransferMoney():
    e21input=e21.get()
    ae1input=ae1.get()
    ae2input=ae2.get()
    e1input=e1.get()

    bal1="select balance from bank where accno=%s"
    d=[e1input]
    cur.execute(bal1,d)
    old=cur.fetchone()
    c=int(old[0])-int(e21input)
    
    q="update bank set balance=%s where accno=%s"
    v=[c,e1input]
    cur.execute(q,v)
    db.commit()

    x="select * from bank where accno=%s and password=%s"
    y=[ae1input,ae2input]
    cur.execute(x,y)
    data=cur.fetchall()
    

    bal1="select balance from bank where accno=%s"
    d=[e1input]
    cur.execute(bal1,d)
    old=cur.fetchone()
    
    c=int(old[0])+int(e21input)
    
    q="update bank set balance=%s where accno=%s"
    v=[c,ae1input]
    cur.execute(q,v)
    
    #passbook transfer money
    type1="credit"
    type2="debit"

    o1="select amount from passbook where fromacc=%s"
    o2=[e1input]
    cur.execute(o1,o2)
    old3=cur.fetchone()
    c3=int(old3[0])-int(e21input)                  
    n1="insert into passbook values(%s,%s,%s,%s,%s)"
    n2=[0,e1input,ae1input,c3,type2]
    cur.execute(n1,n2)
    db.commit()
    

    o3="select amount from passbook where toacc=%s"
    o4=[ae1input]
    cur.execute(o3,o4)
    old4=cur.fetchone()
    c4=int(old[0])+int(e21input)
    n3="insert into passbook values(%s,%s,%s,%s,%s)"
    n4=[0,e1input,ae1input,c4,type1]
    cur.execute(n3,n4)
    db.commit()
    

#def dbPassbook():
    
def addmoney():
    global A
    global e11
    A=Toplevel(W)
    A.geometry("600x300+120+120")
    A.configure(background="OliveDrab1")
    A.title("Transaction options")
    Label(A,bg="OliveDrab1").pack()
    l11=Label(A,text="How Many amount you want to add: ",font=("century",15),bg="OliveDrab1")
    l11.pack()
    e11=Entry(A,font=("century",15))
    e11.pack()
    Label(A,bg="OliveDrab1").pack()
    b11=Button(A,text="Add Money",font=("century",15),bg="spring green",command=dbAddMoney)
    b11.pack()
def transfermoney():
    global B
    global e21,ae1,ae2
    B=Toplevel(W)
    B.geometry("600x300+120+120")
    B.configure(background="OliveDrab1")
    B.title("Transaction options")
    
    l21=Label(B,text="Transfer Money amount",font=("century",15),bg="OliveDrab1")
    l21.pack()
    e21=Entry(B,font=("century",15))
    e21.pack()

    a1=Label(B,text="Another acc no",font=("century",15),bg="OliveDrab1")
    a1.pack()
    ae1=Entry(B,font=("century",15))
    ae1.pack()

    a2=Label(B,text="Another acc password",font=("century",15),bg="OliveDrab1")
    a2.pack()
    ae2=Entry(B,font=("century",15))
    ae2.pack()
    
    b21=Button(B,text="Transfer Money",font=("century",15),bg="spring green",command=dbTransferMoney)
    b21.pack()
    
def passbook():
    global C
    C=Toplevel(W)
    C.geometry("600x300+120+120")
    C.configure(background="OliveDrab1")
    C.title("Transaction options")

    label11="select fromacc from passbook where fromacc=%s"
    label12=[e1input]
    cur.execute(label11,label12)
    old1=cur.fetchone()
    label1=Label(C,text=old1,font=("century",15),bg="OliveDrab1")
    label1.pack()
    
    label11="select toacc from passbook where fromacc=%s"
    label12=[e1input]
    cur.execute(label11,label12)
    old1=cur.fetchone()
    label2=Label(C,text=old1,font=("century",15),bg="OliveDrab1")
    label2.pack()
    
    label11="select amount from passbook where fromacc=%s"
    label12=[e1input]
    cur.execute(label11,label12)
    old1=cur.fetchone()
    label3=Label(C,text=old1,font=("century",15),bg="OliveDrab1")
    label3.pack()
    
    label11="select type from passbook where fromacc=%s"
    label12=[e1input]
    cur.execute(label11,label12)
    old1=cur.fetchone()
    label4=Label(C,text=old1,font=("century",15),bg="OliveDrab1")
    label4.pack()
def dblogin():
    global W,e1input
    e1input=e1.get()
    e2input=e2.get()

    e11="select * from bank where accno=%s and password=%s"
    e12=[e1input,e2input]
    cur.execute(e11,e12)
    data=cur.fetchall()
    if(len(data)>0):
        messagebox.showinfo("Login info","Your welcome! Login successfully!!")  

        W=Toplevel(T)
        W.geometry("600x300+120+120")
        W.configure(background="OliveDrab1")
        W.title("Transaction options")

        b1=Button(W,text="Add Money",bg="gold",font=("century",15),command=addmoney)
        b1.pack()
        Label(W,bg="OliveDrab1").pack()
        b2=Button(W,text="Transfer Money",bg="cyan2",font=("century",15),command=transfermoney)
        b2.pack()
        Label(W,bg="OliveDrab1").pack()
        b3=Button(W,text="Passbook",bg="medium purple",font=("century",15),command=passbook)
        b3.pack()
        
    else:
        messagebox.showinfo("Login info","Sorry! Login failed!!")

def login():
    global T
    global e1,e2
    T=Toplevel(window)
    T.geometry("600x300+120+120")
    T.configure(background="LightSteelBlue1")

    l1=Label(T,text="Account No",bg="LightSteelBlue1",font=("century",15))
    l1.pack()
    e1=Entry(T,font=("century",15))
    e1.pack()

    l2=Label(T,text="Pin Number",bg="LightSteelBlue1",font=("century",15))
    l2.pack()
    e2=Entry(T,font=("century",15),show="*")
    e2.pack()
    Label(T,bg="LightSteelBlue1").pack()
    button=Button(T,text="Login",font=("Arial Black",10),command=dblogin)
    button.pack()

#Registration form=================================================================================================
def dbregister():
    e1input=e1.get()
    e2input=e2.get()
    e3input=e3.get()
    e4input=e4.get()

    e11="insert into bank values(%s,%s,%s,%s,%s)"
    e12=[0,e1input,e2input,e3input,e4input]
    cur.execute(e11,e12)
    db.commit()

def register():
    global e1,e2,e3,e4
    T=Toplevel(window)
    T.geometry("600x600+120+120")
    T.configure(background="LightSteelBlue1")

    l1=Label(T,text="Account holder",bg="LightSteelBlue1",font=("century",15))
    l1.pack()
    e1=Entry(T,font=("century",15))
    e1.pack()

    
    l2=Label(T,text="Account Number",bg="LightSteelBlue1",font=("century",15))
    l2.pack()
    e2=Entry(T,font=("century",15))
    e2.pack()

    l3=Label(T,text="Account Pin",bg="LightSteelBlue1",font=("century",15))
    l3.pack()
    e3=Entry(T,font=("century",15))
    e3.pack()

    l4=Label(T,text="Account Balance",bg="LightSteelBlue1",font=("century",15))
    l4.pack()
    e4=Entry(T,font=("century",15))
    e4.pack()
    
    Label(T,bg="LightSteelBlue1").pack()
    button=Button(T,text="Register",font=("Arial Black",10),command=dbregister)
    button.pack()
    




#Window============================================================================================================
window=Tk()
window.geometry("600x300+120+120")
window.configure(background="burlywood1")
window.title("Form")

Label(window,bg="burlywood1").pack()

label1=Label(window,text="please select the below option ",bg="DarkOrange1",font=("arial",10))
label1.pack()

Label(window,bg="burlywood1").pack()

button1=Button(window,text="Login",width=30,height=2,font=("arial",10),bg="LightskyBlue1",command=login)
button1.pack()

Label(window,bg="burlywood1").pack()

button2=Button(window,text="Register",width=30,height=2,font=("arial",10),bg="khaki1",command=register)
button2.pack()

window.mainloop()
