import numpy as np

# values for the variables
G = 6.6738 * 10 ** -11
M = 1.9891 * 10 ** 30

#Earth
l1 = 1.4710 *10 ** 11
v1 = 3.0287 * 10 ** 4

# solve for v2 we need to use the quadratic formula
a = 1
b = -2 * G * M / (v1 * l1)
c = v1 ** 2 - 2 * G * M * l1

v2 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)

#use given formulas to put find the other quantities
l2 = l1 * v1 / v2
T = (2 * np.pi * ((l1 + l2) / 2)*(np.sqrt(l1*l2))/(l1*v1))
e = (l2 - l1) / (l2 + l1)
print(" Properties of the orbits of the Earth")
print("The distance at aphelion is:", l2, "meters")
print("The velocity at aphelion is:", v2, "m/s")
print("The period of the orbit is:", T, "seconds")
print("The eccentricity of the orbit is:", e)

#Halley's Comet
l1_H = 8.7830 *10 ** 10
v1_H = 5.4529 * 10 ** 4

# solve for v2 we need to use the quadratic formula
a = 1
b = -2 * G * M / (v1_H * l1_H)
c = v1_H ** 2 - 2 * G * M * l1_H

v2_H = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)

#use given formulas to put find the other quantities
l2_H = l1_H * v1_H / v2_H
T_H = (2 * np.pi * ((l1_H + l2_H) / 2)*(np.sqrt(l1_H*l2_H))/(l1_H*v1_H))
e_H = (l2_H - l1_H) / (l2_H + l1_H)

print(" Properties of the orbits of the Halley's Comet")
print("The distance at aphelion is:", l2_H, "meters")
print("The velocity at aphelion is:", v2_H, "m/s")
print("The period of the orbit is:", T_H, "seconds")
print("The eccentricity of the orbit is:", e_H)