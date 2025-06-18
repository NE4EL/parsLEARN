from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://www.avito.ru"

# Настройки браузера
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Запуск Chrome
service = Service(ChromeDriverManager().install())
driver = wd.Chrome(service=service, options=options)

# Шаг 1: Перейти на главную Avito
driver.get(url)

# Шаг 2: Найти строку поиска
search_input = driver.find_element(By.CSS_SELECTOR,
                                   'input[data-marker="search-form/suggest/input"]')
search_input.send_keys("ноутбук")
search_input.send_keys(Keys.ENTER)

# Шаг 3: Подождать загрузку результатов
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-marker="item-title"]')))

# Шаг 4: Получить HTML и отдать BeautifulSoup
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

# Шаг 5: Найти заголовки объявлений
titles = soup.select('a[data-marker="item-title"]')

print("\n🔎 Найдено товаров:", len(titles))
print("📦 Заголовки:\n")

for title in titles:
    print("-", title.text.strip())