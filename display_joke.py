import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = "https://www.countryliving.com/life/a27452412/best-dad-jokes/"


def csv_scrape_reader(filename):
    with open(filename, "r", encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        print(list(csv_reader))


csv_scrape_reader("jokes.csv")
