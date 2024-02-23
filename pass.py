import tkinter
from tkinter import *
import random
window = Tk()
window.title("Password Generation")
window.geometry('450x450')
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
symbols='!@#$%^&*()_<>?/'
characters=uppercase + lowercase + numbers + symbols
label_characters=Label(window, text="Number of characters" , font=('Arial',12)).pack(padx=10)
character_length=Entry (window, font = "Arial 14")
character_length.pack(padx=10)

def generate_password():
    length=character_length.get()
    password="".join(random.sample(characters, int(length)))
    label_password.config(text="Generate Password:" + password)

Button(window,text="Generate password", command =generate_password , font=('Arial',12)).pack(padx=10)
label_password=Label(window, font=('Arial',12))
label_password.pack()
window.mainloop()
                        
