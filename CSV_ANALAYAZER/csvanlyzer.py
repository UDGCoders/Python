import os 
import csv
import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
response=requests.get(url)
if response.status_code != 200:
    print("connection not established")
else:
    print(f"connected to {url}")

soup = BeautifulSoup(response.content,'html.parser')
qoutes=soup.find_all('div',class_='quote')
count=0


with open('files/file.csv','w',newline='') as file:
    writer = csv.writer(file)
    for qoute in qoutes:
        text=qoute.find("span",class_="text").text.strip()
        author=qoute.find("small",class_="author").text.strip()
        writer.writerow([text,author])


with open("files/file.csv",'r',newline='') as file:
    reader = csv.reader(file)
    
    for lines in reader:       
        print(f"{count} {lines[1]} ")
        count = count + 1
print(count)