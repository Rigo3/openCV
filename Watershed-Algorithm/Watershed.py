import cv2
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline


road = cv2.imread('../DATA/road_image.jpg')
road_copy = road.copy()
# plt.imshow(road_copy)

#It is important that we set markers as int32, and segments as uint8
markers_img = np.zeros(road.shape[:2],dtype=np.int32)
segments = np.zeros(road.shape,dtype=np.uint8)

#import color mapping library
from matplotlib import cm

#Test the first color tab10
cm.tab10(0)

#convert the color to 255 values, instead of percentage, and truncate it to the third element only
np.array(cm.tab10(0)[:3])*255

#Functionalizing the color % to 255

def set_color(i):
    return (tuple(np.array(cm.tab10(i)[:3])*255))

#get the first 10 colors from the library and insert them in colors[]
colors=[]
for i in range(10):
    colors.append(set_color(i))


#GLOBAL VARIABLES
n_markers=10
current_marker=1
marker_updated=False

#CALLBACK FUNCTION
def set_seed(event,x,y,flag,paramn):
    
    global marker_updated
    if event==cv2.EVENT_LBUTTONDOWN:

        #set seeds positions on markers_img for later use on watershed method.
        #Note that instead of giving a color to the circle, we only set an int value(current_marker).
        cv2.circle(markers_img,(x,y),10,(current_marker),-1)
    
        #draw a circle on the user view image, with the current marker color.
        cv2.circle(road_copy,(x,y),10,(colors[current_marker]),-1)
        
        marker_updated=True
          
    
#ASSIGN CALLBACK FUNCTION TO MOUSE CLICK
cv2.namedWindow('Road Seeds')
cv2.setMouseCallback('Road Seeds', set_seed)

#WHILE LOOP
while True:
        
    #show 2 windows, markers_img only used for setting the seeds
    cv2.imshow('Road Seeds', road_copy)
    cv2.imshow('Segments',segments)
    
    #CLOSE WINDOWS
    k = cv2.waitKey(1)
    #close if esc is pressed
    if(k == 27):
        break
        
    #If user clicks 'c' key, then clear both images
    elif k == ord('c'):
        road_copy = road.copy()
        markers_img = np.zeros(road_copy.shape[:2],dtype=np.int32)
        segments = np.zeros(road_copy.shape,dtype=np.uint8)
        
    #update colors
        #chr() is used, because the code for each numbered key on the keyboard is different to the real number.
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))
        
    if marker_updated:
        #We need to make a copy because markers_img is in use
        markers_img_copy =markers_img.copy()
        
        #Once the user clicks somewhere, we make a copy, with the properties of the last click.
        #Meaning we already have a new seed, then we can proceed to use watershed method
        markers_img_copy = cv2.watershed(road,markers_img_copy)
        #this watersheded image, is only used to color the sections on the segments image in next step.
        
        segments = np.zeros(road.shape,dtype = np.uint8)
        
        #Loop through each color(1-9), and color the segments-pixels which have same values between markers_img_copy-pixels and (1-9). 
        #The pixel values from markers_img_copy are set each time user clicks.
        for color_ind in range(n_markers):
            #COLORING SEGMENTS, NUMPY CALL
            segments[markers_img_copy == (color_ind)] = colors[color_ind]
        
        
cv2.destroyAllWindows()

    