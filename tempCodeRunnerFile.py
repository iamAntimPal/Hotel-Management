from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector



class cust__Win :
     def __init__(self,root):
          self.root=root
          self.root.title("HOTEL MANAGEMENT SYSTEM")
          self.root.geometry("1295x570+235+220")
          self.root.resizable(False,False)

          #======================Veriables====================
          self.var_ref=StringVar()
          x=random.randint(1000,9999)
          self.var_ref.set(str(x))
          
          self.var_cust_name=StringVar()
          self.var_mother=StringVar()
          self.var_gender=StringVar()
          self.var_post=StringVar()
          self.var_mobile=StringVar()
          self.var_email=StringVar()
          self.var_nationality=StringVar()
          self.var_address=StringVar()
          self.var_idproof=StringVar()
          self.var_idnumber=StringVar()

          #================Title=====================

          lbl_title=Label(self.root ,text="ADD CUSTOMER DETAILS ", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
          lbl_title.place(x=0,y=0,width=1295,height=50)

           #=======================Logo==================

          img2=Image.open("Image/logo2.jpg")

          # img2.resize((100,40),Image.Resampling.LANCZOS)
          self.photoimg2=ImageTk.PhotoImage(img2)

          labimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE )
          labimg.place(x=5,y=2,width=100,height=40)

          #=======================Label frame======================
          
          labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",padx=2,font=("times new roman",12,"bold"),)
          labelframeleft.place(x=5,y=50,width=425,height=490)

          #========================labels and entry====================
          
          #cust ref
          
          lbl_cust_ref=Label(labelframeleft,text="CUSTOMER REF",font=("arial",12,"bold"),padx=2,pady=6)
          lbl_cust_ref.grid(row=0,column=0,sticky=W)
          entry_ref=ttk.Entry(labelframeleft,width=29, textvariable=self.var_ref,font=("arial",13,"bold"),justify=CENTER,state="readonly")
          entry_ref.grid(row=0,column=1)

          #cust name
          
          cname=Label(labelframeleft,text="CUSTOMER NAME",font=("arial",12,"bold"),padx=2,pady=6)
          cname.grid(row=1,column=0,sticky=W)
          txtcname=ttk.Entry(labelframeleft,width=29, textvariable=self.var_cust_name,font=("arial",13,"bold"),justify=CENTER)
          txtcname.grid(row=1,column=1)

          #mother name
          
          lblmname=Label(labelframeleft,text="MOTHER NAME",font=("arial",12,"bold"),padx=2,pady=6)
          lblmname.grid(row=2,column=0,sticky=W)
          txtmname=ttk.Entry(labelframeleft,width=29, textvariable=self.var_mother,font=("arial",13,"bold"),justify=CENTER)
          txtmname.grid(row=2,column=1)
          
          #Gender combo box
          
          label__gender=Label(labelframeleft,text="GENDER",font=("arial",12,"bold"),padx=2,pady=6)
          label__gender.grid(row=3,column=0,sticky=W)
          combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27, textvariable=self.var_gender,state="readonly")
          combo_gender["value"]=("Male","Female","Other")
          combo_gender.current(0)
          combo_gender.grid(row=3,column=1)

          #post code
          
          lblpostcode=Label(labelframeleft,text="POSTCODE",font=("arial",12,"bold"),padx=2,pady=6)
          lblpostcode.grid(row=4,column=0,sticky=W)
          textpostcode=ttk.Entry(labelframeleft,width=29, textvariable=self.var_post,font=("arial",13,"bold"),justify=CENTER)
          textpostcode.grid(row=4,column=1)

          #mobile number
          
          lblmobile=Label(labelframeleft,text="MOBILE",font=("arial",12,"bold"),padx=2,pady=6)
          lblmobile.grid(row=5,column=0,sticky=W)
          txtmobile=ttk.Entry(labelframeleft,width=29, textvariable=self.var_mobile,font=("arial",13,"bold"),justify=CENTER)
          txtmobile.grid(row=5,column=1)

          #Email
          
          lbl_cust_ref=Label(labelframeleft,text="EMAIL",font=("arial",12,"bold"),padx=2,pady=6)
          lbl_cust_ref.grid(row=6,column=0,sticky=W)
          txtEmail=ttk.Entry(labelframeleft,width=29, textvariable=self.var_email,font=("arial",13,"bold"),justify=CENTER)
          txtEmail.grid(row=6,column=1)

          #nationality
          
          lblNationality=Label(labelframeleft,text="NATIONALITY",font=("arial",12,"bold"),padx=2,pady=6)
          lblNationality.grid(row=7,column=0,sticky=W)
          combo_Nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27, textvariable=self.var_nationality,state="readonly")
          combo_Nationality["value"]=("Indain","American","British","Other")
          combo_Nationality.current(0)
          combo_Nationality.grid(row=7,column=1)
     
          #IDproof type combo box
     
          lblIdproof=Label(labelframeleft,text="ID PROOF TYPE",font=("arial",12,"bold"),padx=2,pady=6)
          lblIdproof.grid(row=8,column=0,sticky=W)
          combo_Id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27, textvariable=self.var_idproof,state="readonly")
          combo_Id["value"]=("Adhar Card","Driving Licence","Passport","Pan Card")
          combo_Id.current(0)
          combo_Id.grid(row=8,column=1)
     
          #Idnumber

          lblIdnumber=Label(labelframeleft,text="ID NUMBER",font=("arial",12,"bold"),padx=2,pady=6)
          lblIdnumber.grid(row=9,column=0,sticky=W)
          txtIdnumber=ttk.Entry(labelframeleft,width=29, textvariable=self.var_idnumber,font=("arial",13,"bold"),justify=CENTER)
          txtIdnumber.grid(row=9,column=1)
     
          #address
     
          lblAddress=Label(labelframeleft,text="ADDRESS",font=("arial",12,"bold"),padx=2,pady=6)
          lblAddress.grid(row=10,column=0,sticky=W)
          txtAddress=ttk.Entry(labelframeleft,width=29, textvariable=self.var_address,font=("arial",13,"bold"),justify=CENTER)
          txtAddress.grid(row=10,column=1)

