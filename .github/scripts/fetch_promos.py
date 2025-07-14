import json, random, datetime

shops = ["Biedronka","Lidl","Żabka","Aldi","Kaufland","Netto","Dino"]
products = [
    "Mleko UHT 1 l","Czekolada 100 g","Jogurt 400 g","Chleb 500 g","Jajka 10 szt.",
    "Masło 200 g","Pomidory 500 g","Makaron 500 g","Serek wiejski 150 g","Płatki owsiane 500 g",
    "Ziemniaki 2 kg","Banany 1 kg","Ser żółty 200 g","Woda gazowana 1,5 l","Herbata 50 g"
]

promos = []
for p in products:
    price = round(random.uniform(1.50, 12.00), 2)
    discount = -random.randint(15, 45)
    promos.append({
        "shop": random.choice(shops),
        "product": p,
        "price": price,
        "discount": discount
    })

with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)

print("Wygenerowano", len(promos), "promocji")
