import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://www.monitor.co.ug/uganda/magazines/people-power/museveni-s-famous-quotes-since-1980-1576292")
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
quotes = soup.select(".paragraph-wrapper p")

quote_list = [quote.getText() for quote in quotes]
index = 1
for quote in quote_list:
    with open("Museveni-Quotes.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{index}. {quote}\n\n")
    index += 1

