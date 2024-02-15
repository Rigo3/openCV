import cv2
import matplotlib.pyplot as plt

#Open image
#2nd parameter set to 0: opens image in grayscale color
img = cv2.imread('rainbow.jpg', 0)

#show image
plt.imshow(img, cmap='gray')

#applying threshold 

#you can define the threshold in tuples. first variable gets the value of the threshold, second gets the resulting image.
#threshold options: THRESH_BINARY, THRESH_TRUNC, THRESH_TOZERO, THRESH_TOZERO_INV
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

plt.imshow(thresh1, cmap='gray')

