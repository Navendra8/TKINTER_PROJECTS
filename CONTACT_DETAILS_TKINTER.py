

from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from random import randint


root = tk.Tk()
root.configure()
root.wm_minsize()
root.configure(bg=photo)

width = int(root.winfo_screenwidth()/2)
height =int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)
root.resizable(0,0)
root.title("Contact")


c=Canvas(root, bg="blue", height=250, width=300)
photo=ImageTk.PhotoImage(image.open("/Users/navendrasingh/Downloads/myp1.png"))

c.create_image(0,0,anchor=NW,image=image)
c.pack()

l=tk.Label(root,text="Add Conact",font=("cursive",25))
l.place(x=270,y=60)
l1=tk.Label(root,text="NAME :",font=("cursive",25))
l1.place(x=85,y=130)
e1=tk.Entry(root,font=(None,24))
e1.place(x=280,y=130)
l2=tk.Label(root,text="Mobile Number:",font=("cursive",25))
l2.place(x=85,y=180)
e2=tk.Entry(root,font=(None,24))
e2.place(x=280,y=180)
l3=tk.Label(root,text="EMAIL :",font=("cursive",25))
l3.place(x=85,y=230)
e3=tk.Entry(root,font=(None,24))
e3.place(x=280,y=230)

b1=tk.Button(root,text="SAVE",command="",fg='red',width=25,height=5)
b1.place(x=280,y=350)



root.mainloop()
