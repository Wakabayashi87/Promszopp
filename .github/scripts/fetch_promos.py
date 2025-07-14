import requests
from bs4 import BeautifulSoup
import json

promos = []

# Adres URL strony Żabka z gazetkami promocyjnymi
url = "https://www.zabka.pl/gazetka-promocyjna"

# Pobierz zawartość strony
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Znajdź elementy z gazetkami promocyjnymi
# Przykład selektora: div z klasą "promotion-item"
promotions = soup.find_all('div', class_='promotion-item')

for promo in promotions:
    # Przykład selektorów dla produktu, ceny i rabatu
    gazetka = promo.find('a')['href']
    title = promo.find('h3').text.strip()

    # Dodaj gazetkę do listy
    promos.append({
        "shop": "Żabka",
        "title": title,
        "gazetka": gazetka
    })

# Zapisz gazetki do pliku JSON
with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)

print("Pobrano", len(promos), "gazetek z Żabki")
