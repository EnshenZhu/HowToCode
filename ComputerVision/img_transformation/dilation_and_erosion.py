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
binary_img = cv.threshold(edge_img, thresh=150, maxval=255, type=cv.THRESH_BINARY)[1]
cv.imshow("Binary", binary_img)

# define different kernels
kernel_1 = np.array(object=[[0, 1, 0],
                            [1, 1, 1],
                            [0, 1, 0]],
                    dtype=np.uint8)

kernel_2 = np.array(object=[[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]],
                    dtype=np.uint8)

# Conduct dilation
dilated_binary = cv.filter2D(binary_img, -1, kernel_1)
cv.imshow("Dilation_binary", dilated_binary)

dilated_binary2 = cv.dilate(binary_img, kernel_1, iterations=1)
cv.imshow("Dilation_binary2", dilated_binary2)

# Conduct erosion
eroded_binary = cv.erode(binary_img, kernel_1, iterations=1)
cv.imshow("Erosion_binary", eroded_binary)

# Do some math
produce1 = dilated_binary2 - binary_img  # get the pixels we dilate previously
cv.imshow("DB2-B", produce1)

produce2 = binary_img - eroded_binary  # get the pixels we eroded previously
cv.imshow("B-E", produce2)

# delay the closing of windows till any key is pressed
cv.waitKey(0)
