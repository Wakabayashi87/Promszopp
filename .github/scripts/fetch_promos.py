import requests
from bs4 import BeautifulSoup
import json

# Funkcja do pobierania gazetek z DużeRabaty.pl
def fetch_gazetki_duzerabaty():
    url = "https://duzerabaty.pl/gazetki/gazetka-biedronka"
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

# Funkcja do pobierania gazetek z Gazetkolandia.pl
def fetch_gazetki_gazetkolandia():
    url = "https://gazetkolandia.pl/lidl"
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

# Pobierz gazetki z obu źródeł
promos = fetch_gazetki_duzerabaty() + fetch_gazetki_gazetkolandia()

# Zapisz gazetki do pliku JSON
with open("promos.json", "w", encoding="utf-8") as f:
    json.dump(promos, f, ensure_ascii=False, indent=2)

print("Pobrano", len(promos), "gazetek")
