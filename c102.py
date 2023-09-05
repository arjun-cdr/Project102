import os
import sys
import shutil
#pip install pytest -shutil
from_path = "C:/Users/Arjun/Downloads"
to_path = "C:/Users/Arjun/Documents/WORK/Projects-professional/C102-project/"

file_list = os.listdir(from_path)
print(file_list)

for file_name in file_list:
    name, extention = os.path.splitext(file_name)
    print(name)
    print(extention)
    if extention == "":
        continue
    if extention in [".txt", ".pdf", ".docx", ".doc"] : 
        path1= from_path + '/' + file_name
        path2 = to_path + '/' + "document_files"
        path3 = to_path + '/' + "document_files" + "/" + file_name

        if os.path.exists(path2) :
            print("Moving file " + file_name + ".....")
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("Moving file " + file_name + ".....")
            shutil.move(path1,path3)
        
        