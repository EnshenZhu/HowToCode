import cv2 as cv
import numpy as np

# Load the image
image = cv.imread('sample.png')

start = 200
end = 550

image = image[start:end, start:end]

# Convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply histogram equalization to improve contrast
equalized = cv.equalizeHist(gray)

# Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for better results
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_result = clahe.apply(equalized)

# Apply Gaussian blur to reduce noise and improve edge detection
blurred = cv.GaussianBlur(clahe_result, (17, 17), 0)

# Apply Canny-edge detection
edges = cv.Canny(blurred, 50, 150)

# Display the results
cv.imshow('Original Image', image)
cv.imshow('Enhanced Contrast', clahe_result)
cv.imshow('Blur', blurred)
cv.imshow('Canny Edge', edges)

cv.imwrite("edge.jpg", edges)

cv.waitKey(0)
cv.destroyAllWindows()
