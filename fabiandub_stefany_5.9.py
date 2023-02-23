import numpy as np
import math
import matplotlib.pyplot as plt

# Define the function to integrate 
def f(x):
    if np.isclose(np.exp(x), 1).all():
        return 0
    else:
        return ((x**4)*((np.e)**x))/((((np.e)**x)-1)**2)
#Defnine the function to calculate Cv
def cv(T):
    # Constants
    p = 6.022*(10**28)   # Number density (m^-3)
    V = 0.001     # Volume from cm to m
    k_B = 1.3806*(10**-23)  # Boltzmann constant (J/K)
    theta_D = 428  # Debye temperature (K)
    N = 50        # Number of sample points
    
    # Integration limits
    a = 0              #given in the equation
    b = theta_D/T
    
    # Evaluate integral using trapezoidal rule
    h = (b-a)/50     
    s = 0.5*(f(a) + f(b))
    for i in range(1, N):
        x = a + i*h
        s += f(x)
    integral = h*s
    
    # Calculate Cv 
    Cv = 9 * p * V * k_B * (T/theta_D)**3 * integral #Solve the complete equation given
    return Cv


# Create lists of temperature and Cv values
T_values = [T for T in range(5, 501)]
Cv_values = [cv(T) for T in T_values]

# Plot Cv as a function of T
plt.plot(T_values, Cv_values)
plt.xlabel('Temperature (K)')  #x abel
plt.ylabel('Heat capacity (J/K)') #y label  
plt.title('Graph of Heat Capacity as a Function of Temperature') #title
plt.show()
