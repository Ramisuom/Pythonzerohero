#PDFs and Spreadsheets Puzzle Exercise

#You will need to work with two files for this exercise and solve the following tasks:

#Task One: Grab the Google Drive Link from .csv File
import csv

data = open('Excercise_Files/find_the_link.csv',encoding='utf-8')
csv_data = csv.reader(data)

data_lines = list(csv_data)
print(data_lines[0])

link_str = ''

for row_num,data in enumerate(data_lines):

    link_str += data[row_num]
print(link_str)


#Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.
import PyPDF2
f = open('Excercise_Files/Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfReader(f)
print(pdf.pages)

import re
pattern = r'\d{3}.\d{3}.\d{4}'
all_text = ''

for n in range(pdf.pages):
    page = pdf.pages(n)
    page_text = page.extract_text()

    all_text = all_text+' '+page_text

for match in re.finditer(pattern,all_text):
    print(match)
all_text[41790:41808+20]