import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg')
rows, cols = img.shape[:2]	# row, column, channel

# equalize the histogram of the input image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
histeq = cv2.equalizeHist(gray_img)

cv2.imshow('Original', gray_img)
cv2.imshow('Histogram equalized', histeq)
cv2.waitKey()
