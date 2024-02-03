from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import webbrowser

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1710x1050+0+0")
        self.root.title("Face_Recogonition_System")

        # This part is image labels setting start 
        # first header image  
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


        # backgorund image 
        bg1=Image.open("college_images/bluegrad.png")
        bg1=bg1.resize((1780, 1050))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1780,height=1050)


        #title section
        title_lb1 = Label(bg_img,text="Developer",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1710,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1 Swarnim Bane
        std_img_btn=Image.open("college_images/swarnim.jpg")
        std_img_btn=std_img_btn.resize((210, 210 ))
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.linkedin1,image=self.std_img1,cursor="hand2")
        std_b1.place(x=200,y=240,width=220,height=220)

        std_b1_1 = Button(bg_img,text="Swarnim Bane",command=self.linkedin1,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=200, y=450, width=220, height=40)

        # Harsh Tandel
        det_img_btn=Image.open("college_images/Harsh.png")
        det_img_btn=det_img_btn.resize((245, 230))
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.linkedin2,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=580,y=240,width=220,height=220)

        det_b1_1 = Button(bg_img,command=self.linkedin2,text="Harsh Tandel",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=580, y=450, width=220, height=40)


         # Attendance System  button 3
        att_img_btn=Image.open("college_images/atharva.jpeg")
        att_img_btn=att_img_btn.resize((230, 230))
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=960,y=240,width=220,height=220)

        att_b1_1 = Button(bg_img,text="Atharva Sankhe",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=960, y=450, width=220, height=40)


         # Help  Support  button 4
        hlp_img_btn=Image.open("college_images/vedant.jpeg")
        hlp_img_btn=hlp_img_btn.resize((215, 260))
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,command=self.linkedin3,cursor="hand2",)
        hlp_b1.place(x=1340,y=240,width=220,height=220)

        hlp_b1_1 = Button(bg_img,text="Vedant Raut",command=self.linkedin3,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=1340, y=450, width=220, height=40)


    def linkedin1(self):
            self.new = 1
            self.url = "https://www.linkedin.com/in/swarnimbane0129/"
            webbrowser.open(self.url,new=self.new)

    def linkedin2(self):
            self.new = 1
            self.url = "https://www.linkedin.com/in/harsh-tandel-25795229a/"
            webbrowser.open(self.url,new=self.new
                            )
    def linkedin3(self):
            self.new = 1
            self.url = "https://www.linkedin.com/in/vedant-raut-062b9b2a6/"
            webbrowser.open(self.url,new=self.new)

   
    

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
