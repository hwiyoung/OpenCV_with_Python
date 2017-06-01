import cv2
import numpy as np

input_image = cv2.imread('./image/IMG.jpg')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
output_image = None

sift = cv2.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray_image, None)

output_image = cv2.drawKeypoints(input_image, keypoints, output_image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SIFT features', output_image)
cv2.waitKey()

######

# To detect and compute at the same time
keypoints, descriptors = sift.detectAndCompute(gray_image, None)
print(len(descriptors))
print(descriptors.shape)
print(descriptors[0])
