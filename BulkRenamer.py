import os
import shutil

counter=1
source_dir=input("enter the folder path:  ")

for filename in os.listdir(source_dir):
    if filename.endswith(".pdf"):
        old_path=os.path.join(source_dir,filename)

        new_name=f"file_{counter}.pdf"
        new_path=os.path.join(source_dir,new_name)

        os.replace(old_path,new_path)
        print(f"{filename} is replaced")
        counter = counter+1
    else:
        print("no file found")