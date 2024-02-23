import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    blank_img=np.zeros((600,600))
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300), fontFace=font,fontScale=5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
    return blank_img

def display_img(img):
    fig=plt.figure(figsize=(12,10))
    ax= fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

img = load_img()
display_img(img)

white_noise=np.random.randint(low=0,high=2,size=(600,600))

display_img(white_noise)

#convert the image to 255, because it is in 1s and 0s
white_noise = white_noise*255

noise_img= img+white_noise
display_img(noise_img)

kernel =np.ones((5,5),dtype=np.uint8)
opening = cv2.morphologyEx(noise_img,cv2.MORPH_OPEN,kernel)

display_img(opening)

#this next lines make the foreground noise
black_noise = np.random.randint(0,2,(600,600))

black_noise = black_noise*-255
black_noise_img = img +black_noise

black_noise_img[black_noise_img==-255]=0


#gradient method
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
