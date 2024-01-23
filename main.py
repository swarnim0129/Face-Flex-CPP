from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpdesk import Helpdesk
import subprocess
import platform


class Face_Recognition_System:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1710x1050+0+0")
        self.root.title("face recognition system")

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
        img3 = Image.open("./college_images/backimg.jpg")
        img3 = img3.resize((1710, 1050))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1710, height=1050)

        #white title with red text on background image
        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue");
        title_lbl.place(x=0,y=0,width=1710,height="45")

        # student button
        img4 = Image.open("./college_images/studentInfoButton2.png")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200, y=140, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg='black')
        b1_1.place(x=200, y=350, width=220, height=40)

        # detect face button
        img5 = Image.open("./college_images/men-face.png")
        img5 = img5.resize((245, 245))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command=self.face_detector,cursor="hand2")
        b1.place(x=580, y=140, width=220, height=220)

        b1_1 = Button(bg_img, text="Detect Face", command=self.face_detector,cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue",
                      fg='black')
        b1_1.place(x=580, y=350, width=220, height=40)

        # Attendance button
        img6 = Image.open("./college_images/forbidden.png")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,command=self.attendance_details, cursor="hand2")
        b1.place(x=960, y=140, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_details,font=("times new roman", 20, "bold"), bg="darkblue",
                      fg='black')
        b1_1.place(x=960, y=350, width=220, height=40)

        # help desk button
        img7 = Image.open(
            "./college_images/help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,command=self.help_desk, cursor="hand2")
        b1.place(x=1340, y=140, width=220, height=220)

        b1_1 = Button(bg_img, text="Help-Desk", cursor="hand2", command=self.help_desk,font=("times new roman", 20, "bold"), bg="darkblue",
                      fg='black')
        b1_1.place(x=1340, y=350, width=220, height=40)






        # Train Data Button
        img8 = Image.open("./college_images/face-detect-women.png")
        img8 = img8.resize((310, 250))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, command=self.train_details,cursor="hand2")
        b1.place(x=200, y=480, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data",command=self.train_details, cursor="hand2", font=("times new roman", 20, "bold"),
                      bg="darkblue", fg='black');
        b1_1.place(x=200, y=690, width=220, height=40)

        # Photos Button
        img9 = Image.open("./college_images/photosImg.png")
        img9 = img9.resize((270, 270))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, command=self.open_img,cursor="hand2")
        b1.place(x=580, y=480, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue",
                      fg='black')
        b1_1.place(x=580, y=690, width=220, height=40)

        # Developer Button
        img10 = Image.open("./college_images/DevImg.webp")
        img10 = img10.resize((237, 237))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,  command=self.developer_details,cursor="hand2")
        b1.place(x=960, y=480, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_details,font=("times new roman", 20, "bold"), bg="darkblue",
                      fg='black')
        b1_1.place(x=960, y=690, width=220, height=40)

        # Exit button
        img11= Image.open(
            "./college_images/exitImg.jpeg")
        img11 = img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, command=self.iExit,cursor="hand2")
        b1.place(x=1340, y=480, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit,font=("times new roman", 20, "bold"), bg="darkblue",
                      fg='black')
        b1_1.place(x=1340, y=690, width=220, height=40)






       #===========================function buttons=========================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 

    def train_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_detector(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpdesk(self.new_window)

    


# ================================opening photos from the pc============================
    def open_img(self):
        system = platform.system().lower()
        file_path="data"
        if system == "windows":
          subprocess.Popen(["start", " ", file_path], shell=True)
        elif system == "darwin":
         subprocess.Popen(["open", file_path])
        elif system == "linux":
         subprocess.Popen(["xdg-open", file_path])
        else:
         print("Unsupported operating system")


    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face recognition","Are you sure to exit this project",parent=self.root )
    
       if self.iExit>0:
          self.root.destroy()

       else:
          return
        






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()