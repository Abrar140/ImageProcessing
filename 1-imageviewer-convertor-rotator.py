import cv2

def rotateimage(imagepath, angle):
    image = cv2.imread(imagepath)

    # Check if the image was successfully loaded
    if image is None:
        print("Could not open or find the image")
        return None

    (h, w) = image.shape[:2]
    print(h, w)

    center = (w // 2, h // 2)
    print(center)

    Matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    rotatedimage = cv2.warpAffine(image, Matrix, (w, h), borderMode=cv2.BORDER_REPLICATE)

    return rotatedimage

rotatedimage = rotateimage("1-textimage.jpeg", 90)

# Check if rotated image is None
if rotatedimage is None:
    exit(0)

# Display the rotated image
cv2.imshow("Rotated Image", rotatedimage)

# Convert to grayscale
grayscaleimage = cv2.cvtColor(rotatedimage, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray scale Image", grayscaleimage)

cv2.waitKey(0)
cv2.destroyAllWindows()
