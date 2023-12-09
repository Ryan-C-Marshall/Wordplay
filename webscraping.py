from bs4 import BeautifulSoup
import requests

url = "https://www.dcode.fr/words-starting-with"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")
print(soup)