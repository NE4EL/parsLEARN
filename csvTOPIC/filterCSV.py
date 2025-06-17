import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

# 🔹 Фильтрация по условию:

df.dropna(inplace=True) # удаление пустой строки

print(df[df['age'] > 17])
print('--------------------')
print(df[df['grade'] >= 4.5])
print('--------------------')


# 🔹 Комбинирование условий:

print(df[(df['age'] > 17) & (df['grade'] >= 4.5)])
print('--------------------')
print(df[(df['name'] == 'Egor') | (df['name'] == 'Ivan')])
print('--------------------')

# 🔹 Сортировка:

df.sort_values('grade') # по возрастанию
df.sort_values('grade', ascending=False) # по убыванию