# Execute All Code
try:

    import os 
    from random import randint
    import random, string
    import fnmatch

    # Change Directory To "test" (where files and folders will be generated)
    os.chdir("test")


    # Create Main Function That Creaates Random Files And Folders
    def genRandDirs():
        # Create 3 Random Numbers (pretty much True or False!!!)
        i = randint(0, 1)
        j = randint(0, 1)
        k = randint(0, 1)
        # Use Previously Created Random Numbers To Decide Whether Or Not To
        # a. Create A Random Folder (Most Probable For Some Reason)
        # b. Create A Random File (Happens On A Normal Basis)
        # c. Change To A Randomly Created Folder To Put In More Random Files And Folders! (least probable)
        # If It Doesn't Call any External Functions, Then It Just Runs Again Until An Error
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
    # Global Function To Create Random String In Lowercase Letters With A Specified Length
    def randomWord(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))
    # External Function To Create A Randomly Named Folder
    def createRandDir():
        # Randomize Length Of Random String (Word)
        lenOfNameDir = randint(3, 20)
        # Reuse Previously Defined Global randomWord() Function
        nameDir = randomWord(lenOfNameDir)
        # Actually Create The Folder With The Randomized Name
        os.mkdir(nameDir)
        # Just For Testing Use: Prints Status
        print("Created Directory: ", nameDir)
    # External Function To Create A Randomly Named File With A Random File Type
    def createRandFile():
        # Create List Of File Types To Randomly Choose From Later
        # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        # List Of Supported File Types - So Far...
        # Web Development
        listOfFileTypes = ['.txt', '.pdf', '.htm', '.html', '.xhtml', '.css', '.js', '.xml', '.xsl', '.php', '.phtml', '.sql']
        # Other Commonly Referenced Programming Languages
        listOfFileTypes.extend(['.c', '.cs', '.cpp', '.h', '.o', '.exe', '.xaml', '.asm', '.py'])
        # Some Microsoft Office File Types
        listOfFileTypes.extend(['.accdb', '.mdb','.xls', '.xlsx', '.ppt', '.pptx', '.doc', '.docx'])
        # Randomly Choose Which File Type/Extension To Use In Randomly Created File
        fileExtensionUsed = listOfFileTypes[randint(0, len(listOfFileTypes) - 1)]
        # Just For Testing Use: Prints File Extension Used
        print(fileExtensionUsed)
        # Randomize Length Of Random String (Word)
        lenOfNameFile = randint(3, 20)
        # Reuse Previously Defined Global randomWord() Function And Already Pre-Chosen File Type To Use
        nameFile = str(randomWord(lenOfNameFile)) + str(fileExtensionUsed)
        # Actually Create The File With The Randomized Name And File Type And Then Close It
        newFile = open(nameFile, "w+")
        newFile.close()
        # Just For Testing Use: Prints Status
        print(nameFile, " has just been created in", os.getcwd())
        # Run Main Function Again (Endless Loop?)
        genRandDirs()
    # External Function To Change Into A Randomly Created Folder To Populate It With More Files And Folders
    def changeDir():
        # Initialize Temporary Var
        availDirs = []
        # Check All Available Paths In The Current Directory
        for i in os.listdir():
            # If The Path Currently Being Checked Is A Folder,
            if os.path.isdir(i):
                # Then Add It To The Previoulsy Initialized Temporary Var
                availDirs.extend([str(i)])
        # Choose Randomly The Number Of The Folder To Be Switching To
        a = randint(0, len(availDirs) - 2)
        # Actually Opening The Folder
        os.chdir(availDirs[a])
        # Prints: Status
        print("Available dirs:")
        print(availDirs)
        print("Current Dir:")
        print(os.getcwd())
        genRandDirs()

    # Start The Program By Calling The Main Function Once
    genRandDirs()
# If The Code Fails By Any Chance:
except:
    import sys
    # Go Back To The Original Directory
    os.chdir("..")
    # Exit Program Instead Of Running In An Endless Loop
    sys.exit()
    pass