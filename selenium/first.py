# Для эмуляции работы браузера необходимо написать программу,
# которая будет как человек открывать нужные веб-страницы,
# взаимодействовать с элементами с помощью курсора,
# искать и записывать ценные данные.
# Такой алгоритм можно организовать с помощью библиотеки Selenium.

from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url = "https://habr.com/ru/search/"

options = Options()
options.add_argument('--headless')  # без окна браузера
options.add_argument('--disable-gpu')

service = Service(ChromeDriverManager().install())
driver = wd.Chrome(service=service, options=options)

driver.get(url)
print(driver.title)
driver.quit()