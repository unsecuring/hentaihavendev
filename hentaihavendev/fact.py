import random as r
import requests as s

def fact():
    a = r.randint(1,26)
    x = s.get("https://api.hentaihaven.dev/factapi.json").json()
    fact = print(x[str(a)])
    return fact