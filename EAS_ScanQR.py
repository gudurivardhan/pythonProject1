from tkinter import *
from tkinter import filedialog
import pandas as pd
import pyzbar.pyzbar as pyzbar
from PIL import Image

attendance_label = None


def uploadFile():
    file = filedialog.askopenfilename(initialdir='C:\\Users\\vardhan\\PycharmProjects\\pythonProject1',
                                      filetypes=[("PNG files", '.PNG')])
    print(file)
    if file != "":
        read_qr_code_image(file)


def read_qr_code_image(image_file):
    decoded_objs = pyzbar.decode(Image.open(image_file))
    mark_attendance(decoded_objs[0].data.decode())


def mark_attendance(qr_code_data):
    data_items = qr_code_data.split(',')
    employee_id = int(data_items[0])
    emp_name = data_items[1]
    employee_details = pd.read_csv("employee_details.csv")
    employee_attendance = pd.read_csv("employee_attendance.csv")
    if employee_id in employee_details["ID"].values:
        if employee_id not in employee_attendance["ID"].values:
            emp_attendance_details = pd.concat([employee_attendance, pd.DataFrame(
                {"ID": [employee_id], "Name": [emp_name], "Attendance": ["Present"]})], ignore_index=True)
            emp_attendance_details.to_csv("employee_attendance.csv", index=False)
            attendance_label.config(text=f"Attendance marked for employee ID: {employee_id}")
        else:
            attendance_label.config(text=f"Attendance already marked for employee ID: {employee_id}")
    else:
        attendance_label.config(text=f"Invalid employee ID: {employee_id}")


def scan_QR(root):
    scan_window = Toplevel(root)
    scan_window.geometry("644x560")
    scan_window.title("Scan QR Code")
    scan_window.configure(bg="Black")
    f1 = Frame(scan_window, borderwidth=5, bg="grey", relief=SUNKEN)
    f1.pack(side=TOP, fill="x")
    l1 = Label(f1, text="Scanner for QR code", font="Helvetica 30 bold", fg="red", pady=42, padx=50)
    l1.pack(fill=BOTH)
    content_frame = Frame(scan_window, bg="white", width=500, height=500)
    content_frame.place(relx=0.5, rely=0.75, anchor="center")
    l1 = Label(content_frame, text="Upload QR Code", font="Helvetica 30 bold")
    l1.grid(row=1, column=1)
    b1 = Button(content_frame, text="Upload QR", width=20, command=uploadFile)
    b1.grid(row=2, column=1)
    global attendance_label
    attendance_label = Label(content_frame, text="", font="Helvetica 16")
    attendance_label.grid(row=3, column=1)
