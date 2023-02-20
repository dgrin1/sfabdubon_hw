import numpy as np
from numpy import loadtxt
#from pylab import inshow,show
import matplotlib.pyplot as plt
from matplotlib.pyplot import gray 


data = loadtxt("stm.txt",float)
plt.imshow(data, origin = "lower", aspect= 2.0)
gray()
plt.title("Density Plot")
plt.show()