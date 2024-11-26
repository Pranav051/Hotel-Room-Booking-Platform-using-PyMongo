from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
from tkinter import Tk
import pymongo
from pymongo import MongoClient
import random
import re

client=MongoClient("mongodb+srv://pranav:pranav0510@cluster0.mgbscmu.mongodb.net/")
db=client.get_database('Hotel_Reservation')
col=db['Customer']
col1=db['Room']
# for i in col.find():
#     print(i)
class Cust_Win: 
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Reservation System") 
        self.root.geometry("1295x550+230+220")
        
        
        
        
        # ==========variables ======
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
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        
        lbl_title=Label(self.root, text="Add Customer Details", font=("times new roman" ,18,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=0, width=1295,height=50)
        
        #=====logo=======
        #img2=Image.open("C:\Users\Admin\Desktop\hotel_management_system\images\logohotel.png")
        #img2=img2.resize((100,40), Image.ANTIALIAS)
        #self.photoimg2-ImageTk.PhotoImage(img2)
        
        #lbling-Label(self.root,image=self.photoimg2, bd=4, relief=RIDGE)
        #lbling.place(x=5,y=2,width=100, height=40)
        
        #====labelFrame ==
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",font=("times new roman" ,18,"bold"), padx=2,)
        labelframeleft.place(x=5,y=50, width=425,height=490)
        
                
        #========labels and entrys============
        # lbl_cust_ref=Label(labelframeleft, text="Customer Ref", font=("arial",12,"bold"), padx=2,pady=6) 
        # lbl_cust_ref.grid(row=0, column=0,sticky=W)
        
        
        # enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref, width=22, font=("arial",13,"bold")) 
        # enty_ref.grid(row=0, column=1)
        

        # custRef
        lbl_cust_ref=Label (labelframeleft, text="Customer Ref", font=("arial",12,"bold"), padx=2, pady=6) 
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        enty_ref=ttk.Entry (labelframeleft,textvariable=self.var_ref, font=("arial", 13, "bold"),width=29)
        enty_ref.grid(row=0, column=1)
        #cust name
        cname=Label(labelframeleft, font=("arial",12, "bold"), text="Customer Name: ", padx=2, pady=6) 
        cname.grid(row=1, column=0, sticky=W)
        txtcname=ttk.Entry (labelframeleft,textvariable=self.var_cust_name, font=("arial", 13, "bold"),width=29)
        txtcname.grid(row=1, column=1)
        # mother name
        lblmname=Label(labelframeleft, font=("arial", 12, "bold"), text="Mother Name:", padx=2,pady=6) 
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname=ttk.Entry (labelframeleft,textvariable=self.var_mother, font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2, column=1)
        # gender combobox
        label_gender=Label(labelframeleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6) 
        label_gender.grid(row=3, column=0,sticky=W)
        
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state='readonly')
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)
        

        # postcode
        lb1PostCode=Label (labelframeleft, font=("arial", 12, "bold"), text="PostCode: ", padx=2,pady=6) 
        lb1PostCode.grid(row=4, column=0,sticky=W)
        txtPostCode=ttk.Entry (labelframeleft,textvariable=self.var_post, font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4, column=1)
        #mobilenumber
        lblMobile=Label(labelframeleft, font=("arial",12,"bold"), text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile=ttk.Entry (labelframeleft,textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=5,column=1)
        # email
        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail=ttk.Entry (labelframeleft,textvariable=self.var_email, font=("arial",13, "bold"),width=29)
        txtEmail.grid(row=6, column=1)
        # nationality
        lblNationality=Label(labelframeleft, font=("arial",12,"bold"), text="Nationality: ",padx=2,pady=6) 
        lblNationality.grid(row=7,column=0,sticky=W)
        
        
        combo_Nationality=ttk.Combobox (labelframeleft,textvariable=self.var_nationality, font=("arial",12,"bold"),width=27, state="readonly") 
        combo_Nationality["value"]=("Indian", "American", "British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)
        
        
        
        # idproof type combobox
        lblIdProof=Label (labelframeleft, font=("arial", 12, "bold"), text="Id Proof Type: ", padx=2,pady=6) 
        lblIdProof.grid(row=8, column=0, sticky=W)
        
        
        combo_id=ttk.Combobox (labelframeleft,textvariable=self.var_id_proof, font=("arial",12,"bold"),width=27, state="readonly") 
        combo_id ["value"]=("Adhar Card", "DrivingLicense", "Passport")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)
        
        # id number
        lblIdNumber=Label (labelframeleft, font=("arial", 12, "bold"), text="Id Number:", padx=2,pady=6) 
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number, font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9, column=1)
        # address
        lblAddress=Label(labelframeleft, font=("arial", 12, "bold"), text="Address: ", padx=2,pady=6) 
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress=ttk. Entry (labelframeleft,textvariable=self.var_address, font=("arial",13, "bold"),width=29)
        txtAddress.grid(row=10, column=1)
        
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
        
        
        #======table frame Searching====
        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search ", font=("arial", 12, "bold"),padx=2) 
        Table_Frame.place (x=435,y=50, width=860,height=490)
        
                
        lb1SearchBy=Label (Table_Frame, font=("arial", 12, "bold"), text="Search By: ", bg="red",fg="white") 
        lb1SearchBy.grid(row=0, column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_Serach=ttk.Combobox (Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold"),
                                   width=24, state="readonly")
        combo_Serach ["value"]=("Mobile","Ref")
        combo_Serach.current(0)
        combo_Serach.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("arial",13, "bold"),width=24)
        txtSearch.grid(row=0, column=2,padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search, font=("arial",11,"bold"), bg="black", fg="gold",width=10) 
        btnSearch.grid(row=0, column=3,padx=1)
        
        btnShowAll=Button(Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10) 
        btnShowAll.grid(row=0, column=4, padx=1)
                
        #========Show data Table======
        details_table=Frame (Table_Frame, bd=2,relief=RIDGE) 
        details_table.place(x=0,y=50, width=860,height=350)
        scroll_x=ttk.Scrollbar (details_table, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar (details_table, orient=VERTICAL)
        
        
        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name", "mother", "gender", "post", "mobile", 
                                                               "email","nationality","idproof", "idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self. Cust_Details_Table.xview) 
        scroll_y.config(command=self. Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality") 
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")
        
        self.Cust_Details_Table["show"]="headings" 
        
        
        self.Cust_Details_Table.column ("ref", width=100)
        self.Cust_Details_Table.column ("name", width=100)
        self.Cust_Details_Table.column ("mother", width=100)
        self.Cust_Details_Table.column ("gender", width=100)
        self.Cust_Details_Table.column ("post", width=100) 
        self.Cust_Details_Table.column ("mobile", width=100) 
        self.Cust_Details_Table.column ("email", width=100)
        self.Cust_Details_Table.column ("nationality", width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column ("idnumber", width=100)
        self.Cust_Details_Table.column ("address", width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                mydict={ "ref":self.var_ref.get(),"name":self.var_cust_name.get(),"mother":self.var_mother.get(),
                        "gender":self.var_gender.get(),"post":self.var_post.get(),"mobile":self.var_mobile.get(),
                        "email":self.var_email.get(),"nationality":self.var_nationality.get(),
                        "idproof":self.var_id_proof.get(),"idnumber":self.var_id_number.get(),
                        "address":self.var_address.get(),'room':[]}
                x=col.insert_one(mydict)
                self.fetch_data()
                
                messagebox.showinfo("Success", "customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Something Went Wrong:{str(es)}',parent=self.root)
                
    # def fetch_data(self):
    #     f=col.find()
    #     for data in f:
    #         print(data)
    #         if len(data)!=0:
    #             self.Cust_Details_Table.delete(*self. Cust_Details_Table.get_children())
    #         for i in data:
    #             self.Cust_Details_Table.insert("", END, values=i)
    
    def fetch_data (self):
        for child in self.Cust_Details_Table.get_children():
            self.Cust_Details_Table.delete(child)
        cursor = col.find()
        for data in cursor:
            self.Cust_Details_Table.insert("", END, values=(
                data["ref"], data["name"], data["mother"], data["gender"],
                data["post"], data["mobile"], data["email"], data["nationality"],
                data["idproof"], data["idnumber"], data["address"]
            ))
        
    
    def get_cursor (self, event=""):
        cursor_row=self. Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content ["values"]
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row [7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row [9]),
        self.var_address.set(row[10])
        
    
    def update(self):
        if self.var_mobile.get() =="":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            filter={'ref':self.var_ref.get()}
            newvalues={'$set':{"name":self.var_cust_name.get(),"mother":self.var_mother.get(),
                        "gender":self.var_gender.get(),"post":self.var_post.get(),"mobile":self.var_mobile.get(),
                        "email":self.var_email.get(),"nationality":self.var_nationality.get(),
                        "idproof":self.var_id_proof.get(),"idnumber":self.var_id_number.get(),
                        "address":self.var_address.get()}}
            x=col.update_one(filter,newvalues)
            self.fetch_data()
            messagebox.showinfo("Update", "Customer details has been updated successfully",parent=self.root)
            
            
    
    def Delete(self):
        Delete=messagebox.askyesno ("Hotel Management System", "Do you want delete this customer", parent=self.root)
        if Delete>0:
            value={'ref':self.var_ref.get()}
            x=col.delete_one(value)
        else:
            if not Delete:
                return
        self.fetch_data()
    
    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999) 
        self.var_ref.set(str(x))
            
    def search(self):
        search_string=self.txt_search.get()
        cursor=col.find({
        "$or": [
            {"mobile": {"$regex": search_string, "$options": "i"}},
            {"ref": {"$regex": search_string, "$options": "i"}}
        ]})
        for child in self.Cust_Details_Table.get_children():
            self.Cust_Details_Table.delete(child)
        for data in cursor:
            self.Cust_Details_Table.insert("", END, values=(
                data["ref"], data["name"], data["mother"], data["gender"],
                data["post"], data["mobile"], data["email"], data["nationality"],
                data["idproof"], data["idnumber"], data["address"]
            ))
        
                
if __name__ =="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
    