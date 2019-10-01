#! python3
# pdfParanoia.py - This program will go through every PDF in a folder and encrypt them 
#   using a password provided in the command line. The program also tests to make sure the
#   files were encrypted correctly.

import PyPDF2, os, sys

pdfFiles = []
folderPath = sys.argv[1]    # Get the directory to work in
password = sys.argv[2]  # Get the password to encrypt the PDFs with

# Find all PDF files in all subfolders of the given directory
for folderName, subFolders, filenames in os.walk(folderPath):

    for filename in filenames:
        if filename.endswith('.pdf'):
            absFilePath = os.path.join(folderName, filename)
            pdfFiles.append(absFilePath)

# Loop through all PDFs and encrypt them with given password (skip already encrypted PDFs)
for pdf in pdfFiles:
    
    pdfFileToCopy = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileToCopy)

    # Check to see encrypted status and skip if it is
    if (pdfReader.isEncrypted == True):
        print('File already encrypted.')
    else:
        pdfWriter = PyPDF2.PdfFileWriter()

        # Go through all the pages of the current PDF
        for pageNum in range(pdfReader.numPages):   
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

        splitFileName = pdf.split('.')  # Get the path with the already existing filename - the extension
        pathNeeded = splitFileName[0]      
        pdfWriter.encrypt(password)     # Encrypt file with password
        absNewPath = pathNeeded + '_encrypted.pdf' # Add new file name ending to file
        encryptedPdf = open(absNewPath, 'wb')   
        pdfWriter.write(encryptedPdf)
        encryptedPdf.close()

        # Check to see that the file was created successfully
        print(absNewPath)
        checkPdfReader = PyPDF2.PdfFileReader(open(absNewPath), 'rb')
        if (checkPdfReader.isEncrypted == True):
            print('New file encrypted.')
            print('Attempting to decrypt.')
            
            if (checkPdfReader.decrypt(password)):
                print('File decrypted!')

        # Delete unencrypted file

    
    pdfFileToCopy.close()
