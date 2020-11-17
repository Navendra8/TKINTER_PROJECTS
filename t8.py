
import tkinter as tk
import pymysql as sql
from tkinter import messagebox

root = tk.Tk()  #create a root window or main window
root.title("Desktop")
root.iconbitmap("python_icon.ico")
root.configure(bg="black")


width = int(root.winfo_screenwidth()/2)
height = int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)  #(width,height)
root.resizable(0,0)  #cannot resize height or width it will be same always

def checkvalue():
    db = sql.connect(host="localhost",port=3306,database="internship_batch",user="root",password="")
    cursor = db.cursor()
    email = f2_e1.get()
    password = f2_e2.get()
    cmd = f"select * from users where email='{email}'"
    cursor.execute(cmd)
    data = cursor.fetchone()
    if data:
        if password == data[1]:
            messagebox.showinfo("INFO","WELCOME")
        else:
            messagebox.showerror("ERROR!","Invalid PASSWORD!!!!")
    else:
        messagebox.showerror("ERROR!","Invalid Email!!!!")
    
def getf2():
    f1.forget()
    f2.pack(pady=100)
    
def getf1():
    f2.forget()
    f1.pack(ipadx=width/2,ipady=height/2)
    
def getf3():
    pass
    
    
f1 = tk.Frame(root,bg="gray")
f2 = tk.Frame(root,bg="black")

f1_b1 = tk.Button(f1,text="Login",bg="#123456",fg="white",font=("cursive",15,"italic"),height=4,width=6,command=getf2)
f1_b1.place(rely=0.3,relx=0)
f1_b2 = tk.Button(f1,text="Signup",height=4,width=6,bg="#123456",fg="white",command=getf3,font=("cursive",15,"italic"))
f1_b2.place(rely=0.3,relx=0.9)
f2_l1 = tk.Label(f2,text="Enter your email",font=("cursive",25,"italic"),fg="red",bg="black")
f2_l1.grid(row=0,column=0)
f2_e1 = tk.Entry(f2,font=(None,24),fg="blue")
f2_e1.grid(row=0,column=1)
f2_l2 = tk.Label(f2,text="Enter your password",font=("cursive",25,"italic"),fg="red",bg="black")
f2_l2.grid(row=1,column=0)
f2_e2 = tk.Entry(f2,font=(None,24),fg="blue",show="*")
f2_e2.grid(row=1,column=1)
f2_b1 = tk.Button(f2,text="Submit",height=1,width=7,bg="#123456",fg="white",command=checkvalue,font=("cursive",20,"italic"))
f2_b1.grid(row=2,column=0,columnspan=4)
f2_b1 = tk.Button(f2,text="Back",height=1,width=7,bg="#123456",fg="white",command=getf1,font=("cursive",20,"italic"))
f2_b1.grid(row=2,column=1,columnspan=4)
f1.pack(ipadx=width/2,ipady=height/2)



root.mainloop()
