from agent import headers
import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/companies/selectel/articles/754674/"
req = requests.get(url, headers)

src = req.text

# инициализируем html-код страницы
soup = BeautifulSoup(src, 'lxml')

# считываем заголовок страницы
title = soup.title.string

print(title)