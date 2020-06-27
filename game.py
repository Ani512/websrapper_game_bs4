import requests
import csv
from bs4 import BeautifulSoup
from random import choice

base_url = "http://quotes.toscrape.com/"

def csv_scrape_reader(filename):
   with open(filename, "r", encoding='utf-8', newline='') as file:
      csv_reader = csv.DictReader(file)
      return list(csv_reader)

def start_game(list_):
   quote = choice(list_)
   remaining_guesses = 4
   print("Here is a quote: ")
   print(quote["text"])
   guess = ""
   while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
      guess = input(f"Try to guess the author of the quote! Remaining Guesses -> {remaining_guesses} :\n")
      if guess.lower() == quote["author"].lower():
         print(" You Got It RIGHT !!! ")
         break
      remaining_guesses -= 1
      if remaining_guesses == 3:
         res = requests.get(f"{base_url}{quote['bio-link']}")
         soup = BeautifulSoup(res.text, "html.parser")
         birth_date = soup.find(class_="author-born-date").get_text()
         birth_place = soup.find(class_="author-born-location").get_text()
         print(f"Don't Give Up! Here's a Hint: The Author was born on {birth_date} {birth_place}")
      elif remaining_guesses == 2:
         first_initial = quote["author"].split(" ")[0][0]
         print(f"Try Again Let's Go! Here's another Hint: The Author's first name starts with {first_initial}") 
      elif remaining_guesses == 1:
         last_initial = quote["author"].split(" ")[1][0]
         print(f"Last chance my Friend! Here's the last Hint: The Author's last name starts with {last_initial}")
      else:
         print(f"Sorry You ran out of Guesses. The Correct Answer is {quote['author']}")
   again = ""
   while again.lower() not in ("yes","no","y","n"):
      again = input("Would You Like to Play Again (y/n):")
      if again.lower() in ("yes", "y"):
         return start_game(quotes)
      elif again.lower() in ("no", "n"):
         print("Thank You for Playing ! ")
         print("Adios <--> GoodBye! <--> Shukran")
         break

quotes = csv_scrape_reader("qoutes.csv")
start_game(quotes)