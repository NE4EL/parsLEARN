# Иногда данные на сайте не оформлены таблицей (<table>),
# а размещены в других тегах — например:

# <div class="info">
#   <span class="label">Name:</span> Ivan
#   <br>
#   <span class="label">Age:</span> 21
# </div>

from bs4 import BeautifulSoup
import requests

url = "https://habr.com/ru/articles/541258/"
html = requests.get(url).text # получил html

soup = BeautifulSoup(html, 'html.parser') # Создал объект парсера:

# Извлечение данных по:

element = soup.find('div') # По тегу:
soup.find('div', class_='info') # По классу
soup.find_all('span', class_='label') # Все такие теги

print(element.text.strip())