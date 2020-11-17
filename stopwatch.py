
import tkinter as tk
from random import choice
from datetime import datetime

root = tk.Tk()
root.configure(bg="#123456")
root.wm_minsize(500,500)
root.title("STOPWATCH")
run = False
count = -1

def get_time():
    global count
    if run:
        if count != -1:
            d = datetime.fromtimestamp(count)
            l2.configure(text=d.strftime("%H:%M:%S"))
            count += 1
            l2.after(1000,get_time)
def start():
    global run,count
    if count == -1:
        run = True
        count = 66600
        b1['state'] = "disabled"
        b2['state'] = "normal"
        b3['state'] = "normal"
        b4['state'] = "normal"
        l1.configure(text="STARTED.....")
        get_time()
    else:
        run = True
        b1['state'] = "disabled"
        b2['state'] = "normal"
        b3['state'] = "normal"
        b4['state'] = "normal"
        l1.configure(text="STARTED.....")
        get_time()
    
def reset():
    global run,count
    run = True
    count=66600
    b3['state'] = "disabled"
    b2['state'] = "normal"
    b1['state'] = "normal"
    l1.configure(text="RESET.....")
    get_time()
    
def stop():
    global run,count
    run = False
    count= -1
    l1.configure(text="STOPPED.....")
    b2['state'] = "disabled"
    b1['state'] = "normal"
    b3['state'] = "normal"
    
def pause():
    global run,count
    run = False
    l1.configure(text="PAUSED.....")
    b2['state'] = "normal"
    b1['state'] = "normal"
    b3['state'] = "normal"
    b4['state'] = "disabled"

l1 = tk.Label(root,text="STOPWATCH!!!!",bg="#123456",fg="white",font=(None,30,"italic"))
l1.pack()

l2 = tk.Label(root,text="TIME",bg="black",fg="white",font=(None,25))
l2.pack(pady=40)

b1 = tk.Button(root,text="START",fg="white",bg="black",font=("monospace",20,"bold"),command=start)
b1.pack(fill="x")

b2 = tk.Button(root,text="STOP",fg="white",bg="black",font=("monospace",20,"bold"),command=stop)
b2.pack(fill="x")

b3 = tk.Button(root,text="RESET",fg="white",bg="black",font=("monospace",20,"bold"),command=reset)
b3.pack(fill="x")

b4 = tk.Button(root,text="PAUSE",fg="white",bg="black",font=("monospace",20,"bold"),command=pause)
b4.pack(fill="x")

root.mainloop()
