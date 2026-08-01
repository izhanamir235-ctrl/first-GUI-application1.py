from tkinter import *
from tkinter import messagebox


def submit_data():
    if (
        fname.get() == ""
        or lname.get() == ""
        or address.get() == ""
        or city.get() == ""
        or education.get() == ""
        or experience.get() == ""
        or job.get() == ""
        or department.get() == ""
        or basic_salary.get() == ""
        or skills.get() == ""
    ):
        messagebox.showerror("Invalid or missing input", "Please enter all the values!")
    else:
        messagebox.showinfo("Success", "Employee registration submitted successfully!")


root = Tk()
root.title("HR report of employees")
root.resizable(False, False)

gender = StringVar(value="Male")
fname = StringVar()
lname = StringVar()
address = StringVar()
city = StringVar()
education = StringVar()
experience = StringVar()
job = StringVar()
department = StringVar()
skills = StringVar()
basic_salary = StringVar()


L1 = Label(root, text="Employyes registation form", font=("Claibri", 20, "bold"))
L1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

L2 = Label(root, text="Enter first name: ", font=("Claibri", 14, "normal"))
L2.grid(row=1, column=0)

L3 = Label(root, text="Enter last name: ", font=("Claibri", 14, "normal"))
L3.grid(row=1, column=1)

E1 = Entry(root, font=("Claibri", 14, "normal"), textvariable=fname)
E1.grid(row=2, column=0, padx=10, pady=10)

E2 = Entry(root, font=("Claibri", 14, "normal"), textvariable=lname)
E2.grid(row=2, column=1, padx=10, pady=10)

L4 = Label(root, text="Enter Address: ", font=("Claibri", 14, "normal"))
L4.grid(row=3, column=0, padx=10, pady=10)

L5 = Label(root, text="Enter city: ", font=("Claibri", 14, "normal"))
L5.grid(row=3, column=1, padx=10, pady=10)

E3 = Entry(root, font=("Claibri", 14, "normal"), textvariable=address)
E3.grid(row=4, column=0, padx=10, pady=10)

E4 = Entry(root, font=("Claibri", 14, "normal"), textvariable=city)
E4.grid(row=4, column=1, padx=10, pady=10)

L6 = Label(root, text="Select gender: ", font=("Claibri", 14, "normal"))
L6.grid(row=5, column=0, columnspan=2)

R1 = Radiobutton(root, text="Male", variable=gender, value="Male")
R1.grid(row=6, column=0, padx=10, pady=5)

R2 = Radiobutton(root, text="Female", variable=gender, value="Female")
R2.grid(row=6, column=1, padx=10, pady=5)

L9 = Label(root, text="Select profile", font=("Claibri", 16, "normal"))
L9.grid(row=7, column=0, columnspan=2, pady=10)

L10 = Label(root, text="Enter Education", font=("Claibri", 14, "normal"))
L10.grid(row=8, column=0, padx=10, pady=5)

E5 = Entry(root, font=("Claibri", 14, "normal"), textvariable=education)
E5.grid(row=8, column=1, padx=10, pady=5)

L11 = Label(root, text="Enter Experience", font=("Claibri", 14, "normal"))
L11.grid(row=9, column=0, padx=10, pady=5)

E6 = Entry(root, font=("Claibri", 14, "normal"), textvariable=experience)
E6.grid(row=9, column=1, padx=10, pady=5)

L12 = Label(root, text="Enter Job Title", font=("Claibri", 14, "normal"))
L12.grid(row=10, column=0, padx=10, pady=5)

E7 = Entry(root, font=("Claibri", 14, "normal"), textvariable=job)
E7.grid(row=10, column=1, padx=10, pady=5)

L13 = Label(root, text="Enter Department", font=("Claibri", 14, "normal"))
L13.grid(row=11, column=0, padx=10, pady=5)

E8 = Entry(root, font=("Claibri", 14, "normal"), textvariable=department)
E8.grid(row=11, column=1, padx=10, pady=5)

L14 = Label(root, text="Enter Basic Salary", font=("Claibri", 14, "normal"))
L14.grid(row=12, column=0, padx=10, pady=5)

E9 = Entry(root, font=("Claibri", 14, "normal"), textvariable=basic_salary)
E9.grid(row=12, column=1, padx=10, pady=5)

L15 = Label(root, text="Enter Skills", font=("Claibri", 14, "normal"))
L15.grid(row=13, column=0, padx=10, pady=5)

E10 = Entry(root, font=("Claibri", 14, "normal"), textvariable=skills)
E10.grid(row=13, column=1, padx=10, pady=5)

B1 = Button(root, text="Submit", command=submit_data, font=("Claibri", 14, "normal"), padx=5, pady=5)
B1.grid(row=14, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()
