import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg')
rows, cols = img.shape[:2]	# row, column, channel

kernel_identity = np.array([ [0, 0, 0], [0, 1, 0], [0, 0, 0] ]_
kernel_3x3 = np.ones((3, 3), np.float32) / 9.0	# normalization
kernel_5x5 = np.ones((5, 5), np.float32) / 25.0	# normalization

cv2.imshow('Original', img)

output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('Identity filter', output)

output = cv2.filter2D(img, -1, kernel_3x3)
#output = cv2.blur(img, (3, 3))
cv2.imshow('3x3 filter', output)

output = cv2.filter2D(img, -1, kernel_5x5)
#output = cv2.blur(img, (5, 5))
cv2.imshow('5x5 filter', output)

cv2.waitKey()
