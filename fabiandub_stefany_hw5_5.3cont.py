import numpy as np
from scipy.integrate import fixed_quad
import matplotlib.pyplot as plt

#define the function to integrate
def f(t):
    return np.e**(-t**2)

#define the trapezoidal integration
def trapez_int(a, b, N):         #(from previous hw)
    h = (b-a)/N
    s = (f(a) + f(b))/2.0
    for i in range(1, N):
        s += f(a+i*h)
    return h*s

#define the E(x) function using trapezoidal integration
def E_trapezoidal(x):
    return trapez_int(0, x, 30)

#define the E(x) function using Gaussian quadrature
def E_gaussian(x):
    integrand = lambda t: np.exp(-t**2)
    return fixed_quad(integrand, 0, x, n=5)[0] * np.sqrt(np.pi)
# Calculate E(x) for values of x from 0 to 3 in steps of 0.1 using the trapezoidal rule
x_trapezoidal = np.arange(0, 3.1, 0.1)
E_trapezoidal_values = np.abs(np.array([E_trapezoidal(x) for x in x_trapezoidal]))

# Calculate E(x) for values of x from 0 to 3 in steps of 0.1 using Gaussian quadrature
x_gaussian = np.arange(0, 3.1, 0.1)
E_gaussian_values = np.abs(np.array([E_gaussian(x) for x in x_gaussian]))



# Plot the error curves
plt.plot(x_trapezoidal, E_trapezoidal_values, label='Trapezoidal Rule')
plt.plot(x_gaussian, E_gaussian_values, label='Gaussian Quadrature')
plt.xlabel('N')  #x label
plt.ylabel('Error')  #y label
plt.title('Comparison of Trapezoidal Rule and Gaussian Quadrature')  #title
plt.legend()
plt.show()


