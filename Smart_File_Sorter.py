import os 
import shutil

source_dir=input("Enter the directory path:  ")

file_type={
    "images/jpeg":[".jpeg",'.jpg','.png'],
    # "images/png":".png",
    # "images/jpg":".jpg",
    "zipped":[".zip"],
    "text":[".txt"],
    "pdf":[".pdf"],

}

moved_files = False
moved_files_list=[]
count = 0
summary={}


for filename in os.listdir(source_dir):
    full_path=os.path.join(source_dir,filename)
    if  os.path.isdir(full_path):
        continue
    for key, value in file_type.items():
        # print(f"{value}, {key}")
        if filename.lower().endswith(value):
            final_path=os.path.join(source_dir,key)
            os.makedirs(final_path,exist_ok=True)
            # print(final_path)
            shutil.move(full_path,os.path.join(final_path,filename))
            moved_files=moved_files+1
            moved_files_list.append(value)
            print(f"{moved_files} of type {value} has been moved to {key}")
            break

        if not moved_files:
            other_path = os.path.join(source_dir,'Others')
            count = count+1
            shutil.move(full_path,os.path.join(other_path,filename))
            
# for folder,counts