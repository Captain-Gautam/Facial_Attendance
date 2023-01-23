from tkinter import*
from tkinter import ttk
from tkinter import Tk
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import numpy as np
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from setuptools import Command
import cv2
import csv



mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x688+0+0")       #1360x688
        self.root.title("Face Recognition System")
        
        #===========variable=================
        self.var_atten_id = StringVar()
        self.var_EnrollNo = StringVar()
        self.var_Name = StringVar()
        self.var_Dep = StringVar()
        self.var_Time = StringVar()
        self.var_Date = StringVar()
        self.var_Attendance = StringVar()
        
        
        #Logo
        img = Image.open(r"bg_images/topic.png")
        img = img.resize((1360,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        first_label =  Label(self.root, image=self.photoimg)
        first_label.place(x=0,y=0,width=1360,height=100)
    
        #BackGroundImage
        img2 = Image.open(r"bg_images/Technology3.jpg")
        img2 = img2.resize((1360,688),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img =  Label(self.root, image=self.photoimg2)
        bg_img.place(x=0,y=100,width=1360,height=600)


        #Title Of Project
        title_lable1 = Label(bg_img, text = "ATTENDANCE MANAGEMENT SYSTEM", font = ("comicsansns", 28, "italic"),bg ='#011f4b', fg = '#f8ae97') #We can give bg also.
        title_lable1.place(x=0, y=0, width = 1360, height = 45)
        
        
        #Frame
        main_frame = Frame(bg_img, bd=2, bg = "white")
        main_frame.place(x=10, y=50, width=1340, height=545)
        
        #Left Label Frame
        Left_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Student Attendance Details",  font = ("cursive", 14, "bold"))
        Left_frame.place(x=5, y=5, width=390, height= 515)
        
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg = "white")
        left_inside_frame.place(x=5, y=10, width=370, height=475)
        
        #Labelend Entry(Button Entry)
        
        #Attendance ID
        studentId_label = Label(left_inside_frame, text="Attendance ID:", font = ("comicsansns", 11, "bold"), bg ="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentid_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=25,  font = ("cursive", 10, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10, sticky=W)

        #Enrollment Number
        enrollId_label = Label(left_inside_frame, text="Enrollment No.:", font = ("cursive", 11), bg ="white")
        enrollId_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        enrollid_entry = ttk.Entry(left_inside_frame, textvariable=self.var_EnrollNo, width=25,  font = ("cursive", 10, "bold"))
        enrollid_entry.grid(row=1, column=1, padx=10, sticky=W)

        #Name
        nameId_label = Label(left_inside_frame, text="Name:", font = ("cursive", 11), bg ="white")
        nameId_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        nameid_entry = ttk.Entry(left_inside_frame, textvariable=self.var_Name, width=25,  font = ("cursive", 10, "bold"))
        nameid_entry.grid(row=2, column=1, padx=10, sticky=W)

        #Department
        depId_label = Label(left_inside_frame, text="Department:", font = ("cursive", 11), bg ="white")
        depId_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        depid_entry = ttk.Entry(left_inside_frame, textvariable=self.var_Dep, width=25,  font = ("cursive", 10, "bold"))
        depid_entry.grid(row=3, column=1, padx=10, sticky=W)
        
        #Date
        dateId_label = Label(left_inside_frame, text="Date:", font = ("cursive", 11), bg ="white")
        dateId_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        dateid_entry = ttk.Entry(left_inside_frame, textvariable=self.var_Date, width=25,  font = ("cursive", 10, "bold"))
        dateid_entry.grid(row=4, column=1, padx=10, sticky=W)

        #Time
        timeId_label = Label(left_inside_frame, text="Time:", font = ("cursive", 11), bg ="white")
        timeId_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        timeid_entry = ttk.Entry(left_inside_frame, textvariable=self.var_Time, width=25,  font = ("cursive", 10, "bold"))
        timeid_entry.grid(row=5, column=1, padx=10, sticky=W)
        
        #Attendance Status 
        attendace_label = Label(left_inside_frame, text="Attendace Status:", font = ("cursive", 11), bg ="white")
        attendace_label.grid(row=6, column=0, padx=10, sticky=W)

        self.attendace_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_Attendance, font = ("cursive", 10, "bold"), width=25, state="readonly")
        self.attendace_combo["values"] = ("Status","Present", "Absent") 
        self.attendace_combo.current(0)
        self.attendace_combo.grid(row=6, column=1, pady=10, sticky=W)
        
        
        #===Button====
        #Import_CSV Button
        import_btn =Button(left_inside_frame, text="Import CSV", command=self.importCsv, width=13, height=1, font = ("cursive", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground='#011f4b', activeforeground='#f8ae97')
        import_btn.grid(row=7, column=0,  pady=30)

        #Export_CSV Button
        export_btn =Button(left_inside_frame, text="Export CSV", command=self.exportCsv, width=13, height=1, font = ("cursive", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground='#011f4b', activeforeground='#f8ae97')
        export_btn.grid(row=7, column=1,  pady=30)

        #Update Button
        update_btn =Button(left_inside_frame, text="Update", width=13,  height=1, font = ("cursive", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground='#011f4b', activeforeground='#f8ae97')
        update_btn.grid(row=8, column=0, pady=10)
        
        #Reset Button
        reset_btn =Button(left_inside_frame, text="Reset", command=self.reset_data, width=13, height=1, font = ("cursive", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground='#011f4b', activeforeground='#f8ae97')
        reset_btn.grid(row=8, column=1, pady=10)

                
        #Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Attendance Details",  font = ("cursive", 14, "bold"))
        Right_frame.place(x=400, y=5, width=925, height=515)
        
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=910, height=480)
        
        #========Attendance Details Table ============= 
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("Id", "Enrollment_No", "Name", "Department", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("Id", text="Attendace_Id")
        self.AttendanceReportTable.heading("Enrollment_No", text="Enrollment Number")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Attendance", text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("Id", width=150)
        self.AttendanceReportTable.column("Enrollment_No", width=150)
        self.AttendanceReportTable.column("Name", width=150)
        self.AttendanceReportTable.column("Department", width=150)
        self.AttendanceReportTable.column("Date", width=150)
        self.AttendanceReportTable.column("Time", width=150)
        self.AttendanceReportTable.column("Attendance", width=150)
      
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        
        
    #=======Fetch Data==========
    
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
            
    #======Import CSV Data========        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
        

    #======Export CSV Data========
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error", "No Data Found to Export!!", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success", "Your data is exported to "+os.path.basename(fln)+" successfully!")
        
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)               
        
        
    #======Get Cursor=======
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_EnrollNo.set(rows[1])
        self.var_Name.set(rows[2])
        self.var_Dep.set(rows[3])
        self.var_Time.set(rows[4])
        self.var_Date.set(rows[5])
        self.var_Attendance.set(rows[6])
        
        
    #======Reset Data===========
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_EnrollNo.set("")
        self.var_Name.set("")
        self.var_Dep.set("")
        self.var_Time.set("")
        self.var_Date.set("")
        self.var_Attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
