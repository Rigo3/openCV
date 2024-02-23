#Image Processing Assessment
#This assessment was tested on Jupyter-Lab

import cv2
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

def display_img(img,cmap=None):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

#**TASK: Open and display the giaraffes.jpg image that is located in the DATA folder.**
giraffe = cv2.imread('../DATA/giraffes.jpg')
giraffe = cv2.cvtColor(giraffe,cv2.COLOR_BGR2RGB)
display_img(giraffe)

#**TASK:Apply a binary threshold onto the image.**
giraffe=cv2.imread('../DATA/giraffes.jpg',0)
ref,th=cv2.threshold(giraffe,127,255,cv2.THRESH_BINARY)
display_img(th,cmap='gray')

#**TASK: Open the giaraffes.jpg file from the DATA folder and convert its colorspace to  HSV and display the image.**
giraffe=cv2.imread('../DATA/giraffes.jpg')
giraffe=cv2.cvtColor(giraffe,cv2.COLOR_BGR2HSV)
display_img(giraffe)

#**TASK: Create a low pass filter with a 4 by 4 Kernel filled with values of 1/10 (0.01) and then use 2-D Convolution to blur the giraffer image (displayed in normal RGB)**
kernel=np.ones((4,4),dtype=np.float32)/10
giraffe=cv2.imread('../DATA/giraffes.jpg')
giraffe=cv2.cvtColor(giraffe,cv2.COLOR_BGR2RGB)
giraffe_blurr=cv2.filter2D(giraffe,-1,kernel)
display_img(giraffe_blurr)

#**TASK: Create a Horizontal Sobel Filter (sobelx from our lecture) with a kernel size of 5 to the grayscale version of the giaraffes image and then display the resulting gradient filtered version of the image.**
giraffe = cv2.imread('../DATA/giraffes.jpg',0)
giraffe_sobelx=cv2.Sobel(giraffe,cv2.CV_64F,1,0,ksize=5)
display_img(giraffe_sobelx,cmap='gray')

#**TASK: Plot the color histograms for the RED, BLUE, and GREEN channel of the giaraffe image. Pay careful attention to the ordering of the channels.**
giraffe=cv2.imread('../DATA/giraffes.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    hist=cv2.calcHist([giraffe],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
plt.title('Giraffes Histograms')

