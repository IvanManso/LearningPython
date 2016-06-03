import re
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
    #https://www.google.com/finance?q=
try:
	url = "http://www.weather-forecast.com/locations/"
	url2 = "/forecasts/latest"
	city = raw_input("Enter your city: ")
	#String concatenation
	url = url + city + url2
	print(url)
	data = urlopen(url).read()
	print(data)
	m = re.search('<span class="phrase"', data)
	print(m)
	start = m.start()
	end = start + 100
	newString = data[start:end]
	print(newString)
	m = re.search(">", newString)
	start = m.end()
	newString1=newString[start:]
	print(newString1)
	m = re.search("Warm", newString1)
	end = m.end()-4
	final = newString1[0:end]
	print(final)
	print("The weather of " + city + " is: " + final)
except:
	print("Sorry, your city isn't correct or it isn't on weather-forecast domain")
