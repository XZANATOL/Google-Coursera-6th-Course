#! /usr/bin/env python3
# Coursera Project 2
# Developed by XZANATOL

# Imports
import os
import requests

def get_reqquest_dictionary(file):
    """Returns a parsed dictionary of the feedback text file"""
    with open(file, "r") as file:
        # Read all lines and remove \n character
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip("\n")

        return {"title": lines[0], "name": lines[1], "date": lines[2], "feedback": " ".join(lines[3:])}

def send_request(dict):
    """Send the dictionary to the Django webserver"""
    response = requests.post("http://<corpweb-external-IP>/feedback/", json=dict) # Replace <corpweb-external-IP> by the ip address of the machine

    if not response.ok:
        print("[-] send failed with status code", response.status_code)
    else:
        print("[+] send succeeded with status code", response.status_code)

# Execution begins here
if __name__ == '__main__':

    #Debug output (name of file. dictionary parse, send status code) else can't open name of file

    for i in os.listdir("/data/feedback/"):
        try:
            dict_to_send = get_reqquest_dictionary("/data/feedback/"+i)
            print("")
            print(i, "\n", dict_to_send)
            send_request(dict_to_send)
        except:
            print("\ncan't open", i)

# IT WORKED FROM THE FIRST SUBMIT WOOHOO!, just make sure you name the file "run.py" cuz i submitted it with name "send.py" till i noticed this error...