import cv2

#CALLBACK FUNCTION DRAW RECTANGLE
def drawRectangle(event,x,y,flags,param):
    #GLOBAL VARIABLES
    global x1,y1,x2,y2,pt1Set,pt2Set
    if event == cv2.EVENT_LBUTTONUP:
        
        if pt1Set & pt2Set:
            x1=0
            y1=0
            pt1Set=False
            pt2Set=False
    
        if pt1Set == False:
            x1=x
            y1=y
            pt1Set = True
        elif pt2Set == False:
            x2=x
            y2=y
            pt2Set = True
    
#set values
x1=0
y1=0
x2=0
y2=0
pt1Set=False
pt2Set=False

cap = cv2.VideoCapture(0)
#connect callback function to mouse events
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', drawRectangle)

while True:
    
    ret,frame = cap.read()
    #draw rectangle
    if pt1Set:
        cv2.circle(frame,(x1,y1),5,(0,0,255), 4,-1)
    if pt1Set and pt2Set:
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),4,-1)
        
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()