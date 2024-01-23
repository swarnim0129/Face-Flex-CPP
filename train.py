
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import numpy as np
from tkinter import messagebox
import os
import cv2


class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1710x1150+0+0")
        self.root.title("Training Panel")

        

        title_lb1 = Label(self.root,text="Welcome to Training Window",font=("verdana",38,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1710,height=58)

        img3 = Image.open("./college_images/grid-AI.webp")
        img3 = img3.resize((1710, 1050))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=58, width=1710, height=1050)

        b1_1 = Button(bg_img, text="Train Images",cursor="hand2", command=self.train_classifier,font=("veranda", 45, "bold"), bg="white",
                      fg='black')
        b1_1.place(x=660, y=400,width=420, height=62)


    def train_classifier(self):
        data_dir=("data")
        # path=[os.path.join(data_dir,file)  for file in os.listdir(data_dir)]
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])  #os.path.split splits whole path into two parts i.e path to the image and image name, then it seperates the image name into different parts where '.' is present and takes away the id

            faces.append(imageNp)       #adds into faces array
            ids.append(id)              #adds into ids array
            cv2.imshow('Training',imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)


        # =================================train the classifier===========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clifi.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!",parent=self.root)



        


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()