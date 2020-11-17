
import tkinter as tk
from random import choice
from datetime import datetime

root = tk.Tk()
root.configure(bg="#123456")
root.wm_minsize(500,500)

image = tk.PhotoImage(file="download.png")  #only show png file

l2 = tk.Label(root,text="WELCOME!!!!",bg="black",fg="white",font=(None,25),image=image)
l2.pack(pady=40)

b1 = tk.Button(root,text="START",fg="white",bg="black",font=("monospace",20,"bold"))
b1.pack(fill="x")


root.mainloop()
