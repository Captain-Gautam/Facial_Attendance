from tkinter import*
from tkinter import ttk
from tkinter import Tk
from PIL import Image, ImageTk
import os
import numpy as np
from tkinter import messagebox
import mysql.connector
from setuptools import Command
import cv2
import tensorflow as tf
from train import Train


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
        title_lable1 = Label(bg_img, text = "Face Detector", font = ("cursive", 28, "italic"),bg ='#011f4b', fg = '#f8ae97') #We can give bg also.
        title_lable1.place(x=0, y=0, width = 1360, height = 45)


        #Face Detector Data Button
        b1_1 = Button(self.root, text="Face Recogniton", command=self.face_recog, cursor="hand2", font = ("cursive", 18, "italic"),bg ='#011f4b', fg = '#f8ae97')
        b1_1.place(x=10, y= 160, width = 200, height=50)

    
    #Face Recognition Function=========
    def face_recog(self):
        
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):   #scalefactor, miniNeighbours, color, text, clf
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiscale(gray_image, scaleFactor, minNeighbours, clf)


            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root", password="gautam", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Student_Name from student where Enroll_No=" +str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Enroll_No from student where Enroll_No=" +str(id))
                e = my_cursor.fetchone()
                e= "+".join(e)

                my_cursor.execute("select Dep from student where Enroll_No=" +str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

   

                if confidence > 77:
                    cv2.putText(img, f"Enroll_No:{e}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Student_Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)
               
                    cv2.putText(img, "Unknown Face ", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord[x,y,w,h]
            
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)  #draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img


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
