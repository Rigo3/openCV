import cv2
import numpy as np

#read first frame for setting the roi
cap = cv2.VideoCapture(0)
ret,frame = cap.read()

#In this case we are using face detector cascade classifier
face_cascade=cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_frontalface_default.xml')
face_rects=face_cascade.detectMultiScale(frame)

#unpack tuple of first rectangle detected. As we only are testing 1 face on our camera.
(face_x,face_y,w,h) = tuple(face_rects[0])
track_window = (face_x, face_y, w, h)

roi = frame[face_y:face_y+h, face_x:face_x+w]

#This algorithms work with HSV instead of BGR
roi_hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

#Histogram is needed so the algorithm could track it through the movement of objects.
#We are only selecting the Hue channel.
roi_hist = cv2.calcHist([roi_hsv], [0],None,[180],[0,180])

cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10,1)


while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        #Back Projection needs the histogram previously computed
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        #####################  MeanShift  #####################
#         ret, track_window = cv2.meanShift(dst,track_window,term_crit)
        
#         x,y,w,h = track_window
#         img2 = cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),5)
        #Returning object contains the points for the rectangle
    
        #####################  CamShift  #####################
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        
        img2 = cv2.polylines(frame, [pts],True,(0,0,255),5)
        
        #####################
        cv2.imshow('img',img2)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()