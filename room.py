from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar


class Roombooking :
     def __init__(self,root):
          self.root=root
          self.root.title("HOTEL MANAGEMENT SYSTEM")
          self.root.geometry("1295x570+235+220")
          self.root.resizable(False,False)

          #======================Veriables====================

          self.var_contact=StringVar()
          self.var_checkin=StringVar()
          self.var_checkout=StringVar()
          self.var_roomtype=StringVar()
          self.var_roomno=StringVar()
          self.var_meal=StringVar()
          self.var_noOfDays=StringVar()
          self.var_paidtax=StringVar()
          self.var_subTotal=StringVar()
          self.var_Total=StringVar()

          #================Title=====================

          lbl_title=Label(self.root ,text="ROOM BOOKING DETAILS ", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
          lbl_title.place(x=0,y=0,width=1295,height=50)

           #=======================Logo==================

          img2=Image.open("Image/logo2.jpg")

          # img2.resize((100,40),Image.LANCZOS)
          self.photoimg2=ImageTk.PhotoImage(img2)

          labimg2=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE )
          labimg2.place(x=5,y=2,width=100,height=40)

          #=======================Label frame======================
          
          labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING",padx=2,font=("times new roman",12,"bold"),)
          labelframeleft.place(x=5,y=50,width=425,height=490)

 #========================labels and entry====================
          
          #cust contact
          
          lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
          lbl_cust_contact.grid(row=0,column=0,sticky=W)
          entry_contact=ttk.Entry(labelframeleft, textvariable=self.var_contact,width=20,font=("arial",13,"bold"),justify=CENTER)
          entry_contact.grid(row=0,column=1,sticky=W)
          
     #fetch data button
     
          btnfetchData=Button(labelframeleft,text="Fetch Data", command=self.fetch_contact,font=("arial",10,"bold"),bg="black",cursor="hand2",fg="gold",width=8)
          btnfetchData.place(x=340,y=4)

          #check in date
          
          check_in_date=Label(labelframeleft,text="Check_In Date",font=("arial",12,"bold"),padx=2,pady=6)
          check_in_date.grid(row=1,column=0,sticky=W)
          txtcheck_in_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("arial",13,"bold"),justify=CENTER)
          txtcheck_in_date.grid(row=1,column=1)
          txtcheck_in_date.bind("<Button-1>", lambda event, entry=txtcheck_in_date: self.show_calendar_checkin(event, entry))


          #check_out Date
          
          lbl_Check_out=Label(labelframeleft,text="Check_Out Date",font=("arial",12,"bold"),padx=2,pady=6)
          lbl_Check_out.grid(row=2,column=0,sticky=W)
          txt_check_out=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("arial",13,"bold"),justify=CENTER)
          txt_check_out.grid(row=2,column=1)
          txt_check_out.bind("<Button-1>", lambda event, entry=txt_check_out: self.show_calendar_checkout(event, entry))
          
          #Room type
          
          label__RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
          label__RoomType.grid(row=3,column=0,sticky=W)
          combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_roomtype,width=27,state="readonly")
          combo_RoomType["value"]=("Single","Double","Luxury")
          combo_RoomType.current(0)
          combo_RoomType.grid(row=3,column=1)

          #Room No
          
          lblRoomAvailable=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
          lblRoomAvailable.grid(row=4,column=0,sticky=W)
          textAvailable=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"),textvariable=self.var_roomno,justify=CENTER)
          
          textAvailable.grid(row=4,column=1)

          #Meal
          
          lblMeal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
          lblMeal.grid(row=5,column=0,sticky=W)
          txtMeal=ttk.Combobox(labelframeleft,width=27,font=("arial",13,"bold"),textvariable=self.var_meal,justify=CENTER,state="readonly")
          txtMeal["value"]=("What you want","Breakfast","Lunch","Dinner","Water","Juice","Fast Food")
          txtMeal.current(0)
          txtMeal.grid(row=5,column=1)

          #No of Days
          
          lbl_NoOfDays=Label(labelframeleft,text="No Of Days",font=("arial",12,"bold"),padx=2,pady=6)
          lbl_NoOfDays.grid(row=6,column=0,sticky=W)
          txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noOfDays,font=("arial",13,"bold"),justify=CENTER)
          txtNoOfDays.grid(row=6,column=1)

          #Paid Tax
          
          lblNationality=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
          lblNationality.grid(row=7,column=0,sticky=W)
          txtNationality=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("arial",13,"bold"),justify=CENTER)
          txtNationality.grid(row=7,column=1)
     
          #subtotal
     
          lblIdproof=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
          lblIdproof.grid(row=8,column=0,sticky=W)
          txtIdproof=ttk.Entry(labelframeleft,width=29,textvariable=self.var_subTotal,font=("arial",13,"bold"),justify=CENTER)
          txtIdproof.grid(row=8,column=1)
     
          #Total

          lblAddress=Label(labelframeleft,text="Total",font=("arial",12,"bold"),padx=2,pady=6)
          lblAddress.grid(row=9,column=0,sticky=W)
          txtAddress=ttk.Entry(labelframeleft,width=29,textvariable=self.var_Total,font=("arial",13,"bold"),justify=CENTER)
          txtAddress.grid(row=9,column=1)
 
