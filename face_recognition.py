from tkinter import*
from tkinter import ttk
from tkinter import Tk
from PIL import Image, ImageTk
import os
import numpy as np
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from setuptools import Command
import csv
import cv2
#import tensorflow as tf
from train import Train
from student import Student


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x688+0+0")
        self.root.title("Face Recognition System")


        #Logo
        img = Image.open(r"bg_images/topic.png")
        img = img.resize((1360,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        first_label =  Label(self.root, image=self.photoimg)
        first_label.place(x=0,y=0,width=1360,height=100)
        
             
        #Title Of Institute
        #title_lable = Label(text = "SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY", font = ("palatino", 30, "bold"),bg ='#282b30', fg = '#f5f5f5') 
        #title_lable.place(x=180, y=0, width = 1180, height = 100)

        #BackGroundImage
        img2 = Image.open(r"bg_images/Technology3.jpg")
        img2 = img2.resize((1360,688),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img =  Label(self.root, image=self.photoimg2)
        bg_img.place(x=0,y=100,width=1360,height=600)


        #Title Of Project
        title_lable1 = Label(bg_img, text = "Face Detector", font = ("comicsansns", 28, "italic"),bg ='#011f4b', fg = '#f8ae97') #We can give bg also.
        title_lable1.place(x=0, y=0, width = 1360, height = 45)


        #Face Detector Data Button
        b1_1 = Button(self.root, text="Face Recogniton", command=self.face_recog, cursor="hand2", font = ("comicsansns", 18, "italic"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97')
        b1_1.place(x=10, y= 160, width = 200, height=50)

    #===========Attendance CSV File================
    
    def mark_attendance(self, i, e, n, d):
        filename = datetime.now().strftime("%d-%m-%Y") + "_Attendance.csv"
        file_exists = os.path.isfile(filename)
        
        # Keep track of the last ID added to the file
        last_id = None
        
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
                
                # Add an empty row if the new ID is not consecutive to the last one
                if last_id is not None and int(i) != last_id + 1:
                    writer.writerow({})
                
                writer.writerow({
                    'ID': i,
                    'Enroll_No': e,
                    'Name': n,
                    'Department': d,
                    'Time': dt_string,
                    'Date': d1,
                    'Status': 'Present'
                })
                
                last_id = int(i)

         

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
    obj = Face_Recognition(root)
    root.mainloop()
