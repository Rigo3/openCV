import cv2
import matplotlib.pyplot as plt
import numpy as np


#function for loading images and saving it as RGB 
def load_img():
    img=cv2.imread('bricks.jpg').astype(np.float32)/255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

#function for display the images larger, expects an image
def display_img(img):
    fig=plt.figure(figsize=(14,12))
    ax=fig.add_subplot(111)
    ax.imshow(img)

i = load_img()
display_img(i)

#One way to make brighter or darker the image is applying the gamma correction
gamma=1/4
result = np.power(i,gamma)
display_img(result)

#add text to the image for better view of resultsd
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)


#Aplying kernels has a variety of results.
#kernel is a small matrix used to apply effects like blurring, sharpening, outlining, etc.

kernel = np.ones(shape=(5,5),dtype=np.float32)/25

#blur image by a LOW PASS FILTER with a 2D convolution:
#second parameter:desired depth:  output depth== input depth
dst=cv2.filter2D(img,-1,kernel)
display_img(dst)



#a quicker way to do cv2 prestablished blurring:

#reload image
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
print('reset')

blurred = cv2.blur(img,ksize=(12,12))
display_img(blurred)


#you can also apply the median blur
#kernel size is squared, only 1 digit is needed.
median_result = cv2.medianBlur(img,5)
display_img(median_result)

#median blur is really good for removing noise.


#Bilateral filter
blur = cv2.bilateralFilter(img,9,75,75)

#it is similar to median blur. It keeps some of the edges in a blurring process.
