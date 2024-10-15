import cv2
import numpy as np
from matplotlib import pyplot as plt

def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image not found or unable to read")
    return image

def apply_erosion(image, kernel_size=5, iterations=1):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    eroded_image = cv2.erode(image, kernel, iterations=iterations)
    return eroded_image

def apply_dilation(image, kernel_size=5, iterations=1):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=iterations)
    return dilated_image

def apply_opening(image, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opened_image

def apply_closing(image, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closed_image

def display_images(original, eroded, dilated, opened, closed):
    titles = ['Original Image', 'Eroded Image', 'Dilated Image', 'Opened Image', 'Closed Image']
    images = [original, eroded, dilated, opened, closed]

    for i in range(5):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    # Load the image
    image_path = './fig.jpeg'  # Replace with the path to your image
    image = load_image(image_path)

    # Apply morphological operations
    eroded_image = apply_erosion(image)
    dilated_image = apply_dilation(image)
    opened_image = apply_opening(image)
    closed_image = apply_closing(image)

    # Display the results
    display_images(image, eroded_image, dilated_image, opened_image, closed_image)
