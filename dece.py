import securef as b
import os
from tkinter import * 
from tkinter.ttk import *
import base64
from tkinter.filedialog import askopenfile
from tkinter import messagebox 
import pyperclip
class open1:
        def __init__(self):
              self.file=None
              self.key=""
              self.root = Tk() 
              self.root.geometry('700x400') 
              self.root.title("DECRYPTION OF FILE")
              self.l = Label(self.root, text="DATA ENCRYPTION  PROJECT\n By: Shivansh Nautiyal GEU\n") 
              self.l.config(font =("Courier", 14))
              self.l.grid(row = 1, column = 1, sticky = E, pady = 2)
              self.label1=Label(self.root,text="Select file to decrypt ")
              self.label1.grid(row = 3, column = 1, sticky = W,pady =2)
              self.label1.config(font =("Courier", 11))
              self.but = Button(  self.root, text ='Select File', command =self.open_file) 
              self.but.grid(row = 3, column = 2, sticky = E)
              self.label2=Label(self.root,text="Select key file ")
              self.label2.grid(row = 4, column = 1, sticky = W,pady =2)
              self.label2.config(font =("Courier", 11))
              self.but1 = Button(  self.root, text ='Select Key', command =self.open_key) 
              self.but1.grid(row = 4, column = 2, sticky = E) 
              self.label=Label(self.root,text="OR")
              self.label.grid(row = 5, column = 2, sticky = W,pady =2)
              self.label.config(font =("Courier", 14))
              self.label3=Label(self.root,text="ENTER THE SECRET KEY")
              self.label3.grid(row = 6, column = 1, sticky = W,pady =2)
              self.label3.config(font =("Courier", 14))
              self.e1=Entry(self.root)
              self.e1.grid(row = 6, column = 2, sticky = W,pady =2)
              self.b2 = Button(  self.root, text ='DECRYPT', command=self.drypt) 
              self.b2.grid(row = 8, column = 1, sticky = E)
              self.but1['state']=DISABLED 
              self.label4=Label(self.root,text=" ")
              self.label4.grid(row = 9, column = 2, sticky = W,pady =2)
              self.label4.config(font =("Courier", 14))
              self.b4 = Button(self.root, text ='Back', command=self.back) 
              self.b5 = Button(self.root, text ='Exit', command=self.exit1)
              self.b4.grid(row = 10, column = 1, sticky = E) 
              self.b5.grid(row =10, column = 2, sticky = E)
              self.root.mainloop()    
        def open_file(self):
            self.file = askopenfile(mode ='r', filetypes =[]) 
            if self.file is not None:
                self.but1['state']=NORMAL
            else:
                 messagebox.showinfo("status", "CANNOT OPEN FILE TRY AGAIN")
        def drypt(self):
            if self.file is not None:
                self.key=self.e1.get()
                if self.key !="":
                    file1=open(self.file.name,"rb")
                    data=file1.read()
                    temp=open("secret.txt","wb")
                    # read all file data
                    temp.write(data)
                    file1.close()
                    temp.close()
                    self.decrypt("secret.txt",self.file.name,self.key)
                    os.remove("secret.txt")
                    font1="Sucessfully Decrypted\n YOUR FILE IS READY TO VIEW  - \t"
                    self.label4.config(text= font1)
                    messagebox.showinfo("status", "Sucessfully Decrypted")
                else:
                    font1="PLEASE SELECT KEY FILE OR ENTER THE KEY"
                    self.label4.config(text= font1)
                    messagebox.showinfo("status", "KEY NOT FOUND")
            else:
                 messagebox.showinfo("status", "CANNOT OPEN FILE || FILE NOT FOUND")
        def open_key(self):
            if self.file is not None:
                filekey = askopenfile(mode ='r', filetypes =[('Key files','*.abc')])
                file1=open(filekey.name,"r")
                self.e1.insert(0,file1.read())
                self.b2['state']=NORMAL
        def decrypt(self,filename,oriFile,key):
                file=open(filename, "rb") 
                # read all file data
                data=file.read()
                file.close()
                x=0
                while(x<len(data)):
                    decrypted_data = b.decrypt_msg(data[x:x+699],key)
                    f=open("temp.xy","a")
                    f.write(decrypted_data)
                    x+=699
                    f.close()
                f=open("temp.xy","rb")
                file_data=f.read()
                file_data=base64.urlsafe_b64decode(file_data)
                file=open(oriFile,"wb")
                file.write(file_data)
                file.close()
                f.close()
                os.remove("temp.xy")  
        def back(self):
                self.root.destroy()
                import main
        def exit1(self):
                self.root.destroy()
open1()