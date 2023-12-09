# run the command with python3 /path/to/pythonFile.py
# If this code is being run from a remote device using SSH, then use the following command
# "nohup python3 /path/to/python/file.py &" --> This will let the python script to be run in background
# This process takes more time so make sure to wait (it even may take 1-2 hours to complete the whole process)
# If "os.system("make -j$(nproc)")" is making some error, then change it to "make" and run
# This is more stable but takes more time to complete as it only uses one core

import os

commands1 = ["sudo su",
"apt install cmake build-essential pkg-config git -y",
"apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev -y",
"apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev -y",
"apt install libgtk-3-dev libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 -y",
"apt install libatlas-base-dev liblapacke-dev gfortran -y",
"apt install libhdf5-dev libhdf5-103 -y",
"apt install python3-dev python3-pip python3-numpy -y",
"nano /etc/dphys-swapfile"]

commands2 = ["sudo systemctl restart dphys-swapfile",
"git clone https://github.com/opencv/opencv.git",
"git clone https://github.com/opencv/opencv_contrib.git",
"mkdir /home/pi/opencv/build",
"cd /home/pi/opencv/build",
"cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=/home/pi/opencv_contrib/modules -D ENABLE_NEON=ON -D ENABLE_VFPV3=ON -D BUILD_TESTS=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D OPENCV_ENABLE_NONFREE=ON -D CMAKE_SHARED_LINKER_FLAGS=-latomic -D OPENCV_PYTHON_INSTALL_PATH=lib/python3.9/dist-packages -D BUILD_EXAMPLES=OFF ..",
"make -j$(nproc)",
"sudo make install",
"sudo ldconfig"]

for i in range(len(commands1)):
        os.system(commands1[i])

# If this part throws some error, then
## Go to /etc/dphys-swapfile and replace "CONF_SWAPSIZE=100" to "CONF_SWAPSIZE=2048"
## Then remove this block of code (from line 18 to line 23)
path = "/etc/dphys-swapfile"
with open(path, "r", encoding="utf-8") as file:
        data = file.readlines()
data[15] = "CONF_SWAPSIZE=2048"
with open(path, "w", encoding="utf-8") as file:
        file.writelines(data)

for i in range(len(commands2)):
        os.system(commands2[i])

# If this part throws some error, then
## Go to /etc/dphys-swapfile and replace "CONF_SWAPSIZE=2048" to "CONF_SWAPSIZE=100"
## Then remove this block of code
with open(path, "r", encoding="utf-8") as file:
        data = file.readlines()
data[15] = "CONF_SWAPSIZE=100"
with open(path, "w", encoding="utf-8") as file:
        file.writelines(data)

os.system("sudo systemctl restart dphys-swapfile")
