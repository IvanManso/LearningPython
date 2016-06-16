import requests
from bs4 import BeautifulSoup
data = requests.get("http://www.synonym.com/antonym/cold")
soup = BeautifulSoup(data.text, 'html.parser')
data2 = soup.find('spain', {"class": "equals"})
data2.string
data2.contents