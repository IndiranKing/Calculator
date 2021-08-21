from tkinter import *


def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)        


window=Tk()
window.title("Calculator")
#window.iconbitmap("cal download.ico")
operator=""
text_Input =StringVar()


w=420
h=485
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
x=(sw/2)-(w/2)
y=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d" % (w,h,x,y))




txtdisply=Entry(window,font=('times',24,'bold'),textvariable=text_Input,bd=30,justify=RIGHT,bg="powder blue",insertwidth=10)
txtdisply.grid(columnspan=20)


btn1=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="1",command=lambda:btnClick(1),bg="#3399FF").grid(row=1,column=0)

btn2=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="2",command=lambda:btnClick(2),bg="#3399FF").grid(row=1,column=1)

btn3=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="3",command=lambda:btnClick(3),bg="#3399FF").grid(row=1,column=2)

Addition=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="+",command=lambda:btnClick("+"),bg="powder blue").grid(row=1,column=3)

#===============================================================================================#

btn4=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="4",command=lambda:btnClick(4),bg="#3399FF").grid(row=2,column=0)

btn5=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="5",command=lambda:btnClick(5),bg="#3399FF").grid(row=2,column=1)

btn6=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="6",command=lambda:btnClick(6),bg="#3399FF").grid(row=2,column=2)

Subraction=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="- ",command=lambda:btnClick("-"),bg="powder blue").grid(row=1,column=4)

#===============================================================================================#

btn7=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="7",command=lambda:btnClick(7),bg="#3399FF").grid(row=3,column=0)

btn8=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="8",command=lambda:btnClick(8),bg="#3399FF").grid(row=3,column=1)

btn9=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="9",command=lambda:btnClick(9),bg="#3399FF").grid(row=3,column=2)

Multiple=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="x",command=lambda:btnClick("*"),bg="powder blue").grid(row=3,column=3)

#===============================================================================================#


btn0=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="0",command=lambda:btnClick(0),bg="#3399FF").grid(row=4,column=1)

btnClear=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="C",bg="red",command=btnClearDisplay).grid(row=4,column=2)

btnEqual=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="=",bg="green",command=btnEqualsInput).grid(row=4,column=4)

Division=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="/ ",command=lambda:btnClick("/"),bg="powder blue").grid(row=4,column=3)

#===============================================================================================#            

Divisiondot=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text=".",command=lambda:btnClick("."),bg="powder blue").grid(row=4,column=0) 

Divisiondote=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text=") ",command=lambda:btnClick(")"),bg="powder blue").grid(row=2,column=4)   

Divisiondote2=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="( ",command=lambda:btnClick("("),bg="powder blue").grid(row=2,column=3)      

Divisiondote3=Button(window,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),
            text="^",command=lambda:btnClick("**"),bg="powder blue").grid(row=3,column=4) 

window.mainloop()