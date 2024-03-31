from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk #pip install pillow
from login import Add_User 
from Main import HotelManagementSystem

background = "#06283D"


# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Antim@123",
    database="Hotelmanagement"
)
cursor = db.cursor()

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry('1550x800+0+0')
        self.root.config(bg=background)
        self.root.resizable(False, False)

        self.username_entry = StringVar()
        self.password_entry = StringVar()

        # background Image
        img2 = Image.open("Image/login4.jpg")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        labimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        labimg.place(x=5, y=2)

        User_id = Label(self.root, text="Login", font=("arial", 12, "bold"), padx=2, pady=6)
        User_id.place(x=730, y=265, width=100)

        # USER ID
        self.username_entry = Entry(self.root, width=29, font=("arial", 13, "bold"))
        self.username_entry.place(x=607, y=300, height=55, width=345)
        self.username_entry.insert(0, "Username")
        self.username_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.username_entry))
        self.username_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.username_entry))

        # Password
        self.password_entry = Entry(self.root, width=29, show="*", font=("arial", 13, "bold"))
        self.password_entry.place(x=607, y=390, height=55, width=345)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.password_entry))
        self.password_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.password_entry))

        # Login button
        btnAdd = Button(self.root, text="Login", font=("arial", 12, "bold"), command=self.validate_login, bg="skyblue",cursor="hand2",
                        fg="white")
        btnAdd.place(x=607, y=468, width=345, height=55)
        # Bind the <Return> key to the login button
        self.root.bind("<Return>", lambda event: self.validate_login())

        # ADD USER
        Add_User_id = Label(self.root, text="Not registered?", font=("arial", 12, "bold"), background="white",
                            fg="gray", padx=2, pady=6)
        Add_User_id.place(x=630, y=535)

        Add_btnAdd = Button(self.root, text="New User", command=self.Add_user, fg="skyblue",cursor="hand2",
                            font=("arial", 12, "bold"))
        Add_btnAdd.place(x=755, y=535)
        Add_btnAdd = Button(self.root, text="Forget password", command=self.Add_user, fg="Black",cursor="hand2",
                            font=("arial", 12, "bold"))
        Add_btnAdd.place(x=845, y=535)
        
        #Back btn
        # exit_img=PhotoImage(file="Image\exit.png")
        # lbl_img=Label(image=exit_img)
        # lbl_img.pack(pady=10 )
        Add_btnAdd = Button(self.root, text="Exit", command=self.Logout,cursor="hand2", fg="white",background="black",width=8,
                            font=("arial", 12, "bold"))
        Add_btnAdd.place(x=920, y=250)


        # FUNCTION

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password are valid
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            self.new_window = Toplevel(self.root)
            self.app = HotelManagementSystem(self.new_window)
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def Add_user(self):
        self.new_window = Toplevel(self.root)
        self.app = Add_User(self.new_window)

    def clear_placeholder(self, entry_widget):
        current_text = entry_widget.get()
        if current_text == "Username" or current_text == "Password":
            entry_widget.delete(0, END)

    def restore_placeholder(self, entry_widget):
        current_text = entry_widget.get()
        if current_text.strip() == "":
            if entry_widget == self.username_entry:
                entry_widget.insert(0, "Username")
            elif entry_widget == self.password_entry:
                entry_widget.insert(0, "Password")
    
    def Logout(self):
          self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()
