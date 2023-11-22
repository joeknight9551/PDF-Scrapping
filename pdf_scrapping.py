import pytesseract
from pdf2image import convert_from_path
import re
import csv

def convert_pdf_to_txt_with_ocr(pdf_file_path):
    poppler_path = 'C:\\poppler-23.11.0\\Library\\bin'
    images = convert_from_path(pdf_file_path, poppler_path = poppler_path)

    text = ""
    for image in images:
        text += pytesseract.image_to_string(image, lang='eng')

    return text

# Usage example
pdf_file_path = './2023MSRBAFallWeb.pdf'
extracted_text = convert_pdf_to_txt_with_ocr(pdf_file_path)
# print(extracted_text)

# with open("2023MSRBAFallWeb.txt", 'x') as f:
#     f.write(extracted_text)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# Find matches
matches = re.findall(email_pattern, extracted_text)
if matches:
    matches = set(matches)
    for match in matches:
        print(match)
else:
    print("No email addresses found.")