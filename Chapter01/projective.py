import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg')
rows, cols = img.shape[:2]	# row, column, channel

src_points = np.float32([ [0, 0], [cols-1, 0], [0, rows-1], [cols-1, rows-1] ])
dst_points = np.float32([ [0, 0], [cols-1, 0], [int(0.33*cols), rows-1], [int(0.66*cols-1), rows-1] ])
# minimum 4 points to perform projective transformation
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_output = cv2.warpPerspective(img, projective_matrix, (cols, rows))
cv2.imshow('Input', img)
cv2.imshow('Output', img_output)
cv2.waitKey()