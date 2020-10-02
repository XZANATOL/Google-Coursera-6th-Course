#!/usr/bin/env python3

# Imports
import psutil
import requests

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

subject = ""
if int(psutil.cpu_percent(1)) > int(80):
  subject = "Error - CPU usage is over 80%"
elif (psutil.disk_usage('/').free / psutil.disk_usage('/').used * 100) < 20:
  subject = "Error - Available disk space is less than 20%"
elif (psutil.virtual_memory().free / 1024 / 1024) < 500:
  subject = "Error - Available memory is less than 500MB"
elif (requests.get("http://localhost").status_code) != 200:
  subject = "Error - localhost cannot be resolved to 127.0.0.1"

if subject == "":
  exit()
else:
  message = EmailMessage()

  recipient = "student-03-eb25238b90e3@example.com"
  sender = "automation@example.com"

  message['From'] = sender
  message['To'] = recipient
  message['Subject'] = subject
  message.set_content("Please check your system and resolve the issue as soon as possible.")

  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()