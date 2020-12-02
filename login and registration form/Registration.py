from tkinter import *
window=Tk()
window.title("Registration form")
window.geometry("400x600+30+30")
window.configure(background="gray24")
#window.iconbitmap("1.ico")


l1=Label(window,text="First Name:",font=("Century Schoolbook",15),bg="gray24",fg="snow").pack()
e1=Entry(window,font=("Century Schoolbook",15),bg="gray79",fg="gray3").pack()
l2=Label(window,text="Last Name:",font=("Century Schoolbook",15),bg="gray24",fg="snow").pack()
e2=Entry(window,font=("Century Schoolbook",15),bg="gray79",fg="gray3").pack()
l3=Label(window,text="Username:",font=("Century Schoolbook",15),bg="gray24",fg="snow").pack()
e3=Entry(window,font=("Century Schoolbook",15),bg="gray79",fg="gray3").pack()
l4=Label(window,text="Password:",font=("Century Schoolbook",15),bg="gray24",fg="snow").pack()
e4=Entry(window,font=("Century Schoolbook",15),bg="gray79",fg="gray3").pack()
l5=Label(window,text="Re-Password:",font=("Century Schoolbook",15),bg="gray24",fg="snow").pack()
e5=Entry(window,font=("Century Schoolbook",15),bg="gray79",fg="gray3").pack()
l6=Label(window,text="DOB:",font=("Century Schoolbook",15),bg="gray24",fg="snow").pack()
e6=Entry(window,font=("Century Schoolbook",15),bg="gray79",fg="gray3").pack()
l7=Label(window,text="Address",font=("Century Schoolbook",15),bg="gray24",fg="snow").pack()
t1=Text(window,height=4,width=25,wrap=WORD,font=("Century Schoolbook",12),bg="gray79",fg="gray1").pack()
l8=Label(text="",bg="gray24").pack()

b1=Button(window,text="Cancel",bg="red2",fg="snow",font=("Century Schoolbook",15),width=17).pack()
l9=Label(text="",bg="gray24").pack()
b2=Button(window,text="Login",bg="green2",fg="snow",font=("Century Schoolbook",15),width=17).pack()

b3=Button(window,text="Click here to login")
window.mainloop()

