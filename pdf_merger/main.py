# here we are merging 3 pdf here

import PyPDF2                                       # these file require to merge pdfs

all_pdf_files = ["simple_pdf4.pdf","simplepdf2.pdf","simplepdf1.pdf"]

merge_pdf = PyPDF2.PdfMerger()                                       # pdfmerger objct

for pdf in  all_pdf_files :
    all_pdf_files = open(pdf ,"rb")

    pdf_read =PyPDF2.PdfReader(all_pdf_files)         # it will read all file
    merge_pdf.append(pdf_read)                          # it will merge all file and append

all_pdf_files.close()
merge_pdf.write("three_pdf_merge.pdf")                                    # assinge a new pdf name  for  all merge pdf 