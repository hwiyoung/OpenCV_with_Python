import cv2

gray_img = cv2.imread('./images/IMG.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale', gray_img)
cv2.waitKey()
cv2.imwrite('./images/grayIMG.jpg', gray_img)