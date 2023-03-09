from tkinter import *

import EAS_Registration
import EAS_ScanQR


def open_registration_form():
    obj = EAS_Registration.Registration()
    obj.show_registration_form(root)


def open_scan_form():
    EAS_ScanQR.scan_QR(root)


try:
    root = Tk()
    root.geometry("644x544")
    root.configure(bg="red")
    root.title("Employee Attendance System")
    f1 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
    f1.pack(side=TOP, fill="x")
    l1 = Label(f1, text="Employee Attendance System", font="Helvetica 30 bold", fg="red", pady=42, padx=50)
    l1.pack(fill=BOTH)
    content_frame = Frame(root, bg="white", width=200, height=200)
    content_frame.place(relx=0.5, rely=0.5, anchor="center")

    register = Button(content_frame, text="Register", font="Helvetica 16 bold", command=open_registration_form)
    scan = Button(content_frame, text="Scan QR", font="Helvetica 16 bold", command=open_scan_form)

    register.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
    scan.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

    root.mainloop()
except KeyboardInterrupt:
    pass
