from cProfile import label
from cgitb import text
from struct import pack
import tkinter
from tkinter import *
from turtle import Screen
from unittest import result

root=Tk()
# title
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="black")
# icon
# img_icon=PhotoImage(file="calculator.png")
# root.iconphoto(False,img_icon)

equation=""
def show(value):
    global equation
    equation+=value
    lbl_result.config(text=equation)
def  clear():
    global equation
    equation=""
    lbl_result.config(text=equation)
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    lbl_result.config(text=result)
    

# result screen
lbl_result=Label(root,width=25,height=2,text="",font=("arial",30),bg="whitesmoke")
lbl_result.pack()

# button c
C_button=Button(root,text='C',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#3697f5",command=lambda: clear())
C_button.place(x=10,y=100)
#  button division
div_button=Button(root,text='/',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("/"))
div_button.place(x=150,y=100)
# percentage 
Per_button=Button(root,text='%',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("%"))
Per_button.place(x=290,y=100)
# button mul
mul_button=Button(root,text='*',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("*"))
mul_button.place(x=430,y=100)

# button 7
sev_btn=Button(root,text='7',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("7"))
sev_btn.place(x=10,y=200)
# button 8
eight_btn=Button(root,text='8',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("8"))
eight_btn.place(x=150,y=200)
# button 9
nin_btn=Button(root,text='9',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("9"))
nin_btn.place(x=290,y=200)
# button minus
minus_btn=Button(root,text='-',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("-"))
minus_btn.place(x=430,y=200)

# button 4
four_btn=Button(root,text='4',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("4"))
four_btn.place(x=10,y=300)
# button 5
five_btn=Button(root,text='5',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("5"))
five_btn.place(x=150,y=300)
# button 6
six_btn=Button(root,text='6',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("6"))
six_btn.place(x=290,y=300)
# button plus
plus_btn=Button(root,text='+',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("+"))
plus_btn.place(x=430,y=300)

# button 1
one_btn=Button(root,text='1',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("1"))
one_btn.place(x=10,y=400)
# button 2
two_btn=Button(root,text='2',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("2"))
two_btn.place(x=150,y=400)
# button 3
thr_btn=Button(root,text='3',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("3"))
thr_btn.place(x=290,y=400)
# button zero
zero_btn=Button(root,text='0',width=11,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("0"))
zero_btn.place(x=10,y=500)

# BUTTON DOT(.)
dot_btn=Button(root,text='.',width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2a2d36",command=lambda: show("."))
dot_btn.place(x=290,y=500)
# BUTTON ENTER
ent_btn=Button(root,text='=',width=5,height=3,font=("arial",30,"bold"),bd=1,fg="white",bg="red",command=lambda: calculate())
ent_btn.place(x=430,y=400)






root.mainloop()