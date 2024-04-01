from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
from tkinter import simpledialog

class Detail_win :
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x570+235+220")
        self.root.resizable(False,False)
        
        self.entry_floor=StringVar()
        self.entry_RoomNo=StringVar()
        self.combo_RoomType=StringVar()
        
        #================Title=====================
        lbl_title=Label(self.root ,text="ROOM ADDING DEPARTMENT ", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
         #=======================Logo==================
        img2=Image.open("Image/logo2.jpg")
        # img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        labimg2=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE )
        labimg2.place(x=5,y=2,width=100,height=40)
        #=======================Label frame======================
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Rooms Add",foreground="green",padx=2,font=("times new roman",12,"bold"),)
        labelframeleft.place(x=5,y=60,width=600,height=400)
        
#====================Table frame search system=============================
        table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS AND SEARCH SYSTEM",padx=2,font=("times new roman",12,"bold"),)
        table_Frame.place(x=650,y=60,width=600,height=400)
        
        
        Scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)
        # Treeview widget for displaying data
        self.Detail_table = ttk.Treeview(table_Frame, column=("Floor", "RoomNo", "room type"),
                                        xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.Detail_table.xview)
        Scroll_y.config(command=self.Detail_table.yview)

        self.Detail_table.heading("Floor", text="Floor")
        self.Detail_table.heading("RoomNo", text="Room No")
        self.Detail_table.heading("room type", text="Room Type")
        self.Detail_table["show"] = "headings"

        self.Detail_table.column("Floor", width=100)
        self.Detail_table.column("RoomNo", width=100)
        self.Detail_table.column("room type", width=100)

        self.Detail_table.pack(fill=BOTH, expand=1)
        self.Detail_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


     #========================labels and entry====================
          
          #Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        entry_floor=ttk.Combobox(labelframeleft, width=20,textvariable=self.entry_floor,font=("arial",13,"bold"),justify=CENTER)
        entry_floor["value"]=("First","Second","Third","Fourth")
        entry_floor.current(0)
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=2,column=0,sticky=W)
        entry_RoomNo=ttk.Entry(labelframeleft, width=20,textvariable=self.entry_RoomNo,font=("arial",13,"bold"),justify=CENTER)
        entry_RoomNo.grid(row=2,column=1,sticky=W)
        
        #Room type
        label__RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        label__RoomType.grid(row=3,column=0,sticky=W)
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.combo_RoomType,font=("arial",12,"bold"),width=20,state="readonly")
        combo_RoomType["value"]=("Single","Double","Laxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
#=============================button=========================================
        
        labelframeleft=Frame(labelframeleft,bd=2,relief=RIDGE)
        labelframeleft.place(x=0,y=320,width=412,height=40)
        btnAdd=Button(labelframeleft,text="ADD",command=self.add_room,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=4,column=0,padx=1)
        btnUpdate=Button(labelframeleft,text="UPDATE",command=self.update_room,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=4,column=1,padx=1)
        btnDelete=Button(labelframeleft,text="DELETE",command=self.delete_room,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=4,column=2,padx=1)
        btnReset=Button(labelframeleft,text="RESET",command=self.reset_fields,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=4,column=3,padx=1)
          
          
          
          
          
          
          
    def add_room(self):
        password = simpledialog.askstring("Password", "Enter password to proceed with adding:", show='*')
        if password != 'Antim':
            messagebox.showerror("Error", "Incorrect password!", parent=self.root)
        else:
            floor = self.entry_floor.get()
            room_no = self.entry_RoomNo.get()
            room_type = self.combo_RoomType.get()

            if floor == '' or room_no == '' or room_type == '':
                messagebox.showerror("Error", "All fields are required!", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='Antim@123',
                                                   database='Hotelmanagement')
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO Detail (Floor, roomno, roomType) VALUES (%s, %s, %s)",
                                   (floor, room_no, room_type))
                    conn.commit()
                    messagebox.showinfo("Success", "Room added successfully!", parent=self.root)
                    self.fetch_data()  # Refresh room table after adding
                except Exception as e:
                    messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)
                finally:
                    cursor.close()
                    conn.close()

    def update_room(self):
        selected_item = self.Detail_table.focus()
        values = self.Detail_table.item(selected_item, 'values')

        if not values:
            messagebox.showerror("Error", "Please select a room to update.", parent=self.root)
        else:
            password = simpledialog.askstring("Password", "Enter password to proceed with update:", show='*')
            if password != 'Antim':
                messagebox.showerror("Error", "Incorrect password!", parent=self.root)
            else:
                floor = self.entry_floor.get()
                room_no = self.entry_RoomNo.get()
                room_type = self.combo_RoomType.get()

                if floor == '' or room_no == '' or room_type == '':
                    messagebox.showerror("Error", "All fields are required!", parent=self.root)
                else:
                    try:
                        conn = mysql.connector.connect(host='localhost', user='root', password='Antim@123', database='Hotelmanagement')
                        cursor = conn.cursor()
                        cursor.execute("UPDATE Detail SET Floor=%s, roomno=%s, roomType=%s WHERE roomno=%s",
                                       (floor, room_no, room_type, values[1]))  # Assuming roomno is in the second position of values tuple
                        conn.commit()
                        messagebox.showinfo("Success", "Room updated successfully!", parent=self.root)
                        self.fetch_data()  # Refresh room table after updating
                    except Exception as e:
                        messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)
                    finally:
                        cursor.close()
                        conn.close()
    def delete_room(self):
          # Delete Room Function
          selected_item = self.Detail_table.focus()
          values = self.Detail_table.item(selected_item, 'values')

          if not values:
              messagebox.showerror("Error", "Please select a room to delete.", parent=self.root)
          else:
              confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this room?", parent=self.root)
              if confirmation:
                  try:
                      conn = mysql.connector.connect(host='localhost', user='root', password='Antim@123', database='Hotelmanagement')
                      cursor = conn.cursor()
                      cursor.execute("DELETE FROM Detail WHERE roomno=%s", (values[1],))  # Assuming roomno is in the second position of values tuple
                      conn.commit()
                      messagebox.showinfo("Success", "Room deleted successfully!", parent=self.root)
                      self.fetch_data()  # Refresh room table after deleting
                  except Exception as e:
                      messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)
                  finally:
                      cursor.close()
                      conn.close()

    def reset_fields(self):
        self.entry_floor.set('')
        self.entry_RoomNo.set('')
        self.combo_RoomType.set('')

    def get_cursor(self, event):
        # Get the selected item from the treeview
        item = self.Detail_table.focus()
        values = self.Detail_table.item(item, "values")
        if values:
            # Update entry fields and combo box with selected item's values
            self.entry_floor.set(values[0])
            self.entry_RoomNo.set(values[1])
            self.combo_RoomType.set(values[2])

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123",
                                           database="Hotelmanagement")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Floor, roomno, CONVERT(RoomType USING utf8) FROM Detail")
            rows = my_cursor.fetchall()
    
            # Clear existing data in the treeview
            for child in self.Detail_table.get_children():
                self.Detail_table.delete(child)
    
            # Insert fetched data into the treeview
            for row in rows:
                self.Detail_table.insert("", END, values=row)
    
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}", parent=self.root)




if __name__=="__main__":
     root=Tk()
     obj=Detail_win(root)
     root.mainloop()
