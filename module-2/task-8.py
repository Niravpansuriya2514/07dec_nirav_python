import tkinter
from tkinter import *

from tkinter import ttk
screen=tkinter.Tk()
screen.geometry("400x500")
screen.title("calculator")

lbfn=tkinter.Label(text='firstvalue:',bg='black',fg='white',font='Aptos 12 bold')
lbfn.grid(row=0,column=0,sticky='W')

txtfnm=int
txtfnm=tkinter.Entry()
txtfnm.grid(row=0,column=1,sticky='W')

lbln=tkinter.Label(text='Lastvalue:',bg='black',fg='white',font='Aptos 12 bold')
lbln.grid(row=2,column=0,sticky='W')

txtlnm=int
txtlnm=tkinter.Entry()
txtlnm.grid(row=2,column=1,sticky='W')


def btnclick():
     print("sum: = ",int(txtfnm.get()) +int(txtlnm.get()))

btn=tkinter.Button(text='=',width=10,height=1,font='Aptos 12 bold',command=btnclick)
btn.place(x=150,y=250)

screen.mainloop()