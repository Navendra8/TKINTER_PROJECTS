
import tkinter as tk
from random import choice
from datetime import datetime
from tkinter import *
root = tk.Tk()
root.title("Calculator")

# create input field
operator = ""
text_input = StringVar()
display = Entry(root, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg='powder blue', justify='right')
display.grid(columnspan=4)

# define button click functions
def btnclick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def btnclear():
    global operator
    operator = ''
    text_input.set("")

def eql_button():
    global operator
    try:
        result = str(eval(operator))
        text_input.set(result)
        operator = result
    except:
        text_input.set("ERROR")
        operator = ""

# create buttons
display=Entry(root,font=('arial',20,'bold' ),textvariable=text_input,bd=30,insertwidth=4,bg='powder blue',justify='right').grid(columnspan=4)
btn7=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="7", command = lambda:btnclick(7),bg='powderblue').grid(row=1,column=0)
btn8=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="8",command = lambda:btnclick(8),bg='powderblue').grid(row=1,column=1)
btn9=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="9",command = lambda:btnclick(9),bg='powderblue').grid(row=1,column=2)
add=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="+",command = lambda:btnclick("+"),bg='powderblue').grid(row=1,column=3)
btn4=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="4",command = lambda:btnclick(4),bg='powderblue').grid(row=3,column=0)
btn5=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="5",command = lambda:btnclick(5),bg='powderblue').grid(row=3,column=1)
btn6=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="6",command = lambda:btnclick(6),bg='powderblue').grid(row=3,column=2)
minus=Button(root,padx=16,bd=18,fg="black",font=('arial',20,'bold'),text="-",command = lambda:btnclick("-"),bg='powderblue').grid(row=3,column=3)
btn1=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="1",command = lambda:btnclick(1),bg='powderblue').grid(row=4,column=0)
btn2=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="2",command = lambda:btnclick(2),bg='powderblue').grid(row=4,column=1)
btn3=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="3",command = lambda:btnclick(3),bg='powderblue').grid(row=4,column=2)
mul=Button(root,padx=16,bd=18,fg="black",font=('arial',20,'bold' ),text="*",command = lambda:btnclick("*"),bg='powderblue').grid(row=4,column=3)
div=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="/",command = lambda:btnclick("/"),bg='powderblue').grid(row=6,column=0)
per=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="%",command = lambda:btnclick("%"),bg='powderblue').grid(row=6,column=1)
ac=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="AC",command = lambda:btnclear(),bg='powderblue').grid(row=6,column=3)
eql=Button(root,padx=16,bd=18,fg="black",font=('arial',20,'bold' ),text="=",command = lambda:eql_button(),bg='powderblue').grid(row=6,column=2)
dot=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text=".",command = lambda:btnclick("."),bg='powderblue').grid(row=5,column=0)
zero=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold' ),text="0",command = lambda:btnclick(0),bg='powderblue').grid(row=5,column=1)

root.mainloop()
