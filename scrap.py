import requests
from bs4 import BeautifulSoup

url = "https://olympics.com/fr/paris-2024/medailles"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")

all_countries = soup.find("div", {"data-test-id": "virtuoso-item-list"})

all_countries = all_countries.find_all("div", {"class": "emotion-srm-fvu3gb elhe7kv0"})

for c in enumerate(all_countries):
    drap = c[1].find("span", {"class": "elhe7kv4 emotion-srm-5xu01z"}).text
    if drap == "JPN":
        select = c[0]

select = all_countries[select]
pays = select.find("span", {"class": "elhe7kv5 emotion-srm-uu3d5n"}).text
liste = select.find_all("span")
gold = int(liste[3].text)
silver = int(liste[4].text)
bronze = int(liste[5].text)
total = int(liste[6].text)

print(
    f"pays : {pays}  :  or : {gold}, argent : {silver}, bronze : {bronze}, total : {total}"
)
