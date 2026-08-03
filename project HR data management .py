from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
    ):
        messagebox.showerror("Invalid or missing input", "Please enter all the values!")
    else:
        selected_skills = []
        if skill1.get():
            selected_skills.append("Python")
        if skill2.get():
            selected_skills.append("Excel")
        if skill3.get():
            selected_skills.append("Javascript")

        selected_choice = skills.get()
        if selected_choice:
            selected_skills.append(selected_choice)

        messagebox.showinfo(
            "Success",
            f"Employee registration submitted successfully!\nSkills: {', '.join(selected_skills) if selected_skills else 'None'}",
        )


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
education_list = ["HSC", "B.com", "BCA", "B.sc", "B.E", "M.Sc", "MCA"]
education.set(education_list[-1])
exp_list = [str(year) for year in range(16)]
experience.set(exp_list[0])
skills_options = ["Python", "Excel", "Javascript"]
skills.set(skills_options[0])

skill1 = BooleanVar()
skill2 = BooleanVar()
skill3 = BooleanVar()


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

op1 = ttk.Combobox(root, textvariable=education, values=education_list, state="readonly")
op1.grid(row=9, column=0, padx=10, pady=5)

L11 = Label(root, text="Enter Experience", font=("Claibri", 14, "normal"))
L11.grid(row=8, column=1, padx=10, pady=5)

op2 = ttk.Combobox(root, textvariable=experience, values=exp_list, state="readonly")
op2.grid(row=9, column=1, padx=10, pady=5)

L12 = Label(root, text="Enter Job Title", font=("Claibri", 14, "normal"))
L12.grid(row=10, column=0, padx=10, pady=5)

E7 = Entry(root, font=("Claibri", 14, "normal"), textvariable=job)
E7.grid(row=11, column=0, padx=10, pady=5)

L13 = Label(root, text="Enter Department", font=("Claibri", 14, "normal"))
L13.grid(row=10, column=1, padx=10, pady=5)

E8 = Entry(root, font=("Claibri", 14, "normal"), textvariable=department)
E8.grid(row=11, column=1, padx=10, pady=5)

L14 = Label(root, text="Enter Basic Salary", font=("Claibri", 14, "normal"))
L14.grid(row=12, column=0, padx=10, pady=5)

E9 = Entry(root, font=("Claibri", 14, "normal"), textvariable=basic_salary)
E9.grid(row=13, column=0, padx=10, pady=5)

L15 = Label(root, text="Enter Skills", font=("Claibri", 14, "normal"))
L15.grid(row=12, column=1, padx=10, pady=5)

cb1 = Checkbutton(root, text="Python", variable=skill1, font=("Claibri", 12, "normal"))
cb1.grid(row=13, column=1, padx=10, pady=2, sticky="w")

cb2 = Checkbutton(root, text="Excel", variable=skill2, font=("Claibri", 12, "normal"))
cb2.grid(row=15, column=1, padx=10, pady=2, sticky="w")

cb3 = Checkbutton(root, text="Javascript", variable=skill3, font=("Claibri", 12, "normal"))
cb3.grid(row=16, column=1, padx=10, pady=2, sticky="w")

B1 = Button(root, text="Submit", command=submit_data, font=("Claibri", 14, "normal"), padx=5, pady=5)
B1.grid(row=17, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()
