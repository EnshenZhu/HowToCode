import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.feature import local_binary_pattern
from skimage.color import label2rgb

# Load an example image
image = data.camera()

# Convert the image to grayscale if it's not already
if image.ndim > 2:
    image = image.mean(axis=2)

# Compute LBP features
radius = 3
n_points = 8 * radius
lbp = local_binary_pattern(image, n_points, radius, method='uniform')

# Display the original image and the LBP image
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('Original Image')

ax2.imshow(lbp, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('LBP Image')

plt.show()
