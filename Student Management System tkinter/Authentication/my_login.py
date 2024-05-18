from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
import mysql.connector

def main():
    win= Tk()
    app=login_window(win)
    win=mainloop()


class login_window:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1600x800+0+0")
    
        self.bg=ImageTk.PhotoImage(file=r"./images/College_pic.jpg")
        self.var_name=StringVar()
        self.var_dob=StringVar()

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"./images/MCOE_SYMBOL.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,borderwidth=0)
        lblimg1.config(bg="black")
        lblimg1.place(x=730,y=175,width=100,height=100)

        getstr=Label(frame,text="PESMCOE",font=("times new roman",20,"bold"),fg="white",bg="black")
        getstr.place(x=100,y=105)

        #label

        username=Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtusr=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtusr.place(x=40,y=180,width=270)

        password=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        ##icon images

        img2=Image.open(r"./images/login-icon.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,borderwidth=0)
        lblimg1.config(bg="black")
        lblimg1.place(x=650,y=323,width=25,height=25)


        img3=Image.open(r"./images/pass-image.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimg3,borderwidth=0)
        lblimg1.config(bg="black")
        lblimg1.place(x=650,y=392,width=25,height=25)


        #Login Button
        loginbtn=Button(frame,command=self.login,text="LOGIN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="red",activebackground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        ##register 
        loginbtn=Button(frame,text="NEW USER Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="black",activebackground="white")
        loginbtn.place(x=10,y=350,width=160)

        #forgot pass

        loginbtn=Button(frame,text="Forgot Password",command=self.forget_password,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="black",activebackground="white")
        loginbtn.place(x=10,y=375,width=160)

    def register_window(self):
            self.new_window = Toplevel(self.root)
            self.app=register(self.new_window)
        

    def login(self):
        if self.txtusr.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "Please enter details!")
        
        elif self.txtusr.get()=="admin" and self.txtpass.get()=="mcoe":
            self.new_window = Toplevel(self.root)
            self.app=display_admin(self.new_window)
            # messagebox.showinfo("Successfull As Admin Login","Welcome To The Student DataBase System")

        elif self.txtusr.get()=="adminmcoe@gmail.com" and self.txtpass.get()=="mcoe@2023":
            self.new_window = Toplevel(self.root)
            self.app=display_admin(self.new_window)
            # messagebox.showinfo("Successfull As Admin Login","Welcome To The Student DataBase System")

        else:
            self.name=self.txtusr.get()
            self.pass1=self.txtpass.get()

            conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register2 where name= %s and pass=%s", (
                                                                                    self.txtusr.get(),
                                                                                    self.txtpass.get()            
                                                                                    )) 

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else: 
                # self.new_window = Toplevel(self.root)
                # self.app=self.display_student(self.new_window)
                self.display_student(self.name,self.pass1)
                
            conn.commit()            
            conn.close()

    def forget_password(self):
        if self.txtusr.get()=="":
            messagebox.showerror("Error","Please enter the valid username to reset your password!",parent=self.root)
        else:
            self.root2=Toplevel()
            self.root2.title("Forget Password ")
            self.root2.geometry("500x450+450+180")
            self.root2.config(bg="white")
            self.root2.focus_force()
            self.root2.grab_set()
            t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="lightgrey",fg="red").place(x=0,y=10,relwidth=1)

            ##sequrity question
            question=Label(self.root2,text="Security Question:",font=("times of roman",15,"bold"))
            cmb_quest=ttk.Combobox(self.root2,font=("times of roman",12),state='readonly',justify=CENTER)
            cmb_quest['value']=("Select","What was the name of your first school?","What was the name of your first pet?","What is birthdate of your bestfriend?")
            question.place(x=120,y=70,width=250)
            cmb_quest.place(x=120,y=100,width=250)
            cmb_quest.current(0)
            ##answer(sequrity)
            answer=Label(self.root2,text="Answer:",font=("times of roman",15,"bold")).place(x=120,y=150,width=250)  
            txt_answer=Entry(self.root2,font=("times of roman",12),bg="lightgrey").place(x=120,y=180,width=250)   
            
            #new password
            newpass=Label(self.root2,text="New Password:",font=("times of roman",15,"bold")).place(x=120,y=230,width=250)  
            newpass_answer=Entry(self.root2,font=("times of roman",12),bg="lightgrey").place(x=120,y=260,width=250)   
            ##confirm password
            cpass=Label(self.root2,text="Confirm Password:",font=("times of roman",15,"bold")).place(x=120,y=310,width=250)  
            c_answer=Entry(self.root2,font=("times of roman",12),bg="lightgrey").place(x=120,y=340,width=250)   
            
            ###Reset password
            button_change_pass=Button(self.root2,text="Reset Password",bg="green",fg="white",font=("times of roman",13,"bold")).place(x=170,y=390)
        

    def display_student(self,name,dob):
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
        
        #Symbol

        # Load the image
        image = Image.open("./images/mcoe_sym.png")
        image = image.resize((50, 50))  # Resize the image if necessary

        # Convert the image to Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = Label(self.root, image=photo)
        image_label.pack(anchor='nw')

        #Background image
        self.bg=ImageTk.PhotoImage(file=r"./images/BG1.jpg")
        bglbl=Label(self.root,image=self.bg)
        bglbl.place(x=0,y=0,relwidth=1,relheight=1)

        # bg image
        img=Image.open(r"./images/BG1.jpg")
        self.photoimg=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,width=1600,height=900)
        # MCOE Name

        getstr=Label(self.root,text="Progressive Education Society's Modern College Of Engineering",font=("times new roman",30,"bold"),fg="black")
        getstr.place(x=220,y=20)

        getstr=Label(self.root,text="Deparment Of Computer Engineering",font=("times new roman",30,"bold"),fg="black")
        getstr.place(x=220,y=80)

        # MANAGE FRAME
        Manage_Frame=LabelFrame(bg_lbl,bd=10,relief=RIDGE,padx=4,bg="white")
        Manage_Frame.place(x=20,y=130,width=1480,height=640)

        # STUDENT INFO
        Data_Left_Frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=10,text="Student Information",font=("times new roman",15,"bold"),fg="red",bg="white")
        Data_Left_Frame.place(x=100,y=15,width=1380,height=590)
        
        # CURRENT COURSE INFO
        Current_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Current Course Information",font=("times new roman",15,"bold"),fg="green",bg="white")
        Current_Frame.place(x=5,y=5,width=1360,height=550)

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
        # CITY
        lbl_city=Label(Class_Frame,text="     City : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_city.grid(row=4, column=2,padx=2,sticky=W)

        city=ttk.Entry(Class_Frame,textvariable=self.var_city,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        city.grid(row=4,column=3,padx=2,pady=20,sticky=W)

        # PINCODE
        lbl_pin=Label(Class_Frame,text="   Pincode : ",font=("arial",12,"bold"),bg="white",width=30)
        lbl_pin.grid(row=5, column=2,padx=2,sticky=W)

        pin=ttk.Entry(Class_Frame,textvariable=self.var_pincode,font=("Times New Roman",15,"bold"),width=25,state="readonly")
        pin.grid(row=5,column=3,padx=2,pady=20,sticky=W)

        # BUTTONS FRAME
        Button_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,bg="white")
        Button_Frame.place(x=260,y=520,width=670,height=40)

        # EXIT BUTTON
        save=Button(Button_Frame,text="EXIT",command=self.exit_window,font=("times new roman",10,"bold"),borderwidth=0,width=30,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        save.grid(row=0,column=0,padx=1,pady=0)

        # UPDATE BUTTON
        update=Button(Button_Frame,text="UPDATE",command=self.working_page,font=("times new roman",10,"bold"),borderwidth=0,width=30,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        update.grid(row=0,column=1,padx=7,pady=0)

        # Login BUTTON
        Login=Button(Button_Frame,text="New Registration",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,width=30,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        Login.grid(row=0,column=2,padx=5,pady=0)

        # RESET BUTTON
        reset=Button(Button_Frame,text="RESET",font=("times new roman",10,"bold"),borderwidth=0,width=30,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        reset.grid(row=0,column=3,padx=5,pady=0)

        conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from register2 where name= %s and dob=%s", (
                                                                                    self.txtusr.get(),
                                                                                    self.txtpass.get()            
                                                                                    ))
        data=my_cursor.fetchall()
        my_cursor.execute("select * from register2 where name= %s and dob=%s", (
                                                                                    self.txtusr.get(),
                                                                                    self.txtpass.get()            
                                                                                    ))
        row = my_cursor.fetchone()
        if row == None:
                messagebox.showerror("Error", "Invalid Username and Password")
        else:
            self.var_id.set(row[0])
            self.var_course.set(row[1])
            self.var_year.set(row[2])
            self.var_sem.set(row[3])
            self.var_name.set(row[4])
            self.var_div.set(row[5])
            self.var_roll.set(row[6])
            self.var_gender.set(row[7])
            self.var_dob.set(row[8])
            self.var_email.set(row[9])
            self.var_phone.set(row[10])
            self.var_address.set(row[11])
            self.var_teacher.set(row[12])
            self.var_city.set(row[15])
            self.var_pincode.set(row[16])

        conn.commit()            
        conn.close()

    def exit_window(self):
       # Load the image
        image = Image.open("./images/mcoe_sym.png")
        image = image.resize((50, 50))  # Resize the image if necessary

        # Convert the image to Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = Label(self.root, image=photo)
        image_label.pack(anchor='nw')

        #Background image
        self.bg=ImageTk.PhotoImage(file=r"./images/BG1.jpg")
        bglbl=Label(self.root,image=self.bg)
        bglbl.place(x=0,y=0,relwidth=1,relheight=1)

        # bg image
        img=Image.open(r"./images/BG1.jpg")
        self.photoimg=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,width=1600,height=900)
        # MCOE Name

        getstr=Label(self.root,text="Progressive Education Society's Modern College Of Engineering",font=("times new roman",30,"bold"),fg="black")
        getstr.place(x=220,y=30)

        getstr=Label(self.root,text="Deparment Of Computer Engineering",font=("times new roman",30,"bold"),fg="black")
        getstr.place(x=220,y=100)

        getstr=Label(self.root,text="Thank you!!!!",font=("times new roman",30,"bold"),fg="black")
        getstr.place(x=600,y=300)

    def working_page(self):
        # Load the image
        image = Image.open("./images/mcoe_sym.png")
        image = image.resize((50, 50))  # Resize the image if necessary

        # Convert the image to Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = Label(self.root, image=photo)
        image_label.pack(anchor='nw')

        #Background image
        self.bg=ImageTk.PhotoImage(file=r"./images/BG1.jpg")
        bglbl=Label(self.root,image=self.bg)
        bglbl.place(x=0,y=0,relwidth=1,relheight=1)

        # bg image
        img=Image.open(r"./images/BG1.jpg")
        self.photoimg=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,width=1600,height=900)
        # MCOE Name

        getstr=Label(self.root,text="Progressive Education Society's Modern College Of Engineering",font=("times new roman",30,"bold"),fg="black")
        getstr.place(x=220,y=30)

        getstr=Label(self.root,text="Deparment Of Computer Engineering",font=("times new roman",30,"bold"),fg="black")
        getstr.place(x=220,y=100)

        getstr=Label(self.root,text="Team in Working on Update Function",font=("times new roman",30,"bold"),fg="black")
        getstr.place(x=400,y=300)

        getstr=Label(self.root,text="Admin Login required",font=("times new roman",20,"bold"),fg="black")
        getstr.place(x=600,y=400)


        Manage_Frame=LabelFrame(bg_lbl,bd=4,relief=RIDGE,padx=4,bg="white",background="")
        Manage_Frame.place(x=360,y=520,width=700,height=150)
        


   
    

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
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
        self.var_pass=StringVar()

        

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
        Manage_Frame=LabelFrame(bg_lbl,bd=4,relief=RIDGE,padx=4,bg="white",background="")
        Manage_Frame.place(x=15,y=55,width=1500,height=750)

        # LEFT FRAME
        Data_Left_Frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=4,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Data_Left_Frame.place(x=15,y=15,width=650,height=700)

        # RIGHT FRAME
        Data_Right_Frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=4,text="Student Details",font=("times new roman",12,"bold"),fg="red",bg="white")
        Data_Right_Frame.place(x=825,y=15,width=650,height=700)

        # CURRENT COURSE INFO
        Current_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Current Course Information",font=("times new roman",12,"bold"),fg="green",bg="white")
        Current_Frame.place(x=5,y=5,width=628,height=125)

        # # Dept Dropdown
        # lbl_dep=Label(Current_Frame,text="Department : ",font=("arial",10,"bold"),bg="white",width=12)
        # lbl_dep.grid(row=0, column=0,padx=2,sticky=W)

        # combo_dep=ttk.Combobox(Current_Frame,textvariable=self.var_dep, font=("arial",12),width=15,state="readonly")
        # combo_dep["value"]=("Select Dept.","Computer","Civil","Mechanical","Electrical","EnTC","AIDS","AIML")
        # combo_dep.current(0)
        # combo_dep.grid(row=0, column=1,padx=2,pady=10,sticky=W)
        self.var_dep="computer"

         # CLASS DIVISION

        lbl_div=Label(Current_Frame,text="Division : ",font=("arial",10,"bold"),bg="white")
        lbl_div.grid(row=0, column=0,padx=2,sticky=W)

        combo_div=ttk.Combobox(Current_Frame,textvariable=self.var_div,state="readonly",font=("arial",10,"bold"))
        combo_div['value']=("A","B")
        combo_div.grid(row=0,column=1,sticky=W,padx=2)

        #COURSE
        course=Label(Current_Frame,font=("arial",10,"bold"),text="Course : ",bg="white")
        course.grid(row=0,column=2,sticky=E,padx=20,pady=10)

        combo_course=ttk.Combobox(Current_Frame,textvariable=self.var_course,state="readonly",font=("arial",12),text="Select Course",width=15)
        combo_course['value']=("FE","SE","TE","BE")
        combo_course.grid(row=0,column=3,sticky=W,padx=2,pady=10)  

        # YEAR

        Year=Label(Current_Frame,font=("arial",10,"bold"),text="Year : ",bg="white")
        Year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        combo_year=ttk.Combobox(Current_Frame,textvariable=self.var_year,state="readonly",font=("arial",12,),width=15)
        combo_year['value']=("2020-2021","2021-2022","2022-2023","2023-2024")
        combo_year.grid(row=1,column=1,sticky=W,padx=2)

        #Semester

        Sem=Label(Current_Frame,font=("arial",10,"bold"),text="Semester : ",bg="white")
        Sem.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        combo_sem=ttk.Combobox(Current_Frame,textvariable=self.var_sem,state="readonly",font=("arial",12),width=15)
        combo_sem['value']=("Sem-I","Sem-II")
        combo_sem.grid(row=1,column=3,sticky=W,padx=2,pady=10)

        # STUDENT CLASSS INFORMATION

        Class_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Student Class Information",font=("times new roman",12,"bold"),fg="green",bg="white")
        Class_Frame.place(x=5,y=140,width=628,height=475)

        # STUDENT ID NUMBER

        lbl_id=Label(Class_Frame,text="Student ID : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_id.grid(row=0, column=0,padx=2,sticky=W)

        id=ttk.Entry(Class_Frame,textvariable=self.var_id,font=("Times New Roman",15,"bold"),width=15)
        id.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # STUDENT NAME

        lbl_name=Label(Class_Frame,text="Student Name : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_name.grid(row=0, column=2,padx=2,sticky=W)

        name=ttk.Entry(Class_Frame,textvariable=self.var_name,font=("Times New Roman",15,"bold"),width=15)
        name.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #TEACHER NAME

        lbl_teacher=Label(Class_Frame,text="Teacher : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_teacher.grid(row=1, column=0,padx=2,sticky=W)

        teacher=ttk.Entry(Class_Frame,textvariable=self.var_teacher,font=("Times New Roman",15,"bold"),width=15)
        teacher.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # ROLL NUMBER

        lbl_roll=Label(Class_Frame,text="Roll No. : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_roll.grid(row=1, column=2,padx=2,sticky=W)

        roll=ttk.Entry(Class_Frame,textvariable=self.var_roll,font=("Times New Roman",15,"bold"),width=15)
        roll.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # GENDER

        lbl_gender=Label(Class_Frame,text="Gender : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_gender.grid(row=2, column=0,padx=2,sticky=W)

        combo_gender=ttk.Combobox(Class_Frame,textvariable=self.var_gender,state="readonly",font=("arial",10,"bold"),width=15)
        combo_gender['value']=("Male","Female","Other")
        combo_gender.grid(row=2,column=1,sticky=W,padx=2)

        # DATE OF BIRTH
        
        lbl_dob=Label(Class_Frame,text="Date Of Birth : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_dob.grid(row=2, column=2,padx=2,sticky=W)

        dob=ttk.Entry(Class_Frame,textvariable=self.var_dob,font=("Times New Roman",15,"bold"),width=15)
        dob.grid(row=2,column=3,padx=2,pady=10,sticky=W)        

        # EMAIL

        lbl_mail=Label(Class_Frame,text="Email : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_mail.grid(row=3, column=0,padx=2,sticky=W)

        mail=ttk.Entry(Class_Frame,textvariable=self.var_email,font=("Times New Roman",15,"bold"),width=15)
        mail.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # PHONE

        lbl_phone=Label(Class_Frame,text="Phone No. : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_phone.grid(row=3, column=2,padx=2,sticky=W)

        phone=ttk.Entry(Class_Frame,textvariable=self.var_phone,font=("Times New Roman",15,"bold"),width=15)
        phone.grid(row=3,column=3,padx=2,pady=10,sticky=W)

        # SECURITY QUESTION

        lbl_sec_q=Label(Class_Frame,text="Security Question :",font=("arial",10,"bold"),bg="white",width=12)
        lbl_sec_q.grid(row=4, column=0,padx=2,sticky=W)

        combo_sec_q=ttk.Combobox(Class_Frame,textvariable=self.var_sec_q,state="readonly",font=("arial",10,"bold"),width=20)
        combo_sec_q['value']=("What was the name of your first school?","What was the name of your first pet?","What is birthdate of your bestfriend?")
        combo_sec_q.place(x=110,y=195,width=425,height=25)

        # SECURITY QUESTION ANSWER
        
        lbl_sec_ans=Label(Class_Frame,text="Answer : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_sec_ans.grid(row=5, column=0,padx=2,sticky=W)

        sec_ans=ttk.Entry(Class_Frame,textvariable=self.var_sec_ans,font=("Times New Roman",15,"bold"),width=15)
        sec_ans.grid(row=5,column=1,padx=2,pady=10,sticky=W)      

        # PASSWORD
        
        lbl_pass=Label(Class_Frame,text="Password : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_pass.grid(row=5, column=2,padx=2,sticky=W)

        sec_pass=ttk.Entry(Class_Frame,textvariable=self.var_pass,font=("Times New Roman",15,"bold"),width=15,show='*')
        sec_pass.grid(row=5,column=3,padx=2,pady=10,sticky=W) 
        # CITY

        lbl_city=Label(Class_Frame,text="City : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_city.grid(row=6, column=0,padx=2,sticky=W)

        mail=ttk.Entry(Class_Frame,textvariable=self.var_city,font=("Times New Roman",15,"bold"),width=15)
        mail.grid(row=6,column=1,padx=2,pady=10,sticky=W)

        # PINCODE

        lbl_pincode=Label(Class_Frame,text="Pincode : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_pincode.grid(row=6, column=2,padx=2,sticky=W)

        mail=ttk.Entry(Class_Frame,textvariable=self.var_pincode,font=("Times New Roman",15,"bold"),width=15)
        mail.grid(row=6,column=3,padx=2,pady=10,sticky=W)

        #ADDRESS

        lbl_address=Label(Class_Frame,text="Address : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_address.grid(row=7, column=0,padx=2,sticky=W)

        address=ttk.Entry(Class_Frame,textvariable=self.var_address,font=("Times New Roman",15,"bold"),width=15)
        address.place(x=110,y=320,width=425,height=75)
        
        # BUTTONS FRAME
        Button_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,bg="white")
        Button_Frame.place(x=5,y=625,width=628,height=45)

        # SAVE BUTTON
        save=Button(Button_Frame,text="SAVE",command=self.register_data , font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        save.grid(row=0,column=0,padx=1,pady=0)


        # UPDATE BUTTON

        update=Button(Button_Frame,text="UPDATE",font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        update.grid(row=0,column=1,padx=1,pady=0)

        # DELETE BUTTON

        delete=Button(Button_Frame,text="DELETE",font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        delete.grid(row=0,column=2,padx=1,pady=0)

        # RESET BUTTON

        reset=Button(Button_Frame,text="RESET",command=self.clear_data ,font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        reset.grid(row=0,column=3,padx=1,pady=0)

        # SEARCH FRAME

        Search_Frame=LabelFrame(Data_Right_Frame,bd=4,relief=RIDGE,padx=4,text="Search Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=0,width=634,height=70)

        search_title=Label(Search_Frame,font=("arial",12,"bold"),text="Search By : ",fg="red",bg="white")
        search_title.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        combo_search=ttk.Combobox(Search_Frame,state="readonly",font=("arial",10,"bold"),width=15)
        combo_search['value']=("Name","Student ID","Roll no.","Phone Number")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,sticky=W,padx=2)

        search_txt=ttk.Entry(Search_Frame,font=("Times New Roman",15,"bold"),width=15)
        search_txt.grid(row=0,column=2,padx=2,sticky=W)
        
        search_btn=Button(Search_Frame,text="SEARCH",font=("times new roman",10,"bold"),borderwidth=0,width=15,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        search_btn.grid(row=0,column=3,padx=2,pady=0)

        ShowAll_btn=Button(Search_Frame,text="SHOW ALL",font=("times new roman",10,"bold"),borderwidth=0,width=15,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        ShowAll_btn.grid(row=0,column=4,padx=2,pady=0)

        ######################## TABLE & SCROLL BAR ########################

        Table_Frame=Frame(Data_Right_Frame,bd=4,relief=RIDGE,bg="white")
        Table_Frame.place(x=0,y=71,height=600,width=634)

        Scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        # DECLARING COLUMNS

        self.student_table=ttk.Treeview(Table_Frame,columns=("ID","COURSE","YEAR","SEM","NAME","DIV","ROLL NO.","GENDER","DOB","EMAIL","PHONE","ADDRESS","TEACHER"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        # Packing the scrollbar
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        #DECLARING ALL HEADINGS

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("COURSE",text="COURSE")
        self.student_table.heading("YEAR",text="YEAR")
        self.student_table.heading("SEM",text="SEM")
        self.student_table.heading("NAME",text="NAME")
        self.student_table.heading("DIV",text="DIV")
        self.student_table.heading("ROLL NO.",text="ROLL NO.")
        self.student_table.heading("GENDER",text="GENDER")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("EMAIL",text="EMAIL")
        self.student_table.heading("PHONE",text="PHONE")
        self.student_table.heading("ADDRESS",text="ADDRESS")
        self.student_table.heading("TEACHER",text="TEACHER")

        self.student_table["show"]="headings"

        #ASSIGNING WIDTH TO ALL HEADINGS

        self.student_table.column("ID",width=100)
        self.student_table.column("COURSE",width=100)
        self.student_table.column("YEAR",width=100)
        self.student_table.column("SEM",width=100)
        self.student_table.column("NAME",width=100)
        self.student_table.column("DIV",width=100)
        self.student_table.column("ROLL NO.",width=100)
        self.student_table.column("GENDER",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("EMAIL",width=100)
        self.student_table.column("PHONE",width=100)
        self.student_table.column("ADDRESS",width=100)
        self.student_table.column("TEACHER",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        
       
        
        

###################################################Conections########################################################################################################################
    def register_data(self):
        if self.var_id.get()=="" or self.var_name.get()==""  or self.var_roll.get()==""  or self.var_dob.get()==""  or self.var_email.get()==""  or self.var_phone.get()==""  or self.var_address.get()==""  or self.var_teacher.get()=="" or self.var_sec_ans.get()==""  :
            messagebox.showerror("Error", "All Feilds Are Required.")
        else:  
                try:
                    conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
                    my_cursor = conn.cursor()
                    query = ("select * from register2 where id=%s")
                    value= (self.var_id.get(),)
                    self.name=self.var_name.get()
                    self.dob=self.var_dob.get()
                    my_cursor.execute(query,value)
                    row = my_cursor.fetchone()
                    if row !=None:
                        messagebox.showerror("Error","Student Enter Correct ID")
                        ttk.destroy()
                    else:
                        my_cursor.execute("insert into register2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_id.get(),
                                                                                                                    # self.var_dep,
                                                                                                                    self.var_course.get(),  
                                                                                                                    self.var_year.get(),  
                                                                                                                    self.var_sem.get(),  
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),  
                                                                                                                    self.var_dob.get(),  
                                                                                                                    self.var_email.get(),  
                                                                                                                    self.var_phone.get(),  
                                                                                                                    self.var_address.get(), 
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_sec_q.get(),
                                                                                                                    self.var_sec_ans.get(),
                                                                                                                    self.var_city.get(),
                                                                                                                    self.var_pincode.get(),
                                                                                                                    self.var_pass.get()
                                                                                                                    ))
                        messagebox.showinfo("Success","Entered Data is Saved") 
                    # self.display_student(self.name,self.dob)    
                    conn.commit()
                    # self.fetch_data()
                    conn.close()
                    self.clear_data()
                    # self.fetch_data_for(self.name,self.dob)
                       
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    #Don't which is Root...Need to check once while eceptions 
        
        

    def clear_data(self):
        self.var_id="" 
        self.var_name=""
        self.var_roll=""  
        self.var_dob=""  
        self.var_email=""  
        self.var_phone=""  
        self.var_address="" 
        self.var_teacher=""
        self.var_sec_ans=""
        self.var_city=""
        self.var_pincode=""
        self.var_pass=""


    #Fetching data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from register2 where name= %s and dob=%s", (
                                                                                    self.txtusr.get(),
                                                                                    self.txtpass.get()            
                                                                                    ))
        data=my_cursor.fetchall()
        if(len(data)!=0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def fetch_data_for(self,name,dob):
        conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from register2 where name= %s and dob=%s")
        data=my_cursor.fetchall()
        if(len(data)!=0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()      



    #Display data after the registeration
    def display_student(self,name,dob):
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
        
        frame1=Frame(self.root,bg="white")
        frame1.place(x=100,y=100,width=340,height=150)
        getstr1=Label(frame1,text="PESMCOE",font=("times new roman",20,"bold"),fg="red")
        getstr1.place(x=100,y=100)

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

        #PINCODE
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


        # self.var_dep=StringVar()
        # self.var_course=StringVar()
        # self.var_year=StringVar()
        # self.var_sem=StringVar()
        # self.var_id=StringVar()
        # self.var_name=StringVar()
        # self.var_div=StringVar()
        # self.var_roll=StringVar()
        # self.var_gender=StringVar()
        # self.var_dob=StringVar()
        # self.var_email=StringVar()
        # self.var_phone=StringVar()
        # self.var_address=StringVar()
        # self.var_teacher=StringVar()
        # self.var_sec_q=StringVar()
        # self.var_sec_ans=StringVar()
        # self.var_city=StringVar()
        # self.var_pincode=StringVar()
        # self.var_name.set("adhish")
        conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from register2 where name= %s and dob=%s", (
                                                                                    self.txtusr.get(),
                                                                                    self.txtpass.get()            
                                                                                    ))
        data=my_cursor.fetchall()
        my_cursor.execute("select * from register2 where name= %s and dob=%s", (
                                                                                    self.txtusr.get(),
                                                                                    self.txtpass.get()            
                                                                                    ))
        row = my_cursor.fetchone()
        if row == None:
                messagebox.showerror("Error", "Invalid Username and Password")
        else:
            self.var_id.set(row[0])
            self.var_course.set(row[1])
            self.var_year.set(row[2])
            self.var_sem.set(row[3])
            self.var_name.set(row[4])
            self.var_div.set(row[5])
            self.var_roll.set(row[6])
            self.var_gender.set(row[7])
            self.var_dob.set(row[8])
            self.var_email.set(row[9])
            self.var_phone.set(row[10])
            self.var_address.set(row[11])
            self.var_teacher.set(row[12])

            conn.commit()            
            conn.close() 
        # self.var_city=StringVar()
        # self.var_pincode=StringVar()

    def clear_data(self):
        self.var_id.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_sem.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
                
    


class display_admin:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin")
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
        self.var_pass=StringVar()

        

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
        Manage_Frame=LabelFrame(bg_lbl,bd=4,relief=RIDGE,padx=4,bg="white",background="")
        Manage_Frame.place(x=15,y=55,width=1500,height=750)

        # LEFT FRAME
        Data_Left_Frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=4,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Data_Left_Frame.place(x=15,y=15,width=650,height=700)

        # RIGHT FRAME
        Data_Right_Frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=4,text="Student Details",font=("times new roman",12,"bold"),fg="red",bg="white")
        Data_Right_Frame.place(x=825,y=15,width=650,height=700)

        # CURRENT COURSE INFO
        Current_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Current Course Information",font=("times new roman",12,"bold"),fg="green",bg="white")
        Current_Frame.place(x=5,y=5,width=628,height=125)

        # # Dept Dropdown
        # lbl_dep=Label(Current_Frame,text="Department : ",font=("arial",10,"bold"),bg="white",width=12)
        # lbl_dep.grid(row=0, column=0,padx=2,sticky=W)

        # combo_dep=ttk.Combobox(Current_Frame,textvariable=self.var_dep, font=("arial",12),width=15,state="readonly")
        # combo_dep["value"]=("Select Dept.","Computer","Civil","Mechanical","Electrical","EnTC","AIDS","AIML")
        # combo_dep.current(0)
        # combo_dep.grid(row=0, column=1,padx=2,pady=10,sticky=W)
        self.var_dep="computer"

         # CLASS DIVISION

        lbl_div=Label(Current_Frame,text="Division : ",font=("arial",10,"bold"),bg="white")
        lbl_div.grid(row=0, column=0,padx=2,sticky=W)

        combo_div=ttk.Combobox(Current_Frame,textvariable=self.var_div,state="readonly",font=("arial",10,"bold"))
        combo_div['value']=("A","B")
        combo_div.grid(row=0,column=1,sticky=W,padx=2)

        #COURSE
        course=Label(Current_Frame,font=("arial",10,"bold"),text="Course : ",bg="white")
        course.grid(row=0,column=2,sticky=E,padx=20,pady=10)

        combo_course=ttk.Combobox(Current_Frame,textvariable=self.var_course,state="readonly",font=("arial",12),text="Select Course",width=15)
        combo_course['value']=("FE","SE","TE","BE")
        combo_course.grid(row=0,column=3,sticky=W,padx=2,pady=10)  

        # YEAR

        Year=Label(Current_Frame,font=("arial",10,"bold"),text="Year : ",bg="white")
        Year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        combo_year=ttk.Combobox(Current_Frame,textvariable=self.var_year,state="readonly",font=("arial",12,),width=15)
        combo_year['value']=("2020-2021","2021-2022","2022-2023","2023-2024")
        combo_year.grid(row=1,column=1,sticky=W,padx=2)

        #Semester

        Sem=Label(Current_Frame,font=("arial",10,"bold"),text="Semester : ",bg="white")
        Sem.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        combo_sem=ttk.Combobox(Current_Frame,textvariable=self.var_sem,state="readonly",font=("arial",12),width=15)
        combo_sem['value']=("Sem-I","Sem-II")
        combo_sem.grid(row=1,column=3,sticky=W,padx=2,pady=10)

        # STUDENT CLASSS INFORMATION

        Class_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Student Class Information",font=("times new roman",12,"bold"),fg="green",bg="white")
        Class_Frame.place(x=5,y=140,width=628,height=475)

        # STUDENT ID NUMBER

        lbl_id=Label(Class_Frame,text="Student ID : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_id.grid(row=0, column=0,padx=2,sticky=W)

        id=ttk.Entry(Class_Frame,textvariable=self.var_id,font=("Times New Roman",15,"bold"),width=15)
        id.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # STUDENT NAME

        lbl_name=Label(Class_Frame,text="Student Name : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_name.grid(row=0, column=2,padx=2,sticky=W)

        name=ttk.Entry(Class_Frame,textvariable=self.var_name,font=("Times New Roman",15,"bold"),width=15)
        name.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #TEACHER NAME

        lbl_teacher=Label(Class_Frame,text="Teacher : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_teacher.grid(row=1, column=0,padx=2,sticky=W)

        teacher=ttk.Entry(Class_Frame,textvariable=self.var_teacher,font=("Times New Roman",15,"bold"),width=15)
        teacher.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # ROLL NUMBER

        lbl_roll=Label(Class_Frame,text="Roll No. : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_roll.grid(row=1, column=2,padx=2,sticky=W)

        roll=ttk.Entry(Class_Frame,textvariable=self.var_roll,font=("Times New Roman",15,"bold"),width=15)
        roll.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # GENDER

        lbl_gender=Label(Class_Frame,text="Gender : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_gender.grid(row=2, column=0,padx=2,sticky=W)

        combo_gender=ttk.Combobox(Class_Frame,textvariable=self.var_gender,state="readonly",font=("arial",10,"bold"),width=15)
        combo_gender['value']=("Male","Female","Other")
        combo_gender.grid(row=2,column=1,sticky=W,padx=2)

        # DATE OF BIRTH
        
        lbl_dob=Label(Class_Frame,text="Date Of Birth : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_dob.grid(row=2, column=2,padx=2,sticky=W)

        dob=ttk.Entry(Class_Frame,textvariable=self.var_dob,font=("Times New Roman",15,"bold"),width=15)
        dob.grid(row=2,column=3,padx=2,pady=10,sticky=W)        

        # EMAIL

        lbl_mail=Label(Class_Frame,text="Email : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_mail.grid(row=3, column=0,padx=2,sticky=W)

        mail=ttk.Entry(Class_Frame,textvariable=self.var_email,font=("Times New Roman",15,"bold"),width=15)
        mail.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # PHONE

        lbl_phone=Label(Class_Frame,text="Phone No. : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_phone.grid(row=3, column=2,padx=2,sticky=W)

        phone=ttk.Entry(Class_Frame,textvariable=self.var_phone,font=("Times New Roman",15,"bold"),width=15)
        phone.grid(row=3,column=3,padx=2,pady=10,sticky=W)

        # SECURITY QUESTION

        lbl_sec_q=Label(Class_Frame,text="Security Question :",font=("arial",10,"bold"),bg="white",width=12)
        lbl_sec_q.grid(row=4, column=0,padx=2,sticky=W)

        combo_sec_q=ttk.Combobox(Class_Frame,textvariable=self.var_sec_q,state="readonly",font=("arial",10,"bold"),width=20)
        combo_sec_q['value']=("What was the name of your first school?","What was the name of your first pet?","What is birthdate of your bestfriend?")
        combo_sec_q.place(x=110,y=195,width=425,height=25)

        # SECURITY QUESTION ANSWER
        
        lbl_sec_ans=Label(Class_Frame,text="Answer : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_sec_ans.grid(row=5, column=0,padx=2,sticky=W)

        sec_ans=ttk.Entry(Class_Frame,textvariable=self.var_sec_ans,font=("Times New Roman",15,"bold"),width=15)
        sec_ans.grid(row=5,column=1,padx=2,pady=10,sticky=W)      

        # PASSWORD
        
        lbl_pass=Label(Class_Frame,text="Password : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_pass.grid(row=5, column=2,padx=2,sticky=W)

        sec_pass=ttk.Entry(Class_Frame,textvariable=self.var_pass,font=("Times New Roman",15,"bold"),width=15,show='*')
        sec_pass.grid(row=5,column=3,padx=2,pady=10,sticky=W) 
        # CITY

        lbl_city=Label(Class_Frame,text="City : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_city.grid(row=6, column=0,padx=2,sticky=W)

        mail=ttk.Entry(Class_Frame,textvariable=self.var_city,font=("Times New Roman",15,"bold"),width=15)
        mail.grid(row=6,column=1,padx=2,pady=10,sticky=W)

        # PINCODE

        lbl_pincode=Label(Class_Frame,text="Pincode : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_pincode.grid(row=6, column=2,padx=2,sticky=W)

        mail=ttk.Entry(Class_Frame,textvariable=self.var_pincode,font=("Times New Roman",15,"bold"),width=15)
        mail.grid(row=6,column=3,padx=2,pady=10,sticky=W)

        #ADDRESS

        lbl_address=Label(Class_Frame,text="Address : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_address.grid(row=7, column=0,padx=2,sticky=W)

        address=ttk.Entry(Class_Frame,textvariable=self.var_address,font=("Times New Roman",15,"bold"),width=15)
        address.place(x=110,y=320,width=425,height=75)
        
        # BUTTONS FRAME
        Button_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,bg="white")
        Button_Frame.place(x=5,y=625,width=628,height=45)

        # SAVE BUTTON
        save=Button(Button_Frame,text="SAVE",command=self.register_data , font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        save.grid(row=0,column=0,padx=1,pady=0)


        # UPDATE BUTTON

        update=Button(Button_Frame,text="UPDATE",command=self.update_data,font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        update.grid(row=0,column=1,padx=1,pady=0)

        # DELETE BUTTON

        delete=Button(Button_Frame,text="DELETE",font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        delete.grid(row=0,column=2,padx=1,pady=0)

        # RESET BUTTON

        reset=Button(Button_Frame,text="RESET",command=self.clear_data ,font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        reset.grid(row=0,column=3,padx=1,pady=0)

        # SEARCH FRAME

        Search_Frame=LabelFrame(Data_Right_Frame,bd=4,relief=RIDGE,padx=4,text="Search Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=0,width=634,height=70)

        search_title=Label(Search_Frame,font=("arial",12,"bold"),text="Search By : ",fg="red",bg="white")
        search_title.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        combo_search=ttk.Combobox(Search_Frame,state="readonly",font=("arial",10,"bold"),width=15)
        combo_search['value']=("Name","Student ID","Roll no.","Phone Number")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,sticky=W,padx=2)

        search_txt=ttk.Entry(Search_Frame,font=("Times New Roman",15,"bold"),width=15)
        search_txt.grid(row=0,column=2,padx=2,sticky=W)
        
        search_btn=Button(Search_Frame,text="SEARCH",font=("times new roman",10,"bold"),borderwidth=0,width=15,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        search_btn.grid(row=0,column=3,padx=2,pady=0)

        ShowAll_btn=Button(Search_Frame,text="SHOW ALL",font=("times new roman",10,"bold"),borderwidth=0,width=15,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        ShowAll_btn.grid(row=0,column=4,padx=2,pady=0)

        ######################## TABLE & SCROLL BAR ########################

        Table_Frame=Frame(Data_Right_Frame,bd=4,relief=RIDGE,bg="white")
        Table_Frame.place(x=0,y=71,height=600,width=634)

        Scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        # DECLARING COLUMNS

        self.student_table=ttk.Treeview(Table_Frame,columns=("ID","COURSE","YEAR","SEM","NAME","DIV","ROLL NO.","GENDER","DOB","EMAIL","PHONE","ADDRESS","TEACHER"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        # Packing the scrollbar
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        #DECLARING ALL HEADINGS

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("COURSE",text="COURSE")
        self.student_table.heading("YEAR",text="YEAR")
        self.student_table.heading("SEM",text="SEM")
        self.student_table.heading("NAME",text="NAME")
        self.student_table.heading("DIV",text="DIV")
        self.student_table.heading("ROLL NO.",text="ROLL NO.")
        self.student_table.heading("GENDER",text="GENDER")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("EMAIL",text="EMAIL")
        self.student_table.heading("PHONE",text="PHONE")
        self.student_table.heading("ADDRESS",text="ADDRESS")
        self.student_table.heading("TEACHER",text="TEACHER")

        self.student_table["show"]="headings"

        #ASSIGNING WIDTH TO ALL HEADINGS

        self.student_table.column("ID",width=100)
        self.student_table.column("COURSE",width=100)
        self.student_table.column("YEAR",width=100)
        self.student_table.column("SEM",width=100)
        self.student_table.column("NAME",width=100)
        self.student_table.column("DIV",width=100)
        self.student_table.column("ROLL NO.",width=100)
        self.student_table.column("GENDER",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("EMAIL",width=100)
        self.student_table.column("PHONE",width=100)
        self.student_table.column("ADDRESS",width=100)
        self.student_table.column("TEACHER",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        


        self.student_table.pack(fill=BOTH,expand=1)
        # open_main=messagebox.askyesno("YesNo", "Access only admin")
        # if open_main>0:
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        
        

# ###################################################Conections########################################################################################################################
    def register_data(self):
        if self.var_id.get()=="" or self.var_name.get()==""  or self.var_roll.get()==""  or self.var_dob.get()==""  or self.var_email.get()==""  or self.var_phone.get()==""  or self.var_address.get()==""  or self.var_teacher.get()=="" or self.var_sec_ans.get()==""  :
            messagebox.showerror("Error", "All Feilds Are Required.")
        else:  
                try:
                    conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
                    my_cursor = conn.cursor()
                    query = ("select * from register2 where id=%s")
                    value= (self.var_id.get(),)
                    self.name=self.var_name.get()
                    self.dob=self.var_dob.get()
                    my_cursor.execute(query,value)
                    row = my_cursor.fetchone()
                    if row !=None:
                        messagebox.showerror("Error","Student Enter Correct ID")
                        ttk.destroy()
                    else:
                        my_cursor.execute("insert into register2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_id.get(),
                                                                                                                    # self.var_dep,
                                                                                                                    self.var_course.get(),  
                                                                                                                    self.var_year.get(),  
                                                                                                                    self.var_sem.get(),  
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),  
                                                                                                                    self.var_dob.get(),  
                                                                                                                    self.var_email.get(),  
                                                                                                                    self.var_phone.get(),  
                                                                                                                    self.var_address.get(), 
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_sec_q.get(),
                                                                                                                    self.var_sec_ans.get(),
                                                                                                                    self.var_city.get(),
                                                                                                                    self.var_pincode.get(),
                                                                                                                    self.var_pass.get()
                                                                                                                    ))
                        messagebox.showinfo("Success","Entered Data is Saved") 
                    # self.display_student(self.name,self.dob)    
                    conn.commit()
                    # self.fetch_data()
                    conn.close()
                    self.clear_data()
                    # self.fetch_data_for(self.name,self.dob)
                       
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    #Don't which is Root...Need to check once while eceptions 
        
        

    def clear_data(self):
        self.var_id="" 
        self.var_name=""
        self.var_roll=""  
        self.var_dob=""  
        self.var_email=""  
        self.var_phone=""  
        self.var_address="" 
        self.var_teacher=""
        self.var_sec_ans=""
        self.var_city=""
        self.var_pincode=""
        self.var_pass=""

    #Fetching data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from register2 ")
        data=my_cursor.fetchall()
        if(len(data)!=0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()   


        #  Get cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data=content["values"]

        
        # self.var_id.set(data[1])
        self.var_id.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_name.set(data[4])
        self.var_div.set(data[5])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_teacher.set(data[12])
        self.var_city.set("Pune"),
        self.var_pincode.set("411005"),
        self.var_pass.set(["Can not Access"])
        self.var_sec_ans.set(["Can not Access"])


    def update_data(self):
        if self.var_id.get()=="" or self.var_name.get()==""  or self.var_roll.get()==""  or self.var_dob.get()==""  or self.var_email.get()==""  or self.var_phone.get()==""  or self.var_address.get()==""  or self.var_teacher.get()=="" or self.var_sec_ans.get()==""  :
            messagebox.showerror("Error", "All Feilds Are Required.")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this Stduent data", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="adhish@mysql",database='myproject')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update register set course=%s,year=%s,sem=%s,name=%s,div=%s,rollnum=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,tearcher=%s where id=%s", (
                                                                                                                    self.var_course.get(),  
                                                                                                                    self.var_year.get(),  
                                                                                                                    self.var_sem.get(),  
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),  
                                                                                                                    self.var_dob.get(),  
                                                                                                                    self.var_email.get(),  
                                                                                                                    self.var_phone.get(),  
                                                                                                                    self.var_address.get(), 
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_id.get()

                                                                                                                    ))
                else:
                    if not update:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Sucess", "Studuent Suceesfully Updated",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

        

        
    


if __name__=="__main__":
    # root=Tk()
    # app=login_window(root)
    # root.mainloop()
    main()