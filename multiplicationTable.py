#! python3
# multiplicationTable.py - This program takes a number, N, from command line
#   and creates an N x N multiplication table in an Excel sheet.

import openpyxl, sys

wb = openpyxl.Workbook()    # Create a new blank spreadsheet
sheet = wb['Sheet']

numIn = int(sys.argv[1])

# Set default values for the first row up to numIn (skipping the first cell)
for col in range(1, numIn+1):
    sheet.cell(row=1, column=col+1).value = col

# Set default values for the first column up to numIn (skipping the first cell)
for row in range(1, numIn+1):
    sheet.cell(row=row+1, column=1).value = row

# Do the maths
for i in range(1, sheet.max_row):
    for j in range(1, sheet.max_row):
        sheet.cell(row=i+1, column=j+1).value = i * j

wb.save('excel/' + str(numIn) + 'by' + str(numIn) + '.xlsx')
wb.close()
