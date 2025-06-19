import requests
from practic.agent import headers

req = requests.get("https://jsonplaceholder.typicode.com/posts", headers)
posts = req.json()

for post in posts[:5]: # первые пять посты
    print(post["title"])
