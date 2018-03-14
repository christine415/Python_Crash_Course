import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new random walks, as long as the program is active
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize=(10,6))

    # Use colormap to show the path of the random walk
    point_numbers = list(range(rw.num_points))
    #plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        #edgecolor='none', s=1)
    plt.plot(rw.x_values, rw.y_values, linewidth = 1)
    
    # Emphasize the first and last point of the random walk
    plt.scatter(0,0, c = 'green', edgecolors='none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none', s = 100)
    
    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another random walk? y/n ")
    if keep_running == 'n':
        break