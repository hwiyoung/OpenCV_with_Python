import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_matches(img1, keypoints1, img2, keypoints2, matches):
    rows1, cols1 = img1.shape[:2]
    rows2, cols2 = img2.shape[:2]

    # Create a new output image that concatenates the two images together
    output_img = np.zeros((max([rows1,rows2]), cols1+cols2, 3), dtype='uint8')
    output_img[:rows1, :cols1, :] = np.dstack([img1, img1, img1])
    output_img[:rows2, cols1:cols1+cols2, :] = np.dstack([img2, img2, img2])

    # Draw connecting lines between matching keypoints
    for match in matches:
        # Get the matching keypoints for each of the images
        img1_idx = match.queryIdx
        img2_idx = match.trainIdx

        (x1, y1) = keypoints1[img1_idx].pt
        (x2, y2) = keypoints2[img2_idx].pt

        # Draw a small circle at both co-ordinates and then draw a line
        radius = 5
        colour = (0,255,0)   # green 
        thickness = 1
        cv2.circle(output_img, (int(x1),int(y1)), radius, colour, thickness)   
        cv2.circle(output_img, (int(x2)+cols1,int(y2)), radius, colour, thickness)
        cv2.line(output_img, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), colour, thickness)

    return output_img

if __name__=='__main__':
	img1 = cv2.imread('./image/IMG_20170308_161717.jpg')
	img2 = cv2.imread('./image/IMG_0102.jpg')
	
	gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Initialize ORB detector
	orb = cv2.ORB_create()

    # Extract keypoints and descriptors
	keypoints1, descriptors1 = orb.detectAndCompute(gray_img1, None)
	'''
	print(keypoints1[0].pt)
	print(keypoints1[0].size)
	print(keypoints1[0].angle)
	print(keypoints1[0].response)
	print(keypoints1[0].octave)
	print(keypoints1[0].class_id)
	'''
	
	keypoints2, descriptors2 = orb.detectAndCompute(gray_img2, None)

    # Create Brute Force matcher object
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
	matches = bf.match(descriptors1, descriptors2)

    # Sort them in the order of their distance
	matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 'n' matches
	img3 = draw_matches(gray_img1, keypoints1, gray_img2, keypoints2, matches[:30])
	
	plt.figure(1)
	plt.imshow(img3, aspect='equal')	
	plt.show()