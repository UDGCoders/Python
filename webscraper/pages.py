import requests
from bs4 import BeautifulSoup
import csv

with open('files/loop.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])

    for page in range(1, 6):
        url = f"https://quotes.toscrape.com/page/{page}/"
        print(f"Connecting to {url}")

        response = requests.get(url)

        if response.status_code != 200:
            print("Failed to connect")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            text = quote.find('span', class_='text').text.strip()
            author = quote.find('small', class_='author').text.strip()

            writer.writerow([text, author])

print("All data saved successfully")