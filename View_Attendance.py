from tkinter import *
import pandas as pd


def view_Details(root):
    scan_window = Toplevel(root)
    scan_window.geometry("644x560")
    scan_window.title("List of Attendees")
    scan_window.configure(bg="Black")
    f1 = Frame(scan_window, borderwidth=5, bg="grey", relief=SUNKEN)
    f1.pack(side=TOP, fill="x")
    l1 = Label(f1, text="Attendees List", font="Helvetica 30 bold", fg="red", pady=42, padx=50)
    l1.pack(fill=BOTH)
    employee_attendance = pd.read_csv("employee_attendance.csv")
    emp_arr = employee_attendance.to_numpy()
    canvas = Canvas(scan_window, height=200, width=300)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    frame = Frame(canvas)
    frame.pack(side=TOP, fill=BOTH, expand=1)
    for i in range(len(emp_arr)):
        for j in range(len(emp_arr[0])):
            label = Label(frame, text=str(emp_arr[i][j]),font="Helvetica 16 bold")
            label.grid(row=i, column=j, padx=5, pady=5)
    canvas.create_window((0, 0), window=frame, anchor=NW)
    canvas.configure(scrollregion=canvas.bbox(ALL))
