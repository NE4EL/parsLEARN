from agent import headers
from bs4 import BeautifulSoup
import requests

url = "https://habr.com/ru/companies/selectel/articles/754674/"

req = requests.get(url, headers)
src = req.text

soup = BeautifulSoup(src, 'lxml')

rating_span = soup.find('span', {'data-test-id': 'votes-meter-value'})
if rating_span:
    rating = rating_span.get_text(strip=True)
    print(f"Оценка: {rating}")
else:
    print("Элемент с оценкой не найден")

