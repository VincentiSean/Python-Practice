#! python3
# pdfDecrypt.py - This program decrypts all PDFs in a folder given in the command line.

import PyPDF2, os, sys

folderToSearch = sys.argv[1]
password = sys.argv[2]
pdfList = []

# Walk through the entire folder tree finding all PDFs and adding them to a list
for folderName, subFolders, filenames in os.walk(folderToSearch):
    for filename in filenames:
        if filename.endswith('.pdf'):
            filePath = os.path.join(folderName, filename)
            pdfList.append(filePath)

# Go through the list trying to decrypt all PDFs with the given password
for pdf in pdfList:

    pdfFileToDecrypt = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileToDecrypt)

    try:
        if (pdfReader.isEncrypted == True):
            pdfReader.decrypt(password)
            
            pdfWriter = PyPDF2.PdfFileWriter()

            # Go through all the pages of the current PDF
            for pageNum in range(pdfReader.numPages):   
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

            splitFileName = pdf.split('_')  # Get the path with the already existing filename - the extension
            pathNeeded = splitFileName[0]      
            absNewPath = pathNeeded + '.pdf' # Add new file name ending to file
            decryptedPdf = open(absNewPath, 'wb')   
            pdfWriter.write(decryptedPdf)
            decryptedPdf.close()
    except Exception as exc:
        print('Wrong password!')