#Syntax of the tkinter
import tkinter as tk
window=tk.Tk()
window.title("My tkinter")
window.geometry("1200x600")
window.configure(background="coral1")
window.mainloop()
#program1===================================
'''
import tkinter as tk
window=tk.Tk()
window.title("my tkinter")
window.geometry("1270x600")
window.configure(background="coral1")
tk.Label(window,text="My label",bg="red",fg="white", width=20,height=30,font=("arial",40)).pack()
window.mainloop()
'''
#program2==================================
'''
import tkinter as tk
window=tk.Tk()
window.title("my tkinter")
window.geometry("1270x600")
window.configure(background="coral1")
tk.Label(window,text="My label",bg="red",fg="white", 
width=20,height=5,font=("arial",40)).grid(row=0,column=1)
window.mainloop()
import tkinter as tk
window=tk.Tk()
window.title("my tkinter")
window.geometry("1270x600")
window.configure(background="coral1")
tk.Label(window,text="My label",bg="red",fg="white", width=20,height=5,font=("arial",40)).grid(row=0,column=1)
window.mainloop()
'''

#program3=================================
'''
import tkinter as tk
window=tk.Tk()
window.title("my tkinter")
window.geometry("1270x600")
window.configure(background="coral1")

tk.Entry(window,bg="red",fg="white",width=30).pack()
tk.Button(window,text="Button1",bg="white",fg="black",font=("arial",10),width=9,height=5).pack()
window.mainloop()
'''

