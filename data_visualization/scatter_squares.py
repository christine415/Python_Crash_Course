import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s=40)

plt.title("Sqaure Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis = 'both', labelsize = 14)

# Set the range for each axis
# four parameters are minimum and maximum of x-axis and y-axis
plt.axis([0,1100,0,1100000])

#plt.show()

# The second parameter trims whitespace from the plot
plt.savefig('squre_plot.png', bbox_inches = 'tight')