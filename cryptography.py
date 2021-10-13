#Cryptography
import onetimepad
from tkinter import*
root=Tk()
root.title("CRYPTOGRAPHY APP")
 
 
def encryptMessage():
    a=var.get()
    ct=onetimepad.encrypt(a,"rahul")
    print("working",ct)
    e2.delete(0,END)
    e2.insert(END,ct)
    
 
l1=Label(root,text="Plain text")
l1.grid(row=0, column=0)
var=StringVar()
e1=Entry(root,textvariable=var)
e1.grid(row=0, column=1)
 
 
def decryptMessage():
    a=var3.get()
    ct=onetimepad.decrypt(a,"rahul")
    print("working",ct)
    e4.delete(0,END)
    e4.insert(END,ct)
 
 
l2=Label(root,text="Encrypted text")
l2.grid(row=1, column=0)
e2=Entry(root)
e2.grid(row=1, column=1)
 
l3=Label(root,text="Encrypted text")
l3.grid(row=4, column=0)
var3=StringVar()
e3=Entry(root,textvariable=var3)
e3.grid(row=4, column=1)
 
l4=Label(root,text="plain text")
l4.grid(row=5, column=0)
e4=Entry(root)
e4.grid(row=5, column=1)
 
 
b1=Button(root,text="Encrytion", command=encryptMessage,bg="red",fg="white")
b1.grid(row=2,column=1)
 
b2=Button(root,text="Decryption", command=decryptMessage, bg="green",fg="white")
b2.grid(row=6,column=1)
 
 
root.mainloop()
