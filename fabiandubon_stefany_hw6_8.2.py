import numpy as np
import math
from numpy import array, arange
import matplotlib.pyplot as plt

#define constants
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

#initial values
x = 2
y = 2

#equations
def f(r, t):
    x = r[0]
    y = r[1]
    fx = (alpha * x) - (beta * x * y)
    fy = (gamma * x * y) - (delta * y)
    return array([fx, fy], float)

a = 0.0
b = 30.0
N = 1000
h = (b - a) / N

tpoints = arange(a, b, h)
xpoints = []
ypoints = []


r = array([2.0, 2.0], float)
for t in tpoints:   # uses the fourth-order Runge-Kutta
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

plt.plot(tpoints, xpoints, label="Rabbits")
plt.plot(tpoints, ypoints, label="Foxes")
# plt.ylim(2, 10)
plt.xlabel("Time")
plt.ylabel("Population (Thousands)")
plt.title("Lotka-Volterra Model")
plt.legend()
plt.show()