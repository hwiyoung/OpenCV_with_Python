import cv2
import numpy as np

img = cv2.imread('./images/IMG.jpg')
num_rows, num_cols = img.shape[:2]	# row, column, channel

translation_matrix = np.float32([ [1, 0, 70], [0 , 1, 110] ])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))
img_translation_expSize = cv2.warpAffine(img, translation_matrix, (num_cols + 150, num_rows + 150))
cv2.imshow('Translation', img_translation)
cv2.imshow('Translation_expSize', img_translation_expSize)
cv2.waitKey()