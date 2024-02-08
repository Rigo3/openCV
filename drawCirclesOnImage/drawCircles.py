import cv2

###FUNCTION
def drawCircle(event,x,y,flags,params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0),10)
            
###OPEN IMAGE
img = cv2.imread('dog_backpack.jpg')
   
    
cv2.namedWindow(winname='dog_backpack')
    
cv2.setMouseCallback('dog_backpack',drawCircle)
   
while True:
    
    cv2.imshow('dog_backpack',img)
    ##if Esc(27) is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()