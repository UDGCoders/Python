import os

index=int(0)
source_dir="downloads/"

for filename in os.listdir(source_dir):
    if filename.endswith(".txt"):
        index=index+1
        print(f"{index} {filename} files exists")