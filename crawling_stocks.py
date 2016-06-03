import re
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
    #https://www.google.com/finance?q=
try:
	url = "https://www.google.com/finance?q="
	stock = raw_input("Enter your stock: ")
	#String concatenation
	url = url + stock 
	print(url)
	data = urlopen(url).read()
	print(data)
	m = re.search('meta itemprop="price"', data)
	print(m)
	start = m.start()
	end = start + 50
	newString = data[start:end]
	print(newString)
	m = re.search("content=", newString)
	start = m.end()
	newString1=newString[start:]
	print(newString1)
	m = re.search("/", newString1)
	start = 0
	end = m.end()-2
	final = newString1[0:end]
	print(final)
	end = m.end()-3
	final = newString1[1:end]
	print(final)
	print("The value of " + stock + " is " + final)
except:
	print("Sorry, your company haven't got stock or you entere an incorrect stock name")	
