from tkinter import *

def sumbit_data():
    pass

def showhidepass1():
    if mypass1.get():
        E5.config(show=" ")
    else:
        E5.config(show="*")

def showhidepass2():
    if mypass2.get():
        E6.config(show=" ")
    else:
        E6.config(show=" ")




root=Tk()
root.title("Student registration form")
root.resizable(False,False)

gender=StringVar()
mypass1=BooleanVar()
mypass2=BooleanVar()


L1=Label(root,text="Student Registration form",font=("Claibri",20,"bold"))
L1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

L2=Label(root,text="Enter first name: ",font=("Claibri",14,"normal"))
L2.grid(row=1,column=0)

L3=Label(root,text="Enter last name: ",font=("Claibri",14,"normal"))
L3.grid(row=1,column=1)

E1=Entry(root,font=("Claibri",14,"normal"))
E1.grid(row=2,column=0,padx=10,pady=10)

E2=Entry(root,font=("Claibri",14,"normal"))
E2.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Enter Address: ",font=("Claibri",14,"normal"))
L4.grid(row=3,column=1,padx=10,pady=10)

L5=Label(root,text="Enter city : ",font=("Claibri",14,"normal"))
L5.grid(row=3,column=1,padx=10,pady=10)

E3=Entry(root,font=("Claibri",14,"normal"))
E3.grid(row=4,column=1,padx=10,pady=10)

E4=Entry(root,font=("Claibri",14,"normal"))
E4.grid(row=4,column=1,padx=10,pady=10)

L6=Label(root,text="select gender : ",font=("Claibri",14,"bold"))
L6.E4.grid(row=5,column=2,columnspan=2)

L7=Label(root,text="Male",font=("Claibri",14,"normal"))
L7.grid(row=6,column=0)

L8=Label(root,text="Female",font=("Claibri",14,"normal"))
L8.gird(row=6,column=1)

R1=Radiobutton(root,value="Male",textvariable=gender)
R1.grid(row=6,column=0)


R2=Radiobutton(root,value="female",textvariable=gender)
R2.grid(row=7,column=1)

L9=Label(root,text="Select Hobbies",font=("Claibri",16,"bold"))
L9.grid(row=8,column=0,columnspan=2)

cb1=Checkbutton(root,text="Cricket",font=("Claibri",14,"bold"))
cb1.grid(row=9,column=0)

cb2=Checkbutton(root,text="Football",font=("Claibri",14,"bold"))
cb2.grid(row=10,column=0)

cb3=Checkbutton(root,text="Chess",font=("Claibri",14,"bold"))
cb3.grid(row=11,column=0)

L10=Label(root,text="Type password",font=("Claibri",16,"bold"))
L10.grid(row=12,column=0,columnspan=2)

E5=Entry(root,font=("Claibri",14,"normal"),show="*")
E5.grid(row=13,column=0,padx=10,pady=10)

cb4=Checkbutton(root,text="show/ hide password",variable=mypass1,font=("Claibri",14,"bold"),command=showhidepass1)
cb4.grid(row=13,column=1)

L11=Label(root,text="Verify password",font=("Claibri",16,"bold"))
L11.grid(row=14,column=0,columnspan=2)

E6=Entry(root,font=("Claibri",14,"normal"),show="*")
E6.grid(row=15,column=0,padx=10,pady=10,columnspan=2)

cb5=Checkbutton(root,text="show/ hide password",font=("calibri",14,"bold"),variable=mypass2,command=showhidepass2)
cb5.grid(row=15,column=1)

B1=Button(root,text="sumbit",command=sumbit_data,font=("Claibri",14,"bold"),padx=5,pady=5)
B1.grid(row=16,column=0,padx=10,pady=10,columnspan=2)

root.mainloop()



