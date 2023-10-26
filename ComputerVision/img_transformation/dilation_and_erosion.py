# import required libraries
import cv2 as cv
import numpy as np

# read and show the image
img = cv.imread("../img_src/counter_strike.jpg")
cv.imshow("Techies", img)

# grayscale the img
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# define the edging matrix
edge_kernel = np.array([[-1, -1, -1],
                        [-1, 8, -1],
                        [-1, -1, -1]])

# get the image edge
edge_img = cv.filter2D(gray, -1, edge_kernel)
cv.imshow("Edge", edge_img)

# binarize the image
binary = cv.threshold(edge_img, thresh=150, maxval=255, type=cv.THRESH_BINARY)
cv.imshow("Binary", edge_img)

# keep image showing
cv.waitKey(0)
