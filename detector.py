# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:52:47 2017

@author: acer
"""

import numpy as np
import cv2
import xlrd

book = xlrd.open_workbook('book.xlsx')
sheet = book.sheet_by_index(0)

def detector():
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    cap = cv2.VideoCapture(1)
    it = 0
    
    model = cv2.face.createLBPHFaceRecognizer()
    model.load(r'recognizer/face_recognizer.yml')
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if(len(faces) == 1):
            for (x,y,w,h) in faces:
                it = it + 1
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                id, conf =model.predict(gray[y:y+h,x:x+w])
                print(sheet.cell(id,1))
                #cv2.putText(cv2.fromarray(img), str(id),(x,y+h),font,255)
                cv2.putText(img,str(sheet.cell(id,1))+" conf "+str(conf),(x,y-10),font,0.55,(0,0,0),1)
        cv2.imshow('img',img)
        if (cv2.waitKey(1) == ord('q')):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return 

detector()