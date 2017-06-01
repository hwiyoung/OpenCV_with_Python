import cv2
import numpy as np

img = cv2.imread('./image/IMG.jpg')
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()
# If we don't set this threshold, there will be too many keypoints
surf.setHessianThreshold(1500)

kp, des = surf.detectAndCompute(gray, None)
img = cv2.drawKeypoints(img, kp, None, (0,255,0), 4)

cv2.imshow('SURF features', img)
cv2.waitKey()
