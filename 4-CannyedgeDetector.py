import cv2
import numpy as np

image=cv2.imread("fig.jpeg")

if image is None:
    print("Error image not found")
    exit(1)
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)

edges=cv2.Canny(blurred,30,150)

edge = cv2.Canny(blurred, 100, 200)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.imshow('Canny Edge', edge)

    
    # Wait until a key is pressed and then close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()




















import cv2
import numpy as np

def main():
    # Load the image
    image = cv2.imread('fig.jpeg')
    if image is None:
        print("Error: Image not found")
        exit(1)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 100, 200)
    
    # Display the original and edge-detected images
    cv2.imshow('Original Image', image)
    cv2.imshow('Canny Edges', edges)
    
    # Wait until a key is pressed and then close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


