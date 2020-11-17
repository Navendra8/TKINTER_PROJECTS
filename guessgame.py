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




class Guessgame:
    def __init__(self,master):
        self.master=master
        self.f1=tk.Frame()
        self.f1.pack()
        self.l1=tk.Label(self.f1,text='WELCOME',font=('bold'))
        self.l1.pack()

        self.l2=tk.Label(self.f1,text='GUESS ANY NUMBER BETWEEN 1-100',font=('cursive',10))
        self.l2.pack()


        self.e1=tk.Entry(self.f1,font=(None,34))
        self.e1.pack(fill='x')

        self.l3=tk.Label(self.f1,text='',font=('cursive',10))
        self.l3.pack()
        
        
        self.b1=tk.Button(self.f1,text="SUBMIT",command=self.checkvalue)
        self.b1.pack()
        
        
        self.i = 0
    
        self.num= randint(1,100)

    def check(self,ch):
        if self.num == ch:
                messagebox.showinfo("INFO",f'YOU WON AFTER {self.i} GUESSES')
                self.b1['state'] = 'disabled'
                self.i=0
        elif self.num<ch:
            self.l3.configure(text='THINK LESS')
        elif self.num>ch:
            self.l3.configure(text='THINK HIGH')
          
        
    def checkvalue(self):
      
        ch=int(self.e1.get())
        print(self.num)
        if self.i < 5:
            self.check(ch)
            self.i+=1
                
        else:
            messagebox.showerror("INFO",'YOU LOSS')
            self.i=0
            self.b1['state'] = 'disabled'


obj=Guessgame(root)
root.mainloop()
