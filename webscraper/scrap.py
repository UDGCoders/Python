import requests
from bs4 import BeautifulSoup
import csv

site_link='https://quotes.toscrape.com/'
print('coneecting')
response = requests.get(site_link)
if response.status_code == 200:
    print('connected to site')
else:
    print('request denited')
    exit()

soup=BeautifulSoup(response.content,'html.parser')
# soup = BeautifulSoup

# data_list = []
qoutes_list=[]
author_list=[]
# titles=soup.find_all('h2')
qoutes = soup.find_all('span',class_='text')
author = soup.find_all('small',class_='author',itemprop='author')

# for item in titles:
    # data_list.append(item.text.strip())

for item in author:
    print(item)
    author_list.append(item.text.strip())

for qoute in qoutes:
    qoutes_list.append(qoute.text.strip())
    # print(qoute)


with open('scraping.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Titles','Author'])
    for item in qoutes_list:
        # print(item)
        writer.writerow([item,author])
        # print(f'{author} {item}')
