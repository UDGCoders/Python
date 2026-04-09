import os
import shutil
# folder_name = input("enter the name of folder you want to create")
# if not os.path.exists(folder_name):
    # os.makedirs(folder_name)
    # print(f"folder {folder_name} has been created: ")
# else:
    # print(f"{folder_name} alreaady exists")

source_dir="downloads/"

target_images="images/"
target_pdf="pdf/"
target_txt="txt/"

os.makedirs(target_images,exist_ok=True)
os.makedirs(target_pdf,exist_ok=True)
os.makedirs(target_txt,exist_ok=True)

for filename in os.listdir(source_dir):
    if filename.endswith(".jpg"):
        shutil.move(os.path.join(source_dir,filename),os.path.join(target_images,filename))
        print("image is moved")
    elif filename.endswith(".pdf"):
        shutil.move(os.path.join(source_dir,filename),os.path.join(target_pdf,filename))
        print("pdf is moved")
    elif filename.endswith(".txt"):
        shutil.move(os.path.join(source_dir,filename),os.path.join(target_txt,filename))
        print("text file is moved")
    else:
        print("Cant move the directory")
