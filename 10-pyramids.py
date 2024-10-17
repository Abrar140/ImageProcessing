import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_gaussian_pyramid(image, levels):
    gaussian_pyramid = [image]
    for i in range(levels):
        image = cv2.pyrDown(image)
        gaussian_pyramid.append(image)
    return gaussian_pyramid

def create_laplacian_pyramid(gaussian_pyramid):
    laplacian_pyramid = [gaussian_pyramid[-1]]
    for i in range(len(gaussian_pyramid) - 1, 0, -1):
        size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
        gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
        laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
        laplacian_pyramid.append(laplacian)
    return laplacian_pyramid

def show_pyramids(gaussian_pyramid, laplacian_pyramid):
    num_levels = len(gaussian_pyramid)
    plt.figure(figsize=(20, 10))
    
    for i in range(num_levels):
        # Display Gaussian Pyramid
        plt.subplot(2, num_levels, i + 1)
        plt.imshow(cv2.cvtColor(gaussian_pyramid[i], cv2.COLOR_BGR2RGB))
        plt.title(f'Gaussian Level {i}')
        plt.axis('off')
        
        # Display Laplacian Pyramid
        plt.subplot(2, num_levels, i + 1 + num_levels)
        laplacian_image = np.clip(laplacian_pyramid[i] + 128, 0, 255).astype(np.uint8)
        plt.imshow(cv2.cvtColor(laplacian_image, cv2.COLOR_BGR2RGB))
        plt.title(f'Laplacian Level {i}')
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    image_path = "images/sample.jpeg"
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return
    
    levels = 6  # Number of levels in the pyramid

    # Create Gaussian Pyramid
    gaussian_pyramid = create_gaussian_pyramid(image, levels)

    # Create Laplacian Pyramid
    laplacian_pyramid = create_laplacian_pyramid(gaussian_pyramid)

    # Show both pyramids on the same page
    show_pyramids(gaussian_pyramid, laplacian_pyramid)

if __name__ == "__main__":
    main()
