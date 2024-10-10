import cv2

ref_point = []
cropping = False

def crop(event, x, y, flags, param):
    global ref_point, cropping, image

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            temp_image = image.copy()
            cv2.rectangle(temp_image, ref_point[0], (x, y), (0, 255, 0), 2)
            cv2.imshow("image", temp_image)
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

def crop_image(image, ref_point):
    if len(ref_point) == 2:
        x1, y1 = ref_point[0]
        x2, y2 = ref_point[1]
        cropped_image = image[y1:y2, x1:x2]
        return cropped_image
    else:
        return image

image = cv2.imread("fig.jpeg")
if image is None:
    print("Error: Image not found")
    exit(1)

clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", crop)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):
        image = clone.copy()
    elif key == ord("c"):
        break

if len(ref_point) == 2:
    cropimage = crop_image(clone, ref_point)
    cv2.imshow("cropped image", cropimage)
    cv2.waitKey(0)

cv2.destroyAllWindows()
