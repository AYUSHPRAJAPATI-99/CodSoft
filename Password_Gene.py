import string as s
import random

from tkinter import *

root = Tk()
root.geometry("650x780")
root.title("Password Generator")

def password_generator():
    pass_length = entry1.get()                            
    value_select = var.get()
    symbol = "@#$&"                         # custom_symbol = "you can write than concatenate"
    if  value_select==1:                                      # complex1.lower() == "simple" :
        pass_char = s.ascii_letters + s.digits + symbol
    elif value_select==2:
        pass_char = s.ascii_letters + s.digits + s.punctuation 
   
    password = ""

    for i in range(pass_length):
        char = random.choice(pass_char)
        password += char
    entry2.set(password)
    entry1.set("")

Label(root,text="Password Generator",font="Arial 40 bold underline",bg="grey",fg="black").pack(pady=40)
var = IntVar(value=2)
frame0= Frame(root,bg="#A9A9A9")
radio1 =Radiobutton(frame0,text="Simple",variable =var,value=1,font ='Arial 20 ',bg="grey")
radio1.pack(side=LEFT)
radio2 =Radiobutton(frame0,text="Complex",variable =var,value=2,font ='Arial 20 ',bg="grey")
radio2.pack(side=RIGHT)
frame0.pack(pady=30)

frame1= Frame(root,bg="grey")
entry1 = IntVar(value="")
entry_a = Entry(frame1,textvariable=entry1,font ='Arial 30',justify="right",width=25,borderwidth=2,relief=RIDGE)
entry_a.pack(fill=X,expand=True)
Label(frame1,text="Enter Password Length",font="Arial 10 bold").pack(side=RIGHT)
frame1.pack(pady=30)


frame2= Frame(root,bg="grey")
entry2 = StringVar()
entry_b = Entry(frame2,textvariable=entry2,insertbackground ='white' ,font ='Arial 30 ',justify="right",width=25,borderwidth=2,relief=RIDGE)
entry_b.pack(fill=X,expand=True)
Label(frame2,text="Your Generated Password",font="Arial 10 bold").pack(side=RIGHT)
frame2.pack(pady=20)
Button(root,text="Generate Password",command=password_generator,font="Arial 15 bold",height=1,width=18,bg="yellow").pack(pady=20)


root.configure(background="grey")   
Button(text="Close",command=root.destroy,width=10,font ="Arial 10 bold").pack(pady=20)
root.mainloop()


