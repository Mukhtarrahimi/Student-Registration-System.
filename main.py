from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

background = "#06283d"
framebg = "#ededed"
framefg = "#06283d"

root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)

file = pathlib.Path("student_data.xlsx")
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet['A1']="Registration No."
    sheet['B1']="Name"
    sheet['C1']="Class"
    sheet['D1']="Gender"
    sheet['E1']="DOB"
    sheet['F1']="Date Of Registration"
    sheet['G1']="Religion"
    sheet['H1']="Skill"
    sheet['I1']="Father Name"
    sheet['J1']="Mother Name"
    sheet['K1']="Father's Occupation"
    sheet['L1']="Mother's Occupation"
    
    file.save("student_data.xlsx")

# gender
def selection():
    value = radio.get()
    if value == 1:
        gender = "Male"
    elif value == 2:
        gender = "Female"

# Exit
def Exit():
    root.destroy()

# show img
def show_image():
    pass
# top frames
Label(root, text= "Email: Mukhtarrahimi110@gmail.com", width=10, height=3, bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
Label(root, text= "STUDENT REGISTRATION", width=10, height=2, bg="#c36464",fg="#ffffff", font="arial 20 bold").pack(side=TOP, fill=X)

# search box to update
search = StringVar()
Entry(root, textvariable=search, width=15,bd = 2, font="arial 20").place(x=820, y=70)
imageicon = PhotoImage(file="images/search.png")
srch = Button(root, text="Search", compound=LEFT, image=imageicon, width=123, bg="#68ddfa", font="arial 13 bold")
srch.place(x=1060, y=66)

imageicon1 = PhotoImage(file="images/Layer 4.png")
update_button = Button(root, image=imageicon1, bg="#c36464")
update_button.place(x=110, y=64)

# Registration and date
Label(root, text="Registration No:", bg=framebg, fg=framefg, font="arial 12").place(x=30, y=150)
Label(root, text="Date:", bg=framebg, fg=framefg, font="arial 12").place(x=500, y=150)

Registration = StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable = Registration, width=15, font="arial 10")
reg_entry.place(x=160, y=150)

# registration no()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(root, textvariable = Date, width=15, font="arial 10")
date_entry.place(x=550, y=150)

Date.set(d1)

# student details
obj = Label(root, text="Student Details", bg=framebg, fg=framefg, font="arial 20", width=900, bd=2, height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(obj, text="Name:", bg=framebg, fg=framefg, font="arial 13").place(x=30, y=50)
Label(obj, text="Date of Birth:", bg=framebg, fg=framefg, font="arial 13").place(x=30, y=100)
Label(obj, text="Gender:", bg=framebg, fg=framefg, font="arial 13").place(x=30, y=150)

Label(obj, text="Class:", bg=framebg, fg=framefg, font="arial 13").place(x=500, y=50)
Label(obj, text="Religion:", bg=framebg, fg=framefg, font="arial 13").place(x=500, y=100)
Label(obj, text="Skills:", bg=framebg, fg=framefg, font="arial 13").place(x=500, y=150)

Name = StringVar()
name_entry = Entry(obj, textvariable=Name, width=20, font="arial 10")
name_entry.place(x=160, y=50)

DOB = StringVar()
dob_entry = Entry(obj, textvariable=DOB, width=20, font="arial 10")
dob_entry.place(x=160, y=100)

radio = IntVar()
R1 = Radiobutton(obj, text="Male", variable=radio, value=1, bg=framebg, fg=framefg, command=selection)
R1.place(x=150, y=150)
R2 = Radiobutton(obj, text="Female", variable=radio, value=2, bg=framebg, fg=framefg, command=selection)
R2.place(x=200, y=150)

Religion = StringVar()
religion_entry = Entry(obj, textvariable=Religion, width=20, font="arial 10")
religion_entry.place(x=630, y=100)

Skills = StringVar()
skills_entry = Entry(obj, textvariable=Skills, width=20, font="arial 10")
skills_entry.place(x=630, y=150)

Class = Combobox(obj, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
Class.place(x=630, y=50)
Class.set("Select Class")

# parents details
obj2 = Label(root, text="Parents Details", bg=framebg, fg=framefg, font="arial 20", width=900, bd=2, height=220, relief=GROOVE)
obj2.place(x=30, y=470)

Label(obj2, text="Father's Name:", bg=framebg, fg=framefg, font="arial 13").place(x=30, y=50)
Label(obj2, text="Occupation:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)

Father_Name = StringVar()
FN_entry = Entry(obj2, textvariable=Father_Name, width=20, font="arial 10")
FN_entry.place(x=160, y=50)

Father_Occupation = StringVar()
FO_entry = Entry(obj2, textvariable=Father_Occupation, width=20, font="arial 10")
FO_entry.place(x=160, y=100)

Label(obj2, text="Mother's Name:", bg=framebg, fg=framefg, font="arial 13").place(x=500, y=50)
Label(obj2, text="Occupation:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=100)

Mother_Name = StringVar()
MN_entry = Entry(obj2, textvariable=Mother_Name, width=20, font="arial 10")
MN_entry.place(x=630, y=50)

Mother_Occupation = StringVar()
MO_entry = Entry(obj2, textvariable=Mother_Occupation, width=20, font="arial 10")
MO_entry.place(x=630, y=100)

# image
f = Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE)
f.place(x=1000, y=150)

img = PhotoImage(file="images/upload photo.png")
img_label = Label(f, image=img, bg="black")
img_label.pack()

# button
Button(root, text="Upload", bg="lightblue", font="arial 12 bold", width=19, height=2, command=show_image).place(x=1000, y=370)

save_button = Button(root, text="Save", bg="#68ddfa", font="arial 12 bold", width=19, height=2)
save_button.place(x=1000, y=450)

Button(
    root, text="Reset", bg="lightpink", font="arial 12 bold", width=19, height=2
).place(x=1000, y=530)

Button(
    root, text="Exit", bg="lightpink", font="arial 12 bold", width=19, height=2, command=Exit
).place(x=1000, y=610)

root.mainloop()
