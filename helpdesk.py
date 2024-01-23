from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import webbrowser

class Helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1710x1050+0+0")
        self.root.title("Help Desk")

        # This part is image labels setting start 
        # first header image  
        # backgorund image 
        bg1=Image.open("college_images/help.jpeg")
        bg1=bg1.resize((1780, 1050))
        self.photobg1=ImageTk.PhotoImage(bg1)
        


        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1780,height=1050)

        title_lb1 = Label(bg_img,text="HelpDesk",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1710,height=45)

        std_img_btn=Image.open("college_images/gmail.webp")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=200,y=240,width=220,height=220)
        std_b1_1 = Button(bg_img,command=self.website,text="swarnimbane1234@gmail.com",cursor="hand2",font=("tahoma",13,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=200, y=450, width=220, height=40)

        # Detect Face  button 2
        det_img_btn=Image.open("college_images/linkedin.jpeg")
        det_img_btn=det_img_btn.resize((245, 245),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.linkedin,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=580,y=240,width=220,height=220)


        det_b1_1 = Button(bg_img,command=self.linkedin,text="LinkedIn",cursor="hand2",font=("tahoma",18,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=580, y=450, width=220, height=40)

         # Attendance System  button 3
        att_img_btn=Image.open("college_images/github.jpeg")
        att_img_btn=att_img_btn.resize((245, 245),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.github,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=960,y=240,width=220,height=220)

        att_b1_1 = Button(bg_img,command=self.github,text="GitHub",cursor="hand2",font=("tahoma",18,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=960, y=450, width=220, height=40)

         # Help  Support  button 4
        hlp_img_btn=Image.open("college_images/insta.webp")
        hlp_img_btn=hlp_img_btn.resize((245, 245),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.insta,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=1340,y=240,width=220,height=220)

        hlp_b1_1 = Button(bg_img,command=self.insta,text="Instagram",cursor="hand2",font=("tahoma",18,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=1340, y=450, width=220, height=40)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = ""
        webbrowser.open(self.url,new=self.new)
    
    def linkedin(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/swarnimbane0129/"
        webbrowser.open(self.url,new=self.new)
    
    def github(self):
        self.new = 1
        self.url = "https://github.com/swarnim0129"
        webbrowser.open(self.url,new=self.new)
    
    def insta(self):
        self.new = 1
        self.url = "https://www.instagram.com/ig_swx3rnim07._/"
        webbrowser.open(self.url,new=self.new)

if __name__ == "__main__":
    root=Tk()
    obj=Helpdesk(root)
    root.mainloop()