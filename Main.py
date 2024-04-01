from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from customer import cust__Win
from room import Roombooking
from Deatail import Detail_win




class HotelManagementSystem:
     def __init__(self,root) :
          self.root=root
          self.root.title("Hotel Management System")
          self.root.geometry('1530x800+0+0')
          self.root.resizable(False,False)

          #=========image 1 is hear================
             
          img1=Image.open("Image/mainhotel.jpg")
  
          img1.resize((1550,140),Image.Resampling.LANCZOS)
          self.photoimg1=ImageTk.PhotoImage(img1)

          labimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
          labimg.place(x=0,y=0,width=1550,height=140)

             
          img2=Image.open("Image/logo1.jpg")

          img2.resize((230,140),Image.Resampling.LANCZOS)
          self.photoimg2=ImageTk.PhotoImage(img2)

          labimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE )
          labimg.place(x=0,y=0,width=230,height=140)

          #================Title=====================

          lbl_title=Label(self.root ,text="HOTEL MANAGEMENT SYSTEM ", font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
          lbl_title.place(x=0,y=140,width=1550,height=50)

          #=============== Main frame===================

          main_frame=Frame(self.root,bd=4,relief=RIDGE)
          main_frame.place(x=0,y=190,width=1550,height=620)

          #=============menu========================

          lbl_menu=Label(main_frame ,text="MENU ", font=(" times new roman ",20 ,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
          lbl_menu.place(x=0,y=0,width=230)

          #===============btn frame==============

          btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
          btn_frame.place(x=0,y=35,width=228,height=430)

          cust_btn=Button(btn_frame,text="CUSTOMER",width=20, command=self.cust_details ,font=("times new roman",14,"bold"),justify="center",bg="black",fg="gold",bd=4,cursor="hand1")
          cust_btn.grid(row=0,column=0,pady=1)


          room_btn=Button(btn_frame,text="ROOM",width=20,font=("times new roman",14,"bold"),command=self.room_booking,justify="center",bg="black",fg="gold",bd=4,cursor="hand1")
          room_btn.grid(row=1,column=0,pady=1)

          detail_btn=Button(btn_frame,text="DETAIL",width=20,command=self.Detail_win,font=("times new roman",14,"bold"),justify="center",bg="black",fg="gold",bd=4,cursor="hand1")
          detail_btn.grid(row=2,column=0,pady=1)

          Exit_btn=Button(btn_frame,text="EXIT",width=20,font=("times new roman",14,"bold"),justify="center",bg="black",fg="gold",bd=4,cursor="hand1")
          Exit_btn.grid(row=4,column=0,pady=1)
          
          logout_btn=Button(btn_frame,text="LOGOUT",command=self.Logout,width=20,font=("times new roman",14,"bold"),justify="center",bg="black",fg="gold",bd=4,cursor="hand1")
          logout_btn.grid(row=3,column=0,pady=1)


     # =====================Right side image===================
     
          img3=Image.open("Image/main13.jpg")
  
          img3.resize((1310,590),Image.Resampling.LANCZOS)
          self.photoimg3=ImageTk.PhotoImage(img3)

          labimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
          labimg.place(x=230,y=0,width=1310,height=590)



     #=======================down image=================

          img4=Image.open("Image/food2.jpg")
          img4.resize((230,165),Image.Resampling.LANCZOS)
          self.photoimg4=ImageTk.PhotoImage(img4)

          labimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
          labimg.place(x=0,y=265,width=230,height=165) 

          img5=Image.open("Image/food1.jpg")
          img3.resize((1550,140),Image.Resampling.LANCZOS)
          self.photoimg5=ImageTk.PhotoImage(img5)

          labimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
          labimg.place(x=0,y=420,width=230,height=170)
          
          #======================function ====================
     
     def cust_details(self) :
          self.new_window=Toplevel(self.root)
          self.app=cust__Win( self.new_window)

     def room_booking(self) :
          self.new_window=Toplevel(self.root)
          self.app=Roombooking( self.new_window)
          
     def Detail_win(self) :
          self.new_window=Toplevel(self.root)
          self.app=Detail_win( self.new_window)
          

     def Logout(self):
          self.root.destroy()
          

if __name__=="__main__":
     root=Tk()
     obj=HotelManagementSystem(root)
     root.mainloop()