from tkinter import *
from tkinter import messagebox

def login_function():
    if user.get()=="" or password.get()=="":
        messagebox.showerror("Blank Input","You can not leave username and password balnk!")
    elif user.get()=="Ali" and password.get=="abc#123":
        messagebox.showinfo("Login successful","Your username and password are correct!")
    else :
        messagebox.showwarning("Input passed", "you have enterd"+user.get()+" "+password.get())

def showhide_pass():
    if showhide.get():
         E2.config(show="")
    else:
        E2.config(show="*")

        

window=Tk()
window.title("Login from")
window.resizable(False,False)


user=StringVar()
password=StringVar()
showhide=BooleanVar()

L1=Label(window,text="Login Form",font=("Century",18,"bold"))
L1.pack(padx=10,pady=10)

L2=Label(window,text="username",font=("Arial",14,"normal"))
L2.pack()

E1=Entry(window,font=("Arial",14,"normal"),textvariable=user)
E1.pack(padx=10)

L3=Label(window,text="password",font=("Arial",14,"normal"),pady=5)
L3.pack()

E2=Entry(window,font=("Arial",14,"normal"),show="*",textvariable=password)
E2.pack(padx=10)

c1=Checkbutton(window,text=" show / hide password",command=showhide_pass,variable=showhide)

B1=Button(window,text="Login",font=("Arial",16,"bold"),pady=5,padx=20,command=login_function)
B1.pack()

window.mainloop()
