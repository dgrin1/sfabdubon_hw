import numpy as np
import math 
import matplotlib.pyplot as plt

#define the function to integrate
def f(t):  
    return np.e**(-t**2)

#define the trapezoidal integration
def trapez_int(a, b, N):
    h = (b-a)/N            
    s = (f(a) + f(b))/2.0
    for i in range(1, N):     
        s += f(a+i*h)
    return h*s

#define the E(x) function  
def E(x):       
    return trapez_int(0, x, 30)

# Calculate E(x) for values of x from 0 to 3 in steps of 0.1
for x in range(0, 31):
    x = x/10.0
    print("E",x,"=", E(x))

#make the x and y values lists
x_val = [x/10.0 for x in range(0, 31)]
y_val = [E(x) for x in x_val]

# Plot E(x) as a function of x
plt.plot(x_val, y_val)
plt.xlabel('x')     #x label
plt.ylabel('E(x)')  #y label
plt.title('Graph of E(x) as a Function of x')  #title
plt.show()



