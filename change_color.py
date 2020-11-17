
import tkinter as tk
from random import choice


root = tk.Tk()
root.configure(bg="black")
root.wm_minsize(500,500)
run = False


def on_enter(e):
    global run 
    run = False
    color()
    
def on_leave(e):
    global run
    run = True
    color()
    
def give_color():
    code = ['1','2','3','4','5','6','a','b','c','d','e','f']
    c = "#"
    for i in range(6):
        c += choice(code)
    return c

def color():
    global run
    if run:
        l2.configure(fg=give_color())
        l2.after(1000,color)  #after every 1 sec the function will be called

def changecolor():
    global run
    run = True
    b1['state'] = "disabled"
    color()
    
l1 = tk.Label(root,text="WELCOME!!!!",bg="black",fg="white",font=(None,30,"italic"))
l1.pack()

l2 = tk.Label(root,text="COLORS",bg="black",fg="white",font=(None,25,"italic"))
l2.pack(pady=40)

b1 = tk.Button(root,text="START",fg="white",bg="#123456",font=("monospace",20,"bold"),command=changecolor)
b1.pack(fill="x")

l2.bind("<Enter>",on_enter)   #use 2 event one is for entering and another is for leaving
l2.bind("<Leave>",on_leave)
#enter -- on_enter function
root.mainloop()
