import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('./fig.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display the original and equalized images using matplotlib
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

# Calculate and plot the histogram for the original image
plt.subplot(2, 2, 3)
plt.title('Histogram of Original Image')
plt.hist(image.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
plt.xlim([0, 256])

# Calculate and plot the histogram for the equalized image
plt.subplot(2, 2, 4)
plt.title('Histogram of Equalized Image')
plt.hist(equalized_image.ravel(), bins=256, range=[0, 256], color='green', alpha=0.7)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
