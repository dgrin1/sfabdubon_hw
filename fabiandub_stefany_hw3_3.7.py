import numpy as np
import matplotlib.pyplot as plt

N = 2000                                 # resolution of image
num_iter = 100                             # maximum number of iterations

x_vals = np.linspace(-2, 2, N)           # create a grid of complex numbers  # x values
y_vals = np.linspace(-2, 2, N)                                               #y values
grid = np.array([x + y*1j for x in x_vals for y in y_vals])

colors = []                              # initialize a list to store the color values of each pixel


for c in grid:                           #create and perfom the iterations using the given formula
    z = 0                                #initialize z and i
    i = 0
   
    while i < num_iter and abs(z) < 2:
        z = z**2 + c
        i += 1
    
                                        #this is where we assign the colors for grid points for the desnity plot 
    if abs(z) >= 2:                     # depending on whether they are inside of outside of the Mandelbort set
        colors.append(1) # white
    else:
        colors.append(0) # black

# reshape the list of colors to a 2D array
color_array = np.reshape(colors, (N, N))


plt.imshow(color_array, cmap='binary', extent=[-2, 2, -2, 2]) # plot the Mandelbrot set
plt.show()
