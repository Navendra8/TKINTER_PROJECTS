


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
    if option.get()=="1.XYZ":
        messagebox.showinfo("INFO",'YOU ARE CORRECT')
        
        
    else:
        messagebox.showerror('error','Not Correct')

l=tk.Label(root,text="QUIZ FORM ",font=("cursive",25))
l.place(x=270,y=60)

l1=tk.Label(root,text=" India's Prime Minister:",font=("cursive",25))
l1.place(x=80,y=130)
option =OptionMenu(root,var,"1.XYZ","2.AYZ","3.XXYZ","4.XYyyyZ")
option.place(x=380,y=130)


b1=tk.Button(root,text="SUBMIT",command=check,fg='red',width=25,height=5)
b1.place(x=280,y=350)






root.mainloop()
