from tkinter import *
from tkinter.font import Font
from functools import partial

root = Tk()

work = []
root.title("To Do List")
root.geometry("700x750")
root.maxsize(900,800)

heading = Label (root,text="To Do List", fg = "white",font = "Capsuula 30 bold" ,bg = "orange",padx=5,pady=5)
heading.pack(pady = 30)

def Delete(frame2,val):
    work.remove(val)
    frame2.destroy()

def Done(entry1,val):
    entry1.tag_add('strikethrough','1.0','end') 
    entry1.tag_config('strikethrough',font=('Capsuula', 19, 'overstrike'))


def custom_task(val):
    frame2 = Frame(root,bg="#A9A9A9")
    entry1  = Text(frame2,height=1.2,width=22,wrap="none",font="Capsuula 20")
    entry1.pack(side="left",ipadx=2,ipady=2)
    entry1.insert(END,val)
    entry1.config(state=DISABLED)
    button1 = Button(frame2,text="Delete",font="Capsuula 15",borderwidth=0,relief="flat",highlightthickness=0,command=partial(Delete,frame2,val),bg="orange",fg="white")
    button1.pack(side="right",fill="both",expand=True)
    button2 = Button(frame2,text="Done ",font="Capsuula 15",borderwidth=0,relief="flat",highlightthickness=0,command=partial(Done,entry1,val),bg="orange",fg="white")
    button2.pack(side="right",padx=(0,2),fill="both",expand=True)
    frame2.pack(pady=1)

def Previous():
    with open("work.txt","r") as f:
        content = f.read()
        content = content.replace(content[0:2],"")
        content = content.replace(content[-2:],"")
        global work
        work = content.split("', '")
        for item in work:
            custom_task(item)
            
def Add():
    if (var.get() != ""):
        var1=StringVar(value=var.get())
        work.append(var.get())
        custom_task(var1.get())
        var.set("")


frame1= Frame(root,bg="#A9A9A9")
var = StringVar()
entry = Entry(frame1,textvariable=var,bg="white",fg="black",font = "Arial 20",width=27)
entry.pack(fill=BOTH,expand=True,ipadx=4,ipady=4,side="left")
button = Button(frame1,text=" Add ",font="Capsuula 15",borderwidth=0,relief="flat",highlightthickness=0,command=Add,bg="orange",fg="white")
button.pack(fill="both",expand=True,side="right")
frame1.pack(pady=10)
button4 = Button(root,text=" Add Previous ",command=Previous,width=12,bg='orange',borderwidth=0,relief="flat",highlightthickness=0,fg="white",font="Arial 12 bold")
button4.pack(pady=20)
Button(text="Close",command=root.destroy,width=10,font ="Arial 10 bold").pack(pady=(10,20))
root.configure(bg="#9370DB")
root.mainloop()

if (work != []):
    with open("work.txt","w") as f:
        f.write(str(work))