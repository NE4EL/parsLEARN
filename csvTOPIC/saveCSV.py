import pandas as pd

data = {
    "Название": ["Lenovo IdeaPad", "MacBook Pro"],
    "Цена": ["47 000 ₽", "110 000 ₽"],
    "Ссылка": [
        "https://www.avito.ru/item1",
        "https://www.avito.ru/item2"
    ],
    "Город": ["Москва", "Санкт-Петербург"]
}

df = pd.DataFrame(data)
df.to_csv("save.csv", index=False, encoding="utf-8")

print(df.head())