#!/usr/bin/python3
# Developed by XZANATOL

# Imports
import os
from PIL import Image as image # Install package using "pip3 install Pillow"

def list_dir():
    """Returns the list of images folder"""
    return os.listdir("images/")


# Execution begins here
if __name__ == '__main__':
    dir = list_dir()

    # Loop through each file and edit (IF it was an image)
    for i in dir:
        try:
            # Note .tiff saves image in CYMK color format while .jpg/.jpeg saves image in RGB color format
            Image = image.open("images/" + i).convert("RGB")
        except:
            continue
        print(i)
        new_image = Image.rotate(-90).resize((128,128)).save("/opt/icons/"+i, format="JPEG")
