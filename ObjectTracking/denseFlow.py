import cv2
import numpy as np

#CAPTURE REFERENCE FRAME, FOR MOVEMENT OF PIXELS FROM THIS STARTING POINT
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()

prvsImg = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv_mask = np.zeros_like(frame1)

#WE WANT TO KEEP THE SATURATION CHANNEL TO THE MAX, SO THE COLORS ARE FULLY SHOWN.
hsv_mask[:,:,1] = 255


while True:
    #GET FRAME CONTINUOUSLY
    ret, frame2 = cap.read()
    #WE NEED IT ON GRAYSCALE IN ORDER TO WORK WITH THE ALGORITHM
    nextImg = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    
    #DENSE FLOW GUNNER FARNEBACK'S ALGORITHM. DEFAULT PARAMS.
    #FLOW GETS VECTORS OF MOVEMENT WITH THIS ALGORITHM
    flow = cv2.calcOpticalFlowFarneback(prvsImg,nextImg,None, 0.5,3,15,3,5,1.2,0)
    
    #CONVERT CARTESIAN POINTS TO ANGULAR, FOR USE IN HSV
    mag,ang = cv2.cartToPolar(flow[:,:,0],flow[:,:,1], angleInDegrees=True)
    
    #SELECT ALL THE VALUES FROM HUE CHANNEL AND SET IT TO ANG/2
    #ONLY HALF OF VALUES. NOT ALL NEEDED FOR A REAL CHANGE IN COLORS. 180 INSTEAD OF 360
    hsv_mask[:,:,0]= ang/2
    
    #SELECT ALL VALUES FROM VALUE CHANNEL AND SET THEM TO NORMALIZED VALUES OF MAGNITUDES.
    hsv_mask[:,:,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    
    #TRANSFORM COLOR HSV TO BGR SO WE CAN SEE THEM
    bgr = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
    cv2.imshow('dense flow', bgr)
    
    #ALWAYS A ESCAPE KEY!
    k = cv2.waitKey(10)
    if k == 27:
        break
    #IMPORTANT TO UPDATE THE FRAMES!!  
    prvsImg=nextImg
    
cap.release()
cv2.destroyAllWindows()