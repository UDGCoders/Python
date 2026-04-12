import csv
import os
# import pandas as pd
# from pandas.errors import EmptyDataError

data = [["Name","Age"], 
        ["umair",20], 
        ]

with open("files/file.csv","w",newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("files/file.csv","r",newline='') as file:
    reader =csv.reader(file)
    for row in reader:
        print(f"{row} ")

# try:
#     reader = pd.read_csv("file.csv")
#     print(reader)
# except EmptyDataError:
#     print("No data is written in the file")
# except FileNotFoundError:
#     print("no found is found")
