from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1710x1150+0+0")
        self.root.title("face recognition system")

        #=====================variables=============================
        self.var_dep=StringVar()
        self.var_class=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_div=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_address=StringVar()
       


        # img = Image.open("./college_images/facialrecognition.png")
        # img = img.resize((1710, 130))
        # self.photoimg = ImageTk.PhotoImage(img)
        # f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl.place(x=0, y=0, width=1710, height=130)

        img=Image.open("./college_images/scanning-banner.png")
        img=img.resize((600,130))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=600,height=130)


        img1 = Image.open("./college_images/facialrecognition.png")
        img1 = img1.resize((600, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=600, y=0, width=600, height=130)

        img2 = Image.open("./college_images/facial-recognition-system-banner.jpeg")
        img2 = img2.resize((600, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1200, y=0, width=600, height=130)

                # bg img
        img3 = Image.open("./college_images/gradimg2.webp")
        img3 = img3.resize((1720, 1050))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1720, height=1050)

        title_lbl=Label(bg_img,text="STUDENT RECORDS",font=("verdana",35,"bold"),bg="white",fg="darkgreen");
        title_lbl.place(x=0,y=0,width=1710,height="45")

        main_frame=Frame(bg_img,bd=2,background="white")
        main_frame.place(x=15,y=100,width= 1680,height=750)




        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("verdana",20,"bold"),fg="black",bg="white")
        left_frame.place(x=15,y=10,width=820,height=720)

        img_left = Image.open("./college_images/Canvastudentsbanner.webp")
        img_left = img_left.resize((800, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=0, width=813, height=130)
 
        # current course frame
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current course information",font=("verdana",20,"bold"),bg="white",fg="black")
        current_course_frame.place(x=5,y=135,width=805,height=200)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("verdana",16,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("verdana",16,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","Civil","Mechanical","BD")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=10)

        #year combo box
        year_label=Label(current_course_frame,text="Year",font=("verdana",16,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=0,column=3,padx=0)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("verdana",16,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","First Year","Second Year","Third Year")
        year_combo.current(0)
        year_combo.grid(row=0,column=4,pady=10)

        #semester combo box
        sem_label=Label(current_course_frame,text="Semester",font=("verdana",16,"bold"),bg="white",fg="navyblue")
        sem_label.grid(row=1,column=0,padx=10)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("verdana",16,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Semester","1st Semester","2nd Semester","3rd Semester","4th Semester","5th Semester","6th Semester")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=3,pady=10)


        #Division combo box
        class_label=Label(current_course_frame,text="Class",font=("verdana",16,"bold"),bg="white",fg="navyblue")
        class_label.grid(row=1,column=3,padx=10)

        class_combo=ttk.Combobox(current_course_frame,textvariable=self.var_class,font=("verdana",16,"bold"),state="readonly",width=20)
        class_combo["values"]=("Select Class","FYCO1","FYCO2","SYCO1","SYCO2","TYCO1","TYCO2","FYBD","SYBD","TYBD","FYCE1","FYCE2","SYCE1","SYCE2","TYCE1","TYCE2","FYME1","FYME2","SYME1","SYME2","TYME1","TYME2")
        class_combo.current(0)
        class_combo.grid(row=1,column=4,pady=10)

        #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",17,"bold"),fg="navyblue")
        class_Student_frame.place(x=5,y=340,width=805,height=250)

        #Student id
        studentId_label = Label(class_Student_frame,text="Std-ID:",font=("verdana",16,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",16,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student name
        student_name_label = Label(class_Student_frame,text="Std-Name:",font=("verdana",16,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",16,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        
        #Phone Number
        student_mob_label = Label(class_Student_frame,text="Mob-No:",font=("verdana",16,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=15,font=("verdana",16,"bold"))
        student_mob_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Roll No
        student_roll_label = Label(class_Student_frame,text="Roll-No:",font=("verdana",16,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("verdana",16,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",16,"bold"),fg="navyblue",bg="white")
        student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",16,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        #Date of Birth
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",16,"bold"),fg="navyblue",bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,width=15,textvariable=self.var_dob,font=("verdana",16,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",16,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,width=15,textvariable=self.var_email,font=("verdana",16,"bold"))
        student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

       
        #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",16,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,width=15,textvariable=self.var_address,font=("verdana",16,"bold"))
        student_address_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)


        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1 ,text="No Photo Sample",value="no")
        radiobtn2.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=5,y=605,width=805,height=45)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("verdana",16,"bold"),fg="black",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("verdana",16,"bold"),fg="black",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("verdana",16,"bold"),fg="black",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("verdana",16,"bold"),fg="black",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W) 

        #Button Frame
        btn2_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn2_frame.place(x=5,y=655,width=805,height=35)

         #take photo button
        take_photo_btn=Button(btn2_frame,text="Take Pic",command=self.generate_dataset,width=32,font=("verdana",16,"bold"),fg="black",bg="navyblue")
        take_photo_btn.grid(row=0,column=0,padx=5,pady=3,sticky=W)

        #update photo button
        update_photo_btn=Button(btn2_frame,text="Update Pic",width=32,font=("verdana",16,"bold"),fg="black",bg="navyblue")
        update_photo_btn.grid(row=0,column=1,padx=5,pady=3,sticky=W)


        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("verdana",20,"bold"),fg="black",bg="white")
        right_frame.place(x=845,y=10,width=820,height=720)

        img_right = Image.open("./college_images/studdetailsbaner.png")
        img_right = img_right.resize((800, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=810, height=130)

        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",20,"bold"),fg="navyblue")
        search_frame.place(x=5,y=135,width=805,height=100)

      
        search_label = Label(search_frame,text="Search By:",font=("verdana",17,"bold"),fg="darkgreen",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("verdana",16,"bold"),state="readonly",width=13)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,width=13,font=("verdana",17,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width=9,font=("verdana",17,"bold"),fg="black",bg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn=Button(search_frame,text="Show All",width=8,font=("verdana",17,"bold"),fg="black",bg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

        #table frame
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=245,width=805,height=400)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Department","Class","Year","Sem","Id","Name","Roll-No","Gender","DOB","Email","Phone","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Class",text="Class")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll-No",text="Roll-No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="Photo")

        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Class",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=140)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=100)

        # self.student_table.column("Gender",width=100)
        # self.student_table.column("DOB",width=100)
        # self.student_table.column("Teacher",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        # ====================function declarrtion======================
         
    def add_data(self): 
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="swarnim0129",database="face_recognizer",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_class.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details added successfully ",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# ========================fetch data=======================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="swarnim0129", database="face_recognizer", auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()

# =========================get cursor=========================

    def get_cursor(self,event=" "):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_class.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

#=========================update function=====================
    def update_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)


        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="swarnim0129",database="face_recognizer", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,Class=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo=%s where Student_id=%s",(
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_class.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                             ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

# ===========================delete function====================

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is required to delete the data",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Confirmation","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="swarnim0129",
                                                   database="face_recognizer", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                self.fetch_data()

            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)



# ==============================function reset data=====================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_class.set("Select Class"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")


# ==========================generate dataset and photo samples================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)


        else:
            try:
                
                conn = mysql.connector.connect(host="localhost", user="root", password="swarnim0129",database="face_recognizer", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,Class=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo=%s where Student_id=%s",(
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_class.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                             ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 

# ==============================loadpredefined data on facefrontals from opencv=========================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)  #white color
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==180:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Datasets Completed ")

            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)











 
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()