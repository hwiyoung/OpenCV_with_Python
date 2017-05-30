import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg')
rows, cols = img.shape[:2]	# row, column, channel

size = 15

# generating the kernel - horizontal(column direction)
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

# applying the kernel to the input images/IMG
output = cv2.filter2D(img, -1, kernel_motion_blur)

cv2.imshow('Motion Blur - horizontal', output)

# generating the kernel - vertical(row direction)
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[:, int((size-1)/2)] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

# applying the kernel to the input images/IMG
output = cv2.filter2D(img, -1, kernel_motion_blur)

cv2.imshow('Motion Blur - vertical', output)
cv2.waitKey()