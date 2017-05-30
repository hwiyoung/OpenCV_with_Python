import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]	# row, column, channel

###################
# Embossing
kernel_emboss_1 = np.array([[0,-1,-1], 
							[1,0,-1], 
							[1,1,0]])
kernel_emboss_2 = np.array([[-1,-1,0], 
							[-1,0,1], 
							[0,1,1]])
kernel_emboss_3 = np.array([[1,0,0], 
							[0,0,0], 
							[0,0,-1]])

output_1 = cv2.filter2D(img, -1, kernel_emboss_1) + 128
output_2 = cv2.filter2D(img, -1, kernel_emboss_2) + 128
output_3 = cv2.filter2D(img, -1, kernel_emboss_3) + 128

cv2.imshow('Input', img)
cv2.imshow('Embossing - South West', output_1)
cv2.imshow('Embossing - South East', output_2)
cv2.imshow('Embossing - North West', output_3)
cv2.waitKey()