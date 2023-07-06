import PyPDF2
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f)
print(len(pdf_reader.pages))
page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
print(page_one_text)
f.close()

f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter()
print(type(first_page))
pdf_writer.add_page(first_page)
pdf_output = open('some_BrandNew_Doc.pdf','wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

f = open('Working_Business_Proposal.pdf','rb')

pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())
print(pdf_text[1])