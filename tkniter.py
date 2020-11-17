import tkinter as tk
import pymysql as sql
from tkinter import messagebox




root = tk.Tk()
root.title("Desktop")
root.iconbitmap("/Users/navendrasingh/Downloads/newicon.ico")
root.configure(bg='black')

width = int(root.winfo_screenwidth()/2)
height =int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)
root.resizable(0,0)


def checkvalue():
    db = sql.connect(host="localhost",port=3306,database="navendraproject",user="root",password="")
    cursor=db.cursor()
    email=f2_e1.get()
    password=f2_e2.get()
    cmd=f"select * from users where email='{email}'"
    cursor.execute(cmd)
    data=cursor.fetchone()
    if data:
        if password == data[1]:
            messagebox.showinfo("INFO",'WELCOME')
            
        else:
            messagebox.showerror('ERROR','INVALID PASSWORD')
            
    else:
        messagebox.showerror('ERROR','INVALID EMAIL ADDRESS')


        
def getf2():
    f1.forget()
    f2.pack()
    
    
def getf1():
    f2.forget()
    f1.pack(ipadx=width/2,ipady=height/2)
        
        
f1=tk.Frame(root,bg='grey')
f2=tk.Frame(root,bg='black')

f1_b1=tk.Button(f1,text='LOGIN',command=getf2)
f1_b1.place(rely=0.3,relx=0)
f1_b2=tk.Button(f1,text='SIGNUP',command=getf1)
f1_b2.place(rely=0.3,relx=0.1)
f2_l1=tk.Label(f2,text='ENTER YOUR E-MAIL')
f2_l1.grid(row=0,column=0)
f2_e1=tk.Entry(f2,font=(None,34))
f2_e1.grid(row=0,column=1)
f2_l2=tk.Label(f2,text='ENTER YOUR PASSWORD')
f2_l2.grid(row=1,column=0)
f2_e2=tk.Entry(f2,font=(None,34))
f2_e2.grid(row=1,column=1)
f2_b1=tk.Button(f2,text='SUBMIT',command=checkvalue)
f2_b1.grid(row=2,column=0,columnspan=4)
f2_b1=tk.Button(f2,text='BACK',command=getf1)
f2_b1.grid(row=3,column=0,columnspan=4)





f1.pack(ipadx=width/2,ipady=height/2)





root.mainloop()
