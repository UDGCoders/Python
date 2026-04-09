import os
folder_name = input("enter the name of folder you want to create")

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"folder {folder_name} has been created: ")
else:
    print(f"{folder_name} alreaady exists")