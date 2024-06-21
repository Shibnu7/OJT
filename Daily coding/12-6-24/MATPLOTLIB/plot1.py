import matplotlib.pyplot as plt

#dataset
x=[1,2,3,4,5,6,7]
y=[2,3,4,5,7,11,56]

#create a plot for our data

plt.plot(x,y)

#customaizaton for plot

#add a title

plt.title('line plot')

#add the labels
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#output the plot

plt.show()
