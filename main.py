from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox 
def textenc():
    root.destroy()
    import encryptdata
def fileenc():
    root.destroy()
    import eenc
def textdec():
    root.destroy()
    import decryptdata
def filedec():
    root.destroy()
    import dece
def exit1():
    root.destroy()
root = Tk() 
root.geometry('700x400') 
root.title("ENCRYPTION OF FILE")
var = StringVar()         
var.set("DATA ENCRYPTION  PROJECT\n By: Shivansh Nautiyal GEU\n")
l = Label(root, textvariable=var) 
l.config(font =("Courier", 14))
l.grid(row = 1, column = 2, sticky = W, pady = 3)
b = Button(root, text ='Encrypt', command=textenc) 
b.grid(row = 2, column = 2, sticky = E) 
b1 = Button(root, text ='Encrypt', command=fileenc) 
b1.grid(row = 3, column = 2, sticky = E) 
b2 = Button(root, text ='Decrypt', command=textdec) 
b2.grid(row = 4, column = 2, sticky = E) 
b3 = Button(root, text ='Decrypt', command=filedec) 
b3.grid(row = 5, column = 2, sticky = E) 
b4 = Button(root, text ='Exit', command=exit1) 
b4.grid(row = 6, column = 1, sticky = E) 
l1 = Label(root, text="Encrypt some Message") 
l1.config(font =("Courier", 14))
l1.grid(row = 2, column = 1, sticky = W, pady = 2)
l2 = Label(root, text="Encrypt the File") 
l2.config(font =("Courier", 14))
l2.grid(row = 3, column = 1, sticky = W, pady = 2)
l3 = Label(root, text="Decrypt the Message") 
l3.config(font =("Courier", 14))
l3.grid(row = 4, column = 1, sticky = W, pady = 2)
l4 = Label(root, text="Decrypt the File") 
l4.config(font =("Courier", 14))
l4.grid(row = 5, column = 1, sticky = W, pady = 2)
root.mainloop()
