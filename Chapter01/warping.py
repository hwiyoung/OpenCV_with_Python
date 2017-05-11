import cv2
import numpy as np
import math

img = cv2.imread('./images/IMG.jpg')
rows, cols = img.shape[:2]	# row, column, channel

# Vertical wave
img_output = np.zeros(img.shape, dtype=img.dtype)
for i in range(rows):
	for j in range(cols):
		offset_x = int(25.0 * math.sin(2 * i * 3.14 / 180))
		offset_y = 0
		if j+offset_x < rows:
			img_output[i, j] = img[i, (j+offset_x)%cols]
		else:
			img_output[i, j] = 0
			
cv2.imshow('Input', img)
cv2.imshow('Vertical wave', img_output)

# Horizontal wave
img_output = np.zeros(img.shape, dtype=img.dtype)
for i in range(rows):
	for j in range(cols):
		offset_x = 0
		offset_y = int(16.0 * math.sin(2 * j * 3.14 / 150))
		if i+offset_y < rows:
			img_output[i, j] = img[(i+offset_y)%rows, j]
		else:
			img_output[i, j] = 0
			
cv2.imshow('Horizontal wave', img_output)

# Both horizontal and vertical
img_output = np.zeros(img.shape, dtype=img.dtype)
for i in range(rows):
	for j in range(cols):
		offset_x = int(20.0 * math.sin(2 * i * 3.14 / 150))
		offset_y = int(16.0 * math.cos(2 * j * 3.14 / 150))
		if i+offset_y < rows and j+offset_x < cols:
			img_output[i, j] = img[(i+offset_y)%rows, (j+offset_x)%cols]
		else:
			img_output[i, j] = 0
			
cv2.imshow('Multidirectional wave', img_output)

# Concave
img_output = np.zeros(img.shape, dtype=img.dtype)
for i in range(rows):
	for j in range(cols):
		offset_x = int(128.0 * math.sin(2 * i * 3.14 / (2*cols)))
		offset_y = 0
		if j+offset_x < cols:
			img_output[i, j] = img[i, (j+offset_x)%cols]
		else:
			img_output[i, j] = 0
			
cv2.imshow('Concave', img_output)

cv2.waitKey()