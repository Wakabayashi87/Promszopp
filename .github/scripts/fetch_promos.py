import json, random, datetime

# pełna lista 50 produktów
products = [
    "Mleko UHT 1 l","Czekolada 100 g","Jogurt 400 g","Chleb 500 g","Jajka 10 szt.",
    "Masło 200 g","Pomidory 500 g","Makaron 500 g","Serek wiejski 150 g","Płatki owsiane 500 g",
    "Ziemniaki 2 kg","Banany 1 kg","Ser żółty 200 g","Woda 1,5 l","Herbata 50 g",
    "Mąka 1 kg","Olej roślinny 1 l","Cukier 1 kg","Ryż 1 kg","Kawa 250 g",
    "Kiełbasa 250 g","Pierś z kurczaka 1 kg","Ketchup 500 g","Musztarda 250 g","Chipsy 150 g",
    "Ser feta 150 g","Jogurt naturalny 400 g","Płatki kukurydziane 500 g","Miód 250 g","Czekolada gorzka 100 g",
    "Wafle ryżowe 100 g","Pesto 190 g","Mleko roślinne 1 l","Pieczywo tostowe 500 g","Kefir 400 g",
    "Twaróg 250 g","Makaron świderki 500 g","Pomidory koktajlowe 250 g","Ogórki kiszone 900 g","Herbata zielona 50 g",
    "Mleko kokosowe 400 ml","Kefir 400 g","Sok pomarańczowy 1 l","Koncentrat pomidorowy 500 g","Kasza gryczana 500 g",
    "Makaron spaghetti 500 g","Cukinia 1 szt.","Papryka czerwona 1 szt.","Cebula 1 kg","Ziemniaki 2 kg",
    "Chleb pszenny 500 g","Ser mozzarella 125 g","Mleko UHT 3,2% 1 l","Jogurt grecki 400 g","Masło 200 g",
    "Ser gouda 200 g","Pomidory malinowe 500 g","Cukier trzcinowy 1 kg","Przyprawa gyros 50 g","Żel pod prysznic 250 ml"
]

shops = ["Biedronka","Lidl","Żabka","Aldi","Kaufland","Netto","Dino"]

# generujemy 50 promocji
promos = []
for p in products:
    price = round(random.uniform(1.50, 12.00), 2)
    discount = -random.randint(15, 50)
    promos.append({
        "shop": random.choice(shops),
        "product": p,
        "price": price,
        "discount": discount
    })

# zapis
with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)

print("Wygenerowano", len(promos), "promocji")
