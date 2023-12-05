import cv2
import numpy as np

# Load image
img = cv2.imread("sample.png")

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range of white color in HSV
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 255, 255])

# Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)

# Remove small regions
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Invert mask
img_no_reflection = cv2.bitwise_not(opening)

# Combine original image and inverted mask
result = cv2.bitwise_and(img, img, mask=img_no_reflection)

# Save result
cv2.imshow("result.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()