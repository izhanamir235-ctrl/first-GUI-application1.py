from tkinter import *
from tkinter import messagebox

def greetings():
    messagebox.showinfo("greetings!","goodmorning! "+username.get())

window=Tk()    
window.title("First GUI Application")
#window.geometry("600x400")
window.resizable(False,False)
username=StringVar()

L1=Label(text="First GUI Application",font=("Arial",18,"bold"))
L1.pack()

L2=Label(text=" Enter your name:",font=("Arial",14,"normal"))
L2.pack()

E1=Entry(font=("Arial",14,"normal"),textvariable=username)
E1.pack()

B1=Button(text="Click Here!",font=("Arial",14,"bold"))
B1.pack()

window.mainloop()