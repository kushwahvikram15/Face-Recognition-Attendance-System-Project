from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import Font
import tkinter
import shutil
import pickle
import time
from tkinter import messagebox
import datetime
import numpy as np
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage
import pandas as pd
import cv2
import os
import csv


class Application():
    name = ""
    id = -1

    def __init__(self, master):
        my_font = Font(family='Ink Free', size=40, weight='bold')
        my_font3 = Font(family='Ink Free', size=20, weight='bold')
        my_font2 = Font(family="Ink Free", size=13, weight='bold')
        self.bg_img = ImageTk.PhotoImage(Image.open("Images/bg_image.jpg"))
        self.top_img = ImageTk.PhotoImage(Image.open("Images/top.jpg"))
        self.master = master

        self.top = Frame(self.master, height=100, width=1536, bg='#5e615e')
        self.top.place(x=0, y=0)
        f = Frame(self.master, height=7, width=1536, bg='red')
        f.place(x=0, y=80)
        f = Frame(self.master, height=5, width=1536, bg='red')
        f.place(x=0, y=745)
        self.footer = Frame(self.master, height=100, width=1536, bg='#5e615e')
        self.footer.place(x=0, y=750)
        self.bottom = Frame(self.master, height=660, width=1536, bg='#2b2929')
        self.bottom.place(x=0, y=85)

        self.top_l = Label(self.top, image=self.top_img)
        self.top_l.place(x=0, y=0)
        self.hd = Label(self.top, text="Face Recognition Attendance System", bg='black', fg="#f7883e", font=my_font)
        self.hd.place(x=375, y=10)
        self.hd = Label(self.top, text="Date : ", bg='black', fg="white", font=my_font2)
        self.hd.place(x=10, y=10)
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        self.hd = Label(self.top, text=f"{date}", bg='black', fg="yellow", font=my_font3)
        self.hd.place(x=10, y=30)
        self.bg_l = Label(self.bottom, image=self.bg_img)
        self.bg_l.place(x=0, y=0)
        self.bg_l = Label(self.footer, image=self.top_img)
        self.bg_l.place(x=0, y=0)

        self.reg_image = Image.open('Images/Registration.jpg')
        self.reg_image = self.reg_image.resize((300, 200), Image.ANTIALIAS)
        self.reg_image = ImageTk.PhotoImage(self.reg_image)
        reg_frame = Frame(self.bottom, height=245, width=300, bg='#2b2929', cursor='hand2')
        reg_frame.place(x=600, y=50)
        self.reg_l = Button(reg_frame, image=self.reg_image, command=self.registration)
        self.reg_l.place(x=0, y=0)
        self.lbl = Label(reg_frame, text="Registration", bg="#2b2929", fg='#6dd945', font=my_font3).place(x=80, y=208)

        self.cap_image = Image.open('Images/take_pic.jpg')
        self.cap_image = self.cap_image.resize((300, 200), Image.ANTIALIAS)
        self.cap_image = ImageTk.PhotoImage(self.cap_image)
        reg_frame = Frame(self.bottom, height=245, width=300, bg='#2b2929', cursor='hand2')
        reg_frame.place(x=1050, y=50)
        self.reg_l = Button(reg_frame, image=self.cap_image, command=self.capture)
        self.reg_l.place(x=0, y=0)
        self.lbl = Label(reg_frame, text="Capturing Images", bg="#2b2929", fg='#6dd945', font=my_font3).place(x=35,
                                                                                                              y=208)

        self.tra_image = Image.open('Images/train_image.jpg')
        self.tra_image = self.tra_image.resize((300, 200), Image.ANTIALIAS)
        self.tra_image = ImageTk.PhotoImage(self.tra_image)
        reg_frame = Frame(self.bottom, height=245, width=300, bg='#2b2929', cursor='hand2')
        reg_frame.place(x=600, y=350)
        self.reg_l = Button(reg_frame, image=self.tra_image, command=self.TrainImages)
        self.reg_l.place(x=0, y=0)
        self.lbl = Label(reg_frame, text="Training", bg="#2b2929", fg='#6dd945', font=my_font3).place(x=80, y=208)

        self.track_image = Image.open('Images/track_pic.jpg')
        self.track_image = self.track_image.resize((300, 200), Image.ANTIALIAS)
        self.track_image = ImageTk.PhotoImage(self.track_image)
        reg_frame = Frame(self.bottom, height=245, width=300, bg='#2b2929', cursor='hand2')
        reg_frame.place(x=1050, y=350)
        self.reg_l = Button(reg_frame, image=self.track_image, command=self.TrackImages)
        self.reg_l.place(x=0, y=0)
        self.lbl = Label(reg_frame, text="Tracking Faces", bg="#2b2929", fg='#6dd945', font=my_font3).place(x=35, y=208)

        self.att_frame = Frame(self.bottom, height=600, width=450, bg='#2b2929')
        self.att_frame.place(x=30, y=30)
        self.r1 = Frame(self.bottom, height=605, width=5, bg='#e89c20')
        self.r1.place(x=25, y=30)
        self.r2 = Frame(self.bottom, height=605, width=5, bg='#e89c20')
        self.r2.place(x=480, y=30)
        self.r3 = Frame(self.bottom, height=5, width=460, bg='#e89c20')
        self.r3.place(x=25, y=25)
        self.r4 = Frame(self.bottom, height=5, width=450, bg='#e89c20')
        self.r4.place(x=30, y=630)
        self.r5 = Frame(self.bottom, height=5, width=460, bg='#e89c20')
        self.r5.place(x=25, y=80)

        Label(self.att_frame, text="Today's Attendance", font=my_font3, bg='#2b2929', fg='white').place(x=105, y=10)
        Label(self.att_frame, text="No   Id          Name          Time", font=my_font3, bg="#2b2929",
              fg="#759669").place(x=5, y=65)

    def registration(self):
        my_font1 = Font(family='Ink Free', size=25, weight='bold')
        my_font2 = Font(family='Ink Free', size=15, weight='bold')
        my_font3 = Font(family='Ink Free', size=20, weight='bold')

        self.reg_frame = Frame(self.bottom, height=350, width=340, bg='#2b2929')
        self.reg_frame.place(x=400, y=200)
        top_frame = Frame(self.reg_frame, height=50, width=340, bg='#5e615e')
        top_frame.place(x=0, y=0)
        Label(top_frame, text='Register Here', bg='#5e615e', fg='#f02e2e', font=my_font1).place(x=75, y=0)

        lbl = Label(self.reg_frame, text="Enter ID", height=2, bg="#2b2929", font=my_font2)
        lbl.place(x=10, y=65)

        self.txt = Entry(self.reg_frame, width=20, bg="#2b2929", fg="white", font=my_font3)
        self.txt.place(x=10, y=110)

        lbl2 = Label(self.reg_frame, text="Enter Name", height=2, bg="#2b2929", font=my_font2)
        lbl2.place(x=10, y=160)

        self.txt2 = Entry(self.reg_frame, width=20, bg="#2b2929", fg="white", font=my_font3)
        self.txt2.place(x=10, y=205)

        reg_button = Button(self.reg_frame, text="Submit", bg="yellow", fg="Black", width=10, height=1,
                            command=self.submit)
        reg_button.place(x=250, y=300)

        exit = Button(top_frame, text='X', font='7', activeforeground='black', fg='#2b2929', bg='#5e615e',
                      activebackground='red'
                      , command=self.submit)
        exit.place(x=310, y=0)

    def capture(self):
        try:
            name = self.txt2
            Id = self.txt
        except:
            messagebox.showinfo("Info", "Please Enter your name and Id before")
            self.registration()
        if self.is_number(Id) and name.isalpha():
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            TakeNo = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    TakeNo += 1
                    cv2.imwrite("TrainingImage\ " + name + "." + str(Id) + '.' + str(TakeNo) + ".jpg",
                                gray[y:y + h, x:x + w])
                    cv2.imshow('frame', img)

                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                elif TakeNo > 60:
                    break
            cam.release()
            cv2.destroyAllWindows()

            msg = "Images Saved for Id : " + str(Id) + " Name : " + name
            messagebox.showinfo("Info", msg)
            row = [Id, name]
            with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)

            csvFile.close()
        else:
            msg = "Enter Alphabetical Name or Numeric Id"
            messagebox.showinfo("Error", msg)

    def TrainImages(self):
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces, Id = self.getImageAndLabels("TrainingImage")
        recognizer.train(faces, np.array(Id))
        recognizer.save("TrainingImageLabel\Trainner.yaml")
        msg = "Image Trained"
        messagebox.showinfo("Info", msg)

    def getImageAndLabels(self, path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        Ids = []
        for imagePath in imagePaths:
            pilImage = Image.open(imagePath).convert('L')
            imageNp = np.array(pilImage, 'uint8')
            print(imagePath)
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids

    def TrackImages(self):
        my_font1 = Font(family='Ink Free', size=25, weight='bold')
        my_font2 = Font(family='Ink Free', size=15, weight='bold')
        my_font3 = Font(family='Ink Free', size=20, weight='bold')

        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        recognizer.read("TrainingImageLabel\Trainner.yaml")
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    tt = str(Id) + "-" + aa
                    attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if (conf > 75):
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('im', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        fileName = "Attendance\Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
        attendance.to_csv(fileName, index=False)
        cam.release()
        cv2.destroyAllWindows()

        count = -1
        print(attendance)
        c = 0
        for i in attendance['Name']:
            d = {}
            count += 1
            for j in i:
                if j not in d:
                    d[j] = 1
                else:
                    d[j] += 1
            print(d)
            maxx = max(d.values())
            cnt = 0
            for key, value in d.items():
                if value == maxx:
                    name = key
                    cnt += 1

            if cnt == 1:
                c += 1
                self.att = Label(self.att_frame, text=f" {c}", bg="#2b2929", font=my_font2, fg="white")
                self.att.place(x=5, y=100 + count * 30)
                self.att = Label(self.att_frame, text=f" {attendance.loc[count]['Id']}", bg="#2b2929", font=my_font2,
                                 fg="white")
                self.att.place(x=50, y=100 + count * 30)
                self.name_frame = Frame(self.att_frame, height=30, width=150, bg="#2b2929")
                self.name_frame.place(x=100, y=100 + count * 30)
                self.att = Label(self.name_frame, text=f"{name}", bg="#2b2929", font=my_font2, fg="white",
                                 justify=CENTER)
                self.att.place(x=40, y=0)
                self.att = Label(self.att_frame, text=f" {attendance.loc[count]['Time']}", bg="#2b2929", font=my_font2,
                                 fg="white")
                self.att.place(x=320, y=100 + count * 30)

    def submit(self):
        messagebox.showinfo("Info", "User Registered")
        self.txt = self.txt.get()
        self.txt2 = self.txt2.get()
        self.reg_frame.destroy()

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


root = tk.Tk()
root.title("Application")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenwidth()))
root.resizable(False, False)
app = Application(root)
root.mainloop()