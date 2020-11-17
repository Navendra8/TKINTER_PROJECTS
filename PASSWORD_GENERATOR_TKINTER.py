

from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter.ttk import *
from tkinter import messagebox
from random import randint
import random
import string
import shortuuid
import pyperclip


root = tk.Tk()
root.configure()
root.wm_minsize()
root.configure(bg="powder blue")
width = int(root.winfo_screenwidth()/2)
height =int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)
root.resizable(0,0)
root.title("password generator")
#-------------------------------------------------------------

def password_generator(): 
    
    l=combo.get()
    a=shortuuid.uuid()
    a=shortuuid.ShortUUID().random(length=int(l))
    
    e.delete('0', 'end')
    e.insert(5,a)
    

#-------------------------------------------------------------



l=tk.Label(root,text= "YOUR NEW GENERATED PASSWORD .....",font=("cursive",20))
l.pack(pady=(35,0))

#-------------------------------------------------------------


e=tk.Entry(root,font=(None,20))
e.place(x = 100,
        y = 75,
        width=500,
        height=50)

#-------------------------------------------------------------

var1 = IntVar()
l1=tk.Label(root,text="SELECT LENGTH OF YOUR PASSWORD",font=("cursive",20))
l1.pack(pady=(65,0))


#-------------------------------------------------------------


combo = Combobox(root, textvariable=var1) 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.pack(pady=(20,0)) 

#-------------------------------------------------------------

b1=tk.Button(root,text="GENERATE PASSWORD...",command=password_generator,fg='Black',width=25,height=5)
b1.place(x=250,y=350)



root.mainloop()

