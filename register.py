from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 


class Register:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1710x1150+0+0")
        self.root.title("Register")

        # ==============variables==================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        img3 = Image.open("college_images/u.jpg")
        img3 = img3.resize((1710, 1150))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1710, height=1050)


        frame= Frame(self.root,bg="#F2F2F2",border=3)
        frame.place(x=405,y=200,width=900,height=580)

        get_str = Label(frame,text="Registration",font=("times new roman",36,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=50)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=120)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",18,"bold"))
        self.txtuser.place(x=103,y=145,width=270)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=190)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",18,"bold"))
        self.txtpwd.place(x=103,y=215,width=270)

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=120)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",18,"bold"))
        self.txtuser.place(x=533,y=145,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=190)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",18,"bold"))
        self.txtpwd.place(x=533,y=215,width=270)

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=100,y=270)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",18,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=295,width=270)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=100,y=340)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",18,"bold"))
        self.txtpwd.place(x=103,y=365,width=270)

         #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=270)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",18,"bold"))
        self.txtuser.place(x=533,y=295,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=340)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",18,"bold"))
        self.txtpwd.place(x=533,y=365,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,text="I Agree the Terms & Conditions",variable=self.var_check,font=("times new roman",18,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=415,width=270)


        # Creating Button Register
       

        loginbtn=Button(frame,text="Register",command=self.register_data,font=("times new roman",18,"bold"),relief=RIDGE,fg="black")
        loginbtn.place(x=103,y=470,width=270,height=35)

        # Creating Button Login
        
        loginbtn=Button(frame,text="Login",font=("times new roman",18,"bold"),command=self.ret_login,relief=RIDGE,fg="black")
        loginbtn.place(x=533,y=470,width=270,height=35)  


    def ret_login(self):
        self.root.destroy()

    # ======================function decaration===================
    def register_data(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            try:
            # messagebox.showinfo("Successfully","Successfully Register!")
                conn=mysql.connector.connect(host="localhost",user="root",password="swarnim0129",database="login_schema",auth_plugin='mysql_native_password')
                mycursor = conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_cnum.get(),
                    self.var_email.get(),
                    self.var_ssq.get(),
                    self.var_sa.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
