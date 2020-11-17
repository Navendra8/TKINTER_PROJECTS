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


def password_generator(): 
    
    l=combo.get()
    a=shortuuid.uuid()
    a=shortuuid.ShortUUID().random(length=int(l))
    
    blank.delete('0', 'end')
    blank.insert(5,a)
    
    
root = tk.Tk()
root.configure()
root.wm_minsize()
root.configure()
width = int(root.winfo_screenwidth()/2)
height =int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)
root.resizable(0,0)
root.title("password generator")
root.geometry("125x120")
photo=PhotoImage(file="/Users/navendrasingh/Downloads/myp1.png")
bg_label=Label(image=photo)
bg_label.pack()

b1=tk.Button(root,text="GENERATE PASSWORD...",command=password_generator,fg='red',width=25,height=5)
b1.place(x=280,y=350)


blank = Entry(root,width=100)

blank.grid()

var1 = IntVar()
l1=tk.Label(root,text="Length of password",font=("cursive",20))
l1.place(x=85,y=25)

combo = Combobox(root, textvariable=var1) 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=3) 


root.mainloop()