#==============================button=========================================
          
          btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
          btn_frame.place(x=0,y=400,width=412,height=40)

          btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnAdd.grid(row=0,column=0,padx=1)

          btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnUpdate.grid(row=0,column=1,padx=1)

          btnDelete=Button(btn_frame,text="DELETE",command=self.mDelete , font=("arial",12,"bold"),cursor="hand2",bg="black",fg="gold",width=9)
          btnDelete.grid(row=0,column=2,padx=1)

          btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",cursor="hand2",fg="gold",width=9)
          btnReset.grid(row=0,column=3,padx=1)

#=====================Table frame search system=============================
          table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS AND SEARCH SYSTEM",padx=2,font=("times new roman",12,"bold"),)
          table_Frame.place(x=435,y=50,width=860,height=490)

          lblSearchBy=Label( table_Frame,text="SEARCH BY",font=("arial",12,"bold"),bg="red",fg="white")
          lblSearchBy.grid(row=0,column=0,sticky=W,padx=1)
          
          self.search_var=StringVar()

          combo_Search=ttk.Combobox(table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
          combo_Search["value"]=("REF","Mobile")
          combo_Search.current(0)
          combo_Search.grid(row=0,column=1,padx=1)
                 
          self.txt_search=StringVar()
          txtIdsearch=ttk.Entry(table_Frame,width=29,textvariable=self.txt_search,font=("arial",13,"bold"),justify=CENTER)
          txtIdsearch.grid(row=0,column=2,padx=1)


#==============================button=========================================

          btnSearch=Button(table_Frame,text="SEARCH",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",cursor="hand2",width=9)
          btnSearch.grid(row=0,column=3,padx=1)

          btnShowall=Button(table_Frame,text="SHOW ALL",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",cursor="hand2",width=9)
          btnShowall.grid(row=0,column=4,padx=1)


#==============================Show data table=========================================
          
          details_table=Frame(table_Frame,bd=2,relief=RIDGE)
          details_table.place(x=0,y=50,width=860,height=400)        

          Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
          Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

          self.cust_details_table=ttk.Treeview(details_table, column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
          Scroll_x.pack(side=BOTTOM,fill=X)
          Scroll_y.pack(side=RIGHT,fill=Y)
          Scroll_x.config(command=self.cust_details_table.xview)
          Scroll_y.config(command=self.cust_details_table.yview)

          self.cust_details_table.heading("ref",text="Refer No")
          self.cust_details_table.heading("name",text="Name")
          self.cust_details_table.heading("mother",text="Mother Name")
          self.cust_details_table.heading("gender",text="Gender")
          self.cust_details_table.heading("post",text="Post")
          self.cust_details_table.heading("mobile",text="Mobile")
          self.cust_details_table.heading("email",text="Email")
          self.cust_details_table.heading("nationality",text="Nationality")
          self.cust_details_table.heading("idproof",text="Id Proof")
          self.cust_details_table.heading("idnumber",text="Id Number")
          self.cust_details_table.heading("address",text="Address")
          self.cust_details_table["show"]="headings"

          self.cust_details_table.column("ref",width=100)
          self.cust_details_table.column("name",width=100)
          self.cust_details_table.column("mother",width=100)
          self.cust_details_table.column("gender",width=100)
          self.cust_details_table.column("post",width=100)
          self.cust_details_table.column("mobile",width=100)
          self.cust_details_table.column("email",width=100)
          self.cust_details_table.column("nationality",width=100)
          self.cust_details_table.column("idproof",width=100)
          self.cust_details_table.column("idnumber",width=100)
          self.cust_details_table.column("address",width=100)
     
          self.cust_details_table.pack(fill=BOTH,expand=1)
          self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
          self.fetch_data()
          
          #=========================ADD DATA==========================================
          
     def add_data(self):
          try:
               if self.var_mobile.get()=="" or self.var_mother.get()=="":
                    messagebox.showerror("Error","All fields are requaired ",parent=self.root)
               else:
                    conn=mysql.connector.connect(host="localhost", user="root",password="Antim@123",database="Hotelmanagement")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                                                              self.var_ref.get(),
                                                                                                                                                                                              self.var_cust_name.get(),
                                                                                                                                                                                              self.var_mother.get(),
                                                                                                                                                                                              self.var_gender.get(),
                                                                                                                                                                                              self.var_post.get(),
                                                                                                                                                                                              self.var_mobile.get(),
                                                                                                                                                                                              self.var_email.get(),
                                                                                                                                                                                              self.var_nationality.get(),
                                                                                                                                                                                              self.var_idproof.get(),
                                                                                                                                                                                              self.var_idnumber.get(),
                                                                                                                                                                                              self.var_address.get()
                                                                                                                                                                           ))
                    conn.commit()
                    self.fetch_data()
                    self.reset()
                    conn.close()
                    messagebox.showinfo("success","customer has been added",parent=self.root)
          except EXCEPTION as es:
               messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
               
          #=========================DATA FETCH==========================================
    
     def fetch_data(self):
           conn=mysql.connector.connect(host="localhost", user="root",password="Antim@123", database="Hotelmanagement")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from customer")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
               self.cust_details_table.delete(*self.cust_details_table.get_children())
               for i in rows:
                    self.cust_details_table.insert("",END,values=i)
               conn.commit()
               conn.close()
          
                    #=========================SET CURSOR==========================================
          
     def get_cursor(self,event=""):
          cursor_row=self.cust_details_table.focus()
          content=self.cust_details_table.item(cursor_row)
          row=content["values"]
          
          self.var_ref.set(row[0]),
          self.var_cust_name.set(row[1]),
          self.var_mother.set(row[2]),
          self.var_gender.set(row[3]),
          self.var_post.set(row[4]),
          self.var_mobile.set(row[5]),
          self.var_email.set(row[6]),
          self.var_nationality.set(row[7]),
          self.var_idproof.set(row[8]),
          self.var_idnumber.set(row[9]),
          self.var_address.set(row[10])
          
          #=========================UPDATE FUNCTION==========================================

     def update(self):
          if self.var_mobile.get() == "":
              messagebox.showerror("Error", "Please enter your mobile number", parent=self.root)
          else:
              conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123", database="Hotelmanagement")
              my_cursor = conn.cursor()
              query = "UPDATE customer SET name=%s, mother=%s, gender=%s, post=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s WHERE ref=%s"
              values = (
                  self.var_cust_name.get(),
                  self.var_mother.get(),
                  self.var_gender.get(),
                  self.var_post.get(),
                  self.var_mobile.get(),
                  self.var_email.get(),
                  self.var_nationality.get(),
                  self.var_idproof.get(),
                  self.var_idnumber.get(),
                  self.var_address.get(),
                  self.var_ref.get()
              )
              my_cursor.execute(query, values)
              conn.commit()
              self.fetch_data()
              self.reset()
              conn.close()
              messagebox.showinfo("Update", "Customer has been updated successfully", parent=self.root)


          #=========================DELETE FUNCTION==========================================
          
     def mDelete(self):
          mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
          if mDelete > 0:
             conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123", database="Hotelmanagement")
             my_cursor = conn.cursor()
             query = "DELETE FROM customer WHERE ref = %s"  # Assuming 'ref' is the primary key column
             value = (self.var_ref.get(),)
             my_cursor.execute(query, value)
             conn.commit()
             self.fetch_data()
             self.reset()
             conn.close()
             messagebox.showinfo("Success", "Customer deleted successfully", parent=self.root)
          else:
               if not mDelete:
                    messagebox.showerror("Error","Customer not found")


     #=========================RESET FUNCTION==========================================
          
     def reset(self):
         #self.var_ref.set(""),
          self.var_cust_name.set(""),
          self.var_mother.set(""),
          #self.var_gender.set(""),
          self.var_post.set(""),
          self.var_mobile.set(""),
          self.var_email.set(""),
          #self.var_nationality.set(""),
          #self.var_idproof.set(""),
          self.var_idnumber.set(""),
          self.var_address.set("")
          
          x=random.randint(1000,9999)
          self.var_ref.set(str(x))
     
     #=========================SEARCH FUNCTION==========================================
     
     def search(self):
          conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123", database="Hotelmanagement")
          my_cursor = conn.cursor()
    
          # Check if the search variable is empty or not
          if self.search_var.get() and self.txt_search.get():
              # Use prepared statements to avoid SQL injection
              query = f"SELECT * FROM customer WHERE {self.search_var.get()} LIKE %s"
              value = ('%' + self.txt_search.get() + '%',)
              
              my_cursor.execute(query, value)
              rows = my_cursor.fetchall()
              
              if len(rows) != 0:
                  self.cust_details_table.delete(*self.cust_details_table.get_children())
                  for row in rows:
                      self.cust_details_table.insert("", END, values=row)
                  conn.commit()
          else:
              messagebox.showwarning("Warning", "Please select a search criteria and enter a search term.", parent=self.root)
          conn.close()
          

if __name__=="__main__":
     root=Tk()
     obj=cust__Win(root)
     root.mainloop()