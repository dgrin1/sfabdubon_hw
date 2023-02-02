import numpy as np

# values for the variables
G = 6.6738 * 10 ** -11
M = 1.9891 * 10 ** 30

#input of the user
l1 = float(input("Enter the distance to the sun at perihelion: "))
v1 = float(input("Enter the velocity at perihelion: "))

# solve for v2 we need to use the quadratic formula
a = 1
b = -2 * G * M / (v1 * l1)
c = v1 ** 2 - 2 * G * M * l1

v2 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)

#use given formulas to put find the other quantities
l2 = l1 * v1 / v2
T = (2 * np.pi * ((l1 + l2) / 2)*(np.sqrt(l1*l2))/(l1*v1))
e = (l2 - l1) / (l2 + l1)

print("The distance at aphelion is:", l2, "meters")
print("The velocity at aphelion is:", v2, "m/s")
print("The period of the orbit is:", T, "seconds")
print("The eccentricity of the orbit is:", e)
