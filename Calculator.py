from tkinter import *
root = Tk()
root.geometry("650x780")
root.title("Calculator")
def calculator():
    
    num1 = entry1.get()
    num2 = entry3.get()
    operator = entry2.get()
    
    match operator:
        case '+' :
            result = num1 + num2
        case '-' :
            result = num1 - num2
        case '*' :
            result = num1 * num2
        case '/' :
            if num2 ==0:
                result = "Zero Division Error!"
            else:
                result = num1 / num2
        case '%' :
            result = (num1/100)*num2
        case '//' :
            result = num1/num2 - (num1/num2 - int(num1/num2))
            int(result)
        case _:
                result = "invalid operation!"
    entry4.set(result)
    entry1.set("")
    entry2.set("")
    entry3.set("")

Label(root,text=" Calculator ",font="Arial 40 bold",bg="green",fg="yellow").pack(pady=30)

frame1= Frame(root,bg="aqua")
entry1 = DoubleVar(value="")
entry_a = Entry(frame1,textvariable=entry1,font ='Arial 20',justify="right",width=30,borderwidth=2,relief=RIDGE)
entry_a.pack(fill=X,expand=True)
Label(frame1,text="Operand 1",font="Arial 8 bold").pack(side=RIGHT)
frame1.pack(pady=20)

frame2= Frame(root,bg="aqua")
entry2 = StringVar()
entry_b = Entry(frame2,textvariable=entry2,font ='Arial 20',justify="right",width=30,borderwidth=2,relief=RIDGE)
entry_b.pack(fill=X,expand=True ) 
Label(frame2,text="Operator ( +    -    *    /    %    // )",font="Arial 8 bold").pack(side=RIGHT)
frame2.pack(pady=20)

frame3= Frame(root,bg="aqua")
entry3 = DoubleVar(value="")
entry_c = Entry(frame3,textvariable=entry3,font ='Arial 20',justify="right",width=30,borderwidth=2,relief=RIDGE)
entry_c.pack(fill=X,expand=True)
Label(frame3,text="Operand 2",font="Arial 8 bold").pack(side=RIGHT)
frame3.pack(pady=20)

frame4= Frame(root,bg="aqua")
entry4 = StringVar()                     # value="your output wiil be show here" as paramerter inside StringVar as palceholder
entry_d = Entry(frame4,state="readonly",textvariable=entry4,insertbackground ="white",font ='Arial 26',justify="right",width=20,borderwidth=4,relief=RIDGE)
entry_d.pack(fill=X,expand=True)
frame4.pack(pady=20)
Button(frame4,text="Output",command=calculator,font="Arial 15 bold",width=10).pack(pady=10)

root.configure(background="aqua")   
Button(text="Close",bg="yellow",command=root.destroy,width=10,font ="Arial 10 bold").pack(pady=20)
root.mainloop()


    
