import matplotlib
import matplotlib.pyplot as pt

x=[]
y=[]

readFile = open("Coordinates.txt", 'r')

data=readFile.read().split("\n")

for i in data:
	val = i.split(",")
	x.append(int(val[0]))
	y.append(int(val[1]))

pt.plot(x,y)
pt.show()

print(data)

print(x)
print(y)



# pt.plot([1,2,3,4],[3,8,10,25])
# pt.title("Rain in December")
# pt.xlabel("Day in December")
# pt.ylabel("Inches of Rain")
# pt.show()



