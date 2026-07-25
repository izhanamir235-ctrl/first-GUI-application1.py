from tkinter import *
from tkinter import messagebox

def greetings():
    messagebox.showinfo("greetings!","goodmorning! "+username.get())

window=Tk()    
window.title("First GUI Application")
#window.geometry("600x400")
window.resizable(False,False)
username=StringVar()

l1=Label(text="First GUI Application",font=("Arial",18,"bold"))
l1.pack()

l2=Label(text=" Enter your name:",font=("Arial",14,"normal"))
l2.pack()
