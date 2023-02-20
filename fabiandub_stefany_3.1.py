import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

#gets the file
data= loadtxt("sunspots.txt", float)

#chooses the columns and it displays only the first 1000 data points 
x = data[:1000,0]
y= data[:1000,1]

r=5
y_aveg = np.zeros_like(y)

for i in range (r, len(y)-r):
    y_aveg[i] = 1/(2*r+1)*np.sum(y[i-r:i+r+1])

# make the plot and put labels
plt.xlabel("Month")
plt.ylabel("Sunspots")
plt.plot (x,y, label = 'Sunspots')
#plt.plot(y, label='Sunspots')
plt.plot(y_aveg, label = 'Running Average')
plt.title("Sunspots as a Function of Time")
plt.legend()
plt.show()