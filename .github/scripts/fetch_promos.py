import requests, json, re, datetime, feedparser

promos = []

# 1. Żabka
rss = feedparser.parse("https://www.zabka.pl/pliki/rss/gazetka.xml")
for e in rss.entries:
    price = re.search(r'(\d+(?:[.,]\d+)?)\s*zł', e.title)
    disc  = re.search(r'(-\d+)%', e.title)
    if price and disc:
        promos.append({"shop":"Żabka","product":e.title,"price":float(price.group(1).replace(',','.')),"discount":int(disc.group(1))})

# 2. Carrefour
rss = feedparser.parse("https://carrefour.pl/gazetka/rss")
for e in rss.entries:
    price = re.search(r'(\d+(?:[.,]\d+)?)\s*zł', e.title)
    disc  = re.search(r'(-\d+)%', e.title)
    if price and disc:
        promos.append({"shop":"Carrefour","product":e.title,"price":float(price.group(1).replace(',','.')),"discount":int(disc.group(1))})

# 3. Intermarché
rss = feedparser.parse("https://intermarche.pl/gazetka/rss")
for e in rss.entries:
    price = re.search(r'(\d+(?:[.,]\d+)?)\s*zł', e.title)
    disc  = re.search(r'(-\d+)%', e.title)
    if price and disc:
        promos.append({"shop":"Intermarché","product":e.title,"price":float(price.group(1).replace(',','.')),"discount":int(disc.group(1))})

# 4. statyczne (już masz)
promos.extend([
    {"shop":"Biedronka","product":"Pierś z kurczaka 1 kg","price":9.99,"discount":-33},
    {"shop":"Lidl","product":"Czekolada Milka 100 g","price":2.99,"discount":-40},
    {"shop":"Kaufland","product":"Jogurt naturalny 400 g","price":1.69,"discount":-32},
    {"shop":"Aldi","product":"Pomidory malinowe 500 g","price":4.99,"discount":-29},
    {"shop":"Netto","product":"Mleko UHT 3,2 % 1 l","price":2.49,"discount":-22},
    {"shop":"Dino","product":"Płatki owsiane 500 g","price":2.99,"discount":-30}
])

print(f"Pobrano {len(promos)} promocji")

with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)
