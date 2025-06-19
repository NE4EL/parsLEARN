import requests
from practic.agent import headers

req = requests.get("https://jsonplaceholder.typicode.com/posts", headers)
if req.status_code == 200:
    data = req.json()
    print(data)
else:
    print("Ошибка запроса:", req.status_code)