#!/usr/bin/env python3

# Imports
import os
import requests

upload_url = "http://localhost/upload/"

for file in os.listdir("/home/student-03-eb25238b90e3/supplier-data/images/"):
  if file.endswith(".jpeg"):
    with open("/home/student-03-eb25238b90e3/supplier-data/images/"+file, "rb") as send:
      sender = requests.post(upload_url, files={"file": send})
    print(file, str(sender.status_code))