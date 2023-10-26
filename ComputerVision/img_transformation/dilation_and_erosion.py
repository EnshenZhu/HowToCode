# import required libraries
import cv2 as cv
import numpy as np

# read and show the image
img = cv.imread("../img_src/techies.jpg")
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
binary_img = cv.threshold(edge_img, thresh=150, maxval=255, type=cv.THRESH_BINARY)
cv.imshow("Binary", binary_img[1])

# print(binary[1])

# Conduct dilation
dilation_kernel = np.array(object=[[0, 1, 0],
                                   [1, 1, 1],
                                   [0, 1, 0]],
                           dtype=np.uint8)

dilation_binary = cv.filter2D(binary_img[1], -1, dilation_kernel)
cv.imshow("Dilation_binary", dilation_binary)

dilation_binary2 = cv.dilate(binary_img[1], dilation_kernel, iterations=1)
cv.imshow("Dilation_binary2", dilation_binary2)

# delay the closing of windows till any key is pressed
cv.waitKey(0)
