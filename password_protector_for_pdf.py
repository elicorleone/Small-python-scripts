from PyPDF2 import PdfReader, PdfWriter

pdf_writer = PdfWriter()
pdf_reader = PdfReader(r"C:\Users\Anders Falck\Desktop\Personbevis_Elis.pdf")

for page in pdf_reader.pages:
    pdf_writer.add_page(page)

password = "pepe@1234"
pdf_writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

with open('copy.pdf', 'wb') as f:
    pdf_writer.write(f)
