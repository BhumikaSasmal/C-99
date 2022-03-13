import os
import shutil
source = input("Enter source Folder name: ")
destination = input("Enter Destination Folder Name: ")
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)