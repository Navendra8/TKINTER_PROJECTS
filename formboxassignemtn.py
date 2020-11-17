

import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from random import randint



root = tk.Tk()
root.title("Desktop")
root.iconbitmap("/Users/navendrasingh/Downloads/newicon.ico")
root.configure(bg='white')

width = int(root.winfo_screenwidth()/2)
height =int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)
root.resizable(0,0)

def check():
    if len(e1.get())==0 or  len(e2.get())==0  or  len(e3.get())==0  or  len(e4.get())== 0 :
        messagebox.showerror("error","Please fill In All Require Boxes")
    else:
        messagebox.showinfo("info","Welcome")


l=tk.Label(root,text="REGISTRATION FORM ",font=("cursive",25))
l.place(x=270,y=60)
l1=tk.Label(root,text=" FIRST NAME :",font=("cursive",25))
l1.place(x=80,y=130)
e1=tk.Entry(root,font=(None,24))
e1.place(x=280,y=130)
l2=tk.Label(root,text="LAST NAME :",font=("cursive",25))
l2.place(x=85,y=180)
e2=tk.Entry(root,font=(None,24))
e2.place(x=280,y=180)
l3=tk.Label(root,text="EMAIL :",font=("cursive",25))
l3.place(x=85,y=230)
e3=tk.Entry(root,font=(None,24))
e3.place(x=280,y=230)
l4=tk.Label(root,text="PASSWORD :",font=("cursive",25))
l4.place(x=85,y=280)
e4=tk.Entry(root,font=(None,24))
e4.place(x=280,y=280)
b1=tk.Button(root,text="SUBMIT",command=check,fg='red',width=25,height=5)
b1.place(x=280,y=350)











root.mainloop()
