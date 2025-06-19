import requests
import pandas as pd

from practic.agent import headers

base_url = "https://pokeapi.co/api/v2/pokemon?limit=10"

req = requests.get(base_url, headers)
if req.status_code != 200:
    print("Ошибка загрузки списка покемонов")
    exit()

pokemon_list = req.json()["results"]
data = []

for poke in pokemon_list:
    url = poke["url"]

    p = requests.get(url, headers)
    if p.status_code != 200:
        continue

    info = p.json()

    name = info["name"]
    weight = info["weight"]
    poke_type = info["types"][0]["type"]["name"] if info["types"] else "–"

    data.append({
        "Name": name.title(),
        "Weight": weight,
        "Type": poke_type.title()
    })

df = pd.DataFrame(data)
df.to_csv("pokemon.csv", index=False, encoding="utf-8")
read = pd.read_csv("pokemon.csv")
print(read)