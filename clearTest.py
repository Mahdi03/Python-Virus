import os
import shutil 
try:
    shutil.rmtree("test", ignore_errors=True, onerror=None)
    print("Clearing Folder test...")
except:
    pass
os.mkdir("test")
print("Folder test Cleared!!!")