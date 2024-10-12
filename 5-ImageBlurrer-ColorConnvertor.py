import cv2
import numpy as np
from matplotlib import pyplot as plt

def blurr(image):
    blurred_images=[]
     # Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)
    blurred_images.append(('Gaussian Blur', gaussian_blur))
    
    # Median Blur
    median_blur = cv2.medianBlur(image, 15)
    blurred_images.append(('Median Blur', median_blur))
    
    # Bilateral Filter
    bilateral_blur = cv2.bilateralFilter(image, 15, 75, 75)
    blurred_images.append(('Bilateral Blur', bilateral_blur))
    
    return blurred_images

def convertor(image, type):
     if type == 'RGB to HSV':
        return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
     elif type == 'RGB to LAB':
        return cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
     elif type == 'HSV to RGB':
        return cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
     elif type == 'LAB to RGB':
        return cv2.cvtColor(image, cv2.COLOR_LAB2RGB)
     else:
        raise ValueError("Invalid conversion type")


def displayimage(orignal,convertedimage,conversiontype, blurredimages):
    plt.figure(figsize=(20, 10))

    plt.subplot(2,4,1)
    plt.imshow(orignal)
    plt.title('Original Image')

    for i , (converted, convertedtype) in enumerate(zip(convertedimage,conversiontype),start=2):
        plt.subplot(2,4,i)
        plt.imshow(converted)
        plt.title(convertedtype)
    
    for i,(blurredtype, blurredimage) in enumerate(blurredimages,start=6):
        plt.subplot(2,4,i)
        plt.imshow(blurredimage)
        plt.title(blurredtype)


    plt.show()    
   


imagepath="./fig.jpeg"
image= cv2.imread(imagepath)
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
types=['RGB to HSV','RGB to LAB','HSV to RGB','LAB to RGB']
convertedimages=[convertor(image,types) for types in types]

blurredimages= blurr(image)
displayimage(image,convertedimages,types, blurredimages)







