import requests
r = requests.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
if r.status_code == 200:
    with open("data_txt.txt", "w") as file:
        