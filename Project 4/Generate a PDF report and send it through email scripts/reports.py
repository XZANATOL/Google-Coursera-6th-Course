#!/usr/bin/env python3

# Imports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
  file = SimpleDocTemplate(attachment)
  styles = getSampleStyleSheet()
  file_title = Paragraph(title, styles["h1"])
  file_br = Paragraph("<br/><br/>")
  file_par = Paragraph(paragraph)

  file.build([file_title, file_br, file_par])
