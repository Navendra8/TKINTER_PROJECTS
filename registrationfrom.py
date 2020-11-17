import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from random import randint



root = tk.Tk()
root.title("Desktop")
root.iconbitmap("/Users/navendrasingh/Downloads/newicon.ico")
root.configure(bg='black')

width = int(root.winfo_screenwidth()/2)
height =int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)
root.resizable(0,0)
l=tk.Label(root,text="Welcome",font=("cursive",25))
l.pack()
l1=tk.Label(root,text="ENTER YOUR FIRST NAME",font=("cursive",25))
l1.pack()
e1=tk.Entry(root,font=(None,24))
e1.pack()
l2=tk.Label(root,text="ENTER YOUR LAST NAME",font=("cursive",25))
l2.pack()
e2=tk.Entry(root,font=(None,24))
e2.pack()
l3=tk.Label(root,text="ENTER YOUR  EMAIL",font=("cursive",25))
l3.pack()
e3=tk.Entry(root,font=(None,24))
e3.pack()
l4=tk.Label(root,text="ENTER YOUR PASSWORD",font=("cursive",25))
l4.pack()
e4=tk.Entry(root,font=(None,24))
e4.pack()
l5=tk.Label(root,text="ENTER YOUR PASSWORD",font=("cursive",25))
l5.pack()
e5=tk.Entry(root,font=(None,24))
e5.pack()
b1=tk.Button(root,text="SUBMIT",command="")
b1.pack()
root.mainloop()
