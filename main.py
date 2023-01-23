from base64 import b64decode
from cgitb import text
from logging import root
from tkinter import*
from tkinter import ttk
from tkinter import Tk
import tkinter
from tkinter import messagebox
from tkinter import font
from datetime import datetime
from time import strftime
from PIL import Image, ImageTk
import subprocess, sys
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System :
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x688+0+0")
        self.root.title("Face Recognition System")

        #Logo
        img = Image.open(r"bg_images/ssit_logo2.jpg")
        img = img.resize((180,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        first_label =  Label(self.root, image=self.photoimg)
        first_label.place(x=0,y=0,width=180,height=100)

        #Title Of Institute
        title_lable = Label(text = "SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY", font = ("palatino", 30, "bold"),bg ='#282b30', fg = '#f5f5f5') 
        title_lable.place(x=180, y=0, width = 1180, height = 100)


        #BackGroundImage
        img2 = Image.open(r"bg_images/Technology3.jpg")
        img2 = img2.resize((1360,688),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)


        bg_img =  Label(self.root, image=self.photoimg2)
        bg_img.place(x=0,y=100,width=1360,height=600)

        
        #Title Of Project
        title_lable1 = Label(bg_img, text = "FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font = ("cursive", 22, "italic"),bg ='#011f4b', fg = '#f8ae97') #We can give bg also.
        title_lable1.place(x=0, y=0, width = 1360, height = 45)
        
       
        #===========Time==============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl = Label(self.root, font = ("comicsansns", 16, "italic"),bg ='#011f4b', fg = '#f8ae97')
        lbl.place(x=2, y=148, width=150, height=50)
        time()

        
        #Student Button
        img3 = Image.open(r"bg_images/student_detail.jpg")
        img3 = img3.resize((140,140),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)


        b1 = Button(bg_img, image = self.photoimg3, command=self.student_details,cursor="hand2")
        b1.place(x=235, y= 100, width = 140, height=140)


        b1_1 = Button(bg_img, text="Student Detail", command=self.student_details,cursor="hand2", font = ("cursive", 14, "italic"),bg ='#011f4b', fg = '#f8ae97')
        b1_1.place(x=235, y= 240, width = 140, height=30)



        #Detect Face Button
        img4 = Image.open(r"bg_images/Face.jpg")
        img4 = img4.resize((140,140),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)


        b2 = Button(bg_img, image = self.photoimg4, command=self.face_recogniton, cursor="hand2")
        b2.place(x=585, y= 100, width = 140, height=140)


        b2_2 = Button(bg_img, text="Face Detector", command=self.face_recogniton, cursor="hand2", font = ("cursive", 14, "italic"),bg ='#011f4b', fg = '#f8ae97')
        b2_2.place(x=585, y= 240, width = 140, height=30)

       
       
        #Attendance Button
        img5 = Image.open(r"bg_images/Attendance.jpg")
        img5 = img5.resize((140,140),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)


        b3 = Button(bg_img, image = self.photoimg5, cursor="hand2", command=self.attendace_data)
        b3.place(x=935, y= 100, width = 140, height=140)


        b3_3 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendace_data, font = ("cursive", 14, "italic"),bg ='#011f4b', fg = '#f8ae97')
        b3_3.place(x=935, y= 240, width = 140, height=30)


        #Train Button
        img6 = Image.open(r"bg_images/Face1.jpg")
        img6 = img6.resize((140,140),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)


        b4 = Button(bg_img, image = self.photoimg6, cursor="hand2", command=self.train_data)
        b4.place(x=235, y= 350, width = 140, height=140)


        b4_4 = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font = ("cursive", 14, "italic"),bg ='#011f4b', fg = '#f8ae97')
        b4_4.place(x=235, y= 490, width = 140, height=30)



        
        #Photo Data Button
        img7 = Image.open(r"bg_images/Photo_Collection.jpg")
        img7 = img7.resize((140,140),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)


        b5 = Button(bg_img, image = self.photoimg7, cursor="hand2", command=self.open_img)
        b5.place(x=585, y= 350, width = 140, height=140)


        b5_5 = Button(bg_img, text="Photo Data", cursor="hand2", command =self.open_img, font = ("cursive", 14, "italic"),bg ='#011f4b', fg = '#f8ae97')
        b5_5.place(x=585, y= 490, width = 140, height=30)



        #Exit Button
        img8 = Image.open(r"bg_images/Exit1.jpg")
        img8 = img8.resize((140,140),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)


        b6 = Button(bg_img, image = self.photoimg8, cursor="hand2", command=self.exit)
        b6.place(x=935, y= 350, width = 140, height=140)


        b6_6 = Button(bg_img, text="Exit", cursor="hand2", command=self.exit, font = ("cursive", 14, "italic"),bg ='#011f4b', fg = '#f8ae97')
        b6_6.place(x=935, y= 490, width = 140, height=30)

    #=====To open the Photo Data button==========
    def open_img(self):
        
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, "data"])
        #os.startfile("data")   #startfile
        
    #======Exit Menu===========
    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Exit", "Are sure you want to Exit?", parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    #========Function Buttons=========
 
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recogniton(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def attendace_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


# Download necessory
#python. pip, pillow, opencv, dlib, numpy, face-recogniton, mysql-connector
