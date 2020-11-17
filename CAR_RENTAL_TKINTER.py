
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
root.configure(bg="cyan")
width = int(root.winfo_screenwidth()/2)
height =int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)
root.resizable(0,0)
root.title("CAR RENTAL SERVICE ")

#-------------------------------------------------------------



f1 = tk.Frame(root,bg="cyan")

#-------------------------------------------------------------

l=tk.Label(root,text= "WHICH CAR YOU WANT TO SELECT",font=("cursive",20),bg="cyan")
l.pack(pady=(35,0))

#-------------------------------------------------------------
var1 = IntVar()


l1=tk.Label(f1,text="CAR TYPE",font=("Itlaic",15),bg="cyan")
l1.pack(side=LEFT,padx=(0,10))

combo = Combobox(f1,) 
combo['values'] = ("HATCHBACK","SEDAN","SUV") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.pack(side=LEFT,padx=(20,0))

#-------------------------------------------------------------


l2=tk.Label(f1,text="NO OF DAYS",font=("Itlaic",15),bg="cyan")
l2.pack(side=LEFT,padx=(0,10))

combo2 = Combobox(f1, ) 
combo2['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
30, 31,) 
combo2.current(0) 
combo2.bind('<<ComboboxSelected>>') 
combo2.pack(side=LEFT,padx=(20,0))

#-------------------------------------------------------------
e=tk.Entry(root,font=(None,20))
e.place(x = 120,
        y = 175,
        width=500,
        height=50)
#-------------------------------------------------------------

b1=tk.Button(root,text="GENERATE PASSWORD...",command="",fg='Black',width=25,height=5)
b1.place(x=250,y=250)


#-------------------------------------------------------------






root.mainloop()

