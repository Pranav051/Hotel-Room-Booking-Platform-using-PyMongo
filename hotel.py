
from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from customer import Cust_Win
from rooms import Room_Booking
from details import Room_Details
import PIL
class HotelManagementSystem: 
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Reservation System") 
        self.root.geometry("1550x800+0+0")
        img1=Image.open("E:\\pranav\\Project\\Hotel_booking_platform\\img1.png")
        img1=img1.resize((1550,140), PIL.Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4, relief=RIDGE) 
        lblimg.place(x=0,y=0,width=1550,height=140)
    
        #=====logo=======
        img2=Image.open("E:\\pranav\\Project\\Hotel_booking_platform\\logo.png")
        img2=img2.resize((238,148), PIL.Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbling=Label(self.root,image=self.photoimg2, bd=4, relief=RIDGE)
        lbling.place(x=0,y=0,width=230, height=140)
        
        
        #======title======
        lbl_title=Label(self.root, text="Hotel Reservation System", font=("times new roman" ,40,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=140, width=1550,height=50)
        #=======main Frame===
        main_frame=Frame(self.root, bd=4,background='', relief=RIDGE)
        main_frame.place (x=0,y=190, width=1550,height=620)
        #menu
        lbl_title=Label(main_frame, text="Menu", font=("times new roman" ,20,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=140, width=230)
        
        
        #=btn Frame:
        btn_frame=Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=150)
        
        cust_btn=Button(btn_frame, text="Customer",command=self.cust_details,width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor='hand1')
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame, text="Room",command=self.room_booking,width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor='hand1')
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame, text="Details",command=self.room_details,width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor='hand1')
        details_btn.grid(row=2,column=0,pady=1)
        
        # logout_btn=Button(btn_frame, text="Logout",width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor='hand1')
        # logout_btn.grid(row=4,column=0,pady=1)
        
        
        #==right side image==
        img3=Image.open("E:\\pranav\\Project\\Hotel_booking_platform\\mainimg.png")
        img3=img3.resize((1310,590), PIL.Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label (main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225,y=0, width=1310,height=590)
        
    
    def cust_details(self):
        self.new_window=Toplevel (self.root)
        self.app=Cust_Win(self.new_window)
        
    def room_booking(self):
        self.new_window=Toplevel (self.root)
        self.app=Room_Booking(self.new_window)
        
    def room_details(self):
        self.new_window=Toplevel (self.root)
        self.app=Room_Details(self.new_window)
        
if __name__ =="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
    