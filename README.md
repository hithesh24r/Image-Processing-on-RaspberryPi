# IP-on-RPI
Image Processing on Raspberry Pi 4 using OpenCV v2 and Python coding on Raspberry Pi 4 Model B:

**What this can do:**
- This code can perform the following operations:
    1. Smoothen the Image - Using Gaussian Blurring
    2. Sharpen the Image - Using Laplacian Filter
    3. Enhance the Contrast of the Image - Using Histogram Equilization
    4. Thinning an Image - Morphological Erosion
    5. Thickening an Image - Morphological Dilation
    6. Eliminate protusions in the Original Image - Morphological Opening
    7. Eliminate small holes from the Original Image - Morphological Closing
- It can also send the output to cloud (AWS S3) and email the output based on users' choice


**Steps to be followed before the installation process:**
- Write the Raspbian Lite image onto a sd card through the Laptop
- Insert the SD card into the raspberry pi and boot up the Pi
- make the initial updates and upgrades to the Raspbian Lite OS using the command "sudo apt update && sudo apt upgrade -y"
- Then choose any the following ways and go on with the respective procedure
    1. Basic Image Processing using OpenCV on Raspberry Pi
    2. Image Processing with cloud (Amazon S3) Integration using Raspberry Pi
    3. Image Processing with email feedback
    4. Image Processing with both Cloud Integration and email feedback



**1. Basic Image Processing using OpenCV on Raspberry pi:**
  - Install OpenCV using the python script in the repository
  - Run the script directly to get the required output

**2. Image Processing with cloud (Amazon S3) Integration using Raspberry Pi**
  - Install OpenCV using python script in the repository
  - Create a bucket in Amazon S3
  - Run the script file for AWS S3 and RPi synchronization with the changed values to variables
  - Then run the script with cloud integration to see the output in the S3 Bucket created

**3. Image Processing with email feedback**
**4. Image Processing with both Cloud Integration and email feedback**
