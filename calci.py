import tkinter
from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry("450x450")
window.resizable(False,False)
window.configure(bg="black")


expression= ""
def show(value):
    global expression
    expression+=value
    res.config(text=expression)
def clear():
    global expression
    expression = ""
    res.config(text=expression)
def calculate ():
    global expression
    result=""
    if expression !="":
        try:
            result= eval(expression)
        except:
            result="error"
            expression= " "
        res.config(text=result)
        
res=Label(window,width=25,height=2,text=" " ,font=("arial",30))
res.pack()


Button(window,text="C" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="blue",command=lambda: clear()).place(x=20,y=50)
Button(window,text="/" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("/")).place(x=150,y=100)
Button(window,text="%" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("%")).place(x=290,y=100)
Button(window,text="*" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("*")).place(x=430,y=100)
Button(window,text="7" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("7")).place(x=10,y=200)
Button(window,text="8" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("8")).place(x=150,y=200)
Button(window,text="9" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("9")).place(x=290,y=200)
Button(window,text="-" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("-")).place(x=430,y=200)
Button(window,text="4" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("4")).place(x=10,y=300)
Button(window,text="5" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("5")).place(x=150,y=300)
Button(window,text="6" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("6")).place(x=290,y=300)
Button(window,text="+" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("+")).place(x=430,y=300)
Button(window,text="1" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("1")).place(x=10,y=400)
Button(window,text="2" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("2")).place(x=150,y=400)
Button(window,text="3" , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("3")).place(x=290,y=400)
Button(window,text="0" , width = 11,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show("0")).place(x=10,y=500)
Button(window,text="." , width = 5,   height = 1 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="grey",command=lambda: show(".")).place(x=290,y=500)
Button(window,text="=" , width = 5,   height = 3 ,font=("arial",30,"bold") ,bd=1,fg= "#fff", bg="yellow",command=lambda: calculate()).place(x=430,y=400)











window.mainloop()
