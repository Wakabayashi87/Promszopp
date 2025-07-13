import requests
from bs4 import BeautifulSoup
import json

promos = []

# Wybierz odpowiedni URL z powyższych źródeł
url = "https://www.zabka.pl/gazetka-promocyjna/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Znajdź elementy z promocjami - tutaj trzeba dostosować selektory do struktury strony
promotions = soup.find_all('div', class_='promotion-item')  # Przykład selektora
for promo in promotions:
    product = promo.find('h3').text.strip()  # Przykład selektora
    price = promo.find('span', class_='price').text.strip()  # Przykład selektora
    discount = promo.find('span', class_='discount').text.strip()  # Przykład selektora
    promos.append({
        "shop": "Żabka",
        "product": product,
        "price": float(price.replace(',', '.').replace(' zł', '')),
        "discount": int(discount.replace('%', ''))
    })

# Zapisz do pliku
with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)
