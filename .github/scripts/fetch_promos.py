import requests
from bs4 import BeautifulSoup
import json

# Funkcja do pobierania gazetek z Biedronki
def fetch_biedronka_gazetki():
    url = "https://www.biedronka.pl"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    gazetki = []
    for link in soup.find_all('a', href=True):
        if 'gazetka' in link['href']:
            gazetki.append({
                "shop": "Biedronka",
                "title": link.text.strip(),
                "gazetka": link['href']
            })
    return gazetki

# Funkcja do pobierania gazetek z Lidl
def fetch_lidl_gazetki():
    url = "https://www.lidl.pl"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    gazetki = []
    for link in soup.find_all('a', href=True):
        if 'gazetka' in link['href']:
            gazetki.append({
                "shop": "Lidl",
                "title": link.text.strip(),
                "gazetka": link['href']
            })
    return gazetki

# Pobierz gazetki z obu sklepów
promos = fetch_biedronka_gazetki() + fetch_lidl_gazetki()

# Zapisz gazetki do pliku JSON
with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)

print("Pobrano", len(promos), "gazetek")
