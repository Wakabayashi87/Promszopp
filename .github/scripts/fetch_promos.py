import requests, csv, json, datetime

url = "https://raw.githubusercontent.com/kuba-moo/promos-demo/main/promos.csv"
promos = []

try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    for row in csv.DictReader(r.text.splitlines()):
        promos.append({
            "shop":    row["shop"],
            "product": row["product"],
            "price":   float(row["price"]),
            "discount": int(row["discount"])
        })
except Exception as e:
    print("Błąd pobierania CSV:", e)

# zawsze zapisujemy coś (nawet pustą listę)
with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)

print("Wgrano", len(promos), "promocji")
