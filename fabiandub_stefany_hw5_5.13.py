import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import quad

def H(n, x):     #Following the information of the first 2 Hermite polynomials
    if n == 0:    # H0(x) = 1
        return 1
    elif n == 1:   #H1(x)= 2x
        return 2*x
    else:
        Hn_minus_2 = 1
        Hn_minus_1 = 2*x
        for i in range(2, n+1):
            Hn = 2*x*Hn_minus_1 - 2*(i-1)*Hn_minus_2
            Hn_minus_2 = Hn_minus_1
            Hn_minus_1 = Hn
        return Hn
    
x_1= np.linspace(-4, 4, 1000)  # Generate 1000 evenly spaced points in the range [-4, 4]

plt.figure(figsize=(8, 6))  # Set the size of the plot
plt.xlabel("x")  # Set the x-axis label
plt.ylabel("Hn(x)")  # Set the y-axis label
plt.title("Harmonic Oscillator Wavefunctions for n = 0, 1, 2, and 3 ")

# Plot the harmonic oscillator wavefunctions for n=0, 1, 2, and 3 on the same graph
for n in range(4):
    y = [H(n, xi) for xi in x_1]
    plt.plot(x_1, y, label=f"n = {n}")
    
plt.legend()  # Add a legend to the plot


x_2 = np.linspace(-10, 10, 1000) #Generates 1000 evenly spaced points in the range [-10, 10]
y_2 = [H(30, xi) for xi in x_2]  #Plot the wavefunction for n=30
plt.figure(figsize=(8,6))
plt.xlabel( "x")  # x label for the second graph
plt.ylabel("H30(x)")  # y label for the second graph
plt.plot(x_2, y_2)  # plot the second graph
plt.title("Harmonic Oscillator Wavefunction for n = 30 ")

plt.show()




def psi_n(x, n): # Returns the value of the wave function psi_n(x) for a given x and n.
    return 1/np.sqrt(2**n*np.math.factorial(n))*np.exp(-x**2/2)*H(n, x)

def integrand(t, n):  #Returns the integrand for the <x^2> integral. (helps turn the interval from infinite limits to finite limits)
    x = np.tan(t)
    return (np.tan(t))**2*psi_n(x, n)**2*np.power(1/np.cos(t),2)

def x_squared_integral(n): #Evaluates the integral of x^2|psi_n(x)|^2 from -infinity to infinity using Gaussian quadrature with 100 points.
    integral, _ = quad(integrand, 0, np.pi/2, args=(n,))
    return integral
def uncertainty(n): # Calculates the uncertainty (root-mean-square position) of a particle in the harmonic oscillator potential for a given n.
    x_squared = x_squared_integral(n)
    x_mean_squared = (x_squared_integral(n-1) if n>0 else 0)**2
    return np.sqrt(np.abs(x_squared - x_mean_squared))

# Calculate the uncertainty for n=5
n = 5
unc = uncertainty(n)
print(f"Uncertainty for n={n}: {unc}")
