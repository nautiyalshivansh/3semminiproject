import securef as b
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox 
import pyperclip
def encrypt_msg(msg,key):
    return b.encrypt_msg(msg,key)
def enc():
    msg=e1.get()
    msg=msg.encode('UTF8')
    key=b.get_key()
    text = encrypt_msg(msg,key)
    e3.insert(0,text)
    e2.insert(0,key.decode('UTF8'))
    messagebox.showinfo("status", "Sucessfully Encrypted the file")
def copy():
            pyperclip.copy(e2.get())
            messagebox.showinfo("status", "KEY Sucessfully saved to Clipboard")
def copy1():
            pyperclip.copy(e3.get())
            messagebox.showinfo("status", "TEXT Sucessfully saved to Clipboard")
def back():
    root.destroy()
    import main
def exit1():
    root.destroy()
root = Tk() 
root.geometry('700x400') 
root.title("ENCRYPTION OF FILE")
var = StringVar()         
var.set("DATA ENCRYPTION  PROJECT\n By: Shivansh Nautiyal GEU\n")
l = Label(root, textvariable=var) 
l.config(font =("Courier", 14))
l.grid(row = 1, column = 2, sticky = W, pady = 2)
l1 = Label(root, text="PLEASE ENTER THE TEXT TO ENCRYPT") 
l1.config(font =("Courier", 14))
l1.grid(row = 2, column = 1, sticky = W, pady = 2)
e1=Entry(root)
e1.grid(row = 2, column = 2, sticky = W,pady =2)
b2 = Button(root, text ='Encrypt', command=enc)
b2.grid(row = 3, column = 1, sticky = E) 
l2 = Label(root, text="YOUR KEY:--") 
l2.config(font =("Courier", 14))
l2.grid(row = 5, column = 1, sticky = W, pady = 2)
e2=Entry(root)
e2.grid(row = 5, column = 2, sticky = W,pady =2)
l3 = Label(root, text="THE  ENCRYPTED TEXT :--") 
l3.config(font =("Courier", 14))
l3.grid(row = 4, column = 1, sticky = W, pady = 2)
e3=Entry(root)
e3.grid(row = 4, column = 2, sticky = W,pady =2)
T = Text(root, fg="black",bg="white",font=("Comic Sans MS","11"))
b2 = Button(root, text ='Copy Encrypted text', command=copy1) 
b3 = Button(root, text ='Copy Key', command=copy)
b2.grid(row = 6, column = 1, sticky = E) 
b3.grid(row = 6, column = 2, sticky = E)
b4 = Button(root, text ='Back', command=back) 
b5 = Button(root, text ='Exit', command=exit1)
b4.grid(row = 7, column = 1, sticky = E) 
b5.grid(row = 7, column = 2, sticky = E)
root.mainloop()

