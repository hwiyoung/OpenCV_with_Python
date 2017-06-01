import cv2
import numpy as np

input_image = cv2.imread('./image/IMG.jpg')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
output_image = None

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()
# If we don't set this threshold, there will be too many keypoints
surf.setHessianThreshold(1500)

keypoints = sift.detect(gray_image, None)
#descriptors = sift.compute(gray_image, keypoints, None)
descriptors = surf.compute(gray_image, keypoints, None)

output_image = cv2.drawKeypoints(input_image, keypoints, output_image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SIFT detector - SURF descriptors', output_image)
cv2.waitKey()
