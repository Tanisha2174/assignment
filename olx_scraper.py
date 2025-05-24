import requests
from bs4 import BeautifulSoup

url = "https://www.olx.in/items/q-car-cover"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to load OLX page")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

items = soup.select("li.EIR5N")  # OLX uses dynamic classes; may break

with open("car_covers.txt", "w", encoding="utf-8") as file:
    for item in items:
        title = item.select_one("span._2tW1I").text if item.select_one("span._2tW1I") else "No title"
        price = item.select_one("span.T6sTV").text if item.select_one("span.T6sTV") else "No price"
        file.write(f"{title} - {price}\n")

print("Saved to car_covers.txt")
