# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:52:47 2017

@author: acer
"""

import numpy as np
import cv2
import xlrd
import openpyxl
import os

workbook = openpyxl.load_workbook('book.xlsx')
worksheet = workbook.active

book = xlrd.open_workbook('book.xlsx')
sheet = book.sheet_by_index(0)
print(sheet.nrows)

name = input("user_id")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)
it = 0

model = cv2.face.createLBPHFaceRecognizer()
model.load(r'recognizer/face_recognizer.yml')
path = 'dataset'
classes = [os.path.join(path, str(f[1])) for f in enumerate(os.listdir(path))]

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if(len(faces) == 1):
        for (x,y,w,h) in faces:
            save_str = r"dataset/"+str(int(len(classes)/21))+"."+str(it)+".jpg"
            print(save_str)
            cv2.imwrite(save_str, gray[y:y+h,x:x+w])
            it = it + 1
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.waitKey(15)
    cv2.imshow('img',img)
    cv2.waitKey(1)
    if it > 20:
        num=int(len(classes)/21)
        worksheet['A'+str(num+1)] = num
        worksheet['B'+str(num+1)] = name
        workbook.save("book.xlsx")
        break

cap.release()
cv2.destroyAllWindows()