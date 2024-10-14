import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# Replace with the absolute path to your image file
image_path = r'e:\trial\Python files\fig.jpeg'

# Check if the image file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file not found at {image_path}")

# Load the image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    raise ValueError(f"Failed to load image from {image_path}")

# Apply global thresholding (binary)
# cv2.threshold(source_image, threshold_value, max_value, thresholding_type)
# source_image: input image
# threshold_value: the value used to classify the pixel values
# max_value: the value to be given if the pixel value is more than the threshold value
# thresholding_type: type of thresholding (e.g., cv2.THRESH_BINARY)
_, binary_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Apply adaptive thresholding (mean)
# cv2.adaptiveThreshold(source_image, max_value, adaptive_method, thresholding_type, block_size, C)
# source_image: input image
# max_value: the value to be given to the pixel if the condition is satisfied
# adaptive_method: adaptive thresholding algorithm to use (e.g., cv2.ADAPTIVE_THRESH_MEAN_C)
# thresholding_type: type of thresholding (e.g., cv2.THRESH_BINARY)
# block_size: size of the neighborhood area used to calculate the threshold value
# C: constant subtracted from the mean or weighted sum of the neighborhood pixels
adaptive_thresh_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                             cv2.THRESH_BINARY, 11, 2)

# Apply adaptive thresholding (Gaussian)
adaptive_thresh_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                 cv2.THRESH_BINARY, 11, 2)

# Apply Otsu's thresholding
# Otsu's thresholding automatically determines the optimal threshold value
# cv2.threshold(source_image, threshold_value, max_value, thresholding_type)
# source_image: input image
# threshold_value: initial threshold value (ignored when using Otsu's method)
# max_value: the value to be given if the pixel value is more than the threshold value
# thresholding_type: type of thresholding (e.g., cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Plotting the images
titles = ['Original Image', 'Binary Thresholding', 'Adaptive Mean Thresholding', 
          'Adaptive Gaussian Thresholding', 'Otsu\'s Thresholding']

images = [image, binary_thresh, adaptive_thresh_mean, adaptive_thresh_gaussian, otsu_thresh]

plt.figure(figsize=(10, 10))
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
