import PyPDF2
pdfFileobj = open('guoyan.pdf','rb')
reader = PyPDF2.PdfFileReader(pdfFileobj)
pages = []
for i in range(0,reader.numPages):
    page = reader.getPage(i)
    pages.append(page.extractText())
print(pages)
