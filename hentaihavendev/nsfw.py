import random as r
import requests as s

def nsfw():
    a = r.randint(1,30)
    x = s.get("https://api.hentaihaven.dev/api.json").json()
    nsfw = print(x[str(a)])
    return nsfw