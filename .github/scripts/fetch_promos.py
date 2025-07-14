import requests
from bs4 import BeautifulSoup
import json

promos = []

# Adres URL strony Blix.pl z promocjami
url = "https://blix.pl/gazetki-promocyjne"

# Pobierz zawartość strony
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Znajdź elementy z promocjami
# Przykład selektora: div z klasą "promotion-item"
promotions = soup.find_all('div', class_='promotion-item')

for promo in promotions:
    # Przykład selektorów dla produktu, ceny i rabatu
    product = promo.find('h3').text.strip()
    price = promo.find('span', class_='price').text.strip()
    discount = promo.find('span', class_='discount').text.strip()

    # Dodaj promocję do listy
    promos.append({
        "shop": "Blix",
        "product": product,
        "price": float(price.replace(',', '.').replace(' zł', '')),
        "discount": int(discount.replace('%', ''))
    })

# Zapisz promocje do pliku JSON
with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)
