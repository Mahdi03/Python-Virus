import os 
from random import randint
import random, string
import fnmatch

os.chdir("test")

def genRandDirs():
    i = randint(0, 1)
    j = randint(0, 1)
    k = randint(0, 1)
    
    if i == 1:
        createRandDir()
    elif i == 0:
        genRandDirs()
    if j == 1:
        createRandFile()
    elif j == 0:
        genRandDirs()
    if k == 1:
        changeDir()
    elif k == 0:
        genRandDirs()

def randomWord(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
def createRandDir():
    lenOfNameDir = randint(3, 20)
    nameDir = randomWord(lenOfNameDir)
    os.mkdir(nameDir)
    print("Created Directory: ", nameDir)
def createRandFile():
    # List Of Supported File Types - So Far...
    # Web Development
    listOfFileTypes = ['.txt', '.pdf', '.htm', '.html', '.xhtml', '.css', '.js', '.xml', '.xsl', '.php', '.phtml', '.sql']
    # Other Commonly Referenced Programming Languages
    listOfFileTypes.extend(['.c', '.cs', '.cpp', '.h', '.xaml', '.asm', '.py'])
    # Some Microsoft Office File Types
    listOfFileTypes.extend(['.accdb', '.mdb','.xls', '.xlsx', '.ppt', '.pptx', '.doc', '.docx'])
    fileExtensionUsed = listOfFileTypes[randint(0, len(listOfFileTypes) - 1)]
    print(fileExtensionUsed)
    lenOfNameFile = randint(3, 20)
    nameFile = str(randomWord(lenOfNameFile)) + str(fileExtensionUsed)
    newFile = open(nameFile, "w+")
    newFile.close()
    print(nameFile, " has just been created in", os.getcwd())
    genRandDirs()
def changeDir():
    availDirs = []
    print(len(availDirs))
    for i in os.listdir():
        if os.path.isdir(i):
            availDirs.extend([str(i)])
    a = randint(0, len(availDirs) - 2)
    os.chdir(availDirs[a])
    print("Available dirs:")
    print(availDirs)
    print("Current Dir:")
    print(os.getcwd())
    genRandDirs()

genRandDirs()