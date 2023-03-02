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
import csv
import cv2
import numpy as np
import mysql.connector
from student import Student
from attendance import Attendance


class Face_Recognition_System :
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x688+0+0")
        self.root.title("Face Recognition System")
        #self.root.wm_iconbitmap("face.ico")

        #Logo
        img = Image.open(r"bg_images/ssit_logo2.jpg")
        img = img.resize((140,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        first_label =  Label(self.root, image=self.photoimg)
        first_label.place(x=0,y=0,width=140,height=100)

        #Title Of Institute
        title_lable = Label(text = "SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY", font = ("palatino", 32, "bold"),bg ='#282b30', fg = '#f5f5f5') 
        title_lable.place(x=140, y=0, width = 1220, height = 100)


        #BackGroundImage
        img2 = Image.open(r"bg_images/Technology3.jpg")
        img2 = img2.resize((1360,688),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)


        bg_img =  Label(self.root, image=self.photoimg2)
        bg_img.place(x=0,y=100,width=1360,height=600)

        
        #Title Of Project
        title_lable1 = Label(bg_img, text = "FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font = ("comicsansns", 22, "italic"),bg ='#011f4b', fg = '#f8ae97') #We can give bg also.
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


        b1_1 = Button(bg_img, text="Student Detail", command=self.student_details,cursor="hand2", font = ("comicsansns", 13, "italic"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97')
        b1_1.place(x=235, y= 240, width = 140, height=30)



        #Detect Face Button
        img4 = Image.open(r"bg_images/Face.jpg")
        img4 = img4.resize((140,140),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)


        b2 = Button(bg_img, image = self.photoimg4, command=self.face_recog, cursor="hand2")
        b2.place(x=585, y= 100, width = 140, height=140)


        b2_2 = Button(bg_img, text="Face Detector", command=self.face_recog, cursor="hand2", font = ("comicsansns", 13, "italic"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97')
        b2_2.place(x=585, y= 240, width = 140, height=30)

       
       
        #Attendance Button
        img5 = Image.open(r"bg_images/Attendance.jpg")
        img5 = img5.resize((140,140),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)


        b3 = Button(bg_img, image = self.photoimg5, cursor="hand2", command=self.attendace_data)
        b3.place(x=935, y= 100, width = 140, height=140)


        b3_3 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendace_data, font = ("comicsansns", 13, "italic"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97')
        b3_3.place(x=935, y= 240, width = 140, height=30)


        #Train Button
        img6 = Image.open(r"bg_images/Face1.jpg")
        img6 = img6.resize((140,140),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)


        b4 = Button(bg_img, image = self.photoimg6, cursor="hand2", command=self.train_classifier)
        b4.place(x=235, y= 350, width = 140, height=140)


        b4_4 = Button(bg_img, text="Train Data", command=self.train_classifier, cursor="hand2", font = ("comicsansns", 13, "italic"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97')
        b4_4.place(x=235, y= 490, width = 140, height=30)



        
        #Photo Data Button
        img7 = Image.open(r"bg_images/Photo_Collection.jpg")
        img7 = img7.resize((140,140),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)


        b5 = Button(bg_img, image = self.photoimg7, cursor="hand2", command=self.open_img)
        b5.place(x=585, y= 350, width = 140, height=140)


        b5_5 = Button(bg_img, text="Photo Data", cursor="hand2", command =self.open_img, font = ("comicsansns", 13, "italic"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97')
        b5_5.place(x=585, y= 490, width = 140, height=30)



        #Exit Button
        img8 = Image.open(r"bg_images/Exit1.jpg")
        img8 = img8.resize((140,140),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)


        b6 = Button(bg_img, image = self.photoimg8, cursor="hand2", command=self.exit)
        b6.place(x=935, y= 350, width = 140, height=140)


        b6_6 = Button(bg_img, text="Exit", cursor="hand2", command=self.exit, font = ("comicsansns", 13, "italic"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97')
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


    def attendace_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


#=====================================Train Data================================================
 #Train function
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        ids = []

        for image in path:
            img = Image.open(image).convert('L')        #Converted in to Gray Scale Image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1]) # 1 #To have face unique ids --Grid Scale converteds
            #id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training Images", imageNp)
            cv2.waitKey(1) == 13
        
        ids = np.array(ids)

        #========Train the classifier and Save========
        clf =  cv2.face.LBPHFaceRecognizer_create()
        #clf = cv2.face.createLBPHFaceRecognizer()

        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data Set is Completed")

 #====================================Face Detector=============================================
    
    #===========Attendance CSV File================
    
    def mark_attendance(self, i, e, n, d):
        
        folder_name = "Attendance"
        filename = os.path.join(folder_name, datetime.now().strftime("%d-%m-%Y") + "_Attendance.csv")
       
        file_exists = os.path.isfile(filename)
        with open(filename, "a", newline="\n") as f:
            fieldnames = ['ID', 'Enroll_No', 'Name', 'Department', 'Time', 'Date', 'Status']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            # Write header row if the file doesn't exist yet
            if not file_exists:
                writer.writeheader()

            # Check if the entry already exists in the file
            entries = []
            with open(filename, "r", newline="\n") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    entries.append(row)

            exists = False
            for entry in entries:
                if entry['ID'] == i:
                    exists = True
                    break

            # Write new entry if it doesn't exist yet
            if not exists:
                now = datetime.now()
                dt_string = now.strftime("%H:%M:%S")
                d1 = now.strftime("%d/%m/%Y")
                writer.writerow({
                    'ID': i,
                    'Enroll_No': e,
                    'Name': n,
                    'Department': d,
                    'Time': dt_string,
                    'Date': d1,
                    'Status': 'Present'
                })

    # def mark_attendance(self, i, e, n, d):
    #     if not os.path.exists('Attendance'):
    #         os.makedirs('Attendance')
    #     os.chdir('Attendance')
        
    #     filename = datetime.now().strftime("%d-%m-%Y") + "_Attendance.csv"
    #     file_exists = os.path.isfile(filename)
    #     with open(filename, "a", newline="\n") as f:
    #         fieldnames = ['ID', 'Enroll_No', 'Name', 'Department', 'Time', 'Date', 'Status']
    #         writer = csv.DictWriter(f, fieldnames=fieldnames)
    #         # Write header row if file doesn't exist
    #         if not file_exists:
    #             writer.writeheader()
            
    #         # Write data to file
    #         writer.writerow({
    #             'ID': i,
    #             'Enroll_No': e,
    #             'Name': n,
    #             'Department': d,
    #             'Time': datetime.now().strftime("%H:%M:%S"),
    #             'Date': datetime.now().strftime("%d/%m/%Y"),
    #             'Status': 'Present'
    #         })
         

    #==========Face Recognition Function=========
    def face_recog(self):
        
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf): 
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)


            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                #id, predict = clf.predict(gray_image[int(y):int(y+h), int(x):int(x+w)])
                #id = str(id)

                confidence = int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root", password="gautam", database="face_recognizer_1")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Student_Name FROM student where Student_Id="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("SELECT Enroll_No FROM student where Student_Id="+str(id)) #  my_cursor.execute("select Enroll_No from student where Enroll_No=%s"+str(id))
                e = my_cursor.fetchone()
                e="+".join(e)

                my_cursor.execute("SELECT Dep FROM student where Student_Id="+str(id))
                d = my_cursor.fetchone()
                d="+".join(d)
                
                
                my_cursor.execute("SELECT Student_id FROM student where Student_Id="+str(id))
                i = my_cursor.fetchone()
                i="+".join(i)

   

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Student_Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Enroll_No:{e}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, e, n, d)
                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)
               
                    cv2.putText(img, "Unknown_Face ", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                #coord[x,y,w,h] #h
                coord.append((x,y,w,h))
                conn.close()

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)  #draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img


        #faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Weolcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

   





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


# Download necessory
#python. pip, pillow, opencv, dlib, numpy, face-recogniton, mysql-connector
