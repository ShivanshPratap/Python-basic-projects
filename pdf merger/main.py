#pip install pypdf2

import PyPDF2

pdfiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        pdfMerge.append(pdfReader)

pdfFile.close()
pdfMerge.write('merged.pdf')