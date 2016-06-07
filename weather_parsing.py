import requests
from bs4 import*
data = requests.get("http://www.accuweather.com/en/us/madrid/308526/weather-forecast/308526")
data
soup = BeautifulSoup(data.text, "html.parser")
soup.find("div")
data2 = soup.find("div", {'class': 'info'})
data3 = data2.find('strong', {'class': 'temp'})
data3.contents[0]


