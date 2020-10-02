#!/usr/bin/env python3

# Imports
import reports
import os
import datetime
import emails

if __name__ == "__main__":
  path = "/home/student-03-eb25238b90e3/supplier-data/descriptions/"
  paragraph = []
  for file in os.listdir(path):
    with open(path+file, "r") as text:
      txt = text.readlines()
      paragraph.append("name: "+txt[0].rstrip("\n"))
      paragraph.append("weight: "+txt[1].rstrip("\n")+"<br/>")

  paragraph = "<br/>".join(paragraph)
  attachment = "/tmp/processed.pdf"
  title = "Processed Update on " + str(datetime.date.today().strftime("%B %d, %Y"))

  reports.generate_report(attachment, title, paragraph)


  email = emails.generate_email()
  emails.send_email(email)
