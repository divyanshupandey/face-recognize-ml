# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 15:50:52 2017

@author: acer
"""

import os
import cv2
import numpy as np
from PIL import Image

model = cv2.face.createLBPHFaceRecognizer()

path = 'dataset'

def getImagesWithID(path):
    i_paths = [os.path.join(path, str(f[1])) for f in enumerate(os.listdir(path))]
    faces = []
    face_IDs = []
    print(len(i_paths))
    for imagepath,img in enumerate(i_paths):
        print(img)
        face_img = Image.open(img).convert('L')
        faceNp = np.array(face_img,'uint8')
        face_ID = int(os.path.split(img)[-1].split('.')[0])
        face_IDs.append(face_ID)
        faces.append(faceNp)
    return faces, np.array(face_IDs)
x,y= getImagesWithID(path)
model.train(x,y)
model.save(r'recognizer/face_recognizer.yml')
cv2.destroyAllWindows()
