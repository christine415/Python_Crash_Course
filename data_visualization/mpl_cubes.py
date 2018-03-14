import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, edgecolor = 'none', s= 20)

plt.title("Cubic Values", fontsize = 24)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Cubic Values", fontsize = 14)

plt.axis([0,5100,0,125000000000])

plt.show()