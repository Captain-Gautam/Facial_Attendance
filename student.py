from ast import Delete
from base64 import b64decode
from cgitb import text
import os
from logging import exception, root
from os import stat
from tkinter import*
from tkinter import ttk
from tkinter import Tk
from tkinter import font
from tkinter.tix import INTEGER
from tokenize import String
from turtle import heading, update, width
from tkcalendar import  DateEntry
from tkinter import filedialog
#from typing_extensions import self
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from setuptools import Command
import cv2
import csv


class Student :
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x688+0+0")
        self.root.title("Face Recognition System")


        
        #===========variable=================
        self.var_Dep = StringVar()
        self.var_BatchYear = StringVar()
        self.var_Year = StringVar()
        self.var_Sem = StringVar()
        self.va_std_id = StringVar()
        self.var_EnrollNo = StringVar()
        self.var_Name = StringVar()
        self.var_Div = StringVar()
        self.var_Gender = StringVar()
        self.var_DOB = StringVar()
        self.var_Email = StringVar()
        self.var_Phone = StringVar()
        self.var_Address = StringVar()
        self.var_PhotoSample = StringVar()
        self.var_search = StringVar()
        self.var_search_combo = StringVar()
        self.var_radio1 = StringVar()



        #Logo
        img = Image.open(r"bg_images/topic_1.png")
        img = img.resize((1360,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        first_label =  Label(self.root, image=self.photoimg)
        first_label.place(x=0,y=0,width=1360,height=100)

        #Title Of Institute
        #title_lable = Label(text = "SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY", font = ("palatino", 30, "bold"),bg ='#282b30', fg = '#f5f5f5') 
        #title_lable.place(x=180, y=0, width = 1180, height = 100)
        
        
       
        #BackGroundImage
        img2 = Image.open(r"bg_images/Technology2.jpg")
        img2 = img2.resize((1360,688),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)


        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0,y=100,width=1360,height=600)

        
        #Title Of Project
        title_lable1 = Label(bg_img, text = "STUDENT MANAGEMENT SYSTEM", font = ("comicsansns", 22, "italic"), bg ='#011f4b', fg = '#f8ae97') #We can give bg and fg
        title_lable1.place(x=0, y=0, width = 1360, height = 45)

        
        #Frame
        main_frame = Frame(bg_img, bd=2, bg = "white")
        main_frame.place(x=10, y=50, width=1340, height=545)


        #Left Label Frame
        Left_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Student Details",  font = ("comicsansns", 14, "bold"))
        Left_frame.place(x=5, y=5, width=655, height= 515)

       
        #Current Course Information
        Current_Course_frame = LabelFrame(Left_frame, bd=3, bg="white", relief=RIDGE, text="Current Course Information",  font = ("comicsansns", 12, "bold"))
        Current_Course_frame.place(x=5, y=5, width=638, height= 115)

        #Department
        dep_label = Label(Current_Course_frame, text="Department", font = ("comicsansns", 11), bg ="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_Dep, font = ("comicsansns", 10, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Engg.", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Batch-Year 
        Batch_Year_label = Label(Current_Course_frame, text="Batch-Year", font = ("comicsansns", 11), bg ="white")
        Batch_Year_label.grid(row=0, column=2, padx=10, sticky=W)

        batch_year_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_BatchYear, font = ("comicsansns", 10, "bold"), width=17, state="readonly")
        batch_year_combo["values"] = ("Select Batch-Year", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026")
        batch_year_combo.current(0)
        batch_year_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Year
        year_label = Label(Current_Course_frame, text="Year", font = ("comicsansns", 11), bg ="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_Year, font = ("comicsansns", 10, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year","2022-23","2023-24", "2024-25","2025-26") 
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)


        #Semester
        semester_label = Label(Current_Course_frame, text="Semester", font = ("comicsansns", 11), bg ="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_Sem, font = ("comicsansns", 10, "bold"), width=17, state="readonly")
        semester_combo["values"] = ("Select Semester","Semester-1","Semester-2","Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8") 
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        #Class_Student Information
        Class_Student_frame = LabelFrame(Left_frame, bd=3, bg="white", relief=RIDGE, text="Class Student Information",  font = ("comicsansns", 12, "bold"))
        Class_Student_frame.place(x=5, y=120, width=638, height=370)

        #Student ID
        studentId_label = Label(Class_Student_frame, text="Student ID:", font = ("comicsansns", 11), bg ="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        studentid_entry = ttk.Entry(Class_Student_frame, width=16, textvariable=self.va_std_id, font = ("comicsansns", 10, "bold"))
        studentid_entry.grid(row=0, column=1, padx=0, sticky=W)
        
        # #Export Detail
        # export_btn =Button(Class_Student_frame, text="Export Details", command=self.export_data,  width=12, height=1, font = ("comicsansns", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97' )
        # export_btn.grid(row=0, column=2, padx=0, pady=1)

        
        #Enrollment Number
        Enrollment_No_label = Label(Class_Student_frame, text="Enrollment No:", font = ("comicsansns", 11), bg ="white")
        Enrollment_No_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        enrollmentid = ttk.Entry(Class_Student_frame, width=16, textvariable=self.var_EnrollNo, font = ("comicsansns", 10, "bold"))
        enrollmentid.grid(row=1, column=1, padx=0, sticky=W)

        
        #Student_Name
        Student_Name_label = Label(Class_Student_frame, text="Student Name:", font = ("comicsansns", 11), bg ="white")
        Student_Name_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)

        student_name = ttk.Entry(Class_Student_frame, width=16, textvariable=self.var_Name, font = ("comicsansns", 10, "bold"))
        student_name.grid(row=1, column=3, padx=0, sticky=W)

        
        
        #Division_Name
        Division_label = Label(Class_Student_frame, text="Division:", font = ("comicsansns", 11), bg ="white")
        Division_label.grid(row=2, column=0, padx=5, sticky=W)

        division_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_Div, font = ("comicsansns", 10, "bold"), width=15, state="readonly")
        division_combo["values"] = ("Select Division","A", "B", "C", "D") 
        division_combo.current(0)
        division_combo.grid(row=2, column=1, padx=0, pady=10, sticky=W)

        #Gender
        Gender_label = Label(Class_Student_frame, text="Gender:", font = ("comicsansns", 11), bg ="white")
        Gender_label.grid(row=2, column=2, padx=5, sticky=W)

        gender_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_Gender, font = ("comicsansns", 10, "bold"), width=15, state="readonly")
        gender_combo["values"] = ("Select Gender","Male", "Female", "Others") 
        gender_combo.current(0)
        gender_combo.grid(row=2, column=3, padx=0, pady=10, sticky=W)


        #DOB
        DOB_label = Label(Class_Student_frame, text="DOB:", font = ("comicsansns", 11), bg ="white")
        DOB_label.grid(row=3, column=0, padx=5, pady=10, sticky=W)

        dob_name = DateEntry(Class_Student_frame, width=15, textvariable=self.var_DOB, font = ("comicsansns", 10, "bold"), date_pattern='dd/mm/yyyy')
        dob_name.grid(row=3, column=1, padx=0, sticky=W)

        
        #Email 
        Email_label = Label(Class_Student_frame, text="Email:", font = ("comicsansns", 11), bg ="white")
        Email_label.grid(row=3, column=2, padx=5, pady=10, sticky=W)

        email_name = ttk.Entry(Class_Student_frame, width=16,textvariable=self.var_Email, font = ("comicsansns", 10, "bold"))
        email_name.grid(row=3, column=3, padx=0, sticky=W)


        #Phone Nmber
        Phoneno_label = Label(Class_Student_frame, text="Phone No:", font = ("comicsansns", 11), bg ="white")
        Phoneno_label.grid(row=4, column=0, padx=5, pady=10, sticky=W)

        phoneno_name = ttk.Entry(Class_Student_frame, width=16,textvariable=self.var_Phone, font = ("comicsansns", 10, "bold"))
        phoneno_name.grid(row=4, column=1, padx=0, sticky=W)


        #Address
        Address_label = Label(Class_Student_frame, text="Address:", font = ("comicsansns", 11), bg ="white")
        Address_label.grid(row=4, column=2, padx=5, pady=4, sticky=W)

        address_name = ttk.Entry(Class_Student_frame, width=16,textvariable=self.var_Address, font = ("comicsansns", 10, "bold"))
        address_name.grid(row=4, column=3, padx=0, sticky=W)


        #Radio Button For Taking Photos or not.
        self.var_PhotoSample = StringVar()
        radiobutton1 = Radiobutton(Class_Student_frame, variable=self.var_PhotoSample, text="Take Photo Sample", value="Yes")
        radiobutton1.grid(row=5, column=0, padx=5, pady=5)

        #Radio Button For Taking Photos or not.
        #self.var_radio2 = StringVar()
        radiobutton2 = Radiobutton(Class_Student_frame, variable=self.var_PhotoSample, text="No Photo Sample", value="No")
        radiobutton2.grid(row=5, column=2, padx=5, pady=5)


        #---------Button Frame----------------
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="black")
        btn_frame.place(x=5, y=245, width=620, height=100)

        #Save Button
        save_btn =Button(btn_frame, text="Save", command=self.add_data, width=9, height=1, font = ("comicsansns", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97' )
        save_btn.grid(row=0, column=0, padx=4, pady=1)

        #Update Button
        update_btn =Button(btn_frame, text="Update", command=self.update_data, width=9, height=1, font = ("comicsansns", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97' )
        update_btn.grid(row=0, column=1, padx=4, pady=1)

        #Delete Button
        delete_btn =Button(btn_frame, text="Delete", width=9, command=self.delete_data, height=1, font = ("comicsansns", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97' )
        delete_btn.grid(row=0, column=2, padx=4, pady=1)

        #Reset Button
        reset_btn =Button(btn_frame, text="Reset", command=self.reset_data,  width=9, height=1, font = ("comicsansns", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97' )
        reset_btn.grid(row=0, column=3, padx=4, pady=1)

        #Button_Photo Frame 
        btn_frame1 = Frame(btn_frame, bd=2, relief=RIDGE, bg="black")
        btn_frame1.place(x=2, y=40, width=610, height=65)


        #Take Photo Sample Button
        take_photo_sample_btn =Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample",  width=21, height=2, font = ("comicsansns", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97' )
        take_photo_sample_btn.grid(row=1, column=0, pady=1)


        #Update Photo Sample Button ///// Export Detail
        update_photo_sample_btn =Button(btn_frame1, text="Export Detail", command=self.export_data, width=21, height=2, font = ("comicsansns", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97' )
        update_photo_sample_btn.grid(row=1, column=1, padx=2)





        #Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Student Details",  font = ("comicsansns", 14, "bold"))
        Right_frame.place(x=670, y=5, width=655, height= 515)


        #========Search System==========

        #View Student Detail And Search it.
        Search_frame = LabelFrame(Right_frame, bd=3, bg="white", relief=RIDGE, text="Search System",  font = ("comicsansns", 11, "bold"))
        Search_frame.place(x=5, y=3, width=638, height=70)


        # Search Label
        Search_label = Label(Search_frame, text="Search By:", font = ("comicsansns", 13), bg ="red", fg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=4, sticky=W)


        search_combo = ttk.Combobox(Search_frame, textvariable=self.var_search_combo, font = ("comicsansns", 10, "bold"), width=14, state="readonly")
        search_combo["values"] = ("Select", "Department", "Semester", "Student_ID", "Enrollment No", "Phone No", "Email") 
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        Search_Entry = ttk.Entry(Search_frame, textvariable=self.var_search, font = ("comicsansns", 13, "bold"))
        Search_Entry.grid(row=0, column=2, padx=10, pady=4, sticky=W)


        #Search Button
        Search_btn =Button(Search_frame, text="Search", width=6, command=self.search_student, font = ("comicsansns", 10, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground = '#011f4b', activeforeground = '#f8ae97' )
        Search_btn.grid(row=0, column=3, padx=0, pady=1)
        

        #Show All Button
        Show_All_btn =Button(Search_frame, text="Show All", width=7, font = ("comicsansns", 10, "bold"),bg ='#011f4b', fg = '#f8ae97' )
        Show_All_btn.grid(row=0, column=4, padx=10, pady=1)

        #Tabel Label Frame
        Table_frame = LabelFrame(Right_frame, bd=3, bg="white", relief=RIDGE)
        Table_frame.place(x=5, y=80, width=638, height= 405)

        #Scroll Bar
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        
        self.student_tabel = ttk.Treeview(Table_frame, column=("Student_Id", "EnrollNo", "Name", "Sem",  "Dep", "BatchYear", "Year",   "Div", "Gender", "DOB", "Email", "Phone", "Address", "PhotoSample" ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)


        #Headings OF the Tabel Frame
        self.student_tabel.heading("Student_Id", text="S_ID")
        self.student_tabel.heading("EnrollNo", text="Enrollment No")
        self.student_tabel.heading("Name", text="Name")
        self.student_tabel.heading("Sem", text="Semester")
        self.student_tabel.heading("Dep", text="Department")
        self.student_tabel.heading("BatchYear", text="Batch-Year")
        self.student_tabel.heading("Year", text="Year")
        self.student_tabel.heading("Div", text="Div")
        self.student_tabel.heading("Gender", text="Gender")
        self.student_tabel.heading("DOB", text="DOB")
        self.student_tabel.heading("Email", text="Email")
        self.student_tabel.heading("Phone", text="Phone No")
        self.student_tabel.heading("Address", text="Address")
        self.student_tabel.heading("PhotoSample", text="Photo Status")
        
        self.student_tabel["show"] = "headings"
        
        self.student_tabel.column("Student_Id", width=40)
        self.student_tabel.column("EnrollNo", width=120)
        self.student_tabel.column("Name", width=150)
        self.student_tabel.column("Sem", width=100)   
        self.student_tabel.column("Dep", width=100)
        self.student_tabel.column("BatchYear", width=100)
        self.student_tabel.column("Year", width=100)
        self.student_tabel.column("Div", width=50)
        self.student_tabel.column("Gender", width=100)
        self.student_tabel.column("DOB", width=100)
        self.student_tabel.column("Email", width=150)
        self.student_tabel.column("Phone", width=100)
        self.student_tabel.column("Address", width=100)
        self.student_tabel.column("PhotoSample", width=100)


        self.student_tabel.pack(fill=BOTH, expand=1)
        self.student_tabel.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        #self.get_cursor()

       # found_students = Student.search_student(search_combo, Search_Entry)

    #================Search System=================
    def search_student(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="gautam", database="face_recognizer_1")
        cursor = connection.cursor()

        
    # Get the user input from the search entry widget
        search_by = self.var_search_combo.get()
        search_value = self.var_search.get()

    # Execute the appropriate SQL query based on the user's search criteria
        if search_by == "Department":
            query = "SELECT * FROM student WHERE dep = %s"
        elif search_by == "Semester":
            query = "SELECT * FROM student WHERE semester = %s"
        elif search_by == "Student_ID":
            query = "SELECT * FROM student WHERE student_id = %s"
        elif search_by == "Enrollment No":
            query = "SELECT * FROM student WHERE enroll_no = %s"
        elif search_by == "Phone No":
            query = "SELECT * FROM student WHERE phone_no = %s"
        elif search_by == "Email":
            query = "SELECT * FROM student WHERE email = %s"
        else:
            messagebox.showerror("Error", "Please select a search criteria")
            return
    
    
    # Execute the query and fetch the results
        cursor.execute(query, (search_value,))
        rows = cursor.fetchall()

    # Clear the table before displaying search results
        for row in self.student_tabel.get_children():
           self.student_tabel.delete(row)

    # Display the search results in the table
        for row in rows:
            self.student_tabel.insert("", END, values=row)


        connection.commit()
        connection.close()
  
    #================Function Declaration============

   
    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_EnrollNo == "" or self.va_std_id == "":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="gautam", database="face_recognizer_1")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)", (
                    
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_EnrollNo.get(),
                                                                                                            self.var_Name.get(),
                                                                                                            self.var_Sem.get(),
                                                                                                            self.var_Dep.get(), 
                                                                                                            self.var_BatchYear.get(),
                                                                                                            self.var_Year.get(),
                                                                                                            self.var_Div.get(),
                                                                                                            self.var_Gender.get(),
                                                                                                            self.var_DOB.get(),
                                                                                                            self.var_Email.get(),
                                                                                                            self.var_Phone.get(),
                                                                                                            self.var_Address.get(),
                                                                                                            self.var_PhotoSample.get()
                                                                                                            #self.var_radio1()
                                                                                                          ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully!", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    #=============To Fetch Data===========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="gautam", database="face_recognizer_1")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data:
                self.student_tabel.insert("", END, values=i)
            conn.commit()   
        conn.close()

    #====Get Cursor======
    def get_cursor(self, event=""):
        cursor_focus = self.student_tabel.focus()
        content = self.student_tabel.item(cursor_focus)
        data = content["values"]

        self.va_std_id.set(data[0]),
        self.var_EnrollNo.set(data[1]),
        self.var_Name.set(data[2]),
        self.var_Sem.set(data[3]),
        self.var_Dep.set(data[4]),
        self.var_BatchYear.set(data[5]),
        self.var_Year.set(data[6]),
        self.var_Div.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9])
        self.var_Email.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_PhotoSample.set(data[13]),
        #self.var_radio1.set(data[13])
    
    #=====Update Function=======
    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_EnrollNo == "" or self.va_std_id == "":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)

        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent = self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="gautam", database="face_recognizer_1")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Student_Id=%s, Enroll_No=%s, Student_Name=%s, Semester=%s, Dep=%s, BatchYear=%s, Year=%s,  Division=%s, Gender=%s, DOB=%s, Email=%s, Phone_No=%s, Address=%s, PhotoSample=%s where Student_Id=%s",(

                                                                                                                                                                                                                         self.va_std_id.get(),
                                                                                                                                                                                                                         self.var_EnrollNo.get(),
                                                                                                                                                                                                                         self.var_Name.get(),
                                                                                                                                                                                                                         self.var_Sem.get(),
                                                                                                                                                                                                                         self.var_Dep.get(), 
                                                                                                                                                                                                                         self.var_BatchYear.get(),
                                                                                                                                                                                                                         self.var_Year.get(),
                                                                                                                                                                                                                         self.var_Div.get(),
                                                                                                                                                                                                                         self.var_Gender.get(),
                                                                                                                                                                                                                         self.var_DOB.get(),
                                                                                                                                                                                                                         self.var_Email.get(),
                                                                                                                                                                                                                         self.var_Phone.get(),
                                                                                                                                                                                                                         self.var_Address.get(),
                                                                                                                                                                                                                         self.var_PhotoSample.get(),
                                                                                                                                                                                                                         #self.var_radio1()
                                                                                                                                                                                                                         self.va_std_id.get()
                                                                                                                                                                                                                         ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success", "Student details succesfully updated!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()


            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


    #=====Delete Function=======
    def delete_data(self):
        if self.var_EnrollNo.get() == "":
            messagebox.showerror("Error", "Student Student ID must be required!!", parent=self.root )

        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this details?", parent=self.root)
                if delete>0:
                     conn=mysql.connector.connect(host="localhost", username="root", password="gautam", database="face_recognizer_1")
                     my_cursor = conn.cursor()
                     sql = "delete from student where Student_Id = %s"
                     val = (self.va_std_id.get(),)
                     my_cursor.execute(sql, val)

                else:
                    if not delete:
                        return
                

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)



    #======Reset Function======
    def reset_data(self):
        self.va_std_id.set("")
        self.var_EnrollNo.set("")
        self.var_Name.set("")
        self.var_Sem.set("Select Semester")
        self.var_Dep.set("Select Department")
        self.var_BatchYear.set("Select Batch-Year")
        self.var_Year.set("Select Year")
        self.var_Div.set("Select Division")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_PhotoSample.set("")
        
    #========Emport Details CSV=================
    
    def fetch_data_1(self):
        try:
            connection = mysql.connector.connect(host='localhost', user='root', password='gautam', database='face_recognizer_1')
            cursor = connection.cursor()
            query = "SELECT * FROM student"
            cursor.execute(query)
            students = cursor.fetchall()
            connection.close()
            return students
        except Exception as e:
            messagebox.showerror("Error", f"Due To : {str(e)}", parent=self.root)
   
    def export_data(self):
        try:
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                                    filetypes=[("CSV Files", "*.csv")], defaultextension='.csv')
            if filename:
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Student_Id', 'EnrollNo', 'Name', 'Sem',  'Dep', 'BatchYear', 'Year',   'Div', 'Gender', 'DOB', 'Email', 'Phone', 'Address', 'PhotoSample'])
                    students = self.fetch_data_1()
                    #print(students)
                    for student in students:
                        writer.writerow(student)
            messagebox.showinfo("Success", "Successfully exported student details", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Due To : {str(e)}", parent=self.root)


    #===========Generate Data Set Or Take Photo Sample===============
    def generate_dataset(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_EnrollNo == "" or self.va_std_id == "" :
            messagebox.showerror("Error", "All Fields are required", parent = self.root)

        else:
            try:
               
                conn=mysql.connector.connect(host="localhost", username="root", password="gautam", database="face_recognizer_1")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Student_Id=%s, Enroll_No=%s, Student_Name=%s, Semester=%s, Dep=%s, BatchYear=%s, Year=%s,   Division=%s, Gender=%s, DOB=%s, Email=%s, Phone_No=%s, Address=%s, PhotoSample=%s where Student_Id=%s",(


                                                                                                                                                                                                                         self.va_std_id.get(),
                                                                                                                                                                                                                         self.var_EnrollNo.get(),
                                                                                                                                                                                                                         self.var_Name.get(),
                                                                                                                                                                                                                         self.var_Sem.get(),
                                                                                                                                                                                                                         self.var_Dep.get(), 
                                                                                                                                                                                                                         self.var_BatchYear.get(),
                                                                                                                                                                                                                         self.var_Year.get(),
                                                                                                                                                                                                                         
                                                                                                                                                                                                                         
                                                                                                                                                                                                                         self.var_Div.get(),
                                                                                                                                                                                                                         self.var_Gender.get(),
                                                                                                                                                                                                                         self.var_DOB.get(),
                                                                                                                                                                                                                         self.var_Email.get(),
                                                                                                                                                                                                                         self.var_Phone.get(),
                                                                                                                                                                                                                         self.var_Address.get(),
                                                                                                                                                                                                                         self.var_PhotoSample.get(),
                                                                                                                                                                                                                         #self.var_radio1()
                                                                                                                                                                                                                         self.va_std_id.get()==id+1
                                                                                                                                                                                                                         ))
                conn.commit()
                self.fetch_data()
                self.reset_data ()
                conn.close() 

            #=====Load predefined data on face frontals from opencv========

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor = 1.3
                        #Minimum Neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg" 
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating your data is completed!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


                                
            
                    




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

