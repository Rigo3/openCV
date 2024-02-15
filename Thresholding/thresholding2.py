import cv2
import matplotlib.pyplot as plt

#Open crossword image in grayscale
img = cv2.imread('crossword.jpg',0)

#show image
plt.imshow(img, cmap='gray')

#define function for viewing larger image in grayscale
def show_pic(img):
    fig = plt.figure(figsize = (15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')

show_pic(img)

#you can experiment with the threshold types, or moving the threshold value
ret, th1 =cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
show_pic(th1)


#Adaptive threshold, automatically adapt the values, from pixels around
#blocksize need to be odd numbers
#constant value is substracted from the mean or median mean
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)

#for better results, you can blend both previous thresholds

blended = cv2.addWeighted(src1=th1, alpha=0.6, src2=th2, beta=0.4, gamma=0)
show_pic(blended)
