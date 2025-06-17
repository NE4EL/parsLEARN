import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

# При работе с реальными данными часто встречаются:
# 	•	пропущенные значения (NaN, пустые ячейки),
# 	•	дубликаты строк,
# 	•	неверные типы данных.


# Проверка на пропуски:

print(df.isnull())
print(df.isnull().sum())

# Удаление строк с пропусками:

df.dropna(inplace=True)

# Замена пропусков:

df.fillna(0) # заменить на 0
df.fillna("Нет данных")  # заменить текстом

# Поиск и удаление дубликатов:

df.duplicated()           # логический массив
df.drop_duplicates()      # удалить повторы

# Изменение типов данных:

df['age'] = df['age'].astype(int)