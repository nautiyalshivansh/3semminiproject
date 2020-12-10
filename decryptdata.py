import securef as b
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox 
import pyperclip
def decrypt_msg(msg,key):
    return b.decrypt_msg(msg,key)
def dec():
    msg =e1.get()
    msg=msg.encode('UTF8')
    key = e2.get()
    data = decrypt_msg(msg,key)
    e3.insert(0,data)
def copy():
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
l1 = Label(root, text="PLEASE ENTER THE TEXT TO DECRYPT") 
l1.config(font =("Courier", 14))
l1.grid(row = 2, column = 1, sticky = W, pady = 2)
e1=Entry(root)
e1.grid(row = 2, column = 2, sticky = W,pady =2)
l2 = Label(root, text="PLEASE ENTER THE KEY") 
l2.config(font =("Courier", 14))
l2.grid(row = 3, column = 1, sticky = W, pady = 2)
e2=Entry(root)
e2.grid(row = 3, column = 2, sticky = W,pady =2)
b2 = Button(root, text ='Decrypt', command=dec)
b2.grid(row = 4, column = 1, sticky = E) 
l3 = Label(root, text="MESSAGE FOR YOU:--") 
l3.config(font =("Courier", 14))
l3.grid(row = 5, column = 1, sticky = W, pady = 2)
e3=Entry(root)
e3.grid(row = 5, column = 2, sticky = W,pady =2)
l3 = Label(root, text="THE  ENCRYPTED TEXT :--") 
T = Text(root, fg="black",bg="white",font=("Comic Sans MS","11"))
b3 = Button(root, text ='Copy Decrypted text', command=copy) 
b3.grid(row = 6, column = 1, sticky = E) 
b4 = Button(root, text ='Back', command=back) 
b5 = Button(root, text ='Exit', command=exit1)
b4.grid(row = 7, column = 1, sticky = E) 
b5.grid(row = 7, column = 2, sticky = E)
root.mainloop()