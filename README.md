# Python-Virus
Welcome to Python Virus!! This is a beginner project of mine that involves ***as much code as possible only from Python's Core***.

*No external dependencies!!!*

The goal of this virus is to find *all* recognizable file types in the *top-most* directory and change their content to a designated file made by me.

There is a `virus.py` Python File, this is the main file that acts as a virus.

Above it, there are 2 files that have titles of **md5 Hashes**.
## Extra Files:
* `bf72dda9b27c0fb1f16fc6648348228d.py` is an md5 Hash for `hackedCode` + `.py`:
	* This file was manually created by me.
	* This Python file has no code, ***it only stores variables***.
* `d82b5a265ef9e1c62e6fe52a3613b288.txt` is an md5 Hash for `listOfAvailDirsTXTFile` + `.txt`:
	* This file is auto-generated by `virus.py` and is **by far** the **largest file** in this project.
	* If you try to remove the file, it will automatically regenerate itself the next time `virus.py` is run.
		* To get rid of it:
			1. **Remove all Python code in `virus.py` that pertains to `d82b5a265ef9e1c62e6fe52a3613b288.txt`**.
			1. Then feel free to **remove `d82b5a265ef9e1c62e6fe52a3613b288.txt` for good**.
	* This file is ***only for testing purposes*** to see how the files and their directories are stored.
	* Of course, it's better to get rid of the file for production.
	* This file shows how the directories and the file locations are stored. ***Please feel free to point out a better way of storing such information***
	* Right now, the information is stored in multiple lists as `key, value` pairs.
* `genRandDirs.py`:
	* This file was manually created by me.
	* This file is also not necessary to the project, however, it is used for testing the `virus.py` file.
	* This file generates random files and folders inside the `test` folder, so that later on, ***any damage created by `virus.py` only harms the automatically generated files***, which can be later erased and re-created using the same script (`genRandDirs.py`).
	* When running this file, you will come across certain errors. Just exit and run the file again. No need to try and fix the script. However, feel free to try and fix it!!!
	* You can keep running the script until you are satified with the amount of files and folders.
		*  **Running this file 3-4 times will create about 3,000 files, at least for me!!**
* And of course, ***I HOPE THIS FILE NEVER GOES INTO PRODUCTION***
* If it does, ***I AM NOT RESPONSIBLE for any damage caused by this project.***
* # ***THIS PROJECT IS INTENDED FOR LEARNING PURPOSES ONLY!!!***

## `test` Directory:
Under the `test` directory, you will find a bunch of randomly genereated files by `genRandDirs.py`.

***FEEL FREE TO DELETE THEM AND RUN `genRandDirs.py` OVER AND OVER AGAIN 'TILL SATISFIED.***
#### Note: Sometimes `genRandDirs.py` runs into errors about too many files, don't worry about that,just keep running it until you are satisfied with the files and directories generated. 