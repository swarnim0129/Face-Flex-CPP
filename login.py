from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from main import Face_Recognition_System


def main_log():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1710x1150+0+0")
        self.root.title("Login")

        img3 = Image.open("college_images/employee_img2.jpg")
        img3 = img3.resize((1710, 1150))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1710, height=1050)
            
        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=680,y=200,width=380,height=480)

        img1=Image.open("college_images/LoginIconAppl.png")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=820,y=210, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=160,y=110)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",16,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",16,"bold"))
        self.txtuser.place(x=33,y=190,width=270)

        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",16,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",16,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)

         # Creating Button Login
        loginbtn=Button(frame1,text="Login",font=("times new roman",19,"bold"),command=self.login,bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=80,y=320,width=200,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,text="Register",command=self.reg,font=("times new roman",14,"bold"),bd=0,relief=RIDGE,fg="black",bg="#002B53")
        loginbtn.place(x=33,y=390,width=70,height=25)


        # Creating Button Forget
        loginbtn=Button(frame1,text="Forget",font=("times new roman",14,"bold"),command=self.forget_pwd,bd=0,relief=RIDGE,fg="black",bg="#002B53")
        loginbtn.place(x=110,y=390,width=70,height=25)



        #==========================functions ===========================
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="swarnim0129",database="login_schema",auth_plugin='mysql_native_password')
            mycursor = conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s",(
            self.txtuser.get(),
            self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()



    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.new_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="swarnim0129",database="login_schema",auth_plugin='mysql_native_password')
            mycursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                


    def ret_login(self):
        self.root.destroy()

    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="swarnim0129",database="login_schema",auth_plugin='mysql_native_password')
            mycursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")

            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("380x480+680+240")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.var_sa=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.var_sa.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="black",bg="#002B53")
                loginbtn.place(x=70,y=300,width=270,height=35)
 




if __name__=="__main__":
    main_log()
