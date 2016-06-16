import matplotlib.pyplot as plt

#create figure
fig = plt.figure()

#change font and other kinds
rect = fig.patch
rect.set_facecolor('green')

x=[3,7,5,8]
y=[5,13,2,8]
x2=[0,4,7,10]
y2=[3,7,1,12]
x3=[2,4,6,8]
y3=[13,5,8,2]

graph1 = fig.add_subplot(2,1,1, axisbg='black' )
graph1.plot(x,y,'yellow', linewidth= 2.0)

graph1.tick_params(axis="x", color="white")
graph1.tick_params(axis="y", color="white")

graph1.spines["top"].set_color('w')
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')
graph1.spines["bottom"].set_color('w')

graph1.set_title("Random Graph", color="blue")
graph1.set_xlabel("This is the x axis", color="white")
graph1.set_ylabel("This is the y axis", color="white")

graph2 = fig.add_subplot(2,1,2, axisbg='black' )
graph2.plot(x2,y2,'red', linewidth= 4.0)

graph2.tick_params(axis="x", color="white")
graph2.tick_params(axis="y", color="white")

graph2.spines["top"].set_color('w')
graph2.spines["left"].set_color('w')
graph2.spines["right"].set_color('w')
graph2.spines["bottom"].set_color('w')

graph2.set_xlabel("This is the x axis", color="white")
graph2.set_ylabel("This is the y axis", color="white")

graph3 = fig.add_subplot(2,2,2, axisbg='black' )
graph3.plot(x3,y3,'orange', linewidth= 1.0)

graph3.tick_params(axis="x", color="white")
graph3.tick_params(axis="y", color="white")

graph3.spines["top"].set_color('w')
graph3.spines["left"].set_color('w')
graph3.spines["right"].set_color('w')
graph3.spines["bottom"].set_color('w')

graph3.set_xlabel("This is the x axis", color="white")
graph3.set_ylabel("This is the y axis", color="white")


plt.show()

plt.show()