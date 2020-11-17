

from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from random import randint


def save():
    name=e1.get()
    phone=e2.get()
    email=e3.get()
    db = sql.connect(host="localhost",port=3306,database="navendraproject",user="root",password="")
    cursor=db.cursor()
    cmd=f"select * from my_contact1 where name='{name}'"
    cursor.execute(cmd)
    data=cursor.fetchall()
    if data :
        messagebox.showerror('error',"Contact already saved.....")
          
    else:
        db = sql.connect(host="localhost",port=3306,database="navendraproject",user="root",password="")
        cursor=db.cursor()
        cmd=f"INSERT INTO my_contact1 (name,mobile,email)VALUES ('{name}','{phone}','{email}')"
        cursor.execute(cmd)
        db.commit()
        messagebox.showinfo('INFO','CONTACT NUMBER SAVED.....')
        
        
        
        
def exit():
    root.destroy()
    
    
def add_another():
    name=e1.get()
    phone=e2.get()
    email=e3.get()
    db = sql.connect(host="localhost",port=3306,database="navendraproject",user="root",password="")
    cursor=db.cursor()
    cmd=f"select * from my_contact1 where name='{name}'"
    cursor.execute(cmd)
    data=cursor.fetchall()
    if data :
        messagebox.showerror('error',"Contact already saved.....")
          
    else:
        db = sql.connect(host="localhost",port=3306,database="navendraproject",user="root",password="")
        cursor=db.cursor()
        cmd=f"INSERT INTO my_contact1 (name,mobile,email)VALUES ('{name}','{phone}','{email}')"
        cursor.execute(cmd)
        db.commit()
        messagebox.showinfo('INFO','CONTACT NUMBER SAVED.....')

root = tk.Tk()
root.configure()
root.wm_minsize()
root.configure()

width = int(root.winfo_screenwidth()/2)
height =int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)
root.resizable(0,0)
root.title("Contact")


root.geometry("125x120")
photo=PhotoImage(file="/Users/navendrasingh/Downloads/myp1.png")
bg_label=Label(image=photo)
bg_label.pack()

l=tk.Label(root,text="Add Conact",font=("cursive",25))
l.place(x=270,y=60)
l1=tk.Label(root,text="NAME :",font=("cursive",25))
l1.place(x=85,y=130)
e1=tk.Entry(root,font=(None,24))
e1.place(x=280,y=130)
l2=tk.Label(root,text="Mobile Number :",font=("cursive",25))
l2.place(x=85,y=180)
e2=tk.Entry(root,font=(None,24))
e2.place(x=280,y=180)

l3=tk.Label(root,text="EMAIL :",font=("cursive",25))
l3.place(x=85,y=230)
e3=tk.Entry(root,font=(None,24))
e3.place(x=280,y=230)

b1=tk.Button(root,text="SAVE",command=save,fg='red',width=25,height=5)
b1.place(x=280,y=350)



b2=tk.Button(root,text="ADD ANOTHER",command=add_another,fg='red',width=15,height=3)
b2.place(x=90,y=280)


b3=tk.Button(root,text="EXIT",command=exit,fg='red',width=15,height=3)
b3.place(x=550,y=280)

root.mainloop()

