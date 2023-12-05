import cv2 as cv
import numpy as np

# Load the image
image = cv.imread('sample.png')

start = 200
end = 550

image = image[start:end, start:end]

# Convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve edge detection
blurred = cv.GaussianBlur(gray, (7, 7), 0)

# Apply Canny-edge detection
edge_detection_kernel_1 = np.array([[-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]])
edges = cv.filter2D(blurred, -1, edge_detection_kernel_1)
edges=cv.Canny(blurred, 50, 150)

# Display the results
cv.imshow('Original Image', image)
cv.imshow('Blur', blurred)
cv.imshow('Canny Edge', edges)
cv.waitKey(0)
cv.destroyAllWindows()
