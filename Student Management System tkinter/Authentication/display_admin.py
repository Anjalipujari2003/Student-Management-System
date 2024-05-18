from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox


class display_admin:
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
        Manage_Frame=LabelFrame(bg_lbl,bd=4,relief=RIDGE,padx=4,bg="white")
        Manage_Frame.place(x=15,y=55,width=1500,height=750)

        # LEFT FRAME
        Data_Left_Frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=4,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Data_Left_Frame.place(x=15,y=15,width=650,height=700)

        # RIGHT FRAME
        Data_Right_Frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=4,text="Student Details",font=("times new roman",12,"bold"),fg="red",bg="white")
        Data_Right_Frame.place(x=825,y=15,width=650,height=700)

        # CURRENT COURSE INFO
        Current_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Current Course Information",font=("times new roman",12,"bold"),fg="green",bg="white")
        Current_Frame.place(x=5,y=5,width=628,height=250)


        # CLASS DIVISION

        lbl_div=Label(Current_Frame,text="Division : ",font=("arial",10,"bold"),bg="white")
        lbl_div.grid(row=0, column=0,padx=2,sticky=W)

        combo_div=ttk.Entry(Current_Frame,textvariable=self.var_div,state="readonly",font=("arial",10,"bold"))
        combo_div.grid(row=0,column=1,sticky=W,padx=2)

        #COURSE
        course=Label(Current_Frame,font=("arial",10,"bold"),text="Course : ",bg="white")
        course.grid(row=0,column=2,sticky=E,padx=20,pady=10)

        combo_course=ttk.Entry(Current_Frame,textvariable=self.var_course,state="readonly",font=("arial",12),text="Select Course",width=15)
        combo_course.grid(row=0,column=3,sticky=W,padx=2,pady=10)
        combo_course.insert('end','Comp')

        # YEAR

        Year=Label(Current_Frame,font=("arial",10,"bold"),text="Year : ",bg="white")
        Year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        combo_year=ttk.Entry(Current_Frame,textvariable=self.var_year,state="readonly",font=("arial",12,),width=15)
        combo_year.grid(row=1,column=1,sticky=W,padx=2)

        #Semester

        Sem=Label(Current_Frame,font=("arial",10,"bold"),text="Semester : ",bg="white")
        Sem.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        combo_sem=ttk.Entry(Current_Frame,textvariable=self.var_sem,state="readonly",font=("arial",12),width=15)
        combo_sem.grid(row=1,column=3,sticky=W,padx=2,pady=10)

        # STUDENT CLASSS INFORMATION

        Class_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,text="Student Class Information",font=("times new roman",12,"bold"),fg="green",bg="white")
        Class_Frame.place(x=5,y=265,width=628,height=350)

        # STUDENT ID NUMBER

        lbl_id=Label(Class_Frame,text="Student ID : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_id.grid(row=0, column=0,padx=2,sticky=W)

        id=ttk.Entry(Class_Frame,textvariable=self.var_id,font=("Times New Roman",15,"bold"),width=15,state="readonly")
        id.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # STUDENT NAME

        lbl_name=Label(Class_Frame,text="Student Name : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_name.grid(row=0, column=2,padx=2,sticky=W)

        name=ttk.Entry(Class_Frame,state="readonly",textvariable=self.var_name,font=("Times New Roman",15,"bold"),width=15)
        name.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        # ROLL NUMBER

        lbl_roll=Label(Class_Frame,text="Roll No. : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_roll.grid(row=1, column=2,padx=2,sticky=W)

        roll=ttk.Entry(Class_Frame,textvariable=self.var_roll,font=("Times New Roman",15,"bold"),width=15,state="readonly")
        roll.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # GENDER

        lbl_gender=Label(Class_Frame,text="Gender : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_gender.grid(row=1, column=0,padx=2,sticky=W)

        combo_gender=ttk.Entry(Class_Frame,textvariable=self.var_gender,state="readonly",font=("arial",10,"bold"))
        combo_gender.grid(row=1,column=1,sticky=W,padx=2)

        # DATE OF BIRTH
        
        lbl_dob=Label(Class_Frame,text="Date Of Birth : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_dob.grid(row=2, column=2,padx=2,sticky=W)

        dob=ttk.Entry(Class_Frame,textvariable=self.var_dob,font=("Times New Roman",15,"bold"),width=15,state="readonly")
        dob.grid(row=2,column=3,padx=2,pady=10,sticky=W)        

        # EMAIL

        lbl_mail=Label(Class_Frame,text="Email : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_mail.grid(row=2, column=0,padx=2,sticky=W)

        mail=ttk.Entry(Class_Frame,textvariable=self.var_email,font=("Times New Roman",15,"bold"),width=15,state="readonly")
        mail.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # PHONE

        lbl_phone=Label(Class_Frame,text="Phone No. : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_phone.grid(row=3, column=2,padx=2,sticky=W)

        phone=ttk.Entry(Class_Frame,textvariable=self.var_phone,font=("Times New Roman",15,"bold"),width=15,state="readonly")
        phone.grid(row=3,column=3,padx=2,pady=10,sticky=W)

        #ADDRESS

        lbl_address=Label(Class_Frame,text="Address : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_address.grid(row=4, column=0,padx=2,sticky=W)

        address=ttk.Entry(Class_Frame,textvariable=self.var_address,font=("Times New Roman",15,"bold"),width=15,state="readonly")
        address.place(x=105,y=200,width=425,height=100)

        #TEACHER NAME

        lbl_teacher=Label(Class_Frame,text="Teacher : ",font=("arial",10,"bold"),bg="white",width=12)
        lbl_teacher.grid(row=3, column=0,padx=2,sticky=W)

        teacher=ttk.Entry(Class_Frame,textvariable=self.var_teacher,font=("Times New Roman",15,"bold"),width=15,state="readonly")
        teacher.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # BUTTONS FRAME
        Button_Frame=LabelFrame(Data_Left_Frame,bd=4,relief=RIDGE,padx=4,bg="white")
        Button_Frame.place(x=5,y=625,width=628,height=45)

        # SAVE BUTTON
        save=Button(Button_Frame,text="SAVE",font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        save.grid(row=0,column=0,padx=1,pady=0)

        # UPDATE BUTTON

        update=Button(Button_Frame,text="UPDATE",font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        update.grid(row=0,column=1,padx=1,pady=0)

        # DELETE BUTTON

        delete=Button(Button_Frame,text="DELETE",font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        delete.grid(row=0,column=2,padx=1,pady=0)

        # RESET BUTTON

        reset=Button(Button_Frame,text="RESET",font=("times new roman",10,"bold"),borderwidth=0,width=21,height=2,fg="white",bg="black",activeforeground="black",activebackground="white")
        reset.grid(row=0,column=3,padx=1,pady=0)

        # SEARCH FRAME

        Search_Frame=LabelFrame(Data_Right_Frame,bd=4,relief=RIDGE,padx=4,text="Search Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=0,width=634,height=70)

        search_title=Label(Search_Frame,font=("arial",12,"bold"),text="Search By : ",fg="red",bg="white")
        search_title.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        combo_search=ttk.Combobox(Search_Frame,state="readonly",font=("arial",10,"bold"),width=15)
        combo_search['value']=("Name","Student ID","Roll no.","Phone Number")
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

        self.student_table=ttk.Treeview(Table_Frame,columns=("DEPARTMENT","COURSE","YEAR","SEM","ID","NAME","DIV","ROLL NO.","GENDER","DOB","EMAIL","PHONE","ADDRESS","TEACHER"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        # Packing the scrollbar
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        #DECLARING ALL HEADINGS

        self.student_table.heading("DEPARTMENT",text="DEPARTMENT")
        self.student_table.heading("COURSE",text="COURSE")
        self.student_table.heading("YEAR",text="YEAR")
        self.student_table.heading("SEM",text="SEM")
        self.student_table.heading("ID",text="ID")
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

        self.student_table.column("DEPARTMENT",width=100)
        self.student_table.column("COURSE",width=100)
        self.student_table.column("YEAR",width=100)
        self.student_table.column("SEM",width=100)
        self.student_table.column("ID",width=100)
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

        







if __name__=="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()