# import os
# folder_name = input("enter the name of folder you want to create")

# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)
#     print(f"folder {folder_name} has been created: ")
# else:
#     print(f"{folder_name} alreaady exists")

# creating for file arranging using python script

import os
import shutil

source_dir=input("Enter the path you want to arrange")

images = os.path.join(source_dir,"images/") 
pdf = os.path.join(source_dir,"pdf/")
txt = os.path.join(source_dir,"text/") 
packed = os.path.join(source_dir,"zipped/")

os.makedirs(images,exist_ok=True)
os.makedirs(pdf,exist_ok=True)
os.makedirs(txt,exist_ok=True)
os.makedirs(packed,exist_ok=True)

for filename in os.listdir(source_dir):
    if os.path.isdir(os.path.join(source_dir,filename)):
        continue
    if filename.endswith(".jpeg"):
        # print(f"{filename} with jpg found")
        images=os.path.join(source_dir,"images/jpeg")
        os.makedirs(images,exist_ok=True)
        shutil.move(os.path.join(source_dir,filename),os.path.join(images,filename))
    elif filename.endswith(".jpg"):
        # print("image found")
        images=os.path.join(source_dir,"images/jpg")
        os.makedirs(images,exist_ok=True)
        shutil.move(os.path.join(source_dir,filename),os.path.join(images,filename))
    elif filename.endswith(".png"):
        images=os.path.join(source_dir,"images/png")
        os.makedirs(images,exists_ok=True)
        shutil.move(os.path.join(source_dir,filename),os.path.join(images,filename))
    elif filename.endswith(".zip"):
        images=os.path.join(source_dir,"zip")
        os.makedirs(packed,exist_ok=True)
        shutil.move(os.path.join(source_dir,filename),os.path.join(images,filename))
    else:
        print(f"{filename} \n nothing will change about it")

