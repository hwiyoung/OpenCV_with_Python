import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg')
num_rows, num_cols = img.shape[:2]	# row, column, channel

img_scaled = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Scaling - Linear Interpolation', img_scaled)
cv2.waitKey()
img_scaled = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled)
cv2.waitKey()
img_scaled = cv2.resize(img, (450, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', img_scaled)
cv2.waitKey()