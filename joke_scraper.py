import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = "https://www.countryliving.com/life/a27452412/best-dad-jokes/"
all_jokes = []


def scrape_jokes():
    res = requests.get(f"{base_url}")
    res.encoding = 'utf-8'
    print(f"Scraping {base_url} ->->->->->")
    soup = BeautifulSoup(res.text, "html.parser")
    jokes = soup.find_all(class_="body-ul")
    for joke in jokes:
        all_jokes.append({"jook": joke.find_all("li")})
    return all_jokes


def csv_jk_file_input(jokes):
    with open("jokes.csv", "w", encoding='utf-8', newline='') as file:
        headers = ["jook"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for joke in jokes:
            csv_writer.writerow(joke)


jokes_file = scrape_jokes()
csv_jk_file_input(jokes_file)
