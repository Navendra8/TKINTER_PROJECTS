
import tkinter as tk
from random import choice
from datetime import datetime

root = tk.Tk()
root.configure(bg="#123456")
root.wm_minsize(500,500)
root.configure(bg="black")
i = 0
f2 = tk.Frame(root)
f2.pack()

f1 = tk.Frame(root)
f1.pack()

e1 = tk.Entry(f1,font=(None,24))
e1.pack()
for r in range(1,5):
    for c in range(3):
        if r == 1 and c == 0:
            b= tk.Button(f2,text="CLR",fg="white",bg="black",font=("monospace",20,"bold"),height=2,width=5)
            b.grid(row=r,column=c)
        elif r == 1 and c == 2:
            b= tk.Button(f2,text="<<",fg="white",bg="black",font=("monospace",20,"bold"),height=2,width=5)
            b.grid(row=r,column=c)
        else:
            b= tk.Button(f2,text=i,fg="white",bg="black",font=("monospace",20,"bold"),height=2,width=5)
            b.grid(row=r,column=c)
            i += 1
    
root.mainloop()
