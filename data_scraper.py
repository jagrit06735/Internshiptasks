import requests
from bs4 import BeautifulSoup
import csv

URL = "https://news.ycombinator.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])

    for title in titles:
        link = title.find("a")
        if link:
            writer.writerow([link.text])

print("Scraping completed! Data saved to headlines.csv")