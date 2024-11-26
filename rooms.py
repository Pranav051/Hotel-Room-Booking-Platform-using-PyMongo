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
roomno=col2.find().distinct('RoomNo')



class Room_Booking: 
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Reservation System") 
        self.root.geometry("1295x550+230+220")
        
        
        #=====variables ====
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar() 
        
        lbl_title=Label(self.root, text="Add Room Details", font=("times new roman" ,18,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=0, width=1295,height=50)
        
        #=====logo=======
        #img2=Image.open("C:\Users\Admin\Desktop\hotel_management_system\images\logohotel.png")
        #img2=img2.resize((100,40), Image.ANTIALIAS)
        #self.photoimg2-ImageTk.PhotoImage(img2)
        
        #lbling-Label(self.root,image=self.photoimg2, bd=4, relief=RIDGE)
        #lbling.place(x=5,y=2,width=100, height=40)
        
        #====labelFrame ==
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details",font=("times new roman" ,18,"bold"), padx=2,)
        labelframeleft.place(x=5,y=50, width=425,height=490)
        
        
        #========labels and entrys============ 
        # Customer Contact
        lbl_cust_contact=Label (labelframeleft, text="Customer Contact", font=("arial",12,"bold"), padx=2, pady=6) 
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        enty_contact=ttk.Entry (labelframeleft,textvariable=self.var_contact, font=("arial", 13, "bold"),width=20)
        enty_contact.grid(row=0, column=1,sticky=W)
        
        
        # Fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact, text="Fetch Data", font=("arial", 8,"bold"), bg="black",fg="gold",width=8) 
        btnFetchData.place(x=347,y=4)
        
        
        #Check_in Date
        check_in_date=Label(labelframeleft, font=("arial", 12, "bold"), text="Check_in Date:", padx=2, pady=6) 
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin, font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1, column=1)
        
        # Check_out Date
        lbl_Check_out=Label(labelframeleft, font=("arial",12,"bold"), text="Check_Out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)
        txt_Check_out=ttk. Entry (labelframeleft,textvariable=self.var_checkout, font=("arial", 13, "bold"),width=29)
        txt_Check_out.grid(row=2, column=1)
        
        # Room Type
        label_RoomType=Label(labelframeleft, font=("arial",12,"bold"), text="Room Type:", padx=2, pady=6) 
        label_RoomType.grid(row=3, column=0,sticky=W)
        combo_RoomType=ttk.Combobox (labelframeleft,textvariable=self.var_roomtype, font=("arial",12,"bold"),width=27, state="readonly") 
        roomtypes=col2.find().distinct('RoomType')
        combo_RoomType["value"]=roomtypes
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)
        
        # Available Room
        lblRoomAvailable=Label (labelframeleft, font=("arial", 12, "bold"), text="Available Room: ", padx=2,pady=6) 
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        comboRoomAvailable=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable, font=("arial", 12, "bold"),width=27,state='readonly')
        roomno=col2.find().distinct('RoomNo')
        comboRoomAvailable["value"]=roomno
        comboRoomAvailable.current(0)
        comboRoomAvailable.grid(row=4, column=1)
        
        # Meal
        lblMeal=Label(labelframeleft, font=("arial", 12, "bold"), text="Meal: ",padx=2, pady=6) 
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal=ttk.Entry (labelframeleft,textvariable=self.var_meal, font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5, column=1)
        
        # No Of Days
        lblNoOfDays=Label (labelframeleft, font=("arial",12,"bold"), text="No Of Days: ", padx=2,pady=6) 
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays, font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6, column=1)
                   
        # Paid Tax
        lblNoOfDays=Label(labelframeleft, font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6) 
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax, font=("arial", 13, "bold"),width=29)
        txtNoOfDays.grid(row=7, column=1)
        
        # Sub Total
        lblNoOfDays=Label(labelframeleft, font=("arial",12,"bold"), text="Sub Total:",padx=2,pady=6) 
        lblNoOfDays.grid(row=8, column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, font=("arial",13, "bold"),width=29)
        txtNoOfDays.grid(row=8, column=1)
        
        # Total Cost
        lblIdNumber=Label(labelframeleft, font=("arial",12,"bold"),text="Total Cost:",padx=2, pady=6) 
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total, font=("arial",13, "bold"),width=29)
        txtIdNumber.grid(row=9, column=1)
        
        
        #======Bill Button====
        btnBill=Button (labelframeleft, text="Bill",command=self.total, font=("arial", 11, "bold"), bg="black", fg="gold", width=10) 
        btnBill.grid(row=10, column=0, padx=1, sticky=W)
        
        #button        
        btn_frame=Frame (labelframeleft, bd=2, relief=RIDGE) 
        btn_frame.place (x=0,y=400, width=412,height=48)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0, column=0, padx=1)
        
        btnUpdate=Button (btn_frame, text="Update",command=self.update, font=("arial",11,"bold"),bg="black", fg="gold",width=10) 
        btnUpdate.grid(row=0, column=1, padx=1)
        
        btnDelete=Button (btn_frame, text="Delete",command=self.Delete, font=("arial",11, "bold"),bg="black", fg="gold", width=10) 
        btnDelete.grid(row=0, column=2, padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset, font=("arial",11,"bold"),bg="black",fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        
                
        # #========Rightside image==:
        # img3=Image.open("C:\Users\Admin\Desktop\hotel_management_system\images\bed.jpg") 
        # img3=img3.resize((520,300), Image. ANTIALIAS)
        # self.photoimg3=ImageTk. PhotoImage(img3)
        # lblimg=Label(self.root, image=self.photoimg3, bd=0,relief=RIDGE)
        # lblimg.place(x=760,y=55,width=520,height=200)
        
        #======table frame Searching====
        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search ", font=("arial", 12, "bold"),padx=2) 
        Table_Frame.place (x=435,y=280, width=860,height=260)
        
                
        lb1SearchBy=Label (Table_Frame, font=("arial", 12, "bold"), text="Search By: ", bg="red",fg="white") 
        lb1SearchBy.grid(row=0, column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_Serach=ttk.Combobox (Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Serach ["value"]=("Contact","Room")
        combo_Serach.current(0)
        combo_Serach.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("arial",13, "bold"),width=24)
        txtSearch.grid(row=0, column=2,padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search, font=("arial",11,"bold"), bg="black", fg="gold",width=10) 
        btnSearch.grid(row=0, column=3,padx=1)
        
        btnShowAll=Button(Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10) 
        btnShowAll.grid(row=0, column=4, padx=1)
        
        
        # ============Show data Table======
        details_table=Frame (Table_Frame, bd=2, relief=RIDGE)
        details_table.place (x=0,y=50, width=860, height=180)
        scroll_x=ttk.Scrollbar (details_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (details_table, orient=VERTICAL)
        self.room_table=ttk. Treeview (details_table, column=("contact","checkin", "checkout", "roomtype", "roomavailable","meal","NoOfDays" )
                                       ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack (side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        
        scroll_x.config(command=self.room_table.xview) 
        scroll_y.config(command=self.room_table.yview)
        self.room_table.heading("contact", text="Contact") 
        self.room_table.heading("checkin", text="Check-in ") 
        self.room_table.heading("checkout", text="Check-out") 
        self.room_table.heading ("roomtype", text="Room Type") 
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal") 
        self.room_table.heading("NoOfDays", text="NoOfDays")
        
        self.room_table["show"]="headings"

        self.room_table.column ("contact",width=100)
        self.room_table.column ("checkin", width=100)
        self.room_table.column ("checkout", width=100) 
        self.room_table.column ("roomtype", width=100) 
        self.room_table.column ("roomavailable", width=100) 
        self.room_table.column ("meal", width=100) 
        self.room_table.column ("NoOfDays", width=100) 
        self.room_table.pack (fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                mydict={ "contact":self.var_contact.get(),"checkin":self.var_checkin.get(),
                        "checkout":self.var_checkout.get(),"roomtype":self.var_roomtype.get(),
                        "roomavailable":self.var_roomavailable.get(),"meal":self.var_meal.get(),
                        "noofdays":self.var_noofdays.get()
                    }
                contact=self.var_contact.get()
                x=col.find_one_and_update({'mobile':contact},{'$push':{'room':{"contact":self.var_contact.get(),"checkin":self.var_checkin.get(),
                        "checkout":self.var_checkout.get(),"roomtype":self.var_roomtype.get(),
                        "roomavailable":self.var_roomavailable.get(),"meal":self.var_meal.get(),
                        "noofdays":self.var_noofdays.get()}}},return_document=ReturnDocument.AFTER)
                
                x1=col1.insert_one(mydict)
                self.fetch_data()
                
                messagebox.showinfo("Success", "Room Booked!",parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Something Went Wrong:{str(es)}',parent=self.root)
                
    def fetch_data(self):
        for child in self.room_table.get_children():
            self.room_table.delete(child)
        cursor = col1.find()
        for data in cursor:
            self.room_table.insert("", END, values=(
                data["contact"], data["checkin"], data["checkout"], data["roomtype"],
                data["roomavailable"], data["meal"], data["noofdays"]
            ))
    
    def get_cursor(self,event=""): 
        cursor_row=self.room_table.focus() 
        content=self.room_table.item(cursor_row)
        row=content ["values"]
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])  
        
    def update(self):
        if self.var_contact.get() =="":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            filter={'contact':self.var_contact.get()}
            newvalues={'$set':{"checkin":self.var_checkin.get(),
                        "checkout":self.var_checkout.get(),"roomtype":self.var_roomtype.get(),
                        "roomavailable":self.var_roomavailable.get(),"meal":self.var_meal.get(),
                        "noofdays":self.var_noofdays.get()}}
            x=col1.update_one(filter,newvalues)
            self.fetch_data()
            
            messagebox.showinfo("Update", "Room details has been updated successfully",parent=self.root)
            contact=self.var_contact.get()
            print(contact)
            # x1=col.find_one_and_update({'mobile':contact},{'$set':{'room':{"contact":self.var_contact.get(),
            #                                                                 "checkin":self.var_checkin.get(),
            #             "checkout":self.var_checkout.get(),"roomtype":self.var_roomtype.get(),
            #             "roomavailable":self.var_roomavailable.get(),"meal":self.var_meal.get(),
            #             "noofdays":self.var_noofdays.get()}}},return_document=ReturnDocument.AFTER)
            value={'contact':self.var_contact.get()}
            print(value['contact'])
            
            y=col.update_one({'mobile':value['contact']},{'$set':{'room':[]}})
            y=col.find_one_and_update({'mobile':contact},{'$push':{'room':{"contact":self.var_contact.get(),"checkin":self.var_checkin.get(),
                        "checkout":self.var_checkout.get(),"roomtype":self.var_roomtype.get(),
                        "roomavailable":self.var_roomavailable.get(),"meal":self.var_meal.get(),
                        "noofdays":self.var_noofdays.get()}}},return_document=ReturnDocument.AFTER)
            
            # x1=col.update_one({'mobile':contact},{'$pull':{'room':{"contact":value['contact'],
            #             "checkin":self.var_checkin.get(),"checkout":self.var_checkout.get(),
            #             "roomtype":self.var_roomtype.get(),"roomavailable":self.var_roomavailable.get(),
            #             "meal":self.var_meal.get(),"noofdays":self.var_noofdays.get()}}})
            # x1=col.update_one({'mobile':contact},{'$push':{'room':{"contact":value['contact'],
            #             "checkin":self.var_checkin.get(),"checkout":self.var_checkout.get(),
            #             "roomtype":self.var_roomtype.get(),"roomavailable":self.var_roomavailable.get(),
            #             "meal":self.var_meal.get(),"noofdays":self.var_noofdays.get()}}})
            
            
            
            
    def Delete(self):
        Delete=messagebox.askyesno ("Hotel Management System", "Do you want delete this customer", parent=self.root)
        if Delete>0:
            value={'contact':self.var_contact.get()}
            x=col1.delete_one(value)
            # y=col.update_one({'mobile':value},{'$set':{'room':{}}},multi=TRUE)
            y=col.update_one({'mobile':value['contact']},{'$set':{'room':[]}})
        else:
            if not Delete:
                return
        self.fetch_data()
    
    
    def reset(self):
        self.var_contact.set('')
        self.var_checkin.set('')
        self.var_checkout.set('')
        self.var_roomtype.set('')
        self.var_roomavailable.set('')
        self.var_meal.set('') 
        self.var_noofdays.set('')
        self.var_paidtax.set('')
        self.var_actualtotal.set('')
        self.var_total=StringVar('') 
        
    def search(self):
        search_string=self.txt_search.get()
        cursor=col1.find({
        "$or": [
            {"contact": {"$regex": search_string, "$options": "i"}},
            {"roomavailable": {"$regex": search_string, "$options": "i"}}
        ]})
        for child in self.room_table.get_children():
            self.room_table.delete(child)
        for data in cursor:
            self.room_table.insert("", END, values=(
                data["contact"], data["checkin"], data["checkout"], data["roomtype"],
                data["roomavailable"], data["meal"], data["noofdays"]
            ))
        
    
    def Fetch_contact(self):
        if self.var_contact.get() =="":
            messagebox.showerror("Error", "Please enter Contact Number",parent=self.root)
        else:
            search_string=self.var_contact.get()
            cursor=col.find({'mobile':search_string})
            if cursor==None:
                messagebox.showerror("Error","This Number was not Found",parent=self.root)
            else:
                showDataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2) 
                showDataframe.place (x=455,y=55,width=300,height=180)
                
                cursor1=col.find({'mobile':search_string},{'name':1,'_id':0})
                lblName=Label(showDataframe, text="Name:", font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                for name in cursor1:
                    lb1=Label(showDataframe, text=name['name'], font=("arial",12,"bold")) 
                    lb1.place(x=90,y=0)
                    
                cursor2=col.find({'mobile':search_string},{'gender':1,'_id':0})
                lblGender=Label(showDataframe, text="Gender:", font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                for name in cursor2:
                    lb2=Label(showDataframe, text=name['gender'], font=("arial",12,"bold")) 
                    lb2.place(x=90,y=30)
                    
                cursor3=col.find({'mobile':search_string},{'email':1,'_id':0})
                lblEmail=Label(showDataframe, text="Email:", font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)
                for name in cursor3:
                    lb3=Label(showDataframe, text=name['email'], font=("arial",12,"bold")) 
                    lb3.place(x=90,y=60)
                    
                cursor4=col.find({'mobile':search_string},{'nationality':1,'_id':0})
                lblNationality=Label(showDataframe, text="Nationality:", font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)
                for name in cursor4:
                    lb4=Label(showDataframe, text=name['nationality'], font=("arial",12,"bold")) 
                    lb4.place(x=90,y=90)
                
                cursor5=col.find({'mobile':search_string},{'address':1,'_id':0})
                lblAddress=Label(showDataframe, text="Address:", font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)
                for name in cursor5:
                    lb5=Label(showDataframe, text=name['address'], font=("arial",12,"bold")) 
                    lb5.place(x=90,y=120)
                    
    def roomtypes(self):
        global i
        for j in col2.find().distinct('RoomType'):
            i=i+j
        return i
            
                    
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate, "%d/%m/%Y")
        outDate=datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs (outDate-inDate).days)
        
        
        if (self.var_meal.get() == "Breakfast" and self.var_roomtype.get()=="luxury"): 
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs. "+str("%.2f" % ( (q5) *0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f" % (q5+ ((q5)*0.09))) 
            self.var_paidtax.set(Tax) 
            self.var_actualtotal.set(ST) 
            self.var_total.set(TT)
            
        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get()=="Single"): 
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs. "+str("%.2f" % ( (q5) *0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f" % (q5+ ((q5)*0.09))) 
            self.var_paidtax.set(Tax) 
            self.var_actualtotal.set(ST) 
            self.var_total.set(TT)
            
        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get()=="Single"): 
            q1=float(400)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs. "+str("%.2f" % ( (q5) *0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f" % (q5+ ((q5)*0.09))) 
            self.var_paidtax.set(Tax) 
            self.var_actualtotal.set(ST) 
            self.var_total.set(TT)
            

if __name__ =="__main__":
    root=Tk()
    obj=Room_Booking(root)
    root.mainloop()