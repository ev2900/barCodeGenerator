#!/usr/bin/python

'''
Insturctions: 

    Run the code fomr the command line and pass the commmand the lowest number for
    for the bar codes to be generated and the highest number to be generated.

    ex.

        python barCodeGenerator.py 1 76     

Notes:

    You can fit a maximum of 76 bar codes on a single page
'''

# import
from reportlab.graphics.barcode import code39
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import sys

# arguments from the command line 
lowerRange = sys.argv[1]
upperRange = sys.argv[2]

#set file name and page size 
page = canvas.Canvas(lowerRange + "-" + upperRange + ".pdf", pagesize = A4)

#create an array with the numbers for the barcodes that should be on a page 
numerOfBarCodes = ((int(upperRange) - int(lowerRange)) + 1)
codeList = []
loopCounter = 0

while (loopCounter < numerOfBarCodes):
    codeList.append(str(int(lowerRange) + loopCounter)) 
    loopCounter = loopCounter + 1

#set the defulat position on the page for the first barcode
x = 1 * mm
y = 285 * mm
x1 = 6.4 * mm

for code in codeList:

    barcode = code39.Standard39(code, checksum=0)
    barcode.drawOn(page, x, y)
    x1 = x + 6.4 * mm
    y = y - 5 * mm
    page.drawString(x1, y, code)
    x = x
    y = y - 10 * mm

    if int(y) == 0:
        x = x + 50 * mm
        y = 285 * mm

page.showPage()
page.save()