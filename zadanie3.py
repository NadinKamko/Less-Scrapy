from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

text = soup.find_all('span', class_='text')

print(text)

author = soup.find_all('small', class_='author')
print(author)
for i in range(len(text)):
     print(f"Цитата номер - {i + 1}")
     print(text[i].text)
     print(f"Автор цитаты - {author[i].text}\n")


