import requests, json
from bs4 import BeautifulSoup

# strona główna Blix – agreguje wszystkie gazetki
url = "https://blix.pl/gazetki-promocyjne"

promos = []

try:
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, "html.parser")

    # każda promocja to <div class="card-offer">
    cards = soup.select(".card-offer")
    for card in cards:
        title   = card.select_one(".offer-title").get_text(strip=True)
        price   = card.select_one(".offer-price").get_text(strip=True).replace(" zł", "").replace(",", ".")
        discount = card.select_one(".offer-discount").get_text(strip=True).replace("-", "").replace("%", "")
        shop    = card.select_one(".offer-shop").get_text(strip=True)

        promos.append({
            "shop":    shop,
            "product": title,
            "price":   float(price),
            "discount": int(discount)
        })
except Exception as e:
    print("Scraping Blix: błąd", e)

with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)

print("Pobrano", len(promos), "promocji z Blix.pl")
