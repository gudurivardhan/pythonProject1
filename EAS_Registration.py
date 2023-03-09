from tkinter import *

import pandas as pd
import qrcode
from PIL import Image, ImageTk


class Registration:
    QR_path = None
    identry = None
    male_radio = None
    female_radio = None
    phoneentry = None
    nameentry = None


    def getvals(self):
        # Create a data  with student details

        id = emp_ID_value.get()
        name = namevalue.get()
        self.QR_path = self.generate_qr_code(id, name)
        employee_details = pd.DataFrame({
            "ID": [id],
            "Name": [name],
            "QR Code": [self.QR_path]
        })
        employee_details = employee_details.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        # Write the data to a CSV file
        employee_details.to_csv("employee_details.csv", mode='a', index=False, header=False)

        print("Employee details written to employee_details.csv")
        # Display the QR code in a new window

        qr_window = Toplevel()
        qr_window.title("QR Code")
        qr_window.geometry("600x500")
        f1 = Frame(qr_window, borderwidth=5, bg="grey", relief=SUNKEN)
        f1.pack(side=TOP, fill="x")
        l1 = Label(f1, text="Generated QR Code", font="Helvetica 30 bold", fg="red", pady=42, padx=50)
        l1.pack(fill=BOTH)
        # photo = PhotoImage(file=self.QR_path)
        img = Image.open(self.QR_path)
        img = img.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        pic_label = Label(qr_window, image=photo)
        pic_label.image = photo
        pic_label.pack()

    def generate_qr_code(self, employee_id, name):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(f"{employee_id},{name}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = f"employee{employee_id}.png"
        with open(img_path, "wb") as f:
            img.save(f)
        print(f"QR code generated for employee ID: {employee_id}")
        return img_path

    def clear_form(self):
        self.identry.delete(0, END)
        self.nameentry.delete(0, END)
        self.phoneentry.delete(0, END)
        gendervalue.set(None)

    def show_registration_form(self, root):
        reg_window = Toplevel(root)
        reg_window.geometry("644x560")
        reg_window.title("Registration Form")
        reg_window.configure(bg="Black")
        f1 = Frame(reg_window, borderwidth=5, bg="grey", relief=SUNKEN)
        f1.pack(side=TOP, fill="x")
        l1 = Label(f1, text="Attendance Registration Form", font="Helvetica 30 bold", fg="red", pady=42, padx=50)
        l1.pack(fill=BOTH)
        content_frame = Frame(reg_window, bg="white", width=500, height=500)
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        emp_ID = Label(content_frame, text="Employee ID", font="Helvetica 20 bold")
        name = Label(content_frame, text="Name", font="Helvetica 20 bold")
        gender = Label(content_frame, text="Gender", font="Helvetica 20 bold")
        phone = Label(content_frame, text="Phone", font="Helvetica 20 bold")
        emp_ID.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        name.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        phone.grid(row=2, column=2, padx=10, pady=10, sticky="ew")
        gender.grid(row=3, column=2, padx=10, pady=10, sticky="ew")
        # Tkinter variable for storing entries

        global emp_ID_value
        global namevalue
        global phonevalue
        global gendervalue
        emp_ID_value = StringVar()
        namevalue = StringVar()
        phonevalue = StringVar()
        gendervalue = StringVar()
        gendervalue.set(None)
        self.identry = Entry(content_frame, textvariable=emp_ID_value, )
        self.nameentry = Entry(content_frame, textvariable=namevalue)
        self.phoneentry = Entry(content_frame, textvariable=phonevalue)
        self.male_radio = Radiobutton(content_frame, text="Male", variable=gendervalue, value="Male",
                                      font="Helvetica 20 bold")
        self.female_radio = Radiobutton(content_frame, text="Female", variable=gendervalue, value="Female",
                                        font="Helvetica 20 bold")

        # Packing the Entries

        self.identry.grid(row=0, column=3)
        self.nameentry.grid(row=1, column=3)
        self.phoneentry.grid(row=2, column=3)
        self.male_radio.grid(row=3, column=3)
        self.female_radio.grid(row=3, column=4)
        Button(content_frame, text="Submit", font="Helvetica 16 bold",
               command=self.getvals).grid(row=5, column=3)
        Button(content_frame, text="Clear", font="Helvetica 16 bold",
               command=self.clear_form).grid(row=5,column=4)