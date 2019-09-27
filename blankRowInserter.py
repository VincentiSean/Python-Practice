#! python3
# blankRowInserter.py - This program takes two numbers (N && M) and a file name 
#   when it runs and adds M number rows starting at row N in the file.

import openpyxl, sys, os

insertLocation = sys.argv[1]
numRowsToInsert = sys.argv[2]
fileToEdit = sys.argv[3]

wb = openpyxl.load_workbook(fileToEdit) # Get the file to edit
sheet = wb.active

# Loop through the original file until the row that will have the added rows
for i in range(int(numRowsToInsert)):
    sheet.insert_rows(int(insertLocation))

newFilename = os.path.basename(fileToEdit)
wb.save('excel/edited' + newFilename)
wb.close()