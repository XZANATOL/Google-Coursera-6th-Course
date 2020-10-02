#! /usr/bin/env python3

# Imports
import os
import requests

# URL to send JSON
url = "http://localhost/fruits/"
for text in os.listdir("/home/student-03-eb25238b90e3/supplier-data/descriptions/"):
  dict_to_send = {}
  try:
    print(text)
    with open("/home/student-03-eb25238b90e3/supplier-data/descriptions/"+text, "r") as file:
      elements = file.readlines()
      dict_to_send["name"] = elements[0].rstrip("\n")
      dict_to_send["weight"] = int(elements[1][:-5])
      dict_to_send["description"] = " ".join(elements[2:]).replace("\n", "")
      dict_to_send["image_name"] = text[:-4]+".jpeg"
  except:
    pass

  send = requests.post(url, json=dict_to_send)
  print(text, str(send.status_code))
