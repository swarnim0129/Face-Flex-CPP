from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import numpy as np
from tkinter import messagebox
import os
import mysql.connector
import cv2
from time import strftime
from datetime import datetime


class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1710x1150+0+0")
        self.root.title("Training Panel")

        title_lb1 = Label(self.root,text="Face Recognition",font=("verdana",38,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1710,height=58)

        img3 = Image.open("./college_images/frec.png")
        img3 = img3.resize((1710, 1050))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=58, width=1710, height=1010)

        b1_1 = Button(bg_img, text="Detect Face",cursor="hand2", command=self.face_recog,font=("veranda", 45, "bold"), bg="grey",
                      fg='darkblue')
        b1_1.place(x=660, y=750,width=390, height=50)


# ===============================attendance======================
        
    def mark_attendance(self,i,r,n,c):
        key = cv2.waitKey(1)
        if key== ord("m"):

            with open("Attendance.csv","r+",newline="\n")as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split(",")
                    name_list.append(entry[0])
                if((i not in name_list)and ( r not in name_list) and (n not in name_list) and (c not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{c},{r},{n},{dtString},{d1},Present")
                    



        # ========================recognition====================


        

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="swarnim0129", database="face_recognizer", auth_plugin='mysql_native_password')
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_id="+str(id))
                n_result = cursor.fetchone()
                n = n_result[0] if n_result is not None else "Unknown"

                cursor.execute("select Roll from student where Student_id="+str(id))
                r_result = cursor.fetchone()
                r = r_result[0] if r_result is not None else "Unknown"

                cursor.execute("select Student_id from student where Student_id="+str(id))
                i_result = cursor.fetchone()
                i = i_result[0] if i_result is not None else "Unknown"

                cursor.execute("select Class from student where Student_id="+str(id))
                c_result = cursor.fetchone()
                c = c_result[0] if c_result is not None else "Unknown"


                if confidence > 77:
                    cv2.putText(img,f"Student_id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,r,n,c)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
        
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clifi.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