#============================== Bill button=========================================         
          

          btnAdd=Button(labelframeleft,text="BILL",command=self.calculate_bill,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnAdd.grid(row=10,column=0,padx=1)

#==============================button=========================================
          
          labelframeleft=Frame(labelframeleft,bd=2,relief=RIDGE)
          labelframeleft.place(x=0,y=400,width=412,height=40)

          btnAdd=Button(labelframeleft,text="ADD",command=self.add_customer_data,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnAdd.grid(row=0,column=0,padx=1)

          btnUpdate=Button(labelframeleft,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnUpdate.grid(row=0,column=1,padx=1)

          btnDelete=Button(labelframeleft,text="DELETE",command=self.mDelete,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnDelete.grid(row=0,column=2,padx=1)

          btnReset=Button(labelframeleft,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnReset.grid(row=0,column=3,padx=1)

          #===============Right side Image=================
          
          img3=Image.open("Image/bed3.jpg")

          img3.resize((550,300),Image.Resampling.LANCZOS)
          self.photoimg3=ImageTk.PhotoImage(img3)
          labimg2=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE )
          labimg2.place(x=760,y=55,width=550,height=300)

#=====================Table frame search system=============================
          table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS AND SEARCH SYSTEM",padx=2,font=("times new roman",12,"bold"),)
          table_Frame.place(x=435,y=280,width=860,height=260)

          lblSearchBy=Label( table_Frame,text="SEARCH BY",font=("arial",12,"bold"),bg="red",fg="white")
          lblSearchBy.grid(row=0,column=0,sticky=W,padx=1)

          self.search_var=StringVar()
          
          combo_Search=ttk.Combobox(table_Frame,font=("arial",12,"bold"),textvariable=self.search_var,width=24,state="readonly")
          combo_Search["value"]=("roomno","contact")
          combo_Search.current(0)
          combo_Search.grid(row=0,column=1,padx=1)

          self.txt_search=StringVar()
          
          txtIdsearch=ttk.Entry(table_Frame,width=29,textvariable=self.txt_search,font=("arial",13,"bold"),justify=CENTER)
          txtIdsearch.grid(row=0,column=2,padx=1)


#==============================button=========================================

          btnSearch=Button(table_Frame,text="SEARCH",command=self.search,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnSearch.grid(row=0,column=3,padx=1)

          btnShowall=Button(table_Frame,text="SHOW ALL",command=self.fetch_data,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnShowall.grid(row=0,column=4,padx=1)






#==============================Show data table=========================================
          
          details_table=Frame(table_Frame,bd=2,relief=RIDGE)
          details_table.place(x=0,y=50,width=860,height=180)        

          Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
          Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

          self.room_table=ttk.Treeview(details_table, column=("contact","checkin","checkout","room_type","roomno","meal","no of days","paid_tax","sub_total","total") ,xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
          Scroll_x.pack(side=BOTTOM,fill=X)
          Scroll_y.pack(side=RIGHT,fill=Y)
          Scroll_x.config(command=self.room_table.xview)
          Scroll_y.config(command=self.room_table.yview)

          self.room_table.heading("contact", text="Contact")
          self.room_table.heading("checkin", text="Check-in")
          self.room_table.heading("checkout", text="Check-out")
          self.room_table.heading("room_type", text="Room Type")
          self.room_table.heading("roomno", text="Room No")
          self.room_table.heading("meal", text="Meal")
          self.room_table.heading("no of days", text="No Of Days")
          self.room_table.heading("paid_tax", text="Paid Tax")
          self.room_table.heading("sub_total", text="Aub Total")
          self.room_table.heading("total", text="Total")
          self.room_table["show"]="headings"

          self.room_table.column("contact",width=100)
          self.room_table.column("checkin",width=100)
          self.room_table.column("checkout",width=100)
          self.room_table.column("room_type",width=100)
          self.room_table.column("roomno",width=100)
          self.room_table.column("meal",width=100)
          self.room_table.column("no of days",width=100)     
          self.room_table.column("paid_tax",width=100)     
          self.room_table.column("sub_total",width=100)     
          self.room_table.column("total",width=100)     
          self.room_table.pack(fill=BOTH,expand=1)
          
          self.room_table.pack(fill=BOTH,expand=1)
          self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
          self.fetch_data()


                              #=========================SET CURSOR==========================================
          
     def get_cursor(self,event=""):
          cursor_row=self.room_table.focus()
          content=self.room_table.item(cursor_row)
          row=content["values"]      
          self.var_contact.set(row[0]),
          self.var_checkin.set(row[1]),
          self.var_checkout.set(row[2]),
          self.var_roomtype.set(row[3]),
          self.var_roomno.set(row[4]),
          self.var_meal.set(row[5]),
          self.var_noOfDays.set(row[6]),
          self.var_paidtax.set(row[7]),
          self.var_subTotal.set(row[8]),
          self.var_Total.set(row[9])
          
          #===============fetch data in cutomer table using contact=============
     
     def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Enter Contact Number",parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123", database="Hotelmanagement")
                my_cursor = conn.cursor()

                # Execute the SQL query to fetch customer details
                query = "SELECT * FROM customer WHERE Mobile = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                print(row)
                
                if row is None:
                    messagebox.showerror("Error", "Customer not found with this contact number", parent=self.root)
                else:
                    # Update labels with fetched data
                    self.lbl_name.config(text="Name: " + row[0])
                    self.lbl_gender.config(text="Gender: " + row[1])
                    self.lbl_email.config(text="Email: " + row[2])
                    self.lbl_nationality.config(text="Nationality: " + row[3])
                    self.lbl_address.config(text="Address: " + row[4])

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error connecting to database: {e}", parent=self.root)

            finally:
                # Close the database connection
                if conn.is_connected():
                    my_cursor.close()
                    conn.close()
     
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=455 , y=55, width=300,height=180)
                
                lblName=Label(showDataframe,text="Name",font="arial 12 bold")
                lblName.place(x=0,y=0)
                
                self.lbl_name=Label(showDataframe, text=row, font="arial 12 bold")
                self.lbl_name.place(x=90,y=0)
                
                     #=========================GENDER ==========================================
                conn=mysql.connector.connect(host="localhost", user="root",password="Antim@123",database="Hotelmanagement")
                my_cursor=conn.cursor()
                querry=(" select gender from customer where Mobile =%s")
                
                
                lblName=Label(showDataframe,text="Gender",font="arial 12 bold")
                lblName.place(x=0,y=30)
                
                self.lbl_gender=Label(showDataframe,text=row,font="arial 12 bold")
                self.lbl_gender.place(x=90,y=30)
        
                #=========================EMAIL==========================================
                conn=mysql.connector.connect(host="localhost", user="root",password="Antim@123",database="Hotelmanagement")
                my_cursor=conn.cursor()
                querry=(" select email from customer where Mobile =%s")
                
                lblName=Label(showDataframe,text="Email",font="arial 12 bold")
                lblName.place(x=0,y=60)
                                    
                self.lbl_email=Label(showDataframe,text=row,font="arial 12 bold")
                self.lbl_email.place(x=90,y=60)
                
                #=========================Nationality==========================================
                conn=mysql.connector.connect(host="localhost", user="root",password="Antim@123",database="Hotelmanagement")
                my_cursor=conn.cursor()
                querry=(" select nationality from customer where Mobile =%s")
                
                lblName=Label(showDataframe,text="Nationality",font="arial 12 bold")
                lblName.place(x=0,y=90)
                                    
                self.lbl_nationality=Label(showDataframe,text=row,font="arial 12 bold")
                self.lbl_nationality.place(x=90,y=90)
                
                #=========================Address=========================================       
                        
                conn=mysql.connector.connect(host="localhost", user="root",password="Antim@123",database="Hotelmanagement")
                my_cursor=conn.cursor()
                querry=(" select address from customer where Mobile =%s")
                
                lblName=Label(showDataframe,text="Address",font="arial 12 bold")
                lblName.place(x=0,y=120)
                
                self.lbl_address=Label(showDataframe,text=row,font="arial 12 bold")
                self.lbl_address.place(x=90,y=120)
                  
                  #================== Add data==============================
          
     def add_customer_data(self):
          contact = self.var_contact.get()
          checkin = self.var_checkin.get()
          checkout = self.var_checkout.get()
          room_type = self.var_roomtype.get()
          room_available = self.var_roomno.get()
          meal = self.var_meal.get()
          no_of_days = self.var_noOfDays.get()
          paid_tax = self.var_paidtax.get()
          sub_total = self.var_subTotal.get()
          total = self.var_Total.get()

          if contact == "" or checkin == "" or checkout == "" or room_type == "" or room_available == "" or meal == "" or no_of_days == "" or paid_tax == "" or sub_total == "" or total == "":
              messagebox.showerror("Error", "All fields are required", parent=self.root)
          else:
              try:
                  # Connect to the database
                  conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123", database="Hotelmanagement")
                  my_cursor = conn.cursor()

                  # Insert customer data into the database
                  query = "INSERT INTO room (contact, CheckIn, CheckOut, room_type, roomno, Meal, NoOfDays, paid_tax, sub_total, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                  values = (contact, checkin, checkout, room_type, room_available, meal, no_of_days, paid_tax, sub_total, total)
                  my_cursor.execute(query, values)

                  # Commit the transaction
                  conn.commit()
                  messagebox.showinfo("Success", "Customer data added successfully", parent=self.root)

              except mysql.connector.Error as e:
                  messagebox.showerror("Error", f"Error adding customer data: {e}", parent=self.root)

              finally:
                  # Close the database connection
                  if conn.is_connected():
                       self.fetch_data()
                       self.reset()
                       my_cursor.close()
                       conn.close()

     def calculate_bill(self):
        try:
            # Calculate subtotal based on room type and number of days
            room_type = self.var_roomtype.get()
            no_of_days = int(self.var_noOfDays.get())
            room_rate = 0  # Predefined room rates
            if room_type == "Single":
                room_rate = 1500 # Example rate for Single room
            elif room_type == "Double":
                room_rate = 3000  # Example rate for Double room
            elif room_type == "Luxury":
                room_rate = 5000  # Example rate for Luxury room

            subtotal = room_rate * no_of_days

            # Calculate meal charges based on selected meals
            meal_charge = 0
            selected_meal = self.var_meal.get()
            if "Breakfast" in selected_meal:
                meal_charge += 1000  # Example breakfast charge
            if "Lunch" in selected_meal:
                meal_charge += 1500  # Example lunch charge
            if "Dinner" in selected_meal:
                meal_charge += 2000  # Example dinner charge
            if "Water" in selected_meal:
                meal_charge += 50  # Example water charge
            if "Juice" in selected_meal:
                meal_charge += 200  # Example juice charge
            if "Fast Food" in selected_meal:
                meal_charge += 1500  # Example fast food charge

            paid_tax = (subtotal + meal_charge) * .18  # Assuming 10% tax rate
            total = subtotal + meal_charge + paid_tax

            # Update entry fields with calculated values
            self.var_paidtax.set("{:.2f}".format(paid_tax))  # Format to two decimal places
            self.var_subTotal.set("{:.2f}".format(subtotal + meal_charge))
            self.var_Total.set("{:.2f}".format(total))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of days", parent=self.root)

          #=========================SEARCH FUNCTION==========================================

     def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123", database="Hotelmanagement")
        my_cursor = conn.cursor()

        # Check if the search variable is empty or not
        if self.search_var.get() and self.txt_search.get():
            # Use prepared statements to avoid SQL injection
            query = f"SELECT * FROM room WHERE `{self.search_var.get()}` LIKE %s"
            value = ('%' + self.txt_search.get() + '%',)

            my_cursor.execute(query, value)
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                    self.room_table.insert("", END, values=row)
                conn.commit()
        else:
            messagebox.showwarning("Warning", "Please select a search criteria and enter a search term.", parent=self.root)
        conn.close()


#=========================Fetch data============================
     def fetch_data(self):
           conn=mysql.connector.connect(host="localhost", user="root",password="Antim@123", database="Hotelmanagement")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from room")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
               self.room_table.delete(*self.room_table.get_children())
               for i in rows:
                    self.room_table.insert("",END,values=i)
               conn.commit()
               conn.close()
               
              #=========================UPDATE FUNCTION==========================================

     def update(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error", "Enter Room Number", parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123", database="Hotelmanagement")
                my_cursor = conn.cursor()

                # Check if the room number exists in the database
                room_query = "SELECT * FROM room WHERE roomno = %s"
                room_value = (self.var_roomno.get(),)
                my_cursor.execute(room_query, room_value)
                room_row = my_cursor.fetchone()

                if room_row is None:
                    messagebox.showerror("Error", "Room number does not exist in the database", parent=self.root)
                else:
                    # Update customer details in the database
                    update_query = "UPDATE room SET contact = %s, checkin = %s, checkout = %s, room_type = %s, Meal = %s, NoOfDays = %s, paid_tax = %s, sub_total = %s, total = %s WHERE roomno = %s"
                    update_values = (
                        self.var_contact.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_meal.get(),
                        self.var_noOfDays.get(),
                        self.var_paidtax.get(),
                        self.var_subTotal.get(),
                        self.var_Total.get(),
                        self.var_roomno.get()
                    )
                    my_cursor.execute(update_query, update_values)

                    conn.commit()
                    messagebox.showinfo("Success", "Customer details updated successfully", parent=self.root)
                    self.fetch_data()
                    self.reset()

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error connecting to database: {e}", parent=self.root)

            finally:
                # Close the database connection
                if conn.is_connected():
                    my_cursor.close()
                    conn.close()
         #======================= Delete===================
     
     def mDelete(self):
          mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
          if mDelete > 0:
             conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123", database="Hotelmanagement")
             my_cursor = conn.cursor()
             query = "DELETE FROM room WHERE roomno = %s"  # Assuming 'ref' is the primary key column
             value = (self.var_roomno.get(),)
             my_cursor.execute(query, value)
             conn.commit()
             conn.close()
             messagebox.showinfo("Success", "Customer deleted successfully", parent=self.root)
          else:
               if not mDelete:
                    return
          self.fetch_data()
          self.reset()
          
     def show_calendar_checkin(self, event, entry):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day', year=2024, month=4, day=1)
        cal.pack(fill='both', expand=True)
        cal.bind('<<CalendarSelected>>', lambda event, entry=entry, top=top: self.set_date_checkin(event, entry, top))

     def show_calendar_checkout(self, event, entry):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day', year=2024, month=3, day=8)
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
          
          
          #=========================RESET FUNCTION==========================================
          
     def reset(self):
         #self.var_ref.set(""),
          self.var_contact.set(""),
          self.var_checkin.set(""),
          self.var_checkout.set(""),
          self.var_meal.set(""),
          self.var_noOfDays.set(""),
          self.var_paidtax.set(""),
          self.var_roomno.set(""),
          self.var_subTotal.set(""),
          self.var_Total.set("")
          

if __name__=="__main__":
     root=Tk()
     obj=Roombooking(root)
     root.mainloop()