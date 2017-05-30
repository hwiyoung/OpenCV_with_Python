import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg')
rows, cols = img.shape[:2]	# row, column, channel

# generating the kernels
kernel = np.ones((5,5), np.uint8)

# converting the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# applying the kernels to the grayscale image and adding the offset
img_erosion = cv2.erode(gray_img, kernel, iterations = 1)
img_dilation = cv2.dilate(gray_img, kernel, iterations = 1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.waitKey()