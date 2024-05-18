from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox


class display_student:
    def display_function(self):
        self.root=root
        self.root.title("Student Information")
        self.root.geometry("1600x900+0+0")

        # VARIABLES

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_sec_q=StringVar()
        self.var_sec_ans=StringVar()
        self.var_city=StringVar()
        self.var_pincode=StringVar()
        

        #Background image
        self.bg=ImageTk.PhotoImage(file=r"./images/BG1.jpg")
        bglbl=Label(self.root,image=self.bg)
        bglbl.place(x=0,y=0,relwidth=1,relheight=1)

        # bg image
        img=Image.open(r"./images/BG1.jpg")
        self.photoimg=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,width=1600,height=900)
        
        # MANAGE FRAME
        Manage_Frame=LabelFrame(bg_lbl,bd=10,relief=RIDGE,padx=4,bg="white")
        Manage_Frame.place(x=20,y=55,width=2000,height=2000)

        # LEFT FRAME
        Data_Left_Frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=10,text="Student Information",font=("times new roman",15,"bold"),fg="red",bg="white")
        Data_Left_Frame.place(x=100,y=15,width=8000,height=7000)
        
        # CURRENT COURSE INFO
        Current_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Current Course Information",font=("times new roman",15,"bold"),fg="green",bg="white")
        Current_Frame.place(x=5,y=5,width=7000,height=3000)

        #division 
        lbl_div=Label(Current_Frame,text="       Division : ",font=("arial",13,"bold"),bg="white",width=25)
        lbl_div.grid(row=1, column=0,padx=2,sticky=W)

        combo_div=ttk.Entry(Current_Frame,textvariable=self.var_div,state="readonly",font=("arial",10,"bold"),width=32)
        combo_div.grid(row=1,column=1,sticky=W,padx=2)

        #COURSE
        course=Label(Current_Frame,font=("arial",13,"bold"),text="Course : ",bg="white",width=25)
        course.grid(row=1,column=2,sticky=E,padx=20,pady=10)

        combo_course=ttk.Entry(Current_Frame,textvariable=self.var_course,state="readonly",font=("arial",10,"bold"),text="Select Course",width=32)
        combo_course.grid(row=1,column=3,sticky=W,padx=2,pady=10)  

        # YEAR

        Year=Label(Current_Frame,font=("arial",13,"bold"),text="            Year : ",bg="white",width=25)
        Year.grid(row=2,column=0,sticky=W,padx=2,pady=10)

        combo_year=ttk.Entry(Current_Frame,textvariable=self.var_year,state="readonly",font=("arial",12,),width=25)
        
        combo_year.grid(row=2,column=1,sticky=W,padx=2)

        #Semester

        Sem=Label(Current_Frame,font=("arial",13,"bold"),text="   Semester : ",bg="white",width=25)
        Sem.grid(row=2,column=2,sticky=W,padx=2,pady=10)

        combo_sem=ttk.Entry(Current_Frame,textvariable=self.var_sem,state="readonly",font=("arial",12),width=25)
        
        combo_sem.grid(row=2,column=3,sticky=W,padx=2,pady=10)

        # STUDENT CLASSS INFORMATION

        Class_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Student Class Information",font=("times new roman",15,"bold"),fg="green",bg="white")
        Class_Frame.place(x=5,y=150,width=6280,height=3500)

        # STUDENT ID NUMBER

        lbl_id=Label(Class_Frame,text="Student ID : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_id.grid(row=0, column=0,padx=2,sticky=W)

        id=ttk.Entry(Class_Frame,textvariable=self.var_id,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        id.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # STUDENT NAME

        lbl_name=Label(Class_Frame,text="Student Name : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_name.grid(row=0, column=2,padx=2,sticky=W)

        name=ttk.Entry(Class_Frame,textvariable=self.var_name,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        name.grid(row=0,column=3,padx=2,pady=10,sticky=W)


       

        # ROLL NUMBER

        lbl_roll=Label(Class_Frame,text="           Roll No. : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_roll.grid(row=1, column=2,padx=2,sticky=W)

        roll=ttk.Entry(Class_Frame,textvariable=self.var_roll,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        roll.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # GENDER

        lbl_gender=Label(Class_Frame,text="    Gender : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_gender.grid(row=1, column=0,padx=2,sticky=W)

        combo_gender=ttk.Entry(Class_Frame,textvariable=self.var_gender,state="readonly",font=("arial",10,"bold"),width=35)
        
        combo_gender.grid(row=1,column=1,sticky=W,padx=2)

        # DATE OF BIRTH
        
        lbl_dob=Label(Class_Frame,text="Date Of Birth : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_dob.grid(row=2, column=2,padx=2,sticky=W)

        dob=ttk.Entry(Class_Frame,textvariable=self.var_dob,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        dob.grid(row=2,column=3,padx=2,pady=10,sticky=W)        

        # EMAIL

        lbl_mail=Label(Class_Frame,text="        Email : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_mail.grid(row=2, column=0,padx=2,sticky=W)

        mail=ttk.Entry(Class_Frame,textvariable=self.var_email,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        mail.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # PHONE

        lbl_phone=Label(Class_Frame,text="   Phone No. : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_phone.grid(row=3, column=2,padx=2,sticky=W)

        phone=ttk.Entry(Class_Frame,textvariable=self.var_phone,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        phone.grid(row=3,column=3,padx=2,pady=10,sticky=W)

        #ADDRESS

        lbl_address=Label(Class_Frame,text="  Address : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_address.grid(row=4, column=0,padx=2,sticky=W)

        address=ttk.Entry(Class_Frame,textvariable=self.var_address,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        address.place(x=310,y=220,width=260,height=100)

        #TEACHER NAME

        lbl_teacher=Label(Class_Frame,text="      Teacher : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_teacher.grid(row=3, column=0,padx=2,sticky=W)

        teacher=ttk.Entry(Class_Frame,textvariable=self.var_teacher,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        teacher.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        #City
        lbl_city=Label(Class_Frame,text="     City : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_city.grid(row=4, column=2,padx=2,sticky=W)

        city=ttk.Entry(Class_Frame,textvariable=self.var_city,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        city.grid(row=4,column=3,padx=2,pady=20,sticky=W)

        #pincode
        lbl_pin=Label(Class_Frame,text="   Pincode : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_pin.grid(row=5, column=2,padx=2,sticky=W)

        pin=ttk.Entry(Class_Frame,textvariable=self.var_pincode,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        pin.grid(row=5,column=3,padx=2,pady=20,sticky=W)

         # BUTTONS FRAME
        Button_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,bg="white")
        Button_Frame.place(x=260,y=520,width=670,height=40)

        # SAVE BUTTON
        save=Button(Button_Frame,text="SAVE",font=("times new roman",10,"bold"),borderwidth=0,width=30,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        save.grid(row=0,column=0,padx=1,pady=0)

        # UPDATE BUTTON

        update=Button(Button_Frame,text="UPDATE",font=("times new roman",10,"bold"),borderwidth=0,width=30,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        update.grid(row=0,column=1,padx=1,pady=0)

        

        # RESET BUTTON

        reset=Button(Button_Frame,text="RESET",font=("times new roman",10,"bold"),borderwidth=0,width=30,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        reset.grid(row=0,column=2,padx=1,pady=0)

       

        
        







if __name__=="__main__":
    root=Tk()
    app=display_student()
    root.mainloop()
    self.display_function(self)