#!/usr/bin/env python3

# Imports
from PIL import Image
import os

for image in os.listdir("/home/student-03-eb25238b90e3/supplier-data/images/"):
  try:
    print(image)
    im = Image.open("/home/student-03-eb25238b90e3/supplier-data/images/"+image).convert("RGB")
    new_im = im.resize((600,400)).save("/home/student-03-eb25238b90e3/supplier-data/images/"+image[:-5]+".jpeg", format="JPEG")
  except:
    pass