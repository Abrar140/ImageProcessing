import cv2
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def resize_image(imagepath,targetwidth=None , targetheight=None):
    image=cv2.imread(imagepath)
    if image is None:
        print(f"Error: Unable to load image from {imagepath}")
        return
    
    orignalheight, orignalwidth=image.shape[:2]

    if targetwidth is None and targetheight is None:
        raise ValueError("Either target_width or target_height must be specified.")

    if targetwidth is None:
        scalingfactor=targetheight/orignalheight
        targetwidth=int(orignalwidth*scalingfactor)
    elif targetheight is None:
        scalingfactor=targetwidth/orignalwidth
        targetheight=int(orignalheight*scalingfactor)
    else:
        widthscalingfactor=targetwidth/orignalwidth
        heightscalingfactor=targetheight/orignalheight
        scalingfactor=min(widthscalingfactor,heightscalingfactor)

        targetwidth=int(orignalwidth*scalingfactor) 
        targetheight=int(orignalheight*scalingfactor)
    
    resizedimage=cv2.resize(image,(targetwidth,targetheight), interpolation=cv2.INTER_AREA)
    return resizedimage


imagepath="fig.jpeg"
targetwidth=800
targetheight=600

# resizedimage=resize_image(imagepath,targetwidth,targetheight)

# if resizedimage is not None:
#     cv2.imshow("Resized Image", resizedimage)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

def loadimage():
    global imagepath, orignalimage, displayedimage
    imagepath = filedialog.askopenfilename()
    if imagepath:
        orignalimage = cv2.imread(imagepath)
        displayimage(orignalimage)

def displayimage(image):
    global displayedimage
    bgrimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Corrected here
    pilimage = Image.fromarray(bgrimage)
    displayedimage = ImageTk.PhotoImage(pilimage)
    image_label.config(image=displayedimage)
    image_label.image = displayedimage  # Keep a reference to avoid garbage collection

def flipimage(flipcode):
    if orignalimage is not None:
        flipped_image = cv2.flip(orignalimage, flipcode)
        displayimage(flipped_image)

def fliphorizontal():
    flipimage(1)

def flipvertical():
    flipimage(0)

def flipboth():
    flipimage(-1)

# Initialize the main window
root = tk.Tk()
root.title("Image Flipper")

# Initialize the original image variable
orignalimage = None
displayedimage = None

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()

# Create buttons for loading the image and flipping it
button_frame = tk.Frame(root)
button_frame.pack()

load_button = tk.Button(button_frame, text="Load Image", command=loadimage)
load_button.grid(row=0, column=0, padx=5, pady=5)

flip_horizontal_button = tk.Button(button_frame, text="Flip Horizontal", command=fliphorizontal)
flip_horizontal_button.grid(row=0, column=1, padx=5, pady=5)

flip_vertical_button = tk.Button(button_frame, text="Flip Vertical", command=flipvertical)
flip_vertical_button.grid(row=0, column=2, padx=5, pady=5)

flip_both_button = tk.Button(button_frame, text="Flip Both", command=flipboth)
flip_both_button.grid(row=0, column=3, padx=5, pady=5)

# Run the GUI event loop
root.mainloop()