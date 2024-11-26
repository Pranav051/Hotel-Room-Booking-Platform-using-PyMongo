from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
from tkinter import Tk
import pymongo
from pymongo import MongoClient
import random
import re
from time import strftime
from datetime import datetime
from pymongo.collection import ReturnDocument

client=MongoClient("mongodb+srv://pranav:pranav0510@cluster0.mgbscmu.mongodb.net/")
db=client.get_database('Hotel_Reservation')
col=db['Customer']
col1=db['Room']
col2=db['Room_Details']

class Room_Details: 
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Reservation System") 
        self.root.geometry("1295x550+230+220")
        
        #=====variables ====
        self.var_floor=StringVar()
        self.var_Room_No=StringVar()
        self.var_Room_Type=StringVar()
        
        
        lbl_title=Label(self.root, text="Room Details", font=("times new roman" ,18,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=0, width=1295,height=50)
        
        #=====logo=======
        #img2=Image.open("C:\Users\Admin\Desktop\hotel_management_system\images\logohotel.png")
        #img2=img2.resize((100,40), Image.ANTIALIAS)
        #self.photoimg2-ImageTk.PhotoImage(img2)
        
        #lbling-Label(self.root,image=self.photoimg2, bd=4, relief=RIDGE)
        #lbling.place(x=5,y=2,width=100, height=40)
        
        #====labelFrame ==
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details",font=("times new roman" ,18,"bold"), padx=2,)
        labelframeleft.place(x=5,y=50, width=540,height=350)
        
        # Floor
        lbl_floor=Label (labelframeleft, text="Floor", font=("arial",12,"bold"), padx=2, pady=6) 
        lbl_floor.grid(row=0, column=0, sticky=W,padx=20)
        enty_floor=ttk.Entry (labelframeleft,textvariable=self.var_floor, font=("arial", 13, "bold"),width=20)
        enty_floor.grid(row=0, column=1,sticky=W)
        
        
        # Room No
        lb1_RoomNo=Label (labelframeleft, text="Room No", font=("arial",12,"bold"), padx=2,pady=6) 
        lb1_RoomNo.grid(row=1, column=0,sticky=W, padx=20)
        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_Room_No, font=("arial",13,"bold"),width=20)
        enty_RoomNo.grid(row=1, column=1, sticky=W)
        
        # Room Type
        lb1_RoomType=Label(labelframeleft, text="Room Type",font=("arial",12,"bold"), padx=2,pady=6)
        lb1_RoomType.grid(row=2, column=0, sticky=W, padx=20)
        enty_RoomType=ttk. Entry (labelframeleft,textvariable=self.var_Room_Type, font=("arial", 13, "bold"), width=20)
        enty_RoomType.grid(row=2, column=1, sticky=W)
        
        #button        
        btn_frame=Frame (labelframeleft, bd=2, relief=RIDGE) 
        btn_frame.place (x=0,y=200, width=410,height=35)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0, column=0, padx=1)
        
        btnUpdate=Button (btn_frame, text="Update",command=self.update, font=("arial",11,"bold"),bg="black", fg="gold",width=10) 
        btnUpdate.grid(row=0, column=1, padx=1)
        
        btnDelete=Button (btn_frame, text="Delete",command=self.Delete, font=("arial",11, "bold"),bg="black", fg="gold", width=10) 
        btnDelete.grid(row=0, column=2, padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset, font=("arial",11,"bold"),bg="black",fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        
        #======table frame Searching====
        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details ", font=("arial", 12, "bold"),padx=2) 
        Table_Frame.place (x=600,y=55, width=600,height=350)
        
        scroll_x=ttk.Scrollbar (Table_Frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (Table_Frame, orient=VERTICAL)
        self.room_table=ttk. Treeview (Table_Frame,column=("floor", "roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.room_table.xview) 
        scroll_y.config(command=self.room_table.yview)
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No ") 
        self.room_table.heading("roomType", text="Room Type")
        self.room_table["show"]="headings"
        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomType",width=100)
        self.room_table.pack (fill=BOTH, expand=1)
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_data(self):
        if self.var_floor.get()=="" or self.var_Room_Type.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                mydict={ "Floor":self.var_floor.get(),"RoomNo":self.var_Room_No.get()
                        ,"RoomType":self.var_Room_Type.get(),
                        }
                x=col2.insert_one(mydict)
                self.fetch_data()
                
                messagebox.showinfo("Success", "Room has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Something Went Wrong:{str(es)}',parent=self.root)
                
    def update(self):
        if self.var_floor.get() =="":
            messagebox.showerror("Error", "Please enter floor", parent=self.root)
        else:
            filter={'RoomNo':self.var_Room_No.get()}
            newvalues={'$set':{"Floor":self.var_floor.get(),
                               "RoomType":self.var_Room_Type.get(),
                        }}
            x=col2.update_one(filter,newvalues)
            self.fetch_data()
            messagebox.showinfo("Update", "Room details has been updated successfully",parent=self.root)
            
            
    
    def Delete(self):
        Delete=messagebox.askyesno ("Hotel Management System", "Do you want delete this room", parent=self.root)
        if Delete>0:
            value={'RoomNo':self.var_Room_No.get()}
            x=col2.delete_one(value)
        else:
            if not Delete:
                return
        self.fetch_data()
    
    def reset(self):
        self.var_floor.set(""),
        self.var_Room_No.set(""),
        
        self.var_Room_Type.set(""),
        
    def fetch_data(self):
        for child in self.room_table.get_children():
            self.room_table.delete(child)
        cursor = col2.find()
        for data in cursor:
            self.room_table.insert("", END, values=(
                data["Floor"], data["RoomNo"], data["RoomType"]
            ))
            
            
    
    # getcursor
    def get_cursor(self, event=""): 
        cursor_row=self.room_table.focus() 
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_floor.set(row[0]),
        self.var_Room_No.set(row[1]),
        self.var_Room_Type.set(row[2])

if __name__ =="__main__":
    root=Tk()
    obj=Room_Details(root)
    root.mainloop()