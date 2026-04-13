import os 
from bs4 import BeautifulSoup
import requests
import csv

for page in range(1,6):
    site_url=f"https://quotes.toscrape.com/page/{page}"

    print(f"Connecting to {site_url}")
    response=requests.get(site_url)
    if response.status_code == 200:
        print(f"Connected to site{site_url}")
        
    soup=BeautifulSoup(response.content,'html.parser')

    qoutes=soup.find_all('h2',class_='qoute')

    with 
