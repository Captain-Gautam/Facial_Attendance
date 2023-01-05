from tkinter import*
from tkinter import ttk
from tkinter import Tk
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
from tkinter import messagebox
import mysql.connector
from setuptools import Command




class Train:
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
        title_lable1 = Label(bg_img, text = "TRAIN DATA SET", font = ("cursive", 22, "italic"),bg ='#011f4b', fg = '#f8ae97') #We can give bg also.
        title_lable1.place(x=0, y=0, width = 1360, height = 45)

        #Train Data Button
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font = ("cursive", 18, "italic"),bg ='#011f4b', fg = '#f8ae97')
        b1_1.place(x=10, y= 160, width = 160, height=30)


    #Train function
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        ids = []

        for image in path:
            img = Image.open(image).convert('L')        #Converted in to Gray Scale Image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])   #To have face unique ids --Grid Scale converteds

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

  



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
