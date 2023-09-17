import numpy
import time
import cv2
from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('1300x690')
frame = Frame(root, relief=RIDGE, borderwidth=5)
frame.pack(fill=BOTH,expand=1)
filename = PhotoImage(file="lone.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)

def hel():
   help(cv2)
def web():
    import capture
def web2():
    import cnn_model
def web3():
    import recognise
def web4():
    import recognisee   
def exitt():
    exit(1)
   
but1=Button(frame,padx=5,pady=5,width=20,bg='white',fg='black',relief=GROOVE,command=web,text='Capture',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=20,bg='white',fg='black',relief=GROOVE,command=web2,text='Train',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=20,bg='white',fg='black',relief=GROOVE,command=web3,text='Experiment',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but4=Button(frame,padx=5,pady=5,width=20,bg='white',fg='black',relief=GROOVE,command=web4,text='ASL With Voics',font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(frame,padx=5,pady=5,width=20,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=530,y=478)


root.mainloop()
