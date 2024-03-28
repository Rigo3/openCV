import cv2
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

#Set cascadeClassifier
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Define function for drawing rectangles on faces found
def face_detect(img):
    face_img = img.copy()
    #face_rects contains the position of the rectangles. x,y,w,h
    face_rects=face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)
    
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w, y+h),(0,255,0),5)
    return face_img

#initialize local camera
cap =cv2.VideoCapture(0)


while True:
    
    ret,frame = cap.read()
    frame = face_detect(frame)
    cv2.imshow('Face Detection',frame)
    
    k = cv2.waitKey(1)
    #close when Esc pressed
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()