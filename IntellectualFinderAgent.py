!pip install PyPDF2

# importing required modules
import PyPDF2
source_pdf = '/content/drive/MyDrive/19690031454.pdf'
destination_pdf = '/content/drive/MyDrive/19690031454_annotation.pdf'
# creating a pdf file object
pdfFileObj = open(source_pdf, 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf file
maxPages = pdfReader.numPages
for i in range(maxPages):
    # creating a page object
    pageObj = pdfReader.getPage(i)
    # extracting text from page
    str = pageObj.extractText()
    index = str.find("Abstract")
    if index==-1:
        index = str.find("ABSTRACT")
    else:
        numPage = i
        break
    if index==-1:
        index = str.find("Notice")
    else:
        numPage = i
        break
    if index==-1:
        index = str.find("NOTICE")
    else:
        numPage = i
        break
    if index!=-1:
        numPage = i
        break
if index!=-1:
    print(numPage)
    # creating a pdf writer object for new pdf
    pdfWriter = PyPDF2.PdfFileWriter()
    # adding  page object to pdf writer
    pdfWriter.addPage(pageObj)
    # new pdf file object
    newFile = open(destination_pdf, 'wb')     
    # writing rotated pages to new file
    pdfWriter.write(newFile)  
    # closing the new pdf file object
    newFile.close()
# closing the original pdf file object
pdfFileObj.close()
