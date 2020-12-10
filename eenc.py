import securef as b
import os
from tkinter import * 
from tkinter.ttk import *
import base64
from tkinter.filedialog import askopenfile
from tkinter import messagebox 
import pyperclip
from tkinter import filedialog
class open1:
        def __init__(self):
              self.file=None
              self.root = Tk() 
              self.root.geometry('700x400') 
              self.root.title("ENCRYPTION OF FILE")
              self.l = Label(self.root, text="DATA ENCRYPTION  PROJECT\n By: Shivansh Nautiyal GEU\n") 
              self.l.config(font =("Courier", 14))
              self.l.grid(row = 1, column = 2, sticky = E, pady = 2)
              self.but = Button(  self.root, text ='Select File', command =self.open_file) 
              self.but.grid(row = 3, column = 2, sticky = E) 
              self.b1 = Button(  self.root, text ='Encrypt', command=self.enc)
              self.b1.grid(row = 4, column = 2, sticky = E)
              self.b1['state']=DISABLED
              self.label=Label(self.root,text=" ")
              self.label.grid(row = 5, column = 2, sticky = W,pady =2)
              self.label.config(font =("Courier", 11))
              self.b2 = Button(  self.root, text ='Copy key', command=self.copy) 
              self.b3 = Button(  self.root, text ='SAVE TO FILE', command=self.save)
              self.b2.grid(row =6, column = 1, sticky = E) 
              self.b3.grid(row = 6, column = 3, sticky = E)
              self.b2['state']=DISABLED
              self.b3['state']=DISABLED
              self.b4 = Button(self.root, text ='Back', command=self.back) 
              self.b5 = Button(self.root, text ='Exit', command=self.exit1)
              self.b4.grid(row = 7, column = 1, sticky = E) 
              self.b5.grid(row = 7, column = 2, sticky = E)
              self.root.mainloop()    
        def open_file(self):
            self.file = askopenfile(mode ='r', filetypes =[]) 
            if self.file is not None:
                self.b1['state']=NORMAL
            else:
                 messagebox.showinfo("status", "CANNOT OPEN FILE TRY AGAIN")
        def enc(self): 
            if self.file is not None:
                file1=open(self.file.name,"rb")
                data=file1.read()
                temp=open("secret.txt","wb")
                # read all file data
                data=base64.urlsafe_b64encode(data)
                temp.write(data)
                file1.close()
                temp.close()
                self.key=b.get_key()
                self.encrypt("secret.txt",self.file.name,self.key)
                os.remove("secret.txt")
                self.key=self.key.decode('UTF8')
                font1="**************Sucessfully Encrypted***************\n YOUR PRIVATE KEY IS  - \t" + self.key
                self.but['state']=DISABLED
                self.label.config(text= font1)
                self.b2['state']=NORMAL
                self.b3['state']=NORMAL
        def encrypt(self,filename,oriFile,key):
            file=open(filename, "rb") 
            data=file.read()
            file.close()
            x=0
            while(x<len(data)):
                encrypted_data = b.encrypt_msg(data[x:x+500],key)
                f=open("temp.xy","a")
                f.write(encrypted_data)
                x+=500
                f.close()
            f=open("temp.xy","rb")
            file_data=f.read()
            file=open(oriFile, "wb")
            file.write(file_data)
            file.close()
            f.close()
            os.remove("temp.xy")
        def copy(self):
            pyperclip.copy(self.key)
            messagebox.showinfo("status", "Sucessfully saved to Clipboard")
        def save(self):
                fie=filedialog.askdirectory()
                fie+="/key.abc"
                file1 = open(fie,'w')
                file1.write(self.key)
                file1.close()
                messagebox.showinfo("status", "Sucessfully saved to " + fie)  
        def back(self):
                self.root.destroy()
                import main
        def exit1(self):
                self.root.destroy()
open1()