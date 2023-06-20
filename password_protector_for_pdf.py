from PyPDF2 import PdfReader, PdfWriter

pdf_writer = PdfWriter()
pdf_reader = PdfReader(r"original.pdf") #the path of the original pdf

for page in pdf_reader.pages:
    pdf_writer.add_page(page)

password = "kjlakhsjkhde@1234"
pdf_writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

with open('copy.pdf', 'wb') as f: #creating copy of the original pdf
    pdf_writer.write(f)

   #Python script to copy a pdf file and encrypt it with password 
