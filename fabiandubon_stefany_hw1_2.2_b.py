import numpy as np

G= float(6.67*10**-11 )                     #
M= float(5.97*10**24)
R= 6371000
pi=np.pi

print(pi)
T = float(input("Enter T in seconds: "))



h= ((G*M*T**2)/(4*pi**2))**(1/3)-R

print("The height of the satellite is",h, "meters")