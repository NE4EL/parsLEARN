# Умение читать csv файлы
# CSV (Comma-Separated Values) — формат хранения табличных данных.
# Он широко используется, особенно при экспорте данных из Excel, Google Таблиц и баз данных.
# В Python для работы с CSV-файлами чаще всего используют:

# 🔹 Пример с csv.reader:

# with open('data.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# 🔹 Пример с pandas:

import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())