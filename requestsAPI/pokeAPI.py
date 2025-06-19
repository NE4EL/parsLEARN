import requests
from practic.agent import headers

url = "https://pokeapi.co/api/v2/pokemon/1" # это один огромный файл про одного покемона
req = requests.get(url, headers)

if req.status_code == 200:
    data = req.json()
    name = data["name"]
    weight = data["weight"]
    poke_type = data["types"][0]["type"]["name"]

    print("Имя покемона:", name)
    print("Вес:", weight)
    print("Тип:", poke_type)

else:
    print("None")