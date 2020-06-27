import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = "http://quotes.toscrape.com/"
all_quotes = []


def scrape_quotes():
    url = "/page/1/"
    while url:
        res = requests.get(f"{base_url}{url}")
        res.encoding = 'utf-8'
        sleep(2)
        print(f"Scraping {base_url}{url} ->->->->->")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        if next_btn:
            url = next_btn.find("a")["href"]
        else:
            url = None
    return all_quotes


def csv_file_input(quotes):
    with open("qoutes.csv", "w", encoding='utf-8', newline='') as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

# sleep(2) # REMOVE THIS COMMENT WHILE IMPLEMENTING


quotes_file = scrape_quotes()
csv_file_input(quotes_file)

# Web scraping is done when websites dont have API's to return their data to you
# Many sites are not OK with web scraping. The fact is that it is allowed by the law.
# This Website uses a website that aloows webscraping as indicated by it's Robot.txt file
