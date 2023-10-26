# import required libraries
import cv2 as cv
import numpy as np

# read and show the image
img = cv.imread("../img_src/counter_strike.jpg")
cv.imshow("Techies", img)

# grayscale the img
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Techies_Gray", gray)


# For normalizing the kernel matrix
def kernel_normalizing(X):
    return np.divide(X, X.sum())


# define the transformation matrix
edge_detection_kernel_1 = np.array([[0, -1, 0],
                                    [-1, 4, -1],
                                    [0, -1, 0]])

edge_detection_kernel_2 = np.array([[-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]])

gaussian_kernel_1 = kernel_normalizing(np.array([[1, 2, 1],
                                                 [2, 4, 2],
                                                 [1, 2, 1]]))

gaussian_kernel_2 = kernel_normalizing(np.identity(5))

print(gaussian_kernel_1)

img_filter = cv.filter2D(img, -1, edge_detection_kernel_1)
cv.imshow("Edge1", img_filter)

img_filter = cv.filter2D(img, -1, edge_detection_kernel_2)
cv.imshow("Edge2", img_filter)

img_filter = cv.filter2D(img, -1, gaussian_kernel_1)
cv.imshow("Edge3", img_filter)

# delay the closing of windows till any key is pressed
cv.waitKey(0)
