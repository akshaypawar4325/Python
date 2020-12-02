from tkinter import *
#def login():
    

#def registration():


    
window=Tk()
window.geometry("400x400+30+30")
window.configure(background="magenta2")
window.title("Login Form")


l1=Label(window,text="USERNAME:",bg="magenta2",font=("Century Schoolbook",20)).pack()
e1=Entry(window,font=("Century Schoolbook",20),bg="bisque2").pack()
l3=Label(text="")
l2=Label(window,text="PASSWORD:",bg="magenta2",font=("Century Schoolbook",20)).pack()
e2=Entry(window,font=("Century Schoolbook",20),bg="bisque2").pack()

b1=Button(window,text="Cancel",font=("Century Schoolbook",20),bg="red")
b1.pack()
b2=Button(window,text="Login",font=("Century Schoolbook",20),bg="light blue")
b2.pack()

window.mainloop()
