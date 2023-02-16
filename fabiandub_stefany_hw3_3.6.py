import numpy as np
import matplotlib.pyplot as plt


x=0
num_iter=1000

def logistic_map(r, x, num_iter):
  
    x_list = [x]
    for i in range(num_iter):
        x = r * x * (1 - x)
        x_list.append(x)
    return x_list


r_val = np.arange(1, 4, 0.01)  # initialize the range of values for r


for r in r_val:                # iterate over each value of r and plot the logistic map
    x_list = logistic_map(r, x, num_iter)
    plt.plot([r]*len(x_list), x_list, '.', color='black', markersize=1)


x= plt.xlim(1, 4)        # set the x and y limits of the plot
y =plt.ylim(0, 1)

plt.xlabel('r')       #labels
plt.ylabel('x')
plt.scatter(x,y)
plt.show()
