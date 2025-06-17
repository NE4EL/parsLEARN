import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
tables = pd.read_html(url)

print(f"Найдено таблиц: {len(tables)}")
df = tables[0] # первая таблица
print(df.head())