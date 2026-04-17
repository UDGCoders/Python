import csv
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code != 200:
    print("connection not established")
    exit()
else:
    print(f"connected to {url}")

soup = BeautifulSoup(response.content, 'html.parser')
quotes = soup.find_all('div', class_='quote')

# WRITE CSV
with open('files/file.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        writer.writerow([text, author])

# READ + ANALYZE
count = 0
authors = set()
author_count = {}

with open("files/file.csv", 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    next(reader)  # skip header

    for lines in reader:
        count += 1
        author = lines[1]

        authors.add(author)
        author_count[author] = author_count.get(author, 0) + 1

print(f"Total rows: {count}")
print(f"Unique authors: {len(authors)}")

print("\nTop Authors:")
for name, numbers in sorted(author_count.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"{name} → {numbers}")