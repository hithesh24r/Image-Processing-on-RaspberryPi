# importing all the required libraries
import cv2
import os
import numpy as np

# changing location to the given path
os.system("cd /home/pi")

# defining the destination path for the processed images
image_destination = "/home/pi/result/"

# Getting the name of the image file present in the current dircetory mentioned above i.e., /home/pi
image_name = input("Enter the image name with extension correctly (case-sensitive): ")

image = cv2.imread(image_name)    # reading image into the code using OpenCV
mkernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))    # Kernel used for morphological operations like erosion, dilation, opening, closing

# Defining functions for every operation seperately
def smoothen():
    output = smoothened_image = cv2.blur(image,(5,5))
    global output_path
    output_path = image_destination + "smoothened_" + image_name
    cv2.imwrite(output_path, output)

def sharpen():
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    output = sharpened_image = cv2.filter2D(image,-1,filter)
    global output_path
    output_path = image_destination + "sharpened_" + image_name
    cv2.imwrite(output_path, output)

def enhance_contrast():
    image = cv2.imread(image_name, 0)
    output = equi = cv2.equalizeHist(image)
    global output_path
    output_path = image_destination + "contrast-enhanced_" + image_name
    cv2.imwrite(output_path, output)

def erosion():
    output = erosion = cv2.erode(image,mkernel,iterations = 1)
    global output_path
    output_path = image_destination + "Eroded_" + image_name
    cv2.imwrite(output_path, output)

def dilation():
    output = dilation = cv2.dilate(image,mkernel,iterations = 1)
    global output_path
    output_path = image_destination + "Dilated_" + image_name
    cv2.imwrite(output_path, output)

def opening():
    output = opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, mkernel)
    global output_path
    output_path = image_destination + "opening_" + image_name
    cv2.imwrite(output_path, output)

def closing():
    output = closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, mkernel)
    global output_path
    output_path = image_destination + "closing_" + image_name
    cv2.imwrite(output_path, output)

# Asking the user to select the operation which they want to be performed on the image
operation = int(input("""
Enter the operation you would like to perfomr on the given image:
1. Smoothen the Image - Using Gaussian Blurring
2. Sharpen the Image - Using Laplacian Filter
3. Enhance the Contrast of the Image - Using Histogram Equilization
4. Thinning an Image - Morphological Erosion
5. Thickening an Image - Morphological Dilation
6. Eliminate protusions in the Original Image - Morphological Opening
7. Eliminate small holes from the Original Image - Morphological Closing
Enter your choice: """))

if operation == 1:
    smoothen()

elif operation == 2:
    sharpen()

elif operation == 3:
    enhance_contrast()

elif operation == 4:
    erosion()

elif operation == 5:
    dilation()

elif operation == 6:
    opening()

elif operation == 7:
    closing()

else:
    print("Enter correct input!!")

print(f"The image has been processed successfully!! You can find the resultant image at {output_path}")
