import os
from PyPDF2 import PdfReader

def show_files(dir):
    for (_,_,files) in os.walk(dir):
        print(files)


def get_pdf_text(pdf_docs):
    text = ""
    # for pdf in pdf_docs:
    pdfReader = PdfReader(pdf_docs)
    for pages in pdfReader.pages:
        text += pages.extract_text()

    return text

