from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x570+235+220")
        self.root.resizable(False, False)

        # Variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomno = StringVar()
        self.var_meal = StringVar()
        self.var_noOfDays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subTotal = StringVar()
        self.var_Total = StringVar()

        # Title
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = PhotoImage(file="Image/logo2.jpg")
        self.photoimg2 = img2.subsample(3, 3)
        labimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        labimg2.place(x=5, y=2, width=100, height=40)

        # Label frame for room booking
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM BOOKING", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Labels and Entries
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20, font=("arial", 13, "bold"),
                                  justify=CENTER)
        entry_contact.grid(row=0, column=1, sticky=W)

        check_in_date = Label(labelframeleft, text="Check_In Date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(labelframeleft, width=29, textvariable=self.var_checkin, font=("arial", 13, "bold"),
                                     justify=CENTER)
        txtcheck_in_date.grid(row=1, column=1)
        txtcheck_in_date.bind("<Button-1>", lambda event, entry=txtcheck_in_date: self.show_calendar_checkin(event, entry))

        lbl_Check_out = Label(labelframeleft, text="Check_Out Date", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)
        txt_check_out = ttk.Entry(labelframeleft, width=29, textvariable=self.var_checkout, font=("arial", 13, "bold"),
                                  justify=CENTER)
        txt_check_out.grid(row=2, column=1)
        txt_check_out.bind("<Button-1>", lambda event, entry=txt_check_out: self.show_calendar_checkout(event, entry))

        # Other widgets...
        
    def show_calendar_checkin(self, event, entry):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day', year=2024, month=3, day=24)
        cal.pack(fill='both', expand=True)
        cal.bind('<<CalendarSelected>>', lambda event, entry=entry, top=top: self.set_date_checkin(event, entry, top))

    def show_calendar_checkout(self, event, entry):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day', year=2024, month=3, day=24)
        cal.pack(fill='both', expand=True)
        cal.bind('<<CalendarSelected>>', lambda event, entry=entry, top=top: self.set_date_checkout(event, entry, top))

    def set_date_checkin(self, event, entry, top):
        date_str = event.widget.get_date()
        entry.delete(0, 'end')
        entry.insert('end', date_str)
        top.destroy()

    def set_date_checkout(self, event, entry, top):
        date_str = event.widget.get_date()
        entry.delete(0, 'end')
        entry.insert('end', date_str)
        top.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
