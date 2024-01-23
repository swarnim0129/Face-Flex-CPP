from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
from tkinter import filedialog 
import csv

mydata=[]
class Attendance:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1710x1150+0+0")
        self.root.title("Attendance Management")

        img=Image.open("./college_images/scanning-banner.png")
        img=img.resize((600,130))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=600,height=130)

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()
        


        img1 = Image.open("./college_images/facialrecognition.png")
        img1 = img1.resize((600,150))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=600, y=0, width=600, height=130)

        img2 = Image.open("./college_images/facial-recognition-system-banner.jpeg")
        img2 = img2.resize((600, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1200, y=0, width=600, height=130)

                # bg img
        img3 = Image.open("./college_images/brainai.jpeg")
        img3 = img3.resize((1710, 1050))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1710, height=1050)

        title_lbl=Label(bg_img,text="Attendance Records",font=("verdana",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1710,height="45")

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=75,width= 1680,height=825)

        # left label frame
        left_side_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("verdana",20,"bold"),fg="navyblue",bg="white")
        left_side_frame.place(x=15,y=10,width=820,height=800)
        img_left = Image.open("./college_images/CanvaStudentsbanner.webp")
        img_left = img_left.resize((800, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_side_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=0, width=813, height=110)

        #inside left frame

        left_frame=LabelFrame(left_side_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("verdana",20,"bold"),fg="navyblue",bg="white")
        left_frame.place(x=0,y=135,width=813,height=300)


         #Student id
        studentId_label = Label(left_frame,text="Std-ID:",font=("verdana",18,"bold"),fg="black",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=20,font=("verdana",16,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student Roll
        student_roll_label = Label(left_frame,text="Roll.No:",font=("verdana",18,"bold"),fg="black",bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_roll,width=20,font=("verdana",16,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_frame,text="Std-Name:",font=("verdana",18,"bold"),fg="black",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=20,font=("verdana",16,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(left_frame,text="Time:",font=("verdana",18,"bold"),fg="black",bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=20,font=("verdana",16,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date:",font=("verdana",18,"bold"),fg="black",bg="white")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=20,font=("verdana",16,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("verdana",18,"bold"),fg="black",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=19,font=("verdana",16,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

         #Button Frame
        btn_frame = Frame(left_side_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=5,y=320,width=805,height=110)

        #Import button
        save_btn=Button(btn_frame,text="Import CSV",width=19,command=self.importCsv,font=("verdana",19,"bold"),fg="navyblue",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=22,pady=10,sticky=W)

        #Export button
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=19,font=("verdana",19,"bold"),fg="navyblue",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=22,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,text="Update",width=19,command=self.update_data,font=("verdana",19,"bold"),fg="navyblue",bg="navyblue")
        del_btn.grid(row=1,column=0,padx=22,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",width=19,command=self.reset_data,font=("verdana",19,"bold"),fg="navyblue",bg="navyblue")
        reset_btn.grid(row=1,column=1,padx=22,pady=10,sticky=W)

        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("verdana",20,"bold"),fg="navyblue",bg="white")
        right_frame.place(x=845,y=10,width=820,height=800)


        table_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",20,"bold"),fg="navyblue")
        table_frame.place(x=5,y=5,width=805,height=445)


        # ==========================scroll bar table=========================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReport = ttk.Treeview(table_frame,column=("Student_id","Class","Roll-No","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("Student_id",text="Student_id")
        self.attendanceReport.heading("Roll-No",text="Roll-No")
        self.attendanceReport.heading("Class",text="Class")
        self.attendanceReport.heading("Name",text="Student-Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("Student_id",width=100)
        self.attendanceReport.column("Roll-No",width=100)
        self.attendanceReport.column("Class",width=100)
        self.attendanceReport.column("Name",width=150)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)

        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_left)


# ==============================functions=================================
    def fetchData(self,rows):
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV file","*csv"),( "All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV file","*csv"),( "All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # ========================== cursor for csv=====================
    def get_cursor_left(self,event=""):
            cursor_focus = self.attendanceReport.focus()
            content = self.attendanceReport.item(cursor_focus)
            data = content["values"]

            self.var_id.set(data[0]),
            self.var_roll.set(data[1]),
            self.var_name.set(data[2]),
            self.var_time.set(data[3]),
            self.var_date.set(data[4]),
            self.var_attend.set(data[5])  

    def update_data(self):
        if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="swarnim0129",database="face_recognizer", auth_plugin='mysql_native_password')
                    mycursor = conn.cursor()
                    mycursor.execute("update attendance set std_id=%s,std_roll_no=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
                    self.var_id.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="swarnim0129",database="face_recognizer", auth_plugin='mysql_native_password')
        mycursor = conn.cursor()

        mycursor.execute("select * from attendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()