exec(open("clearTest.py", "r").read())
for i in range(5):
    try:
        exec(open("genRandDirs.py", "r").read())
        print(i)
    except:
        pass
print("Starting Up The Virus!!!!!")
import os
print(os.getcwd())
exec(open("virus.py", "r").read())