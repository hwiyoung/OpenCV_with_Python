import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg')
rows, cols = img.shape[:2]	# row, column, channel

# generating the veignette mask using Gaussian kernels
kernel_x = cv2.getGaussianKernel(cols, 200)	# length, std(radius of the bright central region)
kernel_y = cv2.getGaussianKernel(rows, 200)
kernel = kernel_y * kernel_x.T

# normalization and scaling it up
# if you don't scale it up, the image will look black
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

# applying the kernels to the grayscale image and adding the offset
for i in range(3):
	output[:,:,i] = output[:,:,i] * mask
	
# generating the bigger veignette mask
kernel_x = cv2.getGaussianKernel(int(1.5*cols), 200)	# length, std(radius of the bright central region)
kernel_y = cv2.getGaussianKernel(int(1.5*rows), 200)
kernel = kernel_y * kernel_x.T

# normalization and scaling it up
# if you don't scale it up, the image will look black
mask = 255 * kernel / np.linalg.norm(kernel)
mask = mask[int(0.5*rows):, int(0.5*cols):]
output_offset = np.copy(img)

# applying the kernels to the grayscale image and adding the offset
for i in range(3):
	output_offset[:,:,i] = output_offset[:,:,i] * mask

cv2.imshow('Original', img)
cv2.imshow('Vignette', output)
cv2.imshow('Vignette with shifted focus', output_offset)
cv2.waitKey()
